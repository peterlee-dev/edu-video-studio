# The script: what is read, line by line. Edit this file, then run tools/make_audio.py tts (VOICE=male | female).
# Source: Google Docs "김의석 팀장님 · Brand Repositioning & Execution Strategy (Presentation Script for the English Strategy Summary)" (2026.11.09, 구글챗 유정 · 대언 · 승은 · 소정 방), body word for word.
# Not read: the doc title and meta lines, section headings and the footer. Audio only, no video: scenes are the doc's sections,
# all in CONT (no page-turn whoosh), SCENE_GAP is the pause between sections.
LANGUAGE = 'English'

SCENES = [('s1', '1. Current Situation & Key Challenges'), ('s2', '2. Two Strategic Enemies JEI Must Confront'), ('s3', '3. Core Brand Repositioning Strategy'), ('s4', '4. Strategic Constraints & Risks'), ('s5', '1. Three-Stage Product Strategy by Target Age Group'), ('s6', '2. Four Key Action Plans')]
CONT = {s for s, _ in SCENES}

# (id, scene, line as written, line as read (None = as written), extra pause after it in s)
SCRIPT = [
    # 1. Current Situation & Key Challenges
    ('l1_1', 's1', 'The strategy in this report is to move beyond competing on size and focus on showing parents why they should choose JEI.', 'The strategy in this report is to move beyond competing on size and focus on showing parents why they should choose J-E-I.', 0.25),
    ('l1_2', 's1', 'We identified three key challenges facing the traditional workbook market.', None, 0),
    ('l1_3', 's1', 'First, as learning becomes increasingly digital, more EdTech products have entered the market.', 'First, as learning becomes increasingly digital, more Ed Tech products have entered the market.', 0),
    ('l1_4', 's1', 'However, parents are becoming more concerned about whether these products deliver meaningful learning benefits.', None, 0),
    ('l1_5', 's1', 'Second, instructors face significant pressure to attract new customers.', None, 0),
    ('l1_6', 's1', 'This leads to increased stress and high instructor turnover, creating a continuing cycle of instructors leaving the profession.', None, 0),
    ('l1_7', 's1', 'Third, broad messages such as “Self-Learning” and “The Ability to Learn Independently” have not given parents a clear enough reason to choose JEI.', 'Third, broad messages such as Self-Learning and The Ability to Learn Independently have not given parents a clear enough reason to choose J-E-I.', 0),

    # 2. Two Strategic Enemies JEI Must Confront
    ('l2_1', 's2', 'JEI must address two strategic enemies.', 'J-E-I must address two strategic enemies.', 0),
    ('l2_2', 's2', 'The first is repeating basic math calculations without thinking.', None, 0),
    ('l2_3', 's2', 'This can make it hard for students to solve written math problems in higher grades and may lead them to give up on math.', None, 0.25),
    ('l2_4', 's2', 'The second is mindless tablet tapping.', None, 0),
    ('l2_5', 's2', 'Without clear learning support or instructor coaching, simply using tablets does not show real learning benefits.', None, 0),

    # 3. Core Brand Repositioning Strategy
    ('l3_1', 's3', 'We propose that JEI move beyond traditional workbooks and repetitive math drills.', 'We propose that J-E-I move beyond traditional workbooks and repetitive math drills.', 0),
    ('l3_2', 's3', 'Through precise assessment, we can identify learning gaps and help children understand basic principles and solve problems independently.', None, 0),
    ('l3_3', 's3', 'Our goal is to establish true self-directed learning.', None, 0.25),
    ('l3_4', 's3', 'Our Verbal Nail is “A Child Who Knows Why They Got an Answer Wrong.”', 'Our Verbal Nail is A Child Who Knows Why They Got an Answer Wrong.', 0),
    ('l3_5', 's3', 'This message speaks directly to parents’ concerns.', None, 0),
    ('l3_6', 's3', 'Our Visual Hammer is the “Defect Linker,” a visual map that connects learning gaps across different learning objectives.', 'Our Visual Hammer is the Defect Linker, a visual map that connects learning gaps across different learning objectives.', 0),
    ('l3_7', 's3', 'With a single visual, we can build parents’ trust without lengthy explanations.', None, 0.25),
    ('l3_8', 's3', 'Our proposed brand slogan is “Find the Way, Not Just the Answer.”', 'Our proposed brand slogan is Find the Way, Not Just the Answer.', 0),
    ('l3_9', 's3', 'Rather than simply giving children the right answers, JEI helps them understand the basic principles and find solutions on their own.', 'Rather than simply giving children the right answers, J-E-I helps them understand the basic principles and find solutions on their own.', 0),

    # 4. Strategic Constraints & Risks
    ('l4_1', 's4', 'There are also two risks to consider.', None, 0),
    ('l4_2', 's4', 'A more focused message may appeal to a smaller group of parents.', None, 0),
    ('l4_3', 's4', 'Also, learning gaps may be harder to show clearly for preschool and younger elementary students than for older students.', None, 0),

    # 1. Three-Stage Product Strategy by Target Age Group
    ('l5_1', 's5', 'We will simplify our product lineup into three stages.', None, 0),
    ('l5_2', 's5', 'Stage One offers a free, precise mobile assessment to attract potential customers.', None, 0),
    ('l5_3', 's5', 'Stage Two builds foundational skills through JEI Math, Korean, and Hangul.', 'Stage Two builds foundational skills through J-E-I Math, Korean, and Hangul.', 0),
    ('l5_4', 's5', 'Stage Three expands our offerings through Thinking PIZZA and school exam preparation packages.', 'Stage Three expands our offerings through Thinking Pizza and school exam preparation packages.', 0),
    ('l5_5', 's5', 'This will encourage enrollment in multiple subjects, increase revenue per customer, and support long-term retention.', None, 0.25),
    ('l5_6', 's5', 'We will focus on two core target groups.', None, 0),
    ('l5_7', 's5', 'The first is children preparing for elementary school.', None, 0),
    ('l5_8', 's5', 'We will offer precise school-readiness assessments and six learning courses, including Math and Hangul.', None, 0),
    ('l5_9', 's5', 'These programs will help children build foundational skills before entering elementary school.', None, 0.25),
    ('l5_10', 's5', 'Second, students in Grades 1 to 3.', 'Second, students in Grades one to three.', 0),
    ('l5_11', 's5', 'We will use a 10-minute diagnostic assessment to identify learning gaps and connect students with JEI Math, Korean, and Thinking PIZZA, our signature Thinking Skills program.', 'We will use a ten-minute diagnostic assessment to identify learning gaps and connect students with J-E-I Math, Korean, and Thinking Pizza, our signature Thinking Skills program.', 0),
    ('l5_12', 's5', 'We will then support continued learning through higher grades and middle school exam preparation.', None, 0),

    # 2. Four Key Action Plans
    ('l6_1', 's6', 'Our first step is to launch a free mobile assessment tool.', None, 0),
    ('l6_2', 's6', 'Parents will be able to identify their child’s learning gaps in about 10 minutes.', 'Parents will be able to identify their child’s learning gaps in about ten minutes.', 0),
    ('l6_3', 's6', 'This will lower the barrier to trying JEI and help us attract new customers.', 'This will lower the barrier to trying J-E-I and help us attract new customers.', 0.25),
    ('l6_4', 's6', 'Second, we will standardize instructor consultations and coaching messages.', None, 0),
    ('l6_5', 's6', 'When parents are concerned that their child is falling behind, instructors will use a consistent message: “Moving ahead without fixing learning gaps can cause serious problems in higher grades.”', 'When parents are concerned that their child is falling behind, instructors will use a consistent message, Moving ahead without fixing learning gaps can cause serious problems in higher grades.', 0),
    ('l6_6', 's6', 'This helps parents understand why addressing learning gaps is important.', None, 0.25),
    ('l6_7', 's6', 'Third, we will develop grading support tools with the goal of reducing routine grading work by 50%.', 'Third, we will develop grading support tools with the goal of reducing routine grading work by fifty percent.', 0),
    ('l6_8', 's6', 'This will help reduce instructors’ administrative and sales-related burdens, allowing them to focus more on learning coaching and student support.', None, 0.25),
    ('l6_9', 's6', 'Fourth, every Friday, we will send parents a visual progress report through KakaoTalk Messenger.', 'Fourth, every Friday, we will send parents a visual progress report through Kakao Talk Messenger.', 0),
    ('l6_10', 's6', "The report will show how each child's learning gaps are being addressed and what progress they are making.", None, 0),
    ('l6_11', 's6', 'This will help build parent trust and improve parent satisfaction.', None, 0.25),
    ('l6_12', 's6', 'At the same time, our early-warning system will help identify students who may leave JEI.', 'At the same time, our early-warning system will help identify students who may leave J-E-I.', 0),
    ('l6_13', 's6', 'Before parents decide to withdraw their children, instructors will proactively offer solutions to encourage continued enrollment.', None, 0.25),
    ('l6_14', 's6', 'This concludes the summary of our brand repositioning and execution strategy.', None, 0),
    ('l6_15', 's6', 'Thank you.', None, 0),
]
CLONE = set()
LEAD, GAP, SCENE_GAP, TAIL = .6, .45, 1.0, 1.2
DING_BEFORE = None
import os
# pinned takes per voice (sorted position): closing Thank you = θæŋk with a falling end (Praat, male ceiling 160 / female floor 75); female l5_3 Hangul = h ɑː ŋ ɡ əl (others heng-, hey-)
TAKE = {'male': {'l6_15': 6}, 'female': {'l6_15': 3, 'l5_3': 2}}.get(os.environ.get('VOICE'), {})
PACE = None
