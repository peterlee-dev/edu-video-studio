# The script: what is read, line by line. Edit this file, then run tools/make_audio.py tts (VOICE=male | female).
# Source: Google Docs "김현태 본부장님 · JEI Repositioning: Core Strategy (English Explanation Script | Presentation Summary)" (2026.11.09, 구글챗 유정 · 대언 · 승은 · 소정 방), body word for word.
# Not read: the doc title and meta lines, section headings and the footer. Audio only, no video: scenes are the doc's sections,
# all in CONT (no page-turn whoosh), SCENE_GAP is the pause between sections.
LANGUAGE = 'English'

SCENES = [('s1', 'Opening | Key Conclusion'), ('s2', '01 | Market Shifts and the Limitations of Traditional Competition'), ('s3', '02 | Customer Needs and Pain Points'), ('s4', '03 | Competitor Perceptions and the Learning Design Gap'), ('s5', '04 | Repositioning: From workbooks to Learning Design'), ('s6', '05 | Proposed Positioning Statement and Brand Messages'), ('s7', '06 | Proposed Strategic Actions'), ('s8', 'Closing')]
CONT = {s for s, _ in SCENES}

# (id, scene, line as written, line as read (None = as written), extra pause after it in s)
SCRIPT = [
    # Opening | Key Conclusion
    ('l1_1', 's1', 'Good morning, everyone.', None, 0),
    ('l1_2', 's1', "I'm Hyuntae Kim.", None, 0),
    ('l1_3', 's1', "Today, I will share JEI's core repositioning strategy.", "Today, I will share J-E-I's core repositioning strategy.", 0.25),
    ('l1_4', 's1', 'Let me start with our key conclusion.', None, 0),
    ('l1_5', 's1', 'JEI must move beyond competing on workbooks, scale, and digital features.', 'J-E-I must move beyond competing on workbooks, scale, and digital features.', 0),
    ('l1_6', 's1', "Our goal is to become the brand that designs learning to develop children's ability to learn independently.", None, 0.25),
    ('l1_7', 's1', 'I will explain the market changes, customer needs, the competitive gap, our positioning, and the strategic actions we need to take.', None, 0),

    # 01 | Market Shifts and the Limitations of Traditional Competition
    ('l2_1', 's2', 'First, let’s look at the challenges we face.', None, 0),
    ('l2_2', 's2', 'Three changes are important.', None, 0.25),
    ('l2_3', 's2', 'First, the limitations of our business scale.', None, 0),
    ('l2_4', 's2', 'JEI ranks fourth in the workbook market.', 'J-E-I ranks fourth in the workbook market.', 0),
    ('l2_5', 's2', 'We have about 300 locations, while some competitors have more than 700.', 'We have about three hundred locations, while some competitors have more than seven hundred.', 0),
    ('l2_6', 's2', 'It is difficult to compete based on size.', None, 0.25),
    ('l2_7', 's2', 'Second, changes in the market.', None, 0),
    ('l2_8', 's2', 'There are fewer children entering school, but spending per child is increasing.', None, 0),
    ('l2_9', 's2', 'This means there are fewer customers, but parents are willing to spend more when they see clear value.', None, 0.25),
    ('l2_10', 's2', 'Third, similar features across competitors.', None, 0),
    ('l2_11', 's2', 'AI-based assessment, personalized learning paths, and grading have now become standard features.', None, 0),
    ('l2_12', 's2', 'As these features become increasingly common, we need a different basis for competition.', None, 0),
    ('l2_13', 's2', 'This is why Learning Design is central to our repositioning strategy.', None, 0),

    # 02 | Customer Needs and Pain Points
    ('l3_1', 's3', 'So, what are parents really willing to pay for?', None, 0),
    ('l3_2', 's3', 'We can understand parents’ needs in three layers.', None, 0.25),
    ('l3_3', 's3', 'The first layer is functional needs: learning materials for different levels, connections to school curricula, and learning data.', None, 0),
    ('l3_4', 's3', 'The second layer is emotional needs.', None, 0),
    ('l3_5', 's3', 'Parents want to worry less about their children falling behind.', None, 0),
    ('l3_6', 's3', 'They also want someone to take care of their children’s learning.', None, 0.25),
    ('l3_7', 's3', 'The third and most important layer is children’s ability to learn on their own.', None, 0.25),
    ('l3_8', 's3', 'Why do parents discontinue learning programs?', None, 0),
    ('l3_9', 's3', 'Children may become bored with repetitive activities.', None, 0),
    ('l3_10', 's3', 'Standardized learning pace does not always meet individual needs.', None, 0),
    ('l3_11', 's3', 'Parents struggle to see clear learning outcomes or understand what their children should learn next.', None, 0),
    ('l3_12', 's3', "And much of the responsibility for managing their children's learning still falls on the parents.", None, 0.25),
    ('l3_13', 's3', 'These reasons point to one problem.', None, 0),
    ('l3_14', 's3', 'The problem is not simply a lack of learning materials.', None, 0),
    ('l3_15', 's3', 'Parents need a clearer understanding of what their children should learn next, why it matters, and how their learning will progress.', None, 0),
    ('l3_16', 's3', 'This is why we must shift our focus from workbooks to how children’s ability to learn improves.', None, 0),

    # 03 | Competitor Perceptions and the Learning Design Gap
    ('l4_1', 's4', 'Now, let’s look at whether our competitors are meeting this need.', None, 0),
    ('l4_2', 's4', 'These evaluations are based on customer perceptions.', None, 0.25),
    ('l4_3', 's4', 'Each of our three major competitors is associated with a different strength.', None, 0),
    ('l4_4', 's4', 'Daekyo emphasizes level-based learning, Kumon is known for repetition and building study habits, and Woongjin focuses on online and AI-powered learning platforms.', None, 0.25),
    ('l4_5', 's4', 'Daekyo does not have a clear long-term learning plan.', None, 0),
    ('l4_6', 's4', 'Kumon can become boring, causing children to lose interest.', None, 0),
    ('l4_7', 's4', "Woongjin's platform may feel complex, while screen-based learning can raise concerns about insufficient handwriting practice.", None, 0.25),
    ('l4_8', 's4', 'Above all, no company clearly answers the question parents really ask: “Where should my child’s learning be in three years?”', 'Above all, no company clearly answers the question parents really ask, Where should my child’s learning be in three years?', 0),
    ('l4_9', 's4', 'This is where “Design” comes in.', 'This is where Design comes in.', 0),
    ('l4_10', 's4', 'It means setting a direction after diagnosis and helping children stay motivated along the way.', None, 0.25),
    ('l4_11', 's4', 'According to Al Ries’s positioning principles, it is very difficult for a company ranked fourth to beat the leader in the same category.', 'According to Al Reese’s positioning principles, it is very difficult for a company ranked fourth to beat the leader in the same category.', 0),
    ('l4_12', 's4', 'Rather than trying to move up the existing competitive ladder, JEI aims to establish a new ladder centered on Learning Design—one where we can build a distinctive leadership position.', 'Rather than trying to move up the existing competitive ladder, J-E-I aims to establish a new ladder centered on Learning Design—one where we can build a distinctive leadership position.', 0),

    # 04 | Repositioning: From workbooks to Learning Design
    ('l5_1', 's5', 'We will move from selling workbooks to providing Learning Design.', None, 0),
    ('l5_2', 's5', 'We aim to provide personalized learning roadmaps that help each child understand what to learn next and how to progress.', None, 0.25),
    ('l5_3', 's5', 'We will build on our existing strengths: the JEI Self-Learning Method, diagnostic assessment, and structured learning materials.', 'We will build on our existing strengths: the J-E-I Self-Learning Method, diagnostic assessment, and structured learning materials.', 0),
    ('l5_4', 's5', 'But we will define self-learning as an ability, not just the act of studying.', None, 0),
    ('l5_5', 's5', 'This builds on the nearly 50-year legacy of the JEI Self-Learning Method.', 'This builds on the nearly fifty-year legacy of the J-E-I Self-Learning Method.', 0.25),
    ('l5_6', 's5', 'Our focus is not simply to have more locations or members than competitors.', None, 0),
    ('l5_7', 's5', 'We want to create clear learning paths for individual students and become a leader in the Learning Design category.', None, 0),

    # 05 | Proposed Positioning Statement and Brand Messages
    ('l6_1', 's6', 'Our proposed positioning statement is: "JEI designs learning to develop children\'s ability to learn independently."', "Our proposed positioning statement is, J-E-I designs learning to develop children's ability to learn independently.", 0.25),
    ('l6_2', 's6', "This statement reflects our shift from simply providing workbooks to developing children's Self-Learning Ability through Learning Design.", None, 0.25),
    ('l6_3', 's6', 'Our brand messaging is built around two key concepts: "Design" and "Self-Learning Ability."', 'Our brand messaging is built around two key concepts, Design and Self-Learning Ability.', 0.25),
    ('l6_4', 's6', 'We have proposed several slogan options, including "Learning starts with design," "Studying starts with design," and "Beyond Workbooks. Toward Learning Design."', 'We have proposed several slogan options, including Learning starts with design, Studying starts with design, and Beyond Workbooks. Toward Learning Design.', 0.25),
    ('l6_5', 's6', 'Our proposed campaign message is: "It\'s not a lack of ability. It\'s a lack of learning design."', "Our proposed campaign message is, It's not a lack of ability. It's a lack of learning design.", 0.25),
    ('l6_6', 's6', 'And our customer value message is: "The ability to learn independently begins with Learning Design."', 'And our customer value message is, The ability to learn independently begins with Learning Design.', 0.25),
    ('l6_7', 's6', 'These are proposed expressions, not finalized brand slogans.', None, 0),
    ('l6_8', 's6', "Whatever we ultimately choose, our messages must reinforce a clear and consistent position in customers' minds.", None, 0),

    # 06 | Proposed Strategic Actions
    ('l7_1', 's7', 'Finally, let me outline five strategic priorities for execution.', None, 0.25),
    ('l7_2', 's7', 'First, we will focus on our strongest core subjects rather than promoting all 17 subjects equally.', 'First, we will focus on our strongest core subjects rather than promoting all seventeen subjects equally.', 0),
    ('l7_3', 's7', 'This will allow us to build a clear and differentiated Learning Design approach.', None, 0.25),
    ('l7_4', 's7', 'Second, we will strengthen the connection between assessment, Learning Design, and coaching.', None, 0),
    ('l7_5', 's7', "Each child's learning needs will be assessed, the next learning steps will be designed, and instructors will provide personalized guidance along the way.", None, 0.25),
    ('l7_6', 's7', 'Third, we will continue to emphasize the role of our instructors.', None, 0),
    ('l7_7', 's7', 'While AI-powered learning solutions are important, personal guidance and ongoing learning support remain key reasons why parents choose JEI.', 'While AI-powered learning solutions are important, personal guidance and ongoing learning support remain key reasons why parents choose J-E-I.', 0.25),
    ('l7_8', 's7', 'Fourth, we will communicate a consistent brand message across our products, learning centers, local offices, and advertising.', None, 0),
    ('l7_9', 's7', '"Design" and "Self-Learning Ability" should remain central to how we present our brand.', 'Design and Self-Learning Ability should remain central to how we present our brand.', 0.25),
    ('l7_10', 's7', 'Fifth, we will focus on increasing value per customer and recognize the importance of multi-subject learning, while avoiding competition based solely on the number of subjects or overall business scale.', None, 0.25),
    ('l7_11', 's7', 'Together, these priorities will help JEI strengthen its position in Learning Design and deliver greater value to children and their families.', 'Together, these priorities will help J-E-I strengthen its position in Learning Design and deliver greater value to children and their families.', 0),

    # Closing
    ('l8_1', 's8', "To summarize, JEI aims to move beyond workbooks and establish a leadership position in Learning Design by designing learning to develop children's ability to learn independently.", "To summarize, J-E-I aims to move beyond workbooks and establish a leadership position in Learning Design by designing learning to develop children's ability to learn independently.", 0.25),
    ('l8_2', 's8', 'To achieve this, we must change first.', None, 0),
    ('l8_3', 's8', 'When we develop products, meet customers, and discuss ideas in meetings, we must all use the same language.', None, 0),
    ('l8_4', 's8', 'Starting today, our shared message is “Designing the Ability to Learn.”', 'Starting today, our shared message is Designing the Ability to Learn.', 0.25),
    ('l8_5', 's8', 'Thank you.', None, 0),
    ('l8_6', 's8', 'Please feel free to ask any questions.', None, 0),
]
CLONE = set()
LEAD, GAP, SCENE_GAP, TAIL = .6, .45, 1.0, 1.2
DING_BEFORE = None
import os
# pinned takes per voice (sorted position): female l1_2 Hyuntae = h iː ʊ n t eɪ (the other 10 takes read hoon-tee / heen-tie / hi-yoon-tay)
TAKE = {'female': {'l1_2': 3}}.get(os.environ.get('VOICE'), {})
PACE = None
