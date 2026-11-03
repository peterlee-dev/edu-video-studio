// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
window.SCHEMA = {
 id: 'jei-english-us-plan',          // same as the folder name
 title: 'JEI English 미주 신상품 기획(안) (모눈종이 워크북)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Title', at: 5, fields: [
   { path: 'title.kicker', label: 'Kicker', type: 'text' }, { path: 'title.words.0', label: 'Title line 1', type: 'text' }, { path: 'title.words.1', label: 'Title line 2', type: 'text' }, { path: 'title.words.2', label: 'Title line 3', type: 'text' },
   { path: 'title.sub', label: 'Subtitle', type: 'text' }, { path: 'title.team', label: 'Team (handwriting)', type: 'text' }] },
  { tab: 'text', title: 'Closing', at: sceneAt('outro', 4), fields: [
   { path: 'outro.title', label: 'Title', type: 'text' }, { path: 'outro.points.0', label: 'Point 1', type: 'text' }, { path: 'outro.points.1', label: 'Point 2', type: 'text' }, { path: 'outro.points.2', label: 'Point 3', type: 'text' }, { path: 'outro.thanks', label: 'Thank you', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · positive · 1st of a comparison · pen', 20), col('colors.blue', 'Blue — 2nd of a comparison', sceneAt('week')), col('colors.mint', 'Mint — 3rd · to check', sceneAt('genre', 8)),
   col('colors.navy', 'Navy — negative · wrong · down', sceneAt('naep', 8)), col('colors.ink', 'Text', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.mintDark', 'Mint dark (mint text · white-text chips)', sceneAt('genre', 8)), col('colors.crimson', 'Crimson (small red text)', 20), col('colors.lightRed', 'Light red (secondary rise)', sceneAt('naep', 8)),
   col('colors.blush', 'Blush (highlighter)', 5), col('colors.redTint', 'Red tint (red chip · track)', 20), col('colors.navyTint', 'Navy tint', 20), col('colors.blueTint', 'Blue tint (blue track)', sceneAt('week')), col('colors.mintTint', 'Mint tint', 20),
   col('colors.muted', 'Slate (secondary text)', 20), col('colors.midGrey', 'Mid grey (the rest)', 20), col('colors.lineGrey', 'Line grey (dashed · secondary lines)', 20), col('colors.lightBox', 'Light box (secondary boxes)', 20),
   col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration and timing come from tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
