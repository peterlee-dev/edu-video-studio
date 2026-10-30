---
name: graph-paper-video
description: 모눈종이 워크북 설명 영상(캔버스 애니메이션 + 내레이션, 선생님 펜 필기, 레드 메인 컬러 가이드)을 새로 만들거나 고친다. 장표·대본으로 새 설명 영상 만들기, 검토 시트의 수정사항 반영과 고친 구간만 다시 렌더, 수학 영상 색 기준 적용. adaptive-diagnosis-v2 · math-di-improvement-v2 · ai-learning-platform-v3 같은 영상.
---

# 모눈종이 워크북 영상

영상 전체가 **모눈종이 워크북 한 장**이에요. 장면마다 한 쪽(p. 1, p. 2 …)이고, 쪽이 바뀔 때만 종이가 옆으로 넘어가며(휙 소리), 읽는 동안 화면은 멈춰 있고 선생님 펜(동그라미 · 체크 · 밑줄 · 형광펜 · 포스트잇 · 도장)이 내레이션의 단어에 맞춰 그어져요. 색은 중립 화이트 위에 레드 하나가 포인트예요.

- `template/` — 바로 돌아가는 새 영상 폴더: `index.html`(그리기 엔진 + 예시 4쪽), `content.js`(문구 · 색), `schema.js`(영상 편집기 칸), `tools/script.py`(대본), `tools/make_audio.py`(목소리 → `timeline.js` · `audio/mix.wav` · `subtitles.srt`), `tools/snap.mjs`(정지 화면 확인), `render.mjs`(병렬 렌더 · 부분 렌더)
- [reference/colors.md](reference/colors.md) — 색 팔레트와 쓰는 기준. **색을 하나라도 고르기 전에** 읽어요
- [reference/visual-language.md](reference/visual-language.md) — 쪽 배치, 펜 표시를 언제 쓰는지, 움직임 규칙, 검토에서 지적받았던 것. **장면을 그리기 전에** 읽어요
- [reference/narration.md](reference/narration.md) — 목소리를 만드는 세 길(dry · tts · take)과 대본 쓰는 법. **목소리 단계에서** 읽어요

색의 뼈대: 레드 `#E5303A` = 긍정 · 상승 · 정답 · 체크 · 섹션 태그 · 핵심 숫자 · 펜, 네이비 = 부정 · 오답 · 하락, 비교는 레드 → 블루 → 민트, 나머지는 그레이. 장면 코드에서는 언제나 `K.<이름>` 으로 써요.

## 새 영상 만들기

