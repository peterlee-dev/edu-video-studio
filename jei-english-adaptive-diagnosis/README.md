# JEI English Online Adaptive Assessment (미주 · 모눈종이 워크북)

영어팀 장표 `3. [미주 공유용] 미주 영어 Adaptive 정밀진단평가 기획안_261105.pdf`(12쪽)와 영문 대본 `미주 지사 공유 문건 스크립트 - 3-2.[ENG] Adaptive 진단_English.pdf`(56문장, 12구간)로 만든 영상이에요(5분 25초). 대본은 한 글자도 바꾸지 않았고(1차 피드백 2026.10.30 으로 첫 문장만 "improve" → "introduce the new"), 장표의 한글 문구는 대본의 용어(Initial · Check · Final Check Question, learning objective, standard sets, POD)에 맞춰 영어로 옮겼어요. 화면은 `../jei-english-us-plan` · `../adaptive-diagnosis-v2` 와 같은 **모눈종이 워크북** 콘셉트예요.

- **모눈종이 워크북 한 장**: 장면 26개, 쪽 19장(p. 1 ~ p. 19). 장면이 바뀔 때 종이 위를 옆으로 넘어가고(믹스의 휙 소리와 같은 때), 읽는 동안은 화면이 움직이지 않아요. 같은 그림을 이어 쓰는 장면(프로그램 4개 → 목표 띠, 등급별 막대, 수학 · 영어 비교, 영역별 구조, AS-IS / TO-BE → 학습 선택지, 4단계)은 쪽 넘김 없이 바뀌는 부분만 겹쳐 바뀌어요(`CONT`)
- 선생님 펜 표시: 빨간 동그라미(○ 정답) · 체크 · 밑줄 · 손그림 상자 · 화살표, 네이비 ✗(오답), 형광펜, 포스트잇, 도장(INCORRECT, 네이비)
- 색: `수학 영상 컬러 개선.pdf` 기준(레드 `#E5303A` 메인, 네이비 부정 · 오답, 비교는 레드 → 블루 → 민트, 나머지 그레이). 팔레트는 `content.js` 의 `colors`
  - 등급별 문항 막대(장표 4쪽 그래프에서 읽은 값, 합계는 장표 숫자 그대로): 기초독서(Readiness) 라이트 레드 · Phonics 레드 / Grammar 블루 / Reading 민트 / Communication · Information 그레이
  - 문항 역할: Initial 레드 · Check 블루 · Final Check 민트(아직 판단 전인 확인 대상)
  - 수학 블루 / 영어 레드, AS-IS 블루 / TO-BE 레드, 1차 레드 / 향후 블루, 현재 진단의 한계는 네이비
- 1920×1080, 30fps. 글꼴은 macOS 시스템 글꼴 Avenir Next(본문) · Noteworthy(손글씨). 배경음악 없음 (내레이션 + 쪽 넘김 휙 소리, 끝인사 딩)
- 화면에 자막은 넣지 않아요. 필요하면 `subtitles.srt`

| p. | 장면 | 문장 | 화면 |
|---|---|---|---|
| 1 | title | l1_1 | 제목, 맞히면 어려워지고 틀리면 쉬워지는 문항 경로 → starting point |
| **01** | | | **Background** |
| 2 | parents | l2_1–2 | AI · 데이터 기반 학습, 단순 레벨 진단보다 더 → 학부모의 세 질문(struggle · start · improved) |
| 3 | aim | l2_3 | 진단 체계 개선 → 더 정확한 출발점 · 개인별 학습 계획, 맺음 띠 |
| **02** | | | **U.S. market benchmark** |
| 4 | market | l3_1 | 학생 응답 → 문항 조정 → 개인 맞춤 학습 |
| 5 | catirt | l3_2–3 | CAT(응답 따라 난이도가 오르내리는 그래프) · IRT(정답 확률 곡선, 문항 난이도 → 능력 수준) |
| 6 | programs · connect | l3_4–8 | NWEA MAP Growth · i-Ready · IXL · Star Reading(회사 · 연도 · 방식은 장표), 읽는 줄에 빨간 상자 → "Our goal: Precise assessment → Personalized learning" 띠 |
| **03** | | | **Assessment by level** |
| 7 | levels · levelsCJ | l4_1–5 | AA–J 등급별 영역 문항 수 막대, AA–B 기초독서 + Phonics, C–J Grammar · Reading, I · J 120 / 119 동그라미, 학습목표별 Adaptive 포스트잇 |
| **04** | | | **Question structure** |
| 8 | structure | l5_1–2 | D등급 16번(소문항 3개) 예시, (3) 하나 틀려 대문항 전체 오답, INCORRECT 도장 |
| 9 | roles | l5_3–4 | Initial · Check · Final Check Question 세 역할, 더 정확한 이해 확인 · 필요한 학습 찾기 |
| **05** | | | **A different approach** |
| 10 | mathEng · engConfirm · engSeq | l6_1–6 | 수학(긴 진단 → 피로, 문항 수 줄이기, 뚜렷한 순서) / 영어(이해 확인, 오답 하나 ≠ 모름, 순서가 늘 뚜렷하지 않음, 필요하면 여러 문항) |
| **06** | | | **Skill areas** |
| 11 | areas · areas2 | l7_1–5 | 순서가 뚜렷한 영역(Phonics PHN-01 → 03) / 정해진 순서가 없는 영역(Reading RC-01 ~ 04) → 단계적으로 · 학습목표마다 따로 |
| **07** | | | **Assessment logic** |
| 12 | logic | l8_1–4 | Initial + Check: ○○ 다음 학습목표, ✗✗ 더 학습 필요, 엇갈리면 Final Check Question |
| 13 | logic2 | l8_5 | 순서가 뚜렷하면 쉬운 것부터 단계적으로(틀린 곳에서 학습 시작), 아니면 학습목표 A–D 각각 |
| **08** | | | **Why improve** |
| 14 | limits | l9_1–3 | 한계 둘: 실수인지 모르는 것인지 구분 어려움 / 문항 난이도 · 응답 패턴 데이터 부족 |
| 15 | stages | l9_4–5 | 1차(개별 응답 활용 · 데이터 축적) → 향후(IRT 등, 정확도, 오답 분석) |
| **09** | | | **AS-IS / TO-BE** |
| 16 | asisTobe · options | l10_1–4 | 등급별 고정 문항 → 결과 → 학습 세트 / 응답에 따라 다음 문항 조정 → 학습 선택지 A–D(표준 세트 · 세트 + POD · POD만 · 온라인), 1차는 A · B |
| **10** | | | **Assessment process** |
| 17 | process · process2 | l11_1–6 | 4단계 카드(출발점 찾기 → 이해 확인 → 추가 문항 → 학습 배정), 읽는 단계에 빨간 상자, 진단 결과 → 개인 맞춤 학습 띠 |
| 18 | closing | l12_1–2 | 영어 학습의 특성을 반영한 Adaptive 진단, 기존 문항 개선 → 결과 연결 → 표준 세트 · POD |
| 19 | outro | l12_3–4 | Learning data → More accurate assessment → Adaptive Learning, Thank you |

