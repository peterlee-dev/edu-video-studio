# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: JEI_AI플랫폼_동영상장면.pptx.pdf (12 pages). The paragraph in each page's dark bottom bar is the narration, word for word
# (only the PDF's stray spaces fixed: "제공하고 ," → "제공하고,", "결손으 로" → "결손으로", "**‘…’**" → "‘…’"). Line ids: l<PDF page>_<n>.
# One sentence (page 6) spans two scenes; it is split at its comma into l6_3 / l6_4, words unchanged.
# Review 2026-11-05 (sheet 어댑티브진단&AI플랫폼 소개_ 영상 수정 요청): l8_3 ~ l8_6 rewritten (contents made ahead per objective, kept in a reviewed DB,
# printed from the DB); l8_4 moved to the pod scene.
# Review 2026-11-04: l10_3 reads all four states (미학습 added) and l10_4 (결손 first) is new; the lines after it moved to l10_5 ~ l10_7.
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', '표지'), ('why', '왜 하는가'),
          ('kmapList', '왜 지식맵인가: 목록'), ('kmapDots', '왜 지식맵인가: 점과 선'), ('kmapAI', '왜 지식맵인가: AI의 판단'),
          ('universe', 'JEI Math Universe'),
          ('country', '국가별 지식맵'), ('countryTrack', '국가별 지식맵: 학습자 상태'),
          ('layers', '전체 구조: 지식 계층'), ('layerAgent', '전체 구조: AI 에이전트 계층'), ('layerService', '전체 구조: 서비스 계층'), ('layerPace', '전체 구조: 안정과 유연'),
          ('roadmap', '추진 로드맵'), ('phase1', '로드맵: Phase 1'), ('phase2', '로드맵: Phase 2'), ('wiki', '로드맵: LLM Wiki'),
          ('pod', '핵심 서비스 ① POD'), ('podCycle', 'POD 순환 · 적용 순서'),
          ('online', '핵심 서비스 ② 온라인 학습'), ('assistant', 'AI 보조선생님'),
          ('statusMap', '학습자 활성 지식맵'), ('statuses', '학습 상태 구분'), ('statusUpdate', '상태 갱신 · 경로 조정'),
          ('change1', '네 가지 변화 1'), ('change2', '네 가지 변화 2'), ('change3', '네 가지 변화 3'), ('change4', '네 가지 변화 4'),
          ('outro', '마무리')]
# scenes that continue the page before on the same sheet (one PDF page told in several steps): no page turn and no whoosh
# (index.html SHARED draws the part of the page that stays)
CONT = {'kmapDots', 'kmapAI', 'countryTrack', 'layerAgent', 'layerService', 'layerPace', 'phase1', 'phase2', 'wiki',
        'podCycle', 'assistant', 'statuses', 'statusUpdate', 'change2', 'change3', 'change4'}

# read forms: English names said the Korean way, numbers in words (the screen keeps the written form). "Knowledge" stays in English
# (as in ../ai-learning-platform-v3-ko: 날리지 sounded like Konglish), and Map is written 맵 so no vowel is added after the p
# (review 2026-11-03: "놀리지 매프" at l1_3). make_audio.py also applies SAY to whisper's transcripts
SAY = [('JEI-SLI', '제이이아이 에스엘아이'), ('JEI Math Universe', '제이이아이 매스 유니버스'), ('Knowledge Map', 'Knowledge 맵'), ('JEI', '제이이아이'),
       ('LLM Wiki', '엘엘엠 위키'), ('POD', '피오디'), ('DB', '디비'), ('CCSS', '씨씨에스에스'), ('50년간', '오십 년간'), ('7개', '일곱 개')]
