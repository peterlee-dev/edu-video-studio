"""숲 학교 사계절 — 편마다 내레이션·효과음·배경음과 시각표 만들기

- 목소리: Qwen3-TTS (Apache 2.0), DGX TTS API. VoiceDesign 으로 지은 두 목소리를 Base 모델로 복제해서 읽어요
    내레이터  audio/voice_narr.wav (+ .txt)      곰취 선생님  audio/voice_teacher.wav (+ .txt)
- 대본: tools/script.py. 문제(Q)는 '문제!' → 5초 카운트다운(째깍) → '정답은 ○○!' 순서로 이어 붙여요
- 문장마다 실제 음성 길이로 시각을 정해 timeline_<편>.js 를 쓰고, audio/mix_<편>.wav 를 만들어요

  python3 tools/make_audio.py spring           # spring | summer | autumn | winter | all
  python3 tools/make_audio.py spring --redo g2,gq_q   (만든 음성은 audio/tts_cache/ 에 남아서 바뀐 문장만 다시 읽어요)
"""
import os, sys, json, hashlib, re, subprocess, urllib.request, uuid, wave
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from script import EPISODES

SR = 48000
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
AUD = os.path.join(ROOT, 'audio')
CACHE = os.path.join(AUD, 'tts_cache')
TTS = os.environ.get('TTS_URL', 'http://192.168.51.8:8095')
FFMPEG = os.environ.get('FFMPEG') or next((p for p in [os.path.join(ROOT, 'node_modules/ffmpeg-static/ffmpeg'), os.path.join(ROOT, '../math-di-improvement-v2/node_modules/ffmpeg-static/ffmpeg')] if os.path.exists(p)), 'ffmpeg')
VOICES = {'n': 'voice_narr', 't': 'voice_teacher'}
GAP, SCENE_GAP, LEAD = .45, 1.1, 0.0   # 문장 사이, 장면 사이 쉼(초) — 저학년이 따라오게 넉넉히
OPEN = 6.0                              # 첫 화면(제목 + grok 영상) 길이
COUNT = 5                               # 문제 카운트다운(초)


def h(*a): return hashlib.sha1('|'.join(a).encode()).hexdigest()[:16]


def post(path, fields, files=None):
    if files:
        b = uuid.uuid4().hex; body = b''
        for k, v in fields.items(): body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
        for k, (name, data) in files.items(): body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + data + b'\r\n'
        body += f'--{b}--\r\n'.encode(); ctype = f'multipart/form-data; boundary={b}'
    else:
        body = json.dumps(fields).encode(); ctype = 'application/json'
    req = urllib.request.Request(TTS + path, data=body, headers={'Content-Type': ctype}, method='POST')
    with urllib.request.urlopen(req, timeout=300) as r: return r.read()


