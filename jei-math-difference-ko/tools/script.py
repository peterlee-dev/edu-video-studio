# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 재능수학 차별성 영상 시나리오.pdf (2026-11-05 revision, 18 scenes with three transition pages, scenes 4 · 7 · 11) + the deck
# 재능수학 차별성 영상 시나리오 복사본.pdf (transition slides before each of the three strengths). Word for word.
# ver1 (2026-11-04) read the first narration; ver2 rewrote it. ver4 (2026-11-05, 재능수학 특장점 영상 수정사항.pdf): the transition pages keep only
# their first line, l8_5 is new and l8_6 reworded, 교사 → 선생님 (l12_3, l16_4), the outro ends on one short line.
# ver5 (2026-11-05): l5_3 reworded (…종합적인 문제해결 능력을 기르는 데에는 한계가 있습니다).
# ver6 (2026-11-05, third 재능수학 특장점 영상 수정사항.pdf + the reworked narration): scene 10 (mastery) dropped, its conclusion moves into l9_5;
# a new page for SYSTEM Ⅱ (function, l14b_*), l15_0 leads into SYSTEM Ⅳ; 대교 / 비교한 dropped (l8_4, l9_4, l12_4); l5_3 · l8_5 reworded; l16_4 and
# l18_1 dropped, l17_3 + l17_4 one line, a new single outro line. Line ids: l<ver2 scenario scene>_<n> (kept so unchanged lines keep their takes).
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', '오프닝'), ('intro', '무엇이 다를까요'), ('pillars', '세 가지 핵심 경쟁력'),
          ('t1', '특장점 1 · 트랜지션'), ('kumon', '① 구몬수학 · 수와 연산 중심'), ('areas', '① 재능스스로수학 · 5개 영역'),
          ('t2', '특장점 2 · 트랜지션'), ('addition', '② 덧셈 학습 비교'), ('division', '② 나눗셈 학습 비교'), 
          ('t3', '특장점 3 · 트랜지션'), ('tests', '③ 다른 프로그램의 진단'), ('systems', '③ 2,619개 학습목표 · 세 가지 분석'),
          ('objective', '③ 학습내용별 분석'), ('function', '③ 학습기능별 분석'),
          ('wrong', '③ 오답사례별 분석'), ('learners', '③ 같은 오답 수, 다른 처방'),
          ('summary', '세 가지 경쟁력의 연결'), ('outro', '마무리')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# read forms: names said the Korean way, numbers in words (the screen keeps the written form). make_audio.py also applies SAY to whisper's transcripts
SAY = [('Eye Level Math', '아이레벨 매쓰'), ('2,619개', '이천육백십구 개'), ('7개', '일곱 개'),
       ('67 더하기 18', '육십칠 더하기 십팔'), ('75를', '칠십오를'), ('86을', '팔십육을'), ('715를', '칠백십오를')]
