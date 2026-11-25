# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: Google Docs "그래프 영상 tts, 효과" (= ~/Desktop/그래프 파일/tts-and-screen-effects.docx, 2026-11-24): the TTS narration column,
# word for word. Its 화면 효과 column is what index.html draws. Korean female voice: the adaptive diagnosis voice (~/Desktop/어댑티브학습용.mp3,
# audio/voice_ref.wav = ../jei-ai-vision-ko and ../adaptive-diagnosis-v2-ko). ver1 used the ai플랫폼학습용 voice by mistake (it sounds male).
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', '표지'), ('intro', '맞춤 학습 계획'), ('example', '예시 학생'), ('structure', '① 기본 구조'), ('path', '② 처방 학습 경로'),
          ('standard', '③ 표준 학습 경로'), ('start', '④ 학습출발점'), ('cross', '⑤ 교점'), ('read', '⑥ 안내 문구'), ('outro', '⑦ 마무리')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh. From the example student on, the graph is built
# up on one sheet (the doc: the title changes, the graph and the student panel stay)
CONT = {'structure', 'path', 'standard', 'start', 'cross', 'read', 'outro'}

# read forms (the screen keeps the written form). make_audio.py also applies SAY to whisper's transcripts
SAY = [('‘', ''), ('’', ''), ('D등급', '디등급'), ('C등급', '씨등급'),
       ('19세트', '열아홉 세트'), ('25세트', '스물다섯 세트'), ('6세트', '여섯 세트'), ('26주차', '이십육 주차'), ('25주', '이십오 주'),
       ('평가', '평까'), ('교점', '교쩜'), ('출발점', '출발쩜'), ('학년·학기', '학년 학기')]
