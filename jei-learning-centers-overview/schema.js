// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
window.SCHEMA = {
 id: 'jei-learning-centers-overview',   // same as the folder name
 title: 'Overview of JEI Learning Centers, LLC · 미주 재능 회사 소개 (남자 목소리, 모눈종이 워크북)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Title', at: 5, fields: [
   { path: 'title.kicker', label: 'Kicker', type: 'text' }, { path: 'title.words.0', label: 'Title line 1', type: 'text' }, { path: 'title.words.1', label: 'Title line 2', type: 'text' }, { path: 'title.words.2', label: 'Title line 3', type: 'text' },
   { path: 'title.sub', label: 'Subtitle', type: 'text' }, { path: 'title.site', label: 'Website (handwriting)', type: 'text' }] },
  { tab: 'text', title: 'Closing', at: sceneAt('outro', 4), fields: [
   { path: 'outro.lead', label: 'Title', type: 'text' }, { path: 'outro.mission.0', label: 'Mission line 1', type: 'text' }, { path: 'outro.mission.1', label: 'Mission line 2', type: 'text' }, { path: 'outro.mission.2', label: 'Mission line 3', type: 'text' },
   { path: 'outro.site', label: 'Website (handwriting)', type: 'text' }, { path: 'outro.thanks', label: 'Thank you', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · positive · 1st of a comparison · pen', 20), col('colors.blue', 'Blue — 2nd of a comparison', sceneAt('decline')), col('colors.mint', 'Mint — 3rd · to check', sceneAt('decline')),
   col('colors.navy', 'Navy — negative · wrong · down', sceneAt('decline')), col('colors.ink', 'Text', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.mintDark', 'Mint dark (mint text · white-text chips)', sceneAt('decline')), col('colors.crimson', 'Crimson (small red text)', 20), col('colors.lightRed', 'Light red (secondary rise)', sceneAt('decline')),
   col('colors.blush', 'Blush (highlighter)', 5), col('colors.redTint', 'Red tint (red chip · track)', 20), col('colors.navyTint', 'Navy tint', 20), col('colors.blueTint', 'Blue tint (blue track)', sceneAt('decline')), col('colors.mintTint', 'Mint tint', 20),
   col('colors.muted', 'Slate (secondary text)', 20), col('colors.midGrey', 'Mid grey (the rest)', 20), col('colors.lineGrey', 'Line grey (dashed · secondary lines)', 20), col('colors.lightBox', 'Light box (secondary boxes)', 20),
   col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration and timing come from tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
