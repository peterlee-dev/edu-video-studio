# 내레이션 · 시각표 (`tools/make_audio.py`)

대본은 `tools/script.py` 하나예요. 어느 길로 목소리를 만들든 결과는 같은 모양이에요: `timeline.js`(장면 시각 + 문장마다 읽힌 단어와 그 시각), `audio/mix.wav`(내레이션 + 쪽 넘김 휙 + 끝인사 딩, 배경음악 없음), `subtitles.srt`.

## 어느 길로

| 가진 것 | 모드 | 하는 일 |
|---|---|---|
| 대본만 (아직 목소리 없음) | `dry` | 글자 수로 문장 길이를 어림(14.5 자/초) → `timeline.js` 만. 화면부터 짤 때 |
| 대본 + 목소리 샘플 | `tts` | Qwen3-TTS 가 샘플 목소리를 복제해 문장마다 3번 읽고, whisper 로 받아써서 대본대로 읽은 것 중 말 빠르기가 `PACE`(기본: 전체 중간값)에 가깝고, 중간에 긴 쉼이 없고, 끝이 잘리지 않은 것을 골라요 |
| 대본 전체를 한 번에 읽은 녹음 | `take` | 녹음을 받아쓰고(`audio/narration_words.json`) 대본과 맞춰 문장마다 그 문장 단어 앞뒤 쉼 한가운데에서 잘라 다시 배치해요 |
| 녹음 + 녹음 뒤에 바뀐 문장 몇 개 | `take` + `CLONE` | 바뀐 문장만 녹음 목소리 복제로 새로 읽고, 녹음의 말 빠르기(atempo 0.9~1.15) · 음색(EQ) · 크기에 맞춰 그 자리에 넣어요 |

```bash
uv run --with numpy python tools/make_audio.py dry
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts            # TTS_URL=http://<서버>:8095 (기본값은 사내 DGX)
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l3_2,l6_1   # 그 문장만 8번 새로 읽기
uv run --with numpy --with mlx-whisper python tools/make_audio.py ref 14.1 28.7  # take + CLONE 일 때: 녹음에서 복제용 샘플 자르기
uv run --with numpy --with mlx-whisper python tools/make_audio.py take
```

- ffmpeg 는 `node_modules/ffmpeg-static/ffmpeg` 를 써요(`npm install` 먼저). 다른 것을 쓰려면 `FFMPEG=...`
- whisper 는 `mlx-community/whisper-large-v3-turbo`(Apple Silicon). 처음 한 번 모델을 받아요
- TTS 서버: Qwen3-TTS(`Qwen/Qwen3-TTS-12Hz-1.7B-Base`)를 띄운 HTTP 서버. 주소는 `TTS_URL` 환경변수(기본값 `http://192.168.51.8:8095` = 사내 DGX, 서버 코드는 DGX 의 `~/dev/qwen3-tts-api`). 상태: `curl $TTS_URL/health`. 연결이 안 되면 사용자에게 서버를 켜 달라고(또는 주소를) 물어요
  - 다른 서버를 쓸 때 맞춰야 할 약속: `POST /v1/tts/clone`, multipart form — `text`(읽을 문장), `ref_text`(기준 녹음에서 말한 문장), `language`(`English` | `Korean`), `format`(`wav`), 파일 `ref_audio`(기준 녹음 wav). 응답 본문 = wav 바이트
- 이 서버는 말소리가 끝나는 순간 출력을 끊어요. 그래서 문장 뒤에 짧은 문장을 붙여 읽히고 잘라내요(`TAIL_TEXT`, [voice-qa.md](voice-qa.md) 1)

## 대본 쓰기 (`tools/script.py`)

