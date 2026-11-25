// GEO 모니터링 콘솔, screen by screen — on-screen text and colours (red is the brand colour; ChatGPT/Gemini/Claude = red/blue/mint)
// (the video editor saves edits in this same shape, ../editor/PROTOCOL.md). On-screen text uses commas, never the middle dot (as in ../geo-monitor-ko)
// notes: one per spotlight on that page, in order (index.html SC.<page> marks). caps: one caption per narration line of the page (null = none)
// No report results in any of it (numbers, rankings, who beats us): the captures show them as they are, the words say what the screens do
window.CONTENT = {
 "title": { "ask": "초등학생 수학 학습지 추천해줘", "q": ["재능교육은", "어떻게 소개될까요"], "url": "geo.esls.io" },
 "intro": "화면으로 하나씩 살펴봐요",
 "flow": { "collector": ["수집기", "정해진 시각에 자동으로"], "got": "답변 원문, 출처", "server": ["서버", "판정, 지표 계산"], "console": ["웹 콘솔", "팀이 결과 확인"] },
 "sets": { "label": "질문군 목록", "notes": ["질문군마다 따로 추적", "수집 주기", "수집 중, 수집 꺼짐", "다음 수집 날짜"], "cap": "주기, 상태, 다음 수집을 한눈에" },
 "summary": { "label": "리포트  ›  AI 답변 요약", "notes": ["리포트, 질문, 설정 탭", "회차 선택", "그 회차 AI 답변 요약", "근거 질문 링크"], "cap": "요약마다 근거 질문" },
 "metrics": { "label": "리포트  ›  지표", "notes": ["우리 페이지를 근거로 쓰나", "경쟁사 대비 얼마나 나오나", "세 AI 모두 언급하나", "언급될 때 몇 번째인가", "직전 회차와 비교", "최근 추이"],
   "cap": ["지표 카드, 한눈에", "직전 회차 비교, 추이까지"] },
 "question": { "label": "리포트  ›  질문별 결과", "notes": ["같은 질문, 세 AI의 답", "언급 여부", "등장 순서", "출처, 자사 인용", "함께 나온 경쟁사", "AI별 응답 원문"], "cap": ["세 AI를 나란히 비교", "원문도 바로"] },
 "sources": { "label": "리포트  ›  인용 출처", "notes": ["AI가 근거로 쓴 페이지", "인용 횟수 순", "인용한 AI", "인용한 질문"], "cap": ["AI가 근거로 쓴 페이지", "어떤 AI가, 어느 질문에서"] },
 "competitors": { "label": "리포트  ›  브랜드별 현황", "notes": ["우리와 경쟁사", "언급률", "평균 등장 순서", "직전 회차 대비"], "cap": "한 표로 비교" },
 "responses": { "label": "응답 열람", "title": "회차별로 쌓여요", "notes": ["질문 하나를 따라가요", "회차마다 응답", "AI별로 골라 보기", "답이 어떻게 바뀌었나"] },
 "settings": { "label": "질문군 설정", "title": "수집 주기", "notes": ["설정 탭", "자동 수집 켜기", "N일마다 또는 매월", "다음 수집 시각 자동 계산"] },
 "top": { "label": "학부모 인기 질문", "title": "어떤 질문을 넣을까", "notes": ["ChatGPT가 공개 웹에서 추정", "질문 순위 10위까지", "매월 새로 조사", "질문 고를 때 참고"] },
 "criteria": { "label": "판정 기준", "title": "무엇을 우리로 셀까", "notes": ["우리 브랜드 표현", "띄어쓰기 변형까지", "고치면 지난 회차도 다시 판정", "숫자가 일관되게"] },
 "team": { "label": "구성원", "notes": ["구성원, 알림까지 설정", "질문군, 판정 기준 편집", "보기만 가능"], "chat": ["GEO 모니터", "오늘 회차 수집 결과"], "cap": ["세 역할로 권한", "11시 구글챗 알림"] },
 "end": "놓치지 않아요",
 "colors": {
  "ink": "#22262E", "muted": "#5E6B80",
  "red": "#E5303A", "redHi": "#F4535A", "crimson": "#B81F2E", "navy": "#0F2F57", "navyDeep": "#091E3A", "blue": "#2C64C8", "mint": "#32C2AD", "mintDark": "#1E9C8A",
  "redTint": "#FDE4E0", "navyTint": "#E3E8F0", "blueTint": "#E4EEFB", "mintTint": "#DDF5F2", "midGrey": "#A9AEB6", "lineGrey": "#D5D9E0", "lightBox": "#F1F3F6"
 }
};