def R(s):
    for a, b in SAY:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    ('l0_1', 'title', '개인별 진단처방기록부 내 ‘맞춤 학습 계획’ 그래프에 대해 말씀드리겠습니다.', 0),

    ('l0_2', 'intro', '이 그래프는 학생의 전체 학습 흐름과 예상 학습 기간을 한눈에 보여주는 데 목적을 두었습니다.', 0),
    ('l0_3', 'intro', '주요 학습 정보를 시각화하여 학생과 학부모 모두가 학습 계획을 직관적으로 이해할 수 있도록 구성했습니다.', 0),

    ('l0_4', 'example', '그래프의 구성과 의미를 보다 쉽게 이해할 수 있도록 한 학생의 진단 및 처방 결과를 예시로 살펴보겠습니다.', .3),
    ('l0_5', 'example', '예시 학생은 1학년으로, D등급 진단평가를 실시한 후', -.25),
    ('l0_6', 'example', 'C등급 6세트와 D등급 19세트, 총 25세트의 학습을 처방받았습니다.', 0),
    ('l0_7', 'example', '처방된 학습을 모두 마친 후에는 D등급 총괄평가를 실시할 예정입니다.', .4),
    ('l0_8', 'example', '이 학생의 처방 내용을 바탕으로 맞춤 학습 계획 그래프가 어떻게 구성되는지 순서대로 살펴보겠습니다.', 0),

    ('l1_1', 'structure', '먼저 그래프의 기본 구조부터 살펴보겠습니다.', .2),
    ('l1_2', 'structure', '재능교육의 학습 시스템은 학교 학년이 아닌 학습 등급을 기준으로 운영됩니다.', 0),
    ('l1_3', 'structure', '따라서 그래프의 세로축은 학년이 아닌 학습 등급을 나타냅니다.', 0),
    ('l1_4', 'structure', '다만 학부모가 자녀의 학습 수준을 보다 직관적으로 이해할 수 있도록, 앞으로 학습할 등급이 어느 연령 및 학년·학기 수준에 해당하는지 함께 표시했습니다.', .3),
    ('l1_5', 'structure', '그래프의 가장 위쪽에는 처방된 학습을 마친 후 진행하게 되는 총괄평가 또는 진단평가를 표시했습니다.', .3),
    ('l1_6', 'structure', '가로축은 학습 기간을 주차 단위로 나타냅니다.', 0),
    ('l1_7', 'structure', '앞서 살펴본 예시 학생은 25주 동안 학습하고', -.25),
    ('l1_8', 'structure', '26주차에 D등급 총괄평가를 진행하는 것으로 표현됩니다.', .3),
    ('l1_9', 'structure', '이 그래프는 기본적으로 한 주에 한 세트를 학습한다는 가정으로 작성되었습니다.', 0),
    ('l1_10', 'structure', '다만 한 주에 여러 세트를 학습하는 경우에는 학습 기간이 단축되며, 이에 따라 그래프에 표시되는 주차도 변경됩니다.', 0),

    ('l2_1', 'path', '파란색 실선은 학생의 처방 학습 경로를 나타냅니다.', 0),
    ('l2_2', 'path', '그래프에서는 이전 등급 학습과 실시 등급 학습을 배경색으로 구분했습니다.', 0),
    ('l2_3', 'path', '예시 학생의 경우 이전 등급인 C등급은 6세트, 실시 등급인 D등급은 19세트의 학습 구간으로 구성됩니다.', .3),
    ('l2_4', 'path', '이때 학생마다 처방받은 등급과 세트 수가 다르기 때문에, 그래프에서도 이를 반영하여 등급별 학습 구간의 크기가 다르게 나타납니다.', 0),

    ('l3_1', 'standard', '주황색 점선은 표준 학습 경로를 나타냅니다.', 0),
    ('l3_2', 'standard', '표준 학습은 실시 등급의 첫 번째 세트부터 마지막 세트까지 순서대로 모두 학습하는 경우를 기준으로 합니다.', 0),
    ('l3_3', 'standard', '그래프에서는 이러한 표준 학습 경로를 학생의 처방 학습 경로와 함께 비교할 수 있도록 했습니다.', 0),

    ('l4_1', 'start', '그래프에 표시된 보라색 점은 학습출발점을 의미하며,', -.2),
    ('l4_2', 'start', '점 옆에는 해당 세트 번호가 표시됩니다.', 0),
    ('l4_3', 'start', '보라색 점 아래로 이어지는 세로 점선을 통해 몇 주차에 학습출발점에 도달하는지 확인할 수 있습니다.', 0),

    ('l5_1', 'cross', '파란색 학생 경로와 주황색 표준 경로가 교차하는 경우도 있습니다.', 0),
    ('l5_2', 'cross', '이 교점은 학생의 처방 학습과 표준 학습의 진행 정도가 같아지는 지점을 의미합니다.', 0),
    ('l5_3', 'cross', '교점 이후 파란색 실선이 주황색 점선보다 위에 위치한다면, 학생의 학습이 표준 학습보다 빠르게 진행되는 것을 의미합니다.', .4),

    ('l6_1', 'read', '기록부에는 그래프와 함께 학생의 학습 계획을 설명하는 안내 문구도 제공됩니다.', .3),
    ('l6_2', 'read', '그래프와 학습 안내 문구를 함께 제공하여 학생의 학습 계획과 예상 학습 흐름을 보다 쉽게 확인할 수 있도록 했습니다.', .4),

    ('l7_1', 'outro', '지금까지 맞춤 학습 계획 그래프를 살펴보았습니다.', .2),
    ('l7_2', 'outro', '이 그래프를 통해 학생의 처방 학습 경로와 표준 학습 경로를 비교하고,', -.2),
    ('l7_3', 'outro', '등급별 학습 구간과 학습출발점, 예상 학습 기간 및 최종 평가 시점을 한눈에 확인할 수 있습니다.', 0),
]
# fragments that go on in the next line: a comma at the end, so the extra sentence the TTS reads after them can be cut off in the pause
READ = {'l0_5': '예시 학생은 일학년으로, 디등급 진단평까를 실시한 후,', 'l1_7': '앞서 살펴본 예시 학생은 이십오 주 동안 학습하고,'}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together
BREATH = {
    'l0_3': ['시각화하여'], 'l0_4': ['있도록'], 'l0_8': ['바탕으로'], 'l1_5': ['위쪽에는'], 'l2_3': ['경우'], 'l3_2': ['학습은'],
    'l4_3': ['통해'], 'l5_2': ['교점은'], 'l6_2': ['제공하여'],
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
TAKE = {'l2_1': 7,   # whisper writes 실서는 for all 8 takes; wav2vec2: only take 7 keeps the ㄹ ("s i r s ɔ n ə n" = 실선은, the rest ≈ 시선은)
        'l4_3': 2}   # whisper writes 몇 주차의 for all 3; wav2vec2: take 2 "b j ɔ t … tʃ a j e h a k" (몇 주차에)

# the same voice and pace as ../jei-ai-vision-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
PACE = 5.64
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.5, 3.2   # s before the first line, between lines, extra between pages, after the last line
JOIN = {}
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line
