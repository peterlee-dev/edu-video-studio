# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: the English script of ../jei-math-difference-ko (18 scenes, received 2026-11-06), word for word. The pages are the Korean
# version's 18 pages (ver6) with English text. Line ids: l<scene>_<n>.
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', 'Opening'), ('intro', 'Introduction'), ('pillars', 'Three Key Advantages'),
          ('t1', 'Transition: Learning Content'), ('kumon', '① Program A'), ('areas', '① JEI Math · five areas'),
          ('t2', 'Transition: Learning Progression'), ('addition', '② Addition: JEI Math vs. Program B'), ('division', '② Division: JEI Math vs. Program B'),
          ('t3', 'Transition: Diagnosis and Prescription'), ('tests', '③ Program A and Program B'), ('systems', "③ JEI Math's Diagnostic System"),
          ('objective', '③ System I: Analysis by Objectives'), ('function', '③ System II: Analysis by Learning Functions'),
          ('wrong', '③ System IV: Analysis by Answer Selection'), ('learners', '③ Personalized Learning Prescriptions'),
          ('summary', 'Three Strengths, One Integrated System'), ('outro', 'Closing')]
# scenes that continue the page before on the same sheet: no page turn (index.html SHARED draws the part that stays)
CONT = set()
WHOOSH = False   # no whoosh at page turns (수정사항 2026.11.06: 쉭 효과음 빼기)

# read forms (the screen and subtitles keep the written form). make_audio.py also applies SAY to whisper's transcripts.
# JEI letter by letter (left alone the clone may read it as one word, ../jei-ai-vision review 2026-11-05), numbers in words
SAY = [('JEI', 'J-E-I'), ('2,619', 'two thousand six hundred nineteen'), ('67 plus 18', 'sixty-seven plus eighteen'),
       ('75 may', 'seventy-five may'), ('86 may', 'eighty-six may'), ('715 may', 'seven hundred fifteen may')]
def R(s):
    for a, b in SAY:
        s = s.replace(a, b)
    return s