def decode(path):
    out = subprocess.run([FFMPEG, '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(out, np.float32).copy()


def trim(x, thr=.01):
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx): return x
    return x[max(0, idx[0] - int(.03 * SR)):min(len(x), idx[-1] + int(.08 * SR))]


def ref(who):
    b = os.path.join(AUD, VOICES[who]); return open(b + '.wav', 'rb').read(), open(b + '.txt').read().strip()


def line_path(who, tts):
    wav, txt = ref(who); return os.path.join(CACHE, h(who, wav.hex()[:20000], txt, tts) + '.wav')


def say(who, tts, lid, redo):
    p = line_path(who, tts)
    if not os.path.exists(p) or lid in redo:
        os.makedirs(CACHE, exist_ok=True); print('TTS', who, lid, tts[:40], flush=True)
        wav, txt = ref(who)
        open(p, 'wb').write(post('/v1/tts/clone', {'text': tts, 'ref_text': txt, 'language': 'Korean', 'format': 'wav'}, {'ref_audio': ('ref.wav', wav)}))
    return trim(decode(p))


# ---------------- 합성 소리 ----------------
def t_(d): return np.arange(int(d * SR)) / SR
def tone(f, d, g=.3, dec=6, harm=(1,)):
    tt = t_(d); x = sum(np.sin(2 * np.pi * f * k * tt) / k ** 1.4 for k in harm)
    return x * np.exp(-tt * dec) * np.minimum(1, tt / .004) * g
def noise(d, seed=1): return np.random.default_rng(seed).standard_normal(int(d * SR))
def lp(x, a):
    y = np.empty_like(x); s = 0.
    for i, v in enumerate(x): s += a * (v - s); y[i] = s
    return y
def mix_at(buf, x, t, g=1.):
    i = int(t * SR); n = min(len(x), len(buf) - i)
    if n > 0 and i >= 0: buf[i:i + n] += x[:n] * g


def sfx(name):
    if name == 'pop':
        tt = t_(.14); f = 520 + 900 * np.exp(-tt * 30); return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 28) * .5
    if name == 'swish':
        x = lp(noise(.45, 4), .15); return x * np.sin(np.pi * np.linspace(0, 1, len(x)) ** .6) ** 2 * 1.1
    if name == 'tick':
        return tone(1700, .06, .3, 60) + tone(850, .06, .12, 60)
    if name == 'question':   # 문제 등장: 올라가는 두 음
        out = np.zeros(int(.7 * SR)); mix_at(out, tone(659.25, .25, .25, 7, (1, 2, 3)), 0); mix_at(out, tone(987.77, .5, .25, 6, (1, 2, 3)), .13); return out
    if name == 'dingdong':   # 딩동댕
        out = np.zeros(int(1.4 * SR))
        for i, f in enumerate([783.99, 659.25, 1046.5]): mix_at(out, tone(f, .9, .28, 4, (1, 2, 3)), i * .2)
        return out
    if name == 'bell':       # 골든벨 종소리
        out = np.zeros(int(2.4 * SR))
        for i in range(3): mix_at(out, tone(1318.5, 1.6, .22, 2.2, (1, 2.76, 5.4)) + tone(659.25, 1.6, .14, 2, (1, 2)), i * .32)
        return out
    if name == 'fanfare':
        out = np.zeros(int(1.8 * SR))
        for i, (f, d) in enumerate([(523.25, .14), (659.25, .14), (783.99, .14), (1046.5, .9)]): mix_at(out, tone(f, d + .5, .2, 3 if d > .5 else 8, (1, 2, 3, 4)), i * .15)
        return out
    if name == 'sparkle':
        out = np.zeros(int(1.2 * SR)); rng = np.random.default_rng(11)
        for i in range(9): mix_at(out, tone(rng.choice([2093, 2349, 2637, 3136, 3520]), .4, .09, 9), i * .09)
        return out
    if name == 'birds':      # 짹짹 (오프닝)
        out = np.zeros(int(2.2 * SR)); rng = np.random.default_rng(3)
        for i in range(7):
            tt = t_(.09); f = 3200 + 1400 * np.sin(np.pi * tt / .09) + rng.uniform(-300, 300)
            mix_at(out, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / .09) * .16, .1 + i * .27 + rng.uniform(0, .08))
        return out
    raise KeyError(name)


