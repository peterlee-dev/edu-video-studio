// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneEnd = (id, d = 1) => { const s = TL.scenes.find(x => x.id === id); return s ? s.end - d : 0; };
const secFields = id => [{ path: `sections.${id}.0`, label: '섹션 태그', type: 'text' }, { path: `sections.${id}.1`, label: '제목', type: 'text' }];
window.SCHEMA = {
 id: 'learning-plan-graph',          // same as the folder name
 title: '맞춤 학습 계획 그래프 안내',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: '문구' }, { id: 'color', label: '색' }],
 groups: [
  { tab: 'text', title: '표지', at: 4, fields: [
   { path: 'title.kicker', label: '머리 칩', type: 'text' }, { path: 'title.words.0', label: '제목 1줄 (레드)', type: 'text' }, { path: 'title.words.1', label: '제목 2줄', type: 'text' },
   { path: 'title.sub', label: '부제', type: 'text' }, { path: 'title.team', label: '팀 (손글씨)', type: 'text' }] },
  { tab: 'text', title: '맞춤 학습 계획', at: sceneEnd('intro'), fields: [{ path: 'intro.tag', label: '섹션 태그', type: 'text' }, { path: 'intro.title', label: '제목', type: 'text' },
   { path: 'intro.head', label: '기록부 영역 이름', type: 'text' }, { path: 'intro.caps.0', label: '아래 문구 1', type: 'text' }, { path: 'intro.caps.1', label: '아래 문구 2', type: 'text' }] },
  { tab: 'text', title: '예시 학생', at: sceneEnd('example'), fields: [{ path: 'example.tag', label: '섹션 태그', type: 'text' }, { path: 'example.title', label: '제목', type: 'text' },
   { path: 'example.head', label: '패널 머리', type: 'text' }, { path: 'example.exam.1', label: '실시 진단평가', type: 'text' },
   { path: 'example.plan.1', label: '처방 1', type: 'text' }, { path: 'example.plan.2', label: '처방 2', type: 'text' }, { path: 'example.plan.3', label: '처방 합계 (레드)', type: 'text' },
   { path: 'example.final.1', label: '학습 완료 후 평가', type: 'text' }] },
  ...['structure', 'path', 'standard', 'start', 'cross', 'read', 'outro'].map(id => ({ tab: 'text', title: TL.scenes.find(s => s.id === id)?.label || id, at: sceneEnd(id), fields: secFields(id) })),
  { tab: 'text', title: '그래프 글자', at: sceneEnd('outro', 2), fields: [
   { path: 'graph.yTitle', label: '세로축 이름', type: 'text' }, { path: 'graph.top', label: '맨 위 (평가)', type: 'text' }, { path: 'graph.grade', label: '실시 등급', type: 'text' },
   { path: 'graph.age', label: '연령 · 학년 (학교진도)', type: 'text' }, { path: 'graph.prev', label: '이전 등급', type: 'text' }, { path: 'graph.xTitle', label: '가로축 이름', type: 'text' },
   { path: 'graph.set', label: '학습출발점 세트', type: 'text' }, { path: 'graph.legend.0', label: '범례 1', type: 'text' }, { path: 'graph.legend.1', label: '범례 2', type: 'text' }, { path: 'graph.legend.2', label: '범례 3', type: 'text' }] },
  { tab: 'text', title: '기록부 안내 문구', at: sceneEnd('read'), fields: [0, 1, 2, 3].map(i => ({ path: `note.${i}`, label: `${i + 1}문단`, desc: '{ } 로 감싼 말은 굵게 (안내 문구 쪽의 연결선이 이 말을 찾아요)', type: 'text' })).concat([{ path: 'read.bar', label: '맺음 띠', desc: '{ } 로 감싼 말은 조금 크게', type: 'text' }]) },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — section tags · pen · marks', 20), col('colors.navy', 'Navy — ✗ (학교 학년)', 60), col('colors.ink', 'Text · dark bar', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Graph colours (the record\'s)', fields: [col('colors.gBlue', '학생의 처방 학습 경로 (파란 실선)', sceneEnd('outro', 2)), col('colors.gOrange', '표준 학습 경로 (주황 점선)', sceneEnd('outro', 2)),
   col('colors.gPurple', '학습출발점 (보라 점)', sceneEnd('outro', 2)), col('colors.gBandTop', '실시 등급 배경', sceneEnd('outro', 2)), col('colors.gBandLow', '이전 등급 배경', sceneEnd('outro', 2)),
   col('colors.gAxis', '축', sceneEnd('outro', 2)), col('colors.gLabel', '축 글자', sceneEnd('outro', 2)), col('colors.gNote', '안내 문구 상자', sceneEnd('read'))] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.blush', 'Blush (highlighter)', sceneEnd('read')), col('colors.lightRed', 'Light red (blink)', sceneEnd('path')), col('colors.muted', 'Slate (secondary text)', 20),
   col('colors.lightBox', 'Light box (chips)', 60), col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration: Qwen3-TTS reading tools/script.py in the voice of audio/voice_ref.wav (Korean female, as ../jei-ai-vision-ko and ../adaptive-diagnosis-v2-ko), timed by tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
