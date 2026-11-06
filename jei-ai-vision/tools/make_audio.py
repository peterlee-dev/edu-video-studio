"""Narration, timeline and mix for a graph-paper workbook video. The script is tools/script.py.

  dry       no voice yet: each line's length is estimated from its text (CPS chars/s) → timeline.js only, for laying out pages first
  tts       every line is read by Qwen3-TTS cloning audio/voice_ref.wav (+ its words, audio/voice_ref.txt) on the DGX TTS API
            (TTS_URL, POST /v1/tts/clone), 3 takes each. whisper large-v3-turbo (mlx-whisper) transcribes every take; takes that do
            not read the script word for word are dropped, and of the rest the one nearest the median pace without long pauses wins.
            Takes and transcripts are cached in audio/tts_cache/, so changing a line re-reads only that line.
            --redo l3_2,l6_4 throws those lines' takes away and reads them again (N=8 reads 8 takes for them)
  take      one recorded reading of the whole script (audio/narration.mp3 | .wav | .m4a): transcribed once (audio/narration_words.json),
            the script aligned to the transcript, every line cut in the silences around its own words. Lines in CLONE (reworded after
            the recording) are read like tts mode by a clone of the recorded voice, then brought to the recording's pace, EQ and loudness
  ref A B   cut audio/voice_ref.wav and voice_ref.txt from the recording, A–B seconds (a clean 15–30 s stretch of whole sentences)

Writes timeline.js (scenes, and every line with its spoken words and their times: index.html keys pictures to them),
audio/mix.wav (narration + a whoosh at each page turn + a chime at CHIME_AT and before DING_BEFORE / after the last line when DING_END, no music)
and subtitles.srt (never burned in).

  uv run --with numpy python tools/make_audio.py dry
  uv run --with numpy --with mlx-whisper python tools/make_audio.py tts
  uv run --with numpy --with mlx-whisper python tools/make_audio.py take
"""
import os, sys, json, re, glob, hashlib, subprocess, difflib, urllib.request, uuid, wave
import numpy as np
sys.dont_write_bytecode = True   # no __pycache__ next to script.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from script import LANGUAGE, SCENES, CONT, SCRIPT, CLONE, LEAD, GAP, SCENE_GAP, TAIL, DING_BEFORE, JOIN
import script
TEMPO, CHIME_AT = getattr(script, 'TEMPO', 1.), getattr(script, 'CHIME_AT', None)
TAKE = getattr(script, 'TAKE', {})   # {line id: take index (sorted order of its takes)}: overrides the automatic pick
SAY = getattr(script, 'SAY', [])     # [(written, read)]: names said the Korean way
def say_as(s):
    for a, b in SAY: s = re.sub(re.escape(a), b, s, flags=re.I)
    return s
DING_END = getattr(script, 'DING_END', False)

SR = 48000
TURN = 1.2                  # a page starts this long before its first line (its turn, index.html TR = 1.1 s, starts .15 s before that)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
AUD = os.path.join(ROOT, 'audio')
CACHE = os.path.join(AUD, 'tts_cache')
VOICE = os.environ.get('VOICE', getattr(script, 'VOICE', 'voice_ref'))   # the reference voice: audio/<VOICE>.wav + .txt (script.py VOICE, or VOICE=… to try another)
REF, REF_TXT = os.path.join(AUD, VOICE + '.wav'), os.path.join(AUD, VOICE + '.txt')
WORDS = os.path.join(AUD, 'narration_words.json')
TTS = os.environ.get('TTS_URL', 'http://192.168.51.8:8095')
N_TAKES = int(os.environ.get('N', 3))
CPS = 14.5                  # dry mode: characters per second of a calm read
SILENT_DB, TRIM_DB = -45, -55   # take mode: 10 ms frames below SILENT_DB are a pause; a line keeps its frames above TRIM_DB
PRE, POST = .08, .15        # take mode: air kept before / after a line's voiced frames
LANG = {'English': 'en', 'Korean': 'ko'}[LANGUAGE]
FFMPEG = os.environ.get('FFMPEG') or next((p for p in [os.path.join(ROOT, 'node_modules/ffmpeg-static/ffmpeg')] if os.path.exists(p)), 'ffmpeg')
IDS = [lid for lid, *_ in SCRIPT]
LINE = {lid: (sc, sub, read or sub, extra) for lid, sc, sub, read, extra in SCRIPT}


