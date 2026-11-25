// On-screen text and colours (the video editor saves edits in this same shape, ../editor/PROTOCOL.md)
// Palette and rules: .claude/skills/graph-paper-video/reference/colors.md — red is the one main colour (section tags · teacher's pen ·
// key numbers); navy negative · wrong. The graph keeps the record's own colours (g…): the narration names them
// (파란색 실선 · 주황색 점선 · 보라색 점), so blue / orange / purple stay inside the graph only.
// Wording: Google Docs "그래프 영상 tts, 효과" (2026-11-24) and the graph files ~/Desktop/그래프 파일/그래프.svg · 그래프 설명.svg
window.CONTENT = {
 "title": { "kicker": "개인별 진단처방기록부", "words": ["맞춤 학습 계획", "그래프 안내"], "sub": "예시 학생으로 보는 그래프의 구성과 의미", "team": "수학팀" },
 "intro": { "tag": "INTRO  ·  맞춤 학습 계획", "title": "맞춤 학습 계획 그래프", "head": "맞춤 학습 계획", "caps": ["전체 학습 흐름과 예상 학습 기간", "학습 계획을 직관적으로 이해"] },
 "example": { "tag": "EXAMPLE  ·  예시 학생", "title": "1학년 학생의 진단 및 처방", "head": "1학년 학생의 진단 및 처방",
  "exam": ["실시 진단평가", "D등급 진단평가"], "plan": ["처방 학습", "C등급 6세트", "D등급 19세트", "총 25세트"], "final": ["학습 완료 후 평가", "D등급 총괄평가"] },
 "sections": {
  "structure": ["01  ·  기본 구조", "그래프의 기본 구조"],
  "path": ["02  ·  처방 학습 경로", "학생의 처방 학습 경로"],
  "standard": ["03  ·  표준 학습 경로", "표준 학습 경로"],
  "start": ["04  ·  학습출발점", "학습출발점"],
  "cross": ["05  ·  교점", "학생과 표준 학습 경로의 교점"],
  "read": ["06  ·  안내 문구", "그래프와 함께 제공되는 안내 문구"],
  "outro": ["SUMMARY  ·  정리", "맞춤 학습 계획 한눈에 보기"] },
 "compare": ["학교 학년", "학습 등급"],
 "graph": { "yTitle": "학습 단계", "top": "D 총괄", "grade": "D등급", "age": "(만 5.5세~초1 1학기)", "prev": "이전 등급", "xTitle": "학습 주차",
  "w1": "1주차", "w7": "7주차", "w10": "10주차", "w26": "26주차", "w14": "13주차", "set": "D20",
  "legend": ["학생의 처방 학습 경로", "표준 학습 경로", "학습출발점"], "perWeek": "한 주에 한 세트", "twoSets": "주 2세트라면" },
 "note": [
  "처방된 순서대로 한 세트씩 해내는 동안, 스스로 문제를 발견하고 생각하고 해결하며 끝까지 해내는 힘이 자랍니다.",
  "먼저 {C등급 6개 세트}와 {D등급 3개 세트}, {총 9개 세트}를 준비 학습으로 진행합니다.",
  "{10주차}에는 학습출발점인 {D20세트}부터 본학습을 시작하며, 이후 {16개 세트}를 포함해 {총 25개 세트}의 학습을 완료할 예정입니다.",
  "{26주차}에는 {D등급 총괄평가}를 통해 학습 성취도를 확인하고 다음 학습을 준비합니다."],
 "read": { "bar": "그래프와 문구를 함께 제공하여 {학생의 학습 계획}과 {예상 학습 흐름}을 보다 쉽게 확인" },
 "colors": {
  "paper": "#FEFFFF", "grid": "#E6EBEE", "gridMajor": "#D3DAE0", "margin": "#F4B1AB", "ink": "#383838", "muted": "#5E6B80",
  "red": "#E5303A", "navy": "#0F2F57", "blue": "#2C64C8", "mint": "#32C2AD",
  "lightRed": "#FF8F8F", "blush": "#FDDCD6", "redTint": "#FDE4E0", "crimson": "#B81F2E", "navyTint": "#E3E8F0", "blueTint": "#E4EEFB",
  "mintDark": "#1E9C8A", "mintTint": "#DDF5F2", "midGrey": "#A9AEB6", "lineGrey": "#B8BDC6", "lightBox": "#F3F4F6",
  "gBlue": "#2864BF", "gOrange": "#EC8833", "gPurple": "#7B55D3", "gBandTop": "#E4F3FF", "gBandLow": "#D4E0ED", "gGuide": "#B9CDDE",
  "gAxis": "#4C627A", "gLabel": "#526985", "gSub": "#7E94AA", "gRing": "#DAE8FF", "gNote": "#E4E4E4"
 }
};
