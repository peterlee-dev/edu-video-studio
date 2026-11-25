#!/bin/sh
# 새 모눈종이 워크북 영상 폴더 만들기: template/ 복사 + 목소리 기준 녹음(voices/) + 글꼴(fonts/) + npm install
#   sh <스킬 폴더>/scripts/new_video.sh <새 폴더> [--voice en-female|en-male|ko-female|ko-male|none] [--no-install]
# 목소리 목록: voices/README.md. --voice 를 빼면 en-female. 언어(script.py LANGUAGE)는 목소리에 맞춰 바꿔요
set -e
SKILL=$(cd "$(dirname "$0")/.." && pwd)
DEST=""; VOICE=en-female; INSTALL=1
while [ $# -gt 0 ]; do
  case "$1" in
    --voice) VOICE="$2"; shift 2 ;;
    --no-install) INSTALL=0; shift ;;
    -h|--help) sed -n '2,4p' "$0"; exit 0 ;;
    *) DEST="$1"; shift ;;
  esac
done
[ -n "$DEST" ] || { sed -n '2,4p' "$0"; exit 1; }
[ -e "$DEST" ] && { echo "이미 있어요: $DEST"; exit 1; }
if [ "$VOICE" != none ] && [ ! -f "$SKILL/voices/$VOICE/voice_ref.wav" ]; then
  echo "목소리가 없어요: $VOICE (있는 것: $(ls "$SKILL/voices" | grep -v README | tr '\n' ' '))"; exit 1
fi

cp -R "$SKILL/template" "$DEST"
mkdir -p "$DEST/audio" "$DEST/fonts" "$DEST/out"
cp "$SKILL"/fonts/*.ttf "$DEST/fonts/"
NAME=$(basename "$DEST")
sed -i.bak "s/id: 'FOLDER-NAME'/id: '$NAME'/" "$DEST/schema.js" && rm "$DEST/schema.js.bak"
if [ "$VOICE" != none ]; then
  cp "$SKILL/voices/$VOICE/voice_ref.wav" "$SKILL/voices/$VOICE/voice_ref.txt" "$DEST/audio/"
  case "$VOICE" in ko-*) sed -i.bak "s/^LANGUAGE = 'English'/LANGUAGE = 'Korean'/" "$DEST/tools/script.py" && rm "$DEST/tools/script.py.bak" ;; esac
fi
if [ "$INSTALL" = 1 ]; then (cd "$DEST" && npm install --silent); fi

echo "만들었어요: $DEST (목소리 $VOICE, $(sed -n "s/^LANGUAGE = '\([A-Za-z]*\)'.*/\1/p" "$DEST/tools/script.py"))"
echo "다음: tools/script.py 에 대본 → make_audio.py (dry | tts) → index.html 의 SC.<id> 장면 → tools/snap.mjs → render.mjs"