1. **폴더 만들기**: 저장소 맨 위에 `cp -R .claude/skills/graph-paper-video/template <영상-이름>` → 그 폴더에서 `npm install`. 폴더 이름은 kebab-case(렌더 결과 `out/<영상_이름>.mp4` 가 여기서 나와요). 끝: `node_modules/ffmpeg-static/ffmpeg` 가 있어요
2. **대본 → 쪽 나누기**: 받은 장표 · 대본(PDF 등)을 끝까지 읽고 `tools/script.py` 를 채워요. 한 쪽에 1~3문장, 한 쪽은 한 가지 생각. 대본 문장은 한 글자도 바꾸지 않아요(틀린 표기 · 용어 불일치가 보이면 사용자에게 물어요). 끝: 대본의 모든 문장이 `SCRIPT` 에 순서대로 있고, 모든 장면 id 가 `SCENES` 에 있어요
3. **목소리**: [narration.md](reference/narration.md) 를 따라 가진 재료에 맞는 모드를 돌려요(목소리가 아직 없으면 `dry` 로 먼저 화면을 짜고 나중에 바꿔요). 끝: `done: …s, N lines` 가 나오고 경고(`!`, `reads differently`)가 없어요
4. **장면 그리기**: `index.html` 의 예시 장면(`SC.title`, `SC.problem`, `SC.steps`, `SC.outro`)을 지우고 `SCENES` 순서대로 `SC.<id> = t => { … }` 를 써요. 쪽마다 `header()` + 그림 + 펜 표시, 모든 시각은 `Wc(문장, 단어)` · `st()` · `H0()` 로 내레이션에 묶어요. 엔진(맨 위 `basics` ~ `page furniture`)과 compositor 는 그대로 두고, 여러 쪽에서 쓰는 그림만 도우미 함수로 더해요. 화면 문구 중 제목 · 마무리처럼 편집기에서 바꿀 만한 것은 `content.js` 에
5. **확인**: `node tools/snap.mjs out/snaps --ends` 로 쪽마다 다 그려진 화면을 뽑고 **한 장도 빠짐없이 열어 봐요**. 펜 표시가 그 단어에 그어지는 순간도 `node tools/snap.mjs out/snaps <초> …` 로 봐요. 끝: 모든 쪽 PNG 를 봤고, `cue words not found` · `ERR` 출력이 없고, 글자가 상자 · 화면 밖으로 넘치지 않고, 색이 [colors.md](reference/colors.md) 규칙을 지켜요
6. **렌더**: `node render.mjs --workers 6` (macOS Chrome 사용, 다른 브라우저는 `CHROMIUM=…`). 미리 보기는 `--preview`(15 fps). 끝: `완료: out/….mp4 (오디오: mix.wav)` 이고, 영상 길이가 `TL.duration` 과 같아요
7. **마무리**: `README.md` 를 이 저장소의 다른 영상 README 처럼 한국어로 써요(콘셉트 · 색 · 쪽 표 `| p. | 장면 | 화면 |` · 음성 만들기 · 렌더 명령). `schema.js` 의 `id` · `title` 을 채우고 `editor/videos.js` 맨 위에 `{ id, title }` 를 더해요(규칙: `editor/PROTOCOL.md`)

## 수정 요청 반영 (검토 시트 · 피드백)

1. **항목마다 장면 찾기**: 시트의 쪽 번호는 영상의 `p.` 와 다를 수 있어요(시트 8쪽 = 영상 p.5 였던 적이 있어요). 캡처 그림 · 문구로 장면을 찾고, `grep` 으로 `index.html` 의 해당 코드를 찾아요. PDF 캡처가 작으면 `pdftoppm -r 400` 으로 키워서 봐요
2. **고치기**: 요청한 것만 고쳐요. 문구를 바꾸면 같은 말이 쓰인 다른 쪽도 같은 표기로 맞췄는지 `grep` 으로 확인해요. 대본(내레이션)이 바뀌면 [narration.md](reference/narration.md) — 녹음 영상이면 `take` + `CLONE`
3. **확인**: 고친 순간마다 정지 화면을 뽑아 고치기 전과 비교해 봐요. 끝: 요청 항목 수만큼 확인한 PNG 가 있어요
4. **고친 구간만 다시 렌더**: 처음부터 다시 그리지 않아요. 구간 = 바뀐 것이 처음 보이는 때부터 그 장면이 끝나고 다음 쪽으로 넘어가는 0.8초까지(장면 처음부터 보이면 들어오는 쪽 넘김도 포함). `TL.scenes` 로 초를 계산해요
   - template 으로 만든 영상, ai-learning-platform-v3: `node render.mjs --workers 6 --only 44-60,84-91.6` (기존 `out/….mp4` 를 바탕으로 이어 붙여요)
   - adaptive-diagnosis-v2: 같은 index.html 약속이라 `template/render.mjs` 를 복사해 같은 명령
   - math-di-improvement-v2: `node render.js patch <이전영상.mp4> out/math_di_improvement_v2.mp4 44-60,84-91.6`
   - 대본 · 시각표가 바뀌어 길이가 달라졌으면 부분 렌더는 쓸 수 없어요: 전체 렌더
   - 끝: 고치지 않은 구간의 프레임이 이전 영상과 같은 시각끼리 맞아요(이음매 앞뒤 한 프레임씩 비교)
5. **전달**: 사용자가 받아 보던 파일(예: `~/Desktop/<이름>_ver6.mp4`)이 있으면 그것을 바탕으로 쓰고, 결과는 덮어쓰지 않고 다음 번호(`_ver7`)로 복사해요. 무엇을 어떻게 고쳤는지 시트 항목별로 표로 알려요
