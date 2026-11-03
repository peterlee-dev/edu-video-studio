# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Korean version of ../ai-learning-platform-v3 (same 30 pages). The Korean script is longer than the English one, so line ids are its own:
# l<slide>_<n>, one id per sentence. One sentence (slide 3) spans two pages; it is split at its comma into l3_2 / l3_3, words unchanged.
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', '제목'), ('vision', '비전'),
          ('kmap', 'Knowledge Map이란?'), ('kmapHow', '학습능력이 발전하는 과정'),
          ('gather', '구축: 교육철학과 비교·분석'), ('analyze', '구축: AI 제안, 연구원 검토'), ('expand', '구축: 국가별 교육과정 연계'),
          ('layerK', 'Knowledge Layer'), ('layerA', 'AI Engine Layer'), ('layerS', 'Service Layer'),
          ('phases', '두 단계, 7개 프로젝트'), ('phase1', '1단계'), ('phase2', '2단계'), ('wiki', 'LLM Wiki'),
          ('pod', '개인 맞춤형 POD'), ('podCycle', 'POD 학습 순환'),
          ('behavior', '온라인 학습 행동 분석'), ('loop', '적응형 학습경로'), ('assistant', 'AI Learning Assistant'),
          ('statusMap', '학생의 학습상태'), ('statuses', '네 가지 학습상태'), ('recommend', '다음 학습 추천'),
          ('ben1', '기대효과 1'), ('ben2', '기대효과 2'), ('ben3', '기대효과 3'), ('ben4', '기대효과 4'),
          ('roadmap', '일정: 1단계'), ('roadmapPhases', '일정: 2단계'), ('roadmapAll', '개발 전 과정'),
          ('outro', '마무리')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = {'statuses', 'recommend', 'roadmapPhases'}

# read forms: English names said the Korean way, numbers in words (the screen keeps the written form).
# "Knowledge" stays in English: read as 날리지 it sounded like Konglish (review 1). A take whisper writes as 날리지 counts as a misread
def R(s):
    for a, b in [('JEI-Math', '제이이아이 매스'), ('Knowledge, AI Engine, Service', 'Knowledge, 에이아이 엔진, 서비스'),
                 ('AI Engine Layer', '에이아이 엔진 레이어'), ('Service Layer', '서비스 레이어'),
                 ('AI Learning Assistant', '에이아이 러닝 어시스턴트'), ('LLM Wiki', '엘엘엠 위키'), ('POD', '피오디'), ('JEI-SLI', '제이이아이 에스엘아이'),
                 ('50년', '오십 년'), ('18 이하', '십팔 이하'), ('7개', '일곱 개'),
                 ('2026년 4분기', '이천이십육 년 사 분기'), ('2027년', '이천이십칠 년'), ('2028년', '이천이십팔 년'), ('비교·분석', '비교 분석')]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s)
