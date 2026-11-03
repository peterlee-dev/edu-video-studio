# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# GEO 모니터링 콘솔(geo.esls.io) for the executives: what it is and why, in under a minute. One line per page.
# No report results (numbers, rankings, who beats us): the user asked to keep the video on the strengths.
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')
VOICE = 'voice_ref_b'   # audio/voice_ref_b.wav: the app-guide narrator from the user's reference playlist (chosen over audio/voice_ref.wav, the ai-learning-platform-v3-ko voice)

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
# Asks and answers like the app promo videos the user pointed to, and stays on the good side: no report results at all
# (the user: the real numbers are bad, leave them out and stress the strengths). A question to an AI → how it was done until now →
# the tool → what it compares → summaries with their sources → "can we trust it?" → "what if the rules change?" → what it brings → end card
SCENES = [('title', '질문: 재능교육은 나올까요?'), ('before', '지금까지는'), ('purpose', 'GEO 모니터링 콘솔'), ('look', '나란히 비교'),
          ('summary', 'AI 요약과 근거'), ('trust', '믿을 수 있을까요?'), ('rules', '기준이 바뀌면요?'), ('outro', '기대효과'), ('end', '마무리')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# read forms: the name in words (the screen keeps the written form)
def R(s):
    for a, b in [('GEO', '지이오')]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s). Line ids: l<page>_<n>
_SCRIPT = [
    ('l1_1', 'title', '학부모가 AI에게 학습지를 추천해 달라고 하면, 재능교육은 나올까요?', .3),
    ('l2_1', 'before', '지금까지는 하나하나 직접 물어봐야 알 수 있었어요.', 0),
    ('l3_1', 'purpose', '이제 GEO 모니터링 콘솔이 정해진 주기마다 주요 AI 플랫폼에 같은 질문을 하고 답을 모아요.', 0),   # not "매일": the collection cycle is set per question group (could be every two weeks)
    ('l4_1', 'look', '우리가 나오는지, 몇 번째인지, 출처와 경쟁사까지 나란히 비교해요.', 0),
    ('l5_1', 'summary', 'AI 요약에는 근거 질문이 붙어 있어서, 원문도 바로 확인해요.', 0),
    ('l6_1', 'trust', '그럼 이 숫자, 믿을 수 있을까요?', .2),
    ('l6_2', 'trust', '성격이 다른 질문은 따로 재고, 지표마다 계산법을 붙였어요.', 0),
    ('l7_1', 'rules', '기준이 바뀌면요?', .1),
    ('l7_2', 'rules', '지난 회차까지 다시 판정해서 일관성이 유지돼요.', 0),
    ('l8_1', 'outro', '수집과 알림은 자동이라 손이 덜 가고, 무엇부터 고칠지 데이터로 알 수 있어요.', 0),
    ('l9_1', 'end', 'AI가 우리 브랜드를 어떻게 소개하는지, 이제 놓치지 않아요.', 0),   # answers the opening question ("…숫자로 관리해요" sounded odd)
]
READ = {'l7_2': '지난 회차까지 다시 판정해서, 일관성이 유지되어요.'}   # read in full: as "유지돼요" every take came out "유지되어" (the final 요 lost)
# breaths: a comma after these words in the read form, so the voice pauses between phrases
BREATH = {'l1_1': ['학부모가'], 'l3_1': ['콘솔이'], 'l7_2': ['판정해서'], 'l8_1': ['자동이라']}
QUESTIONS = {'l1_1', 'l6_1', 'l7_1'}   # a rising two-note sting just before these lines (mix)
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
CLONE = set()

# under a minute: shorter breaks than the 6-minute videos
LEAD, GAP, SCENE_GAP, TAIL = 1.1, .5, .8, 1.6   # s before the first line, between lines, extra between pages, after the last line (every take already ends with ~0.2 s of its own air)
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = None         # a bright chime at this time on the title page; None for none (the music starts the video instead)
DING_BEFORE = None
MUSIC = True            # upbeat music under the voice (make_audio.py music), asked for like the user's app-promo reference videos, and louder (2nd review)