def h(*a): return hashlib.sha1('|'.join(a).encode()).hexdigest()[:12]


def decode(path, sr=SR):
    out = subprocess.run([FFMPEG, '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(out, np.float32).astype(np.float64)


def write_wav(path, y, stereo=False):
    y = np.repeat(y, 2) if stereo else y
    with wave.open(path, 'wb') as w:
        w.setnchannels(2 if stereo else 1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y, -1, 1) * 32767).astype('<i2').tobytes())


def transcribe(path, cache=None):
    """{'text', 'words': [{'w', 's', 'e'}]}, cached as json next to the audio (or at cache)"""
    j = cache or os.path.splitext(path)[0] + '.json'
    if os.path.exists(j): return json.load(open(j, encoding='utf-8'))
    import mlx_whisper   # audio is decoded here, so whisper needs no ffmpeg on PATH
    r = mlx_whisper.transcribe(decode(path, 16000).astype(np.float32), path_or_hf_repo='mlx-community/whisper-large-v3-turbo', language=LANG, word_timestamps=True)
    out = {'text': r['text'].strip(), 'words': [{'w': w['word'], 's': round(w['start'], 3), 'e': round(w['end'], 3)} for s in r['segments'] for w in s.get('words', [])]}
    json.dump(out, open(j, 'w', encoding='utf-8'), ensure_ascii=False); return out


