# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: Google Slides "진단처방기록부 개선 영상" (수학팀 박소영, 2026-11-18), page 1 = the script (revised by the team lead the same morning),
# pages 2–7 = the deck. Word for word. For the chairman's report: female voice, the report zooms in on each new part as it is explained.
# ver5 (2026-11-20): the deck's new page 1 (수정내용, 11 items) + page 2 (the revised script). The QR line moves onto the 1페이지 page (the lens
# moves on to it, no page of its own), 감사합니다 gets a page of its own. Lines that did not change keep their checked takes.
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', '표지'), ('core', '개선의 핵심'), ('old', '01 기존 리포트'), ('new', '02 개선 리포트'),
          ('p1', '03 1페이지 시안'), ('p2', '04 2페이지 시안'), ('outro', '마무리'), ('thanks', '감사합니다')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# read forms: numbers said in words (the screen keeps the written form). make_audio.py also applies SAY to whisper's transcripts
SAY = [('진단평가', '진단평까'), ('강점', '강쩜'),   # review 2: said the way they are pronounced
       ('1페이지', '일 페이지'), ('2페이지', '이 페이지'), ('4자리', '네 자리'), ('3자리', '세 자리'), ('QR코드', '큐알 코드')]
def R(s):
    for a, b in SAY:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    ('l1_1', 'title', '재능스스로수학은 진단평가와 총괄평가 결과를 정밀하게 분석해 학습자에게 맞는 처방 프로그램을 제시해 왔습니다.', 0),
    ('l1_2', 'title', '오늘은 이러한 분석 결과를 담은 개인별 진단처방 기록부의 개선 시안을 말씀드리고자 합니다.', 0),

    ('l1_3', 'core', '이번 개선의 핵심은 기존의 정밀한 분석을 바탕으로, 학습자와 학부모는 결과를 쉽게 이해하고 선생님은 보다 명확하게 설명할 수 있도록 시각화하고 전달 방식을 개선한 것입니다.', 0),

    ('l2_1', 'old', '현재 개인별 진단처방기록부입니다.', 0),
    ('l2_2', 'old', '1페이지는 종합 성취도와 영역별 분석, 오답내용 분석을 통해 학습자의 강점과 보완할 부분, 그 원인을 알려줍니다.', .1),
    ('l2_5', 'old', '총평을 통해 잘하는 것과 약한 것을 분석하고 앞으로 어떤 학습을 하게 될지 안내합니다.', .3),   # the deck writes "학습 을" (a stray space)
    ('l2_6', 'old', '2페이지는 학습출발점과 처방 프로그램, 예상 진도를 제시하여 어느 영역이 약한지, 어디서부터 얼마 동안 공부하는지의 흐름으로 기록부를 읽을 수 있습니다.', 0),

    ('l3_1', 'new', '지금부터 개선된 개인별 진단처방기록부를 페이지별로 설명드리겠습니다.', 0),

    ('l4_1', 'p1', '1페이지부터 말씀드리겠습니다.', .3),
    ('l4_2', 'p1', '첫째, 한눈에 보는 진단 결과입니다.', 0),
    ('l4_3', 'p1', '종합 성취도를 원그래프로 나타내고, 성취도 수준 구간과 동일 등급 학습자의 평균을 함께 제시하여 현재 학습 수준을 쉽게 비교할 수 있도록 했습니다.', .1),
    ('l4_4b', 'p1', '오른쪽 카드에는 보완이 필요한 세트 수와 본학습이 시작되는 학습출발점과 학습 내용을 요약했습니다.', .5),
    ('l4_5', 'p1', '둘째, 영역별 분석입니다.', 0),
    ('l4_6', 'p1', '방사형 그래프를 통해 학습자의 강점과 보완이 필요한 영역을 한눈에 확인할 수 있으며, 오른쪽 표에서는 영역별 세부 수치를 확인할 수 있습니다.', .5),
    ('l4_7', 'p1', '셋째, 핵심 학습목표 진단 결과입니다.', 0),
    ('l4_8', 'p1', '진단한 등급에서 중요하게 다루는 학습목표를 중심으로, 학습자가 알고 있는 내용과 보완이 필요한 내용을 대표 문항 이미지와 함께 제시했습니다.', .1),
    ('l4_9b', 'p1', '이를 통해 학습자가 무엇을 알고 무엇을 모르는지 구체적으로 이해할 수 있도록 했습니다.', .5),
    ('l4_10', 'p1', '마지막으로, 종합 분석입니다.', 0),
    ('l4_11b', 'p1', '진단 결과를 바탕으로 학습자의 성취도와 앞으로의 학습 계획을 정리했습니다.', .5),
    ('l4_12', 'p1', '오답내용 분석은 QR코드를 통해 영역별로 틀린 문항의 학습목표와 오답 사례, 관련 학교 진도를 자세히 확인하실 수 있습니다.', 0),

    ('l6_1b', 'p2', '2페이지는 맞춤 학습 계획을 그림으로 먼저 보여줍니다.', .1),
    ('l6_2', 'p2', '처방 내용을 이전 등급까지의 학습과 해당 등급 학습으로 나누고, 언제까지가 결손을 보충하는 준비학습이고 언제부터 본학습인지, 그 다음 과정은 무엇인지를 표준 학습 경로와 비교하여 보여줍니다.', .3),
    ('l6_3', 'p2', '이 내용을 오른쪽에 쉬운 설명으로 정리했습니다.', .4),
    ('l6_4b', 'p2', '아래 예상 진도와 처방 프로그램은 기존 그대로 유지했습니다.', 0),
    ('l6_5b', 'p2', '2페이지에서는 위에서 큰 흐름을, 아래에서 세부 내용을 차례로 확인할 수 있습니다.', .5),
    ('l6_6b', 'p2', '추가로 선생님과 학부모가 쉽게 이해할 수 있도록 기존 세트 번호 4자리를 3자리로도 선택할 수 있도록 했습니다.', 0),

    ('l7_1', 'outro', '이번 개선은 분석을 바꾸는 것이 아니라, 학습자의 학습정도 및 능력을 정확히 분석한 내용을 선생님과 학부모님이 더 잘 이해하시도록 보여주는 방식을 바꾼 것입니다.', 0),

    ('l7_2', 'thanks', '감사합니다.', 0),
]
# l1_2: the revised script writes "진단처방 기록부" (a space); it is read as before, so the checked take (시안) stays
READ = {'l1_2': '오늘은 이러한 분석 결과를 담은 개인별 진단처방기록부의 개선 시안을 말씀드리고자 합니다.'}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together
BREATH = {
    'l1_1': ['분석해'], 'l1_3': ['이해하고'],
    'l2_2': ['통해'], 'l2_5': ['분석하고'], 'l2_6': ['제시하여'],
    'l4_3': ['제시하여'], 'l4_4b': ['카드에는'], 'l4_6': ['통해'], 'l4_11b': ['바탕으로'], 'l4_12': ['통해'],
    'l6_2': ['준비학습이고'], 'l6_6b': ['있도록'], 'l7_1': ['내용을'],
}
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording (none: this video is read by the TTS clone)
CLONE = set()
# tts mode: a take chosen by ear or by the phoneme / pitch check, instead of the automatic pick ({line id: index in the sorted takes})
TAKE = {'l1_2': 1,   # whisper writes 시한 for every take; wav2vec2: take 1 says "ɕ j a n" (시안, no h) and ends cleanly (0.29 s of air)
        # review 2 (강쩜 · 진단평까 read forms), checked with wav2vec2: 평까 = "p j ə ŋ k a", 강쩜 = "k a ŋ tʃ ə" (tense), 보완 = "p uː (w) a n"
        'l1_1': 3, 'l2_2': 5,
        'l4_6': 2,   # file _10 (sorted position 2): 강쩜 tense, 보완 "p uː a n" (not the 보안-like "p o a n"), 180 Hz, 0.28 s of air
        'l4_4b': 4,   # ver5: 보완 "p uː a n", 0.29 s of air
        'l4_9b': 5,   # ver5: the level take (170 Hz; the automatic pick reads low, 142–158 Hz)
        'l4_8': 2}   # the level take (170 Hz; the automatic pick 6 sits low at 149 Hz, line median 169 Hz)

# the same voice and pacing as ../jei-math-difference-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
PACE = 6.71   # the pace the ver3 picks were made at, so the new lines don't move the other lines' picks
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.8, 3.2   # s before the first line, between lines, extra between pages, after the last line
# lines that finish the sentence of the line before on the next scene of the same sheet: only this pause (s) before them
JOIN = {}
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line
