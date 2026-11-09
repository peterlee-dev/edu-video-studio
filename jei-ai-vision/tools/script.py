# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: the English narration script sent with the review sheet 어댑티브진단&AI플랫폼 소개_ 영상 수정 요청.pdf (2026-11-05), 12 sections
# that follow the 12 pages of ../jei-ai-vision-ko (JEI_AI플랫폼_동영상장면.pptx.pdf). Lines are word for word; only the leading space
# before "Now," is dropped. Line ids: l<section>_<n>.
# 2nd review (same sheet name, 2026-11-05 17:00): l4_4 · l5_1 · l11_2 global map / each country’s curriculum, l7_3 · l8_3 without step-by-step
# 3rd review (same sheet name, 2026-11-06): page 2 (why, l2_1 ~ l2_5) dropped, the voice changed to the adaptive-diagnosis female voice,
# page 8 redrawn as two panels (content pool / personalized delivery)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', 'Opening'),
          ('kmapList', 'The knowledge map: a list'), ('kmapDots', 'The knowledge map: points and lines'), ('kmapAI', 'The knowledge map: what AI decides'),
          ('universe', 'How the map is built'),
          ('country', 'What the map makes possible'), ('countryTrack', 'What the map makes possible: each student'),
          ('layers', 'Three layers: knowledge'), ('layerAgent', 'Three layers: AI engine'), ('layerService', 'Three layers: service'), ('layerPace', 'Three layers: stable and flexible'),
          ('roadmap', 'Seven projects, two phases'), ('phase1', 'Roadmap: Phase 1'), ('phase2', 'Roadmap: Phase 2'), ('wiki', 'Roadmap: LLM Wiki'),
          ('pod', 'Phase 1: Personalized POD'), ('podCycle', 'POD: the next round · rollout'),
          ('online', 'Phase 2: Adaptive online learning'), ('assistant', 'AI learning assistant'),
          ('statusMap', 'A student’s progress on the map'), ('statuses', 'Four statuses'), ('statusUpdate', 'Updates · next path'),
          ('change1', 'Benefit 1'), ('change2', 'Benefit 2'), ('change3', 'Benefit 3'), ('change4', 'Benefit 4'),
          ('outro', 'Closing')]
# scenes that continue the page before on the same sheet (one page told in several steps): no page turn and no whoosh
# (index.html SHARED draws the part of the page that stays)
CONT = {'kmapDots', 'kmapAI', 'countryTrack', 'layerAgent', 'layerService', 'layerPace', 'phase1', 'phase2', 'wiki',
        'podCycle', 'assistant', 'statuses', 'statusUpdate', 'change2', 'change3', 'change4'}
WHOOSH = False   # no whoosh at page turns (2026-11-06, as in ../jei-math-difference)

