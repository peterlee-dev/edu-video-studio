# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: the English script pasted on 2026.11.04, revised 2026.11.05 (one paragraph per deck page, word for word; its opening line "Let me start with a brief overview of JEI Corporation." left out). Deck: 1. Overview of JEI Corporation_v4 (1).pdf (20 pages)
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
    # deck p.1–2 (the script's opening "Let me start with a brief overview of JEI Corporation." is left out)
    ('l1_1', 'title', "JEI is an integrated education and culture company headquartered in South Korea.",
     "J-E-I is an integrated education and culture company headquartered in South Korea.", 0),
    ('l1_2', 'title', "Since our founding in 1977, we have focused on helping students reach their full potential through personalized education.",
     "Since our founding in nineteen seventy-seven, we have focused on helping students reach their full potential through personalized education.", .3),
    ('l1_3', 'contents', "We will now introduce six key areas: our business, the JEI Self-Learning Method, history, organization, subsidiaries, and global operations.",
     "We will now introduce six key areas: our business, the J-E-I Self-Learning Method, history, organization, subsidiaries, and global operations.", .2),

    # deck p.3 · what we do
    ('l2_1', 'whatWeDo', "Under the leadership of our founder and chairman, Sung Hoon Park, the company has grown into an international education organization.", None, 0),
    ('l2_2', 'whatWeDo', "Today, we provide a wide range of services in education, research, technology, and culture, offering comprehensive educational solutions.", None, .2),
    # deck p.4 · business model
    ('l2_3', 'business', "We provide personalized learning through three business models: home visits, learning centers, and online learning.", None, 0),
    ('l2_4', 'business', "We design each student's learning program based on their diagnostic test results.", None, .2),
    # deck p.5 · philosophy, vision, mission & core values
    ('l2_5', 'values', "We believe everyone has the potential to learn and grow independently.", None, 0),
    ('l2_6', 'values', "Based on this belief, our vision is “A Better Life Through Better Education.”",
     "Based on this belief, our vision is, A Better Life Through Better Education.", .3),
    ('l2_7', 'values', "Through our Self-Learning System, we help students reach their full potential and build better lives.", None, .3),
    # deck p.6 · our programs
    ('l2_8', 'programs', "We offer a wide range of learning programs, including Math, English, Korean, Science, and Critical Thinking, as well as digital learning options.", None, .3),

    # deck p.7 · JEI self-learning method
    ('l3_1', 'method', "The JEI Self-Learning Method is the foundation of our education system.",
     "The J-E-I Self-Learning Method is the foundation of our education system.", 0),
    ('l3_2', 'method', "Through personalized learning based on each student's level and pace, we help students learn independently and develop good study habits.", None, 0),
    ('l3_3', 'method', "This process helps students build confidence and develop the ability to grow on their own.", None, .2),
    # deck p.8 · what makes it possible?
    ('l3_4', 'possible', "Three key elements make this possible: the JEI Self-Learning System and Self-Learning Materials, JEI teachers, and parents.",
     "Three key elements make this possible: the J-E-I Self-Learning System and Self-Learning Materials, J-E-I teachers, and parents.", 0),
    ('l3_5', 'possible', "Together, they support each student's learning and development.", None, .2),
    # deck p.9 · self-learning system flow
    ('l3_6', 'flow', "Our system begins with a diagnostic test to identify each student's starting point.", None, 0),
    ('l3_7', 'flow', "The results are provided in an individual diagnostic report, which helps us design a personalized learning path and select appropriate workbooks.", None, 0),
    ('l3_8', 'flow', "Then, we use regular evaluations, including Interim Evaluation Tests and Achievement Tests, to monitor progress and achievement.", None, 0),
    ('l3_9', 'flow', "These results help us adjust each student's future learning.", None, .3),

    # deck p.10 · history
    ('l4_1', 'history', "Over the decades, we have continued to expand, from launching JEI Math in 1981 to entering international markets in 1992 and introducing new digital learning programs.",
     "Over the decades, we have continued to expand, from launching J-E-I Math in nineteen eighty-one to entering international markets in nineteen ninety-two and introducing new digital learning programs.", .2),
    # deck p.11 · awards & recognition
    ('l4_2', 'awards', "Over the years, we have received numerous awards for educational quality, customer satisfaction, innovation, and brand excellence.", None, 0),
    ('l4_3', 'awards', "These achievements reflect our commitment to providing quality education.", None, .3),

    # deck p.12 · organization
    ('l5_1', 'org', "JEI is organized into specialized divisions for business operations, management, research and development, and global business.",
     "J-E-I is organized into specialized divisions for business operations, management, research and development, and global business.", 0),
    ('l5_2', 'org', "These divisions work closely together to continuously develop and improve our educational programs and services.", None, .3),

    # deck p.13 · printing & distribution
    ('l6_1', 'printing', "Our printing and distribution subsidiaries manage the production and delivery of educational materials.", None, 0),
    ('l6_2', 'printing', "This integrated system helps us maintain quality and ensure efficient distribution.", None, .2),
    # deck p.14 · university & training institution
    ('l6_3', 'university', "JEI University provides professional education across various fields.",
     "J-E-I University provides professional education across various fields.", 0),
    ('l6_4', 'university', "The JEI Training Institution supports employee development, leadership training, and educational programs.",
     "The J-E-I Training Institution supports employee development, leadership training, and educational programs.", .2),
    # deck p.15 · TV, English TV & eAcademy
    ('l6_5', 'tv', "JEI TV and English TV provide a wide range of educational content, extending learning beyond workbooks.",
     "J-E-I TV and English TV provide a wide range of educational content, extending learning beyond workbooks.", 0),
    ('l6_6', 'tv', "JEI eAcademy develops digital content and adaptive learning platforms based on the JEI Self-Learning Method, helping us improve our educational services to meet changing learning needs.",
     "J-E-I e-Academy develops digital content and adaptive learning platforms based on the J-E-I Self-Learning Method, helping us improve our educational services to meet changing learning needs.", .2),
    # deck p.16 · culture
    ('l6_7', 'culture', "Beyond education, we support arts and culture through the JEI Culture Foundation.",
     "Beyond education, we support arts and culture through the J-E-I Culture Foundation.", 0),
    ('l6_8', 'culture', "Our Creative Center and Art Center provide spaces for creativity, cultural activities, and artistic development.", None, .2),
    # deck p.17 · global network
    ('l6_9', 'network', "JEI has expanded its global network across South Korea, the United States, Canada, Hong Kong, Australia, and New Zealand.", "J-E-I has expanded its global network across South Korea, the United States, Canada, Hong Kong, Australia, and New Zealand.", 0),
    ('l6_10', 'network', "Through this network, we provide personalized education based on the JEI Self-Learning Method to students around the world.", "Through this network, we provide personalized education based on the J-E-I Self-Learning Method to students around the world.", .3),

    # deck p.18 · global JEI
    ('l7_1', 'global', "Our global expansion began in the United States in 1992, followed by New Zealand, Hong Kong, and Australia.",
     "Our global expansion began in the United States in nineteen ninety-two, followed by New Zealand, Hong Kong, and Australia.", 0),
    ('l7_2', 'global', "Today, our international learning centers help students learn independently, build confidence, and develop good study habits.", None, .2),
    # deck p.19 · programmed workbooks
    ('l7_3', 'workbooks', "In international markets, we offer a variety of English-language workbooks, including JEI Math, Problem Solving Math, JEI English, and Reading & Writing.", "In international markets, we offer a variety of English-language workbooks, including J-E-I Math, Problem Solving Math, J-E-I English, and Reading and Writing.", 0),
    ('l7_4', 'workbooks', "Based on individual diagnostic test results, we provide workbooks suited to each student's level, helping students learn independently at their own pace.", None, .2),
    # deck p.20 · global awards & closing
    ('l7_5', 'globalAwards', "In 2016, we ranked 37th among the Top Global Franchises and 175th in Entrepreneur's Franchise 500.",
     "In twenty sixteen, we ranked thirty-seventh among the Top Global Franchises and one hundred seventy-fifth in Entrepreneur's Franchise five hundred.", .2),
    ('l7_6', 'outro', "Building on decades of educational experience, we will continue working toward our vision: “A Better Life Through Better Education.”",
     "Building on decades of educational experience, we will continue working toward our vision: A Better Life Through Better Education.", .4),
    ('l7_7', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # no chime before the closing line (as in ../jei-corporation-overview)

PACE = 15.06   # the pace the 2026.11.05 picks were made at, so l7_7's 14 extra takes (review 1) don't move the other lines' picks
TAKE = {'l7_7': 10}   # l7_7 (review 1, 2026.11.03: "you" should fall): of 14 takes most turn back up to 220–250 Hz in the last 50 ms of "you"; file _6 (sorted position 10) falls 164 → 115 Hz and stays down (Praat, floor 75 Hz), phonemes θ eɪ ŋ k uː. line id → take index (sorted take position) where the picked take reads wrong or clips its end
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female English, ../adaptive-diagnosis-v2/audio/narration.mp3)
VOICE = 'voice_ref'