def bgm(dur, mood):
    """잔잔한 반복 선율 — 계절마다 조와 빠르기만 달리 (오르골·마림바 느낌)"""
    key = {'spring': 1.0, 'summer': 1.122, 'autumn': .891, 'winter': .944}[mood]
    bpm = {'spring': 92, 'summer': 100, 'autumn': 84, 'winter': 76}[mood]
    out = np.zeros(int(dur * SR) + SR); beat = 60 / bpm
    def mar(f, d=.5, g=.1): return tone(f * key, d, g, 6, (1, 4))
    chords = [(130.81, [261.63, 329.63, 392]), (174.61, [261.63, 349.23, 440]), (196, [246.94, 293.66, 392]), (130.81, [261.63, 329.63, 392])]
    melody = [523.25, 659.25, 783.99, 659.25, 698.46, 659.25, 587.33, 523.25, 587.33, 659.25, 587.33, 493.88, 523.25, 392, 440, 523.25]
    t, bar = 0., 0
    while t < dur:
        root, ch = chords[bar % 4]
        mix_at(out, tone(root / 2 * key, beat * 2, .14, 2.5, (1, 2)), t); mix_at(out, tone(root / 2 * key, beat * 2, .09, 2.5, (1, 2)), t + beat * 2)
        for k in range(4):
            for f in ch: mix_at(out, mar(f, .35, .03), t + k * beat + beat / 2)
        if (bar // 4) % 3 != 2:
            for k in range(4): mix_at(out, mar(melody[(bar % 4) * 4 + k], .5, .06), t + k * beat)
        t += beat * 4; bar += 1
    return out[:int(dur * SR)]


def chunks(text, maxc=30):
    parts = re.split(r'(?<=[,.?!])\s+', text); out, cur = [], ''
    for p in parts:
        if cur and len(cur) + len(p) + 1 > maxc: out.append(cur); cur = p
        else: cur = (cur + ' ' + p).strip()
    if cur: out.append(cur)
    return out


def speakable(s): return s.replace('·', ' ').replace('‘', '').replace('’', '')


def build(ep, redo):
    E = EPISODES[ep]
    items, scenes, cues, voice = [], [], [], []
    t = LEAD
    def add_line(lid, who, sub, tts, scene, extra=None, pause=0.0):
        nonlocal t
        x = say(who, speakable(tts or sub), lid, redo); d = len(x) / SR
        cs = chunks(sub); tot = sum(len(c) for c in cs) or 1; ct, ch = t, []
        for c in cs: dd = d * len(c) / tot; ch.append({'text': c, 'start': round(ct, 3), 'end': round(ct + dd, 3)}); ct += dd
        it = {'id': lid, 'who': who, 'scene': scene, 'text': sub, 'start': round(t, 3), 'end': round(t + d, 3), 'chunks': ch}
        if extra: it.update(extra)
        items.append(it); voice.append((t, x)); t += d + GAP + pause
        return it
    def scene_start(sid, label, kind='scene'):
        nonlocal t
        if scenes: t += SCENE_GAP
        scenes.append({'id': sid, 'label': label, 'kind': kind, 'start': round(t - (SCENE_GAP * .5 if scenes else 0), 3)})
    def quiz(q, scene, num=None):
        nonlocal t
        pre = f'{num}번 문제!' if num else '문제!'
        qi = add_line(q['id'] + '_q', 'n', q['q'], f"{pre} {q['tts_q'] or q['q']}", scene, {'role': 'q'})
        cues.append({'t': round(qi['start'] - .35, 3), 'name': 'question', 'g': .7})
        t += .2; cd0 = t
        for k in range(COUNT): cues.append({'t': round(cd0 + k, 3), 'name': 'tick', 'g': .8})
        t = cd0 + COUNT
        cues.append({'t': round(t, 3), 'name': 'dingdong', 'g': .8}); t += .7
        ai = add_line(q['id'] + '_a', 'n', q['a'], q['tts_a'] or f"정답은, {q['a']}!", scene, {'role': 'a'}, pause=.5)
        quizzes.append({'id': q['id'], 'scene': scene, 'num': num, 'q': q['q'], 'a': q['a'], 'ox': q['ox'],
                        'start': round(qi['start'] - .5, 3), 'qEnd': qi['end'], 'cd': round(cd0, 3), 'reveal': round(cd0 + COUNT, 3), 'end': round(ai['end'] + .6, 3)})
    quizzes = []

    # 1) 첫 화면: 제목 + grok 영상 (말 없이 효과음)
    scenes.append({'id': 'title', 'label': f"{E['title']} — 제목", 'kind': 'title', 'start': 0})
    cues += [{'t': .3, 'name': 'birds', 'g': .6}, {'t': 1.2, 'name': 'fanfare', 'g': .7}]
    t = OPEN
    # 2) 장면들
    for sid, label, lines in E['scenes']:
        scene_start(sid, label)
        for L in lines:
            if L['kind'] == 'quiz': quiz(L, sid); continue
            add_line(L['id'], L['who'], L['text'], L['tts'], sid, {'bg': L['bg'], 'ov': L['ov']}, L['pause'])
            if L['ov'] and L['ov'][0] in ('key', 'panel', 'chain'): cues.append({'t': round(items[-1]['start'] + .05, 3), 'name': 'pop', 'g': .5})
    # 3) 도전 골든벨
    scene_start('gb', '도전! 골든벨', 'gb')
    cues.append({'t': round(t, 3), 'name': 'bell', 'g': .7}); t += 2.2
    add_line('gb0', 'n', '도전! 골든벨! 지금까지 배운 내용으로 문제를 풀어 봐요. 문제를 듣고, 정답을 크게 외쳐 보세요!', None, 'gb', {'role': 'gbintro'}, .3)
    for i, q in enumerate(E['gb']): quiz(q, 'gb', i + 1)
    # 4) 마무리
    scene_start('end', '마무리', 'end')
    cues.append({'t': round(t, 3), 'name': 'fanfare', 'g': .7}); t += .6
    last = E['id'] == 'winter'
    add_line('end1', 'n', '골든벨을 울렸나요? 정말 잘했어요!', None, 'end', {'role': 'end'}, .2)
    add_line('end2', 'n', '사계절 숲 학교는 여기까지! 이제 여러분도 숲 박사예요!' if last else f"{E['title']} 숲 이야기, 재미있었나요? 다음 편에서 또 만나요!", None, 'end', {'role': 'end'}, 2.0)
    cues.append({'t': round(items[-1]['end'] + .3, 3), 'name': 'sparkle', 'g': .7})
    dur = round(t + .8, 2)
    for i, s in enumerate(scenes): s['end'] = scenes[i + 1]['start'] if i + 1 < len(scenes) else dur
    for s in scenes[2:]: cues.append({'t': round(s['start'] + .05, 3), 'name': 'swish', 'g': .5})

    # 믹스: 목소리 + 효과음 + 배경음(말할 때·카운트다운 때 작게)
    n = int(dur * SR); vo, fx = np.zeros(n), np.zeros(n)
    for st, x in voice: mix_at(vo, x, st)
    for c in cues: mix_at(fx, sfx(c['name']), c['t'], c['g'] * .55)
    talk = np.zeros(n)
    for L in items: talk[int((L['start'] - .2) * SR):int((L['end'] + .25) * SR)] = 1
    for q in quizzes: talk[int(q['cd'] * SR):int(q['reveal'] * SR)] = .7
    k = int(.25 * SR); duck = np.convolve(talk, np.ones(k) / k, 'same')
    music = bgm(dur, ep) * (1 - .6 * duck) * .55
    fade = np.ones(n); fade[-int(2.5 * SR):] = np.linspace(1, 0, int(2.5 * SR)); fade[:int(.5 * SR)] = np.linspace(0, 1, int(.5 * SR))
    m = vo * .95 + fx + music * fade
    m = m / np.abs(m).max() * .89
    with wave.open(os.path.join(AUD, f'mix_{ep}.wav'), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((m * 32767).astype('<i2').tobytes())
    tl = {'ep': ep, 'title': E['title'], 'sub': E['sub'], 'color': E['color'], 'openBg': E['bg'], 'duration': dur, 'open': OPEN, 'count': COUNT,
          'scenes': scenes, 'items': items, 'quizzes': quizzes, 'sfx': sorted(cues, key=lambda c: c['t'])}
    open(os.path.join(ROOT, f'timeline_{ep}.js'), 'w').write('// written by tools/make_audio.py (timing from the real narration length). Do not edit by hand — rerun make_audio.py\n'
                                                            f'window.TLS = window.TLS || {{}}; window.TLS.{ep} = ' + json.dumps(tl, ensure_ascii=False) + ';\n')
    print(f'완료 {ep}: {dur / 60:.1f}분, 문장 {len(items)}개, 문제 {len(quizzes)}개 → timeline_{ep}.js, audio/mix_{ep}.wav')


def main():
    eps = [a for a in sys.argv[1:] if a in EPISODES or a == 'all']
    eps = list(EPISODES) if not eps or 'all' in eps else eps
    redo = set(sys.argv[sys.argv.index('--redo') + 1].split(',')) if '--redo' in sys.argv else set()
    for ep in eps: build(ep, redo)


if __name__ == '__main__':
    main()
