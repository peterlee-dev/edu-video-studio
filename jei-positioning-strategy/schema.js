// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
window.SCHEMA = {
 id: 'jei-positioning-strategy',   // same as the folder name
 title: 'JEI Positioning & Execution Strategy · 재능교육 포지셔닝 및 실행전략 (영문, 여자 목소리)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Title', at: 5, fields: [
   { path: 'title.kicker', label: 'Kicker', type: 'text' }, { path: 'title.words.0', label: 'Title line 1', type: 'text' }, { path: 'title.words.1', label: 'Title line 2', type: 'text' }, { path: 'title.words.2', label: 'Title line 3', type: 'text' },
   { path: 'title.sub', label: 'Subtitle', type: 'text' }] },
  { tab: 'text', title: 'Closing', at: sceneAt('outro', 8), fields: [
   { path: 'outro.lead', label: 'Title', type: 'text' }, { path: 'outro.quote.0', label: 'Quote line 1', type: 'text' }, { path: 'outro.quote.1', label: 'Quote line 2', type: 'text' },
   { path: 'outro.quote.2', label: 'Quote line 3 (red)', type: 'text' }, { path: 'outro.quote.3', label: 'Quote line 4', type: 'text' }, { path: 'outro.site', label: 'Website (handwriting)', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · positive · 1st of a comparison · pen', 20), col('colors.blue', 'Blue — 2nd of a comparison', sceneAt('targets', 6)), col('colors.mint', 'Mint — 3rd · to check', sceneAt('targets', 6)),
   col('colors.navy', 'Navy — negative · wrong · down', sceneAt('failed', 12)), col('colors.ink', 'Text', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.mintDark', 'Mint dark (mint text · white-text chips)', sceneAt('targets', 6)), col('colors.crimson', 'Crimson (small red text)', 20), col('colors.lightRed', 'Light red (secondary rise)', sceneAt('failed', 12)),
   col('colors.blush', 'Blush (highlighter)', 5), col('colors.redTint', 'Red tint (red chip · track)', 20), col('colors.navyTint', 'Navy tint', 20), col('colors.blueTint', 'Blue tint (blue track)', sceneAt('targets', 6)), col('colors.mintTint', 'Mint tint', 20),
   col('colors.muted', 'Slate (secondary text)', 20), col('colors.midGrey', 'Mid grey (the rest)', 20), col('colors.lineGrey', 'Line grey (dashed · secondary lines)', 20), col('colors.lightBox', 'Light box (secondary boxes)', 20),
   col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration and timing come from tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
