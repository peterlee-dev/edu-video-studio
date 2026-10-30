# 숲 학교 사계절 (도전 골든벨 준비 영상, 4편)

숲 학교 그림책(책 14~89쪽, 곰취 선생님과 아이들의 봄·여름·가을·겨울 숲 탐험)의 내용을 빠짐없이 담은 초등 1~2학년용 설명 영상이에요. 봄·여름·가을·겨울 4편으로 나누었고, 편마다 장면이 끝날 때 확인 문제를 풀고 마지막에 **도전! 골든벨** 10문제를 풀어요. 1920×1080, 30fps.

- 책 내용 전사: `book.md` (사진 38장, 쪽마다 본문·말풍선·이름표·설명 상자 전부. ★는 아이가 표시한 핵심어)
- 대본·문제: `tools/script.py` (장면 끝 문제는 "문제! → 5초 카운트다운 → 정답은 ○○!", 골든벨은 번호가 붙은 10문제, O·X 문제 포함)
- 그림: codex 이미지 생성으로 그린 그림책풍(색연필·수채) 장면 그림과 생물 그림판(`tools/images.py` → `img/gen/`). 등장인물 기준 그림 `img/gen/cast.png`를 장면마다 붙여서 생김새를 맞춰요. 그림 속에는 글자를 넣지 않고, 이름표·설명은 화면 코드가 올려요
- 움직이는 장면: grok `image_to_video`로 그림을 6초 영상으로 만들어(`tools/gen_videos.py` → `video/<키>/프레임.jpg`) 편 오프닝과 움직임이 중요한 장면(민들레 씨, 개미지옥, 물푸레나무, 물봉선화, 딱따구리)에 써요
- 목소리: Qwen3-TTS (Apache 2.0), DGX TTS API. VoiceDesign으로 지은 내레이터(밝은 여성, `audio/voice_narr.wav`)와 곰취 선생님(푸근한 할아버지, `audio/voice_teacher.wav`)을 Base 모델로 복제해 읽어요. 선생님 대사는 자막에 '곰취 쌤' 표시가 붙어요
- 효과음(문제 등장, 째깍 카운트다운, 딩동댕, 골든벨 종, 팡파르, 새소리)과 계절마다 조가 다른 배경음은 `tools/make_audio.py`에서 합성해요. 배경음은 말할 때 작아져요
- 글꼴: Jua(주아체)·Noto Sans KR (SIL OFL)

## 만들기

```bash
npm install
python3 tools/gen_images.py --jobs 6          # 그림 (없는 것만, 다시: --redo 키1,키2)
python3 tools/gen_videos.py --jobs 3          # grok 영상 클립 + 프레임
python3 tools/make_audio.py all               # 음성·믹스·timeline_<편>.js (바뀐 문장만 다시 읽어요)
node render.mjs --ep spring --workers 6       # out/forest_spring.mp4 (summer, autumn, winter)
node tools/snap.mjs spring out/snaps 10 60    # 확인용 프레임
```

- 화면: `index.html?ep=spring` (브라우저로 열면 미리보기 재생). 장면 그림은 대사의 `bg`, 그림판·핵심 낱말은 `ov`로 정해요
- 곤충 몸 이름표 위치는 `ANAT`, 잣나무 마디 위치는 `NODES`(그림 비율 0~1)
