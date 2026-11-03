# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 미주 지사 공유 문건 스크립트 - 3-2.[ENG] Adaptive 진단_English.pdf (word for word, except l1_1: "improve" → "introduce the new", review 1 · 2026.10.30). Deck: 3. [미주 공유용] 미주 영어 Adaptive 정밀진단평가 기획안_261105.pdf
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Title'),
    # 01 background
    ('parents', 'What parents expect'), ('aim', 'Our aim'),
    # 02 U.S. market benchmark
    ('market', 'U.S. adaptive assessments'), ('catirt', 'CAT and IRT'), ('programs', 'Four programs'), ('connect', 'Assessment to learning'),
    # 03 current assessment by level
    ('levels', 'Questions by level'), ('levelsCJ', 'Levels C to J'),
    # 04 question structure
    ('structure', 'Main and sub-questions'), ('roles', 'Three question roles'),
    # 05 why English is different
    ('mathEng', 'Math vs English'), ('engConfirm', 'Confirming understanding'), ('engSeq', 'No fixed sequence'),
    # 06 skill areas
    ('areas', 'Sequences by skill area'), ('areas2', 'Step by step or separately'),
    # 07 logic
    ('logic', 'Initial and Check Questions'), ('logic2', 'Sequence or independent'),
    # 08 why improve
    ('limits', 'Two limitations'), ('stages', 'First stage, then IRT'),
    # 09 AS-IS / TO-BE
    ('asisTobe', 'AS-IS / TO-BE'), ('options', 'Learning options'),
    # 10 process
    ('process', 'Four steps · 1–2'), ('process2', 'Four steps · 3–4'),
    ('closing', 'Closing'), ('outro', 'Thank you'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = {'connect', 'levelsCJ', 'engConfirm', 'engSeq', 'areas2', 'options', 'process2'}

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    ('l1_1', 'title', "We would like to share our plans to introduce the new JEI English Online Adaptive Assessment system.", "We would like to share our plans to introduce the new J-E-I English Online Adaptive Assessment system.", .3),

    ('l2_1', 'parents', "As AI and data-driven learning become more common, parents expect more than a simple level assessment.", "As A-I and data-driven learning become more common, parents expect more than a simple level assessment.", .1),
    ('l2_2', 'parents', "They want to know where their children struggle, where they should start, and how much they have improved.", None, .3),
    ('l2_3', 'aim', "We aim to improve our assessment system to provide more accurate starting points and personalized learning plans.", None, .3),

    ('l3_1', 'market', "Major U.S. Adaptive Assessment programs adjust questions based on student responses and connect results with personalized learning.", None, .2),
    ('l3_2', 'catirt', "Two common methods are CAT, or Computerized Adaptive Testing, and IRT, or Item Response Theory.", "Two common methods are C-A-T, or Computerized Adaptive Testing, and I-R-T, or Item Response Theory.", .1),
    ('l3_3', 'catirt', "CAT adjusts questions based on student responses, while IRT uses question difficulty and responses to estimate ability levels.", "C-A-T adjusts questions based on student responses, while I-R-T uses question difficulty and responses to estimate ability levels.", .3),
    ('l3_4', 'programs', "NWEA MAP Growth tracks student progress through regular assessments.", "N-W-E-A MAP Growth tracks student progress through regular assessments.", 0),
    ('l3_5', 'programs', "i-Ready connects assessment results with personalized learning.", "Eye-Ready connects assessment results with personalized learning.", 0),
    ('l3_6', 'programs', "IXL recommends learning activities based on ongoing assessments.", "I-X-L recommends learning activities based on ongoing assessments.", 0),
    ('l3_7', 'programs', "Star Reading focuses on reading skills and progress tracking.", None, .2),
    ('l3_8', 'connect', "Our goal is to connect precise assessment with personalized learning, as these programs do.", None, .3),

    ('l4_1', 'levels', "Our current JEI English assessments vary by level.", "Our current J-E-I English assessments vary by level.", 0),
    ('l4_2', 'levels', "Lower levels focus mainly on basic reading and Phonics.", None, .2),
    ('l4_3', 'levelsCJ', "From Level C to J, Grammar and Reading become the main areas.", None, 0),
    ('l4_4', 'levelsCJ', "Levels I and J also have significantly more questions.", None, .2),
    ('l4_5', 'levelsCJ', "We plan to review these differences and determine how to apply Adaptive Assessment to each learning objective.", None, .3),

    ('l5_1', 'structure', "Many JEI English assessment questions contain several sub-questions.", "Many J-E-I English assessment questions contain several sub-questions.", 0),
    ('l5_2', 'structure', "Currently, even one incorrect sub-question causes the entire main question to be marked incorrect.", None, .3),
    ('l5_3', 'roles', "We plan to assess sub-questions separately and assign three roles: Initial, Check, and Final Check Questions.", None, .1),
    ('l5_4', 'roles', "This will help us check understanding more accurately and identify specific learning needs.", None, .3),

    ('l6_1', 'mathEng', "Math and English require different approaches to Adaptive Assessment.", None, 0),
    ('l6_2', 'mathEng', "In Math, reducing the number of questions is a key goal because long assessments can cause student fatigue.", None, .2),
    ('l6_3', 'engConfirm', "In English, the main challenge is confirming understanding.", None, 0),
    ('l6_4', 'engConfirm', "One incorrect answer may not mean a student does not understand a skill.", None, .2),
    ('l6_5', 'engSeq', "Also, English learning objectives do not always follow a clear sequence.", None, 0),
    ('l6_6', 'engSeq', "Therefore, we will focus on checking understanding through multiple questions when needed.", None, .3),

    ('l7_1', 'areas', "English skill areas have different learning structures.", None, 0),
    ('l7_2', 'areas', "Phonics, Decoding, and some Grammar skills follow a clear sequence.", None, 0),
    ('l7_3', 'areas', "Reading Comprehension skills do not always follow a fixed order.", "Reading, Comprehension skills do not always follow a fixed order.", .43),   # take 0 (TAKE) is .23 s shorter than the take before: the gap keeps later lines in place
    ('l7_4', 'areas2', "We will assess skills step by step where the sequence is clear.", None, 0),
    ('l7_5', 'areas2', "For other skills, we will check each learning objective separately.", None, .3),

    ('l8_1', 'logic', "We will use an Initial Question and a Check Question to assess each learning objective.", None, .1),
    ('l8_2', 'logic', "If both answers are correct, we move to the next learning objective.", None, 0),
    ('l8_3', 'logic', "If both are incorrect, we identify the objective as an area that needs further learning.", None, 0),
    ('l8_4', 'logic', "If the answers are mixed, we provide a Final Check Question.", None, .2),
    ('l8_5', 'logic2', "We will then follow the learning sequence where it is clear or assess objectives independently where it is not.", None, .3),

    ('l9_1', 'limits', "Our current assessment has two main limitations.", None, 0),
    ('l9_2', 'limits', "First, it is difficult to distinguish simple mistakes from a lack of understanding.", None, 0),
    ('l9_3', 'limits', "Second, we have limited data to analyze question difficulty and response patterns.", None, .2),
    ('l9_4', 'stages', "In the first stage, we will improve how we use individual responses and collect more data.", None, 0),
    ('l9_5', 'stages', "Later, we plan to use methods such as IRT to improve assessment accuracy and analyze incorrect answers.", "Later, we plan to use methods such as I-R-T to improve assessment accuracy and analyze incorrect answers.", .3),

    ('l10_1', 'asisTobe', "Currently, students complete fixed assessment questions, and we assign learning sets based on the results.", None, 0),
    ('l10_2', 'asisTobe', "With Adaptive Assessment, we will adjust questions based on student responses.", None, .2),
    ('l10_3', 'options', "We will also expand learning options to include standard sets, sets with POD, POD-only learning, and online learning.", "We will also expand learning options to include standard sets, sets with P-O-D, P-O-D only learning, and online learning.", 0),
    ('l10_4', 'options', "In the first stage, we will focus on standard sets and sets combined with POD.", "In the first stage, we will focus on standard sets and sets combined with P-O-D.", .3),

    ('l11_1', 'process', "Our Adaptive Assessment will follow four steps.", None, 0),
    ('l11_2', 'process', "First, we will identify possible starting points.", None, 0),
    ('l11_3', 'process', "Second, we will check understanding using Initial and Check Questions.", None, .1),
    ('l11_4', 'process2', "Third, we will provide additional questions when results are unclear.", None, 0),
    ('l11_5', 'process2', "Finally, we will assign standard sets or sets combined with POD based on each student's needs.", "Finally, we will assign standard sets or sets combined with P-O-D based on each student's needs.", .1),
    ('l11_6', 'process2', "This process connects assessment results directly with personalized learning.", None, .3),

    ('l12_1', 'closing', "We aim to develop an Adaptive Assessment system that reflects the unique characteristics of English learning.", None, 0),
    ('l12_2', 'closing', "We will improve our existing assessment questions and connect the results with personalized learning through standard sets and POD.", "We will improve our existing assessment questions and connect the results with personalized learning through standard sets and P-O-D.", .3),
    ('l12_3', 'outro', "In the future, we plan to use learning data to improve assessment accuracy and expand into Adaptive Learning.", None, .3),
    ('l12_4', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

# tts mode only: keep these lines on a given take (index in audio/tts_cache) instead of the automatic pick.
# l7_3: review 2 (2026.11.02) — the picked take paused after "Reading,"; take 0 reads "Reading Comprehension" as one phrase (wav2vec2: k ɑː m p…)
TAKE = {'l7_3': 0}

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l12_4'   # a soft ding just before this line (the thank-you); None for no ding
