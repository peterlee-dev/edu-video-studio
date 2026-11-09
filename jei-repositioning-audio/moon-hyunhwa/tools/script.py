# The script: what is read, line by line. Edit this file, then run tools/make_audio.py tts (VOICE=male | female).
# Source: Google Docs "문현화 팀장님 · JEI Korea Market Repositioning (English Presentation Script | Executive Summary)" (2026.11.09, 구글챗 유정 · 대언 · 승은 · 소정 방), body word for word.
# Not read: the doc title and meta lines, section headings and the footer. Audio only, no video: scenes are the doc's sections,
# all in CONT (no page-turn whoosh), SCENE_GAP is the pause between sections.
LANGUAGE = 'English'

SCENES = [('s1', 'Opening & Key Takeaway'), ('s2', '01. Korean Workbook Market and Competitive Landscape'), ('s3', "02. JEI's Strengths and Current Limitations"), ('s4', "03. Parents' Needs and Primary Target Customers"), ('s5', '04. Core Differentiation: From Assessment to Visible Growth'), ('s6', '05. Proposed Brand Positioning and Customer Messaging'), ('s7', '06. Service Development and Operational Directions'), ('s8', 'Closing')]
CONT = {s for s, _ in SCENES}

# (id, scene, line as written, line as read (None = as written), extra pause after it in s)
SCRIPT = [
    # Opening & Key Takeaway
    ('l1_1', 's1', "Today, I will present JEI's repositioning strategy for the Korean market.", "Today, I will present J-E-I's repositioning strategy for the Korean market.", 0.25),
    ('l1_2', 's1', 'Our key message to customers is clear.', None, 0.25),
    ('l1_3', 's1', 'JEI can differentiate itself by using precise diagnosis and assessment to design the learning path each child needs, and by helping children develop the ability to grow independently.', 'J-E-I can differentiate itself by using precise diagnosis and assessment to design the learning path each child needs, and by helping children develop the ability to grow independently.', 0.25),
    ('l1_4', 's1', "To deliver on that promise, we must connect our diagnostic results to each child's actual learning experience and show parents clear evidence of progress.", None, 0.25),
    ('l1_5', 's1', "I'll begin with the competitive landscape, then discuss JEI's strengths and limitations, what parents need, our proposed brand positioning, and the steps needed to deliver it.", "I'll begin with the competitive landscape, then discuss J-E-I's strengths and limitations, what parents need, our proposed brand positioning, and the steps needed to deliver it.", 0),

    # 01. Korean Workbook Market and Competitive Landscape
    ('l2_1', 's2', 'The Korean workbook market has become more competitive, with traditional providers offering increasingly different learning models.', None, 0.25),
    ('l2_2', 's2', 'Competition now extends beyond workbook providers to local study rooms, private learning centers, and digital learning programs.', None, 0.25),
    ('l2_3', 's2', 'The four major workbook providers in Korea have different business models and strategies.', None, 0.25),
    ('l2_4', 's2', 'Daekyo operates learning spaces such as Learning Centers and Hi CAMPUS, and offers learning content through its Summit program.', 'Daekyo operates learning spaces such as Learning Centers and Hi Campus, and offers learning content through its Summit program.', 0.25),
    ('l2_5', 's2', "Kumon records students' handwritten work digitally and supports learning between home visits through Daily Care.", None, 0.25),
    ('l2_6', 's2', 'Woongjin combines learning across all subjects with AI features through its Smart All program.', None, 0.25),
    ('l2_7', 's2', "JEI's strengths include paper-based learning, individualized learning paths, precise assessment, and instructor coaching.", "J-E-I's strengths include paper-based learning, individualized learning paths, precise assessment, and instructor coaching.", 0.25),
    ('l2_8', 's2', 'Among these competitors, Kumon is our most direct competitor because we both focus on paper-based learning and home visits.', None, 0.25),
    ('l2_9', 's2', 'Therefore, JEI needs to clearly show how we design learning for each child based on assessment results.', 'Therefore, J-E-I needs to clearly show how we design learning for each child based on assessment results.', 0),

    # 02. JEI's Strengths and Current Limitations
    ('l3_1', 's3', "JEI has five key strengths: precise diagnostic assessment, learning at each child's own pace, step-by-step workbooks, paper-based learning, and instructor coaching.", "J-E-I has five key strengths: precise diagnostic assessment, learning at each child's own pace, step-by-step workbooks, paper-based learning, and instructor coaching.", 0.25),
    ('l3_2', 's3', 'We also have a long history and a strong reputation for quality learning materials.', None, 0.25),
    ('l3_3', 's3', 'However, parents now have many learning options, including AI and digital programs.', None, 0.25),
    ('l3_4', 's3', 'So, we need to give parents a clear reason to choose JEI.', 'So, we need to give parents a clear reason to choose J-E-I.', 0.25),
    ('l3_5', 's3', 'The problem we want to solve is that assessment results do not always lead to the right learning materials, starting level, or learning pace for each child.', None, 0.25),
    ('l3_6', 's3', 'Even at JEI Learning Centers, if we assess students only when they first join, or only tell parents how far their child has progressed, parents may still have questions.', 'Even at J-E-I Learning Centers, if we assess students only when they first join, or only tell parents how far their child has progressed, parents may still have questions.', 0.25),
    ('l3_7', 's3', "Assessment results should lead to real changes in each child's learning.", None, 0.25),
    ('l3_8', 's3', 'We also need to show parents how these changes help their children improve.', None, 0.25),
    ('l3_9', 's3', 'Simply emphasizing self-learning, personalized learning, or AI is not enough to differentiate JEI from competitors.', 'Simply emphasizing self-learning, personalized learning, or AI is not enough to differentiate J-E-I from competitors.', 0),

    # 03. Parents' Needs and Primary Target Customers
    ('l4_1', 's4', 'The first question parents ask is, "Where is my child having difficulty, and what should my child learn first?"', 'The first question parents ask is, Where is my child having difficulty, and what should my child learn first?', 0.25),
    ('l4_2', 's4', 'When sharing assessment results, we should also explain which subject and level their child should start with, as well as the most appropriate learning pace.', None, 0.25),
    ('l4_3', 's4', 'Parents also want their children to study independently, without constant reminders.', None, 0.25),
    ('l4_4', 's4', "Once learning begins, short assignments and instructors' encouragement help children keep studying every day.", None, 0.25),
    ('l4_5', 's4', 'Over time, progress reports should show parents what their child can now do on their own and what they will learn next.', None, 0.25),
    ('l4_6', 's4', 'Our first priority is parents of children in Grades 1 to 4 who want to understand where their child is having difficulty.', 'Our first priority is parents of children in Grades one to four who want to understand where their child is having difficulty.', 0.25),
    ('l4_7', 's4', 'For Grades 1 and 2, we focus on building regular study habits and independent learning skills.', 'For Grades one and two, we focus on building regular study habits and independent learning skills.', 0.25),
    ('l4_8', 's4', 'For Grades 2 to 4, we focus on identifying learning gaps and areas of difficulty.', 'For Grades two to four, we focus on identifying learning gaps and areas of difficulty.', 0.25),
    ('l4_9', 's4', 'Seven-year-olds preparing for elementary school and students in Grades 5 and 6 are also important target groups.', 'Seven-year-olds preparing for elementary school and students in Grades five and six are also important target groups.', 0),

    # 04. Core Differentiation: From Assessment to Visible Growth
    ('l5_1', 's5', 'Our key differentiation is not simply better grading.', None, 0.25),
    ('l5_2', 's5', "It is how we connect assessment results to individualized learning and make each child's progress visible.", None, 0.25),
    ('l5_3', 's5', 'We use assessment to find where each child needs help.', None, 0.25),
    ('l5_4', 's5', 'Based on the results, we select appropriate workbooks, determine the starting level, and design an individualized learning path.', None, 0.25),
    ('l5_5', 's5', 'Instructors check their work, coach them where needed, and adjust their learning pace.', None, 0.25),
    ('l5_6', 's5', 'Then, we assess students again and use progress reports to see what has changed and set the next learning goal.', None, 0.25),
    ('l5_7', 's5', "This is how we connect assessment, individualized learning, and instructor coaching to each child's actual progress.", None, 0.25),
    ('l5_8', 's5', 'Progress reports should not simply present information in a better format.', None, 0.25),
    ('l5_9', 's5', 'They should provide clear evidence of how our learning system works and how children are improving.', None, 0),

    # 05. Proposed Brand Positioning and Customer Messaging
    ('l6_1', 's6', 'JEI aims to be a brand that helps children build the ability to grow on their own through precise assessment and personalized learning paths designed for each child.', 'J-E-I aims to be a brand that helps children build the ability to grow on their own through precise assessment and personalized learning paths designed for each child.', 0.25),
    ('l6_2', 's6', 'For parents, precise assessment is a reason to choose JEI.', 'For parents, precise assessment is a reason to choose J-E-I.', 0.25),
    ('l6_3', 's6', 'The core of our service is using assessment results to choose the right learning materials and learning sequence for each child.', None, 0.25),
    ('l6_4', 's6', 'Our goal is to help children understand more and solve more problems on their own.', None, 0.25),
    ('l6_5', 's6', "This is based on JEI's philosophy:", "This is based on J-E-I's philosophy.", 0.25),
    ('l6_6', 's6', '"We believe in the power of self-learning."', 'We believe in the power of self-learning.', 0.25),
    ('l6_7', 's6', 'Our message to customers is:', 'Our message to customers is.', 0.25),
    ('l6_8', 's6', '"What your child needs to learn. The power to learn independently."', 'What your child needs to learn. The power to learn independently.', 0.25),
    ('l6_9', 's6', 'We can explain this message in one sentence:', 'We can explain this message in one sentence.', 0.25),
    ('l6_10', 's6', '"Start with a precise assessment and focus on what your child needs to learn now."', 'Start with a precise assessment and focus on what your child needs to learn now.', 0.25),
    ('l6_11', 's6', "In our advertising and on our website, we will show how we check each child's level and help them learn step by step in the right order.", None, 0.25),
    ('l6_12', 's6', 'When meeting with parents, we will start by asking, "What should your child learn first?"', 'When meeting with parents, we will start by asking, What should your child learn first?', 0.25),
    ('l6_13', 's6', 'Rather than simply promoting personalized learning or AI features, we need to show parents what their child needs to learn and how their child is improving.', None, 0),

    # 06. Service Development and Operational Directions
    ('l7_1', 's7', "We need to connect JEI's strengths in assessment and learning management across subjects.", "We need to connect J-E-I's strengths in assessment and learning management across subjects.", 0.25),
    ('l7_2', 's7', 'First, we will set clear standards for assessment and learning plans.', None, 0),
    ('l7_3', 's7', 'Then, we will expand from Math to Korean and English.', None, 0.25),
    ('l7_4', 's7', 'Second, we will connect paper-based learning and instructor coaching with digital progress reports.', None, 0.25),
    ('l7_5', 's7', "These reports should help parents track their child's progress through mobile apps and parent consultations.", None, 0.25),
    ('l7_6', 's7', 'We can also explore how our Learning Centers and personalized POD workbooks could work together.', 'We can also explore how our Learning Centers and personalized P-O-D workbooks could work together.', 0.25),
    ('l7_7', 's7', 'In addition, we need to focus not only on new enrollment but also on student retention, the number of subjects per member, and revenue per customer.', None, 0.25),
    ('l7_8', 's7', 'We will check our results using enrollment rates after assessment, reassessment rates, report viewing rates, and retention rates.', None, 0),

    # Closing
    ('l8_1', 's8', "In the end, parents should be able to explain how their child's learning has changed and what the next learning goal is.", None, 0.25),
    ('l8_2', 's8', "Our goal is to connect precise assessment, individualized learning, and instructor coaching, and make each child's progress visible to parents.", None, 0.25),
    ('l8_3', 's8', 'This is the reason we want parents to choose JEI.', 'This is the reason we want parents to choose J-E-I.', 0.25),
    ('l8_4', 's8', 'This concludes my presentation.', None, 0.25),
    ('l8_5', 's8', 'Thank you.', None, 0),
]
CLONE = set()
LEAD, GAP, SCENE_GAP, TAIL = .6, .45, 1.0, 1.2
DING_BEFORE = None
import os
# pinned takes per voice (sorted position): female closing Thank you = θ æ n k uː at her normal pitch, 260 → 135 Hz (the first 3 takes sat at ~145 Hz)
TAKE = {'female': {'l8_5': 5}}.get(os.environ.get('VOICE'), {})
PACE = None