# ---------------------------------------------------------------- words: script vs. what was read
ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
def say(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10 - 2] + ('' if n % 10 == 0 else ONES[n % 10])
    if 2000 <= n < 2100: return 'twenty' + say(n - 2000) if n > 2009 else 'twothousand' + ('' if n == 2000 else say(n - 2000))
    if n < 1000: return ONES[n // 100] + 'hundred' + ('' if n % 100 == 0 else say(n % 100))
    return str(n)
def toks(text):
    """lower-case tokens without punctuation; numbers spelled out (English); hyphenated letters joined (P-O-D → pod)"""
    out = []
    for w in re.split(r'[\s—–]+', text.lower()):
        if re.fullmatch(r"([a-z]-)+[a-z][.,]?", w): w = w.replace('-', '')
        for p in w.split('-'):
            p = re.sub(r'[^\w]|_', '', p.replace("'", '').replace('%', ' percent'))
            if not p: continue
            out.append(say(int(p)) if p.isdigit() and LANG == 'en' else p)
    return out
def flat(text): return ''.join(toks(text))   # blind to spacing, hyphens and how numbers are written


def spoken(words, off=0., tempo=1.):
    """whisper words → [[word, time]]; pieces without a leading space ("two" "-digit") join the word before"""
    out = []
    for w in words:
        if out and not w['w'].startswith(' '): out[-1][0] += w['w'].strip()
        else: out.append([w['w'].strip(), (w['s'] - off) / tempo])
    return [[re.sub(r"[^\w'%-]", '', w).lower(), round(s, 3)] for w, s in out]


# ---------------------------------------------------------------- levels and trimming
def frames_db(x, hop=SR // 100):
    n = len(x) // hop
    return 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)


def trim(x, db, c0=0., c1=None, pre=.06, post=.18, floor=-50):
    """(start s, samples) of x[c0:c1] cut to its voiced frames plus a little air, with short fades"""
    c1 = len(x) / SR if c1 is None else c1
    f0, f1 = int(c0 * 100), int(c1 * 100)
    v = np.where(db[f0:f1] > floor)[0]
    a, b = max(c0, (f0 + v[0]) / 100 - pre), min(c1, (f0 + v[-1] + 1) / 100 + post)
    y = x[int(a * SR):int(b * SR)].copy(); fi, fo = int(.01 * SR), int(.04 * SR)
    y[:fi] *= np.linspace(0, 1, fi); y[-fo:] *= np.linspace(1, 0, fo)
    return a, y


def speech_rms(y):
    e = 10 ** (frames_db(y) / 20)
    return np.sqrt(np.mean(e[e > np.percentile(e, 50)] ** 2))


def longest_pause(db):
    v = np.where(db > -45)[0]; best = run = 0
    for q in (db[v[0]:v[-1]] < -45):
        run = run + 1 if q else 0; best = max(best, run)
    return best * .01


def atempo(y, tempo):
    p = subprocess.run([FFMPEG, '-v', 'error', '-f', 'f64le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af', f'atempo={tempo:.4f}', '-f', 'f64le', '-'], input=y.tobytes(), capture_output=True, check=True)
    return np.frombuffer(p.stdout, np.float64).copy()


def ltas(y, n=4096):
    """average power spectrum of the louder 60 % of frames"""
    fr = np.lib.stride_tricks.sliding_window_view(y, n)[::n // 2] * np.hanning(n)
    e = (fr ** 2).mean(1)
    return (np.abs(np.fft.rfft(fr[e > np.percentile(e, 40)], axis=1)) ** 2).mean(0)


def match_eq(y, ref, n=4096, maxdb=12, passes=3):
    """zero-phase EQ bringing y's average spectrum to ref's in 1/3-octave bands (60 Hz–11 kHz), ±maxdb, 0 dB at 1 kHz.
    The cloned voice comes out duller than a recording (24 kHz output, -5…-15 dB at 5–11 kHz); this puts the air back"""
    f = np.fft.rfftfreq(n, 1 / SR)
    cen = 60 * 2 ** (np.arange(0, np.log2(11000 / 60), 1 / 3))
    bands = [(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6)) for c in cen]
    Pr = ltas(ref, n)
    Y0 = np.fft.rfft(y, 2 * len(y)); F = np.fft.rfftfreq(2 * len(y), 1 / SR)
    g, out = np.zeros(len(cen)), y
    for _ in range(passes):
        Py = ltas(out, n)
        d = np.array([10 * np.log10(Pr[b].sum() / Py[b].sum()) for b in bands])
        g = np.clip(g + d - np.interp(1000, cen, d), -maxdb, maxdb)
        out = np.fft.irfft(Y0 * 10 ** (np.interp(np.log2(np.maximum(F, 1)), np.log2(cen), g) / 20))[:len(y)]
    return out


# ---------------------------------------------------------------- the cloned voice (tts mode, and CLONE lines in take mode)
def post(path, fields, files):
    b = uuid.uuid4().hex; body = b''
    for k, v in fields.items(): body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    for k, (name, data) in files.items(): body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + data + b'\r\n'
    body += f'--{b}--\r\n'.encode()
    req = urllib.request.Request(TTS + path, data=body, headers={'Content-Type': f'multipart/form-data; boundary={b}'}, method='POST')
    with urllib.request.urlopen(req, timeout=300) as r: return r.read()


def ref_id(): return h(open(REF, 'rb').read().hex()[:40000], open(REF_TXT, encoding='utf-8').read().strip())
def take_key(lid): return h(ref_id(), LINE[lid][2], TAIL_TEXT)
def takes_of(lid): return sorted(glob.glob(os.path.join(CACHE, f'{lid}_{take_key(lid)}_*.wav')))

# The TTS server stops the moment the speech stops, so a line's last syllable loses its natural fall and sounds cut off (worst with
# voices whose sentences end hard, like ad narration). So every line is read with a short sentence after it, and the take is cut in the
# pause between the two: the line then ends the way a sentence inside speech does, with its fall and a little air.
TAIL_TEXT = os.environ.get('TAIL_TEXT', '감사합니다.' if LANGUAGE == 'Korean' else 'Thank you.')
def cut_tail(data):
    """the take without the extra sentence, cut in the last pause (>= 80 ms below SILENT_DB) before it; None when there is no such pause"""
    tmp = os.path.join(CACHE, '_tail.wav'); open(tmp, 'wb').write(data); x = decode(tmp); os.remove(tmp)
    db = frames_db(x); v = np.where(db > SILENT_DB)[0]
    if not len(v): return None
    end, runs, i = v[-1], [], 0
    while i <= end:
        if db[i] <= SILENT_DB:
            j = i
            while j <= end and db[j] <= SILENT_DB: j += 1
            if j - i >= 8: runs.append((i, j))
            i = j
        else: i += 1
    for a, b in reversed(runs):
        rest = (end + 1 - b) / 100   # the extra sentence: about 0.4–1.5 s
        if rest > 1.6: return None
        if rest >= .35:
            y = x[:(a + max(0, min(b - a - 3, 20))) * (SR // 100)]   # keep up to 200 ms of the pause after the line (not the 30 ms before the extra sentence)
            return np.concatenate([y, np.zeros(int(.1 * SR))])
    return None


def make_takes(ids, redo):
    if not (os.path.exists(REF) and os.path.exists(REF_TXT)): sys.exit('needs audio/voice_ref.wav and audio/voice_ref.txt (take mode: make_audio.py ref A B)')
    os.makedirs(CACHE, exist_ok=True)
    ref, ref_text = open(REF, 'rb').read(), open(REF_TXT, encoding='utf-8').read().strip()
    for lid in ids:
        read = LINE[lid][2]
        if lid in redo:
            for f in takes_of(lid): os.remove(f); os.path.exists(f[:-4] + '.json') and os.remove(f[:-4] + '.json')
        for k in range(len(takes_of(lid)), N_TAKES if lid in redo else 3):
            print(f'TTS {lid} #{k}', read[:60], flush=True)
            for attempt in range(3):   # a take whose extra sentence cannot be cut off is read again (kept as it is after 3 tries: it then fails the word check)
                data = post('/v1/tts/clone', {'text': f'{read} {TAIL_TEXT}', 'ref_text': ref_text, 'language': LANGUAGE, 'format': 'wav'}, {'ref_audio': ('ref.wav', ref)})
                y = cut_tail(data)
                if y is not None: break
                print(f'  {lid} #{k}: no pause before the extra sentence, reading again', flush=True)
            out = os.path.join(CACHE, f'{lid}_{take_key(lid)}_{k}.wav')
            if y is None: open(out, 'wb').write(data)
            else: write_wav(out, y)


def pick_takes(ids, rate=None):
    """best take per line: reads the script word for word, nearest the target pace (default: the median), no long pause inside"""
    cands = {}
    for lid in ids:
        want, cs = flat(LINE[lid][1]), []
        for k, p in enumerate(takes_of(lid)):
            tr = transcribe(p); x = decode(p); db = frames_db(x); off, y = trim(x, db)
            got = flat(say_as(tr['text']))
            # whisper may write what was read either way ("Knowledge Map" / "날리지 맵", "7개" / "일곱 개"): the nearer of the written and the read form counts.
            # Names whisper writes in letters ("JEI", "POD") are turned into their read form first (script.py SAY), so a line mixing both still matches
            miss = min(0 if got == w else sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, w, got, autojunk=False).get_opcodes() if op != 'equal')
                       for w in {want, flat(LINE[lid][2]), flat(say_as(LINE[lid][1]))})
            # a take that still stops mid-sound (its last 30 ms loud) sounds clipped: such takes lose
            cut = 10 * np.log10(np.mean(x[-int(.03 * SR):] ** 2) + 1e-12) > 10 * np.log10(np.mean(x ** 2) + 1e-12) - 20
            # and one that ends its last word on its own leaves air after it: under 0.2 s of silence at the end means the voice was stopped
            v = np.where(db > -45)[0]; tail = (len(db) - 1 - v[-1]) / 100 if len(v) else 0
            cut = cut or tail < .2
            cs.append({'k': k, 'tr': tr, 'y': y, 'off': off, 'miss': miss, 'rate': len(want) / (len(y) / SR), 'pause': longest_pause(db), 'cut': cut, 'tail': tail})
        cands[lid] = cs
    med = rate or float(np.median([c['rate'] for cs in cands.values() for c in cs if c['miss'] == 0] or [1]))
    pick = {}
    for lid, cs in cands.items():
        for c in cs: c['score'] = c['miss'] * 10 + abs(c['rate'] - med) / med + max(0, c['pause'] - .7) * 4 + c['cut'] * 5
        pick[lid] = c = cs[TAKE[lid]] if lid in TAKE else min(cs, key=lambda c: c['score'])   # TAKE: a take chosen by ear / phoneme check
        print(f"  {lid:6s} take {c['k']}  {len(c['y']) / SR:5.2f}s  miss {c['miss']}  pause {c['pause']:.2f}s  tail {c['tail']:.2f}s  [{' '.join(str(x['miss']) + ('c' if x['cut'] else '') for x in cs)}]" + ('  (TAKE)' if lid in TAKE else ''))
        if c['cut'] and not c['miss']: print(f"  ! {lid}: every take ends mid-sound (clipped last syllable) → N=8 ... --redo {lid}")
        if c['miss']: print(f"  ! {lid}: no take reads the script word for word (best differs by {c['miss']} chars: {c['tr']['text']}) → N=8 ... --redo {lid}, or write a read form in script.py")
    print(f'pace {med:.2f} chars/s')
    return pick, med


# ---------------------------------------------------------------- the three ways to get each line's clip: {lid: {'y', 'dur', 'words'}}
def clips_dry():
    out = {}
    for lid in IDS:
        read = LINE[lid][2]; d = len(read) / CPS + .2; at, words = 0, []
        for w in read.split():
            words.append([re.sub(r"[^\w'%-]", '', w).lower(), round(at / len(read) * d, 3)]); at += len(w) + 1
        out[lid] = {'y': None, 'dur': d, 'words': words}
    return out


def clips_tts(redo):
    make_takes(IDS, redo)
    pick, _ = pick_takes(IDS)
    out = {}
    for lid, c in pick.items():
        db = frames_db(c['y']); y = c['y'] * (.08 / np.sqrt(np.mean(10 ** (db[db > -40] / 10))))   # same loudness for every line
        if TEMPO != 1: y = atempo(y, TEMPO)
        y = y.copy(); y[-int(.02 * SR):] *= np.linspace(1, 0, int(.02 * SR))   # no click where a take stops
        out[lid] = {'y': y, 'dur': len(y) / SR, 'words': spoken(c['tr']['words'], c['off'], TEMPO)}
    return out


def recording():
    f = next((os.path.join(AUD, f'narration.{e}') for e in ('mp3', 'wav', 'm4a') if os.path.exists(os.path.join(AUD, f'narration.{e}'))), None)
    return f or sys.exit('take mode needs audio/narration.mp3 (or .wav / .m4a): one reading of the whole script')


def silence_mid(db, a, b):
    """middle of the longest pause near a (end of one word) … b (start of the next), in s; halfway if there is none"""
    f0, f1 = int((min(a, b) - .4) * 100), int((max(a, b) + .4) * 100)
    best, run, k0 = (0, 0), 0, 0
    for k, q in enumerate(db[max(0, f0):f1] < SILENT_DB):
        if q:
            k0 = k if run == 0 else k0; run += 1
            if run > best[0]: best = (run, k0)
        else: run = 0
    return (max(0, f0) + best[1] + best[0] / 2) / 100 if best[0] >= 3 else (a + b) / 2


def clips_take(redo):
    rec = recording(); x = decode(rec); db = frames_db(x); words = transcribe(rec, WORDS)['words']
    wt, wi = [], []
    for i, w in enumerate(words):
        for tok in toks(w['w']): wt.append(tok); wi.append(i)
    ids = [lid for lid in IDS if lid not in CLONE]
    st, own = [], []
    for lid in ids:
        for tok in toks(LINE[lid][1]): st.append(tok); own.append(lid)
    span, hit = {}, {lid: 0 for lid in ids}
    for a, b, n in difflib.SequenceMatcher(None, st, wt, autojunk=False).get_matching_blocks():
        for k in range(n):
            lid, j = own[a + k], wi[b + k]; hit[lid] += 1
            span[lid] = [min(span.get(lid, [j])[0], j), max(span.get(lid, [j, j])[1], j)]
    print(f'aligned {sum(hit.values())}/{len(st)} script tokens to {len(wt)} transcript tokens')
    for lid in ids:
        n = own.count(lid)
        if hit[lid] < n: print(f'  {lid}: {hit[lid]}/{n} words found in the recording' + ('  ← reads differently: put it back as recorded, or add it to CLONE' if hit[lid] < .7 * n else ''))
        if lid not in span: sys.exit(f'{lid} is not in the recording')
    out, recorded = {}, []
    for lid in ids:
        i0, i1 = span[lid]
        c0 = silence_mid(db, words[i0 - 1]['e'] if i0 else 0, words[i0]['s'])
        c1 = silence_mid(db, words[i1]['e'], words[i1 + 1]['s'] if i1 + 1 < len(words) else len(x) / SR)
        a, y = trim(x, db, c0, c1, PRE, POST, TRIM_DB)
        out[lid] = {'y': y, 'dur': len(y) / SR, 'words': spoken(words[i0:i1 + 1], a)}; recorded.append(lid)
        print(f'  {lid}: {a:7.2f}–{a + len(y) / SR:7.2f}s of the recording')
    if CLONE:
        rate = float(np.median([len(flat(LINE[lid][1])) / out[lid]['dur'] for lid in recorded]))
        level = float(np.median([speech_rms(out[lid]['y']) for lid in recorded]))
        make_takes([lid for lid in IDS if lid in CLONE], redo)
        pick, _ = pick_takes([lid for lid in IDS if lid in CLONE], rate)
        for lid, c in pick.items():
            tempo = float(np.clip(c['rate'] and rate / c['rate'], .9, 1.15)); y = c['y']
            if abs(tempo - 1) > .03: y = atempo(y, tempo)
            else: tempo = 1.
            y = match_eq(y, x); y *= level / speech_rms(y)
            out[lid] = {'y': y, 'dur': len(y) / SR, 'words': spoken(c['tr']['words'], c['off'], tempo)}
            print(f'  {lid}: cloned reading {len(y) / SR:.2f}s (tempo {tempo:.3f})')
    return out


# ---------------------------------------------------------------- lay the lines out → timeline.js, subtitles.srt
def lay_out(clips):
    known = {s for s, _ in SCENES}
    for lid, (sc, *_) in LINE.items():
        if sc not in known: sys.exit(f'{lid}: scene "{sc}" is not in SCENES')
    t, prev, lines, scene_t, voice = LEAD, None, {}, {}, []
    for lid in IDS:
        sc, sub, _, extra = LINE[lid]; c = clips[lid]
        if lid in JOIN: t = t_end + JOIN[lid]   # the sentence goes on: its scene starts in the short pause (a CONT scene, no page turn)
        elif prev and sc != prev: t += SCENE_GAP
        if sc not in scene_t: scene_t[sc] = 0 if not prev else t - JOIN[lid] / 2 if lid in JOIN else t - TURN   # the page turn (index.html TR) lands just before its first line
        lines[lid] = {'scene': sc, 'text': sub, 'start': round(t, 3), 'end': round(t + c['dur'], 3), 'words': [[w, round(t + s, 3)] for w, s in c['words']]}
        if c['y'] is not None: voice.append((t, c['y']))
        t_end = t + c['dur']; t += c['dur'] + GAP + extra; prev = sc
    dur = round(t - GAP + TAIL, 2)
    ids = [s for s, _ in SCENES]
    for s in ids:
        if s not in scene_t: sys.exit(f'scene "{s}" has no lines')
    scenes = [{'id': s, 'label': lab, 'start': round(scene_t[s], 3), 'end': round(scene_t[ids[i + 1]] if i + 1 < len(ids) else dur, 3)} for i, (s, lab) in enumerate(SCENES)]
    TL = {'duration': dur, 'scenes': scenes, 'cont': sorted(CONT), 'order': IDS, 'lines': lines}
    with open(os.path.join(ROOT, 'timeline.js'), 'w', encoding='utf-8') as f:
        f.write('// written by tools/make_audio.py (lines[id].words = spoken words and their start times). Do not edit by hand — rerun make_audio.py\n')
        f.write('window.TL = ' + json.dumps(TL, ensure_ascii=False) + ';\n')
    srt(lines)
    return scenes, lines, voice, dur


def srt(lines, maxc=84):
    ts = lambda s: f'{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(round(s % 1 * 1000)) % 1000:03d}'
    cues = []
    for lid in IDS:
        L = lines[lid]; text, chunks, cur = L['text'], [], ''
        n = -(-len(text) // maxc); size = len(text) / n   # n even chunks of about maxc characters or less, two lines each
        for w in text.split():
            cur = f'{cur} {w}'.strip()
            if len(cur) >= size - 4 and len(chunks) < n - 1: chunks.append(cur); cur = ''
        if cur: chunks.append(cur)
        at = 0
        for c in chunks:
            s, e = L['start'] + (L['end'] - L['start']) * at / len(text), L['start'] + (L['end'] - L['start']) * min(1, (at + len(c)) / len(text)); at += len(c) + 1
            sp = [i for i, ch in enumerate(c) if ch == ' ']; cut = min(sp, key=lambda i: abs(i - len(c) / 2)) if len(c) > maxc // 2 and sp else -1
            cues.append((s, e, c if cut < 0 else c[:cut] + '\n' + c[cut + 1:]))
    open(os.path.join(ROOT, 'subtitles.srt'), 'w', encoding='utf-8').write(''.join(f'{i + 1}\n{ts(s)} --> {ts(e)}\n{c}\n\n' for i, (s, e, c) in enumerate(cues)))


# ---------------------------------------------------------------- sounds and mix
def t_(d): return np.arange(int(d * SR)) / SR
def lp(x, a):
    y = np.empty_like(x); s = 0.
    for i, v in enumerate(x): s += a * (v - s); y[i] = s
    return y
def whoosh():
    x = lp(np.random.default_rng(3).standard_normal(int(.75 * SR)), .06); e = np.sin(np.pi * np.linspace(0, 1, len(x)) ** .8) ** 2; return x * e * 1.4
def chime():
    """a bright rising C–E–G–C bell arpeggio (the single high ding sounded like a wrong-answer buzzer, review 1)"""
    out = np.zeros(int(1.6 * SR))
    for i, f in enumerate((1046.5, 1318.5, 1568.0, 2093.0)):
        tt = t_(1.6 - i * .09); y = (np.sin(2 * np.pi * f * tt) + .25 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt * 6)) * np.exp(-tt * (3.2 if i == 3 else 5.5))
        y[:int(.004 * SR)] *= np.linspace(0, 1, int(.004 * SR)); place(out, i * .09, y * (.22 if i < 3 else .3))
    return out
def place(buf, t, x, g=1.):
    i = int(t * SR); n = min(len(x), len(buf) - i)
    if n > 0 and i >= 0: buf[i:i + n] += x[:n] * g


def mix(scenes, lines, voice, dur):
    n = int(dur * SR); nar, fx = np.zeros(n), np.zeros(n)
    for s0, y in voice: place(nar, s0, y)
    nar *= .9 / (np.abs(nar).max() + 1e-9)
    for s in scenes[1:]:   # the page slides sideways at the same time (index.html draw); CONT pages do not turn
        if s['id'] not in CONT: place(fx, s['start'] - .15, whoosh(), .3)
    if CHIME_AT is not None: place(fx, CHIME_AT, chime(), .4)
    if DING_BEFORE: place(fx, lines[DING_BEFORE]['start'] - .55, chime(), .4)
    if DING_END: place(fx, lines[IDS[-1]]['end'] + .45, chime(), .4)
    m = np.tanh((nar + fx) * 1.1) / 1.1
    write_wav(os.path.join(AUD, 'mix.wav'), m / (np.abs(m).max() + 1e-9) * .89, stereo=True)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    redo = set(sys.argv[sys.argv.index('--redo') + 1].split(',')) if '--redo' in sys.argv else set()
    os.makedirs(AUD, exist_ok=True)
    if mode == 'ref':
        a, b = float(sys.argv[2]), float(sys.argv[3]); rec = recording(); x = decode(rec)
        write_wav(REF, x[int(a * SR):int(b * SR)])
        said = ''.join(w['w'] for w in transcribe(rec, WORDS)['words'] if w['s'] >= a - .05 and w['e'] <= b + .05).strip()
        open(REF_TXT, 'w', encoding='utf-8').write(said + '\n'); print(f'audio/voice_ref.wav ({b - a:.1f}s): {said}'); return
    if mode not in ('dry', 'tts', 'take'): sys.exit(__doc__)
    clips = {'dry': clips_dry, 'tts': lambda: clips_tts(redo), 'take': lambda: clips_take(redo)}[mode]()
    scenes, lines, voice, dur = lay_out(clips)
    if mode == 'dry':
        print(f'done: {dur:.1f}s, {len(IDS)} lines (estimated, no audio) → timeline.js, subtitles.srt')
        if os.path.exists(os.path.join(AUD, 'mix.wav')): print('  audio/mix.wav is from an earlier narration and no longer matches; run tts or take before rendering')
        return
    mix(scenes, lines, voice, dur)
    print(f'done: {dur:.1f}s, {len(IDS)} lines → timeline.js, audio/mix.wav, subtitles.srt')


if __name__ == '__main__':
    main()
