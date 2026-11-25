# GEO 모니터링 콘솔 화면 설명 (2분 46초)

GEO 모니터링 콘솔(geo.esls.io)의 화면을 하나씩 보여 주며 무엇을 하는 화면인지 설명하는 영상이에요. 사용자의 "GEO 모니터 기능 소개" 덱(Slides 아티팩트)의 캡처 11장으로 만들었어요. `../geo-monitor-ko`(1분 경영진 설명)는 그대로 두고, 그 영상의 그림 방식과 목소리를 이어받았어요.

- 그림 방식: `../geo-monitor-ko` 의 앱 홍보 모션그래픽(브랜드 레드와 흰 배경이 번갈아, 원형 전환, 단어에 맞춰 튀어나오는 큰 글자). 화면 장면은 캡처를 브라우저 창에 띄우고, 내레이션이 부분을 말할 때 스포트라이트가 그 부분으로 옮겨 가며 창 안에서 살짝 확대돼요(`index.html` 의 `screen()`)
  - 가로로 넓은 캡처(01~06): 창이 화면 대부분, 스포트라이트 옆에 빨간 설명 칩, 창 아래 큰 자막
  - 세로로 긴 캡처(07~10): 창은 왼쪽, 오른쪽에 화면 이름과 설명 목록(지금 말하는 줄이 빨간 점)
- **대본에는 리포트 결과를 넣지 않아요**(`../geo-monitor-ko` 와 같은 원칙): 수치, 순위, 경쟁사에 밀리는 내용은 내레이션, 설명 칩, 자막에 없어요. 캡처는 그대로 보여 줘요(사내용)
- 캡처(`assets/screens`)는 덱의 원본에서 **왼쪽 메뉴를 잘라냈어요**(아래쪽에 직원 이메일). 구성원 화면(`11-roles.png`)은 역할 표까지만 남기고 구성원 목록(이메일)은 잘라냈어요. 알림 화면은 웹훅 주소가 있어 캡처 대신 구글챗 메시지 카드를 그려요
- "매일"이라고 하지 않아요: 수집 주기는 질문군마다 정하는 설정이라 "정해진 시각에", "주기"라고 해요
- 화면 글자는 가운뎃점(·) 대신 쉼표, 화면 이름의 단계는 `›`
- 장면 전체가 천천히 커지는 push-in은 없어요(`../geo-monitor-ko` 에는 있어요): Chrome이 캔버스 글자를 정수 픽셀에 맞춰 그려서, 천천히 확대하면 그림은 부드럽게 커지는데 글자만 1초에 1px쯤 툭툭 내려가 보였어요(ver1 리뷰 "글자가 살짝씩 아래로")
- 내레이션: 해요체 25문장, `../geo-monitor-ko` 와 같은 목소리(`audio/voice_ref_b.wav`, DGX Qwen3-TTS 복제, 내부 검토용). 장면마다 설명이 끝나고 1.1초쯤 머문 뒤 넘어가요(`SCENE_GAP`), 원형 전환 0.9초
- 배경음: `../geo-monitor-ko` 와 같은 합성 팝(`tools/make_audio.py` 의 `music()`)
- 1920×1080, 30fps

| p. | 장면 | 화면 |
|---|---|---|
| 1 | title | 레드. 채팅창에 "초등학생 수학 학습지 추천해줘", 세 AI, "재능교육은 어떻게 소개될까요?" |
| 2 | intro | 흰색. GEO 모니터링 콘솔, 캡처 11장이 부채꼴로 한 장씩 |
| 3 | flow | 레드. 수집기 → 세 AI(질문, 답변) → 서버(판정, 지표) → 웹 콘솔 |
| 4 | sets | 흰색. 질문군 목록: 질문군 카드, 주기, 수집 상태, 다음 수집 |
| 5 | summary | 레드. 리포트 탭, 회차 선택, AI 답변 요약, 근거 질문 링크 |
| 6 | metrics | 흰색. 지표 카드 네 개, 직전 회차 비교, 추이 그래프 |
| 7 | question | 레드. 질문별 결과: 세 AI 카드의 언급, 등장 순서, 출처, 경쟁사 줄, 응답 원문 |
| 8 | sources | 흰색. 인용 출처 표: URL, 횟수, 인용한 AI, 인용한 질문 |
| 9 | competitors | 레드. 브랜드별 현황 표의 열 |
| 10 | responses | 흰색. 응답 열람: 질문, 회차 목록, AI 필터, 본문 |
| 11 | settings | 레드. 설정 탭: 자동 수집, 반복과 간격, 다음 수집 |
| 12 | top | 흰색. 학부모 인기 질문: 순위, 조사 시각 |
| 13 | criteria | 레드. 판정 기준: 브랜드 표현, 띄어쓰기 변형, "고치면 지난 회차까지 다시 판정" |
| 14 | team | 흰색. 역할 세 가지, 11시 구글챗 알림 카드 |
| 15 | end | 레드. GEO 모니터링 콘솔, "놓치지 않아요", geo.esls.io |

## 대본, 음성, 시각표

- `tools/script.py`: 대본, 장면 목록, 읽는 형태(GEO → 지이오, ChatGPT → 챗지피티, Share of Voice → 셰어 오브 보이스, 11시 → 열한 시), 간격
- 고른 녹음은 `audio/lines/` 에 문장마다 남아요. 간격이나 쉼(`PAUSE`)만 바꿀 때는 `remix` (TTS를 다시 하면 녹음이 바뀌어요)

```bash
npm install
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts     # → timeline.js, audio/mix.wav, subtitles.srt, audio/lines/
uv run --with numpy python tools/make_audio.py remix                       # 같은 녹음으로 간격, 쉼만 다시
```

## 고치기, 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.end`. 스포트라이트 위치는 각 장면의 `marks`(캡처 PNG 픽셀 좌표), 설명 칩 문구와 자막은 `content.js`
- 미리보기: `index.html` (재생 막대), `index.html?t=20` (그 시각)

```bash
node tools/snap.mjs out/snaps --ends            # 장면마다 끝나기 직전 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                      # out/geo_monitor_features_ko.mp4 (GPU)
node render.mjs --workers 3 --only 33-42         # 고친 구간(초)만 다시 그려요
```