## 음성 · 시각표 만들기

- 대본: `tools/script.py` (대본 PDF 와 글자 그대로 같아요). 읽는 문장을 따로 둔 곳: JEI → "J-E-I", AI → "A-I", CAT → "C-A-T", IRT → "I-R-T", NWEA → "N-W-E-A", IXL → "I-X-L", i-Ready → "Eye-Ready"(그대로 두면 "라이 레디"처럼 읽어서), POD → "P-O-D"(그대로 두면 "파드" · "페오디"), "Reading Comprehension" → "Reading, Comprehension"(붙여 읽으면 "Donprehension"으로 뭉개져서). 쉼표 때문에 "Reading," 뒤에서 쉬는 테이크가 많아서(2차 피드백 2026.11.02), 두 단어를 한 단어처럼 이어 읽은 테이크 0 을 `tools/script.py` 의 `TAKE` 로 고정했어요(짧아진 0.23초는 그 문장 뒤 쉼에 더해 뒤 시각은 그대로)
- 목소리: `tts` 모드, `../math-di-improvement-v2` 와 같은 목소리. 그 영상의 TTS 가 복제한 원본(`D~I 개선.mp3` = `../.claude/narration-src/di_narration.mp3`, 남성)의 앞 15.9초(두 문장)를 `audio/voice_ref.wav` 로 잘랐어요. DGX Qwen3-TTS(`http://192.168.51.8:8095`)가 이 목소리를 복제해 문장마다 3번 읽고, whisper 로 받아써 대본대로 읽은 것 중 고르게 읽은 것을 골라요(`audio/tts_cache/`)

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts   # timeline.js, audio/mix.wav, subtitles.srt
N=8 uv run --with numpy --with mlx-whisper python tools/make_audio.py tts --redo l3_2   # 한 문장만 다시 읽기
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.<id>`, 제목 · 마무리 문구와 색: `content.js` (영상 편집기에서도 수정 가능)
- 미리보기: `index.html` (재생 막대), `index.html?t=120` (그 시각)

```bash
node tools/snap.mjs out/snaps --ends            # 장면마다 다 그려진 때의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                     # out/jei_english_adaptive_diagnosis.mp4 (GPU)
node render.mjs --workers 3 --only 44-60        # 고친 구간만 다시 렌더해 이어 붙이기
node render.mjs --cpu --workers 6               # 예전 CPU 방식
```

### GPU 렌더 (이 영상부터)

`render.mjs` 는 기본으로 **GPU** 를 써요.

- 그리기: Chrome 을 `--use-angle=metal` 로 띄워 캔버스를 Apple GPU(Metal)로 그려요. 예전에는 SwiftShader(CPU 로 흉내 낸 GPU)였어요
- 압축: 그린 캔버스를 브라우저 안에서 바로 `VideoFrame` 으로 만들어 WebCodecs `VideoEncoder`(하드웨어 H.264, macOS VideoToolbox)에 넣어요. 브라우저 밖으로는 압축된 H.264 만 나와요. 예전에는 프레임마다 PNG 스크린샷을 떠서 libx264(CPU)로 압축했어요
- 이어 붙이기: 조각마다 첫 프레임이 키 프레임(SPS/PPS 포함)이고 B 프레임이 없어서, 조각들을 다시 인코딩하지 않고 바이트 그대로 이어 붙인 뒤 mp4 로 감싸요. 색 정보는 BT.709 로 표시해요
- `--only`(부분 렌더)는 새로 그린 조각과 이전 영상의 나머지를 한 번에 이어 ffmpeg 의 하드웨어 인코더(`h264_videotoolbox`)로 다시 압축해요
- 화질: 같은 프레임을 비교하면 GPU 압축 40–41 dB(PSNR), 예전 libx264 CRF 18 41.0 dB 로 같은 수준이에요
- 속도(같은 Mac, 다른 렌더가 함께 돌던 때, 브라우저 하나, 60 프레임): CPU 방식 0.1 fps, GPU 그리기 + PNG 2.9 fps, GPU 그리기 + 하드웨어 압축 10.6 fps
- GPU 가 없는 컴퓨터이거나 하드웨어 인코더를 쓸 수 없으면 `--cpu`
