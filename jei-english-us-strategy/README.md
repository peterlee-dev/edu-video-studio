# JEI English 미주 개발 방향 및 전략 (모눈종이 워크북)

영어팀 장표 `1. [미주 공유용] 미주 JEI 영어 개발 방향 및 전략_v3_261105.pdf`(22쪽)와 영문 대본 `미주 지사 공유 문건 스크립트 - 1-2. [ENG, 1차] 미주 영어 기획(안).pdf`(ENG_Short Version, 178문장)로 만든 영상이에요(17분 43초). 대본은 한 글자도 바꾸지 않았어요(문해력 쪽 마지막 문장 끝의 마침표 두 개만 하나로). 장표의 한글 문구는 대본에 맞춰 영어로 옮겼고, 화면은 `../jei-english-us-plan` · `../ai-learning-platform-v3` 와 같은 **모눈종이 워크북** 콘셉트예요(`.claude/skills/graph-paper-video`).

- **모눈종이 워크북 한 장**: 장면 63개, 쪽 40장(p. 1 ~ p. 40). 장면이 바뀔 때 종이 위를 옆으로 넘어가고(믹스의 휙 소리와 같은 때), 읽는 동안은 화면이 움직이지 않아요. 같은 그림을 이어 쓰는 장면(NCTE, 3C, SWOT, Ansoff, 타깃 학년, 포지셔닝 맵, 고객 여정, 4P, 2단계 상품, AI 4영역, Next steps, 학습 화면, 3단계)은 쪽 넘김 없이 바뀌는 부분만 겹쳐 바뀌어요(`CONT`)
- 선생님 펜 표시: 빨간 동그라미 · 체크 · 밑줄 · 손그림 상자 · 화살표, 네이비 ✗, 형광펜, 포스트잇, 도장(NEW APPROACH, KEY POSITION)
- 색: `수학 영상 컬러 개선.pdf` 기준(레드 `#E5303A` 메인, 네이비 부정 · 하락, 비교는 레드 → 블루 → 민트, 나머지 그레이). 팔레트는 `content.js` 의 `colors`
  - NAEP 하락(−5점, 학년별 선)과 약점 · 위협, "부모에게 잘 보이지 않음"은 네이비
  - 3C: 고객 블루 · 경쟁사 그레이 · 자사 레드 / SWOT: 강점 레드 · 기회 블루 · 약점 · 위협 네이비 / 포지셔닝 맵: JEI 레드, Kumon 블루, 나머지 그레이
  - "Read → Understand → Decide → Express" 계단은 레드 한 가지의 진하기(그레이 → 블러시 → 라이트 레드 → 레드)
- 화면 용어는 그 쪽 내레이션을 따라요: 대본이 precise assessment 와 detailed assessment 를 섞어 쓰므로 화면도 쪽마다 대본과 같은 말
- 1920×1080, 30fps. 글꼴은 macOS 시스템 글꼴 Avenir Next(본문) · Noteworthy(손글씨). 배경음악 없음 (내레이션 + 쪽 넘김 휙 소리, 끝인사 딩)
- 화면에 자막은 넣지 않아요. 필요하면 `subtitles.srt`

