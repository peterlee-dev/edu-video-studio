# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: the English script received 2026.11.06 (one paragraph per deck page, word for word), with the 2026.11.07 review (US JEI소개영상 피드백 sheet) rewordings and the US COO's follow-up (60-minute again, SOCi added) and third review (Hong Kong, SOCi line reworded). Deck: Overview of JEI Learning Centers, LLC (3).pdf (11 pages)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Overview of JEI Learning Centers, LLC'), ('contents', 'Contents'),
    # 01 company overview (deck p.3–6)
    ('story', 'Our story: from Korea to North America'), ('business', 'Business model'), ('centers', 'JEI Learning Centers'),
    ('decline', 'Number of centers over the years'), ('subjects', 'JEI subjects and grades'),
    # 02 programs and competitive analysis (deck p.7–8)
    ('programs', 'JEI programs'), ('landscape', 'Competitive programs landscape'),
    # 03 franchise business structure (deck p.9–10)
    ('tuition', 'Tuition and royalty structure'), ('rivals', 'JEI and competitors'),
    # websites and social media (deck p.11) · closing
    ('web', 'JEI websites and social media'), ('outro', 'Closing'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # deck p.1 · title
    ('l1_1', 'title', "Welcome to JEI Learning Centers.", "Welcome to J-E-I Learning Centers.", 0),
    ('l1_2', 'title', "JEI provides personalized education through the JEI Self-Learning Method.",
     "J-E-I provides personalized education through the J-E-I Self-Learning Method.", 0),
    ('l1_3', 'title', "Our goal is to help students learn independently, build confidence, and develop good study habits.", None, .2),
    # deck p.2 · contents
    ('l1_4', 'contents', "Today, we will introduce JEI Learning Centers in North America.", "Today, we will introduce J-E-I Learning Centers in North America.", 0),
    ('l1_5', 'contents', "First, we will provide a company overview, including our history, business model, and students.", None, 0),
    ('l1_6', 'contents', "Next, we will introduce our learning programs and compare them with major competitors.", None, 0),
    ('l1_7', 'contents', "Finally, we will explain our franchise business structure and online platforms.", None, .2),

    # deck p.3 · our story
    ('l2_1', 'story', "JEI was founded by Sung Hoon Park in South Korea.", "J-E-I was founded by Sung Hoon Park in South Korea.", 0),
    ('l2_2', 'story', "He developed the JEI Self-Learning Method to help students learn at their own pace in small steps.",
     "He developed the J-E-I Self-Learning Method to help students learn at their own pace in small steps.", 0),
    ('l2_3', 'story', "In 1992, JEI Learning Centers was established in the United States.",
     "In nineteen ninety-two, J-E-I Learning Centers was established in the United States.", 0),
    ('l2_4', 'story', "Since then, JEI has expanded into several international markets, including Canada, Australia, New Zealand and Hong Kong.",
     "Since then, J-E-I has expanded into several international markets, including Canada, Australia, New Zealand and Hong Kong.", .2),
    # deck p.4 · business model
    ('l2_5', 'business', "JEI operates after-school learning centers where students study at their individual learning levels.",
     "J-E-I operates after-school learning centers where students study at their individual learning levels.", 0),
    ('l2_6', 'business', "Students typically visit a center once a week for a 60-minute session.",
     "Students typically visit a center once a week for a sixty-minute session.", 0),
    ('l2_7', 'business', "Our classes have a teacher-to-student ratio of one to five, allowing teachers to provide personalized coaching.", None, 0),
    ('l2_8', 'business', "Students also receive one workbook per subject each week to support continued learning at home.", None, .2),
    # deck p.5 · learning centers (the map, then the trend)
    ('l2_9', 'centers', "As of June 2026, JEI operates 54 learning centers across North America, with 44 in the United States and 10 in Canada.",
     "As of June twenty twenty-six, J-E-I operates fifty-four learning centers across North America, with forty-four in the United States and ten in Canada.", 0),
    ('l2_10', 'centers', "Our major locations include California, New Jersey, and New York.", None, .2),
    ('l2_11', 'decline', "However, the number of JEI centers has declined significantly over the past several years.",
     "However, the number of J-E-I centers has declined significantly over the past several years.", 0),
    ('l2_12', 'decline', "While major competitors have recovered and expanded, JEI continues to face challenges in strengthening its market position.",
     "While major competitors have recovered and expanded, J-E-I continues to face challenges in strengthening its market position.", 0),
    ('l2_13', 'decline', "This highlights the need for clearer brand positioning and stronger competitiveness.", None, .2),
    # deck p.6 · subjects and grades
    ('l2_14', 'subjects', "Math and English are JEI's two main subjects.", "Math and English are J-E-I's two main subjects.", 0),
    ('l2_15', 'subjects', "Math accounts for 53.6 percent of total subject enrollments, while English accounts for 41.3 percent.",
     "Math accounts for fifty-three point six percent of total subject enrollments, while English accounts for forty-one point three percent.", 0),
    ('l2_16', 'subjects', "Together, they represent nearly 95 percent of our business.", "Together, they represent nearly ninety-five percent of our business.", .2),
    ('l2_17', 'subjects', "More than 60 percent of our students are in grades two through six.", "More than sixty percent of our students are in grades two through six.", 0),
    ('l2_18', 'subjects', "This shows that elementary Math and English are the core of JEI's current business.",
     "This shows that elementary Math and English are the core of J-E-I's current business.", .3),

    # deck p.7 · programs
    ('l3_1', 'programs', "JEI offers four main learning programs.", "J-E-I offers four main learning programs.", 0),
    ('l3_2', 'programs', "JEI Math helps students develop mathematical understanding through step-by-step learning.",
     "J-E-I Math helps students develop mathematical understanding through step-by-step learning.", 0),
    ('l3_3', 'programs', "Problem Solving Math develops advanced problem-solving skills.", None, 0),
    ('l3_4', 'programs', "JEI English builds a strong foundation in phonics, grammar, vocabulary, and reading comprehension.",
     "J-E-I English builds a strong foundation in phonics, grammar, vocabulary, and reading comprehension.", 0),
    ('l3_5', 'programs', "The JEI Pen also supports pronunciation and listening.", "The J-E-I Pen also supports pronunciation and listening.", 0),
    ('l3_6', 'programs', "Finally, Reading and Writing strengthens reading comprehension, writing skills, and creativity.", None, .2),
    # deck p.8 · competitive landscape
    ('l3_8', 'landscape', "JEI competes with major learning brands such as Kumon, Mathnasium, and Eye Level.",
     "J-E-I competes with major learning brands such as Kumon, Mathnasium, and Eye Level.", 0),
    ('l3_9', 'landscape', "Each company has different strengths.", None, 0),
    ('l3_10', 'landscape', "Kumon focuses on repetition and calculation skills.", None, 0),
    ('l3_11', 'landscape', "Mathnasium emphasizes personalized math instruction and coaching.", None, 0),
    ('l3_12', 'landscape', "Eye Level combines foundational math skills with critical thinking.", None, .2),
    ('l3_13', 'landscape', "JEI's strengths include structured workbooks, individualized learning, and personalized teacher support.",
     "J-E-I's strengths include structured workbooks, individualized learning, and personalized teacher support.", 0),
    ('l3_14', 'landscape', "However, we also need to improve our content, digital learning options, and consistency across centers.", None, .3),

    # deck p.9 · tuition & royalty
    ('l4_1', 'tuition', "Now, let's look at our franchise business structure.", None, 0),
    ('l4_2', 'tuition', "JEI's monthly tuition generally ranges from 130 to 180 dollars, depending on the center.",
     "J-E-I's monthly tuition generally ranges from one hundred thirty to one hundred eighty dollars, depending on the center.", 0),
    ('l4_3', 'tuition', "This is lower than Mathnasium's typical tuition range.", None, .2),
    ('l4_4', 'tuition', "JEI also uses a tiered royalty structure, with lower fees as subject enrollments increase.",
     "J-E-I also uses a tiered royalty structure, with lower fees as subject enrollments increase.", 0),
    ('l4_5', 'tuition', "This structure helps support franchise operations as centers grow.", None, .2),
    # deck p.10 · JEI & competitors
    ('l4_6', 'rivals', "JEI entered the U.S. market in 1992.", "J-E-I entered the U.S. market in nineteen ninety-two.", 0),
    ('l4_7', 'rivals', "Today, we compete with well-established brands, including Kumon, Mathnasium, and Eye Level.", None, 0),
    ('l4_8', 'rivals', "Over recent years, Kumon and Mathnasium have continued to expand, while JEI's network has become smaller.",
     "Over recent years, Kumon and Mathnasium have continued to expand, while J-E-I's network has become smaller.", 0),
    ('l4_9', 'rivals', "This comparison shows why JEI needs to strengthen its competitive position and support future growth.",
     "This comparison shows why J-E-I needs to strengthen its competitive position and support future growth.", .3),

    # deck p.11 · websites and social media
    ('l5_1', 'web', "Finally, JEI connects with customers and franchise partners through several online platforms.",
     "Finally, J-E-I connects with customers and franchise partners through several online platforms.", 0),
    ('l5_2', 'web', "Our main website introduces JEI's history, programs, and learning centers.",
     "Our main website introduces J-E-I's history, programs, and learning centers.", 0),
    ('l5_3', 'web', "Each center also has its own website with local information and appointment scheduling.", None, 0),
    ('l5_4', 'web', "Our franchise website provides information for potential business partners.", None, 0),
    ('l5_5', 'web', "We also connect with families through Facebook, Instagram, and TikTok, with AI support from SOCi.",
     "We also connect with families through Facebook, Instagram, and TikTok, with A-I support from So-see.", .2),
    # closing
    ('l5_6', 'outro', "JEI remains committed to its vision: “A Better Life Through Better Education.”",
     "J-E-I remains committed to its vision: A Better Life Through Better Education.", .4),
    ('l5_7', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # no chime before the closing line (as in ../jei-corporation-overview-female)

PACE = 14.31   # the pace the first picks were made at, so extra takes of one line (l5_7) don't move the other lines' picks
TAKE = {'l5_7': 8}   # l5_7: of 13 takes (one silent take dropped) most turn back up on "you"; file _5 (sorted position 8) falls 167 → 150 Hz and stays down (Praat, floor 75 Hz), phonemes θ ɛ ŋ k uː, 0.24 s breath after. line id → take index (sorted take position) where the picked take reads wrong or clips its end
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female English, ../adaptive-diagnosis-v2/audio/narration.mp3)
VOICE = 'voice_ref'
