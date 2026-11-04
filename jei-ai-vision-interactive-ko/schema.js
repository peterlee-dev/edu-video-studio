// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneAt = (id, d = 3) => { const s = TL.scenes.find(x => x.id === id); return s ? s.start + d : 0; };
const end = sceneAt('outro', 0) + 22;
window.SCHEMA = {
 id: 'jei-ai-vision-interactive-ko',
 title: 'JEI AI 전환 비전 (인터랙티브)',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: 'Text' }, { id: 'color', label: 'Colours' }],
 groups: [
  { tab: 'text', title: 'Cover', at: 12, fields: [
   { path: 'title.kicker', label: 'Kicker', type: 'text' }, { path: 'title.sub', label: 'Line above the title', type: 'text' }, { path: 'title.main', label: 'Title', type: 'text' },
   { path: 'title.tag1', label: 'Tagline 1', type: 'text' }, { path: 'title.tag2', label: 'Tagline 2', type: 'text' }, { path: 'title.date', label: 'Date', type: 'text' }, { path: 'title.button', label: 'Button', type: 'text' }] },
  { tab: 'text', title: 'Closing', at: Math.min(end, TL.duration - 2), fields: [
   { path: 'outro.line1', label: 'Line 1', type: 'text' }, { path: 'outro.line2', label: 'Line 2', type: 'text' }, { path: 'outro.big1', label: 'Title line 1', type: 'text' }, { path: 'outro.big2', label: 'Title line 2', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.gold', 'Gold — JEI accent · phase 1', 12), col('colors.green', 'Green — phase 2 · mastered', sceneAt('status', 20)), col('colors.blue', 'Blue — service · online', sceneAt('online', 8)),
   col('colors.orange', 'Orange — needs practice', sceneAt('status', 20)), col('colors.red', 'Red — learning gap', sceneAt('status', 20)), col('colors.ink', 'Text', 12), col('colors.bg', 'Background', 12)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.bg2', 'Background glow', 12), col('colors.panel', 'Panel', sceneAt('why', 6)), col('colors.panelHead', 'Panel header', sceneAt('why', 6)), col('colors.card', 'Card', sceneAt('why', 6)),
   col('colors.cardLine', 'Card outline', sceneAt('why', 6)), col('colors.muted', 'Secondary text', sceneAt('why', 6)), col('colors.dim', 'Dim text · lines', sceneAt('kmap', 6)), col('colors.grey', 'Grey — not yet studied', sceneAt('status', 20)), col('colors.sky', 'Light blue — relation lines', sceneAt('kmap', 20))] },
 ],
 locked: 'Narration: Qwen3-TTS reading the Korean script (tools/script.py) in the voice of audio/voice_ref.wav, timed by tools/make_audio.py. Every animation is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
