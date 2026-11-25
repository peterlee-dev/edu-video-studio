"""Checks for a TTS narration that whisper's word check (make_audio.py) lets through. See the skill's reference/voice-qa.md.

  pitch            every line of audio/mix.wav (times from timeline.js): median F0, its 2 s windows, and how the line ends.
                   Flags a line read in a lower / higher tone than the rest (reviewers: "갑자기 톤이 낮아짐"), a drop partway
                   through a line, and a last word that rises like a question
  takes l3_2 [..]  every cached take of those lines (audio/tts_cache, the current voice and read form): length, air after the last
                   word, median F0, 2 s windows, end slope, and which take make_audio would pick. Pin a good one with TAKE in script.py
                   (the number printed is its position, the same index TAKE uses)
  phonemes l3_2 [A B]   the takes of a line decoded to IPA phonemes by wav2vec2 (whisper writes what it expects; this writes what was
                   said). A B = seconds inside each take to decode just that stretch (a name and its neighbours, 2–3 s)
  phonemes some.wav [A B]   the same for any audio file

  uv run --with numpy --with praat-parselmouth python tools/voice_check.py pitch
  uv run --with numpy --with praat-parselmouth python tools/voice_check.py takes l3_2 l6_1
  uv run --with numpy --with torch --with transformers python tools/voice_check.py phonemes l3_2

Pitch range: from the reference voice (floor 75 Hz, ceiling 1.6 × its median), or PITCH_FLOOR / PITCH_CEIL. A ceiling far above the
voice (300 Hz for a 120 Hz male voice) makes Praat jump an octave and fakes a rise; a female voice goes creaky (80–100 Hz) at the
end of a line, so its floor stays at 75.
"""
import os, sys, json, re
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_audio as M

ROOT = M.ROOT


def f0_track(x, sr, floor, ceil):
    import parselmouth
    p = parselmouth.Sound(x, sampling_frequency=sr).to_pitch(time_step=.01, pitch_floor=floor, pitch_ceiling=ceil)
    return p.xs(), p.selected_array['frequency']


def pitch_range():
    floor, ceil = float(os.environ.get('PITCH_FLOOR', 75)), os.environ.get('PITCH_CEIL')
    if ceil: return floor, float(ceil)
    if not os.path.exists(M.REF): return floor, 400.
    ts, f = f0_track(M.decode(M.REF), M.SR, 75, 400); f = f[f > 0]
    return floor, round(1.6 * float(np.median(f))) if len(f) else 400.


def st(a, b): return 12 * np.log2(a / b)   # semitones from b to a


