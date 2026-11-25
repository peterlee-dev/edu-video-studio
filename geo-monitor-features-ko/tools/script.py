# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take | remix).
# GEO 모니터링 콘솔(geo.esls.io), screen by screen: the console's captures (the user's "GEO 모니터 기능 소개" deck) each explained.
# Same rule as ../geo-monitor-ko: the narration says what each screen does, never the report's results (numbers, rankings, who beats us).
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')
VOICE = 'voice_ref_b'   # audio/voice_ref_b.wav: the app-guide narrator of ../geo-monitor-ko

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor. The screens follow the deck's order
SCENES = [('title', '질문: 재능교육은 어떻게?'), ('intro', '화면으로 살펴보기'), ('flow', '어떻게 돌아가나'),
          ('sets', '질문군 목록'), ('summary', '리포트: AI 답변 요약'), ('metrics', '리포트: 지표'), ('question', '리포트: 질문별 결과'),
          ('sources', '리포트: 인용 출처'), ('competitors', '리포트: 브랜드별 현황'), ('responses', '응답 열람'), ('settings', '설정: 수집 주기'),
          ('top', '학부모 인기 질문'), ('criteria', '판정 기준'), ('team', '구성원과 알림'), ('end', '마무리')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# read forms: names in words (the screen keeps the written form)
def R(s):
    for a, b in [('GEO', '지이오'), ('Share of Voice', '셰어 오브 보이스'), ('11시', '열한 시')]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s). Line ids: l<page>_<n>
_SCRIPT = [
    ('l1_1', 'title', '학부모가 AI에게 학습지를 추천해 달라고 하면, 재능교육은 어떻게 소개될까요?', .3),
    ('l2_1', 'intro', 'GEO 모니터링 콘솔의 화면을 하나씩 살펴볼게요.', 0),
    ('l3_1', 'flow', '수집기가 정해진 시각에 세 AI에게 질문하고, 답변 원문과 출처를 모아요.', 0),   # the collector wakes at 01:00 and asks only the groups that are due: not "매일"
    ('l3_2', 'flow', '서버는 답을 판정해 지표를 계산하고, 팀은 웹 콘솔에서 결과를 봐요.', 0),
    ('l4_1', 'sets', '첫 화면은 질문군 목록이에요.', 0),
    ('l4_2', 'sets', '질문군마다 수집 주기를 따로 정하고, 수집 상태와 다음 수집 날짜를 한눈에 봐요.', 0),
    ('l5_1', 'summary', '질문군을 열면 리포트가 나와요.', 0),
    ('l5_2', 'summary', '맨 위에는 그 회차 AI 답변 요약이 있고, 문단마다 근거 질문이 링크로 붙어 있어요.', 0),
    ('l6_1', 'metrics', '그 아래 지표 카드는 자사 인용률, Share of Voice, 일관성, 평균 등장 순서를 보여 줘요.', 0),
    ('l6_2', 'metrics', '카드마다 직전 회차와 비교하고, 최근 추이를 작은 그래프로 그려요.', 0),
    ('l7_1', 'question', '질문별 결과에서는 세 AI의 답을 나란히 놓고, 언급 여부와 등장 순서, 출처, 경쟁사를 비교해요.', 0),
    ('l7_2', 'question', '응답 보기를 누르면, 원문이 바로 펼쳐져요.', 0),
    ('l8_1', 'sources', '인용 출처 표는 AI가 근거로 쓴 페이지를 인용 횟수 순으로 모아요.', 0),
    ('l8_2', 'sources', '어떤 AI가 어느 질문에서 인용했는지도 함께 나와요.', 0),
    ('l9_1', 'competitors', '브랜드별 현황에서는 우리와 경쟁사의 언급률, 평균 등장 순서, 직전 대비 변화를 한 표로 비교해요.', 0),
    ('l10_1', 'responses', '질문 번호를 누르면, 그 질문의 지난 응답이 회차별로 쌓여 있어요.', 0),
    ('l10_2', 'responses', 'AI별로 골라 보면서, 답이 어떻게 바뀌는지 따라갈 수 있어요.', 0),
    ('l11_1', 'settings', '설정 탭에서 자동 수집을 켜고 반복 간격을 정하면, 다음 수집 시각이 자동으로 계산돼요.', 0),
    ('l12_1', 'top', '학부모 인기 질문은 ChatGPT가 공개 웹에서 찾아 추정한 질문 순위예요.', 0),
    ('l12_2', 'top', '매월 새로 조사해서, 질문군에 넣을 질문을 고를 때 참고해요.', 0),
    ('l13_1', 'criteria', '판정 기준에는 우리 브랜드로 셀 표현과 경쟁사를 등록해요.', 0),
    ('l13_2', 'criteria', '기준을 고치면 지난 회차까지 다시 판정해서, 숫자가 일관되게 유지돼요.', 0),
    ('l14_1', 'team', '구성원은 팀 관리자, 편집자, 열람자 세 역할로 권한을 나눠요.', 0),
    ('l14_2', 'team', '수집 결과는 11시에 팀 구글챗으로 알려 줘요.', 0),
    ('l15_1', 'end', 'AI가 우리 브랜드를 어떻게 소개하는지, 이제 놓치지 않아요.', 0),
]
READ = {}
# takes chosen by a phoneme check (wav2vec2): l12_1 "ChatGPT" — take 1 reads 챗찌피티가 cleanly, the auto pick (3) adds a syllable (차찌찌피티).
# The read form 챗지피티 was no better (whisper writes either as 채찌 PT, the normal Korean sound of it)
# l10_2 take 0 and l5_2 take 1: by F0, level with the other lines (the auto picks read lower, 109 / 117 Hz against ~130, l10_2 ending on a rise)
TAKE = {'l12_1': 1, 'l10_2': 0, 'l5_2': 1}
# breaths: a comma after these words in the read form, so the voice pauses between phrases
BREATH = {'l1_1': ['학부모가']}
# extra silence before these spoken words (make_audio.py add_pauses), cut into the voice's own comma pauses; the voice is not slowed
PAUSE = {}
QUESTIONS = {'l1_1'}   # a rising two-note sting just before these lines (mix)
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
CLONE = set()

# breaks: a page stays ~1.1 s after its narration (GAP + SCENE_GAP - make_audio TURN 1.2 - .15) before the circle wipe starts,
# like ../geo-monitor-ko after its review (the page turns there felt rushed); screens get time to be looked at
LEAD, GAP, SCENE_GAP, TAIL = 1.1, .6, 2., 1.8   # s before the first line, between lines, extra between pages, after the last line (every take already ends with ~0.2 s of its own air)
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = None         # a bright chime at this time on the title page; None for none (the music starts the video instead)
DING_BEFORE = None
MUSIC = True            # the same synthesized upbeat music as ../geo-monitor-ko
