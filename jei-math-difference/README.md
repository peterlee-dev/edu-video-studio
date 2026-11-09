# JEI Math: Three Strengths That Make a Difference (재능스스로수학, 차이를 만드는 세 가지 경쟁력 영문판)

`../jei-math-difference-ko`(한국어판 ver6, 18쪽)의 영문판이에요. 대본은 2026.11.06에 받은 영문 대본(18씬)이고 한 글자도 바꾸지 않았어요. 화면은 한국어판과 같은 18쪽 · 같은 그림 배치를 영어 문구로 옮긴 것이고, 목소리는 한국어판처럼 여자 목소리(영어)예요. 디자인 시스템도 같아요(`.claude/skills/graph-paper-video`).

- **모눈종이 워크북 한 장**: 씬 하나 = 워크북 한 쪽(p. 1 ~ p. 18, 씬 번호 = 쪽 번호). 쪽이 바뀔 때만 종이가 옆으로 0.73초 동안 넘어가요(소리 없음, ver4). 그림 · 펜 표시는 내레이션 단어에 맞춰 하나씩 나타나요(`Wc(문장, 단어)`, 큐 단어는 영어)
- **교재 사진**: 한국어판 `assets/photos/` 와 같은 파일이에요. 재능 · Eye Level 교재 쪽과 분석표는 원래 영문판 교재라 그대로 써요. 구몬 자료는 ver2(2026.11.06)부터 `재능수학 특장점 영상 수정사항.pdf`(2쪽)의 영문판이에요: 교재 3쪽(`kumon_1.jpg` 2A1a Add · `kumon.jpg` C32a Multiplication · `kumon_3.jpg` F108a Four Operations, PDF 안 이미지 그대로)과 Kumon North America P3 테스트 결과표(`diag_kumon.jpg`, "8 / 67" 손글씨와 빨간 점선이 PDF 위에 얹혀 있어 300dpi 로 그린 쪽에서 잘라냄). p. 11 의 결과표 사진 폭과 그래프 동그라미는 새 그림에 맞췄어요. 학습기능별 분석 표(`func_table.jpg`)의 "(26번)" 은 "(#26)" 으로 고쳤어요
- **ver3(2026.11.06 수정사항.pdf 11쪽)**: 화면 문구만 고쳤어요(p. 2 · 5 · 6 · 8 · 9 · 11 · 12 · 13 · 14 · 15 · 16, 아래 쪽 표에 반영). 내레이션 · 시각표는 그대로라 길이도 같고, 바뀐 구간(28.5–32.6 · 65.8–100.7 · 127.5–134.8 · 184.5–239.4 · 262.5–455.3초)만 다시 렌더했어요
- **ver4(2026.11.06 재능수학 특장점 영상 수정사항.pdf 5쪽 + 새 영문 대본)**: 비교 상대 이름을 익명으로 바꿨어요. 대본 5문장(l5_1 · l11_2 = Program A, l8_4 · l9_4 · l11_4 = program B, 받은 대본 그대로 소문자)을 다시 읽히고, 화면도 Kumon Math → Program A, Eye Level Math → Program B, p. 11 부제는 How other math programs determine starting points 로. 구몬 교재 3쪽은 PDF 5쪽처럼 위쪽 KUMON 로고를 흰색으로 지웠어요(옆의 © 문구는 PDF 그대로 둠). 쪽 넘김 휙 소리를 빼고(`script.py` `WHOOSH = False`) 넘김을 1.5배 빠르게(`index.html` `TR` 1.1 → 0.73초). 다른 문장의 테이크가 바뀌지 않게 `PACE = 15.44` 로 고정
- **ver5(2026.11.06 재능수학 특장점 영상 수정사항.pdf 3쪽)**: 부제 세 개만 고쳤어요. p. 5 How Program A is organized → A look at another math learning program: Program A, p. 8 → How JEI Math and another math learning program (Program B) introduce addition, p. 9 → How JEI Math and Program B approach division. 내레이션 · 시각표는 그대로라 길이도 같고, 그 구간(66.8–101.6 · 141.6–240.1초)만 다시 렌더했어요
- 선생님 펜 표시 · 색은 한국어판과 같아요(`content.js` 의 `colors`). 레드가 메인, 비교 상대(Program A · Program B · Learner B)는 블루, 세 가지 경쟁력은 레드 → 블루 → 민트, 네이비는 오답과 "limited" 에만
- 도장: TARGETED(p. 13) · FOCUSED(p. 14) · COMPLETE MASTERY(p. 18)
- 글꼴: 본문 Avenir Next(시스템), 손글씨 Noteworthy(시스템, `../jei-ai-vision` 과 같음)
- 길이 8분 19.8초(499.75초), 말 빠르기 약 15.4자/초. 1920×1080, 30fps. 배경음악 없음(내레이션 + 시작과 끝의 오르는 4음 차임, 쪽 넘김 소리는 ver4 에서 뺌). 화면 자막 없음(`subtitles.srt` 따로)