_SCRIPT = [
    ('l1_1', 'title', '이 프로젝트는 단순히 AI를 활용해 업무 효율을 높이는 것을 넘어, 재능교육의 학습 상품과 서비스 자체를 혁신하기 위한 것입니다.', .3),
    ('l1_2', 'vision', '지난 50년간 재능교육은 학습설계에 대한 풍부한 전문성을 축적하고, 다양한 교육자료를 확보해 왔습니다.', 0),
    ('l1_3', 'vision', '이러한 전문성과 교육자료를 AI가 활용할 수 있는 지식체계로 전환하여, 기존 인쇄 학습지와 개인 맞춤형 POD, 온라인 학습을 하나로 연결하는 통합 학습플랫폼을 구축하고자 합니다.', 0),

    ('l2_1', 'kmap', '이 학습플랫폼의 기반이 되는 것이 바로 JEI-Math Knowledge Map입니다.', .2),
    ('l2_2', 'kmap', 'Knowledge Map은 수학의 학습목표들을 서로 연결하여, 개별 학습능력이 어떤 관계를 맺고 단계적으로 발전하는지를 보여주는 지식체계입니다.', 0),
    ('l2_3', 'kmapHow', '예를 들어, 한 자리 수 덧셈에서 시작해 합이 18 이하인 덧셈을 학습하고, 이후 받아올림이 있는 두 자리 수 덧셈으로 발전하는 과정을 연결하여 보여줍니다.', .2),
    ('l2_4', 'kmapHow', '각 학습목표에는 학습 내용과 난이도에 대한 정보도 포함되어 있어, AI가 전체 수학 학습체계의 구조를 이해할 수 있도록 합니다.', 0),

    ('l3_1', 'gather', 'JEI-Math Knowledge Map은 특정 국가의 교육과정에 종속되지 않고, 재능교육의 교육철학을 중심으로 한 공통 수학 학습체계로 구축합니다.', .2),
    ('l3_2', 'gather', '이를 위해 AI는 재능교육의 교재와 연구자료, 교육철학을 여러 국가의 교육과정 및 학습기준과 비교·분석하고,', 0),
    ('l3_3', 'analyze', '이를 바탕으로 학습목표와 목표 간 연결관계를 제안합니다.', .2),
    ('l3_4', 'analyze', '재능교육 연구원은 AI가 제안한 내용의 교육적 타당성을 검토하며, 새로운 자료를 지속적으로 반영해 Knowledge Map을 발전시킵니다.', 0),
    ('l3_5', 'expand', '이렇게 구축된 공통 Knowledge Map을 국가별 교육과정과 연계하면, 각 국가와 지역에 적합한 학습 콘텐츠를 더욱 신속하고 유연하게 개발할 수 있습니다.', 0),

    ('l4_1', 'layerK', '이 플랫폼은 Knowledge, AI Engine, Service의 세 계층이 서로 연결된 구조로 구성됩니다.', .2),
    ('l4_2', 'layerK', '먼저 Knowledge Layer는 학습목표와 교재, 교육 전문 지식을 체계적으로 정리하여 플랫폼 전체가 활용할 수 있는 공통 지식기반을 제공합니다.', 0),
    ('l4_3', 'layerA', 'AI Engine Layer는 이러한 지식기반을 활용해 단계별 프로그램식 학습자료를 생성하고, 학생의 학습 진행 상황을 분석하며, 힌트와 해설을 제공하는 역할을 수행합니다.', 0),
    ('l4_4', 'layerS', '마지막으로 Service Layer는 이러한 기능을 기존 학습지와 개인 맞춤형 POD, 온라인 학습, 교사 지원도구 등의 실제 서비스로 구현합니다.', .2),
    ('l4_5', 'layerS', '학생의 학습 결과는 다시 시스템에 반영되어 다음에 무엇을 학습할지 결정하는 데 활용됩니다.', 0),

    ('l5_1', 'phases', '서로 연계된 7개 프로젝트는 크게 두 단계에 걸쳐 추진됩니다.', 1.4),   # the bars grow on its last word: time to read them
    ('l5_2', 'phase1', '1단계에서는 Knowledge Map 구축과 학습 콘텐츠 자동 생성, 개인 맞춤형 POD에 집중합니다.', .1),
    ('l5_3', 'phase1', '이를 통해 진단 결과가 학습 처방과 후속 연습으로 연결되는 학습체계를 구현하고 검증합니다.', 0),
    ('l5_4', 'phase2', '2단계에서는 학습 진행 상황 분석과 적응형 학습경로, AI Learning Assistant를 결합하여 온라인 개인 맞춤형 학습으로 확장합니다.', 0),
    ('l5_5', 'wiki', '이와 함께 재능교육 직원들이 직접 관리하고 업데이트할 수 있는 공통 지식기반인 LLM Wiki를 구축하여 전체 프로젝트를 지원할 계획입니다.', 0),

    ('l6_1', 'pod', '1단계의 핵심 서비스는 개인 맞춤형 POD 학습입니다.', .2),
    ('l6_2', 'pod', '먼저 학생의 진단 결과와 학습이력을 분석하여 어떤 내용을 학습해야 하고, 어느 정도의 연습이 필요한지 파악합니다.', 0),
    ('l6_3', 'pod', '이를 바탕으로 AI가 학습자료를 생성하고, 재능교육 연구원의 검토를 거쳐 학생에게 제공합니다.', 0),
    ('l6_4', 'podCycle', '이후 학습 결과를 반영해 다음 학습을 조정하며, 기존 교재에 필요한 보충학습을 추가하는 방식으로도 활용할 수 있습니다.', 0),
    ('l6_5', 'behavior', '2단계에서는 이러한 개인 맞춤형 학습방식을 온라인으로 확장합니다.', .1),
    ('l6_6', 'behavior', '온라인에서는 정답과 오답뿐 아니라 문제 풀이에 걸린 시간, 힌트 사용 여부, 재도전 횟수 등 학생의 학습 행동까지 분석합니다.', 0),
    ('l6_7', 'loop', 'AI는 이러한 정보를 활용해 학생별 학습경로를 조정하고, 필요한 복습이나 추가 연습, 심화 학습을 제공합니다.', 0),
    ('l6_8', 'assistant', '또한 AI Learning Assistant는 정답을 바로 알려주기보다 힌트와 해설을 제공해 학생이 스스로 문제를 해결하도록 돕습니다.', .1),
    ('l6_9', 'assistant', '교사 역시 학생별 학습정보를 활용하여 더욱 효과적인 맞춤형 지도를 할 수 있습니다.', 0),

    ('l7_1', 'statusMap', '이 화면은 Knowledge Map을 통해 개별 학생의 학습상태를 어떻게 나타낼 수 있는지 보여주는 예시입니다.', .2),
    ('l7_2', 'statusMap', '화면 위쪽에는 아직 학습하지 않은 내용이, 가운데에는 현재 학습 중이거나 추가 평가가 필요한 내용이, 아래쪽에는 이미 학습한 내용이 표시됩니다.', 0),
    ('l7_3', 'statuses', "각 학습목표는 ‘숙달(Mastered)’, ‘추가 연습 필요(Needs More Practice)’, ‘학습 결손(Learning Gap)’, ‘미학습(Not Yet Studied)’의 네 가지 상태로 구분됩니다.", 0),
    ('l7_4', 'recommend', 'AI는 이러한 학습상태를 통해 학생이 무엇을 이해하고 있는지 파악하고, 다음에 학습할 내용과 학습경로를 추천합니다.', .2),
    ('l7_5', 'recommend', '구체적인 학습상태 판정 기준은 실제 진단 결과와 학습데이터를 활용하여 개발하고 검증할 계획입니다.', 0),

    ('l8_1', 'ben1', '이 플랫폼을 통해 크게 네 가지 효과를 기대하고 있습니다.', .2),
    ('l8_2', 'ben1', '첫째, 국가별 교육과정에 맞는 학습 콘텐츠를 더욱 신속하게 개발할 수 있습니다.', 0),
    ('l8_3', 'ben2', '둘째, 진단 결과와 학습데이터를 통해 학생 개개인의 강점과 보완이 필요한 부분을 파악할 수 있습니다.', 0),
    ('l8_4', 'ben3', '셋째, 학생별로 학습목표와 연습량을 조정하여 POD와 온라인 서비스를 통해 개인 맞춤형 학습을 제공할 수 있습니다.', 0),
    ('l8_5', 'ben4', '마지막으로, 학업 성취도와 재능교육 자기주도학습지수인 JEI-SLI를 함께 살펴봄으로써 학생의 성장 과정을 더욱 종합적으로 이해하고 지원할 수 있습니다.', 0),

    ('l9_1', 'roadmap', '1단계는 2026년 4분기부터 2027년 말까지 진행됩니다.', .2),
    ('l9_2', 'roadmap', '이 기간에는 Knowledge Map과 학습 콘텐츠 생성 기능을 개발하고, 미국에서 개인 맞춤형 POD 서비스를 시범 운영한 후 한국으로 확대할 계획입니다.', 0),
    ('l9_3', 'roadmapPhases', '2단계는 2028년부터 시작되며, 학습 진행 상황 분석과 적응형 학습경로, AI Learning Assistant를 하나로 통합한 온라인 개인 맞춤형 학습플랫폼을 구현합니다.', 0),
    ('l9_4', 'roadmapAll', '개발 전 과정에서 Knowledge Map과 AI 엔진은 분기별로 지속 개선하고, LLM Wiki는 프로젝트 전반을 지원하는 공통 지식기반으로 활용합니다.', 0),

    ('l10_1', 'outro', '재능교육은 지난 50년간 축적한 학습설계 전문성과 AI 기술을 결합하여, 학생 한 명 한 명의 필요에 더욱 적합한 개인 맞춤형 학습환경을 만들어 가고자 합니다.', .5),
    ('l10_2', 'outro', '감사합니다.', 0),
]
# the four statuses are said in Korean only (the English names in brackets are on screen)
READ = {'l7_3': '각 학습목표는, 숙달, 추가 연습 필요, 학습 결손, 미학습의, 네 가지 상태로 구분됩니다.'}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together (review 1)
BREATH = {
    'l1_1': ['프로젝트는'], 'l1_2': ['재능교육은'], 'l1_3': ['교육자료를', '학습을'],
    'l2_1': ['것이'], 'l2_2': ['Map은', '맺고'], 'l2_3': ['시작해'], 'l2_4': ['학습목표에는'],
    'l3_1': ['Map은'], 'l3_2': ['위해', '교육철학을'], 'l3_3': ['바탕으로'], 'l3_4': ['연구원은'], 'l3_5': ['Map을', '콘텐츠를'],
    'l4_1': ['플랫폼은'], 'l4_2': ['먼저', 'Layer는', '정리하여'], 'l4_3': ['Layer는', '활용해'], 'l4_4': ['마지막으로', 'Layer는'], 'l4_5': ['결과는'],
    'l5_1': ['프로젝트는'], 'l5_2': ['1단계에서는'], 'l5_3': ['통해'], 'l5_4': ['2단계에서는', '결합하여'], 'l5_5': ['함께', '구축하여'],
    'l6_1': ['서비스는'], 'l6_2': ['먼저', '분석하여'], 'l6_3': ['바탕으로', '거쳐'], 'l6_4': ['이후'], 'l6_5': ['2단계에서는'],
    'l6_6': ['온라인에서는', '아니라'], 'l6_7': ['AI는', '활용해'], 'l6_8': ['또한', 'Assistant는', '제공해'], 'l6_9': ['역시', '활용하여'],
    'l7_1': ['화면은', '통해'], 'l7_4': ['AI는', '통해'], 'l7_5': ['기준은', '활용하여'],
    'l8_1': ['통해'], 'l8_2': ['콘텐츠를'], 'l8_3': ['통해'], 'l8_4': ['조정하여'], 'l8_5': ['살펴봄으로써'],
    'l9_1': ['1단계는'], 'l9_2': ['기간에는', '후'], 'l9_3': ['통합한'], 'l9_4': ['과정에서'], 'l10_1': ['재능교육은'],
}
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

# review 1: the voice came in late on a silent title page, and pages turned too soon after their last word → a chime at the start,
# the first line sooner, longer breaks between lines and pages. The voice keeps its own pace (asked for pauses, not a slower read)
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.8, 2.4   # s before the first line, between lines, extra between pages, after the last line
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = 'l10_2'   # the same chime just before this line (the thank-you); None for none
