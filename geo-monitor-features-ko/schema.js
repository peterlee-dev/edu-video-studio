// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
const notes = (id, n) => Array.from({ length: n }, (_, i) => ({ path: `${id}.notes.${i}`, label: `Note ${i + 1}`, type: 'text' }));
window.SCHEMA = {
 id: 'geo-monitor-features-ko',
 title: 'GEO 모니터링 콘솔 화면 설명',
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
  { tab: 'text', title: 'Screens', at: sceneAt('intro', 3), fields: [{ path: 'intro', label: 'Words (last word boxed)', type: 'text' }] },
  ...['sets', 'summary', 'metrics', 'question', 'sources', 'competitors', 'responses', 'settings', 'top', 'criteria', 'team'].map(id => ({
   tab: 'text', title: TL.scenes.find(s => s.id === id)?.label || id, at: sceneAt(id, 4),
   fields: [{ path: `${id}.label`, label: 'Page name', type: 'text' }, ...notes(id, window.CONTENT[id].notes.length)] })),
  { tab: 'text', title: 'End card', at: sceneAt('end', 5), fields: [{ path: 'end', label: 'Line (first word boxed)', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — brand, backgrounds, spotlight, ChatGPT', 3), col('colors.redHi', 'Red background, light corner', 3), col('colors.crimson', 'Red background, dark corner', 3),
   col('colors.blue', 'Blue — Gemini', sceneAt('flow', 4)), col('colors.mintDark', 'Mint dark — Claude', sceneAt('flow', 4)), col('colors.ink', 'Text', sceneAt('sets', 4))] },
 ],
 locked: 'Narration: Qwen3-TTS reading the Korean script (tools/script.py) in the voice of audio/voice_ref_b.wav, timed by tools/make_audio.py, with synthesized upbeat music under it. The captures are the console as it is (sidebar and member list cut off); spotlight positions are in index.html. No report results in the script (asked for). Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
