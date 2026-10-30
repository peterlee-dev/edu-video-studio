# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
LANGUAGE = 'English'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('title', 'Title'), ('problem', 'The problem today'), ('steps', 'Three steps'), ('outro', 'Closing')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s). Line ids: l<section>_<n>
# Write the read form only where the voice would stumble: acronyms read letter by letter ("JEI-SLI" → "J-E-I S-L-I"), years, codes
SCRIPT = [
    ('l1_1', 'title', "Hello. Today, I'd like to introduce a faster way to find each learner's starting point.", None, .3),
    ('l2_1', 'problem', "Currently, every learner answers the same 91 questions.", None, .2),
    ('l2_2', 'problem', "More questions help accuracy, but they add to the burden, and efficiency drops.", None, 0),
    ('l3_1', 'steps', "The new approach works in three steps: assess, diagnose, and prescribe.", None, .2),
    ('l3_2', 'steps', "Each step builds on the one before it.", None, 0),
    ('l4_1', 'outro', "Thank you.", None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l4_1'   # a soft ding just before this line (the thank-you); None for no ding
