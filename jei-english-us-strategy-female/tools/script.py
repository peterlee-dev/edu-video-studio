# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: 미주 지사 공유 문건 스크립트 - 1-2. [ENG, 1차] 미주 영어 기획(안).pdf (ENG_Short Version, word for word; only the doubled
# full stop at the end of the literacy page is made single). Deck: 1. [미주 공유용] 미주 JEI 영어 개발 방향 및 전략_v3_261105.pdf (22 pages)
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [
    ('title', 'Title'),
    # 01 development direction (deck p.2–3)
    ('goal', 'What sets the new program apart'), ('beyond', 'Beyond reading'), ('path', 'Assess → path → progress'),
    ('literacy', 'What literacy means'), ('connect', 'Language skills → reading, writing, thinking'),
    # 02 education and market (deck p.4–7)
    ('ncte', 'NCTE · past ten years'), ('ncteNext', 'NCTE · next ten years'), ('ncteJei', 'NCTE · our direction'),
    ('naep', 'NAEP 2024'), ('naepDrop', 'NAEP · five-point drop'),
    ('parents', 'What parents want'), ('address', 'Assessment, roadmap, reports'),
    ('opportunity', 'Market opportunity'),
    # 03 competition and analysis (deck p.8–12)
    ('rivals', 'Competitors'), ('standOut', 'Where JEI can stand out'), ('showWhat', 'Problems, next steps, growth'), ('slogan', 'Accurate Assessment, Clear Growth'), ('hospital', 'Like a diagnosis specialist'),
    ('c3cust', '3C · customer'), ('c3comp', '3C · competitors'), ('c3jei', '3C · company'), ('c3plan', '3C · what we will do'),
    ('bench', 'Literacy product benchmark'), ('benchJei', 'Our difference'), ('benchNext', 'Further study'),
    ('swotS', 'SWOT · strengths'), ('swotW', 'SWOT · weakness'), ('swotO', 'SWOT · opportunities'), ('swotT', 'SWOT · threats'), ('swotSum', 'SWOT · direction'),
    ('ansoff', 'Ansoff Matrix'), ('ansoffPD', 'Product development'),
    # 04 target and positioning (deck p.13–16)
    ('target', 'Pre-K to Grade 9, Grades 3–6 first'), ('targetWhy', 'Why Grades 3–6'),
    ('posMap', 'Positioning map'), ('posX', 'Horizontal axis'), ('posY', 'Vertical axis'), ('posJei', 'JEI English today'), ('posKumon', 'Kumon'),
    ('posShift', 'The market moves on'), ('posMove', 'From Q4 to Q1'), ('position', 'Key position'),
    ('journey', 'Customer journey'), ('journeyFix', 'Clear at every stage'),
    ('fourP', '4P · product, price'), ('fourP2', '4P · place, promotion'),
    # 05 product and next steps (deck p.17–22)
    ('step1', 'Blended learning · Step 1'), ('step2', 'Blended learning · Step 2'),
    ('ai1', 'AI · tutor, analysis'), ('ai2', 'AI · POD scan, content'),
    ('direction', 'Product direction'), ('nextA', 'Next steps 1–2'), ('nextB', 'Next steps 3–4'), ('summary', 'Final direction'),
    ('ccss', 'Standards vary by state'), ('ccssPlan', 'Common ELA structure'),
    ('platform', 'Learning experience'), ('platform2', 'POD, online or both'),
    ('three', 'Three steps'), ('adaptive', 'Adaptive Learning'),
    ('outro', 'Thank you'),
]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = {'ncteNext', 'ncteJei', 'c3comp', 'c3jei', 'swotW', 'swotO', 'swotT', 'swotSum', 'ansoffPD', 'targetWhy',
        'posX', 'posY', 'posJei', 'posKumon', 'posShift', 'posMove', 'journeyFix', 'fourP2', 'step2', 'ai2', 'nextB', 'platform2', 'adaptive'}

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    ('l1_1', 'title', "We would like to share our development strategy and direction for the new JEI English program in the U.S.", None, .3),

    # deck p.2 · development direction
    ('l2_1', 'goal', "We aim to develop a new JEI English program centered on literacy development.", None, 0),
    ('l2_2', 'goal', "What sets the new JEI English program apart is not simply more literacy content.", None, 0),
    ('l2_3', 'goal', "While our current program already develops foundational language and basic literacy skills, the new program will integrate literacy instruction, precise assessment, personalized learning, and progress tracking into one integrated learning experience.", None, .2),
    ('l2_5', 'beyond', "More specifically, we want students to go beyond reading English.", None, 0),
    ('l2_6', 'beyond', "We want them to understand texts, make decisions, and express their own ideas.", None, .2),
    ('l2_7', 'path', "Through precise assessment, we will identify each student's current level and areas that need improvement.", None, 0),
    ('l2_8', 'path', "We will then provide a personalized learning path and use learning results to track each student's progress.", None, .2),
    # deck p.3 · literacy in U.S. education
    ('l3_1', 'literacy', "In U.S. education, literacy means more than reading comprehension.", None, 0),
    ('l3_2', 'literacy', "It goes beyond understanding texts.", None, 0),
    ('l3_3', 'literacy', "Literacy also includes understanding complex texts, using evidence to make decisions, and expressing ideas.", None, .2),
    ('l3_4', 'connect', "These skills also support learning across different subjects.", None, 0),
    ('l3_5', 'connect', "For our new program, we plan to connect basic language skills, such as Phonics, Vocabulary, and Grammar, with Reading, Writing, and Thinking.", None, 0),
    ('l3_6', 'connect', "Our goal is to help students move beyond reading comprehension to deeper understanding, decision-making, and expression.", None, .3),

    # deck p.4 · NCTE
    ('l4_1', 'ncte', "We also reviewed NCTE's major education directions over the past ten years and their possible direction for the next ten years.", "We also reviewed N-C-T-E's major education directions over the past ten years and their possible direction for the next ten years.", 0),
    ('l4_2', 'ncte', "Over the past decade, digital and media literacy, along with critical literacy, have been important areas of focus.", None, 0),
    ('l4_3', 'ncte', "These areas emphasize reading and evaluating texts critically, making independent decisions, and expressing ideas.", None, .2),
    ('l4_4', 'ncteNext', "Looking ahead, the growing use of AI agents is expected to make new skills even more important.", None, 0),
    ('l4_5', 'ncteNext', "These include understanding and using AI critically, human-centered writing, digital citizenship, and expressing ideas in different ways.", None, .2),
    ('l4_6', 'ncteJei', "Based on these findings, our English team plans to develop a program that goes beyond basic literacy.", None, 0),
    ('l4_7', 'ncteJei', "We want students to evaluate information and express their ideas clearly and logically.", None, .3),
    # deck p.5 · NAEP
    ('l5_1', 'naep', "According to the 2024 NAEP results, reading achievement in the U.S. remains below pre-pandemic levels.", None, 0),
    ('l5_2', 'naep', "Only about 30% of Grade 4 and Grade 8 students reached the Proficient level in reading.", None, .2),
    ('l5_3', 'naepDrop', "Both grades also showed a five-point drop in average reading scores from 2019 to 2024.", None, 0),
    ('l5_4', 'naepDrop', "These results show a continued need to improve reading comprehension and literacy skills.", None, .3),
    # deck p.6 · market changes and the need for improvement
    ('l6_1', 'parents', "Parents increasingly want personalized learning and clear evidence of progress.", None, 0),
    ('l6_2', 'parents', "JEI already has strong assessment and learning systems, but our strengths and learning results are not always clear to parents.", "J-E-I already has strong assessment and learning systems, but our strengths and learning results are not always clear to parents.", .2),
    ('l6_3', 'address', "To address this, we plan to use online Adaptive Assessment to better identify each student's current level and areas that need improvement.", None, 0),
    ('l6_4', 'address', "We will then provide a personalized learning roadmap that parents can easily understand.", None, 0),
    ('l6_5', 'address', "We also plan to improve our reports so parents can clearly see progress and achievement for each learning objective, supported by learning results.", None, .3),
    # deck p.7 · market opportunity
    ('l7_1', 'opportunity', "We also reviewed opportunities in the U.S. education market.", None, 0),
    ('l7_2', 'opportunity', "Although the market is already well developed, we found that parents continue to show demand for extra education.", None, 0),
    ('l7_3', 'opportunity', "They are also still willing to spend money on additional learning support for their children.", None, 0),
    ('l7_4', 'opportunity', "This shows that there are still opportunities for JEI in the U.S. education market.", None, .3),

    # deck p.8 · competitive landscape
    ('l8_1', 'rivals', "We reviewed major competitors to understand how each brand is positioned in the market and what direction JEI should take.", "We reviewed major competitors to understand how each brand is positioned in the market and what direction J-E-I should take.", 0),
    ('l8_2', 'rivals', "Kumon is known for repeated practice and building learning habits.", None, 0),
    ('l8_3', 'rivals', "Eye Level focuses on level-based personalized learning.", None, 0),
    ('l8_4', 'rivals', "Best Brains focuses on instruction by qualified teachers.", None, 0),
    ('l8_5', 'rivals', "Huntington focuses on test preparation and improving academic results.", None, .2),
    ('l8_6', 'standOut', "We believe JEI has limited opportunities to stand out if we compete only on repeated practice, test scores, or price.", None, 0),
    ('l8_7', 'standOut', "Instead, we need to build on our strength in precise assessment.", None, .2),
    ('l8_8', 'showWhat', "We want to clearly show what each student's learning problems are, what they need to learn next, and how much they have improved.", None, 0),
    ('l8_9', 'showWhat', "In other words, we want to connect assessment, personalized learning paths, and clear evidence of growth.", None, .2),
    ('l8_10', 'slogan', "Our goal is to build a clear position around the message:", None, .1),
    ('l8_11', 'slogan', "Accurate Assessment and Clear Growth.", None, .2),
    ('l8_12', 'hospital', "Think about hospitals.", None, 0),
    ('l8_13', 'hospital', "Almost all of them have CT and MRI scans, but patients only trust a select few as true diagnostic specialists.", "Almost all of them have C-T and M-R-I scans, but patients only trust a select few as true diagnostic specialists.", 0),
    ('l8_14', 'hospital', "That's the kind of authority JEI should have: a learning program recognized for precise diagnosis and real student growth.", "That's the kind of authority J-E-I should have: a learning program recognized for precise diagnosis and real student growth.", .3),
    # deck p.9 · 3C analysis
    ('l9_1', 'c3cust', "We also conducted a 3C analysis.", "We also conducted a three C analysis.", 0),
    ('l9_2', 'c3cust', "Our findings show that parents expect more than basic English learning.", None, 0),
    ('l9_3', 'c3cust', "They want stronger literacy skills, learning that matches each student's level, and clear evidence of improvement.", None, 0),
    ('l9_4', 'c3cust', "They also want their children to gain confidence through learning success.", None, .2),
    ('l9_5', 'c3comp', "When we look at competitors, each has already developed its own strengths.", None, 0),
    ('l9_6', 'c3comp', "Kumon focuses on repeated practice and self-learning.", None, 0),
    ('l9_7', 'c3comp', "Eye Level provides literacy learning across reading, writing, grammar, and vocabulary.", None, 0),
    ('l9_8', 'c3comp', "Sylvan and Huntington focus on assessment-based tutoring and test results.", None, 0),
    ('l9_9', 'c3comp', "Best Brains provides small-group Language Arts instruction.", None, .2),
    ('l9_10', 'c3jei', "JEI also has important strengths.", "J-E-I also has important strengths.", 0),
    ('l9_11', 'c3jei', "These include small-step learning, a spiral curriculum, structured content, and assessment-based self-learning.", None, 0),
    ('l9_12', 'c3jei', "However, these strengths and learning results are not yet clearly shown to parents.", None, .2),
    ('l9_13', 'c3plan', "Therefore, we want to maintain JEI's strengths in small-step and structured learning.", "Therefore, we want to maintain J-E-I's strengths in small-step and structured learning.", 0),
    ('l9_14', 'c3plan', "At the same time, we plan to strengthen literacy education and use precise assessment to provide personalized learning paths.", None, 0),
    ('l9_15', 'c3plan', "We also want to make each student's progress and results easier to see.", None, 0),
    ('l9_16', 'c3plan', "This will help us build a stronger position in the market.", None, .3),
    # deck p.10 · U.S. literacy product benchmark
    ('l10_1', 'bench', "We reviewed the main approaches and strengths of major literacy programs in the U.S.", None, 0),
    ('l10_2', 'bench', "Amplify builds background knowledge to support reading comprehension.", None, 0),
    ('l10_3', 'bench', "Lexia uses learning data to identify skills that need improvement.", None, 0),
    ('l10_4', 'bench', "i-Ready connects assessment results with personalized learning.", None, 0),
    ('l10_5', 'bench', "IXL tracks progress across individual skills.", "I-X-L tracks progress across individual skills.", .2),
    ('l10_6', 'benchJei', "We want to learn from these programs and their strengths.", None, 0),
    ('l10_7', 'benchJei', "However, our goal is not to make literacy itself our only key difference.", None, 0),
    ('l10_8', 'benchJei', "Instead, we want to combine literacy learning with precise assessment, personalized learning, and progress tracking.", None, 0),
    ('l10_9', 'benchJei', "Through this approach, we aim to offer a different learning experience.", None, .2),
    ('l10_10', 'benchNext', "Our English team is continuing to study major U.S. literacy programs in more detail.", None, 0),
    ('l10_11', 'benchNext', "Based on this research, we are working to define the unique strengths of JEI English and prepare a more detailed product plan.", None, .3),
    # deck p.11 · SWOT
    ('l11_1', 'swotS', "We also conducted a SWOT analysis.", None, 0),
    ('l11_2', 'swotS', "First, JEI has several internal strengths.", None, 0),
    ('l11_3', 'swotS', "Our precise assessment system allows us to provide personalized learning roadmaps.", None, 0),
    ('l11_4', 'swotS', "Our learning content is based on JEI's educational philosophy and programmed learning approach.", None, 0),
    ('l11_5', 'swotS', "It follows a small-step and spiral learning structure.", None, 0),
    ('l11_6', 'swotS', "This structure helps students learn independently and work toward mastering each skill.", None, .2),
    ('l11_7', 'swotW', "However, one weakness is that parents may not clearly see changes or improvements in a short period.", None, 0),
    ('l11_8', 'swotW', "We need better measures and reports that help parents understand exactly what their children have improved.", None, .2),
    ('l11_9', 'swotO', "Looking at external opportunities, demand for literacy and personalized learning is growing.", None, 0),
    ('l11_10', 'swotO', "AI and digital education are also expanding.", None, 0),
    ('l11_11', 'swotO', "As a result, parents increasingly expect to see learning progress through clear data.", None, .2),
    ('l11_12', 'swotT', "At the same time, strong competitors with well-known brands remain a challenge.", None, 0),
    ('l11_13', 'swotT', "Competition based on price and convenience is another possible risk.", None, .2),
    ('l11_14', 'swotSum', "Based on this analysis, we want to strengthen JEI's position by connecting our assessment and learning system with literacy-focused learning, Adaptive personalization, and clear progress tracking.", None, .3),
    # deck p.12 · Ansoff Matrix
    ('l12_1', 'ansoff', "Based on the Ansoff Matrix, we believe product development should be our first priority.", None, 0),
    ('l12_2', 'ansoff', "We could focus on increasing sales of existing products through advertising and promotions.", None, 0),
    ('l12_3', 'ansoff', "While this may work in the short term, it does not address the need to strengthen our product competitiveness and attract new customers.", None, .2),
    ('l12_4', 'ansoffPD', "JEI already has a presence in key U.S. markets, so market development is not our immediate priority.", "J-E-I already has a presence in key U.S. markets, so market development is not our immediate priority.", 0),
    ('l12_5', 'ansoffPD', "Instead, we plan to build on our existing content, assessment, and learning systems to develop a new personalized literacy program.", None, 0),
    ('l12_6', 'ansoffPD', "This is not simply an update to our existing product, but a new approach to personalized learning.", None, .3),

    # deck p.13 · segmentation and target students
    ('l13_1', 'target', "Our new program will target students from Pre-K through Grade 9.", None, 0),
    ('l13_2', 'target', "For the first development and testing phase, we plan to focus on Grades 3 to 6.", None, .2),
    ('l13_3', 'targetWhy', "At this stage, students move from basic reading to deeper understanding, vocabulary, and written expression.", None, 0),
    ('l13_4', 'targetWhy', "Learning gaps also become clearer.", None, 0),
    ('l13_5', 'targetWhy', "We believe this is a good stage to test our precise assessment and personalized learning approach.", None, .3),
    # deck p.14 · positioning map
    ('l14_1', 'posMap', "We also developed a positioning map.", None, 0),
    ('l14_2', 'posMap', "We compared major competitors based on two factors: the level of assessment detail and how learning paths are adjusted.", None, .2),
    ('l14_3', 'posX', "The horizontal axis shows the difference between basic assessment and precise assessment.", None, 0),
    ('l14_4', 'posX', "Basic assessment identifies a student's starting point.", None, 0),
    ('l14_5', 'posX', "Precise assessment goes further by identifying the student's current level and specific areas that need improvement.", None, .2),
    ('l14_6', 'posY', "The vertical axis shows the difference between a fixed learning path and an Adaptive Learning path.", None, 0),
    ('l14_7', 'posY', "A fixed path follows a set learning order.", None, 0),
    ('l14_8', 'posY', "An Adaptive path changes based on each student's learning results.", None, .2),
    ('l14_9', 'posJei', "Currently, JEI English is in the fourth quadrant.", None, 0),
    ('l14_10', 'posJei', "We use assessment to identify strengths and learning needs in different skill areas.", None, 0),
    ('l14_11', 'posJei', "We also set personalized learning paths.", None, 0),
    ('l14_12', 'posJei', "However, students mainly continue learning through a fixed learning path.", None, .2),
    ('l14_13', 'posKumon', "Kumon is in the third quadrant.", None, 0),
    ('l14_14', 'posKumon', "It uses assessment to identify a suitable starting point.", None, 0),
    ('l14_15', 'posKumon', "Students then follow a set learning path, with adjustments to their pace and repeated practice.", None, .2),
    ('l14_16', 'posShift', "The education market is now moving one step further.", None, 0),
    ('l14_17', 'posShift', "It is no longer enough to simply identify a starting point or adjust each student's pace.", None, 0),
    ('l14_18', 'posShift', "It is becoming more important to understand each student's learning needs accurately and change what they learn next based on their results.", None, .2),
    ('l14_19', 'posMove', "Therefore, our goal is to move JEI English from the fourth quadrant to the first quadrant.", None, 0),
    ('l14_20', 'posMove', "We want to use precise assessment to identify each student's current level and learning needs.", None, 0),
    ('l14_21', 'posMove', "We will then continue to adjust personalized learning paths based on learning results.", None, 0),
    ('l14_22', 'posMove', "Finally, we want to clearly show how much each student has improved.", None, .2),
    ('l14_23', 'position', "This is what we mean by:", None, .1),
    ('l14_24', 'position', "Accurate Assessment, Clear Growth.", None, .2),
    ('l14_25', 'position', "We aim to make precise assessment, personalized Adaptive Learning, and clear progress tracking one connected learning experience.", None, 0),
    ('l14_26', 'position', "This will be the key position of the new JEI English program.", None, .3),
    # deck p.15 · customer journey and pain points
    ('l15_1', 'journey', "We reviewed the customer journey from first interest in JEI English to re-enrollment.", None, 0),
    ('l15_2', 'journey', "Parents need clear reasons to choose JEI, easy-to-understand assessment results, and personalized learning plans.", None, 0),
    ('l15_3', 'journey', "They also want to see their children's progress.", None, .2),
    ('l15_4', 'journeyFix', "We plan to improve consultation, learning roadmaps, and progress reports throughout the customer journey.", None, 0),
    ('l15_5', 'journeyFix', "Our goal is to make the value of JEI English clear at every stage.", None, .3),
    # deck p.16 · 4P strategy
    ('l16_1', 'fourP', "Our 4P strategy focuses on Product, Price, Place, and Promotion.", "Our four P strategy focuses on Product, Price, Place, and Promotion.", 0),
    ('l16_2', 'fourP', "For Product, we will provide personalized English and literacy learning based on precise assessment.", None, 0),
    ('l16_3', 'fourP', "For Price, we will consider the full learning value, including assessment, personalized learning, coaching, and progress tracking.", None, .2),
    ('l16_4', 'fourP2', "For Place, we will connect center learning with self-learning at home.", None, 0),
    ('l16_5', 'fourP2', "For Promotion, we will clearly show the learning journey from assessment to growth.", None, .3),

    # deck p.17 · product types and step-by-step development
    ('l17_1', 'step1', "We plan to develop our Personalized Blended Learning program in two steps.", None, 0),
    ('l17_2', 'step1', "In Step 1, we will provide personalized POD workbooks based on Adaptive Assessment results and connect them with existing JEI English workbooks.", "In Step 1, we will provide personalized P-O-D workbooks based on Adaptive Assessment results and connect them with existing JEI English workbooks.", .2),
    ('l17_3', 'step2', "In Step 2, we will introduce online learning.", None, 0),
    ('l17_4', 'step2', "Students will be able to choose online learning, POD workbooks, or both.", "Students will be able to choose online learning, P-O-D workbooks, or both.", 0),
    ('l17_5', 'step2', "We also plan to connect learning results and adjust each student's next learning path.", None, .3),
    # deck p.18 · AI for personalized learning
    ('l18_1', 'ai1', "We plan to use AI in four areas.", None, 0),
    ('l18_2', 'ai1', "First, an AI Tutor will provide hints and additional explanations during learning.", None, 0),
    ('l18_3', 'ai1', "Second, AI will help analyze answers, learning processes, and student progress.", None, .2),
    ('l18_4', 'ai2', "Third, we plan to scan POD worksheets and connect offline results with online learning data.", "Third, we plan to scan P-O-D worksheets and connect offline results with online learning data.", 0),
    ('l18_5', 'ai2', "Finally, we will use AI to support content development, with our researchers reviewing and improving the content.", None, 0),
    ('l18_6', 'ai2', "Our goal is to improve personalized learning and make content development more efficient.", None, .3),
    # deck p.19 · product development direction and next steps
    ('l19_1', 'direction', "Our goal is to develop a new JEI English program that builds literacy skills through precise assessment and personalized learning.", None, 0),
    ('l19_2', 'direction', "As we explained earlier, this is not simply about improving our existing English content.", None, 0),
    ('l19_3', 'direction', "The key is to bring literacy learning, precise assessment, personalized learning, and clear evidence of progress together in one program.", None, .2),
    ('l19_4', 'nextA', "To achieve this, we plan to design a program structure that can cover Pre-K through Grade 9.", None, 0),
    ('l19_5', 'nextA', "We will use precise assessment to identify each student's current level and areas that need improvement.", None, 0),
    ('l19_6', 'nextA', "Based on the results, we will provide a personalized learning path.", None, .2),
    ('l19_7', 'nextB', "We will also organize Vocabulary, Grammar, Phonics, Reading, and Writing into a structured literacy curriculum.", None, 0),
    ('l19_8', 'nextB', "This will help students develop skills in understanding, making inferences, making decisions, and expressing ideas.", None, 0),
    ('l19_9', 'nextB', "In addition, we plan to improve our learning reports.", None, 0),
    ('l19_10', 'nextB', "We want parents and students to easily understand and use information about learning progress and growth.", None, .2),
    ('l19_11', 'summary', "To summarize, our final direction is to develop a new program that builds literacy through precise assessment and personalized learning.", None, 0),
    ('l19_12', 'summary', "We also want to make learning results and progress clearly visible.", None, .3),
    # deck p.20 · CCSS and state standards
    ('l20_1', 'ccss', "To put our product strategy into practice, we first need to connect national and state education standards with our learning system and assessment.", None, 0),
    ('l20_2', 'ccss', "However, education standards vary across U.S. states.", None, 0),
    ('l20_3', 'ccss', "Among the 50 states, 39 use either modified versions of the CCSS or independently developed ELA standards.", "Among the 50 states, 39 use either modified versions of the C-C-S-S or independently developed E-L-A standards.", .2),
    ('l20_4', 'ccssPlan', "We reviewed ELA standards across all 50 U.S. states, including California, New Jersey, New York, Florida, and Texas.", "We reviewed E-L-A standards across all 50 U.S. states, including California, New Jersey, New York, Florida, and Texas.", 0),
    ('l20_5', 'ccssPlan', "Our plan is to build a common ELA and Literacy structure while reflecting each state's standards in assessment and personalized learning paths.", "Our plan is to build a common E-L-A and Literacy structure while reflecting each state's standards in assessment and personalized learning paths.", 0),
    ('l20_6', 'ccssPlan', "This will help us design assessments and learning paths that match local education standards.", None, .3),
    # deck p.21 · personalized learning experience
    ('l21_1', 'platform', "We are also considering how to turn this product strategy into an actual learning experience.", None, 0),
    ('l21_2', 'platform', "Students will select their program, country, state, and language.", None, 0),
    ('l21_3', 'platform', "Based on this information, they will take an online Adaptive Assessment that reflects local education standards and learning conditions.", None, .2),
    ('l21_4', 'platform2', "We will then use the assessment results to provide personalized learning.", None, 0),
    ('l21_5', 'platform2', "Students will be able to choose POD workbooks, online learning, or a combination of both, depending on their needs.", "Students will be able to choose P-O-D workbooks, online learning, or a combination of both, depending on their needs.", 0),
    ('l21_6', 'platform2', "In the long term, we aim to expand this into a global personalized learning platform.", None, .3),
    # deck p.22 · curriculum-based adaptive assessment and learning
    ('l22_1', 'three', "We plan to provide personalized learning through three main steps.", None, 0),
    ('l22_2', 'three', "First, we will set learning standards based on each student's country, state, and grade.", None, 0),
    ('l22_3', 'three', "Second, we will use Adaptive Assessment to identify the student's current level and learning needs.", None, 0),
    ('l22_4', 'three', "Third, we will design a personalized learning path and adjust it based on learning results.", None, .2),
    ('l22_5', 'adaptive', "This will lead to Adaptive Learning, where each student's next learning steps change based on their progress.", None, .4),
    ('l22_6', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l22_6'   # a soft ding just before this line (the thank-you); None for no ding

# tts takes pinned by hand (index = the _k in audio/tts_cache): the cloned female voice often stops mid last word inside the
# length the server gives it, so these were picked by the phonemes of the last word (wav2vec2 espeak), not by whisper.
# audio/voice_ref.wav ends right on the last "s" of "questions" (no pause), which seems to teach the clone to stop early; a ref
# cut 14.1–28.95 s (0.25 s of silence at the end) cut fewer endings in a test. l14_5 take 8 was read with that ref (16 takes with this one all cut)
# review 1 (2026-10-30 sheet): the reworded lines and l1_1 ("U.S." clipped at 0:08) were read as line + " Thank you." with the ref
# cut 14.1–28.95 s and cut in the pause before the extra sentence, so each ends with its natural fall (cache takes _6–_9, l1_1 _9–_12).
# Index = position in the sorted take list (l1_1: 2 = file _10)
# review 2 (2026-10-30 sheet, 2nd round): the reworded lines (l2_3, l8_11, l8_12–14) and the lines heard clipped (l2_8 "path",
# l7_2, l14_15, l18_3, l22_5) were read the same way. l8_11 take falls in pitch at the end (208 → 162 Hz); l18_3 take says
# "processes" with a short last vowel (-iz, not -eez); l8_14 reads JEI as J-E-I (as written it came out "J.I." / "JE")
# review 3: l22_5 take 3 rose at the end ("progress" 192 → 337 Hz, odd right before "Thank you."); take 12 falls 209 → 168 Hz.
# l9_12 reworded (communicated → shown), read the same way; take 3 falls on "parents" (195 → 162 Hz)
TAKE = {'l1_1': 2, 'l3_2': 1, 'l4_6': 2, 'l8_9': 4, 'l11_7': 2, 'l14_9': 0, 'l14_12': 2, 'l14_19': 0, 'l17_5': 0, 'l18_4': 7, 'l2_1': 9, 'l2_2': 6, 'l4_3': 8, 'l9_14': 8, 'l10_8': 9, 'l11_3': 8, 'l14_3': 6, 'l14_5': 7, 'l14_20': 9, 'l14_25': 7, 'l19_1': 9, 'l19_3': 9, 'l19_5': 7, 'l19_11': 6, 'l20_3': 6,
        'l2_3': 4, 'l2_8': 3, 'l7_2': 11, 'l8_11': 4, 'l8_12': 1, 'l8_13': 4, 'l8_14': 0, 'l14_15': 5, 'l18_3': 4, 'l22_5': 12, 'l9_12': 3}