# read forms (the screen keeps the written form). Review 2026-11-05: POD as P.O.D and JEI as J.E.I, letter by letter
# (the voice said "pod"); written with hyphens, as in ../jei-corporation-overview, so the letters don't end a sentence.
# make_audio.py also applies SAY to whisper's transcripts
SAY = [('JEI-SLI', 'J-E-I S-L-I'), ('JEI', 'J-E-I'), ('POD', 'P-O-D'), ('50 years', 'fifty years')]
def R(s):
    for a, b in SAY + [('’', "'")]:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    # [1] Opening
    ('l1_1', 'title', 'Over the past 50 years, JEI has built deep expertise in learning design.', .2),
    ('l1_2', 'title', 'Now, by combining that expertise with AI, we aim to deliver learning optimized for every student and set a new global standard for AI-powered math learning.', .1),
    ('l1_3', 'title', 'Here is our plan: building an AI personalized learning platform based on the JEI Math Knowledge Map.', 0),

    # [3] The knowledge map
    ('l3_1', 'kmapList', 'The foundation of this platform is the JEI Math Knowledge Map.', .1),
    ('l3_2', 'kmapList', 'For AI to give each student exactly what they need, it must understand how learning objectives relate to one another, and in what order they should be learned.', 0),
    ('l3_3', 'kmapDots', 'Think of it as connecting countless stars scattered across space.', 0),
    ('l3_4', 'kmapDots', 'We define how individual learning objectives connect and organize them into one network.', .1),
    ('l3_5', 'kmapDots', 'Each point represents a learning objective.', 0),
    ('l3_6', 'kmapDots', 'The lines between points show how skills build on one another, such as prerequisite and follow-up relationships.', 0),
    ('l3_7', 'kmapDots', 'Line color and thickness show the type and strength of each connection.', 0),
    ('l3_8', 'kmapAI', 'With this network, AI can understand the overall structure of math learning, and decide what each student needs to review and what to learn next.', 0),

    # [4] How the map is built
    ('l4_1', 'universe', 'We’re building the JEI Math Knowledge Map around JEI’s educational philosophy, along with our workbooks, learning objectives, and curricula from Korea and North America.', .1),
    ('l4_2', 'universe', 'AI then compares these with textbooks, curricula, and learning standards from different countries, including the U.S. Common Core State Standards, and proposes how learning objectives connect.', 0),
    ('l4_3', 'universe', 'JEI researchers review these proposals for educational soundness.', .1),
    ('l4_4', 'universe', 'The result is a global math knowledge map, one that isn’t tied to any single country’s curriculum and can be used anywhere, in Korea and overseas.', 0),
    ('l4_5', 'universe', 'We call it the JEI Math Universe.', 0),

    # [5] What the map makes possible
    ('l5_1', 'country', 'By aligning this global map with each country’s curriculum, we can develop and validate learning content for different markets much more quickly.', 0),
    ('l5_2', 'country', 'When we enter a new market, we don’t have to start from scratch.', 0),
    ('l5_3', 'country', 'We connect that country’s curriculum and learning standards to the knowledge map, and build the content we need.', 0),
    ('l5_4', 'countryTrack', 'And by linking each student’s results to the map, we can see what they understand, where they need help, and how their learning changes over time.', .1),
    ('l5_5', 'countryTrack', 'In short, the JEI Math Knowledge Map helps us develop products for each market faster, and personalize learning for every student.', 0),

    # [6] Three layers
    ('l6_1', 'layers', 'The platform has three connected layers: knowledge, AI engine, and service.', 0),
    ('l6_2', 'layers', 'We build them step by step, from the bottom up.', .1),
    ('l6_3', 'layers', 'The knowledge layer turns JEI’s learning materials and educational expertise into the knowledge map, a shared foundation AI can use.', 0),
    ('l6_4', 'layerAgent', 'The AI engine layer uses that foundation to generate content and analyze learning progress.', 0),
    ('l6_5', 'layerService', 'Finally, the service layer delivers these capabilities to students through POD and online learning.', 0),
    ('l6_6', 'layerPace', 'Once built, the knowledge layer stays relatively stable, while the service layer can evolve quickly as technology and learning environments change.', 0),

    # [7] Seven projects, two phases
    ('l7_1', 'roadmap', 'Seven interconnected projects will move forward in two phases.', 0),
    ('l7_2', 'phase1', 'Phase 1 focuses on the knowledge map and automated content generation.', .1),
    ('l7_3', 'phase1', 'AI creates programmed learning materials in advance, and we deliver them through personalized POD.', 0),
    ('l7_4', 'phase2', 'Phase 2 expands into online learning through progress analysis, adaptive learning paths, and an AI learning assistant.', .1),
    ('l7_5', 'phase2', 'The system analyzes each student’s understanding and progress as they learn, and adjusts their learning path in real time.', 0),
    ('l7_6', 'wiki', 'Throughout both phases, LLM Wiki serves as a shared knowledge base that organizes JEI’s educational knowledge and supports every project.', 0),

    # [8] Phase 1: Personalized POD
    ('l8_1', 'pod', 'The centerpiece of Phase 1 is personalized POD.', .2),
    ('l8_2', 'pod', 'First, we analyze each student’s assessment results and learning history to identify what they need to study and how much practice they need.', 0),
    ('l8_3', 'pod', 'AI generates programmed learning materials in advance for each learning objective.', 0),
    ('l8_4', 'pod', 'JEI researchers review them, and they’re stored in a content database.', .1),
    ('l8_5', 'pod', 'From this reviewed content, we create and print personalized materials for each student.', 0),
    ('l8_6', 'podCycle', 'The student’s results then shape the next round of learning, adding review where needed and adjusting the amount of practice.', .1),
    ('l8_7', 'podCycle', 'We’ll launch this service in the United States first, validate the results, and then expand to Korea.', 0),

    # [9] Phase 2: Adaptive online learning
    ('l9_1', 'online', 'In Phase 2, we extend this approach online.', .2),
    ('l9_2', 'online', 'Along with correct and incorrect answers, the system analyzes learning behaviors, including time spent on problems, hint usage, and repeated attempts.', 0),
    ('l9_3', 'online', 'It uses those insights to adjust each student’s content and learning path in real time.', 0),
    ('l9_4', 'assistant', 'The AI learning assistant supports both students and teachers.', .1),
    ('l9_5', 'assistant', 'For students, it provides hints and explanations rather than simply giving answers, so they can solve problems on their own.', .1),
    ('l9_6', 'assistant', 'For teachers, it shows each student’s progress and challenges, so they can guide and coach each student more effectively.', 0),

    # [10] A student's progress on the map
    ('l10_1', 'statusMap', 'This screen shows a student’s progress on the knowledge map.', .1),
    ('l10_2', 'statusMap', 'The bottom shows concepts already studied, the middle shows concepts being learned, and the top shows concepts not yet studied.', 0),
    ('l10_3', 'statuses', 'Each objective is classified as mastered, needs more practice, learning gap, or not yet studied.', 0),
    ('l10_4', 'statusUpdate', 'These statuses are updated whenever new assessment and learning data come in.', .1),
    ('l10_5', 'statusUpdate', 'So even if a concept was studied earlier, any gap that appears is filled, and the next learning path is adjusted.', .1),
    ('l10_6', 'statusUpdate', 'Students don’t repeat what they already know, they get the practice they need, and each student follows their own learning path.', 0),

    # [11] Four key benefits
    ('l11_1', 'change1', 'We expect four key benefits.', .2),
    ('l11_2', 'change1', 'First, we can develop and validate content aligned with each country’s curriculum more quickly.', 0),
    ('l11_3', 'change2', 'Second, we can personalize learning objectives and the amount of practice across POD and online learning, delivering the right content at the right time.', 0),
    ('l11_4', 'change3', 'Third, we can fill learning gaps and adjust each student’s learning path in real time, based on their understanding and progress.', 0),
    ('l11_5', 'change4', 'Finally, by considering academic achievement alongside the JEI Self-Learning Index, or JEI-SLI, we can show each student’s growth over time to students, teachers, and parents.', .1),
    ('l11_6', 'change4', 'Students are compared not with others, but with their own past progress.', 0),

    # [12] Closing
    ('l12_1', 'outro', 'Turning 50 years of learning design expertise into knowledge AI can understand and use.', .1),
    ('l12_2', 'outro', 'This is where the project begins.', .2),
    ('l12_3', 'outro', 'On this foundation, we’ll develop learning content for each market more quickly, and build JEI’s own AI personalized learning platform that supports every student’s learning and growth.', .3),
    ('l12_4', 'outro', 'Through this, JEI will further advance the value of individualized, ability-based learning, and set a new global standard for AI-powered math learning.', 0),
]
READ = {}
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(s)), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording (none: this video is read by the TTS clone)
CLONE = set()
# tts mode: a take chosen by ear or by the phoneme check, instead of the automatic pick ({line id: index in the sorted takes})
# l12_4 (the closing line, read 10 times): every take says "learn-" creaky low and lifts on "-ing"; take 0 falls 262 → 244 → 105 Hz to the end
TAKE = {'l12_4': 0}
PACE = 14.82   # pace of the first full read with the adaptive female voice (chars/s): extra takes for one line don't move the other lines' picks

# the same pacing as ../jei-ai-vision-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .5, 1.6, 3.2   # s before the first line, between lines, extra between pages, after the last line
JOIN = {}               # no sentence is split across scenes here
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line (the script has no thank-you line)
