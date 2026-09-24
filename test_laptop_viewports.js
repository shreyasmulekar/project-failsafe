const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const artifactDir = 'C:\\Users\\shrey\\.gemini\\antigravity\\brain\\17c36665-51d0-4b98-8e9d-7e8fd18fcd27';

const viewports = [
  { name: 'small_laptop_1280x720', width: 1280, height: 720 },
  { name: 'common_laptop_1366x768', width: 1366, height: 768 },
  { name: 'macbook_1440x900', width: 1440, height: 900 },
  { name: 'scaled_windows_1536x864', width: 1536, height: 864 },
  { name: 'large_laptop_1920x1080', width: 1920, height: 1080 }
];

async function testViewport(vp) {
  const port = 9300 + Math.floor(Math.random() * 500);
  const edge = spawn(edgeExe, [
    `--remote-debugging-port=${port}`,
    '--headless',
    '--disable-gpu',
    `--window-size=${vp.width},${vp.height}`,
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  const tabs = await new Promise((resolve, reject) => {
    http.get(`http://localhost:${port}/json`, res => {
      let raw = '';
      res.on('data', c => raw += c);
      res.on('end', () => resolve(JSON.parse(raw)));
    }).on('error', reject);
  });

  const page = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new globalThis.WebSocket(page.webSocketDebuggerUrl);

  let msgId = 1;
  const send = (method, params = {}) => new Promise((resolve) => {
    const id = msgId++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });

  return new Promise((resolve) => {
    ws.onopen = async () => {
      await send('Runtime.enable');
      await send('Page.enable');
      await send('Emulation.setDeviceMetricsOverride', {
        width: vp.width,
        height: vp.height,
        deviceScaleFactor: 1,
        mobile: false
      });

      // Login
      await send('Runtime.evaluate', {
        expression: `
          applyAuthenticatedTeam({
            team_id: 'TEAM-01',
            team_name: 'Alpha Squadron',
            current_stage: 1
          });
        `
      });

      await new Promise(r => setTimeout(r, 500));

      // Measure layout metrics
      const metrics = await send('Runtime.evaluate', {
        expression: `
          (() => {
            const body = document.body;
            const doc = document.documentElement;
            const container = document.querySelector('.nexus-dashboard-container');
            const topRow = document.querySelector('.nexus-top-row');
            const hero = document.querySelector('.nexus-hero-card');
            const assistant = document.querySelector('.nexus-assistant-card');
            const grid = document.querySelector('.nexus-cards-grid');
            const header = document.querySelector('.nexus-header');
            const bottomDock = document.querySelector('.nexus-bottom-dock');

            // Open a modal to check modal metrics
            openModal('modal-recovery');
            const modal = document.getElementById('modal-recovery');
            const modalRect = modal ? modal.getBoundingClientRect() : null;
            closeModal('modal-recovery');

            return {
              viewport: { width: window.innerWidth, height: window.innerHeight },
              docScroll: { scrollWidth: doc.scrollWidth, clientWidth: doc.clientWidth, hasHScroll: doc.scrollWidth > doc.clientWidth },
              bodyScroll: { scrollWidth: body.scrollWidth, clientWidth: body.clientWidth, hasHScroll: body.scrollWidth > body.clientWidth },
              headerRect: header ? header.getBoundingClientRect() : null,
              topRowRect: topRow ? topRow.getBoundingClientRect() : null,
              heroRect: hero ? hero.getBoundingClientRect() : null,
              assistantRect: assistant ? assistant.getBoundingClientRect() : null,
              gridRect: grid ? grid.getBoundingClientRect() : null,
              bottomDockRect: bottomDock ? bottomDock.getBoundingClientRect() : null,
              modalRect: modalRect,
              modalOverflowY: modalRect ? (modalRect.height > window.innerHeight) : false,
              modalOverflowX: modalRect ? (modalRect.width > window.innerWidth) : false
            };
          })()
        `,
        returnByValue: true
      });

      // Capture screenshot
      const ss = await send('Page.captureScreenshot', { format: 'png' });
      const buffer = Buffer.from(ss.data, 'base64');
      const ssPath = path.join(artifactDir, `viewport_${vp.name}.png`);
      fs.writeFileSync(ssPath, buffer);

      // Also capture screenshot with modal open on this viewport
      await send('Runtime.evaluate', { expression: `openModal('modal-recovery');` });
      await new Promise(r => setTimeout(r, 300));
      const ssModal = await send('Page.captureScreenshot', { format: 'png' });
      const ssModalPath = path.join(artifactDir, `viewport_modal_${vp.name}.png`);
      fs.writeFileSync(ssModalPath, Buffer.from(ssModal.data, 'base64'));

      edge.kill();
      resolve({ name: vp.name, metrics: metrics.result.value, ssPath, ssModalPath });
    };
  });
}

async function main() {
  console.log('Testing responsiveness across 5 laptop viewports...');
  for (const vp of viewports) {
    const res = await testViewport(vp);
    console.log(`\n=== Viewport: ${res.name} (${vp.width}x${vp.height}) ===`);
    console.log('Horizontal Scroll on Document:', res.metrics.docScroll.hasHScroll ? '⚠️ YES' : '✅ NO');
    console.log('Horizontal Scroll on Body:', res.metrics.bodyScroll.hasHScroll ? '⚠️ YES' : '✅ NO');
    console.log('Top Row Layout:', `${Math.round(res.metrics.topRowRect.width)}x${Math.round(res.metrics.topRowRect.height)}`);
    console.log('Hero Card:', `${Math.round(res.metrics.heroRect.width)}x${Math.round(res.metrics.heroRect.height)}`);
    console.log('Assistant Card:', `${Math.round(res.metrics.assistantRect.width)}x${Math.round(res.metrics.assistantRect.height)}`);
    console.log('Modal Rect:', res.metrics.modalRect ? `${Math.round(res.metrics.modalRect.width)}x${Math.round(res.metrics.modalRect.height)} (Overflow Y: ${res.metrics.modalOverflowY}, Overflow X: ${res.metrics.modalOverflowX})` : 'N/A');
    console.log('Header Rect:', res.metrics.headerRect ? `${Math.round(res.metrics.headerRect.width)}x${Math.round(res.metrics.headerRect.height)}` : 'N/A');
  }
}

main().catch(console.error);
