# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 미주 재능 회사 소개 스크립트.pdf (one script page per deck page, word for word). Deck: 2. Overview of JEI Learning Centers, LLC.pdf (11 pages)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Overview of JEI Learning Centers, LLC'), ('contents', 'Contents'),
    # 01 company overview (deck p.3–6)
    ('story', 'Our story: from Korea to North America'), ('business', 'Business model'), ('centers', 'JEI Learning Centers'),
    ('decline', 'Number of centers over the years'), ('subjects', 'JEI subject & grade'),
    # 02 programs and competitive analysis (deck p.7–8)
    ('programs', 'JEI programs'), ('landscape', 'Competitive programs landscape'),
    # 03 franchise business structure (deck p.9–10)
    ('tuition', 'Tuition & royalty structure'), ('rivals', 'JEI & competitors'),
    # websites and social media (deck p.11) · closing
    ('web', 'JEI websites and social media'), ('outro', 'Closing'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # deck p.1 · title
    ('l1_1', 'title', "JEI Learning Centers is a supplementary education provider offering personalized learning across North America through the JEI Self-Learning Method.",
     "J-E-I Learning Centers is a supplementary education provider offering personalized learning across North America through the J-E-I Self-Learning Method.", 0),
    ('l1_2', 'title', "Our mission is \"A Better Life Through Better Education.\"",
     "Our mission is, A Better Life Through Better Education.", .2),
    # deck p.2 · contents
    ('l1_3', 'contents', "Today, we'll introduce JEI's North American operations, learning centers, educational programs, competitive landscape, and franchise business structure.",
     "Today, we'll introduce J-E-I's North American operations, learning centers, educational programs, competitive landscape, and franchise business structure.", .2),

    # deck p.3 · our story
    ('l2_1', 'story', "Founded by Chairman Sung-hoon Park, JEI introduced the Self-Learning Method to help students master concepts through individualized, step-by-step learning.",
     "Founded by Chairman Sung-hoon Park, J-E-I introduced the Self-Learning Method to help students master concepts through individualized, step-by-step learning.", 0),
    ('l2_2', 'story', "In 1992, JEI expanded into the United States, bringing its proven educational philosophy to North America.",
     "In nineteen ninety-two, J-E-I expanded into the United States, bringing its proven educational philosophy to North America.", .2),
    # deck p.4 · business model
    ('l2_3', 'business', "JEI operates franchise learning centers where students study at their individualized learning levels.",
     "J-E-I operates franchise learning centers where students study at their individualized learning levels.", 0),
    ('l2_4', 'business', "Students typically visit once a week for a 60-minute session, with a teacher-to-student ratio of one to five.",
     "Students typically visit once a week for a sixty-minute session, with a teacher-to-student ratio of one to five.", 0),
    ('l2_5', 'business', "Each student receives one workbook per subject per week, supporting independent learning at home.", None, .2),
    # deck p.5 · learning centers (map, then the trend)
    ('l2_6', 'centers', "As of June 2026, JEI operates 54 learning centers across the United States and Canada, with 44 in the U.S. and 10 in Canada.",
     "As of June twenty twenty-six, J-E-I operates fifty-four learning centers across the United States and Canada, with forty-four in the U.S. and ten in Canada.", .2),
    ('l2_7', 'decline', "However, the number of centers has declined from 105 in 2019.",
     "However, the number of centers has declined from one hundred five in twenty nineteen.", 0),
    ('l2_8', 'decline', "While major competitors have expanded, JEI faces challenges in rebuilding its market presence.",
     "While major competitors have expanded, J-E-I faces challenges in rebuilding its market presence.", 0),
    ('l2_9', 'decline', "This highlights the need to strengthen JEI's brand positioning and competitiveness.",
     "This highlights the need to strengthen J-E-I's brand positioning and competitiveness.", .2),
    # deck p.6 · subject & grade
    ('l2_10', 'subjects', "Math and English account for nearly 95 percent of JEI's total subject enrollments.",
     "Math and English account for nearly ninety-five percent of J-E-I's total subject enrollments.", 0),
    ('l2_11', 'subjects', "More than 60 percent of students are in grades two through six, making elementary education our core market.",
     "More than sixty percent of students are in grades two through six, making elementary education our core market.", 0),
    ('l2_12', 'subjects', "These results highlight the importance of Math and English in JEI's future product strategy.",
     "These results highlight the importance of Math and English in J-E-I's future product strategy.", .3),

    # deck p.7 · programs
    ('l3_1', 'programs', "JEI offers four main educational programs.",
     "J-E-I offers four main educational programs.", 0),
    ('l3_2', 'programs', "JEI Math develops conceptual understanding through step-by-step learning.",
     "J-E-I Math develops conceptual understanding through step-by-step learning.", 0),
    ('l3_3', 'programs', "Problem Solving Math strengthens advanced problem-solving skills.", None, 0),
    ('l3_4', 'programs', "JEI English builds a strong foundation in phonics, vocabulary, grammar, and reading, while JEI Reading and Writing develops comprehension, writing skills, and creativity.",
     "J-E-I English builds a strong foundation in phonics, vocabulary, grammar, and reading, while J-E-I Reading and Writing develops comprehension, writing skills, and creativity.", .2),
    # deck p.8 · competitive landscape
    ('l3_5', 'landscape', "We compared JEI with three major competitors: Kumon, Mathnasium, and Eye Level.",
     "We compared J-E-I with three major competitors: Kumon, Mathnasium, and Eye Level.", 0),
    ('l3_6', 'landscape', "JEI's strengths include structured workbooks, conceptual understanding, and personalized instruction.",
     "J-E-I's strengths include structured workbooks, conceptual understanding, and personalized instruction.", 0),
    ('l3_7', 'landscape', "However, limited content updates, insufficient digital integration, and inconsistent service quality remain key challenges.", None, 0),
    ('l3_8', 'landscape', "Competitors offer distinct strengths, including computation practice, coaching-based learning, and critical thinking.", None, 0),
    ('l3_9', 'landscape', "This analysis highlights where JEI needs to strengthen its competitiveness.",
     "This analysis highlights where J-E-I needs to strengthen its competitiveness.", .3),

    # deck p.9 · tuition & royalty
    ('l4_1', 'tuition', "JEI's monthly tuition generally ranges from 130 to 180 dollars, compared with 150 to 200 dollars for Kumon and 250 to 400 dollars for Mathnasium.",
     "J-E-I's monthly tuition generally ranges from one hundred thirty to one hundred eighty dollars, compared with one hundred fifty to two hundred dollars for Kumon and two hundred fifty to four hundred dollars for Mathnasium.", 0),
    ('l4_2', 'tuition', "JEI uses a tiered royalty structure, with lower fees as subject enrollments increase.",
     "J-E-I uses a tiered royalty structure, with lower fees as subject enrollments increase.", 0),
    ('l4_3', 'tuition', "This provides a different pricing and franchise model from its major competitors.", None, .2),
    # deck p.10 · JEI & competitors
    ('l4_4', 'rivals', "JEI entered the U.S. market in 1992, following Kumon's earlier expansion.",
     "J-E-I entered the U.S. market in nineteen ninety-two, following Kumon's earlier expansion.", 0),
    ('l4_5', 'rivals', "Today, major competitors operate significantly larger learning center networks.", None, 0),
    ('l4_6', 'rivals', "This highlights the importance of strengthening JEI's product competitiveness and brand positioning for future growth.",
     "This highlights the importance of strengthening J-E-I's product competitiveness and brand positioning for future growth.", .3),

    # deck p.11 · websites and social media
    ('l5_1', 'web', "JEI connects with families and prospective franchise partners through its corporate website, individual center websites, and franchise website.",
     "J-E-I connects with families and prospective franchise partners through its corporate website, individual center websites, and franchise website.", 0),
    ('l5_2', 'web', "Social media platforms, including Facebook, Instagram, and TikTok, also support customer engagement.", None, .2),
    # closing
    ('l5_3', 'outro', "Moving forward, JEI aims to strengthen its educational value and expand its presence across North America.",
     "Moving forward, J-E-I aims to strengthen its educational value and expand its presence across North America.", .2),
    ('l5_4', 'outro', "A Better Life Through Better Education.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l5_4'   # the rising closing chime just before this line (the mission); None for no chime

TAKE = {}   # line id → take index (sorted take position) where the picked take reads wrong or clips its end
TEMPO = 1.0
