// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
window.SCHEMA = {
 id: 'geo-monitor-ko',
 title: 'GEO 모니터링 콘솔 (경영진 설명)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Opening question', at: 5.5, fields: [
   { path: 'title.ask', label: 'Typed question', type: 'text' }, { path: 'title.q.0', label: 'Question (boxed part)', type: 'text' }, { path: 'title.q.1', label: 'Question (rest)', type: 'text' },
   { path: 'title.url', label: 'Address', type: 'text' }] },
  { tab: 'text', title: 'Until now', at: sceneAt('before', 3), fields: [{ path: 'before', label: 'Words', type: 'text' }] },
  { tab: 'text', title: 'Questions', at: sceneAt('trust', 2.5), fields: [
   { path: 'questions.0', label: 'Trust question', type: 'text' }, { path: 'questions.1', label: 'Rules question', type: 'text' }] },
  { tab: 'text', title: 'What it brings', at: sceneAt('outro', 3), fields: [
   { path: 'outro.title', label: 'Title', type: 'text' }, { path: 'outro.points.0', label: 'Switch 1', type: 'text' }, { path: 'outro.points.1', label: 'Switch 2', type: 'text' }, { path: 'outro.points.2', label: 'Switch 3', type: 'text' },
   { path: 'outro.decide.0', label: 'Line 1', type: 'text' }, { path: 'outro.decide.1', label: 'Line 2 (first word boxed)', type: 'text' }] },
  { tab: 'text', title: 'End card', at: sceneAt('end', 5), fields: [{ path: 'end', label: 'Line (first word boxed)', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — brand, backgrounds, ChatGPT', 3), col('colors.redHi', 'Red background, light corner', 3), col('colors.crimson', 'Red background, dark corner', 3),
   col('colors.navy', 'Navy — the old way', sceneAt('before', 3)), col('colors.blue', 'Blue — Gemini', sceneAt('purpose', 5)), col('colors.mintDark', 'Mint dark — Claude', sceneAt('purpose', 5)), col('colors.ink', 'Text', sceneAt('look', 3))] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.redTint', 'Red tint', sceneAt('outro', 3)), col('colors.navyDeep', 'Navy background, dark corner', sceneAt('before', 3)), col('colors.muted', 'Slate (secondary text)', sceneAt('look', 3)),
   col('colors.lineGrey', 'Line grey', sceneAt('trust', 4)), col('colors.lightBox', 'Placeholder bars', sceneAt('look', 3))] },
 ],
 locked: 'Narration: Qwen3-TTS reading the Korean script (tools/script.py) in the voice of audio/voice_ref.wav (the ai-learning-platform-v3-ko voice), timed by tools/make_audio.py, with synthesized upbeat music under it. No report results on screen or in the script (asked for). Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