- `SCRIPT` 한 줄 = `(id, 장면, 쓰는 문장, 읽는 문장 또는 None, 뒤 쉼 초)`. id 는 `l<구역>_<번호>`. 장면 id 는 `SCENES` 와 `index.html` 의 `SC.<id>` 와 같아요
- **쓰는 문장**은 화면 · 자막에 맞는 바른 표기, **읽는 문장**은 TTS 가 더듬을 때만: 약어를 한 글자씩(`JEI-SLI` → `J-E-I S-L-I`), 연도(`2026–2028` → 말로), 코드명
- 한국어: 숫자 · 영문은 소리대로(7개 → 일곱 개, D등급 → 디등급, GEO → 지이오), 된소리(평가 → 평까, 강점 → 강쩜). 여러 문장에 되풀이되면 `SAY = [('D등급', '디등급'), …]` 에 두고 읽는 문장을 만들 때 적용해요(make_audio 는 받아쓰기에도 `SAY` 를 적용해 비교해요). 가운뎃점(·)은 띄어 읽어요
- 숨 쉴 곳: 긴 문장은 읽는 문장에서 구절 뒤에 쉼표를 넣어요(목소리 속도는 그대로)
- `JOIN = {'l5_1': .25}`: 대본의 한 문장이 두 장면에 걸칠 때, 다음 줄이 그 짧은 쉼 뒤에 바로 이어져요(그 장면은 `CONT`)
- 효과음: 쪽 넘김 휙(`CONT` 쪽은 없음), `CHIME_AT`(제목 쪽에서 그 초에) · `DING_BEFORE`(그 문장 앞) · `DING_END`(끝 문장 뒤) 밝은 차임. 모두 `make_audio.py` 안에서 합성해요(효과음 파일 없음). 배경음악은 없어요
- 문장 사이 0.45초, 쪽 사이 +1.0초, 첫 문장 전 2.6초, 끝 2.4초(`LEAD, GAP, SCENE_GAP, TAIL`). 문단이 끝나는 문장에 0.2~0.5초 쉼을 더 줘요. 한국어 영상은 문장 사이 0.6초 · 쪽 사이 +1.5초 정도가 자연스러웠어요
- 장면 시작은 그 쪽 첫 문장 1.2초 전(`make_audio.py` 의 `TURN`): 종이가 1.1초 동안 넘어가(`index.html` 의 `TR`) 자리 잡은 뒤에 말이 시작돼요. 둘은 함께 바꿔요
- 대본을 고친 뒤에는 언제나 `make_audio.py` 를 다시 돌리고 `timeline.js` 는 손으로 고치지 않아요

## tts 모드

- 목소리 샘플: `audio/voice_ref.wav` + 그 대사 `audio/voice_ref.txt`. 스킬의 `voices/` 에 4개(영어 남 · 여, 한국어 남 · 여)가 있고 `scripts/new_video.sh --voice <id>` 가 복사해 줘요. 목록 · 음 높이 · 주의점: [../voices/README.md](../voices/README.md). **영상 언어와 같은 언어의 목소리**를 써요. 성별은 문서 표기 말고 음 높이로 확인해요(여자 ≈ 210 Hz 이상)
- 다른 목소리를 시험할 때: `audio/<이름>.wav` + `.txt` 를 두고 `VOICE=<이름> … tts` (또는 `script.py` 의 `VOICE`)
- 받아쓰기 결과와 읽은 것은 `audio/tts_cache/` 에 남아요. 문장을 고치면 그 문장만 다시 읽어요. 샘플을 바꾸면 모두 다시 읽어요
- 출력 한 줄: `l3_2  take 1  4.13s  miss 0  pause 0.31s  tail 0.30s  [0 0 2c]` — 고른 테이크, 길이, 대본과 다른 글자 수, 가장 긴 쉼, 끝 여유, 테이크마다 miss(`c` = 끝 잘림). 마지막에 `pace 5.64 chars/s`
- `! l3_2: no take reads the script word for word` 가 나오면: `N=8 ... tts --redo l3_2` (그 문장만 8번 새로 읽기), 그래도 안 되면 읽는 문장(4번째 칸)이나 `SAY` 를 고쳐요
- 받아쓰기를 통과해도 톤 · 발음 · 끝인사 억양이 틀릴 수 있어요: 넘기기 전에 [voice-qa.md](voice-qa.md) 대로 `tools/voice_check.py pitch` 와 이름 · 약어 문장의 `phonemes` 를 확인해요
- 고른 테이크를 바꾸려면 `TAKE = {'l3_2': 7}`. 한 번 넘긴 영상은 `PACE` 를 출력된 값으로 고정해서, 한 문장을 다시 읽혀도 다른 문장이 바뀌지 않게 해요
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
