# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: "JEI Repositioning: Core Strategy", the English script pasted in the request (2026.11.06), one section per deck page, word for word.
# Deck: (클라우드)재능교육 리포지셔닝 핵심전략_통합본(쳇GPT+젠스파크)_국문_최종.pptx (22 pages + 2 appendix pages of translation notes, Korean)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Opening'), ('questions', 'Five key questions'), ('position', 'Our current position'),
    ('market', 'Changes in the market'), ('aiStandard', 'AI is becoming standard'), ('needs', 'What parents really want'),
    ('churn', 'Why parents leave'), ('competitors', 'Competitor positioning'), ('opportunity', 'The opportunity: Learning Design'),
    ('ladder', 'Creating a new category'), ('principles', 'Six positioning principles'), ('strategies', 'Five core strategies'),
    ('roadmap', 'Strategy 1: Personalized learning roadmaps'), ('subjects', 'Strategy 2: Focus on core subjects'),
    ('studios', 'Strategy 3: Learning Design Studios'), ('hybrid', 'Strategy 4: AI and human coaching'),
    ('selfLearning', 'Strategy 5: Redefining self-learning'), ('statement', 'Our positioning statement'),
    ('services', 'Five services that prove our value'), ('message', 'A consistent brand message'),
    ('metrics', 'Measuring success'), ('outro', 'Closing'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    # p.01 · opening
    ('l1_1', 'title', "Today, I'd like to share JEI's core repositioning strategy.", "Today, I'd like to share J-E-I's core repositioning strategy.", .1),
    ('l1_2', 'title', "Our main message is simple.", None, 0),
    ('l1_3', 'title', "JEI must move beyond selling worksheets and become a company that designs children's ability to learn on their own.",
     "J-E-I must move beyond selling worksheets and become a company that designs children's ability to learn on their own.", .3),

    # p.02 · five key questions
    ('l2_1', 'questions', "Our strategy addresses five questions.", None, .1),
    ('l2_2', 'questions', "Why do we need to change?", None, 0),
    ('l2_3', 'questions', "What do parents really want?", None, 0),
    ('l2_4', 'questions', "Where are the opportunities?", None, 0),
    ('l2_5', 'questions', "How can JEI compete?", "How can J-E-I compete?", 0),
    ('l2_6', 'questions', "And how will we deliver and measure our results?", None, .2),
    ('l2_7', 'questions', "Let's begin with the market.", None, .3),

    # p.03 · our current position
    ('l3_1', 'position', "JEI currently ranks fourth in Korea's worksheet learning market.", "J-E-I currently ranks fourth in Korea's worksheet learning market.", 0),
    ('l3_2', 'position', "Our three main competitors have more than 700 locations and over one million members each, while JEI has about 300 locations.",
     "Our three main competitors have more than seven hundred locations and over one million members each, while J-E-I has about three hundred locations.", 0),
    ('l3_3', 'position', "Our revenue also fell by 53% between 2010 and 2025.",
     "Our revenue also fell by fifty-three percent between twenty ten and twenty twenty-five.", .1),
    ('l3_4', 'position', "Competing through size alone is difficult.", None, 0),
    ('l3_5', 'position', "We need to create a new category.", None, .3),

    # p.04 · changes in the market
    ('l4_1', 'market', "The number of children in Korea is declining.", None, 0),
    ('l4_2', 'market', "In 2026, about 298,000 children entered first grade, down 8% from the previous year.",
     "In twenty twenty-six, about two hundred ninety-eight thousand children entered first grade, down eight percent from the previous year.", 0),
    ('l4_3', 'market', "Total private education spending also fell to 27.5 trillion won in 2025.",
     "Total private education spending also fell to twenty-seven point five trillion won in twenty twenty-five.", .1),
    ('l4_4', 'market', "However, monthly spending per elementary student participating in private education reached 512,000 won.",
     "However, monthly spending per elementary student participating in private education reached five hundred twelve thousand won.", 0),
    ('l4_5', 'market', "Parents are willing to pay for clear value.", None, .1),
    ('l4_6', 'market', "Our focus must shift toward greater value per customer and stronger retention.", None, .3),

    # p.05 · AI is becoming standard
    ('l5_1', 'aiStandard', "AI-based assessment, personalized learning, and automatic grading are becoming common across the industry.", None, 0),
    ('l5_2', 'aiStandard', "These features alone are no longer enough to stand out.", None, .1),
    ('l5_3', 'aiStandard', "Parents want to save time, reduce their burden, and see clear learning progress.", None, 0),
    ('l5_4', 'aiStandard', "JEI must offer something beyond worksheets and AI features.", "J-E-I must offer something beyond worksheets and AI features.", .3),

    # p.06 · what parents really want
    ('l6_1', 'needs', "Parents have three levels of needs.", None, .1),
    ('l6_2', 'needs', "Functional needs include suitable materials and learning reports.", None, 0),
    ('l6_3', 'needs', "Emotional needs include less worry and less responsibility for managing study.", None, 0),
    ('l6_4', 'needs', "But their most important need is for their children to learn independently.", None, .1),
    ('l6_5', 'needs', "JEI should focus on developing this ability through personalized learning plans and teacher support.",
     "J-E-I should focus on developing this ability through personalized learning plans and teacher support.", .3),

    # p.07 · why parents leave
    ('l7_1', 'churn', "Parents often stop learning services for five reasons.", None, .1),
    ('l7_2', 'churn', "Repetitive learning becomes boring.", None, 0),
    ('l7_3', 'churn', "Progress is difficult to see.", None, 0),
    ('l7_4', 'churn', "Parents still manage daily study.", None, 0),
    ('l7_5', 'churn', "Fees increase without clear results.", None, 0),
    ('l7_6', 'churn', "And AI features make brands look similar.", None, .2),
    ('l7_7', 'churn', "The main problem is that parents cannot clearly see their children's growth.", None, 0),
    ('l7_8', 'churn', "This is the problem JEI must solve.", "This is the problem J-E-I must solve.", .3),

    # p.08 · competitor positioning
    ('l8_1', 'competitors', "Our three main competitors have different strengths.", None, .1),
    ('l8_2', 'competitors', "Daekyo focuses on level-based learning.", None, 0),
    ('l8_3', 'competitors', "Kumon is known for basic skills and repetition.", None, 0),
    ('l8_4', 'competitors', "Woongjin offers an integrated learning platform.", None, .1),
    ('l8_5', 'competitors', "But from a customer perspective, these approaches may leave gaps in long-term learning direction, motivation, and personalized support.", None, 0),
    ('l8_6', 'competitors', "JEI should focus on these opportunities rather than directly copying competitors.",
     "J-E-I should focus on these opportunities rather than directly copying competitors.", .3),

    # p.09 · the opportunity: Learning Design
    ('l9_1', 'opportunity', "Competitors mainly focus on how learning is delivered.", None, 0),
    ('l9_2', 'opportunity', "But parents want to know something more.", None, .1),
    ('l9_3', 'opportunity', "\"Where should my child's learning go over the next three years?\"",
     "Where should my child's learning go over the next three years?", .2),
    ('l9_4', 'opportunity', "We believe this creates an opportunity for Learning Design.", None, 0),
    ('l9_5', 'opportunity', "JEI can use assessment results to create personalized learning paths and help students stay motivated.",
     "J-E-I can use assessment results to create personalized learning paths and help students stay motivated.", 0),
    ('l9_6', 'opportunity', "This can become our new position in the market.", None, .3),

    # p.10 · creating a new category. Al Ries is read "Al Reese"
    ('l10_1', 'ladder', "Al Ries explained that positioning happens in the customer's mind.", "Al Reese explained that positioning happens in the customer's mind.", 0),
    ('l10_2', 'ladder', "Customers often rank brands on a ladder within each category.", None, .1),
    ('l10_3', 'ladder', "JEI is currently number four in the worksheet market.", "J-E-I is currently number four in the worksheet market.", 0),
    ('l10_4', 'ladder', "Instead of competing on the same ladder, we can create a new one.", None, .1),
    ('l10_5', 'ladder', "That new category is Learning Design.", None, 0),
    ('l10_6', 'ladder', "Our goal is to become the brand customers associate with \"Design.\"",
     "Our goal is to become the brand customers associate with, Design.", .3),

    # p.11 · six positioning principles
    ('l11_1', 'principles', "We can apply six positioning principles from Al Ries.", "We can apply six positioning principles from Al Reese.", .1),
    ('l11_2', 'principles', "First, the Law of the Ladder: create a new category.", "First, the Law of the Ladder. Create a new category.", 0),
    ('l11_3', 'principles', "Second, the Law of the Opposite: offer what competitors do not clearly provide.",
     "Second, the Law of the Opposite. Offer what competitors do not clearly provide.", 0),
    ('l11_4', 'principles', "Third, the Law of Sacrifice: focus on core subjects.", "Third, the Law of Sacrifice. Focus on core subjects.", 0),
    ('l11_5', 'principles', "Fourth, avoid the trap of line extension by expanding the meaning of self-learning rather than adding more products.", None, 0),
    ('l11_6', 'principles', "Fifth, the Laws of the Mind and Focus: communicate one clear word, \"Design,\" starting with parents of first- and second-grade students.",
     "Fifth, the Laws of the Mind and Focus. Communicate one clear word, Design, starting with parents of first and second grade students.", 0),
    ('l11_7', 'principles', "Sixth, the Law of Candor: acknowledge our smaller scale and focus on each child's learning.",
     "Sixth, the Law of Candor. Acknowledge our smaller scale and focus on each child's learning.", .3),

    # p.12 · five core strategies
    ('l12_1', 'strategies', "We have five core strategies.", None, .1),
    ('l12_2', 'strategies', "First, redefine our category as Learning Design.", None, 0),
    ('l12_3', 'strategies', "Second, focus on core subjects.", None, 0),
    ('l12_4', 'strategies', "Third, transform our locations into Learning Design Studios.", None, 0),
    ('l12_5', 'strategies', "Fourth, combine AI with human coaching.", None, 0),
    ('l12_6', 'strategies', "And fifth, redefine self-learning as an ability.", None, .1),
    ('l12_7', 'strategies', "These strategies work together to build a stronger position for JEI.",
     "These strategies work together to build a stronger position for J-E-I.", .3),

    # p.13 · strategy 1: personalized learning roadmaps
    ('l13_1', 'roadmap', "Our products should move beyond question difficulty and volume.", None, 0),
    ('l13_2', 'roadmap', "Instead, we will focus on personalized learning roadmaps.", None, .1),
    ('l13_3', 'roadmap', "The process has four steps.", None, 0),
    ('l13_4', 'roadmap', "Assess each child's level.", None, 0),
    ('l13_5', 'roadmap', "Set learning goals and a roadmap.", None, 0),
    ('l13_6', 'roadmap', "Follow a personalized learning routine.", None, 0),
    ('l13_7', 'roadmap', "And regularly review progress and provide coaching.", None, .1),
    ('l13_8', 'roadmap', "This cycle will guide each child's learning.", None, .3),

    # p.14 · strategy 2: focus on core subjects
    ('l14_1', 'subjects', "JEI currently offers 17 subjects.", "J-E-I currently offers seventeen subjects.", 0),
    ('l14_2', 'subjects', "We will focus our resources on five priority subjects: Math, Korean, English, Thinking Pizza, and Hanja.",
     "We will focus our resources on five priority subjects. Math, Korean, English, Thinking Pizza, and Hanja.", 0),
    ('l14_3', 'subjects', "Other subjects may be reduced or managed through partnerships and referrals.", None, .1),
    ('l14_4', 'subjects', "Our initial target is parents of first- and second-grade students choosing their first learning program.",
     "Our initial target is parents of first and second grade students choosing their first learning program.", 0),
    ('l14_5', 'subjects', "By focusing our expertise, we can build stronger customer trust.", None, .3),

    # p.15 · strategy 3: Learning Design Studios
    ('l15_1', 'studios', "We plan to transform approximately 300 locations into Learning Design Studios.",
     "We plan to transform approximately three hundred locations into Learning Design Studios.", 0),
    ('l15_2', 'studios', "Each studio will provide three services.", None, 0),
    ('l15_3', 'studios', "An AI Diagnostic Report to identify the child's current level.", None, 0),
    ('l15_4', 'studios', "A personalized three-month and annual learning roadmap.", None, 0),
    ('l15_5', 'studios', "And monthly coaching to review progress and support learning habits.", None, .1),
    ('l15_6', 'studios', "Our locations will become centers for assessment, design, and coaching.", None, .3),

    # p.16 · strategy 4: AI and human coaching
    ('l16_1', 'hybrid', "AI will provide personalized questions, assess learning, grade answers, and prepare reports.", None, 0),
    ('l16_2', 'hybrid', "Learning Design Coaches will use these results to create learning plans and support motivation and study habits.", None, .1),
    ('l16_3', 'hybrid', "AI handles learning data, while teachers provide human guidance.", None, 0),
    ('l16_4', 'hybrid', "This combination is one of JEI's key strengths.", "This combination is one of J-E-I's key strengths.", .2),
    ('l16_5', 'hybrid', "\"AI provides the questions. JEI designs the learning.\"", "AI provides the questions. J-E-I designs the learning.", .3),

    # p.17 · strategy 5: redefining self-learning
    ('l17_1', 'selfLearning', "JEI has promoted the Self-Learning Method for nearly 50 years.",
     "J-E-I has promoted the Self-Learning Method for nearly fifty years.", 0),
    ('l17_2', 'selfLearning', "But today, many education companies use the term \"self-learning.\"",
     "But today, many education companies use the term, self-learning.", 0),
    ('l17_3', 'selfLearning', "We need to give it a stronger meaning.", None, .1),
    ('l17_4', 'selfLearning', "Self-learning is not simply studying alone.", None, 0),
    ('l17_5', 'selfLearning', "It is the ability to learn independently.", None, .1),
    ('l17_6', 'selfLearning', "JEI will focus on designing and developing this ability in every child.",
     "J-E-I will focus on designing and developing this ability in every child.", .3),

    # p.18 · our positioning statement
    ('l18_1', 'statement', "\"JEI designs children's ability to learn on their own.\"", "J-E-I designs children's ability to learn on their own.", .2),
    ('l18_2', 'statement', "This statement represents our new direction.", None, 0),
    ('l18_3', 'statement', "It creates a new category, establishes \"Design\" as our key word, reflects the importance of human support in the AI era, and builds on JEI's educational heritage.",
     "It creates a new category, establishes Design as our key word, reflects the importance of human support in the AI era, and builds on J-E-I's educational heritage.", 0),
    ('l18_4', 'statement', "It will guide our products, services, and communication.", None, .3),

    # p.19 · five services that prove our value
    ('l19_1', 'services', "We will demonstrate Learning Design through five services.", None, .1),
    ('l19_2', 'services', "An AI Diagnostic Report.", None, 0),
    ('l19_3', 'services', "A personalized learning roadmap.", None, 0),
    ('l19_4', 'services', "Monthly coaching.", None, 0),
    ('l19_5', 'services', "A learning routine record.", None, 0),
    ('l19_6', 'services', "And a Self-Learning Ability Growth Report.", None, .1),
    ('l19_7', 'services', "These services will help parents see their children's progress and reduce their management burden.", None, 0),
    ('l19_8', 'services', "To achieve this, we must first strengthen our core-subject curricula.", None, .3),

    # p.20 · a consistent brand message
    ('l20_1', 'message', "Our brand communication has three levels.", None, .1),
    ('l20_2', 'message', "First, key words: \"Design\" and \"Self-Learning Ability.\"", "First, key words. Design, and Self-Learning Ability.", 0),
    ('l20_3', 'message', "Second, brand slogans, such as \"Learning Starts with Design.\"", "Second, brand slogans, such as, Learning Starts with Design.", 0),
    ('l20_4', 'message', "Third, campaign messages that encourage parents to take action.", None, .1),
    ('l20_5', 'message', "We should not use too many messages at once.", None, 0),
    ('l20_6', 'message', "One clear and consistent message will help customers remember JEI.",
     "One clear and consistent message will help customers remember J-E-I.", .3),

    # p.21 · measuring success
    ('l21_1', 'metrics', "After 12 months, we will evaluate five indicators.", "After twelve months, we will evaluate five indicators.", .1),
    ('l21_2', 'metrics', "Brand association with independent learning ability.", None, 0),
    ('l21_3', 'metrics', "The share of new first- and second-grade students.", "The share of new first and second grade students.", 0),
    ('l21_4', 'metrics', "A 100% delivery rate for Learning Design Reports.", "A one hundred percent delivery rate for Learning Design Reports.", 0),
    ('l21_5', 'metrics', "Customer retention and cancellation rates.", None, 0),
    ('l21_6', 'metrics', "And the share of revenue from core subjects.", None, .1),
    ('l21_7', 'metrics', "These indicators will show whether our strategy is producing real results.", None, .3),

    # p.22 · closing
    ('l22_1', 'outro', "Daekyo is known for levels, Kumon for repetition, and Woongjin for its platform.", None, 0),
    ('l22_2', 'outro', "JEI will focus on a new opportunity: Learning Design.", "J-E-I will focus on a new opportunity. Learning Design.", .1),
    ('l22_3', 'outro', "We want to become more than a worksheet company.", None, 0),
    ('l22_4', 'outro', "We want to become a company that designs children's ability to learn independently.", None, .2),
    ('l22_5', 'outro', "Our focus is clear: Designing the Ability to Learn.", "Our focus is clear. Designing the Ability to Learn.", .4),
    ('l22_6', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = None   # no chime before the thank-you (as in ../jei-corporation-overview-female)
# line id → take index (sorted take position) where the picked take reads wrong or clips its end
TAKE = {}
TEMPO = 1.0
# the reference voice: audio/<VOICE>.wav + .txt. voice_ref = the adaptive diagnosis recording 14.1–28.95 s (female English, ../adaptive-diagnosis-v2/audio/narration.mp3)
VOICE = 'voice_ref'
