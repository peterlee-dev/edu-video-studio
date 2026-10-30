"""확인용 페이지에 올릴 장면별 조각 영상 만들기 — out/review_<편>/NN.mp4 (720p, 조각마다 14MB 아래) + chapters.json

  python3 tools/review_parts.py spring
"""
import os, sys, json, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FFMPEG = os.environ.get('FFMPEG') or os.path.join(ROOT, '../math-di-improvement-v2/node_modules/ffmpeg-static/ffmpeg')
EP = sys.argv[1] if len(sys.argv) > 1 else 'spring'
LIMIT = 13.5e6   # 바이트


def load_tl():
    s = open(os.path.join(ROOT, f'timeline_{EP}.js')).read()
    return json.loads(s[s.index(f'.{EP} = ') + len(f'.{EP} = '):].rstrip().rstrip(';'))


def chapters(tl):
    sc = tl['scenes']; out = []
    for s in sc:
        if s['id'] == 'title': continue
        if s['id'] == 'open': out.append({'label': '오프닝', 'start': 0, 'end': s['end'], 'scenes': ['title', 'open']}); continue
        if s['id'] == 'gb':   # 골든벨은 둘로 나눠요
            qs = [q for q in tl['quizzes'] if q['scene'] == 'gb']; mid = qs[5]['start'] - .2
            out.append({'label': '도전! 골든벨 1~5번', 'start': s['start'], 'end': mid, 'scenes': ['gb']})
            out.append({'label': '도전! 골든벨 6~10번', 'start': mid, 'end': s['end'], 'scenes': ['gb']}); continue
        out.append({'label': s['label'], 'start': s['start'], 'end': s['end'], 'scenes': [s['id']]})
    out[-1]['end'] = tl['duration']
    for c in out:
        c['quizzes'] = [{'num': q['num'], 'q': q['q'], 'a': q['a'], 'at': round(q['start'] - c['start'], 1)} for q in tl['quizzes'] if c['start'] <= q['start'] < c['end']]
    return out


def main():
    tl = load_tl(); src = os.path.join(ROOT, 'out', f'forest_{EP}.mp4')
    od = os.path.join(ROOT, 'out', f'review_{EP}'); os.makedirs(od, exist_ok=True)
    chs = chapters(tl)
    for i, c in enumerate(chs):
        dur = c['end'] - c['start']; f = f'{i + 1:02d}.mp4'; dst = os.path.join(od, f)
        vb = int(min(2200e3, LIMIT * 8 / dur - 112e3) / 1000)
        for attempt in range(3):
            subprocess.run([FFMPEG, '-v', 'error', '-y', '-ss', f"{c['start']:.3f}", '-i', src, '-t', f'{dur:.3f}',
                            '-vf', 'scale=1280:720:flags=lanczos', '-c:v', 'libx264', '-preset', 'medium', '-b:v', f'{vb}k', '-maxrate', f'{int(vb * 1.3)}k', '-bufsize', f'{vb * 2}k',
                            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k', '-ac', '1', '-movflags', '+faststart', dst], check=True)
            if os.path.getsize(dst) <= 14.5e6: break
            vb = int(vb * .8)
        c.update({'file': f'parts/{f}', 'dur': round(dur, 2), 'start': round(c['start'], 2), 'end': round(c['end'], 2)})
        print(f, c['label'], f'{dur:.0f}s', f'{os.path.getsize(dst) / 1e6:.1f}MB', f'{vb}k', flush=True)
    json.dump({'ep': EP, 'title': tl['title'], 'duration': tl['duration'], 'chapters': chs}, open(os.path.join(od, 'chapters.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
