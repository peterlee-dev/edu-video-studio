# 내레이션 · 시각표 (`tools/make_audio.py`)

대본은 `tools/script.py` 하나예요. 어느 길로 목소리를 만들든 결과는 같은 모양이에요: `timeline.js`(장면 시각 + 문장마다 읽힌 단어와 그 시각), `audio/mix.wav`(내레이션 + 쪽 넘김 휙 + 끝인사 딩, 배경음악 없음), `subtitles.srt`.

## 어느 길로

| 가진 것 | 모드 | 하는 일 |
|---|---|---|
| 대본만 (아직 목소리 없음) | `dry` | 글자 수로 문장 길이를 어림(14.5 자/초) → `timeline.js` 만. 화면부터 짤 때 |
| 대본 + 목소리 샘플 | `tts` | DGX Qwen3-TTS 가 샘플 목소리를 복제해 문장마다 3번 읽고, whisper 로 받아써서 대본대로 읽은 것 중 말 빠르기가 가운데에 가깝고 중간에 긴 쉼이 없는 것을 골라요 |
| 대본 전체를 한 번에 읽은 녹음 | `take` | 녹음을 받아쓰고(`audio/narration_words.json`) 대본과 맞춰 문장마다 그 문장 단어 앞뒤 쉼 한가운데에서 잘라 다시 배치해요 |
| 녹음 + 녹음 뒤에 바뀐 문장 몇 개 | `take` + `CLONE` | 바뀐 문장만 녹음 목소리 복제로 새로 읽고, 녹음의 말 빠르기(atempo 0.9~1.15) · 음색(EQ) · 크기에 맞춰 그 자리에 넣어요 |

```bash
uv run --with numpy python tools/make_audio.py dry
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts            # TTS_URL 기본값 http://192.168.51.8:8095
uv run --with numpy --with mlx-whisper python tools/make_audio.py ref 14.1 28.7  # take + CLONE 일 때: 녹음에서 복제용 샘플 자르기
uv run --with numpy --with mlx-whisper python tools/make_audio.py take
```

- ffmpeg 는 `node_modules/ffmpeg-static/ffmpeg` 를 써요(`npm install` 먼저). 다른 것을 쓰려면 `FFMPEG=...`
- whisper 는 `mlx-community/whisper-large-v3-turbo`(Apple Silicon). 처음 한 번 모델을 받아요
- TTS 서버 상태: `curl http://192.168.51.8:8095/health` (DGX `~/dev/qwen3-tts-api`, 복제는 `POST /v1/tts/clone` 에 `text`, `ref_text`, `language`, `ref_audio`). 연결이 안 되면 사용자에게 DGX 서버를 켜 달라고 해요

## 대본 쓰기 (`tools/script.py`)

- `SCRIPT` 한 줄 = `(id, 장면, 쓰는 문장, 읽는 문장 또는 None, 뒤 쉼 초)`. id 는 `l<구역>_<번호>`. 장면 id 는 `SCENES` 와 `index.html` 의 `SC.<id>` 와 같아요
- **쓰는 문장**은 화면 · 자막에 맞는 바른 표기, **읽는 문장**은 TTS 가 더듬을 때만: 약어를 한 글자씩(`JEI-SLI` → `J-E-I S-L-I`), 연도(`2026–2028` → 말로), 코드명
- 문장 사이 0.45초, 쪽 사이 +1.0초, 첫 문장 전 2.6초, 끝 2.4초(`LEAD, GAP, SCENE_GAP, TAIL`). 문단이 끝나는 문장에 0.2~0.5초 쉼을 더 줘요
- 장면 시작은 그 쪽 첫 문장 0.9초 전: 종이가 넘어가 자리 잡은 뒤에 말이 시작돼요
- 대본을 고친 뒤에는 언제나 `make_audio.py` 를 다시 돌리고 `timeline.js` 는 손으로 고치지 않아요

## tts 모드

- 목소리 샘플: `audio/voice_ref.wav`(15~30초, 잡음 없이 문장 단위) + 그 대사 `audio/voice_ref.txt`. 지금까지 쓴 샘플: `ai-learning-platform-v3/audio/voice_ref.wav`(D–I 개선 내레이션 29초, 여성 영어)
- 받아쓰기 결과와 읽은 것은 `audio/tts_cache/` 에 남아요. 문장을 고치면 그 문장만 다시 읽어요. 샘플을 바꾸면 모두 다시 읽어요
- `! l3_2: no take reads the script word for word` 가 나오면: `N=8 ... tts --redo l3_2` (그 문장만 8번 새로 읽기), 그래도 안 되면 읽는 문장(4번째 칸)을 고쳐요
- 문장마다 소리 크기를 같게 맞춰요

## take 모드

- 녹음: `audio/narration.mp3`(또는 `.wav`, `.m4a`). 받아쓰기는 `audio/narration_words.json` 에 한 번만 해 두고 다시 써요(녹음을 바꾸면 이 파일을 지워요)
- 출력의 `aligned 572/578` 과 문장별 `found` 를 확인해요. `← reads differently` 가 붙은 문장은 녹음과 대본이 달라요: 대본을 녹음대로 되돌리거나 `CLONE` 에 넣어요
- 문장 경계에 쉼이 없으면(녹음에서 붙여 읽음) 두 단어 사이 가운데에서 잘라요. 출력의 구간(초)으로 확인해요
- `CLONE` 문장의 샘플은 `ref A B` 로 녹음에서 직접 잘라요(같은 사람 목소리). 복제 음성은 녹음보다 먹먹하게 나와서 EQ 로 고음을 돌려놓아요

## timeline.js 모양 (index.html 이 읽는 것)

```js
window.TL = {
  duration: 31.6,
  scenes: [{ id: 'title', label: 'Title', start: 0, end: 9.4 }, ...],
  cont: [],                      // script.py CONT
  order: ['l1_1', ...],
  lines: { l1_1: { scene: 'title', text: '…', start: 2.6, end: 7.6, words: [['hello', 2.66], ['today', 3.2], ...] } }
};
```