| p. | 씬 | 장면 | 문장 | 화면 |
|---|---|---|---|---|
| 1 | 1 Opening | title | l1_1–2 | JEI MATH 칩, JEI Math: / Three Strengths That / Make a Difference, 표지 사진, ① Comprehensive content ② Systematic progression ③ Precise diagnosis |
| 2 | 2 Introduction | intro | l2_1–2 | What do students learn? · How do they learn? · How are they assessed? 카드 셋, 맺음 띠(It's not how many problems students solve, but **how their learning is structured**.) |
| 3 | 3 Three Key Advantages | pillars | l3_1–4 | JEI Math 지붕 아래 기둥 셋이 First · Second · Third 에 맞춰 올라서고, 오른쪽에 세 가지 강점 |
| 4 | 4 Transition | t1 | l4_1 | STRENGTH 1. Range of Mathematical Content |
| 5 | 5 Program A | kumon | l5_1–3 | 제목 Program A primarily focuses on numbers and operations., 부제 A look at another math learning program: Program A, 칩 Program A, 구몬 교재 3쪽(로고 지움), Numbers and operations 블루 밑줄, Repeated calculation practice · Accuracy and speed → Less exposure to other areas, limited broader problem-solving(네이비) |
| 6 | 6 JEI Math | areas | l6_1–3 | 다섯 영역 교재 사진(Numbers and operations · Geometry · Measurement · Data and graphs · Patterns), Computation + Logical thinking + Mathematical connections + Problem-solving → Well-rounded math skills |
| 7 | 7 Transition | t2 | l7_1 | STRENGTH 2. How Concepts Are Taught |
| 8 | 8 Addition | addition | l8_1–6 | 덧셈 교재 3쪽씩(Concrete situations → Addition activities → Addition equations / Equations first → Concrete objects → Meaning of addition), 파란 손글씨 "Calculation before the meaning of addition"(칩 Program B), 강점 상자(From **concrete experiences** to **conceptual understanding**, then to addition equations.) |
| 9 | 9 Division | division | l9_1–5 | 제목 Division: Understanding One Concept in Multiple Ways, 나눗셈 교재 3쪽씩(Grouping objects · Skip-counting · Repeated subtraction, 빨간 상자 "Connected to one mathematical principle" / Program B: Procedures · Practice), 강점 상자(A systematic learning progression from **conceptual understanding** to **application and mastery**.) |
| 10 | 10 Transition | t3 | l10_1 | STRENGTH 3. Diagnosis and Prescription |
| 11 | 11 Program A and B | tests | l11_1–4 | 부제 How other math programs determine starting points, 칩 Program A · Program B, 두 교재종료테스트 결과표, Program A 4단계(… Instructor's observations and judgment → Final starting point) / Program B 3단계(Questions answered incorrectly → Regardless of time taken → Starting point determined) |
| 12 | 12 Diagnostic System | systems | l12_1–5 | SYSTEM Ⅰ · Ⅱ · Ⅳ 카드(Analysis by Objectives · Learning Functions · Answer Selection, 아래에 Which learning objectives need attention · Which learning functions need improvement · What may have caused the errors) → Personalized prescription: what to learn · how much to practice, 맺음 띠 |
| 13 | 13 System I | objective | l13_1–3 | 제목 Identifying Learning Gaps and Prescribing Workbooks, Analysis By Objective 표(분수 줄 빨간 상자), 포스트잇 Learning Gaps Identified, ① Group by objective · ② Match Workbooks · ③ Prescribe Workbooks(G01, G19–G21), TARGETED 도장 |
| 14 | 14 System II | function | l14_1–4 | 제목 From Learning Functions to Prescribed Workbooks, Analysis By Learning Function 표, ① Group by function(Related addition objectives grouped by learning function) · ② Match Workbooks · ③ Prescribe Workbooks(D 세트), FOCUSED 도장 |
| 15 | 15 System IV | wrong | l15_1–6 | 67 + 18 = ? 보기 넷(정답 ② 85), 오답 ① 75 · ③ 86 · ④ 715 마다 원인, 맺음 띠(Each wrong answer provides clues to …) |
| 16 | 16 Personalized Prescriptions | learners | l16_1–4 | Learner A · B: Wrong answers 7, ≠, Main learning gaps, Prescribed Workbooks, 맺음 띠(Different learning gaps call for different learning prescriptions.) |
| 17 | 17 Three Strengths, One System | summary | l17_1–4 | 세 카드가 선으로 이어져 One integrated learning system |
| 18 | 18 Closing | outro | l18_1 | Not the same learning for everyone, / but learning that fits each student. → Personalized, ability-based learning toward complete mastery, COMPLETE MASTERY 도장 |

## 대본 · 음성 · 시각표

- `tools/script.py`: 대본(`_SCRIPT`, 받은 영문 대본 그대로), 장면 목록(`SCENES`), 읽는 형태(`SAY`), 테이크 고정(`TAKE`), 간격. 씬 11 의 두 문장(Kumon … / The instructor then …)과 씬 15 · 16 의 긴 단락은 문장마다 한 줄로 나눴어요
  - 읽는 형태: JEI → "J-E-I"(한 글자씩, `../jei-ai-vision` 검토 2026.11.05), 2,619 → "two thousand six hundred nineteen", 67 plus 18 · 75 · 86 · 715 → 말로. 화면 · 자막은 쓰는 형태 그대로예요
- 목소리: `audio/voice_ref.wav` = `../jei-corporation-overview-female/audio/voice_ref.wav`(`../adaptive-diagnosis-v2/audio/narration.mp3` 14.1–28.95초, 여자 영어 목소리). DGX Qwen3-TTS(`http://192.168.51.8:8095`, `/v1/tts/clone`)가 문장마다 3번 읽고, whisper large-v3-turbo(mlx-whisper)로 받아써서 골라요. 줄 끝을 잘라먹지 않게 "Thank you." 를 붙여 읽히고 그 앞 쉼에서 잘라요. 끝 무음이 0.2초 안 되는 테이크는 잘린 것으로 쳐요
- 확인(2026.11.06): 고른 59개 테이크 모두 끝 무음 0.2초 이상이고, wav2vec2 음소(`facebook/wav2vec2-lv-60-espeak-cv-ft`)로 문장마다 마지막 단어까지 읽힌 것을 확인했어요. JEI 17곳 모두 "dʒ eɪ iː aɪ"(한 글자씩)예요. 받아쓰기 경고가 남은 l15_4 는 whisper 가 "basic addition" 을 "Basic Edition" 으로 적은 것이고, 음소로는 "b eɪ s ɪ k ɐ d ɪ ʃ ə n"(addition)이에요. 목소리 높이(Praat F0)는 문장마다 중간값 180–222Hz(전체 가운데 213Hz)로 갑자기 낮아진 테이크는 없고, 마지막 문장은 "learning" 에서 173 → 80Hz 로 내려가며 끝나요
- 첫 문장은 1.3초에 시작하고(0.25초에 차임), 문장 사이 0.6초, 쪽 사이 1.8초. 마지막 문장 뒤에 같은 차임이 울려요

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts                    # → timeline.js, audio/mix.wav, subtitles.srt
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l5_1     # 그 문장만 8번 새로 읽기
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.outro`(한국어판과 같은 구조, 문구와 큐 단어만 영어). 표지 · 맺음 띠 · 강점 상자 · 마무리 문구와 색은 `content.js`(영상 편집기에서도 수정 가능)
- 미리보기: `index.html`(재생 막대), `index.html?t=120`(그 시각)

```bash
node tools/snap.mjs out/snaps --ends              # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                        # out/jei_math_difference.mp4 (GPU: Chrome Metal + WebCodecs H.264)
node render.mjs --workers 3 --only 44-60           # 고친 구간(초)만 다시 그리고 나머지는 기존 영상에서 가져와요
```
