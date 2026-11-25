# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Source: <the deck / script this video is made from, and its date>
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', 'Title'), ('problem', 'The problem today'), ('steps', 'Three steps'), ('outro', 'Closing')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes.
# Korean: numbers and English names in the read form the Korean way ("7개" → "일곱 개", "D등급" → "디등급"), or use SAY below
SCRIPT = [
    ('l1_1', 'title', "Hello. Today, I'd like to introduce a faster way to find each learner's starting point.", None, .3),
    ('l2_1', 'problem', "Currently, every learner answers the same 91 questions.", None, .2),
    ('l2_2', 'problem', "More questions help accuracy, but they add to the burden, and efficiency drops.", None, 0),
    ('l3_1', 'steps', "The new approach works in three steps: assess, diagnose, and prescribe.", None, .2),
    ('l3_2', 'steps', "Each step builds on the one before it.", None, 0),
    ('l4_1', 'outro', "Thank you.", None, 0),
]

# [(written, read)]: applied by make_audio.py to whisper's transcripts too, so a take that said the read form still counts as word for word.
# To read them, also put them in the read forms (a helper like R(s) that applies SAY to each line keeps it in one place)
SAY = []

# tts mode: the reference voice is audio/<VOICE>.wav + .txt (VOICE=… on the command line tries another without editing this)
VOICE = 'voice_ref'
# tts mode: a take chosen by ear or by tools/voice_check.py, instead of the automatic pick ({line id: position in the sorted takes})
TAKE = {}
# tts mode: the pace (chars/s) takes are picked against. None = the median of all takes. Once a version has been delivered, pin it to the
# value make_audio printed, so re-reading one line with N=8 does not move every other line's pick (and the timeline with it)
PACE = None

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
JOIN = {}               # {line id: s}: the sentence goes on from the line before into a CONT scene after only this short pause
TEMPO = 1.              # tts mode: 1 = as read. Only change it when asked (more breathing room = commas in the read form, longer GAP)
CHIME_AT = None         # a bright chime at this time on the title page; None for none
DING_BEFORE = 'l4_1'    # the same chime just before this line (the thank-you); None for none
DING_END = False        # and after the last line
