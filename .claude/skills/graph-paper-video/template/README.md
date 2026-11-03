# <영상 제목>

<출처: 어떤 장표 · 대본으로 만들었는지 한두 문장>

- **모눈종이 워크북 한 장**: 장면마다 한 쪽(p. 1 ~ p. N). 장면이 바뀔 때 종이 위를 옆으로 넘어가고(믹스의 휙 소리와 같은 때), 읽는 동안은 화면이 움직이지 않아요
- 선생님 펜 표시: <이 영상에서 쓴 것: 빨간 동그라미 · 체크 · 밑줄, 형광펜, 포스트잇, 도장(…)>
- 색: `수학 영상 컬러 개선.pdf` 기준(레드 `#E5303A` 메인, 네이비 부정 · 하락, 비교는 레드 → 블루 → 민트, 나머지 그레이). 팔레트는 `content.js` 의 `colors`
- 1920×1080, 30fps. 글꼴은 macOS 시스템 글꼴 Avenir Next(본문) · Noteworthy(손글씨). 배경음악 없음 (내레이션 + 쪽 넘김 휙 소리, 끝인사 딩)
- 화면에 자막은 넣지 않아요. 필요하면 `subtitles.srt`

| p. | 장면 | 문장 | 화면 |
|---|---|---|---|
| 1 | title | l1_1 | … |

## 음성 · 시각표 만들기

- 대본: `tools/script.py`. <목소리: tts(복제 샘플 …) / take(녹음 …)>

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py <tts|take>   # timeline.js, audio/mix.wav, subtitles.srt
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.<id>`, 제목 · 마무리 문구와 색: `content.js` (영상 편집기에서도 수정 가능)
- 미리보기: `index.html` (재생 막대), `index.html?t=120` (그 시각)

```bash
node tools/snap.mjs out/snaps --ends            # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                      # out/<폴더_이름>.mp4 (GPU)
node render.mjs --workers 3 --only 99-115,217-end   # 고친 구간(초)만 다시 그리고 나머지는 기존 영상에서 가져와요
node render.mjs --cpu --workers 6                # GPU 가 없을 때: 예전 CPU 방식
```

`render.mjs` 는 GPU 로 렌더해요: Chrome 이 Metal 로 캔버스를 그리고, 브라우저 안의 하드웨어 H.264 인코더(WebCodecs → VideoToolbox)로 바로 압축해 조각을 다시 인코딩하지 않고 이어 붙여요(`jei-english-adaptive-diagnosis` 에서 가져옴). 예전 CPU 방식(SwiftShader + PNG + libx264)보다 훨씬 빠르고 메모리도 덜 써요. GPU 가 없는 컴퓨터는 `--cpu`.
