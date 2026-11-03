# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 미주 지사 공유 문건 스크립트 - 2. [2차] 미주 영어 기획(안) ENG.pdf (word for word, except as asked: "learning goals" → "learning objectives" in l3_15 and l4_15; review 2026.10.30: "detailed" → "precise" assessment in l2_13, l4_9, l4_13, "learning order" → "learning sequence" in l4_15 and l7_5, no "JEI" before Reading Builder · Plus · Pro in l3_5, l3_7, l3_9; review 2026.11.03: "stages" → "levels" in l3_13 and l3_15). Deck: 2. [미주 공유용] 글로벌 JEI 영어 상품 기획안 요약본_261105.pdf
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Title'),
    # 01 development direction
    ('sor', 'Science of Reading'), ('naep', 'NAEP 2024'), ('market', 'States and companies'), ('response', 'JEI response'),
    ('goal', 'Learning goal'), ('system', 'Learning system'), ('levels', 'Pre-K to Grade 9'),
    ('ready', 'Reading Ready'), ('builder', 'Reading Builder'), ('plus', 'Reading Plus'), ('pro', 'Reading Pro'),
    ('growth', 'Step by step'), ('scale', 'Program at a glance'),
    # 02 features, differentiation and curriculum
    ('features', 'Four features'), ('feat1', 'Feature 1 · SoR'), ('feat2', 'Feature 2 · Context'), ('feat34', 'Features 3 & 4'),
    ('diff', 'What makes JEI different'), ('diff2', 'State standards · adaptive'),
    ('themes', 'Eight themes'), ('spiral', 'Spiral curriculum'), ('example', 'Animals and Nature'),
    ('genre', 'Literary and informational'), ('ratio', 'Ratio guide'), ('curSum', 'More than reading'),
    # 03 sample workbook and future plan
    ('sample', 'Sample workbook'), ('sampleTexts', 'Two texts, one theme'), ('week', 'Weekly schedule'), ('flow', 'Learning flow'),
    ('pages', '32 pages'), ('podNext', 'Personalized POD'),
    ('next', 'Plan · standards'), ('objectives', 'Plan · objectives'), ('existing', 'Plan · curriculum'), ('ai', 'Plan · AI content'),
    ('pilot', 'Reading Builder first'), ('outro', 'Thank you'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = {'builder', 'plus', 'pro', 'feat2', 'feat34', 'ratio', 'objectives', 'existing', 'ai'}

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    ('l1_1', 'title', "We would like to share the development direction for our new JEI English program in the U.S.", None, 0),
    ('l1_2', 'title', "We will also explain the curriculum design we have developed so far.", None, .3),

    ('l2_1', 'sor', "In the U.S., reading education based on the Science of Reading, or SoR, is expanding through state laws and education policies.", "In the U.S., reading education based on the Science of Reading, or S-O-R, is expanding through state laws and education policies.", 0),
    ('l2_2', 'sor', "SoR brings together scientific research on how children learn to read and understand texts.", "S-O-R brings together scientific research on how children learn to read and understand texts.", 0),
    ('l2_3', 'sor', "In the U.S., this research is being used to improve reading education policies and teaching methods.", None, .2),
    ('l2_4', 'naep', "However, according to the 2024 National Assessment of Educational Progress, or NAEP, about 40% of fourth-grade students scored Below Basic in reading.", None, 0),
    ('l2_5', 'naep', "This shows that there is still a strong need to improve literacy skills.", None, .2),
    ('l2_6', 'market', "Major states, including New York, New Jersey, California, Florida, and Texas, are also introducing related policies.", None, 0),
    ('l2_7', 'market', "Major education companies, such as Amplify, Lexia, and Savvas, also emphasize SoR-based curricula.", "Major education companies, such as Amplify, Lexia, and Savvas, also emphasize S-O-R-based curricula.", .2),
    ('l2_8', 'response', "In response to these changes, we aim to develop a new JEI English program.", None, 0),
    ('l2_9', 'response', "The program will help students build skills step by step, from basic reading to vocabulary, reading comprehension, and broader language understanding.", None, 0),
    ('l2_10', 'response', "It will also help students develop their thinking skills.", None, .2),
    ('l2_11', 'goal', "Our goal is to go beyond simply reading and understanding texts.", None, 0),
    ('l2_12', 'goal', "We want students to think independently, make decisions, and express their ideas using evidence.", None, .2),
    ('l2_13', 'system', "To achieve this, we plan to build a learning system that connects JEI's strengths in precise assessment and personalized learning plans with POD workbooks and center coaching.", "To achieve this, we plan to build a learning system that connects JEI's strengths in precise assessment and personalized learning plans with P-O-D workbooks and center coaching.", .3),

    ('l3_1', 'levels', "Our target students range from Pre-K through Grade 9.", None, 0),
    ('l3_2', 'levels', "We have organized the program into four levels based on students' stages of development.", None, .2),
    ('l3_3', 'ready', "JEI Reading Ready is designed for Pre-K through Grade 2.", None, 0),
    ('l3_4', 'ready', "It focuses on building the basic skills students need to read independently.", None, 0),
    ('l3_5', 'builder', "Reading Builder is designed for Grades 3 through 5.", None, 0),
    ('l3_6', 'builder', "It helps students expand their vocabulary and background knowledge through reading.", None, 0),
    ('l3_7', 'plus', "Reading Plus is designed for Grades 6 and 7.", None, 0),
    ('l3_8', 'plus', "It helps students develop deeper thinking skills by comparing and analyzing what they read.", None, 0),
    ('l3_9', 'pro', "Finally, Reading Pro is designed for Grades 8 and 9.", None, 0),
    ('l3_10', 'pro', "It helps students evaluate information and express their ideas logically using evidence.", None, .2),
    ('l3_11', 'growth', "Through these four programs, we aim to help students grow step by step.", None, 0),
    ('l3_12', 'growth', "They will move from basic reading skills to analysis, evaluation, and building arguments.", None, .2),
    ('l3_13', 'scale', "Overall, we plan to develop 11 levels with a total of 352 standard sets.", None, 0),
    ('l3_14', 'scale', "We plan to provide the content through POD workbooks first and later expand into online learning.", "We plan to provide the content through P-O-D workbooks first and later expand into online learning.", 0),
    ('l3_15', 'scale', "However, we will continue to review and improve the number of sets and learning objectives at each level during development.", None, .5),

    ('l4_1', 'features', "We will now explain the key features of the new program, what makes it different, and how we are designing the curriculum.", None, 0),
    ('l4_2', 'features', "Our new program has four main features.", None, 0),
    ('l4_3', 'feat1', "First, we focus on building reading skills step by step based on the Science of Reading.", None, 0),
    ('l4_4', 'feat1', "We are designing the program to match each student's reading development.", None, 0),
    ('l4_5', 'feat1', "Students will move from basic reading skills to vocabulary and reading comprehension in a structured way.", None, 0),
    ('l4_6', 'feat2', "Second, we provide integrated literacy learning based on context.", None, 0),
    ('l4_7', 'feat2', "We connect different types of texts, including literary and informational texts, under one theme.", None, 0),
    ('l4_8', 'feat2', "Students will learn reading comprehension, vocabulary, grammar, and writing together.", None, 0),
    ('l4_9', 'feat34', "Third, we plan to provide precise Adaptive Assessment.", None, 0),
    ('l4_10', 'feat34', "Fourth, we plan to use AI to support learning and coaching.", None, 0),
    ('l4_11', 'feat34', "We are considering using AI for writing feedback, POD workbook grading, learning result analysis, and center coaching support.", "We are considering using AI for writing feedback, P-O-D workbook grading, learning result analysis, and center coaching support.", .2),
    ('l4_12', 'diff', "Next, we will explain what makes JEI different.", None, 0),
    ('l4_13', 'diff', "Our main goal is to connect precise assessment, personalized learning paths, customized POD workbooks, and center coaching into one learning system.", "Our main goal is to connect precise assessment, personalized learning paths, customized P-O-D workbooks, and center coaching into one learning system.", 0),
    ('l4_14', 'diff', "Through this approach, we aim to provide students with a unique personalized learning experience.", None, .2),
    ('l4_15', 'diff2', "We also plan to reflect each state's education standards in our learning objectives and learning sequence.", None, 0),
    ('l4_16', 'diff2', "At the same time, we will adjust learning content through Adaptive Learning based on each student's level.", None, 0),
    ('l4_17', 'diff2', "This will allow us to provide a higher level of personalized learning.", None, .4),

    ('l5_1', 'themes', "Now, we will explain our curriculum design.", None, 0),
    ('l5_2', 'themes', "We have selected eight common themes based on topics from major U.S. textbooks and grade-level standards in CCSS.", "We have selected eight common themes based on topics from major U.S. textbooks and grade-level standards in C-C-S-S.", .2),
    ('l5_3', 'spiral', "We use a spiral curriculum structure.", None, 0),
    ('l5_4', 'spiral', "This means students revisit the same themes across different grades.", None, 0),
    ('l5_5', 'spiral', "As students move to higher grades, the topics become deeper, and the level of reading and thinking also increases.", None, .2),
    ('l5_6', 'example', "For example, let's look at the theme of Animals and Nature.", None, 0),
    ('l5_7', 'example', "In Pre-K, students begin by learning about animals around them.", None, 0),
    ('l5_8', 'example', "In Grade 4, they learn how animals survive and adapt to their environments.", None, 0),
    ('l5_9', 'example', "By Grade 9, students evaluate and build arguments about their responsibility to protect the environment.", None, .2),
    ('l5_10', 'genre', "We have also adjusted the balance between literary and informational texts based on students' grade levels and development.", None, 0),
    ('l5_11', 'genre', "In the early grades, we place more focus on literary texts.", None, 0),
    ('l5_12', 'genre', "This helps students become more familiar with reading.", None, 0),
    ('l5_13', 'genre', "As students move to higher grades, we increase the amount of informational texts and texts related to arguments and opinions.", None, -.6),
    ('l5_14', 'ratio', "We developed these ratios as JEI's own guidelines, using the reading standards in CCSS and the grade-level assessment structure of NAEP as references.", "We developed these ratios as JEI's own guidelines, using the reading standards in C-C-S-S and the grade-level assessment structure of N-A-E-P as references.", .2),
    ('l5_15', 'curSum', "Through this curriculum design, we want students to develop more than reading skills.", None, 0),
    ('l5_16', 'curSum', "Even within the same theme, students will gradually build vocabulary, background knowledge, analysis skills, and critical thinking skills.", None, .5),

    ('l6_1', 'sample', "Finally, we will explain an example of our workbook design and our future development plans.", None, 0),
    ('l6_2', 'sample', "First, we will introduce a sample Reading Builder workbook developed for Grade 3 students in the U.S.", "First, we will introduce a sample Reading Builder workbook developed for Grade 3 students in the U.S. ...", 0),
    ('l6_3', 'sample', "The sample uses one theme, Building a Home Together.", None, .2),
    ('l6_4', 'sampleTexts', "We connect literary and informational texts under this theme.", None, 0),
    ('l6_5', 'sampleTexts', "The learning activities move from reading comprehension to analysis, application, and writing.", None, .2),
    ('l6_6', 'week', "We also follow JEI's small-step learning approach.", None, 0),
    ('l6_7', 'week', "The weekly learning schedule includes one center session and four days of home learning.", None, .2),
    ('l6_8', 'flow', "The learning activities are connected step by step.", None, 0),
    ('l6_9', 'flow', "Students begin with vocabulary preparation before reading.", None, 0),
    ('l6_10', 'flow', "They then move to reading the main text, reading comprehension, advanced vocabulary, grammar, and writing.", None, 0),
    ('l6_11', 'flow', "This structure is designed to help students learn independently.", None, .2),
    ('l6_12', 'pages', "Each set includes 24 pages of learning content.", None, 0),
    ('l6_13', 'pages', "It also includes two pages for the Interim Test, answer sheets, and covers.", None, 0),
    ('l6_14', 'pages', "The total is 32 pages.", None, .2),
    ('l6_15', 'podNext', "However, this is a standard sample workbook.", None, 0),
    ('l6_16', 'podNext', "We are currently studying how to apply personalized POD learning.", "We are currently studying how to apply personalized P-O-D learning.", 0),
    ('l6_17', 'podNext', "Our goal is to adjust and assign the right content based on each student's assessment results.", None, .4),

    ('l7_1', 'next', "Finally, we will explain our next development steps.", None, 0),
    ('l7_2', 'next', "We have completed our review and analysis of ELA education standards across all 50 U.S. states.", None, 0),
    ('l7_3', 'next', "We are now working to match JEI's learning objectives with each state's education standards.", None, 0),
    ('l7_4', 'objectives', "As part of this process, we are reviewing our existing learning objectives.", None, 0),
    ('l7_5', 'objectives', "We are checking whether they are appropriate and whether they follow the right learning sequence.", None, 0),
    ('l7_6', 'objectives', "We plan to improve any areas that need changes.", None, 0),
    ('l7_7', 'existing', "At the same time, we are analyzing the content of our existing JEI English workbooks in the U.S.", None, 0),
    ('l7_8', 'existing', "We are reviewing which content can be used in the new program.", None, 0),
    ('l7_9', 'existing', "Based on these findings, we will connect the improved learning objectives with state education standards.", None, 0),
    ('l7_10', 'existing', "We will then develop a more detailed theme-based curriculum and personalized learning paths.", None, 0),
    ('l7_11', 'ai', "Next, we plan to use AI Agents to develop content for each learning objective.", None, 0),
    ('l7_12', 'ai', "Our researchers will review and improve the content.", None, 0),
    ('l7_13', 'ai', "We will then build a content pool and use it for product development.", None, .2),
    ('l7_14', 'pilot', "Rather than developing all four programs at the same time, we plan to focus on Reading Builder first.", None, 0),
    ('l7_15', 'pilot', "We will conduct a pilot test to check learning results and how well the program works at JEI centers.", None, 0),
    ('l7_16', 'pilot', "After this, we plan to expand development to the other programs step by step.", None, .3),
    ('l8_1', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

# tts mode only: keep these lines on a given take (index in audio/tts_cache) instead of the automatic pick.
# Every line is pinned to the take heard in ver3 (2026-10-30), so a later fix re-reads only the lines it changes:
# drop a line from here when its text changes (or give it a new take number after listening)
TAKE = {'l1_1': 2, 'l1_2': 0, 'l2_1': 7, 'l2_2': 7, 'l2_3': 1, 'l2_4': 3, 'l2_5': 0, 'l2_6': 0, 'l2_7': 3, 'l2_8': 1, 'l2_9': 0, 'l2_10': 1, 'l2_11': 0, 'l2_12': 10, 'l2_13': 2, 'l3_1': 2, 'l3_2': 2, 'l3_3': 1, 'l3_4': 0, 'l3_5': 4, 'l3_6': 0, 'l3_7': 1, 'l3_8': 2, 'l3_9': 0, 'l3_10': 0, 'l3_11': 2, 'l3_12': 0, 'l3_13': 0, 'l3_14': 3, 'l3_15': 1, 'l4_1': 2, 'l4_2': 0, 'l4_3': 0, 'l4_4': 1, 'l4_5': 0, 'l4_6': 1, 'l4_7': 0, 'l4_8': 1, 'l4_9': 3, 'l4_10': 0, 'l4_11': 2, 'l4_12': 1, 'l4_13': 2, 'l4_14': 0, 'l4_15': 4, 'l4_16': 0, 'l4_17': 0, 'l5_1': 0, 'l5_2': 2, 'l5_3': 2, 'l5_4': 1, 'l5_5': 1, 'l5_6': 0, 'l5_7': 1, 'l5_8': 1, 'l5_9': 2, 'l5_10': 1, 'l5_11': 2, 'l5_12': 1, 'l5_13': 2, 'l5_14': 2, 'l5_15': 0, 'l5_16': 0, 'l6_1': 2, 'l6_2': 1, 'l6_3': 2, 'l6_4': 1, 'l6_5': 1, 'l6_6': 0, 'l6_7': 2, 'l6_8': 2, 'l6_9': 2, 'l6_10': 5, 'l6_11': 2, 'l6_12': 2, 'l6_13': 2, 'l6_14': 0, 'l6_15': 1, 'l6_16': 2, 'l6_17': 1, 'l7_1': 2, 'l7_2': 1, 'l7_3': 1, 'l7_4': 0, 'l7_5': 1, 'l7_6': 0, 'l7_7': 2, 'l7_8': 1, 'l7_9': 0, 'l7_10': 2, 'l7_11': 2, 'l7_12': 0, 'l7_13': 2, 'l7_14': 0, 'l7_15': 2, 'l7_16': 0, 'l8_1': 1}

# tts mode only: speed the picked takes up (ffmpeg atempo, pitch kept). 1.05 = the pace of ../math-di-improvement-v2, whose voice this is
TEMPO = 1.0

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l8_1'   # a soft ding just before this line (the thank-you); None for no ding
