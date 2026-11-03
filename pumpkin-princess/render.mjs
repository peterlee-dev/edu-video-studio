// 사용법: node render.mjs [--fps 30] [--out out/<폴더이름>.mp4] [--preview] [--project 편집기에서_저장한.json] [--workers 4] [--cpu] [--lang en]
// audio/mix.wav (또는 song.mp3/.wav/.m4a) 가 있으면 자동으로 합성합니다.
// GPU(기본): Chrome 이 Metal GPU 로 캔버스를 그리고, 브라우저 안의 하드웨어 H.264 인코더(WebCodecs → VideoToolbox)로 바로 압축해요.
//   브라우저 밖으로는 압축된 영상만 나와서(PNG 스크린샷 · CPU 인코딩 없음) 빨라요. 조각들은 다시 인코딩하지 않고 그대로 이어 붙여요.
// --cpu: 예전 방식(SwiftShader 소프트웨어 그리기 + PNG 스크린샷 + libx264). GPU 가 없는 컴퓨터용
// --workers N: 브라우저 N개가 구간을 나눠 그린 뒤 이어 붙여요(빠름). 1이면 한 브라우저가 처음부터 끝까지 그려요.
// --only 99.4-114.4,217-end: 그 구간(초)만 다시 그리고 나머지는 이미 있는 결과 영상에서 가져와 이어 붙여요 (일부만 고쳤을 때)
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync, appendFileSync, rmSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const preview = process.argv.includes('--preview');
const GPU = !process.argv.includes('--cpu');
const FPS = +arg('--fps', preview ? 15 : 30);
const WORKERS = Math.max(1, +arg('--workers', 1));
const LANG = arg('--lang', 'ko'), SUF = LANG === 'ko' ? '' : '_' + LANG;   // --lang en → 영어판
const NAME = path.basename(dir).replace(/-/g, '_') + SUF;
const OUT = path.resolve(dir, arg('--out', preview ? `out/${NAME}_preview.mp4` : `out/${NAME}.mp4`));
const FFMPEG = process.env.FFMPEG || [path.join(dir, 'node_modules/ffmpeg-static/ffmpeg')].find(existsSync) || 'ffmpeg';
const AUDIO_START = process.env.AUDIO_START || '0'; // 노래의 시작 지점(초)
const audio = [`mix${SUF}.wav`, 'song.mp3', 'song.wav', 'song.m4a'].map(f => path.join(dir, 'audio', f)).find(existsSync);
// CPU: libx264. GPU re-encodes (only --only joins) use the hardware encoder in ffmpeg
const VIDEO_ARGS = GPU ? ['-c:v', 'h264_videotoolbox', '-profile:v', 'high', '-b:v', preview ? '6M' : '20M', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-r', String(FPS)]
  : ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', preview ? 'veryfast' : 'medium', '-crf', preview ? '26' : '18', '-r', String(FPS)];
// in-browser encoder: H.264 High, Annex B (SPS/PPS before every key frame, no B-frames), so pieces join byte for byte
const ENC = { codec: 'avc1.640028', width: 1920, height: 1080, framerate: FPS, bitrate: preview ? 6e6 : 20e6, bitrateMode: 'variable', latencyMode: 'quality', hardwareAcceleration: 'prefer-hardware', avc: { format: 'annexb' } };
const TAG = ['-bsf:v', 'h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1'];   // label as plain BT.709 (Chrome writes sRGB transfer)
const CHROME_ARGS = GPU ? ['--use-angle=metal', '--enable-gpu', '--enable-gpu-rasterization', '--ignore-gpu-blocklist', '--allow-file-access-from-files']   // file:// 그림을 그려도 캔버스를 읽을 수 있게 (VideoFrame)
  : ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'];

mkdirSync(path.dirname(OUT), { recursive: true });
async function openPage() {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', args: CHROME_ARGS });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(dir, 'index.html')).href + '?render' + (SUF ? '&lang=' + LANG : ''));
  await page.evaluate(() => window.ready);
  const projectPath = arg('--project');                  // 영상 편집기에서 저장한 문구·색 (../editor/PROTOCOL.md)
  if (projectPath) await page.evaluate(p => window.VIDEO.apply(p.content), JSON.parse(readFileSync(path.resolve(projectPath), 'utf8')));
  return { browser, page, canvas: await page.$('#c') };
}
// a browser that will not close (e.g. Chrome updated itself mid-render) must not hold the render up
const close = b => Promise.race([b.close(), new Promise(r => setTimeout(r, 15000))]);
const run = (args, stdin) => new Promise((res, rej) => { const p = spawn(FFMPEG, args, { stdio: [stdin ? 'pipe' : 'ignore', 'inherit', 'inherit'] }); p.on('close', c => c === 0 ? res() : rej(new Error(`ffmpeg exit ${c}`))); if (stdin) stdin(p); });
const log = (tag, done, all) => process.stdout.write(`${tag}${(done / FPS).toFixed(0)}s / ${(all / FPS).toFixed(0)}s\n`);

// CPU: draw frames [from, to) and pipe PNG screenshots into an ffmpeg process
async function frames(w, from, to, ff, tag) {
  for (let i = from; i < to; i++) {
    await w.page.evaluate(t => window.draw(t), i / FPS);
    const buf = await w.canvas.screenshot({ type: 'png', timeout: 300000 });   // generous: a busy machine can take long
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((i - from) % (FPS * 10) === 0) log(tag, i - from, to - from);
  }
  ff.stdin.end();
}
// GPU: draw frames [from, to) and encode them in the page; the H.264 comes out in 10 s batches and is appended to file
async function encodeGPU(w, from, to, file, tag) {
  const ok = await w.page.evaluate(async cfg => {
    if (!window.VideoEncoder || !(await VideoEncoder.isConfigSupported(cfg)).supported) return false;
    const E = window.__enc = { out: [], err: null };
    E.enc = new VideoEncoder({ output: ch => { const a = new Uint8Array(ch.byteLength); ch.copyTo(a); E.out.push(a); }, error: e => { E.err = e.message; } });
    E.enc.configure(cfg); return true;
  }, ENC);
  if (!ok) throw new Error('이 Chrome 에서 하드웨어 H.264 인코딩을 쓸 수 없어요. --cpu 로 렌더하세요');
  writeFileSync(file, '');
  for (let a = from; a < to; a += FPS * 10) {
    const b = Math.min(to, a + FPS * 10);
    const b64 = await w.page.evaluate(async ({ a, b, from, last, FPS, KEY }) => {
      const E = window.__enc, cv = document.getElementById('c');
      for (let i = a; i < b; i++) {
        window.draw(i / FPS);
        const f = new VideoFrame(cv, { timestamp: Math.round((i - from) * 1e6 / FPS), duration: Math.round(1e6 / FPS) });
        E.enc.encode(f, { keyFrame: (i - from) % KEY === 0 }); f.close();
        while (E.enc.encodeQueueSize > 4) await new Promise(r => setTimeout(r, 1));
      }
      if (last) await E.enc.flush();
      if (E.err) throw new Error(E.err);
      const n = E.out.reduce((s, x) => s + x.length, 0), all = new Uint8Array(n); let o = 0;
      for (const x of E.out) { all.set(x, o); o += x.length; } E.out = [];
      let s = ''; for (let i = 0; i < n; i += 0x8000) s += String.fromCharCode.apply(null, all.subarray(i, i + 0x8000));
      return btoa(s);
    }, { a, b, from, last: b === to, FPS, KEY: FPS * 2 });
    appendFileSync(file, Buffer.from(b64, 'base64'));
    log(tag, b - from, to - from);
  }
}
// draw [from, to) into one piece file (.h264 on the GPU path, .mp4 on the CPU path)
const piece = (w, from, to, file, tag) => GPU ? encodeGPU(w, from, to, file, tag)
  : run(['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', ...VIDEO_ARGS, file], ff => frames(w, from, to, ff, tag));
const EXT = GPU ? 'h264' : 'mp4';
const audioArgs = duration => audio ? ['-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-af', `afade=t=in:d=0.3,afade=t=out:st=${duration - 2}:d=2`, '-t', String(duration)] : [];
const audioIn = () => audio ? ['-ss', AUDIO_START, '-i', audio] : [];
// join pieces without re-encoding: raw H.264 pieces are joined byte for byte, mp4 pieces with the concat demuxer
async function join(files, tmp, duration) {
  if (GPU) {
    const all = path.join(tmp, 'all.h264'); writeFileSync(all, ''); for (const f of files) appendFileSync(all, readFileSync(f));
    await run(['-y', '-v', 'error', '-fflags', '+genpts', '-r', String(FPS), '-f', 'h264', '-i', all, ...audioIn(), '-c:v', 'copy', ...TAG, ...audioArgs(duration), '-movflags', '+faststart', OUT]);
  } else {
    const list = path.join(tmp, 'list.txt'); writeFileSync(list, files.map(p => `file '${p}'`).join('\n'));
    await run(['-y', '-f', 'concat', '-safe', '0', '-i', list, ...audioIn(), '-c:v', 'copy', ...audioArgs(duration), '-movflags', '+faststart', OUT]);
  }
}

const first = await openPage();
const duration = await first.page.evaluate(() => window.DURATION);
const total = Math.round(duration * FPS);
const started = Date.now();
console.log(`${GPU ? 'GPU (Metal + 하드웨어 H.264)' : 'CPU (SwiftShader + libx264)'} · ${total} 프레임 · 작업자 ${WORKERS}`);

const ONLY = arg('--only');
const tmp = path.join(path.dirname(OUT), 'parts'); rmSync(tmp, { recursive: true, force: true }); mkdirSync(tmp, { recursive: true });
if (ONLY) {
  // re-draw only the given spans; the rest comes from the existing OUT
  if (!existsSync(OUT)) throw new Error(`--only needs an existing ${OUT}`);
  await close(first.browser);
  const old = path.join(tmp, 'old.mp4'); writeFileSync(old, readFileSync(OUT));
  const spans = ONLY.split(',').map(r => r.split('-').map(v => v === 'end' ? total : Math.max(0, Math.min(total, Math.round(+v * FPS))))).sort((a, b) => a[0] - b[0]);
  const segs = []; let at = 0;
  for (const [a, b] of spans) { if (a > at) segs.push({ from: at, to: a, old: true }); if (b > Math.max(a, at)) segs.push({ from: Math.max(a, at), to: b }); at = Math.max(at, b); }
  if (at < total) segs.push({ from: at, to: total, old: true });
  // split the new spans into pieces so every browser gets about the same amount
  const newFrames = segs.filter(x => !x.old).reduce((n, x) => n + x.to - x.from, 0), per = Math.ceil(newFrames / WORKERS), pieces = [];
  segs.forEach((x, i) => { x.files = []; if (x.old) return; for (let f = x.from, j = 0; f < x.to; f += per, j++) { const file = path.join(tmp, `s${i}_${j}.${EXT}`); x.files.push(file); pieces.push({ from: f, to: Math.min(x.to, f + per), file }); } });
  console.log(`다시 그릴 프레임 ${newFrames} / ${total} (${(newFrames / FPS).toFixed(1)}s)`);
  const queue = [...pieces];
  await Promise.all(Array.from({ length: Math.min(WORKERS, pieces.length) }, async (_, k) => {
    const w = await openPage();
    for (let q; (q = queue.shift());) await piece(w, q.from, q.to, q.file, `[w${k}] ${(q.from / FPS).toFixed(0)}s+`);
    await close(w.browser);
  }));
  // old spans cut from the old video by frame + the new pieces, joined and encoded once
  const ins = [], parts = [];
  const add = (input, f) => { parts.push(`[${parts.length}:v]${f},setpts=PTS-STARTPTS[v${parts.length}]`); ins.push(...input); };
  segs.forEach(x => x.old ? add(['-i', old], `trim=start_frame=${x.from}:end_frame=${x.to}`)
    : x.files.forEach(f => add(GPU ? ['-r', String(FPS), '-f', 'h264', '-i', f] : ['-i', f], 'null')));
  const filter = parts.join(';') + ';' + parts.map((_, i) => `[v${i}]`).join('') + `concat=n=${parts.length}:v=1:a=0[v]`;
  await run(['-y', '-v', 'error', ...ins, ...audioIn(), '-filter_complex', filter, '-map', '[v]',
    ...(audio ? ['-map', `${parts.length}:a`, '-c:a', 'aac', '-b:a', '192k', '-af', `afade=t=in:d=0.3,afade=t=out:st=${duration - 2}:d=2`] : []),
    ...VIDEO_ARGS, '-t', String(duration), '-movflags', '+faststart', OUT]);
} else {
  // one piece per browser
  if (WORKERS > 1) await close(first.browser);
  const per = Math.ceil(total / WORKERS), files = Array.from({ length: WORKERS }, (_, k) => path.join(tmp, `part${k}.${EXT}`));
  await Promise.all(files.map(async (file, k) => {
    const from = k * per, to = Math.min(total, from + per); if (from >= to) return;
    const w = WORKERS > 1 ? await openPage() : first;
    await piece(w, from, to, file, WORKERS > 1 ? `[w${k}] ` : '');
    await close(w.browser);
  }));
  await join(files.filter(existsSync), tmp, duration);
}
rmSync(tmp, { recursive: true, force: true });
console.log(`\n완료: ${OUT}${audio ? ` (오디오: ${path.basename(audio)})` : ' (오디오 없음 — audio/mix.wav 를 넣고 다시 렌더링하세요)'} · ${((Date.now() - started) / 1000).toFixed(0)}초`);
process.exit(0);
