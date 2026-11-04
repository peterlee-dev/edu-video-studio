# JEI AI 전환 비전 — 인터랙티브판 (한국어)

`~/Desktop/JEI_AI플랫폼_동영상장면.pptx.pdf`(12쪽) 장표를 **실제 제품 화면을 조작하는 것처럼 보이는** 내레이션 영상으로 만든 판이에요. 모눈종이 워크북(v3) 디자인은 쓰지 않고 그리기를 새로 짰어요.

- **한 공간 · 카메라 이동**: 어두운 공간에 PDF 쪽마다 앱 창(패널) 하나가 4 × 3 격자로 놓여 있고, 쪽이 바뀌면 카메라가 옆 패널로 날아가요(이동 + 살짝 줌아웃, 믹스의 휙 소리와 같은 때). 쪽 안에서는 천천히 다가가고, 내레이션이 가리키는 곳으로 줌해요. 마무리 쪽은 먼저 모든 패널을 한눈에 보여 준 뒤 마무리 카드로 들어가요
- **인터랙티브**: 마우스 커서가 버튼 · 토글 · 카드를 누르고(누를 때 금색 물결) 올려 두면 카드가 들려요. 지식맵 점이 별자리처럼 이어지고, 학습자 지식맵이 실시간으로 갱신되고, 3계층이 아이소메트릭으로 쌓이고, 로드맵이 스크롤바를 끌어 펼쳐지고, POD 순환이 돌아가요
- **내레이션**: `../jei-ai-vision-ko` 와 **같은 내레이션**이에요(코디네이터 지시로 통일). 그쪽 `tools/script.py` · `audio/tts_cache/` · `timeline.js` · `audio/mix.wav` · `subtitles.srt` 를 그대로 복사해 썼어요. 목소리는 `ai-learning-platform-v3-ko` 와 같은 복제 목소리(`audio/voice_ref.wav`, DGX Qwen3-TTS)
- **큐**: 그쪽 시각표는 한 쪽을 여러 장면(예: `kmapList · kmapDots · kmapAI`)으로 나눠요. 여기서는 `index.html` 의 `PAGE_OF` 로 같은 쪽의 장면을 한 패널로 묶어요. 그림은 `Wc(문장 id, 단어)` 로 그 단어가 읽히는 때에 맞춰 움직여요(한국어는 조사가 붙어 읽히므로 단어의 앞부분이 맞으면 찾아요)
- 색: 남색 공간 + 금색(JEI 강조 · Phase 1), 초록(Phase 2 · 완전학습), 파랑(서비스 · 온라인), 주황(미숙), 빨강(결손만), 회색(미학습). `content.js` 의 `colors`
- 글꼴: Noto Sans KR(`fonts/`, OFL)
- 길이 8분 37초(516.96초), 1920×1080, 30fps. 화면 자막 없음(`subtitles.srt` 는 따로). 배경음악 없음(내레이션 + 쪽이 바뀔 때 휙 소리 + 시작 · 끝 차임, 그쪽 믹스 그대로)
- 쪽을 읽는 동안 카메라는 가만히 있어요. 아주 느린 줌을 걸면 글자가 몇 초마다 1px 씩 위로 튀어 보여서 뺐어요(커서를 올린 카드도 내용은 움직이지 않고 테두리 · 그림자만 바뀌어요)

