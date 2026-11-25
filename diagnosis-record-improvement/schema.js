// Fields shown in the video editor (../video-editor.html). Rules: ../editor/PROTOCOL.md
(() => {
const TL = window.TL;
const col = (path, label, at) => ({ path, label, desc: '', type: 'color', at });
const sceneEnd = (id, d = 1) => { const s = TL.scenes.find(x => x.id === id); return s ? s.end - d : 0; };
// the caption under the lens: title + line for each item of the report page
const itemFields = (id, n) => [...Array(n)].flatMap((_, i) => [{ path: `${id}.items.${i}.0`, label: `${i + 1} 제목`, type: 'text' }, { path: `${id}.items.${i}.1`, label: `${i + 1} 설명`, type: 'text' }]);
window.SCHEMA = {
 id: 'diagnosis-record-improvement',          // same as the folder name
 title: '개인별 진단처방기록부 개선 시안',
 duration: TL.duration, fps: 30,
 audio: ['audio/mix.wav', 'audio/mix.mp3'],
 audioFade: { in: 0.3, out: 2 },
 scenes: TL.scenes.map(s => ({ start: s.start, end: s.end, label: s.label })),
 sounds: [],
 tabs: [{ id: 'text', label: '문구' }, { id: 'color', label: '색' }],
 groups: [
  { tab: 'text', title: '표지', at: 4, fields: [
   { path: 'title.kicker', label: '머리 칩', type: 'text' }, { path: 'title.words.0', label: '제목 1줄', type: 'text' }, { path: 'title.words.1', label: '제목 2줄', type: 'text' }, { path: 'title.words.2', label: '제목 3줄', type: 'text' },
   { path: 'title.sub', label: '부제', type: 'text' }, { path: 'title.team', label: '팀 · 날짜 (손글씨)', type: 'text' }] },
  { tab: 'text', title: '개선의 핵심', at: sceneEnd('core'), fields: [{ path: 'core.title', label: '제목', type: 'text' }, { path: 'core.bar', label: '맺음 띠', desc: '{ } 로 감싼 말은 조금 크게', type: 'text' }] },
  { tab: 'text', title: '01 기존 리포트', at: sceneEnd('old'), fields: [{ path: 'old.title', label: '제목', type: 'text' }, { path: 'old.head', label: '카드 머리', type: 'text' },
   { path: 'old.change.0', label: '카드 1줄', type: 'text' }, { path: 'old.change.1', label: '카드 2줄', type: 'text' },
   { path: 'old.asks.0', label: '①', type: 'text' }, { path: 'old.asks.1', label: '②', type: 'text' }, { path: 'old.asks.2', label: '③', type: 'text' }] },
  { tab: 'text', title: '03 1페이지 시안', at: sceneEnd('p1'), fields: [{ path: 'p1.title', label: '제목', type: 'text' }, ...itemFields('p1', 6)] },
  { tab: 'text', title: '04 2페이지 시안', at: sceneEnd('p2'), fields: [{ path: 'p2.title', label: '제목', type: 'text' }, ...itemFields('p2', 4)] },
  { tab: 'text', title: '마무리', at: sceneEnd('outro', 2), fields: [{ path: 'outro.title', label: '제목', type: 'text' },
   { path: 'outro.keep.0', label: '왼쪽 카드 제목', type: 'text' }, { path: 'outro.keep.1', label: '왼쪽 카드 설명', type: 'text' },
   { path: 'outro.change.0', label: '오른쪽 카드 제목 (레드)', type: 'text' }, { path: 'outro.change.1', label: '오른쪽 카드 설명', type: 'text' }] },
  { tab: 'text', title: '감사합니다', at: sceneEnd('thanks', 2), fields: [{ path: 'thanks.text', label: '끝인사 (손글씨)', type: 'text' }, { path: 'thanks.sub', label: '아래 줄', type: 'text' }, { path: 'thanks.team', label: '팀 (손글씨)', type: 'text' }] },
  { tab: 'color', title: 'Main colours', fields: [col('colors.red', 'Red — main · pen · focus box', 20), col('colors.navy', 'Navy — 보완 필요 circles', sceneEnd('p1')), col('colors.ink', 'Text · dark card', 20), col('colors.paper', 'Background · lens dimming', 20)] },
  { tab: 'color', title: 'Sub colours', fields: [col('colors.lightRed', 'Light red (dark card heading)', sceneEnd('old')), col('colors.blush', 'Blush (highlighter)', 5), col('colors.muted', 'Slate (secondary text)', 20),
   col('colors.lineGrey', 'Line grey (tape)', 5), col('colors.lightBox', 'Light box (lens background · chips)', sceneEnd('p1')),
   col('colors.grid', 'Graph-paper lines', 20), col('colors.gridMajor', 'Graph-paper lines (every 5th)', 20), col('colors.margin', 'Left margin line', 20)] },
 ],
 locked: 'Narration: Qwen3-TTS reading tools/script.py in the voice of audio/voice_ref.wav (as ../jei-math-difference-ko), timed by tools/make_audio.py. Every animation and lens move is keyed to a narration line or a spoken word.',
 warnings: [],
};
})();