# (id, scene, line as written (screen · subtitles), extra pause after it in s)
_SCRIPT = [
    ('l1_1', 'title', 'What makes JEI Math different from other math learning programs?', .1),
    ('l1_2', 'title', "Let's explore three key strengths of JEI Math: comprehensive mathematical content, systematic learning progression, and precise diagnosis and personalized prescriptions.", 0),

    ('l2_1', 'intro', "What makes a difference in math learning isn't simply how many problems students solve.", 0),
    ('l2_2', 'intro', 'What truly matters is what students learn, how they learn, and how their individual learning levels and needs are assessed.', 0),

    ('l3_1', 'pillars', 'JEI Math stands out in three key ways.', .1),
    ('l3_2', 'pillars', 'First, it covers all five major areas of mathematics, going beyond arithmetic.', 0),
    ('l3_3', 'pillars', 'Second, it provides a systematic learning progression, from understanding mathematical concepts and principles to applying them and developing mastery.', 0),
    ('l3_4', 'pillars', 'Third, it analyzes learning gaps and possible causes of errors from multiple perspectives to provide precise diagnosis and personalized learning prescriptions.', 0),

    ('l4_1', 't1', 'The first difference lies in the range of mathematical content.', 0),

    ('l5_1', 'kumon', 'Program A primarily focuses on numbers and operations, from basic arithmetic with whole numbers to calculations involving fractions and decimals.', 0),
    ('l5_2', 'kumon', 'Through repeated practice, from basic to more complex calculations, it emphasizes improving computational accuracy and speed.', .1),
    ('l5_3', 'kumon', 'While this approach helps students develop computational fluency, its emphasis on numbers and operations provides less exposure to other areas of mathematics, limiting opportunities to build broader mathematical connections and problem-solving skills.', 0),

    ('l6_1', 'areas', 'In contrast, JEI Math goes beyond arithmetic to cover all five major areas of mathematics: numbers and operations, geometry, measurement, data and graphs, and patterns.', .1),
    ('l6_2', 'areas', 'Students gradually learn the key concepts and principles in each area and apply them to a variety of problems, broadening their mathematical understanding.', 0),
    ('l6_3', 'areas', 'This comprehensive approach helps students develop not only computational skills but also logical thinking, the ability to recognize mathematical relationships, and well-rounded mathematical problem-solving skills.', 0),

    ('l7_1', 't2', 'The second difference lies in how mathematical concepts are taught and developed.', 0),

    ('l8_1', 'addition', "Let's first compare how addition is introduced.", 0),
    ('l8_2', 'addition', 'Rather than starting with numerical equations, JEI Math introduces addition through concrete situations and a variety of activities that help students naturally understand its meaning and principles.', 0),
    ('l8_3', 'addition', 'Students begin by counting and combining objects, then gradually connect these experiences to addition equations.', .1),
    ('l8_4', 'addition', 'In contrast, the program B materials reviewed introduce addition equations first, followed by activities using concrete objects to explore the meaning of addition.', .1),
    ('l8_5', 'addition', 'This sequence places greater emphasis on calculation procedures before students have fully explored the meaning of addition.', .1),
    ('l8_6', 'addition', 'JEI Math, on the other hand, builds conceptual understanding through concrete experiences before progressing to mathematical expressions and calculations, helping students develop the ability to understand and apply mathematics independently.', 0),

    ('l9_1', 'division', 'A similar difference can be seen in division.', 0),
    ('l9_2', 'division', 'JEI Math helps students understand the principles of division through multiple approaches, including grouping objects, skip-counting on a number line, and repeated subtraction.', 0),
    ('l9_3', 'division', 'Through these activities, students discover how different representations connect to the same mathematical principle.', .1),
    ('l9_4', 'division', 'In the program B materials reviewed, greater emphasis is placed on learning calculation procedures and practicing similar types of problems after introducing the principles of division.', .1),
    ('l9_5', 'division', 'This systematic progression, from understanding mathematical principles through multiple approaches to application and mastery, is the second key advantage of JEI Math.', 0),

    ('l10_1', 't3', 'The third and final difference lies in the Diagnosis and Prescription System.', 0),

    ('l11_1', 'tests', "Math learning programs differ in how they assess students' abilities and determine their starting points.", .1),
    ('l11_2', 'tests', 'Program A uses test completion time and the number of correct answers to identify a recommended starting point based on a reference graph.', 0),
    ('l11_3', 'tests', "The instructor then considers their observations and judgment to determine the student's actual starting point.", .1),
    ('l11_4', 'tests', "Meanwhile, program B determines each student's starting level based on which questions they answer incorrectly, regardless of how long they take to complete the test.", 0),

    ('l12_1', 'systems', 'In contrast, JEI Math analyzes assessment results from three perspectives: Analysis by Objectives, Analysis by Learning Functions, and Analysis by Answer Selection.', .1),
    ('l12_2', 'systems', 'Rather than simply identifying correct and incorrect answers, the system examines which learning objectives students have not mastered, which learning functions need improvement, and the possible reasons behind their errors.', .1),
    ('l12_3', 'systems', 'Built around 2,619 detailed learning objectives, the system uses these results to determine what each student needs to learn and how much practice they need.', .2),
    ('l12_4', 'systems', 'By combining systematic learning design with precise diagnosis and personalized prescriptions, JEI Math provides targeted learning tailored to each student\'s needs.', 0),
    ('l12_5', 'systems', 'This is the third key advantage of JEI Math.', 0),

    ('l13_1', 'objective', "JEI Math identifies students' learning gaps through both Analysis by Objectives and Analysis by Learning Functions.", .1),
    ('l13_2', 'objective', 'The first, Analysis by Objectives, groups related assessment questions according to their learning objectives and analyzes the results.', 0),
    ('l13_3', 'objective', "When a learning gap is identified in a particular area, the system selects the appropriate Prescribed Workbooks to address that gap, providing targeted learning based on each student's needs.", 0),

    ('l14_1', 'function', 'The second is Analysis by Learning Functions.', 0),
    ('l14_2', 'function', 'This system groups learning objectives associated with the same learning function and analyzes the assessment results.', 0),
    ('l14_3', 'function', 'When a gap is identified in a particular learning function, the system selects Prescribed Workbooks designed to strengthen that function.', .1),
    ('l14_4', 'function', 'This helps identify which learning functions students are struggling with and provides focused practice to address those specific gaps.', 0),

    ('l15_1', 'wrong', 'Next is Analysis by Answer Selection.', 0),
    ('l15_2', 'wrong', 'Even when students answer the same problem incorrectly, the reasons behind their errors may be different.', .1),
    ('l15_3', 'wrong', 'For example, in the addition problem 67 plus 18, choosing 75 may indicate difficulty with regrouping.', 0),
    ('l15_4', 'wrong', 'Choosing 86 may suggest an error in basic addition, while choosing 715 may indicate a misunderstanding of place value.', .1),
    ('l15_5', 'wrong', 'By analyzing the incorrect answer selected, JEI Math identifies possible causes of errors and prescribes workbooks to address the underlying learning gaps.', 0),
    ('l15_6', 'wrong', 'Instead of simply having students repeat the problems they missed, the system focuses on addressing the reasons behind their mistakes.', 0),

    ('l16_1', 'learners', 'Even when two students make the same number of errors, their learning needs may be very different.', .1),
    ('l16_2', 'learners', 'For example, two students may each answer seven questions incorrectly.', 0),
    ('l16_3', 'learners', 'Yet one may struggle with two-digit addition, while the other has gaps in counting and basic arithmetic.', .1),
    ('l16_4', 'learners', 'JEI Math systematically analyzes these differences to determine the appropriate starting level for each student and select Prescribed Workbooks tailored to their individual needs.', 0),

    ('l17_1', 'summary', "We've explored the three key advantages of JEI Math.", .1),
    ('l17_2', 'summary', 'Comprehensive coverage of all five major areas of mathematics, systematic learning progression from conceptual understanding to application and mastery, and precise diagnosis and personalized prescriptions.', .2),
    ('l17_3', 'summary', "Together, these three strengths form an integrated learning system that supports each student's progress according to their individual abilities and needs.", 0),
    ('l17_4', 'summary', 'This is the core competitive advantage of JEI Math.', 0),

    ('l18_1', 'outro', 'JEI Math provides learning tailored to each student\'s abilities and needs, helping students progress toward complete mastery through personalized, ability-based learning.', 0),
]
READ = {}
# breaths: a comma after these words in the read form, so the voice pauses between phrases instead of running the words together
BREATH = {}
def breathe(lid, s):
    for w in BREATH.get(lid, []):
        assert w + ' ' in s, f'{lid}: no "{w} " to breathe after'
        s = s.replace(w + ' ', w + ', ', 1)
    return s
SCRIPT = [(lid, sc, s, READ.get(lid) or (lambda r: r if r != s else None)(R(breathe(lid, s))), x) for lid, sc, s, x in _SCRIPT]

# take mode only: lines reworded after the recording (none: this video is read by the TTS clone)
CLONE = set()
# tts mode: a take chosen by ear or by the phoneme / pitch check, instead of the automatic pick ({line id: index in the sorted takes})
TAKE = {}

# the same pacing as ../jei-math-difference-ko (a chime at the start, breaks between lines and pages). The voice keeps its own pace
PACE = 15.44   # the median pace of the takes before the 2026.11.06 rewording (Program A · B), pinned so the unchanged lines keep their takes
LEAD, GAP, SCENE_GAP, TAIL = 1.3, .6, 1.8, 3.2   # s before the first line, between lines, extra between pages, after the last line
# lines that finish the sentence of the line before on the next scene of the same sheet: only this pause (s) before them
JOIN = {}
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked
CHIME_AT = .25          # a bright chime at this time on the title page; None for none
DING_BEFORE = None      # the same chime just before this line; None for none
DING_END = True         # and after the last line (the script has no thank-you line)