| PDF 쪽 | 패널(`SC.`) | 내레이션 장면 | 문장 | 화면 |
|---|---|---|---|---|
| 1 | title | title | l1_1–3 | 표지 문구, 별자리 지식맵(자산이 모이고 → AI 노드 → 학생 → 국가 궤도), 50년 카운터, "구축 방안 보기" 버튼 클릭 |
| 2 | why | why | l2_1–4 | 토글 "일반적인 AX / JEI의 AI 전환" 클릭, 업무 시간 막대가 줄어듦, AI 학습 플랫폼 허브가 교재 · 온라인 학습 · POD 를 연결 |
| 3 | kmap | kmapList · kmapDots · kmapAI | l3_1–6 | 목록 5줄 → 별 공간으로 날아가 점이 되고 선으로 연결, 점에 올리면 정보 카드, 선 = 선수 → 후속, 색 · 굵기, 보충학습 · 다음 학습 경로 |
| 4 | universe | universe | l4_1–3 | 두 자산 카드 → AI 비교 · 분석(진행률) → 380개 점의 JEI Math Universe 가 채워지고 줌 |
| 5 | country | country · countryTrack | l5_1–4 | 미주 · 국내 체계 → 공통맵 → 국가별 지식맵, "새 국가 추가" 클릭, 학습자 상태 추적, 3단계 설명과 결론 상자 |
| 6 | layers | layers · layerAgent · layerService · layerPace | l6_1–5 | 아래부터 쌓이는 아이소메트릭 3계층 + 계층 카드(P-번호), "안정적 유지" · "빠르고 유연하게 v1→v3" |
| 7 | roadmap | roadmap · phase1 · phase2 · wiki | l7_1–6 | 타임라인 눈금 + Phase 1 카드, 스크롤바를 끌어 Phase 2, 전체로 줄어든 뒤 P-06 LLM Wiki 가 모든 프로젝트에 공급 |
| 8 | pod | pod · podCycle | l8_1–6 | 5단계 파이프라인(체크 · 생성 · 검토 · 출력), 순환 고리가 돌며 회차가 올라감, 적용 순서 미국 → 한국 |
| 9 | online | online · assistant | l9_1–5 | 문제 풀이 화면(오답 → 힌트 → 다시 풀기 → 정답, 행동 기록 → 경로 조정), AI 튜터 대화, 선생님 대시보드와 코칭 제안 |
| 10 | status | statusMap · statuses · statusUpdate | l10_1–6 | 340개 점의 학습자 지식맵: 세 영역 → 네 상태 → 실시간 갱신, 결손 클릭 → 보충 → 다음 학습경로 |
| 11 | benefits | change1–4 | l11_1–5 | 네 카드를 차례로 클릭: 국가 칩, 학생별 학습지, 경로 재구성, JEI-SLI 성장 곡선 |
| 12 | outro | outro | l12_1–3 | 모든 패널 한눈에 + "50년의 학습설계 자산 → AI가 이해하고 활용하는 지식", 마무리 카드 "JEI만의 AI 개인화 학습 플랫폼" |

## 내레이션

이 폴더의 `tools/script.py` · `tools/make_audio.py` 는 `../jei-ai-vision-ko` 에서 복사한 것이에요. 내레이션을 고칠 때는 그쪽에서 고치고 TTS 를 돌린 뒤, 아래처럼 다시 복사해요.

```bash
cp ../jei-ai-vision-ko/{timeline.js,subtitles.srt} . && cp ../jei-ai-vision-ko/audio/mix.wav audio/ && cp ../jei-ai-vision-ko/tools/{script.py,make_audio.py} tools/
rsync -a ../jei-ai-vision-ko/audio/tts_cache/ audio/tts_cache/
uv run --with numpy python tools/make_audio.py dry   # 목소리 없이 시각표만 (화면 배치용)
```

## 고치기 · 렌더링

- 장면: `index.html` 의 `SC.title` ~ `SC.outro`, 쪽 안 카메라 `CAM.<패널>`, 커서 `CURSOR.<패널>`(도착 시각, x, y, 클릭)
- 표지 · 마무리 문구와 색: `content.js` (영상 편집기에서도 수정 가능)
- 미리보기: `index.html` (재생 막대), `index.html?t=120` (그 시각)

```bash
npm install
node tools/snap.mjs out/snaps --ends            # 장면마다 끝나기 0.4초 전의 정지 화면 + 못 찾은 큐 단어
node render.mjs --workers 3                      # out/jei_ai_vision_interactive_ko.mp4 (GPU: Chrome Metal + WebCodecs H.264)
node render.mjs --workers 3 --only 99-115        # 고친 구간(초)만 다시 그리기
```

## 내레이션 (최종)

`../jei-ai-vision-ko` 에서 확정된 내레이션(13문장 다시 읽힘, l1_3 의 Knowledge Map 읽기 변경, 516.96초)을 그대로 복사해 썼어요. `audio/mix.wav` · `timeline.js` · `subtitles.srt` · `tools/script.py` · `audio/tts_cache/` 가 그쪽과 바이트까지 같아요. 발음 · 테이크 확인은 그쪽 일이에요(`../jei-ai-vision-ko/out_tts.log`).
이 폴더의 큐는 받아쓰기 표기(띄어쓰기 "학습 목표" · "제시도" · "3개" 등)도 찾도록 맞춰 두었어요(`tools/snap.mjs` 에서 못 찾은 큐 없음).
