# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 국내 재능 회사 소개 (1).pdf (one script page per deck page, word for word), reworded by JEI소개영상 피드백 2026.11.03 - 국내 1차.pdf. Deck: 1. Overview of JEI Corporation_v4 (1).pdf (20 pages)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Overview of JEI Corporation'), ('contents', 'Contents'),
    # 01 what we do (deck p.3–6)
    ('whatWeDo', 'What we do'), ('business', 'Business model'), ('values', 'Philosophy, vision, mission & core values'), ('programs', 'Our programs'),
    # 02 self-learning method (deck p.7–9)
    ('method', 'JEI Self-Learning Method'), ('possible', 'What makes it possible?'), ('flow', 'Self-Learning System flow'),
    # 03 history (deck p.10–11)
    ('history', 'History'), ('awards', 'Awards & recognition'),
    # 04 organization (deck p.12)
    ('org', 'Organization'),
    # 05 subsidiaries (deck p.13–17)
    ('printing', 'JEI Printing & Distribution'), ('university', 'JEI University & Training Institution'), ('tv', 'JEI TV, English TV & eAcademy'),
    ('culture', 'JEI Culture'), ('network', 'Global network'),
    # 06 global JEI (deck p.18–20)
    ('global', 'Global JEI'), ('workbooks', 'JEI Programmed Workbooks'), ('globalAwards', 'Global awards'), ('outro', 'Closing'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # deck p.1–2
    ('l1_1', 'title', "Founded in 1977, JEI has been dedicated to helping learners reach their full potential through personalized education.",
     "Founded in nineteen seventy-seven, J-E-I has been dedicated to helping learners reach their full potential through personalized education.", .3),
    ('l1_2', 'contents', "Today, we'll introduce JEI's business, Self-Learning Method, history, organization, subsidiaries, and global operations.",
     "Today, we'll introduce J-E-I's business, Self-Learning Method, history, organization, subsidiaries, and global operations.", .2),

    # deck p.3 · what we do
    ('l2_1', 'whatWeDo', "Under the vision of our founder and chairman, Sung-hoon Park, the company has grown into a global education organization.", None, 0),
    ('l2_2', 'whatWeDo', "JEI combines education, research, technology, and cultural services to help students reach their full potential.",
     "J-E-I combines education, research, technology, and cultural services to help students reach their full potential.", .2),
    # deck p.4 · business model
    ('l2_3', 'business', "JEI provides individualized learning through three models: home visits, learning centers, and online learning.",
     "J-E-I provides individualized learning through three models: home visits, learning centers, and online learning.", 0),
    ('l2_4', 'business', "Each model is supported by diagnostic assessments that identify students' needs and guide their learning.", None, .2),
    # deck p.5 · philosophy, vision, mission & core values
    ('l2_5', 'values', "We believe every individual has the potential to learn and grow independently.", None, 0),
    ('l2_6', 'values', "Our vision is \u201cA Better Life Through Better Education.\u201d",
     "Our vision is, A Better Life Through Better Education.", .9),
    # deck p.6 · our programs
    ('l2_7', 'programs', "We offer a wide range of learning programs, including Math, English, Korean, Science, and Critical Thinking, as well as digital learning options.", None, .3),

    # deck p.7 · JEI self-learning method
    ('l3_1', 'method', "The JEI Self-Learning Method helps students learn independently, build confidence, and develop good study habits.",
     "The J-E-I Self-Learning Method helps students learn independently, build confidence, and develop good study habits.", 0),
    ('l3_2', 'method', "Through personalized learning and precise assessment, students progress at their own pace.", None, .2),
    # deck p.8 · what makes it possible?
    ('l3_3', 'possible', "The method combines JEI's scientific evaluation system with systematically designed self-learning workbooks.",
     "The method combines J-E-I's scientific evaluation system with systematically designed self-learning workbooks.", 0),
    ('l3_4', 'possible', "Together, they help students develop independent learning skills, confidence, and good study habits.", None, .2),
    # deck p.9 · self-learning system flow
    ('l3_5', 'flow', "The process begins with an individual diagnostic test.", None, 0),
    ('l3_6', 'flow', "Based on the results, JEI prescribes a personalized learning path for each student.",
     "Based on the results, J-E-I prescribes a personalized learning path for each student.", 0),
    ('l3_7', 'flow', "Interim Evaluation Tests, Achievement Tests, and Individual Progress Prescription Reports then guide each student's continued learning.", None, .3),

    # deck p.10 · history
    ('l4_1', 'history', "Over the decades, we have continued to expand, from launching JEI Math in 1981 to entering international markets in 1992 and introducing new digital learning programs.",
     "Over the decades, we have continued to expand, from launching J-E-I Math in nineteen eighty-one to entering international markets in nineteen ninety-two and introducing new digital learning programs.", .2),
    # deck p.11 · awards & recognition
    ('l4_3', 'awards', "Our commitment to educational quality, customer satisfaction, innovation, and brand excellence has earned us numerous awards and recognition.", None, 0),
    ('l4_4', 'awards', "These achievements demonstrate our ongoing efforts to deliver better educational experiences.", None, .3),

    # deck p.12 · organization
    ('l5_1', 'org', "JEI operates through specialized divisions covering business operations, management, research and development, and overseas expansion.",
     "J-E-I operates through specialized divisions covering business operations, management, research and development, and overseas expansion.", 0),
    ('l5_2', 'org', "This structure supports the continuous improvement of our educational services.", None, .3),

    # deck p.13 · printing & distribution
    ('l6_1', 'printing', "Our printing and distribution subsidiaries ensure the efficient production and delivery of educational materials.", None, .2),
    # deck p.14 · university & training institution
    ('l6_2', 'university', "JEI University provides professional education across various fields.",
     "J-E-I University provides professional education across various fields.", 0),
    ('l6_3', 'university', "The JEI Training Institution supports employee development, leadership training, and educational programs.",
     "The J-E-I Training Institution supports employee development, leadership training, and educational programs.", .2),
    # deck p.15 · TV, English TV & eAcademy
    ('l6_4', 'tv', "Our broadcasting subsidiary provides educational content through JEI TV and English TV, extending learning beyond workbooks.",
     "Our broadcasting subsidiary provides educational content through J-E-I TV and English TV, extending learning beyond workbooks.", 0),
    ('l6_5', 'tv', "JEI eAcademy develops digital content and adaptive learning platforms based on the Self-Learning Method.",
     "J-E-I e-Academy develops digital content and adaptive learning platforms based on the Self-Learning Method.", .2),
    # deck p.16 · culture
    ('l6_6', 'culture', "Through its cultural foundation, Creative Center, and Art Center, JEI supports creativity, arts, and cultural education.",
     "Through its cultural foundation, Creative Center, and Art Center, J-E-I supports creativity, arts, and cultural education.", .2),
    # deck p.17 · global network
    ('l6_7', 'network', "Our international network spans South Korea, the United States, Canada, Hong Kong, Australia, and New Zealand.", None, .3),

    # deck p.18 · global JEI
    ('l7_1', 'global', "Our global expansion began in the United States in 1992.",
     "Our global expansion began in the United States in nineteen ninety-two.", 0),
    ('l7_2', 'global', "Today, our international learning centers help students develop confidence and independent learning skills.", None, .2),
    # deck p.19 · programmed workbooks
    ('l7_3', 'workbooks', "We offer English-based workbooks in international markets, covering Math, English, Reading and Writing, and Problem Solving Math.", None, 0),
    ('l7_4', 'workbooks', "These workbooks support programmed learning, combined with customized diagnostic tests.", None, .2),
    # deck p.20 · global awards & closing
    ('l7_5', 'globalAwards', "In 2016, JEI was ranked 37th among the Top Global Franchises and 175th in Entrepreneur's Franchise 500.",
     "In twenty sixteen, J-E-I was ranked thirty-seventh among the Top Global Franchises and one hundred seventy-fifth in Entrepreneur's Franchise five hundred.", .2),
    ('l7_6', 'outro', "Building on decades of educational experience, JEI continues to pursue its mission: A Better Life Through Better Education.",
     "Building on decades of educational experience, J-E-I continues to pursue its mission: A Better Life Through Better Education.", .4),
    ('l7_7', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # no chime (1차 feedback 2026.11.03: the bell before the mission removed); 'l7_6' puts the rising chime back before the mission

TAKE = {'l2_2': 0, 'l7_7': 1}   # l2_2: take 1 reads the opening JEI as "jai"; l7_7: takes 0 and 2 say "sank you" (wav2vec2 phonemes). line id → take index (sorted take position) where the picked take reads wrong or clips its end
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_male = the D–I recording (../ai-learning-platform-v3/audio/voice_ref.wav, male);
# voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female, ver1; with it pin TAKE = {'l6_2': 1}: take 2 drops the J of the opening JEI)
VOICE = 'voice_male'
