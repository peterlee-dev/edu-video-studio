// 사용법: node render.mjs --ep spring [--workers 6] [--fps 30] [--preview] [--out out/forest_spring.mp4]
// audio/mix_<편>.wav 를 함께 넣어요. --workers N: 브라우저 N개가 구간을 나눠 그린 뒤 이어 붙여요.
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const EP = arg('--ep', 'spring');
const preview = process.argv.includes('--preview');
const FPS = +arg('--fps', preview ? 15 : 30);
const WORKERS = Math.max(1, +arg('--workers', 1));
const OUT = path.resolve(dir, arg('--out', preview ? `out/forest_${EP}_preview.mp4` : `out/forest_${EP}.mp4`));
const FFMPEG = process.env.FFMPEG || path.join(dir, '../math-di-improvement-v2/node_modules/ffmpeg-static/ffmpeg');
const CHROMIUM = process.env.CHROMIUM || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const audio = path.join(dir, 'audio', `mix_${EP}.wav`);
const VIDEO_ARGS = ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', preview ? 'veryfast' : 'medium', '-crf', preview ? '26' : '18', '-r', String(FPS)];

mkdirSync(path.dirname(OUT), { recursive: true });
async function openPage() {
  const browser = await chromium.launch({ executablePath: CHROMIUM });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.error('pageerror', e.message));
  await page.goto(pathToFileURL(path.join(dir, 'index.html')).href + `?render&ep=${EP}`);
  await page.evaluate(() => window.ready);
  return { browser, page, canvas: await page.$('#c') };
}
const run = (args, stdin) => new Promise((res, rej) => { const p = spawn(FFMPEG, args, { stdio: [stdin ? 'pipe' : 'ignore', 'inherit', 'inherit'] }); p.on('close', c => c === 0 ? res() : rej(new Error(`ffmpeg exit ${c}`))); if (stdin) stdin(p); });
async function frames(w, from, to, ff, tag) {
  for (let i = from; i < to; i++) {
    await w.page.evaluate(t => window.draw(t), i / FPS);
    const buf = await w.canvas.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((i - from) % (FPS * 20) === 0) process.stdout.write(`${tag}${((i - from) / FPS).toFixed(0)}s / ${((to - from) / FPS).toFixed(0)}s\n`);
  }
  ff.stdin.end();
}
const audioArgs = duration => existsSync(audio) ? ['-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-t', String(duration)] : [];

const first = await openPage();
const duration = await first.page.evaluate(() => window.DURATION);
const total = Math.round(duration * FPS);
await first.browser.close();
const tmp = path.join(path.dirname(OUT), `parts_${EP}`); mkdirSync(tmp, { recursive: true });
const per = Math.ceil(total / WORKERS), parts = [];
await Promise.all(Array.from({ length: WORKERS }, async (_, k) => {
  const from = k * per, to = Math.min(total, from + per), part = path.join(tmp, `part${String(k).padStart(2, '0')}.mp4`); parts.push(part);
  const w = await openPage();
  await run(['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', ...VIDEO_ARGS, part], ff => frames(w, from, to, ff, `[w${k}] `));
  await w.browser.close();
}));
const list = path.join(tmp, 'list.txt'); writeFileSync(list, parts.sort().map(p => `file '${p}'`).join('\n'));
const args = ['-y', '-f', 'concat', '-safe', '0', '-i', list];
if (existsSync(audio)) args.push('-i', audio);
await run([...args, '-c:v', 'copy', ...audioArgs(duration), '-movflags', '+faststart', OUT]);
rmSync(tmp, { recursive: true, force: true });
console.log(`\n완료: ${OUT}`);
