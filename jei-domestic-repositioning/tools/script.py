# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: "JEI Repositioning Strategy — English Video Narration Script", pasted in the request (2026.11.06), one section per deck page, word for word.
# Deck: JEI_리포지셔닝_재구성_발표자료_20261105_2022 (1) (2).pptx (21 pages, Korean, 재능교육 | 국내 리포지셔닝, 2026.11.06 스스로사업본부)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'JEI Repositioning Strategy'), ('market', 'Changes in the market'), ('competition', 'Competitive environment'),
    ('competitors', 'Key competitor strategies'), ('current', 'Current brand positioning'), ('direction', 'New direction for differentiation'),
    ('perception', 'Current brand perception'), ('parents', 'What parents want'), ('grades', 'Learning needs by grade'),
    ('target', 'Core target customers'), ('challenge', 'Our strategic challenge'), ('strengths', "JEI's core strengths"),
    ('principles', 'Principles of differentiation'), ('targetPos', 'Target positioning'), ('final', 'Final brand positioning'),
    ('elements', 'Key elements of positioning'), ('action', 'Turning positioning into action'), ('message', 'Customer communication'),
    ('success', 'Key success strategy'), ('plans', 'Key action plans'), ('outro', 'Conclusion'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # p.01 · JEI Repositioning Strategy
    ('l1_1', 'title', "Today, I would like to share JEI's repositioning strategy in Korea.", "Today, I would like to share J-E-I's repositioning strategy in Korea.", .2),
    ('l1_2', 'title', "Our goal is to become a brand that uses precise assessments to design the right learning path for each child and helps children develop the ability to grow independently.", None, .3),

    # p.02 · changes in the market
    ('l2_1', 'market', "The traditional home-visit education market is facing challenges due to the declining number of school-age children and the growing range of education options.", None, .1),
    ('l2_2', 'market', "From 2021 to 2025, the number of potential customers aged 4 to 14 decreased by about 14.6%.",
     "From twenty twenty-one to twenty twenty-five, the number of potential customers aged four to fourteen decreased by about fourteen point six percent.", .1),
    ('l2_3', 'market', "We now compete with a wider range of education services for a smaller number of customers.", None, .3),

    # p.03 · competitive environment
    ('l3_1', 'competition', "Our competition goes beyond traditional home-visit education.", None, 0),
    ('l3_2', 'competition', "Smart learning services, large private academies, local learning centers, and digital workbooks are all competing for parents' time and education budgets.", None, .1),
    ('l3_3', 'competition', "This makes it important for JEI to build a clear competitive advantage.", "This makes it important for J-E-I to build a clear competitive advantage.", .3),

    # p.04 · key competitor strategies
    ('l4_1', 'competitors', "Major education companies are following different strategies.", None, 0),
    ('l4_2', 'competitors', "Daekyo focuses on learning centers, Kumon combines paper-based and digital learning, and Woongjin focuses on AI-based learning programs.",
     "Daekyo focuses on learning centers, Kumon combines paper-based and digital learning, and Woongjin focuses on A-I-based learning programs.", .1),
    ('l4_3', 'competitors', "JEI needs to expand its existing assessment strengths across different subjects.", "J-E-I needs to expand its existing assessment strengths across different subjects.", .3),

    # p.05 · current brand positioning
    ('l5_1', 'current', "JEI's current image of self-learning partly overlaps with Kumon's focus on study habits and independent learning.",
     "J-E-I's current image of self-learning partly overlaps with Kumon's focus on study habits and independent learning.", .1),
    ('l5_2', 'current', "To stand out, JEI needs to focus on precise assessments and personalized learning paths.", "To stand out, J-E-I needs to focus on precise assessments and personalized learning paths.", .3),

    # p.06 · new direction for differentiation
    ('l6_1', 'direction', "Independent learning is not the starting point.", None, 0),
    ('l6_2', 'direction', "It is the final goal.", None, .2),
    ('l6_3', 'direction', "We need to design learning paths based on precise assessments and support each child's growth through teacher coaching and regular progress reviews.", None, .3),

    # p.07 · current brand perception
    ('l7_1', 'perception', "JEI has a long history, a trusted reputation, structured learning materials, and strong assessment capabilities.",
     "J-E-I has a long history, a trusted reputation, structured learning materials, and strong assessment capabilities.", .1),
    ('l7_2', 'perception', "However, parents may not clearly understand why they should choose JEI today.", "However, parents may not clearly understand why they should choose J-E-I today.", .1),
    ('l7_3', 'perception', "Changing this perception is an important priority.", None, .3),

    # p.08 · what parents want
    ('l8_1', 'parents', "Parents want to understand their child's current learning level and receive learning programs that meet their child's needs.", None, .1),
    ('l8_2', 'parents', "They also want to see clear evidence of their child's progress.", None, .3),

    # p.09 · learning needs by grade
    ('l9_1', 'grades', "Learning needs change as children grow.", None, .1),
    ('l9_2', 'grades', "Preschool children need basic preparation.", None, 0),
    ('l9_3', 'grades', "Younger elementary students need good study habits.", None, 0),
    ('l9_4', 'grades', "Middle elementary students need support to prevent learning gaps.", None, 0),
    ('l9_5', 'grades', "Older elementary students need to prepare for middle school.", None, .2),
    ('l9_6', 'grades', "The common goal is to start with learning that fits each child.", None, .3),

    # p.10 · core target customers
    ('l10_1', 'target', "Our primary target customers are parents of children in Grades 1 through 4.", "Our primary target customers are parents of children in grades one through four.", .1),
    ('l10_2', 'target', "We will focus especially on parents who want to understand exactly where their children need additional support.", None, .3),

    # p.11 · our strategic challenge
    ('l11_1', 'challenge', "Our main challenge is one-size-fits-all learning that begins without proper assessment.", None, .1),
    ('l11_2', 'challenge', "We need to move away from simply following a fixed learning schedule without understanding each child's level and areas of difficulty.", None, .3),

    # p.12 · JEI's core strengths
    ('l12_1', 'strengths', "JEI has strong capabilities in diagnostic assessment, personalized learning progress, structured workbooks, paper-based learning, and teacher support.",
     "J-E-I has strong capabilities in diagnostic assessment, personalized learning progress, structured workbooks, paper-based learning, and teacher support.", .1),
    ('l12_2', 'strengths', "The key is to connect these strengths into one process: assessment, learning recommendations, learning, coaching, and reassessment.",
     "The key is to connect these strengths into one process. Assessment, learning recommendations, learning, coaching, and reassessment.", .3),

    # p.13 · principles of differentiation
    ('l13_1', 'principles', 'Words such as "self-learning," "personalized," and "AI" are no longer enough to set us apart.',
     "Words such as self-learning, personalized, and A-I, are no longer enough to set us apart.", .1),
    ('l13_2', 'principles', "JEI needs to provide a real learning experience that connects precise assessment, learning path design, teacher coaching, and clear evidence of progress.",
     "J-E-I needs to provide a real learning experience that connects precise assessment, learning path design, teacher coaching, and clear evidence of progress.", .3),

    # p.14 · target positioning
    ('l14_1', 'targetPos', "JEI's new positioning will focus on assessment-based learning design for individual growth.",
     "J-E-I's new positioning will focus on assessment-based learning design for individual growth.", .1),
    ('l14_2', 'targetPos', "Rather than focusing only on repetition or digital content, we will identify each child's learning needs, design the right learning path, and track their progress.", None, .3),

    # p.15 · final brand positioning
    ('l15_1', 'final', "JEI aims to become a brand that helps children develop the ability to grow independently through precise assessment and personalized learning design.",
     "J-E-I aims to become a brand that helps children develop the ability to grow independently through precise assessment and personalized learning design.", .2),
    ('l15_2', 'final', "Assessment gives parents a reason to choose JEI.", "Assessment gives parents a reason to choose J-E-I.", 0),
    ('l15_3', 'final', "Learning design is the core of our service.", None, 0),
    ('l15_4', 'final', "And independent growth is the final outcome.", None, .3),

    # p.16 · key elements of positioning
    ('l16_1', 'elements', "Our new positioning is based on a clear customer need and a clear solution.", None, .1),
    ('l16_2', 'elements', "We assess each child's current level, provide a personalized learning path and teacher coaching, and build trust through regular progress reviews.", None, .3),

    # p.17 · turning positioning into action
    ('l17_1', 'action', "Our strategy must go beyond creating a new brand message.", None, .1),
    ('l17_2', 'action', "Parents need to understand their child's learning gaps and what they need to study next.", None, 0),
    ('l17_3', 'action', "They should also be able to see changes in learning materials and progress over time.", None, .3),

    # p.18 · customer communication
    ('l18_1', 'message', "Our message to parents should be simple and clear.", None, .2),
    ('l18_2', 'message', '"The Right Learning for Every Child. The Power to Learn Independently."',
     "The right learning for every child. The power to learn independently.", .3),
    ('l18_3', 'message', "We will consistently communicate that JEI starts with precise assessment to identify what each child needs to learn now.",
     "We will consistently communicate that J-E-I starts with precise assessment to identify what each child needs to learn now.", .3),

    # p.19 · key success strategy
    ('l19_1', 'success', "Our success depends on connecting five elements: precise assessment, focused paper-based learning, teacher coaching, digital progress reports, and clear evidence of growth.",
     "Our success depends on connecting five elements. Precise assessment, focused paper-based learning, teacher coaching, digital progress reports, and clear evidence of growth.", .1),
    ('l19_2', 'success', "Parents should be able to see how their children are improving and understand their next learning goals.", None, .3),

    # p.20 · key action plans
    ('l20_1', 'plans', "We will focus on five key actions.", None, .1),
    ('l20_2', 'plans', "First, standardize assessment and learning recommendations.", None, 0),
    ('l20_3', 'plans', "Second, connect online and offline learning management.", None, 0),
    ('l20_4', 'plans', "Third, improve student retention and encourage learning across multiple subjects.", None, 0),
    ('l20_5', 'plans', "Fourth, focus on important grade transitions.", None, 0),
    ('l20_6', 'plans', "Fifth, develop local branches and learning centers into key assessment locations.", None, .3),

    # p.21 · conclusion
    ('l21_1', 'outro', "JEI's new positioning is clear.", "J-E-I's new positioning is clear.", .1),
    ('l21_2', 'outro', "We will design the right learning path for each child through precise assessment and help children develop the ability to grow independently.", None, .2),
    ('l21_3', 'outro', "This direction builds on JEI's long-standing philosophy:", "This direction builds on J-E-I's long-standing philosophy.", .1),
    ('l21_4', 'outro', '"We Believe in the Power of Self-Learning."', "We believe in the power of self-learning.", .4),
    ('l21_5', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # no chime before the thank-you (as in ../jei-repositioning-strategy)
# line id → take index (sorted take position) where the picked take reads wrong or clips its end
TAKE = {'l21_5': 1}   # the thank-you: take 1 falls (339 → 197 → 117 Hz); take 0 rises at the end
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female English, ../adaptive-diagnosis-v2/audio/narration.mp3)
VOICE = 'voice_ref'