def describe(x, floor, ceil):
    """median F0, 2 s window medians, and the slope over the last voiced 0.35 s (semitones, + = rises)"""
    ts, f = f0_track(x, M.SR, floor, ceil); v = f > 0
    if v.sum() < 10: return None
    med = float(np.median(f[v]))
    wins = []
    for a in np.arange(0, ts[-1] - 1.5, 2.):   # whole windows only (a short last one is mostly the final syllable's creak)
        w = f[(ts >= a) & (ts < a + 2) & v]
        if len(w) > 20: wins.append(float(np.median(w)))
    tv = ts[v]; last = f[v][tv >= tv[-1] - .35]
    k = max(1, len(last) // 4)
    end = st(np.median(last[-k:]), np.median(last[:k])) if len(last) >= 8 else 0.
    return {'med': med, 'wins': wins, 'end': end}


def load_tl():
    s = open(os.path.join(ROOT, 'timeline.js'), encoding='utf-8').read()
    return json.loads(s[s.index('{'):s.rindex('}') + 1])


def cmd_pitch():
    floor, ceil = pitch_range(); tl = load_tl()
    mix = M.decode(os.path.join(M.AUD, 'mix.wav'))
    rows = []
    for lid in tl['order']:
        L = tl['lines'][lid]; d = describe(mix[int(L['start'] * M.SR):int(L['end'] * M.SR)], floor, ceil)
        if d: rows.append((lid, L, d))
    allmed = float(np.median([d['med'] for _, _, d in rows]))
    print(f'pitch {floor:.0f}–{ceil:.0f} Hz, all lines {allmed:.0f} Hz. ! = off by 2.5+ semitones, a 2 s window 3+ below its line, or an end rising 3+')
    bad = 0
    for lid, L, d in rows:
        off = st(d['med'], allmed); drop = min((st(w, d['med']) for w in d['wins']), default=0)
        flag = abs(off) >= 2.5 or drop <= -3 or d['end'] >= 3
        bad += flag
        m, s_ = divmod(L['start'], 60)
        print(f"{'!' if flag else ' '} {lid:7s} {int(m)}:{s_:04.1f}  {d['med']:4.0f} Hz ({off:+.1f})  windows {' '.join(f'{w:.0f}' for w in d['wins'])}  end {d['end']:+.1f} st")
    print(f'{bad} line(s) to listen to. Re-read one with N=8 make_audio.py tts --redo <id>, then: voice_check.py takes <id>')


def cmd_takes(ids):
    floor, ceil = pitch_range()
    allmed = None
    if os.path.exists(os.path.join(M.AUD, 'mix.wav')) and os.path.exists(os.path.join(ROOT, 'timeline.js')):
        tl = load_tl(); mix = M.decode(os.path.join(M.AUD, 'mix.wav'))
        meds = [d['med'] for L in tl['lines'].values() if (d := describe(mix[int(L['start'] * M.SR):int(L['end'] * M.SR)], floor, ceil))]
        allmed = float(np.median(meds)) if meds else None
    pick, _ = M.pick_takes(ids, M.PACE)
    for lid in ids:
        print(f'\n{lid}: {M.LINE[lid][2]}' + (f'   (all lines {allmed:.0f} Hz)' if allmed else ''))
        for i, path in enumerate(M.takes_of(lid)):
            x = M.decode(path); db = M.frames_db(x); v = np.where(db > -45)[0]
            tail = (len(db) - 1 - v[-1]) / 100 if len(v) else 0
            d = describe(x, floor, ceil) or {'med': 0, 'wins': [], 'end': 0}
            tr = M.transcribe(path)['text']
            mark = '*' if pick[lid]['k'] == i else ' '
            off = f" ({st(d['med'], allmed):+.1f})" if allmed and d['med'] else ''
            print(f"{mark} {i:2d}  {len(x) / M.SR:5.2f}s  air {tail:.2f}s{' CUT' if tail < .2 else ''}  {d['med']:4.0f} Hz{off}  windows {' '.join(f'{w:.0f}' for w in d['wins'])}  end {d['end']:+.1f} st  | {tr}")
    print('\n* = the current pick. TAKE = {id: number} in tools/script.py pins another (the number above, not the file name)')


_W2V = None
def phonemes(x16):
    global _W2V
    import torch
    from transformers import Wav2Vec2ForCTC, Wav2Vec2FeatureExtractor
    from huggingface_hub import hf_hub_download
    mid = 'facebook/wav2vec2-lv-60-espeak-cv-ft'   # the tokenizer needs espeak installed; the feature extractor + vocab.json do not
    if _W2V is None:
        inv = {v: k for k, v in json.load(open(hf_hub_download(mid, 'vocab.json'), encoding='utf-8')).items()}
        _W2V = (Wav2Vec2FeatureExtractor.from_pretrained(mid), Wav2Vec2ForCTC.from_pretrained(mid).eval(), inv)
    fe, model, inv = _W2V
    with torch.no_grad():
        ids = model(fe(x16.astype(np.float32), sampling_rate=16000, return_tensors='pt').input_values).logits.argmax(-1)[0].tolist()
    out, prev = [], None
    for i in ids:
        if i != prev and not inv.get(i, '<pad>').startswith('<'): out.append(inv[i])
        prev = i
    return ' '.join(out)


def cmd_phonemes(target, a=None, b=None):
    paths = [target] if os.path.exists(target) else M.takes_of(target)
    if not paths: sys.exit(f'no takes for {target} (current voice and read form)')
    if target in M.LINE: print(f'{target}: {M.LINE[target][2]}')
    for i, path in enumerate(paths):
        x = M.decode(path, 16000)
        if a is not None: x = x[int(a * 16000):int(b * 16000)]
        print(f'{i:2d}  {phonemes(x)}')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == 'pitch': cmd_pitch()
    elif a[0] == 'takes' and len(a) > 1: cmd_takes(a[1:])
    elif a[0] == 'phonemes' and len(a) in (2, 4): cmd_phonemes(a[1], *(map(float, a[2:]) if len(a) == 4 else ()))
    else: sys.exit(__doc__)