| p. | 장면 | 문장 | 화면 |
|---|---|---|---|
| 1 | title | l1_1 | 제목, 새 프로그램의 네 요소(문해력 · 정밀 진단 · 개인 맞춤 · 성장 확인)가 체크되는 워크시트 |
| **01** | | | **Development direction** (장표 2–3쪽) |
| 2 | goal | l2_1–2 | 지금의 JEI English(문법 · 어휘 · 읽기) → 문해력을 키우는 새 프로그램 |
| 3 | oneExp | l2_3–4 | 콘텐츠 추가 · 기존 개선 ✗, 네 요소 → One learning experience |
| 4 | beyond | l2_5–6 | Read → Understand → Decide → Express 계단 |
| 5 | path | l2_7–8 | 정밀 진단 → 개인별 학습 경로 → 학습 결과 → 성장 확인 |
| 6 | literacy | l3_1–3 | Reading comprehension 을 품은 Literacy 원, 포함하는 세 가지 |
| 7 | connect | l3_4–6 | Phonics · Vocabulary · Grammar → Reading · Writing · Thinking, 교과 학습 포스트잇 |
| **02** | | | **Education & market** (장표 4–7쪽) |
| 8 | ncte · ncteNext · ncteJei | l4_1–7 | 한 장: 지난 10년 / 다음 10년(AI agents), 아래에 JEI English 방향 |
| 9 | naep | l5_1–2 | NAEP Proficient 비율 선 그래프(2019 · 2022 · 2024, 장표 숫자), about 30% · 10명 중 3명 |
| 10 | naepDrop | l5_3–4 | 평균 점수 220 → 215, 263 → 258(−5), 맺음 띠 |
| 11 | parents | l6_1–2 | 학부모의 바람(말풍선) ↔ JEI 강점, 그 사이 "not always clear to parents" |
| 12 | address | l6_3–5 | 온라인 Adaptive 진단 · 학습 로드맵 · 학습목표별 리포트 |
| 13 | opportunity | l7_1–4 | $10B+ · 19% +24% · $333(장표 숫자), 기회 띠 |
| **03** | | | **Competition & analysis** (장표 8–12쪽) |
| 14 | rivals | l8_1–5 | Kumon · Eye Level · Best Brains · Huntington 표, JEI 는 "which direction?" |
| 15 | standOut | l8_6–7 | 반복 학습 · 시험 점수 · 가격 ✗ → 정밀 진단 |
| 16 | showWhat | l8_8–9 | 세 가지 질문 → 진단 · 학습 경로 · 성장 증거 연결 |
| 17 | slogan | l8_10–11 | Accurate Assessment, Clear Growth. |
| 18 | hospital | l8_12–14 | CT · MRI 병원 여섯 곳 중 진단 전문 병원 → JEI English |
| 19 | c3cust · c3comp · c3jei | l9_1–12 | 한 장에 고객 · 경쟁사 · 자사 세 칸이 차례로 |
| 20 | c3plan | l9_13–16 | KEEP · STRENGTHEN · SHOW, 시장 포지션 띠 |
| 21 | bench | l10_1–5 | Amplify · Lexia · i-Ready · IXL 표 |
| 22 | benchJei | l10_6–9 | 문해력만 차별점 ✗, 네 요소의 합 = 다른 학습 경험 |
| 23 | benchNext | l10_10–11 | 상세 조사 → JEI 고유 강점 → 상세 상품 계획 |
| 24 | swotS · swotW · swotO · swotT · swotSum | l11_1–14 | 한 장의 SWOT 네 칸, 아래 방향 띠 |
| 25 | ansoff · ansoffPD | l12_1–6 | Ansoff 2×2, Product Development ✓, NEW APPROACH 도장 |
| **04** | | | **Target & positioning** (장표 13–16쪽) |
| 26 | target · targetWhy | l13_1–5 | Pre-K ~ G9 띠에서 G3–G6, 아래에 그 이유 |
| 27 | posMap ~ posMove | l14_1–22 | 한 장의 포지셔닝 맵(장표의 점 위치), 오른쪽 카드만 바뀜: 두 기준 → 가로축 → 세로축 → JEI(4사분면) → Kumon(3사분면) → 시장 변화 → 4 → 1사분면 |
| 28 | position | l14_23–26 | Accurate Assessment, Clear Growth + 하나로 이어진 학습 경험, KEY POSITION |
| 29 | journey · journeyFix | l15_1–5 | 일곱 단계 고객 여정, 학부모가 필요한 것(네이비) → 개선(레드) |
| 30 | fourP · fourP2 | l16_1–5 | Product · Price · Place · Promotion 카드 |
| **05** | | | **Product & next steps** (장표 17–22쪽) |
| 31 | step1 · step2 | l17_1–5 | STEP 1 POD + 기존 교재(블루) → STEP 2 온라인 + POD(레드) |
| 32 | ai1 · ai2 | l18_1–6 | AI Tutor · 분석 · POD 스캔 · 콘텐츠 개발 |
| 33 | direction | l19_1–3 | 방향 띠, 기존 콘텐츠 개선 ✗, 네 요소를 한 프로그램으로 |
| 34 | nextA · nextB | l19_4–10 | Next steps 01–04 |
| 35 | summary | l19_11–12 | 최종 방향 띠, 학습 결과 · 성장 막대 |
| 36 | ccss | l20_1–3 | 50개 주 칸, 39개 주(장표의 11 · 24 · 11 · 4) |
| 37 | ccssPlan | l20_4–6 | 다섯 주 카드, 공통 ELA & Literacy 구조 + 주별 기준 → 진단 · 학습 경로 |
| 38 | platform · platform2 | l21_1–6 | 학습 화면(프로그램 · 국가 · 주 · 언어 → Adaptive Assessment → POD · 온라인 · 둘 다), 글로벌 플랫폼 |
| 39 | three · adaptive | l22_1–5 | 세 단계(학습 기준 → 진단 → 학습 경로)와 오른쪽 화면, Adaptive Learning 고리 |
| 40 | outro | l22_6 | 요약 세 줄, Thank you |

## 음성 · 시각표 만들기

- 대본: `tools/script.py`. 읽는 문장을 따로 둔 곳: NCTE → "N-C-T-E", CCSS → "C-C-S-S", ELA → "E-L-A", POD → "P-O-D", IXL → "I-X-L", l8_1 의 JEI → "J-E-I"(그냥 두면 8번 모두 "JE" 로 들림), CT · MRI → "C-T", "M-R-I", 3C → "three C", 4P → "four P"
- 목소리: `tts` 모드. `audio/voice_ref.wav` 는 `../ai-learning-platform-v3/audio/voice_ref.wav`(D–I 개선 내레이션 29초, 남자 영어 목소리)를 그대로 쓴 것이에요. DGX Qwen3-TTS(`http://192.168.51.8:8095`)가 이 목소리를 복제해 문장마다 3번 읽고, whisper 로 받아써 대본대로 읽은 것 중 고르게 읽고 끝이 잘리지 않은 것을 골라요(`audio/tts_cache/`). 속도는 1.0배
- 발음 확인: whisper 는 잘못 읽은 단어를 고쳐 적기도 해서, 문장 끝 단어와 약어(JEI · POD · NCTE · CCSS · ELA · IXL · comprehension)를 `facebook/wav2vec2-lv-60-espeak-cv-ft` 음소로 다시 확인했어요. `l20_3` 은 whisper 가 "used their" 로 적지만 음소는 "use their"(j uː z ð ɛ ɹ)예요. make_audio 의 "끝이 잘림" 경고는 이 목소리의 바닥 잡음(-40~-50 dB) 때문에 대부분 오탐이에요(끝 단어 음소로 확인)

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts   # timeline.js, audio/mix.wav, subtitles.srt
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l3_2   # 한 문장만 다시 읽기
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.outro`, 제목 · 마무리 문구와 색: `content.js` (영상 편집기에서도 수정 가능)
- 미리보기: `index.html` (재생 막대), `index.html?t=120` (그 시각)

```bash
node tools/snap.mjs out/snaps --ends            # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                      # out/jei_english_us_strategy.mp4 (GPU 렌더)
node render.mjs --workers 3 --only 99-115,217-end   # 고친 구간(초)만 다시 그리고 나머지는 기존 영상에서 가져와요
```
