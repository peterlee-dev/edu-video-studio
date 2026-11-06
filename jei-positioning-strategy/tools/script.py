# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: JEI Positioning & Execution Strategy_영상_김의석팀장님.pdf (English script, one section per deck page, word for word).
# Deck: 재능교육 포지셔닝 및 실행전략_202611.pptx (13 pages, Korean)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'JEI Positioning & Execution Strategy'), ('failed', 'Why traditional workbook solutions failed'),
    ('enemies', 'Two strategic enemies'), ('compete', 'Competing on a clear reason to choose JEI'),
    ('reposition', 'JEI repositioning strategy'), ('nailHammer', 'Verbal Nail & Visual Hammer'),
    ('targets', 'Two core target groups'), ('product', 'Three-stage product strategy'),
    ('assessment', '10-minute mobile AI assessment'), ('consult', 'Standardized teacher consultations & AI support'),
    ('retention', 'Weekly reports & early-warning CRM'), ('roadmap', '2027 execution roadmap'), ('outro', 'Closing'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # deck p.1 · JEI Positioning & Execution Strategy
    ('l1_1', 'title', "This report proposes a shift from competing on scale to giving parents a clear reason to choose JEI.",
     "This report proposes a shift from competing on scale to giving parents a clear reason to choose J-E-I.", .3),

    # deck p.2 · why traditional workbook solutions failed
    ('l2_1', 'failed', "We identified three main problems in the traditional workbook market.", None, .1),
    ('l2_2', 'failed', "First, simply moving paper workbooks to tablets did not demonstrate better learning results.", None, 0),
    ('l2_3', 'failed', "Second, sales pressure without effective tools led to teacher burnout.", None, 0),
    ('l2_4', 'failed', "Third, vague messages about study habits failed to address parents' concerns.", None, .3),

    # deck p.3 · two strategic enemies
    ('l3_1', 'enemies', "JEI must address two strategic enemies.", "J-E-I must address two strategic enemies.", .1),
    ('l3_2', 'enemies', "The first is repetitive math drills that focus on speed rather than understanding.", None, 0),
    ('l3_3', 'enemies', "The second is tablet-based learning that relies too much on gamification.", None, .1),
    ('l3_4', 'enemies', "Instead, JEI aims to help students understand their mistakes and solve problems independently.",
     "Instead, J-E-I aims to help students understand their mistakes and solve problems independently.", .3),

    # deck p.4 · competing on a clear reason to choose JEI
    ('l4_1', 'compete', "Competitors often focus on more content, repetitive drills, and heavy advertising.", None, 0),
    ('l4_2', 'compete', "JEI will take a different approach.", "J-E-I will take a different approach.", 0),
    ('l4_3', 'compete', "Through precise assessment, personalized step-by-step learning, and independent problem-solving, we aim to give parents a clear reason to choose JEI.",
     "Through precise assessment, personalized step-by-step learning, and independent problem-solving, we aim to give parents a clear reason to choose J-E-I.", 0),
    ('l4_4', 'compete', "This can help keep current students and attract new students through referrals.", None, .3),

    # deck p.5 · JEI repositioning strategy
    ('l5_1', 'reposition', "Our positioning is \"Thinking-Focused Diagnostic Learning.\"",
     "Our positioning is, Thinking-Focused Diagnostic Learning.", 0),
    ('l5_2', 'reposition', "Our Verbal Nail is \"A Child Who Understands Why They Got It Wrong.\"",
     "Our Verbal Nail is, A Child Who Understands Why They Got It Wrong.", 0),
    ('l5_3', 'reposition', "Our Visual Hammer is the \"Defect Linker,\" based on 12,759 error patterns.",
     "Our Visual Hammer is the Defect Linker, based on twelve thousand, seven hundred fifty-nine error patterns.", .1),
    ('l5_4', 'reposition', "Our goal is to help students discover solutions on their own, rather than simply memorize answers.", None, .3),

    # deck p.6 · Verbal Nail & Visual Hammer
    ('l6_1', 'nailHammer', "We also need to change how we communicate with parents.", None, 0),
    ('l6_2', 'nailHammer', "Instead of focusing on general study habits, we highlight a child's ability to understand their mistakes.", None, .1),
    ('l6_3', 'nailHammer', "The Defect Linker shows the causes of learning gaps through a simple visual map.", None, 0),
    ('l6_4', 'nailHammer', "This helps parents understand their child's learning needs and builds trust.", None, .3),

    # deck p.7 · two core target groups
    ('l7_1', 'targets', "We will focus on two main target groups.", None, .1),
    ('l7_2', 'targets', "First, children aged six to seven preparing for elementary school.", None, 0),
    ('l7_3', 'targets', "We offer precise assessment and step-by-step learning to build basic literacy and number skills.", None, .1),
    ('l7_4', 'targets', "Second, students in Grades 1 to 3 who struggle with math.", "Second, students in Grades one to three who struggle with math.", 0),
    ('l7_5', 'targets', "Our 10-minute assessment identifies learning gaps and connects students with suitable learning programs.",
     "Our ten-minute assessment identifies learning gaps and connects students with suitable learning programs.", .3),

    # deck p.8 · three-stage product strategy
    ('l8_1', 'product', "Our product strategy has three stages.", None, .1),
    ('l8_2', 'product', "First, a free mobile AI assessment to attract new customers.", None, 0),
    ('l8_3', 'product', "Second, JEI Math and Korean programs to provide core learning.", "Second, J-E-I Math and Korean programs to provide core learning.", 0),
    ('l8_4', 'product', "Third, additional programs in critical thinking and literacy to support continued learning and increase customer lifetime value.", None, .3),

    # deck p.9 · ACTION 01 · launching a 10-minute mobile AI assessment
    ('l9_1', 'assessment', "Our first action is to launch a free 10-minute mobile assessment.",
     "Our first action is to launch a free ten-minute mobile assessment.", 0),
    ('l9_2', 'assessment', "Students answer 10 questions, and parents can immediately see a map of their learning gaps.",
     "Students answer ten questions, and parents can immediately see a map of their learning gaps.", 0),
    ('l9_3', 'assessment', "Results can be shared through KakaoTalk and linked to a consultation with a nearby JEI teacher.",
     "Results can be shared through Kakao Talk and linked to a consultation with a nearby J-E-I teacher.", 0),
    ('l9_4', 'assessment', "By using our existing assessment data, we aim to attract new customers through word of mouth.", None, .3),

    # deck p.10 · ACTION 02 · standardized teacher consultations & AI support
    ('l10_1', 'consult', "We will improve teacher consultations through standard guidelines and AI support.", None, 0),
    ('l10_2', 'consult', "Teachers will help parents understand why learning gaps should be addressed before moving ahead.", None, 0),
    ('l10_3', 'consult', "AI will reduce grading and administrative tasks, so teachers can spend more time coaching and supporting students.", None, 0),
    ('l10_4', 'consult', "We will also offer combined programs to increase enrollment value.", None, .3),

    # deck p.11 · ACTION 03 · weekly reports & early-warning CRM
    ('l11_1', 'retention', "To improve student retention, we will introduce weekly progress reports and an early-warning CRM system.",
     "To improve student retention, we will introduce weekly progress reports and an early-warning C-R-M system.", 0),
    ('l11_2', 'retention', "Every Friday, parents will receive a visual report showing how their child has overcome learning difficulties.", None, 0),
    ('l11_3', 'retention', "If a student's error rate increases, the system will alert the teacher.", None, 0),
    ('l11_4', 'retention', "Teachers can then provide support before parents consider leaving.", None, .3),

    # deck p.12 · 2027 execution roadmap
    ('l12_1', 'roadmap', "In Q1, we will develop the mobile assessment system and complete teacher training.",
     "In Q-one, we will develop the mobile assessment system and complete teacher training.", 0),
    ('l12_2', 'roadmap', "In Q2, we will launch the \"A Child Who Understands Why They Got It Wrong\" campaign to increase new enrollments.",
     "In Q-two, we will launch the, A Child Who Understands Why They Got It Wrong, campaign to increase new enrollments.", 0),
    ('l12_3', 'roadmap', "In Q3, we aim to reduce student dropout rates by 20% through weekly reports and early-warning CRM.",
     "In Q-three, we aim to reduce student dropout rates by twenty percent through weekly reports and early-warning C-R-M.", 0),
    ('l12_4', 'roadmap', "In Q4, we will review customer lifetime value and establish a standard operating model across JEI.",
     "In Q-four, we will review customer lifetime value and establish a standard operating model across J-E-I.", .3),

    # deck p.13 · closing. The script PDF breaks off in the second sentence ("By combining our assessment system with pe"); l13_2 was
    # finished from deck p.13 (이미 축적된 진단 알고리즘과 교사의 따뜻한 손길을 가장 강력한 선택 이유로 만드는 것), as agreed on 2026.11.06
    ('l13_1', 'outro', "JEI's goal is not simply to teach more, but to find the right starting point for every child.",
     "J-E-I's goal is not simply to teach more, but to find the right starting point for every child.", .1),
    ('l13_2', 'outro', "By combining our assessment system with personal care from our teachers, we will make it the strongest reason to choose JEI.",
     "By combining our assessment system with personal care from our teachers, we will make it the strongest reason to choose J-E-I.", 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # the script has no thank-you line
# line id → take index (sorted take position) where the picked take reads wrong or clips its end. Checked with the wav2vec2 phoneme model:
# l11_1 · l12_3: the picked take read CRM as "C-R-am" (s iː ɑːɹ ɹ æ m), take 1 reads "C-R-M" (ɑːɹ ɛ m); l8_4: "value" lost its l (v æ j uː), take 1 has it
TAKE = {'l8_4': 1, 'l11_1': 1, 'l12_3': 1}
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female English, ../adaptive-diagnosis-v2/audio/narration.mp3)
VOICE = 'voice_ref'
