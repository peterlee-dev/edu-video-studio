# The script: what is said on which page. Edit this file, then run tools/make_audio.py (dry | tts | take).
# Korean version of ../adaptive-diagnosis-v2 (same 12 pages, same line ids l1–l31 so index.html keys to the same lines).
# Two Korean sentences cover two English lines each; they are split at their comma into l15 / l16 and l27 / l28, words unchanged.
LANGUAGE = 'Korean'   # TTS and whisper language ('English' or 'Korean')

# (id, label). id = index.html SC.<id>; pages appear in this order, the label shows in the video editor
SCENES = [('intro', '제목'), ('what', '진단평가란'), ('problem', '현재의 고민'), ('adaptive', 'Adaptive 진단평가'),
          ('necessary', '필요한 문항만'), ('benefit', '좋아지는 점'), ('how', '작동 원리'), ('path', '문항 예시'),
          ('validate', '신뢰도 장치'), ('quick', '간편진단'), ('effects', '기대 효과'), ('outro', '감사합니다')]
# scenes that continue the page before on the same sheet: no page turn and no whoosh (index.html SHARED draws the part that stays)
CONT = set()

A = '어댑티브'   # read form of "Adaptive"
# (id, scene, line as written (screen · subtitles), line as read (None = as written), extra pause after it in s)
SCRIPT = [
    ('l1', 'intro', '안녕하세요. 오늘은 현재 개발 중인 재능스스로수학 온라인 Adaptive 진단평가의 기획 방향과 기대 효과를 말씀드리겠습니다.',
     f'안녕하세요. 오늘은 현재 개발 중인 재능스스로수학 온라인 {A} 진단평가의 기획 방향과 기대 효과를 말씀드리겠습니다.', .6),
    ('l2', 'what', '먼저 현재의 진단평가가 가진 고민부터 말씀드리겠습니다.', None, .2),
    ('l3', 'what', '진단평가는 학습을 시작하기 전, 학습자의 수준을 파악해서 개인별 맞춤 프로그램을 처방하기 위한 평가입니다.', None, .4),
    ('l4', 'problem', '현재는 모든 학습자가 동일한 문항을 다 풀어야만 정확한 진단이 가능합니다.', None, .2),
    ('l5', 'problem', '물론 많은 문항을 풀어 정확도를 높이려는 취지이지만, 그만큼 아이들이 느끼는 부담이 컸습니다.', None, .2),
    ('l6', 'problem', '결과적으로는 정작 아이의 진짜 학습 출발점을 파악하는 효율성이 떨어질 수밖에 없었습니다.', None, .4),
    ('l7', 'adaptive', '이 문제를 해결하기 위해 저희는 Adaptive 진단평가를 준비하고 있습니다.', f'이 문제를 해결하기 위해 저희는 {A} 진단평가를 준비하고 있습니다.', .2),
    ('l8', 'adaptive', '하나의 학습목표마다 정답과 오답에 따라 다음 문항이 실시간으로 조정되는, 반응형 정밀진단 체계입니다.', None, .4),
    ('l9', 'necessary', '핵심은 모든 문항을 푸는 것이 아니라 학습자의 응답에 따라 필요한 문항만 실시간으로 제시하는 것입니다.', None, .4),
    ('l10', 'benefit', '이 체계는 진단의 효율성과 신뢰도를 높이고 평가에 걸리는 시간도 줄여줍니다.', None, .2),
    ('l11', 'benefit', '정리하면, 진단 부담은 줄이면서도, 학습 출발점을 정확히 찾아내는 목적은 그대로 유지하는 평가 시스템입니다.', None, .4),
    ('l12', 'how', '그럼 Adaptive 진단평가는 실제로 어떻게 작동할까요?', f'그럼 {A} 진단평가는 실제로 어떻게 작동할까요?', .3),
    ('l13', 'how', '문항을 하나 제시했을 때, 맞히면 더 높은 난도의 문항을, 틀리면 부족한 개념을 확인하는 하위 문항을 제공합니다.',
     '문항을 하나 제시했을 때, 마치면 더 높은 난도의 문항을, 틀리면 부족한 개념을 확인하는 하위 문항을 제공합니다.', .4),   # 맞히면 [마치면]: read as written it came out 맞추면
    ('l14', 'path', '예를 들어 1번부터 9번까지 모든 문항을 순서대로 풀게 하는 대신, 핵심이 되는 대표 문항부터 먼저 제시합니다.',
     '예를 들어 일 번부터 구 번까지 모든 문항을 순서대로 풀게 하는 대신, 핵심이 되는 대표 문항부터 먼저 제시합니다.', .2),
    ('l15', 'path', '이 문항을 틀리면 하위 개념인 3번, 1번 순으로 내려가며 결손 지점을 추적하고,',
     '이 문항을 틀리면 하위 개념인 삼 번, 일 번 순으로 내려가며 결손 지점을 추적하고,', .3),
    ('l16', 'path', '반대로 맞히면 7번, 9번으로 올라가며 어디까지 알고 있는지 확인합니다.', '반대로 맞히면 칠 번, 구 번으로 올라가며 어디까지 알고 있는지 확인합니다.', .3),
    ('l17', 'path', '이런 방식으로 문항 수는 최소화하면서도, 아이의 실제 실력 위치는 정확하게 짚어낼 수 있습니다.', None, .4),
    ('l18', 'validate', '다만 문항 수가 줄어드는 만큼, 평가의 신뢰도를 지키는 장치도 마련했습니다.', None, .2),
    ('l19', 'validate', '등급별 최종학습목표, 즉 가장 핵심이 되는 대표문항에 대해서는 2개의 유사 문항을 추가로 준비해서 평가할 수 있도록 했습니다.',
     '등급별 최종학습목표, 즉 가장 핵심이 되는 대표문항에 대해서는 두 개의 유사 문항을 추가로 준비해서 평가할 수 있도록 했습니다.', .3),
    ('l20', 'validate', "세 문항 중 두 문항을 맞히면 '안다'로, 그렇지 않으면 '모른다'로 판정합니다.", '세 문항 중 두 문항을 맞히면 안다로, 그렇지 않으면 모른다로 판정합니다.', .3),
    ('l21', 'validate', '문항 수는 줄이되, 판정의 신뢰도는 잃지 않으려는 장치입니다.', None, .4),
    ('l22', 'quick', "현장에서 더 빠르게 활용하실 수 있도록 '간편진단'도 함께 준비했습니다.", '현장에서 더 빠르게 활용하실 수 있도록 간편진단도 함께 준비했습니다.', .2),
    ('l23', 'quick', '간편진단은 수학의 기초가 되는 수와 연산 영역을 우선적으로 진단하고, 그 결과를 간편 리포트로 바로 확인할 수 있습니다.', None, .2),
    ('l24', 'quick', '이 리포트로 전체 진단이 끝나기 전에 수와 연산에서 아는 정도와 다음 학습 방향 등을 상담하실 수 있습니다.', None, .4),
    ('l25', 'effects', '그럼 Adaptive 진단평가가 실제로 어떤 도움이 될지 말씀드리겠습니다.', f'그럼 {A} 진단평가가 실제로 어떤 도움이 될지 말씀드리겠습니다.', .2),
    ('l26', 'effects', "현재 진단평가의 페인포인트였던 '과도한 문항 수' 문제를 해결합니다.", '현재 진단평가의 페인포인트였던 과도한 문항 수 문제를 해결합니다.', .2),
    ('l27', 'effects', '회원과 선생님 모두 진단에 드는 부담이 줄어들고,', None, .1),
    ('l28', 'effects', '그만큼 상담과 수업 운영 효율이 높아질 것으로 기대합니다.', None, .2),
    ('l29', 'effects', 'Adaptive 진단평가는 재능스스로수학에 우선 적용하지만, 이후 다른 과목으로도 확장할 수 있다고 보고 있습니다.',
     f'{A} 진단평가는 재능스스로수학에 우선 적용하지만, 이후 다른 과목으로도 확장할 수 있다고 보고 있습니다.', .5),
    ('l30', 'outro', '지금까지 Adaptive 진단평가 소개를 마치겠습니다.', f'지금까지 {A} 진단평가 소개를 마치겠습니다.', .3),
    ('l31', 'outro', '감사합니다.', None, 0),
]

# take mode only: lines reworded after the recording. They are read by a clone of the recorded voice (audio/voice_ref.wav)
# instead of being cut from the recording
CLONE = set()

LEAD, GAP, SCENE_GAP, TAIL = 2.6, .45, 1.0, 2.4   # s before the first line, between lines, extra between pages, after the last line
DING_BEFORE = 'l31'   # a soft ding just before this line (the thank-you); None for no ding
