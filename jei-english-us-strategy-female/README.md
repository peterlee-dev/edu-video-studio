# JEI English 미주 개발 방향 및 전략 · 여자 목소리 (모눈종이 워크북)

`../jei-english-us-strategy`(남자 목소리)와 화면 · 대본이 같고 목소리만 다른 판이었어요. 1차 검토(`JEI소개영상 피드백 2026.10.30 - 3. 전략영상_1차.pdf`)는 이 여자 목소리 판에만 반영해서, 지금은 대본 · 화면이 남자 목소리 판과 달라요(아래 **1차 검토 반영**).

영어팀 장표 `1. [미주 공유용] 미주 JEI 영어 개발 방향 및 전략_v3_261105.pdf`(22쪽)와 영문 대본 `미주 지사 공유 문건 스크립트 - 1-2. [ENG, 1차] 미주 영어 기획(안).pdf`(ENG_Short Version, 178문장)로 만든 영상이에요(16분 55초). 대본은 1차 · 2차 · 3차 검토에서 바꾼 문장 말고는 한 글자도 바꾸지 않았어요(문해력 쪽 마지막 문장 끝의 마침표 두 개만 하나로). 장표의 한글 문구는 대본에 맞춰 영어로 옮겼고, 화면은 `../jei-english-us-plan` · `../ai-learning-platform-v3` 와 같은 **모눈종이 워크북** 콘셉트예요(`.claude/skills/graph-paper-video`).

- **모눈종이 워크북 한 장**: 장면 62개, 쪽 39장(p. 1 ~ p. 39). 장면이 바뀔 때 종이 위를 옆으로 넘어가고(믹스의 휙 소리와 같은 때), 읽는 동안은 화면이 움직이지 않아요. 같은 그림을 이어 쓰는 장면(NCTE, 3C, SWOT, Ansoff, 타깃 학년, 포지셔닝 맵, 고객 여정, 4P, 2단계 상품, AI 4영역, Next steps, 학습 화면, 3단계)은 쪽 넘김 없이 바뀌는 부분만 겹쳐 바뀌어요(`CONT`)
- 선생님 펜 표시: 빨간 동그라미 · 체크 · 밑줄 · 손그림 상자 · 화살표, 네이비 ✗, 형광펜, 포스트잇, 도장(NEW APPROACH, KEY POSITION)
- 색: `수학 영상 컬러 개선.pdf` 기준(레드 `#E5303A` 메인, 네이비 부정 · 하락, 비교는 레드 → 블루 → 민트, 나머지 그레이). 팔레트는 `content.js` 의 `colors`
  - NAEP 하락(−5점, 학년별 선)과 약점 · 위협, "부모에게 잘 보이지 않음"은 네이비
  - 3C: 고객 블루 · 경쟁사 그레이 · 자사 레드 / SWOT: 강점 레드 · 기회 블루 · 약점 · 위협 네이비 / 포지셔닝 맵: JEI 레드, Kumon 블루, 나머지 그레이
  - "Read → Understand → Decide → Express" 계단은 레드 한 가지의 진하기(그레이 → 블러시 → 라이트 레드 → 레드)
- 진단 용어는 화면 · 음성 모두 precise assessment 하나로 써요(1차 검토. "a more detailed product plan" 은 진단이 아니라 그대로)
- 1920×1080, 30fps. 글꼴은 macOS 시스템 글꼴 Avenir Next(본문) · Noteworthy(손글씨). 배경음악 없음 (내레이션 + 쪽 넘김 휙 소리, 끝인사 딩)
- 화면에 자막은 넣지 않아요. 필요하면 `subtitles.srt`

