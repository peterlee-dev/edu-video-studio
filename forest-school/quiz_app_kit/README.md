# 숲 학교 도전 골든벨 — 퀴즈 앱 재료

숲 학교 그림책(사계절) 설명 영상에서 쓴 퀴즈 68문제와 이미지, 영상, 음성이에요.
대상: 초등 1~2학년.

- `quiz.json`
  - `episodes[]`: 봄, 여름, 가을, 겨울 순서
    - `title`, `sub`, `color`: 계절 대표색
    - `cover`: 표지 이미지
    - `clip`: 6초 영상
    - `questions[]`
  - `questions[]`의 필드
    - `type`: `scene`(장면 퀴즈) 또는 `goldenbell`(1~10번)
    - `q`, `a`: 문제와 정답
    - `ox`: true면 O/X 문제이고 정답은 "O" 또는 "X"
    - `explain`: 정답 해설. 일부 문제만 있어요.
    - `img`: 관련 장면 그림
    - `audio_q`, `audio_a`: 문제와 정답을 읽어 주는 내레이터 음성(mp3)
- `img/*.jpg`
  - 생성 그림 72장(1280px, 16:9, 그림 속 글자 없음)
  - 등장인물: 곰취 선생님과 아이들
  - `images.json`에 그림마다 영어 설명이 있어요.
  - `cast.png`는 등장인물 설정 그림이에요.
- `video/*.mp4`
  - grok 영상 9개(736x400, 6초, 소리 없음)
  - 계절 표지: `sp_title`, `su_title`, `au_title`, `wi_title`
  - 장면: `sp_dandelion`, `sp_antlion`, `su_ash`, `au_seeds`, `wi_wood`
- 원본 영상: `~/Desktop/숲학교_{봄,여름,가을,겨울}_ver1.mp4`
- 그림책 전체 내용: `../book.md`
