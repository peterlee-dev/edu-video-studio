// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
const sceneEnd = (id, d = 1) => { const s = TL.scenes.find(x => x.id === id); return s ? s.end - d : 0; };
const barField = (id, label, note = '') => ({ tab: 'text', title: label, at: sceneEnd(id), fields: [{ path: `${id}.bar`, label: '맺음 띠', desc: note, type: 'text' }] });
// the pink "strength" box under the comparison pages: {words} get the highlighter
const strengthField = (id, label, n) => ({ tab: 'text', title: label, at: sceneEnd(id), fields: [...Array(n)].map((_, i) => ({ path: `${id}.strength.${i}`, label: `강점 상자 ${i + 1}줄`, desc: '{ } 로 감싼 말에 형광펜', type: 'text' })) });
window.SCHEMA = {
 id: 'jei-math-difference-ko',          // same as the folder name
 title: '재능스스로수학, 차이를 만드는 세 가지 경쟁력',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: '문구' }, { id: 'color', label: '색' }],
 groups: [
  { tab: 'text', title: '표지', at: 4, fields: [
   { path: 'title.kicker', label: '머리 칩', type: 'text' }, { path: 'title.words.0', label: '제목 1줄', type: 'text' }, { path: 'title.words.1', label: '제목 2줄', type: 'text' }, { path: 'title.words.2', label: '제목 3줄', type: 'text' },
   { path: 'title.sub', label: '부제', type: 'text' }] },
  barField('intro', '무엇이 다를까요', '{ } 로 감싼 말은 조금 크게'), { tab: 'text', title: '강점 상자 칩', at: sceneEnd('addition'), fields: [{ path: 'strength', label: '칩 문구', type: 'text' }] },
  { tab: 'text', title: '② 덧셈 · Eye Level 순서', at: sceneEnd('addition'), fields: [{ path: 'addition.order', label: 'Eye Level 아래 손글씨', type: 'text' }] },
  strengthField('addition', '② 덧셈', 2), strengthField('division', '② 나눗셈', 2),
  barField('systems', '③ 학습목표 · 세 가지 분석'), barField('wrong', '③ 오답 원인'), barField('learners', '③ 두 학습자'), barField('summary', '정리'),
  { tab: 'text', title: '마무리', at: sceneEnd('outro', 2), fields: [
   { path: 'outro.kicker', label: '머리 칩', type: 'text' }, { path: 'outro.lines.0', label: '1줄', type: 'text' }, { path: 'outro.lines.1', label: '2줄', type: 'text' },
   { path: 'outro.sub', label: '부제', type: 'text' }, { path: 'outro.key', label: '핵심 문구 (레드)', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · positive · 1st of a comparison · pen', 20), col('colors.blue', 'Blue — 2nd of a comparison (Eye Level Math · 구몬 · 학습자 B)', sceneEnd('addition')), col('colors.mint', 'Mint — 3rd', sceneEnd('pillars')),
   col('colors.navy', 'Navy — negative · wrong answer', sceneEnd('wrong')), col('colors.ink', 'Text', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.mintDark', 'Mint dark (white-text circles)', sceneEnd('summary')), col('colors.crimson', 'Crimson (small red text)', sceneEnd('wrong')), col('colors.lightRed', 'Light red', 20),
   col('colors.blush', 'Blush (highlighter)', 5), col('colors.redTint', 'Red tint (red chip · box)', sceneEnd('systems')), col('colors.navyTint', 'Navy tint', 20), col('colors.blueTint', 'Blue tint', sceneEnd('learners')), col('colors.mintTint', 'Mint tint', 20),
   col('colors.muted', 'Slate (secondary text)', 20), col('colors.midGrey', 'Mid grey', 20), col('colors.lineGrey', 'Line grey (tape · outlines)', sceneEnd('areas')), col('colors.lightBox', 'Light box (secondary boxes · sticky notes)', sceneEnd('kumon')),
   col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration: Qwen3-TTS reading tools/script.py in the voice of audio/voice_ref.wav (as ../jei-ai-vision-ko), timed by tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