| p. | 장면 | 문장 | 화면 |
|---|---|---|---|
| 1 | title | l1_1 | 제목, 새 프로그램의 네 요소(문해력 · 정밀 진단 · 개인 맞춤 · 성장 확인)가 체크되는 워크시트 |
| **01** | | | **Development direction** (장표 2–3쪽) |
| 2 | goal | l2_1–3 | 새 프로그램(문해력 발달 중심) · 문해력 콘텐츠만 더하는 것 ✗ · 지금 프로그램의 기초, 네 요소 → One cohesive learning experience |
| 3 | beyond | l2_5–6 | Read → Understand → Decide → Express 계단 |
| 4 | path | l2_7–8 | 정밀 진단 → 개인별 학습 경로 → 학습 결과 → 성장 확인 |
| 5 | literacy | l3_1–3 | Reading comprehension 을 품은 Literacy 원, 포함하는 세 가지 |
| 6 | connect | l3_4–6 | Phonics · Vocabulary · Grammar 묶음 ⇒ Reading · Writing · Thinking 묶음, 교과 학습 포스트잇 |
| **02** | | | **Education & market** (장표 4–7쪽) |
| 7 | ncte · ncteNext · ncteJei | l4_1–7 | 한 장: 지난 10년 / 다음 10년(AI agents), 아래에 JEI English 방향 |
| 8 | naep | l5_1–2 | NAEP Proficient 비율 선 그래프(2019 · 2022 · 2024, 장표 숫자), about 30% · 10명 중 3명 |
| 9 | naepDrop | l5_3–4 | 평균 점수 220 → 215, 263 → 258(−5), 맺음 띠 |
| 10 | parents | l6_1–2 | 학부모의 바람(말풍선) ↔ JEI 강점, 그 사이 "not always clear to parents" |
| 11 | address | l6_3–5 | 온라인 Adaptive 진단 · 학습 로드맵 · 학습목표별 리포트 |
| 12 | opportunity | l7_1–4 | $10B+ · 19% 24%(같은 크기) · $333(장표 숫자), 기회 띠 |
| **03** | | | **Competition & analysis** (장표 8–12쪽) |
| 13 | rivals | l8_1–5 | Kumon · Eye Level · Best Brains · Huntington 표, JEI 는 "which direction?" |
| 14 | standOut | l8_6–7 | 반복 학습 · 시험 점수 · 가격 ✗ → 정밀 진단 |
| 15 | showWhat | l8_8–9 | 세 가지 질문 → 진단 · 학습 경로 · 성장 증거 연결 |
| 16 | slogan | l8_10–11 | Accurate Assessment, Clear Growth. (음성은 "…assessment and clear growth.") |
| 17 | hospital | l8_12–14 | CT · MRI 병원 여섯 곳 중 진단 전문 병원 → JEI English (음성은 2차 검토의 "Think about hospitals." 비유) |
| 18 | c3cust · c3comp · c3jei | l9_1–12 | 한 장에 고객 · 경쟁사 · 자사 세 칸이 차례로 |
| 19 | c3plan | l9_13–16 | KEEP · STRENGTHEN · SHOW, 시장 포지션 띠 |
| 20 | bench | l10_1–5 | Amplify · Lexia · i-Ready · IXL 표 |
| 21 | benchJei | l10_6–9 | 문해력만 차별점 ✗, 네 요소의 합 = 다른 학습 경험 |
| 22 | benchNext | l10_10–11 | 상세 조사 → JEI 고유 강점 → 상세 상품 계획 |
| 23 | swotS · swotW · swotO · swotT · swotSum | l11_1–14 | 한 장의 SWOT 네 칸, 아래 방향 띠 |
| 24 | ansoff · ansoffPD | l12_1–6 | Ansoff 2×2, Product Development ✓, NEW APPROACH 도장(잉크색) |
| **04** | | | **Target & positioning** (장표 13–16쪽) |
| 25 | target · targetWhy | l13_1–5 | Pre-K ~ G9 띠에서 G3–G6, 아래에 그 이유 |
| 26 | posMap ~ posMove | l14_1–22 | 한 장의 포지셔닝 맵(장표의 점 위치), 오른쪽 카드만 바뀜: 두 기준 → 가로축 → 세로축 → JEI(4사분면) → Kumon(3사분면) → 시장 변화 → 4 → 1사분면 |
| 27 | position | l14_23–26 | Accurate Assessment, Clear Growth + 하나로 이어진 학습 경험, KEY POSITION |
| 28 | journey · journeyFix | l15_1–5 | 일곱 단계 고객 여정, 학부모가 필요한 것(네이비) → 개선(레드) |
| 29 | fourP · fourP2 | l16_1–5 | Product · Price · Place · Promotion 카드 |
| **05** | | | **Product & next steps** (장표 17–22쪽) |
| 30 | step1 · step2 | l17_1–5 | STEP 1 POD + 기존 교재(블루) → STEP 2 온라인 + POD(레드) |
| 31 | ai1 · ai2 | l18_1–6 | AI Tutor · 분석 · POD 스캔 · 콘텐츠 개발 |
| 32 | direction | l19_1–3 | 방향 띠, 기존 콘텐츠 개선 ✗, 네 요소를 한 프로그램으로 |
| 33 | nextA · nextB | l19_4–10 | Next steps 01–04 |
| 34 | summary | l19_11–12 | 최종 방향 띠, 학습 결과 · 성장 막대 |
| 35 | ccss | l20_1–3 | 50개 주 칸, 39개 주가 원래 CCSS 를 그대로 쓰지 않음(장표의 11 · 24 · 11 · 4) |
| 36 | ccssPlan | l20_4–6 | 다섯 주 카드, 공통 ELA & Literacy 구조 + 주별 기준 → 진단 · 학습 경로 |
| 37 | platform · platform2 | l21_1–6 | 학습 화면(프로그램 · 국가 · 주 · 언어 → Adaptive Assessment → POD · 온라인 · 둘 다), 글로벌 플랫폼 |
| 38 | three · adaptive | l22_1–5 | 세 단계(학습 기준 → 진단 → 학습 경로)와 오른쪽 화면, Adaptive Learning 고리 |
| 39 | outro | l22_6 | 요약 세 줄, Thank you |

