// 편집본(작업 파일)을 최고 화질 MP4 로: node editor/render.mjs 작업파일.json [--out out.mp4] [--fps 30] [--cpu]
// 저장소 맨 위를 잠깐 로컬 서버로 열고, 편집기 페이지(?render)에서 한 장씩 그려 영상으로 묶음
// GPU(기본): Chrome 이 Metal GPU 로 그리고, 브라우저 안의 하드웨어 H.264 인코더(WebCodecs → VideoToolbox)로 바로 압축해요.
// --cpu: 예전 방식(SwiftShader 소프트웨어 그리기 + PNG + libx264). GPU 가 없는 컴퓨터용
// 필요: 영상 폴더 하나의 npm install (playwright-core), FFMPEG(없으면 ffmpeg), CHROMIUM(없으면 Google Chrome)
import { createServer } from 'node:http';
import { readFileSync, writeFileSync, appendFileSync, existsSync, statSync, mkdirSync, readdirSync, rmSync } from 'node:fs';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import path from 'node:path';
import os from 'node:os';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2), arg = (k, d) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : d; };
const projectFile = argv.find(a => a.endsWith('.json'));
if (!projectFile) { console.error('사용법: node editor/render.mjs 작업파일.json [--out out.mp4]'); process.exit(1); }
const project = JSON.parse(readFileSync(projectFile, 'utf8'));
const GPU = !argv.includes('--cpu');
const OUT = path.resolve(arg('--out', 'out/edit.mp4')), FFMPEG = process.env.FFMPEG || 'ffmpeg';
const pwDir = readdirSync(root).map(d => path.join(root, d, 'node_modules', 'playwright-core')).find(existsSync);
if (!pwDir) { console.error('playwright-core 가 없어요. 영상 폴더 하나에서 npm install 을 먼저 하세요.'); process.exit(1); }
const { chromium } = createRequire(import.meta.url)(pwDir);
const CHROME_ARGS = GPU ? ['--use-angle=metal', '--enable-gpu', '--enable-gpu-rasterization', '--ignore-gpu-blocklist', '--allow-file-access-from-files']   // file:// 그림을 그려도 캔버스를 읽을 수 있게 (VideoFrame)
  : ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'];
const TAG = ['-bsf:v', 'h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1'];   // label as plain BT.709 (Chrome writes sRGB transfer)

const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '.ttf': 'font/ttf', '.wav': 'audio/wav', '.mp3': 'audio/mpeg', '.png': 'image/png', '.jpg': 'image/jpeg' };
const server = createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!p.startsWith(root) || !existsSync(p) || statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': TYPES[path.extname(p)] || 'application/octet-stream' }); res.end(readFileSync(p));
}).listen(0);
const port = server.address().port;

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', args: CHROME_ARGS });
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
page.on('pageerror', e => console.error('페이지 오류:', e.message));
await page.goto(`http://127.0.0.1:${port}/video-editor.html?render`);
await page.waitForFunction(() => window.EDITOR);
await page.evaluate(p => EDITOR.loadProject(p), project);
await page.waitForFunction(() => EDITOR.ready, null, { timeout: 300000 });
const total = await page.evaluate(() => EDITOR.total), FPS = +arg('--fps', 30), frames = Math.round(total * FPS);
console.log(GPU ? 'GPU (Metal + 하드웨어 H.264)' : 'CPU (SwiftShader + libx264)');

const wav = path.join(os.tmpdir(), `jei_edit_${process.pid}.wav`);
writeFileSync(wav, Buffer.from(await page.evaluate(() => EDITOR.wavBase64()), 'base64'));
mkdirSync(path.dirname(OUT), { recursive: true });
const run = (args, stdin) => new Promise((res, rej) => { const p = spawn(FFMPEG, args, { stdio: [stdin ? 'pipe' : 'ignore', 'inherit', 'inherit'] }); p.on('close', c => c === 0 ? res() : rej(new Error(`ffmpeg exit ${c}`))); if (stdin) stdin(p); });
const audioArgs = ['-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-t', String(total), '-movflags', '+faststart', OUT];

if (GPU) {
  // draw and encode in the page; the H.264 comes out in 10 s batches
  const ENC = { codec: 'avc1.640028', width: 1920, height: 1080, framerate: FPS, bitrate: 20e6, bitrateMode: 'variable', latencyMode: 'quality', hardwareAcceleration: 'prefer-hardware', avc: { format: 'annexb' } };
  const ok = await page.evaluate(async cfg => {
    if (!window.VideoEncoder || !(await VideoEncoder.isConfigSupported(cfg)).supported) return false;
    const E = window.__enc = { out: [], err: null };
    E.enc = new VideoEncoder({ output: ch => { const a = new Uint8Array(ch.byteLength); ch.copyTo(a); E.out.push(a); }, error: e => { E.err = e.message; } });
    E.enc.configure(cfg); return true;
  }, ENC);
  if (!ok) throw new Error('이 Chrome 에서 하드웨어 H.264 인코딩을 쓸 수 없어요. --cpu 로 렌더하세요');
  const h264 = path.join(os.tmpdir(), `jei_edit_${process.pid}.h264`); writeFileSync(h264, '');
  for (let a = 0; a < frames; a += FPS * 10) {
    const b = Math.min(frames, a + FPS * 10);
    const b64 = await page.evaluate(async ({ a, b, last, FPS, KEY }) => {
      const E = window.__enc, cv = document.getElementById('view');
      for (let i = a; i < b; i++) {
        EDITOR.draw(i / FPS);
        const f = new VideoFrame(cv, { timestamp: Math.round(i * 1e6 / FPS), duration: Math.round(1e6 / FPS) });
        E.enc.encode(f, { keyFrame: i % KEY === 0 }); f.close();
        while (E.enc.encodeQueueSize > 4) await new Promise(r => setTimeout(r, 1));
      }
      if (last) await E.enc.flush();
      if (E.err) throw new Error(E.err);
      const n = E.out.reduce((s, x) => s + x.length, 0), all = new Uint8Array(n); let o = 0;
      for (const x of E.out) { all.set(x, o); o += x.length; } E.out = [];
      let s = ''; for (let i = 0; i < n; i += 0x8000) s += String.fromCharCode.apply(null, all.subarray(i, i + 0x8000));
      return btoa(s);
    }, { a, b, last: b === frames, FPS, KEY: FPS * 2 });
    appendFileSync(h264, Buffer.from(b64, 'base64'));
    process.stdout.write(`\r${(b / FPS).toFixed(0)}s / ${total.toFixed(1)}s`);
  }
  await run(['-y', '-v', 'error', '-fflags', '+genpts', '-r', String(FPS), '-f', 'h264', '-i', h264, '-i', wav, '-c:v', 'copy', ...TAG, ...audioArgs]);
  rmSync(h264, { force: true });
} else {
  await run(['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', '-i', wav, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18', '-r', String(FPS), ...audioArgs], async ff => {
    for (let i = 0; i < frames; i++) {
      const url = await page.evaluate(t => EDITOR.frame(t), i / FPS);
      if (!ff.stdin.write(Buffer.from(url.slice(url.indexOf(',') + 1), 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
      if (i % FPS === 0) process.stdout.write(`\r${(i / FPS).toFixed(0)}s / ${total.toFixed(1)}s`);
    }
    ff.stdin.end();
  });
}
rmSync(wav, { force: true });
await browser.close(); server.close();
console.log(`\n완료: ${OUT} (${total.toFixed(1)}초, 장면 ${project.clips ? project.clips.length : 1}개)`);
