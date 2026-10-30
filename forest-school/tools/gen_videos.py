"""grok(image_to_video)로 codex 그림을 짧은 영상으로 — video/<key>.mp4, 그리고 화면이 그릴 프레임 video/<key>/0001.jpg …

- 오프닝 4개: 계절 풍경이 살짝 움직이고, 그 위에 제목이 얹혀요
- 움직여야 이해되는 장면 몇 개: 그 장면 그림(bg)이 나올 때 그림 대신 영상이 한 번 재생된 뒤 원래 그림으로 돌아와요

  python3 tools/gen_videos.py [--jobs 3] [--redo sp_title]
"""
import os, sys, subprocess, concurrent.futures as cf, time, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FFMPEG = os.environ.get('FFMPEG') or os.path.join(ROOT, '../math-di-improvement-v2/node_modules/ffmpeg-static/ffmpeg')
arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
JOBS = int(arg('--jobs', 3))
REDO = set((arg('--redo') or '').split(',')) - {''}
KEEP = 'Keep the exact same framing, characters, colors and hand-drawn picture-book illustration style; no text; no new objects; no camera cuts.'

VIDEOS = {
    'sp_title': 'Gentle spring breeze: yellow and pink blossoms sway softly, a few petals drift, the two yellow butterflies flutter across, clouds slowly move; the camera slowly pushes in a little.',
    'su_title': 'The clear stream flows and sparkles between the mossy boulders, leaves rustle in a light breeze, a dragonfly darts across, clouds drift; slow gentle push-in.',
    'au_title': 'Colorful autumn leaves flutter down from the trees in the breeze, the flock of wild geese flies slowly across the sky; slow gentle push-in.',
    'wi_title': 'Soft snowflakes fall steadily over the winter mountain, the hawk glides slowly across the sky, dry grass sways; slow gentle push-in.',
    'sp_dandelion': 'The children softly blow on the dandelion seed heads and dozens of fluffy white seeds lift off and float up and away across the sky on the wind.',
    'sp_antlion': 'The tiny ant slips and slides down the steep side of the sand pit, grains of sand trickle down after it toward the bottom; the children watch closely.',
    'su_ash': 'Bright sky-blue color slowly spreads and swirls out from the twig through the clear water in the basin while the children watch in amazement.',
    'au_seeds': 'The ripe pink jewelweed seed pod suddenly bursts open with a snap and the little seeds shoot out in every direction; the children laugh in surprise.',
    'wi_wood': 'The woodpecker on the left pecks the tree trunk very fast again and again, tiny wood chips fly; the flying squirrel on the right blinks and peeks out of its hole.',
}


def job(key):
    src, dst = os.path.join(ROOT, 'img/gen', key + '.png'), os.path.join(ROOT, 'video', key + '.mp4')
    if not os.path.exists(src): return f'skip {key}: 그림 없음'
    t = time.time()
    if key in REDO or not os.path.exists(dst):
        prompt = (f'Use your image_to_video tool to animate the image file img/gen/{key}.png into a short video of about 6 seconds. '
                  f'Motion: {VIDEOS[key]} {KEEP} Save the resulting mp4 to video/{key}.mp4 (overwrite) and reply with the path only.')
        subprocess.run(['grok', '--always-approve', '--cwd', ROOT, '-p', prompt], capture_output=True, text=True, timeout=900)
        if not os.path.exists(dst): return f'FAIL {key}'
    fd = os.path.join(ROOT, 'video', key)
    os.makedirs(fd, exist_ok=True)
    for f in glob.glob(os.path.join(fd, '*.jpg')): os.remove(f)
    subprocess.run([FFMPEG, '-v', 'error', '-y', '-i', dst, '-map', '0:v:0', '-vf', 'fps=24', '-q:v', '2', os.path.join(fd, '%04d.jpg')], check=True)
    return f'ok   {key} ({time.time() - t:.0f}s, {len(os.listdir(fd))} frames)'


def main():
    os.makedirs(os.path.join(ROOT, 'video'), exist_ok=True)
    keys = list(VIDEOS)
    with cf.ThreadPoolExecutor(JOBS) as ex:
        for r in ex.map(job, keys): print(r, flush=True)
    # 화면이 읽는 목록: 키 → 프레임 수
    import json
    meta = {k: len(glob.glob(os.path.join(ROOT, 'video', k, '*.jpg'))) for k in VIDEOS}
    open(os.path.join(ROOT, 'video', 'clips.js'), 'w').write('// written by tools/gen_videos.py\nwindow.CLIPS = ' + json.dumps({k: v for k, v in meta.items() if v}) + ';\n')


if __name__ == '__main__':
    main()
