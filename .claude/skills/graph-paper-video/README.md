# graph-paper-video (Claude Code 스킬)

장표 · 대본을 주면 **모눈종이 워크북 설명 영상**(캔버스 애니메이션 + 복제 목소리 내레이션 + 선생님 펜 필기, 1920×1080 mp4)을 만들어 주는 Claude Code 스킬이에요. 재능교육 수학 · 영어 · 회사 소개 영상 20여 편을 만들며 쌓인 엔진, 색 기준, 목소리, TTS 검수 노하우가 이 폴더 하나에 들어 있어요.

## 설치

이 폴더(`graph-paper-video/`)를 통째로 복사하면 끝이에요.

```bash
# 모든 프로젝트에서 쓰기
cp -R graph-paper-video ~/.claude/skills/
# 한 프로젝트에서만 (저장소에 같이 커밋하면 팀이 같이 써요)
cp -R graph-paper-video <프로젝트>/.claude/skills/
```

그다음 Claude Code 에서 "이 장표랑 대본으로 모눈종이 영상 만들어 줘(한국어 여자 목소리)" 처럼 말하면 스킬이 불려요. `/graph-paper-video` 로 직접 부를 수도 있어요.

## 준비물

| 무엇 | 왜 |
|---|---|
| macOS (Apple Silicon) | whisper(mlx-whisper), GPU 렌더(Metal · VideoToolbox) |
| Google Chrome | 렌더 · 정지 화면 (`CHROMIUM=…` 로 다른 경로) |
| Node.js | `render.mjs`, `snap.mjs` (`npm install` 이 ffmpeg · playwright-core 를 받아요) |
| [uv](https://docs.astral.sh/uv/) | 파이썬 도구들 (`uv run --with …` 가 numpy · mlx-whisper · praat-parselmouth · torch 를 알아서 받아요) |
| Qwen3-TTS 복제 서버 | `tts` 모드. 사내 DGX(`http://192.168.51.8:8095`)가 기본값이고, 다른 서버는 `TTS_URL=…`. API 약속은 `reference/narration.md` |

TTS 서버가 없어도 `dry` 모드(글자 수로 길이 어림)로 화면은 다 만들 수 있고, 녹음 파일이 있으면 `take` 모드로 그 녹음을 잘라 써요.

## 들어 있는 것

```
SKILL.md                  Claude 가 따르는 순서(새 영상 · 수정 요청 반영)
reference/                색 기준, 화면 언어, 내레이션, TTS 검수(voice-qa.md)
template/                 새 영상 폴더의 원본 (엔진 index.html, 대본 script.py, make_audio.py, voice_check.py, render.mjs, snap.mjs)
voices/                   목소리 기준 녹음 4종: en-female · en-male · ko-female · ko-male (voices/README.md)
fonts/                    Noto Sans KR, Gaegu (SIL OFL 1.1, 라이선스 파일 포함)
scripts/new_video.sh      새 영상 폴더 만들기: 템플릿 + 목소리 + 글꼴 + npm install
```

효과음(쪽 넘김 휙, 차임)은 `make_audio.py` 안에서 합성해서 따로 파일이 없어요.

## 사람이 직접 돌릴 때

```bash
sh ~/.claude/skills/graph-paper-video/scripts/new_video.sh my-video --voice ko-female
cd my-video
# tools/script.py 에 대본을 쓰고
uv run --with numpy --with mlx-whisper python tools/make_audio.py tts         # timeline.js, audio/mix.wav, subtitles.srt
uv run --with numpy --with praat-parselmouth python tools/voice_check.py pitch
open index.html                                                                # 미리 보기 (재생 막대)
node tools/snap.mjs out/snaps --ends                                           # 쪽마다 정지 화면
node render.mjs --workers 3                                                    # out/my_video.mp4
```

## 주의

- 목소리 기준 녹음은 사내 영상 내레이션에서 자른 것이라 **사내 영상용**이에요. 밖으로 나가는 영상에 쓸지는 먼저 확인해요
- 색 기준(`reference/colors.md`)은 재능교육 수학팀 `수학 영상 컬러 개선.pdf`(2026-10-22) 기준이에요. 다른 브랜드는 `template/content.js` 의 `colors` 를 바꿔요
- 영상 편집기(`editor/`) 연동은 그 편집기가 있는 저장소에서만 쓰여요. 없어도 영상 만들기에는 상관없어요