def R(s):
    for a, b in SAY + [('·', ' ')]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    ('l1_1', 'title', '재능스스로수학은 다른 수학 학습 프로그램과 무엇이 다를까요?', .1),
    ('l1_2', 'title', '지금부터 학습 영역, 학습 내용, 진단 시스템의 세 가지 측면에서 재능스스로수학만의 차별화된 강점을 살펴보겠습니다.', 0),

    ('l2_1', 'intro', '수학 학습의 차이는 단순히 얼마나 많은 문제를 푸느냐에 있지 않습니다.', 0),
    ('l2_2', 'intro', '무엇을 배우고, 같은 내용이라도 어떻게 학습하며, 학습자의 수준과 부족한 부분을 어떻게 진단하는지에 따라 달라집니다.', 0),

    ('l3_1', 'pillars', '재능스스로수학은 세 가지 핵심 경쟁력을 갖추고 있습니다.', .1),
    ('l3_2', 'pillars', '첫째, 연산뿐만 아니라 수학의 다섯 개 영역을 고르게 학습합니다.', 0),
    ('l3_3', 'pillars', '둘째, 개념과 원리의 이해부터 다양한 문제에 적용하고 충분히 숙달하는 과정까지 체계적으로 구성되어 있습니다.', 0),
    ('l3_4', 'pillars', '셋째, 학습 결손과 오답 원인을 다각도로 분석하여 학생 개개인에게 필요한 학습을 진단하고 처방합니다.', 0),

    ('l4_1', 't1', '먼저, 첫 번째 차별점은 학습 영역의 차이입니다.', 0),

    ('l5_1', 'kumon', '구몬수학은 자연수의 사칙연산부터 분수와 소수의 계산까지, 수와 연산을 중심으로 학습 내용이 구성되어 있습니다.', 0),
    ('l5_2', 'kumon', '기초 계산부터 복잡한 계산까지 반복적인 문제 풀이를 통해 계산의 정확성과 속도를 높이는 데 중점을 두고 있습니다.', .1),
    ('l5_3', 'kumon', '이처럼 수와 연산에 집중된 학습 구성은 계산 능력의 숙달에 강점이 있지만, 서로 다른 수학적 개념을 연결하여 종합적인 문제해결 능력을 기르는 데에는 한계가 있습니다.', 0),

    ('l6_1', 'areas', '반면, 재능스스로수학은 연산 중심의 학습을 넘어 수와 연산, 도형, 측정, 자료와 그래프, 규칙성 등 수학의 다섯 개 영역을 모두 다루도록 구성되어 있습니다.', .1),
    ('l6_2', 'areas', '각 영역의 핵심 개념과 원리를 단계적으로 학습하고, 이를 다양한 문제에 적용하면서 수학에 대한 이해의 폭을 넓혀갑니다.', 0),
    ('l6_3', 'areas', '이를 통해 학생들은 기초 계산 능력뿐만 아니라 논리적으로 생각하고, 수학적 관계를 파악하며, 다양한 문제 상황을 해결하는 종합적인 수학적 사고력을 기를 수 있습니다.', 0),

    ('l7_1', 't2', '두 번째는 학습 내용과 전개 방식의 차이입니다.', 0),

    ('l8_1', 'addition', '먼저, 덧셈의 학습 과정을 비교해 보겠습니다.', 0),
    ('l8_2', 'addition', '재능스스로수학은 처음부터 계산식을 제시하기보다, 구체적인 상황과 다양한 활동을 통해 덧셈의 의미와 원리를 자연스럽게 이해하도록 구성되어 있습니다.', 0),
    ('l8_3', 'addition', '학생들은 사물을 세고 합치는 경험을 바탕으로 덧셈의 원리를 익히고, 이를 덧셈식과 연결하면서 단계적으로 학습을 확장해 나갑니다.', .1),
    ('l8_4', 'addition', '반면, Eye Level Math는 덧셈식을 먼저 제시한 후, 구체물을 활용해 덧셈의 의미를 이해하도록 구성되어 있습니다.', .1),
    ('l8_5', 'addition', '이러한 학습 순서는 덧셈의 의미를 충분히 이해하기 전에 계산 방법에 먼저 집중하게 되어, 덧셈의 원리를 이해하기보다 형식화된 계산 절차를 익히는 데 치중하게 될 우려가 있습니다.', .1),
    ('l8_6', 'addition', '이에 비해 재능스스로수학은 구체적인 경험을 통해 덧셈의 개념과 원리를 이해한 후, 이를 수학적 표현과 계산으로 발전시켜 학생 스스로 수학을 이해하고 응용하는 힘을 기르도록 합니다.', 0),

    ('l9_1', 'division', '나눗셈 학습에서도 차이가 나타납니다.', 0),
    ('l9_2', 'division', '재능스스로수학은 구체물을 묶어 나누는 활동부터 수직선에서 뛰어세기, 반복 뺄셈까지 다양한 방법으로 나눗셈의 원리를 이해하도록 구성되어 있습니다.', 0),
    ('l9_3', 'division', '이를 통해 학생들은 서로 다른 활동이 하나의 수학적 원리로 연결된다는 것을 이해할 수 있습니다.', .1),
    ('l9_4', 'division', '반면, Eye Level Math 교재에서는 나눗셈의 원리를 학습한 후, 계산 방법을 익히고 유사한 유형의 문제를 반복적으로 연습하는 데 상대적으로 중점을 두고 있습니다.', .1),
    ('l9_5', 'division', '원리를 다양한 관점에서 이해하고 적용과 숙달까지 이어지는 체계적인 학습 설계가 재능스스로수학의 두 번째 핵심 차별성입니다.', 0),

    ('l11_1', 't3', '마지막 세 번째는 진단과 처방 시스템의 차이입니다.', 0),

    ('l12_1', 'tests', '수학 학습 프로그램마다 학습자의 수준을 평가하고, 다음 학습을 결정하는 방식에는 차이가 있습니다.', .1),
    ('l12_2', 'tests', '구몬수학은 테스트의 소요 시간과 정답 수를 기준 그래프에 적용하여 권장 학습 시작점을 확인합니다.', 0),
    ('l12_3', 'tests', '이후 선생님의 관찰과 판단을 함께 반영하여 실제 학습 출발점을 결정합니다.', .1),
    ('l12_4', 'tests', '또한 Eye Level Math는 테스트 소요 시간과 관계없이 오답이 발생한 문항을 중심으로 학습 수준을 평가하고, 그 결과에 따라 학습 시작점을 결정합니다.', 0),

    ('l13_1', 'systems', '반면, 재능스스로수학의 진단평가 시스템은 학습자의 평가 결과를 학습내용별 분석, 학습기능별 분석, 오답사례별 분석의 세 가지 관점에서 다각도로 분석합니다.', .1),
    ('l13_2', 'systems', '이를 통해 단순히 문제의 정답과 오답을 확인하는 데 그치지 않고, 어떤 학습내용이 부족한지, 어떤 학습기능에 결손이 있는지, 왜 틀렸는지까지 세밀하게 파악합니다.', .1),
    ('l13_3', 'systems', '이러한 분석은 2,619개의 세분화된 학습목표를 기반으로 이루어지며, 그 결과를 학생 개개인에게 필요한 학습내용과 학습량을 결정하는 맞춤형 처방으로 연결합니다.', .2),
    ('l13_4', 'systems', '이처럼 체계적인 학습 설계와 정교한 진단·처방 시스템을 통해 학생마다 꼭 필요한 학습을 제공한다는 점이 재능스스로수학의 세 번째 핵심 차별성입니다.', 0),

    ('l14_1', 'objective', '재능스스로수학의 진단평가 시스템은 학습내용별 분석과 학습기능별 분석을 통해 학습자의 부족한 부분을 파악합니다.', .1),
    ('l14_2', 'objective', '이 중 첫 번째 학습내용별 분석은 관련 평가 문항을 학습내용에 따라 그룹화하여 분석합니다.', 0),
    ('l14_3', 'objective', '특정 학습내용에서 결손이 확인되면, 해당 학습목표와 연계된 학습 세트를 처방합니다.', .1),
    ('l14_4', 'objective', '이를 통해 학생마다 부족한 학습내용을 파악하고, 필요한 학습을 선별하여 맞춤형으로 제공합니다.', 0),

    ('l14b_1', 'function', '두 번째는 학습기능별 분석입니다.', 0),
    ('l14b_2', 'function', '학습기능별 분석은 동일한 학습기능과 관련된 학습목표들을 하나의 그룹으로 묶어 평가 결과를 분석합니다.', 0),
    ('l14b_3', 'function', '특정 학습기능에서 결손이 확인되면, 해당 기능을 보완할 수 있는 학습 세트를 처방합니다.', .1),
    ('l14b_4', 'function', '이를 통해 학생이 어떤 학습기능에 어려움을 겪고 있는지 파악하고, 부족한 기능을 집중적으로 보완할 수 있도록 합니다.', 0),

    ('l15_0', 'wrong', '다음으로 오답사례별 분석입니다.', 0),
    ('l15_1', 'wrong', '같은 문제를 틀리더라도 학생마다 틀린 이유는 다를 수 있습니다.', .1),
    ('l15_2', 'wrong', '예를 들어, 67 더하기 18의 계산에서 75를 선택했다면 받아올림에 대한 이해가 부족할 수 있고, 86을 선택했다면 기초 계산 과정의 점검이 필요합니다.', 0),
    ('l15_3', 'wrong', '또한 715를 선택했다면 자릿값에 대한 이해가 부족할 가능성이 있습니다.', .1),
    ('l15_4', 'wrong', '재능스스로수학은 이처럼 학생이 선택한 오답을 통해 오류의 원인을 세밀하게 분석하고, 부족한 개념과 원리를 찾아 개인별로 필요한 학습을 처방합니다.', 0),
    ('l15_5', 'wrong', '즉, 단순히 틀린 문제를 다시 풀게 하는 것이 아니라, 왜 틀렸는지를 분석하여 학습 결손의 원인부터 보완하도록 설계된 시스템입니다.', 0),

    ('l16_1', 'learners', '오답 수가 같더라도 학생에게 필요한 학습은 다를 수 있습니다.', .1),
    ('l16_2', 'learners', '예를 들어 두 학생이 똑같이 7개의 문제를 틀렸더라도, 한 학생은 두 자리 수의 덧셈에서, 다른 학생은 수 세기와 기초 연산에서 학습 결손이 나타날 수 있습니다.', .1),
    ('l16_3', 'learners', '재능스스로수학은 이러한 학습 결손의 차이를 체계적으로 분석하여 학생마다 적합한 학습 출발점을 결정하고, 필요한 학습 세트를 개별적으로 처방합니다.', 0),

    ('l17_1', 'summary', '지금까지 재능스스로수학의 세 가지 차별성을 살펴보았습니다.', .1),
    ('l17_2', 'summary', '수학의 다섯 개 영역을 폭넓게 다루고, 개념과 원리의 이해에서 적용과 숙달까지 체계적으로 학습하며, 정교한 진단과 처방을 통해 학생마다 필요한 학습을 제공합니다.', .2),
    ('l17_3', 'summary', '이 세 가지 경쟁력이 하나의 학습 체계로 연결되어, 학생 개개인의 능력과 수준에 맞는 스스로학습을 실현하는 것이 바로 재능스스로수학의 핵심 경쟁력입니다.', 0),

    ('l18_1', 'outro', '재능스스로수학은 학습자 개개인의 수준과 능력에 맞는 학습을 제공하여 개인별·능력별 완전학습을 실현합니다.', 0),
]
READ = {}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together
BREATH = {
    'l1_2': ['측면에서'],
    'l3_3': ['이해부터'], 'l3_4': ['분석하여'],
    'l5_1': ['중심으로'], 'l5_2': ['통해'],
    'l6_1': ['넘어', '등'], 'l6_3': ['아니라'],
    'l8_2': ['통해'], 'l8_3': ['바탕으로'], 'l8_6': ['비해', '발전시켜'],
    'l9_2': ['재능스스로수학은', '뺄셈까지'], 'l9_4': ['익히고'], 'l9_5': ['이해하고', '설계가'],
    'l12_2': ['적용하여'], 'l12_3': ['이후'], 'l12_4': ['관계없이'],
    'l13_3': ['기반으로'], 'l13_4': ['이처럼', '통해'],
    'l14_1': ['통해'], 'l14b_2': ['묶어'], 'l15_4': ['이처럼'], 'l15_5': ['분석하여'],
    'l16_1': ['같더라도'], 'l16_2': ['들어'], 'l16_3': ['분석하여'],
    'l17_3': ['것이'], 'l18_1': ['제공하여'],
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
TAKE = {'l12_2': 5,               # ver2 pick, pinned so the ver4 lines (a new median pace) do not move it
        'l8_6': 6,                 # ver4: the level take (the automatic pick sits low, 146–160 Hz)
        'l8_4': 5, 'l8_5': 2,      # ver6: l8_4 take 5 says 아이레벨 매쓰 clearly (wav2vec2; whisper writes I-Level MES), level pitch; the auto pick (3) is clipped and dips to 136 Hz
        'l18_1': 2}                # ver6: the closing line falls (take 1 rises to 149 Hz on its last syllable)

# the same voice and pacing as ../jei-ai-vision-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
PACE = 6.77   # the pace (chars/s) the ver5 picks were made at, so the ver6 lines don't move the other lines' picks
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.8, 3.2   # s before the first line, between lines, extra between pages, after the last line
# lines that finish the sentence of the line before on the next scene of the same sheet: only this pause (s) before them
JOIN = {}
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line (the script has no thank-you line)
