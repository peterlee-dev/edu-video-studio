# JEI AI Transformation Vision — AI Personalized Learning Platform Built on the JEI Math Knowledge Map (영문판)

`../jei-ai-vision-ko`(한국어판, `JEI_AI플랫폼_동영상장면.pptx.pdf` 12쪽)의 영문판이에요. 대본은 검토 시트 `어댑티브진단&AI플랫폼 소개_ 영상 수정 요청.pdf`(2026.11.05)와 함께 받은 영문 대본(12단락)이고, 화면은 한국어판과 같은 11쪽 · 27장면(2026.11.06 검토로 [2] 쪽을 뺌)을 영어 문구로 옮긴 것이에요. 디자인 시스템도 같아요(`.claude/skills/graph-paper-video`).

- **검토(2026.11.06, `어댑티브진단&AI플랫폼 소개_ 영상 수정 요청.pdf` 새 판, 영문 · 국문 공통)**: 목소리를 어댑티브진단 영상의 여자 영어 목소리로 바꾸고, [2] Beyond efficiency 쪽(l2_1–5)을 빼서 표지 다음 바로 지식맵 쪽이 나와요(뒤 쪽 번호는 p. 2 ~ p. 11 로 다시 매김). p. 7(POD)은 시트의 새 영문 화면대로 두 칸(1 Content Pool Development / 2 Personalized Delivery)으로 다시 그렸어요. 쪽 넘김 휙 소리를 빼고 넘김을 1.5배 빠르게 했어요(`script.py` `WHOOSH = False`, `index.html` `TR` 1.1 → 0.73초, `../jei-math-difference` 와 같음)
- **모눈종이 워크북 한 장**: 대본 한 단락 = 워크북 한 쪽(p. 1 ~ p. 11, [2] 단락은 뺌). 쪽이 바뀔 때만 종이가 옆으로 넘어가요(소리 없음). 긴 쪽은 같은 종이 위에서 여러 장면으로 나눠요(`CONT`, 쪽 넘김 · 휙 소리 없음). 그림은 내레이션 단어에 맞춰 하나씩 나타나요(`Wc(문장, 단어)`)
- 선생님 펜 표시: 빨간 동그라미 · 체크 · 손그림 상자 · 화살표, 형광펜, 포스트잇, 도장(STABLE · FLEXIBLE · CORE · STARTING POINT)
- 색: 한국어판과 같아요(`content.js` 의 `colors`). p. 9 도 한국어판 검토(2026.11.05)대로 Mastered = 네이비, Learning gap = 레드예요
- 글꼴: 본문 Avenir Next(시스템), 손글씨 Noteworthy(시스템, `../jei-corporation-overview` 와 같음)
- 길이 7분 22.1초(442.1초), 말 빠르기 약 14.8자/초. 1920×1080, 30fps. 배경음악 없음(내레이션 + 시작과 끝의 오르는 4음 차임). 화면 자막 없음(`subtitles.srt` 따로)

| p. | 대본 | 장면 | 문장 | 화면 |
|---|---|---|---|---|
| 1 | [1] Opening | title | l1_1–3 | Built on the JEI Math Knowledge Map · AI Personalized Learning Platform, "50 years" 동그라미 · "learning design expertise" 밑줄, 자산이 AI로 이어지는 지식맵, Every student, Learning optimized for every student · A new global standard |
| 2 | [3] The knowledge map | kmapList · kmapDots · kmapAI | l3_1–8 | Learning objective 1~5 목록 → JEI Math Knowledge Map, How do they relate? In what order? → 별처럼 흩어진 점이 선으로 이어짐, Point = objective · Line = relationship, Color · thickness → Review(네이비) · Next to learn(레드) |
| 3 | [4] How the map is built | universe | l4_1–5 | One Map for Every Curriculum. JEI learning design + Curricula worldwide(U.S. Common Core State Standards) → AI compares → Global math knowledge map, (JEI Math Universe) 동그라미, "used in Korea and overseas" 밑줄(2차 검토: 오른쪽 아래 REVIEWED 도장 뺌) |
| 4 | [5] What the map makes possible | country · countryTrack | l5_1–5 | Country knowledge maps · From one global map to country maps. 현행 체계(U.S. / Korea — 검토 2026.11.05: 한국어판 "미주용"과 같이 개수 · 영역 수 없음) → ① AI compares → Global math knowledge map → ② Aligned to each country(U.S. — CCSS / Korea — Revised curriculum), "Starting from scratch" 포스트잇에 X, 미국 지도 위 학생 상태 추적, Faster products for each market ↑ · Personalized for every student |
| 5 | [6] Three layers | layers · layerAgent · layerService · layerPace | l6_1–6 | 아래부터 쌓는 3계층(Knowledge · AI engine · Service)과 P-번호, 읽는 계층에 손그림 상자, STABLE · FLEXIBLE 도장 |
| 6 | [7] Seven projects, two phases | roadmap · phase1 · phase2 · wiki | l7_1–6 | Phase 1(2026.10 ~ 2027) · Phase 2(2028.01 ~) 여섯 과제와 개월 수, CORE 도장, P-06 LLM Wiki 가 모든 과제에 공급 |
| 7 | [8] Phase 1: Personalized POD | pod · podCycle | l8_1–7 | P-03 Personalized POD: One Student, One Workbook(검토 2026.11.06 시트 영문 화면). 1 Content Pool Development (In Advance): AI-assisted content drafting → Researcher review, revision & approval → Verified Content DB, "Built in advance, not on the spot" — l8_3 · l8_4 에서 차례로. 2 Personalized Delivery (Operational Stage): 다섯 칸이 l8_5 에서 한 칸씩, DB 에서 셋째 칸(Select & assemble …)으로 화살표가 내려와요. l8_6 에서 아래 점선 화살표(Each round’s results inform the next personalized learning cycle), l8_7 에 손글씨 "U.S. first → validate, then expand to Korea" |
| 8 | [9] Phase 2: Adaptive online learning | online · assistant | l9_1–6 | Learning behaviors(Right / wrong · Time · Hints · Retries) · AI for students · AI for teachers(P-05 AI learning assistant) |
| 9 | [10] A student’s progress | statusMap · statuses · statusUpdate | l10_1–6 | 지도의 세 영역(Top · Middle · Bottom) → Mastered · Needs more practice · Learning gap · Not yet studied → 지나온 학습 결손을 찾아 채움(체크), 지도의 선을 따라 올라가는 파란 화살표(Next) |
| 10 | [11] Four key benefits | change1–4 | l11_1–6 | 2×2 카드가 한 장씩 채워지고, 읽는 카드에 손그림 상자와 체크, "Compared with their own past, not with others" |
| 11 | [12] Closing | outro | l12_1–4 | 왼쪽 그림(50 years of learning design expertise → knowledge AI can understand and use, STARTING POINT), 오른쪽 글(JEI’s own AI personalized learning platform, A new global standard for AI-powered math learning) |

