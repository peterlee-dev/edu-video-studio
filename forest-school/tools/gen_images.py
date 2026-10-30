"""tools/images.py 의 그림을 codex(이미지 생성)로 그려 img/gen/<key>.png 에 저장 — 없는 그림만, 여러 개를 동시에

  python3 tools/gen_images.py [--jobs 6] [--redo key1,key2] [--only sp_]
"""
import os, sys, subprocess, concurrent.futures as cf, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from images import IMAGES, STYLE, CAST, PANEL

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'img', 'gen')
arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
JOBS = int(arg('--jobs', 6))
REDO = set((arg('--redo') or '').split(',')) - {''}
ONLY = arg('--only', '')


def job(key):
    spec, dst = IMAGES[key], os.path.join(OUT, key + '.png')
    parts = [spec['prompt'], STYLE]
    if spec['kind'] == 'panel': parts.insert(1, PANEL)
    if spec['cast']: parts.append(CAST)
    prompt = (f'Use your image generation tool to create exactly ONE image, then copy the generated PNG to {dst} '
              f'(overwrite if it exists) and reply with just the path. Do not create any other files.\n\nImage: ' + ' '.join(parts))
    cmd = ['codex', 'exec', '--skip-git-repo-check', '--sandbox', 'workspace-write', '-C', ROOT]
    if spec['cast']: cmd += ['-i', os.path.join(OUT, 'cast.png')]
    t = time.time()
    for attempt in range(2):
        r = subprocess.run(cmd + ['--', prompt], capture_output=True, text=True, timeout=900)
        if os.path.exists(dst) and os.path.getmtime(dst) > t: return f'ok   {key} ({time.time() - t:.0f}s)'
    return f'FAIL {key}: {r.stdout[-300:]} {r.stderr[-300:]}'


def main():
    os.makedirs(OUT, exist_ok=True)
    keys = [k for k in IMAGES if k.startswith(ONLY) and (k in REDO or not os.path.exists(os.path.join(OUT, k + '.png')))]
    print(f'{len(keys)}장 그리기 (동시 {JOBS})', flush=True)
    with cf.ThreadPoolExecutor(JOBS) as ex:
        for res in ex.map(job, keys): print(res, flush=True)


if __name__ == '__main__':
    main()