def R(s):
    for a, b in SAY + [('‘', ''), ('’', ''), ('·', ' ')]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    ('l1_1', 'title', '재능교육이 지난 50년간 축적해 온 학습설계 자산.', .2),
    ('l1_2', 'title', '이제 이 자산에 AI 기술을 더해, 학생 한 명 한 명에게 최적화된 학습을 제공하고, 글로벌 수학 AI 학습의 새로운 표준을 만들어가고자 합니다.', .1),
    ('l1_3', 'title', '이를 실현하기 위한 ‘JEI Knowledge Map 기반 AI 개인화 학습 플랫폼 구축 방안’을 소개합니다.', 0),

    ('l2_1', 'why', '일반적으로 기업에서 AI를 도입하는 목적은 업무의 생산성과 효율성을 높이는 데 있습니다.', 0),
    ('l2_2', 'why', '하지만 재능교육이 추진하는 AI는 업무의 효율화를 넘어, 기존의 교재와 학습 시스템을 새로운 상품과 서비스로 발전시키는 데 목적이 있습니다.', .2),
    ('l2_3', 'why', '이를 위해 AI 학습 플랫폼을 기반으로 오프라인 교재와 온라인 학습, POD를 연결하고, 학습자에게 필요한 상품을 보다 유연하게 제공하고자 합니다.', 0),
    ('l2_4', 'why', '또한 국가별 교육환경과 다양한 학습 수요에 맞춰 커리큘럼과 콘텐츠를 신속하게 개발하고, 이를 새로운 서비스로 연결할 수 있는 체계를 구축하려고 합니다.', 0),

    ('l3_1', 'kmapList', 'AI 학습 플랫폼을 구축하기 위해 가장 먼저 해야 할 일은 재능교육 고유의 지식맵을 만드는 것입니다.', .1),
    ('l3_2', 'kmapList', 'AI가 학생에게 필요한 학습을 정확하게 제공하려면, 각각의 학습목표가 서로 어떤 관계에 있고, 어떤 순서로 학습해야 하는지 이해할 수 있어야 하기 때문입니다.', 0),
    ('l3_3', 'kmapDots', '이를 위해 마치 우주 공간에 흩어져 있는 수많은 별을 연결하듯, 개별 학습목표의 관계를 정의하고 하나의 지식체계로 구성합니다.', .1),
    ('l3_4', 'kmapDots', '이때 하나의 점은 하나의 학습목표를 의미하고, 점과 점을 잇는 선은 선수·후속 관계 등을 나타냅니다.', 0),
    ('l3_5', 'kmapDots', '또한 선의 색상과 굵기로 관계의 유형과 강도를 구분합니다.', 0),
    ('l3_6', 'kmapAI', '이렇게 학습목표 간의 관계를 연결하면, AI는 학습의 전체 구조를 바탕으로 학생에게 필요한 보충학습과 다음 학습경로를 판단할 수 있게 됩니다.', 0),

    ('l4_1', 'universe', '재능교육의 학습철학과 국내·미주 교재, 학습목표, 커리큘럼을 기반으로 지식맵을 구축합니다.', .1),
    ('l4_2', 'universe', '여기에 국내외 교과서와 교육과정, 미국의 CCSS 등 다양한 교육자료를 AI 에이전트가 함께 분석하여 학습목표 간의 관계를 정의하고 하나의 지식체계로 연결합니다.', .1),
    ('l4_3', 'universe', '이를 통해 특정 국가의 교육과정에 종속되지 않으면서도, 국내와 해외에서 공통으로 활용할 수 있는 재능교육만의 수학 공통 지식맵, 바로 ‘JEI Math Universe’를 구축하고자 합니다.', 0),

    ('l5_1', 'country', 'JEI 지식맵을 활용하면, 국가별 교육과정에 맞는 커리큘럼과 콘텐츠를 지금보다 훨씬 빠르게 개발하고 검증할 수 있습니다.', 0),
    ('l5_2', 'country', '새로운 국가에 진출할 때도 처음부터 학습체계를 만드는 것이 아니라, JEI 지식맵을 바탕으로 해당 국가의 교육과정과 성취기준을 연결하여 필요한 커리큘럼과 콘텐츠를 구성할 수 있습니다.', 0),
    ('l5_3', 'countryTrack', '또한 학습자의 학습 결과를 지식맵과 연결하면, 어떤 내용을 알고 있고 무엇이 부족한지 파악하고, 학습 상태의 변화를 지속적으로 추적할 수 있습니다.', .1),
    ('l5_4', 'countryTrack', '결국 JEI 지식맵은 국가별 상품 개발 속도를 높이고, 학습자 개개인에게 맞는 학습을 제공하는 기반이 됩니다.', 0),

    ('l6_1', 'layers', 'AI 학습 플랫폼은 크게 세 개의 계층으로 구성되며, 아래에서부터 단계적으로 구축합니다.', .1),
    ('l6_2', 'layers', '가장 아래의 지식 계층은 재능교육의 학습자료를 AI가 활용할 수 있는 JEI 지식맵으로 구축하는 단계입니다.', 0),
    ('l6_3', 'layerAgent', '그 위의 AI 에이전트 계층에서는 지식맵을 바탕으로 콘텐츠를 생성하고 학습 결과를 분석하며,', 0),
    ('l6_4', 'layerService', '최상위 서비스 계층에서는 이를 POD와 온라인 학습으로 학습자에게 제공합니다.', 0),
    ('l6_5', 'layerPace', '이때 기반이 되는 지식 계층은 한 번 구축하면 비교적 안정적으로 유지되는 반면, 서비스 계층은 기술 발전과 학습 환경의 변화에 맞춰 빠르고 유연하게 발전시킬 수 있습니다.', 0),

    ('l7_1', 'roadmap', 'AI 학습 플랫폼은 총 7개의 프로젝트로 구성되며, 크게 두 단계로 나누어 추진합니다.', 0),
    ('l7_2', 'phase1', '1단계에서는 JEI 지식맵과 콘텐츠 자동생성 AI 에이전트를 구축합니다.', .1),
    ('l7_3', 'phase1', '이를 바탕으로 AI가 재능교육의 프로그램식 학습원리에 따라 학생별 맞춤 콘텐츠를 생성하고, 이를 개인별 맞춤 POD 서비스로 제공합니다.', 0),
    ('l7_4', 'phase2', '2단계에서는 여기에 학습자 상태 분석과 AI 보조선생님 기능을 더해 온라인 개인화 학습 플랫폼으로 확장합니다.', .1),
    ('l7_5', 'phase2', '즉, 학습 과정에서 나타나는 학생의 이해도와 학습 상태를 분석하고, 그 결과에 따라 개인별 학습경로를 실시간으로 조정하며 필요한 학습을 제공하는 것입니다.', 0),
    ('l7_6', 'wiki', '이러한 두 단계의 개발 과정에서 LLM Wiki는 재능교육의 교육지식을 체계적으로 정리하고, 각 프로젝트에서 공통으로 활용할 수 있도록 지원하는 역할을 합니다.', 0),

    ('l8_1', 'pod', '1단계의 핵심 서비스는 개인별 맞춤 POD입니다.', .2),
    ('l8_2', 'pod', '먼저 학생의 진단 결과와 학습 이력을 바탕으로 필요한 학습목표와 학습 분량을 정합니다.', 0),
    ('l8_3', 'pod', '콘텐츠는 AI가 재능교육의 프로그램식 학습원리를 적용해 학습목표별로 미리 생성하고, 연구원의 검토를 거쳐 DB에 쌓아 둡니다.', .1),
    ('l8_4', 'pod', '이 검증된 DB에서 필요한 콘텐츠를 개인을 위한 POD 학습지로 제작해 출력합니다.', 0),
    ('l8_5', 'podCycle', '학습 결과는 다시 분석해 다음 POD에 반영하고, 보충할 내용과 분량을 조정하며 맞춤 학습을 이어갑니다.', .1),
    ('l8_6', 'podCycle', '이 서비스는 미국에서 먼저 적용하고, 운영 결과를 검증한 뒤 국내로 단계적으로 확대할 계획입니다.', 0),

    ('l9_1', 'online', '2단계의 핵심 서비스는 적응형 온라인 학습 플랫폼입니다.', .2),
    ('l9_2', 'online', '학습자의 정오답뿐 아니라 풀이 시간, 힌트 사용, 재시도 등 학습 과정에서 나타나는 행동을 분석해 학생의 학습 상태에 맞춰 콘텐츠와 학습경로를 실시간으로 조정합니다.', 0),
    ('l9_3', 'assistant', '또한 AI 보조선생님은 학생과 선생님을 각각 지원합니다.', .1),
    ('l9_4', 'assistant', '학생에게는 정답을 바로 알려주기보다 스스로 문제를 해결할 수 있도록 힌트와 설명을 제공하고, 선생님에게는 학생의 학습 상태와 어려움을 알려주어 보다 구체적인 학습 지도와 코칭이 가능하도록 돕습니다.', .1),
    ('l9_5', 'assistant', '이를 통해 학생에게는 개인별 맞춤 학습을, 선생님에게는 효과적인 학습 지도를 지원하는 온라인 학습 환경을 구현하고자 합니다.', 0),

    ('l10_1', 'statusMap', '학습자 한 명의 학습 상태를 지식맵 위에 표시하면 이와 같은 모습으로 나타납니다.', .1),
    ('l10_2', 'statusMap', '아래쪽은 이미 학습한 영역, 가운데는 현재 학습 중인 영역, 위쪽은 앞으로 학습할 영역을 의미합니다.', 0),
    ('l10_3', 'statuses', '이때 각각의 학습목표는 학생의 이해도에 따라 완전히 이해함, 보완 필요, 결손, 미학습으로 구분됩니다.', 0),
    ('l10_4', 'statuses', '이 중 결손으로 확인된 학습목표는 가장 먼저 보완합니다.', 0),
    ('l10_5', 'statusUpdate', '이러한 학습 상태는 진단과 학습 결과가 쌓일 때마다 계속 갱신됩니다.', .1),
    ('l10_6', 'statusUpdate', '따라서 이미 지나온 학습 내용이라도 부족한 부분이 발견되면 필요한 내용을 보충하고, 그 결과를 반영해 다음 학습경로를 다시 조정합니다.', .1),
    ('l10_7', 'statusUpdate', '결국 학생이 이미 알고 있는 내용은 불필요하게 반복하지 않고, 부족한 부분은 충분히 보충하면서 학생 개개인에게 맞는 학습경로를 만들어가는 것입니다.', 0),

    ('l11_1', 'change1', 'AI 학습 플랫폼을 통해 우리는 크게 네 가지 변화를 만들어갈 수 있습니다.', .2),
    ('l11_2', 'change1', '첫째, 국가와 지역의 교육과정에 맞는 학습체계와 콘텐츠를 보다 빠르게 개발하고 검증할 수 있습니다.', 0),
    ('l11_3', 'change2', '둘째, 학생 개개인에게 필요한 학습목표와 분량을 정해, 필요한 시점에 맞춤형 콘텐츠를 제공할 수 있습니다.', 0),
    ('l11_4', 'change3', '셋째, 학습자의 이해도와 학습 상태에 따라 부족한 부분은 보충하고, 다음 학습경로를 실시간으로 조정할 수 있습니다.', 0),
    ('l11_5', 'change4', '마지막으로, 학업 성취도뿐 아니라 JEI-SLI를 통해 스스로학습능력의 변화까지 분석하여, 다른 학생과의 비교가 아닌 이전의 자신과 비교한 성장 과정을 학습자와 선생님, 학부모에게 보여줄 수 있습니다.', 0),

    ('l12_1', 'outro', '재능교육이 지난 50년간 축적해 온 학습설계 자산을 AI가 이해하고 활용할 수 있는 지식으로 만드는 것, 이것이 이번 프로젝트의 출발점입니다.', .2),
    ('l12_2', 'outro', '이를 바탕으로 국가별 학습체계와 콘텐츠를 더욱 빠르게 개발하고, 학생 한 명 한 명의 수준과 학습 상태에 맞춰 학습과 성장을 지원하는 JEI만의 AI 개인화 학습 플랫폼을 구축하고자 합니다.', .3),
    ('l12_3', 'outro', '재능교육은 이를 통해 개인별·능력별 학습의 가치를 더욱 발전시키고, 글로벌 수학 AI 학습의 새로운 표준을 만들어가겠습니다.', 0),
]
READ = {}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together
BREATH = {
    'l1_1': ['재능교육이'], 'l1_2': ['이제'], 'l1_3': ['위한'],
    'l2_1': ['일반적으로', '목적은'], 'l2_2': ['하지만', 'AI는'], 'l2_3': ['위해', '기반으로'], 'l2_4': ['또한', '맞춰'],
    'l3_1': ['위해', '일은'], 'l3_2': ['하는지'], 'l3_3': ['위해', '정의하고'], 'l3_4': ['이때', '선은'], 'l3_5': ['또한'], 'l3_6': ['AI는', '바탕으로'],
    'l4_1': ['기반으로'], 'l4_2': ['여기에', '분석하여', '정의하고'], 'l4_3': ['통해'],
    'l5_1': ['콘텐츠를'], 'l5_2': ['때도', '바탕으로', '연결하여'], 'l5_3': ['또한', '있고'], 'l5_4': ['결국', '지식맵은'],
    'l6_1': ['플랫폼은'], 'l6_2': ['계층은', '학습자료를'], 'l6_3': ['계층에서는', '생성하고'], 'l6_4': ['계층에서는'], 'l6_5': ['이때', '계층은', '맞춰'],
    'l7_1': ['플랫폼은'], 'l7_2': ['1단계에서는'], 'l7_3': ['바탕으로', '따라'], 'l7_4': ['2단계에서는', '더해'], 'l7_5': ['조정하며'], 'l7_6': ['과정에서', 'Wiki는'],
    'l8_1': ['서비스는'], 'l8_2': ['먼저', '바탕으로'], 'l8_3': ['콘텐츠는', '적용해', '거쳐'], 'l8_4': ['DB에서'], 'l8_5': ['결과는', '조정하며'], 'l8_6': ['서비스는', '뒤'],
    'l9_1': ['서비스는'], 'l9_2': ['아니라', '분석해', '맞춰'], 'l9_3': ['또한', '보조선생님은'], 'l9_4': ['학생에게는', '알려주기보다', '선생님에게는', '알려주어'], 'l9_5': ['통해'],
    'l10_1': ['표시하면'], 'l10_2': ['아래쪽은', '가운데는', '위쪽은'], 'l10_3': ['이때', '학습목표는', '따라'], 'l10_4': ['학습목표는'], 'l10_5': ['상태는'], 'l10_6': ['따라서', '발견되면', '반영해'], 'l10_7': ['결국', '보충하면서'],
    'l11_1': ['우리는'], 'l11_2': ['콘텐츠를'], 'l11_4': ['따라'], 'l11_5': ['아니라', '아닌'],
    'l12_1': ['자산을'], 'l12_2': ['바탕으로', '맞춰', '지원하는'], 'l12_3': ['재능교육은', '통해'],
}
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording (none: this video is read by the TTS clone)
CLONE = set()
# tts mode: a take chosen by ear or by the phoneme check, instead of the automatic pick ({line id: index in the sorted takes})
# l4_2: the take whose pitch stays level (review 2026-11-04: the voice suddenly dropped low at 2:00, median F0 124 Hz vs ~170 elsewhere)
# picked by ear-substitute checks (isolated whisper of the name + wav2vec2 phonemes of the whole take, trailing silence >= 0.2 s):
# JEI as 제이 이아이 (not 제아이), JEI-SLI 에셀아이, POD 피오디 (not 푸디 / 피디), LLM 엘엘엠, Knowledge with /a/ first (not 놀) and 맵 with no vowel after p
# l8_3 ~ l8_5 (rewritten 2026-11-05): POD 피오디 (not 피디 / 피우디), DB 디비, 목표별로 미리 clear, F0 level to the end (l8_5 take 6 fell to 122 Hz).
# l6_1: kept the take it had before (the new lines moved the median pace, and with it the automatic pick)
TAKE = {'l1_3': 9, 'l4_2': 4, 'l4_3': 1, 'l5_1': 1, 'l6_1': 5, 'l6_4': 2, 'l7_3': 0, 'l7_6': 2, 'l8_3': 5, 'l8_4': 2, 'l8_5': 7, 'l11_5': 3, 'l12_2': 2}

# the same pacing as ../ai-learning-platform-v3-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.8, 3.2   # s before the first line, between lines, extra between pages, after the last line
# lines that finish the sentence of the line before on the next scene of the same sheet: only this pause (s) before them, not GAP + SCENE_GAP
# (review 2026-11-04: 2.4 s of silence at the comma in l6_3 / l6_4)
JOIN = {'l6_4': .35}
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line (the script has no thank-you line)