## 대본 · 음성 · 시각표

- `tools/script.py`: 대본(`_SCRIPT`, 받은 영문 대본 그대로 — "Now," 앞의 빈칸만 지움), 장면 목록(`SCENES`), 같은 종이 장면(`CONT`), 읽는 형태(`SAY`), 테이크 고정(`TAKE`), 간격
  - 읽는 형태: 검토(2026.11.05) 요청으로 POD → "P-O-D", JEI → "J-E-I"(한 글자씩, 그냥 두면 "pod" 처럼 읽혀요), JEI-SLI → "J-E-I S-L-I", 50 years → "fifty years". 화면 · 자막은 쓰는 형태 그대로예요
- 목소리(2026.11.06 검토로 교체): `audio/voice_ref.wav` = `../jei-corporation-overview-female/audio/voice_ref.wav`(어댑티브진단 영상 `../adaptive-diagnosis-v2/audio/narration.mp3` 14.1–28.95초, 여자 영어 목소리). DGX Qwen3-TTS(`http://192.168.51.8:8095`, `/v1/tts/clone`)가 문장마다 3번 읽고, whisper large-v3-turbo(mlx-whisper)로 받아써서 골라요. 줄 끝을 잘라먹지 않게 "Thank you." 를 붙여 읽히고 그 앞 쉼에서 잘라요
- 확인(2026.11.06): 고른 62개 테이크 모두 받아쓰기가 대본과 같고(`miss 0`), 끝 무음 0.23초 이상이에요. wav2vec2 음소(`facebook/wav2vec2-lv-60-espeak-cv-ft`)로 문장마다 마지막 단어까지 읽힌 것을 확인했고, JEI 는 모두 "dʒ eɪ iː aɪ", POD 는 모두 "p iː oʊ d iː"(한 글자씩)예요. 목소리 높이(Praat F0)는 문장마다 중간값 189–255Hz(전체 가운데 214Hz)로 갑자기 낮아진 테이크는 없어요. 마지막 문장 l12_4 는 10번 읽혀도 모두 "learn-" 을 낮게 긁고 "-ing" 에서 올라가서, "-ing" 262 → 244Hz 에서 끝까지 105Hz 로 내려가는 0번을 `TAKE` 에 고정했어요. 다시 읽힌 테이크 때문에 다른 문장의 선택이 바뀌지 않게 `PACE = 14.82` 로 고정했어요
- 첫 문장은 1.3초에 시작하고(0.25초에 차임), 문장 사이 0.5초, 쪽 사이 1.6초. 마지막 문장 뒤에 같은 차임이 울려요

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts                    # → timeline.js, audio/mix.wav, subtitles.srt
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l5_1     # 그 문장만 8번 새로 읽기
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.outro`(한국어판과 같은 구조, 문구와 큐 단어만 영어). 제목 · 마무리 문구와 색은 `content.js`(영상 편집기에서도 수정 가능)
- 미리보기: `index.html`(재생 막대), `index.html?t=120`(그 시각)

```bash
node tools/snap.mjs out/snaps --ends              # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                        # out/jei_ai_vision.mp4 (GPU: Chrome Metal + WebCodecs H.264)
node render.mjs --workers 3 --only 99-115,217-end  # 고친 구간(초)만 다시 그리고 나머지는 기존 영상에서 가져와요
# 검토 2026.11.06(목소리 교체 · p. 2 삭제 · p. 7 POD 새 배치 · 쪽 넘김 소리 없음): 전체 렌더 → out/jei_ai_vision_ver3.mp4 (ver2 = 그 전)
```
