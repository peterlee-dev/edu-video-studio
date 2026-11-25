// On-screen text and colours (the video editor saves edits in this same shape, ../editor/PROTOCOL.md)
// Palette and rules: .claude/skills/graph-paper-video/reference/colors.md — red is the one main colour (positive · up · correct ·
// section tags · key numbers · teacher's pen, 1st of a comparison); blue / mint the 2nd / 3rd of a comparison; navy negative · wrong · down; the rest grey
// Wording from the deck (Google Slides 진단처방기록부 개선 영상, 2026-11-18)
window.CONTENT = {
 "title": { "kicker": "재능스스로수학", "words": ["개인별", "진단처방기록부", "개선 시안"], "sub": "학습 결과를 한눈에 보이게", "team": "수학팀 · 2026.11.18." },
 "core": { "title": "정밀한 분석은 그대로, 전달은 쉽고 명확하게", "bar": "{시각화}하고 {전달 방식}을 개선" },
 "old": { "title": "학습 결과를 한눈에 보이게", "head": "이렇게 바꿉니다", "change": ["글과 표를", "이미지와 그래프로"],
  "asks": ["무엇을 알고, 무엇을 모르는지", "어느 영역이 약한지", "어디서부터, 얼마 동안 공부하는지"] },
 "p1": { "title": "진단 결과를 그래프로 한눈에", "items": [
  ["성취도", "전체 학습목표의 성취율을 그래프로 제시, 성취도 수준 구간과 같은 등급 학생 평균이 함께 보입니다."],
  ["맞춤 보완, 학습출발점", "보완이 필요한 15세트만 공부하고, 본학습은 G25세트부터 시작합니다.", "학습출발점: 보완이 필요한 준비학습 뒤 본학습으로 이어지는 첫 세트"],
  ["영역별 분석", "파란색은 우리 아이, 회색은 평균. 강한 영역과 약한 영역이 바로 보입니다."],
  ["핵심 학습목표 진단 결과", "해당 등급에서 중요하게 다루는 학습목표 성취 여부를 문항 이미지와 함께 보여줍니다."],
  ["종합 분석", "진단 성취도와 예상진도를 요약, 오답사례 분석은 QR로 볼 수 있게 했습니다."],
  ["영역별 오답보기는 QR로 자세히", "틀린 문항의 학습목표와 오답사례, 관련 학교진도"]] },
 "p2": { "title": "얼마 동안 공부하는지 그림으로", "items": [
  ["학습 과정 그래프", "준비학습을 거쳐 본학습까지 걸리는 기간, 표준 학습 경로와 비교해 보여줍니다."],
  ["학습 과정 설명", "몇 주에, 얼마동안 공부하는지, 다음 학습은 무엇인지 정리했습니다."],
  ["예상 진도, 처방 프로그램", "월·주별 세트와 학습 내용 표는 그대로입니다."],
  ["세트 번호 3자리로도 선택", "선생님과 학부모가 쉽게 이해할 수 있도록, 기존 세트 번호 4자리를 3자리로도 선택할 수 있습니다."]] },
 "outro": { "title": "분석은 그대로, 보여주는 방식을 바꿉니다", "keep": ["분석", "학습정도 및 능력을 정확히 분석"], "change": ["보여주는 방식", "선생님과 학부모님이 더 잘 이해하도록"] },
 "thanks": { "text": "감사합니다.", "sub": "개인별 진단처방기록부 개선 시안", "team": "수학팀" },
 "colors": {
  "paper": "#FEFFFF", "grid": "#E6EBEE", "gridMajor": "#D3DAE0", "margin": "#F4B1AB", "ink": "#383838", "muted": "#5E6B80",
  "red": "#E5303A", "navy": "#0F2F57", "blue": "#2C64C8", "mint": "#32C2AD",
  "lightRed": "#FF8F8F", "blush": "#FDDCD6", "redTint": "#FDE4E0", "crimson": "#B81F2E", "navyTint": "#E3E8F0", "blueTint": "#E4EEFB",
  "mintDark": "#1E9C8A", "mintTint": "#DDF5F2", "midGrey": "#A9AEB6", "lineGrey": "#B8BDC6", "lightBox": "#F3F4F6"
 }
};