## 음성 · 시각표 만들기

- 대본: `tools/script.py`. 읽는 문장을 따로 둔 곳: NCTE → "N-C-T-E", CCSS → "C-C-S-S", ELA → "E-L-A", POD → "P-O-D", IXL → "I-X-L", l8_1 의 JEI → "J-E-I"(그냥 두면 8번 모두 "JE" 로 들림), CT · MRI → "C-T", "M-R-I", 3C → "three C", 4P → "four P"
- 목소리: `tts` 모드. `audio/voice_ref.wav` 는 `../adaptive-diagnosis-v2/audio/narration.mp3` 의 14.1–28.7초(여자 영어 목소리, `../jei-english-us-plan` 과 같은 샘플)예요. DGX Qwen3-TTS(`http://192.168.51.8:8095`)가 이 목소리를 복제해 문장마다 3번 읽고, whisper 로 받아써 대본대로 읽은 것 중 고르게 읽고 끝이 잘리지 않은 것을 골라요(`audio/tts_cache/`). 속도는 1.0배
- 발음 확인: whisper 는 잘못 읽은 단어를 고쳐 적기도 해서, 문장 끝 단어와 약어를 `facebook/wav2vec2-lv-60-espeak-cv-ft` 음소로 다시 확인했어요
  - 이 목소리는 서버가 준 길이 안에서 마지막 단어를 삼키는 일이 잦아요(growth → "gro", period → "p"). 끝 단어 음소로 끝까지 읽은 테이크를 골라 `tools/script.py` 의 `TAKE` 에 고정했어요(13문장)
  - 원인으로 보이는 것: `audio/voice_ref.wav` 가 "questions" 의 마지막 s 에서 바로 끝나요(쉼 없음). 끝에 0.25초 쉼을 둔 14.1–28.95초 샘플로 시험하면 잘림이 줄어요. `l14_5` 는 지금 샘플로 16번 모두 잘려서 그 샘플로 읽은 테이크(8번)를 넣었어요. 다음에 전체를 새로 읽을 때는 샘플을 그것으로 바꾸는 게 좋아요(모든 문장을 다시 읽게 돼요)
  - JEI 가 문장 첫머리에서 "JE" · "J.I." 로 들린 `l6_2`, `l9_10`, `l9_13`, `l12_4` 는 읽는 문장을 "J-E-I" 로. `l20_3` 은 whisper 가 "used their" 로 적지만 음소는 "use their" 예요

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts   # timeline.js, audio/mix.wav, subtitles.srt
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l3_2   # 한 문장만 다시 읽기
```

## 1차 검토 반영 (`JEI소개영상 피드백 2026.10.30 - 3. 전략영상_1차.pdf`, 여자 목소리 판만)

| # | 고친 것 |
|---|---|
| 1 | p.6 connect: 일대일 화살표 대신 Phonics · Vocabulary · Grammar 를 묶은 괄호 ⇒ Reading · Writing · Thinking 을 묶은 괄호 |
| 2 | p.24 Ansoff: NEW APPROACH 도장을 잉크색(`K.ink`)으로 (빨간 카드 위에서 보이게) |
| 3 | p.7 NCTE: "Understanding information carefully" → "Reading and evaluating texts critically" (화면 · 음성 `l4_3`) |
| 4 | p.12 시장 기회: + 표시 없이 19% · 24% 같은 크기, "TUTORING USE AND INTEREST AMONG PARENTS", "19% using, 24% interested (2025.10)" |
| 5–7 | p.31 AI: "Offline → Online"(한 방향), 콘텐츠 개발 아이콘을 문서 + AI 반짝임으로, "Offline results / → online learning data" 두 줄(같은 크기, 같은 시작점) |
| 8 | p.33 Next steps 03: "→ comprehension, inference, critical evaluation, expression" (음성은 그대로) |
| 9 | p.35 CCSS: "do not use the CCSS as originally written", 항목 문구 넷, 음성 `l20_3` "…39 use either modified versions of the CCSS or independently developed ELA standards." |
| 10 | 학습 화면 첫 칸 "Elementary (G1–6)"는 장표 21쪽 그대로 둠 (학년군에 따른 프로그램 선택) |
| 11 | detailed assessment → precise assessment (음성 12문장, 화면 전부). "a more detailed product plan" 은 그대로 |
| 12 | p.2 · p.3 을 한 쪽(p.2 `goal`, `l2_1–3`)으로 합치고 시트의 수정 대본으로 다시 읽음. 이후 쪽 번호가 하나씩 당겨짐 |
| 13 | p.30 Step 2: "Online, POD workbooks, Both" 칩 사이 콤마 |
| 추가 | 0:08 첫 문장 끝 "U.S." 잘림: 다시 읽음 |

- 바뀐 문장 18개(첫 문장 포함)는 "문장 + Thank you." 로 읽혀 그 사이 쉼에서 자른 테이크예요(서버가 문장 끝을 자르는 문제, `geo-monitor-ko` 의 방식). 샘플은 끝에 쉼이 있는 14.1–28.95초. 고른 테이크는 `TAKE`

## 2차 검토 반영 (`JEI소개영상 피드백 2026.10.30 - 전략영상_2차.pdf`)

| # | 고친 것 |
|---|---|
| 1 | 3:36 `l7_2` "…extra education." 끝 잘림: 다시 읽음 |
| 2 | 0:56 `l2_8` "learning path" 의 th 잘림: 다시 읽음 (path 를 /p æ θ/ 로 끝까지 읽은 테이크) |
| 3 | p.2 `goal`: 화면 "foundational language + basic literacy skills", "One integrated learning experience". 음성 `l2_3` "…foundational language and basic literacy skills, … into one integrated learning experience." |
| 4 | p.16 `l8_11` 음성만 "Accurate Assessment and Clear Growth." (끝음이 내려가는 테이크, 208 → 162 Hz). 화면은 그대로 |
| 5 · 8 | 13:30 `l18_3` "student progress" 끝 잘림, processes 를 -eez 로 읽음: -iz 로 읽고 끝까지 읽은 테이크 |
| 6 | p.17 `hospital` 음성만 시트의 수정안 세 문장으로(`l8_12–14`, "Think about hospitals." …). 화면은 그대로, CT · MRI 칩은 새 `l8_13` 에 맞춤. 시트 문구대로 "precise diagnosis", "diagnostic specialists" 를 씀. `l8_14` 의 JEI 는 "J.I." · "JE" 로 들려 읽는 문장을 "J-E-I" 로 |
| 7 | 10:54 `l14_15` "…repeated practice." 끝 잘림: 다시 읽음 |
| 9 | 16:56 `l22_5` "…their progress." 끝 잘림: 다시 읽음 |

- 1차와 같은 방식(14.1–28.95초 샘플, "문장 + Thank you." 를 읽혀 그 사이 쉼에서 자름)으로 10문장을 5~6번씩 읽고, 끝 단어 음소와 끝 쉼(0.2초 이상)으로 골라 `TAKE` 에 고정했어요. 길이가 바뀌어 전체를 다시 렌더했어요

## 3차 검토 반영

| # | 고친 것 |
|---|---|
| 1 | 16:51 `l22_5` "…based on their progress." 끝음이 올라감(2차에서 고른 테이크, progress 192 → 337 Hz) → 끝음이 내려가는 테이크(209 → 168 Hz, /s/ 까지 읽고 0.23초 쉼) |
| 2 | 5:56 p.18 `c3jei` 화면 "not yet clearly shown / to parents", 음성 `l9_12` "…are not yet clearly shown to parents." (communicated → shown, 같은 방식으로 6번 읽어 끝음이 내려가는 테이크) |

- `l9_12` 가 0.85초 짧아져 그 뒤가 당겨졌어요. 353초 앞은 시각이 그대로라 `--only 353-end` 로 다시 렌더

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.outro`, 제목 · 마무리 문구와 색: `content.js` (영상 편집기에서도 수정 가능)
- 미리보기: `index.html` (재생 막대), `index.html?t=120` (그 시각)

```bash
node tools/snap.mjs out/snaps --ends            # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                      # out/jei_english_us_strategy_female.mp4 (GPU 렌더)
node render.mjs --workers 3 --only 99-115,217-end   # 고친 구간(초)만 다시 그리고 나머지는 기존 영상에서 가져와요
```
