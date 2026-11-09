// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
window.SCHEMA = {
 id: 'jei-ai-vision',
 title: 'JEI AI Transformation Vision · JEI AI 전환 비전 (영문, 남자 목소리, 모눈종이 워크북)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Title', at: 6, fields: [
   { path: 'title.kicker', label: 'Kicker', type: 'text' }, { path: 'title.words.0', label: 'Title line 1', type: 'text' }, { path: 'title.words.1', label: 'Title line 2', type: 'text' }, { path: 'title.words.2', label: 'Title line 3', type: 'text' },
   { path: 'title.sub.0', label: 'Subtitle line 1', type: 'text' }, { path: 'title.sub.1', label: 'Subtitle line 2', type: 'text' }] },
  { tab: 'text', title: 'Closing', at: sceneAt('outro', 22), fields: [
   { path: 'outro.lead.0', label: 'Lead line 1', type: 'text' }, { path: 'outro.lead.1', label: 'Lead line 2', type: 'text' }, { path: 'outro.words.0', label: 'Title line 1', type: 'text' }, { path: 'outro.words.1', label: 'Title line 2', type: 'text' }, { path: 'outro.words.2', label: 'Title line 3', type: 'text' },
   { path: 'outro.value', label: 'Handwriting 1', type: 'text' }, { path: 'outro.standard', label: 'Handwriting 2', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · positive · 1st of a comparison · pen', 20), col('colors.blue', 'Blue — 2nd of a comparison (Phase 2)', sceneAt('phase2', 5)), col('colors.mint', 'Mint — 3rd · needs more practice', sceneAt('statuses', 6)),
   col('colors.navy', 'Navy — negative · mastered (p. 10)', sceneAt('statuses', 6)), col('colors.ink', 'Text', 20), col('colors.paper', 'Background', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.mintDark', 'Mint dark (text · white-text chips)', sceneAt('wiki', 5)), col('colors.crimson', 'Crimson (small red text)', sceneAt('pod', 10)), col('colors.lightRed', 'Light red', sceneAt('layerPace', 5)),
   col('colors.blush', 'Blush (highlighter)', 8), col('colors.redTint', 'Red tint', sceneAt('universe', 15)), col('colors.blueTint', 'Blue tint', sceneAt('country', 10)), col('colors.mintTint', 'Mint tint', sceneAt('wiki', 5)), col('colors.navyTint', 'Navy tint', sceneAt('kmapAI', 8)),
   col('colors.muted', 'Slate (secondary text)', 20), col('colors.midGrey', 'Mid grey (not yet studied)', sceneAt('statuses', 6)), col('colors.lineGrey', 'Line grey (outlines)', sceneAt('kmapDots', 8)), col('colors.lightBox', 'Light box (secondary boxes)', sceneAt('title', 8)), col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration: Qwen3-TTS reading the English script (tools/script.py) in the voice of audio/voice_ref.wav (as ../ai-learning-platform-v3), timed by tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
