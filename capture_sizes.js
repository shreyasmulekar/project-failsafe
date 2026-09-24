const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const artifactDir = 'C:\\Users\\shrey\\.gemini\\antigravity\\brain\\17c36665-51d0-4b98-8e9d-7e8fd18fcd27';

async function captureSize(name, width, height) {
  const port = 9350 + Math.floor(Math.random() * 500);
  const edge = spawn(edgeExe, [
    `--remote-debugging-port=${port}`,
    '--headless',
    '--disable-gpu',
    `--window-size=${width},${height}`,
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2200));

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

  await new Promise(resolve => {
    ws.onopen = async () => {
      await send('Runtime.enable');
      await send('Page.enable');
      await send('Emulation.setDeviceMetricsOverride', {
        width,
        height,
        deviceScaleFactor: 1,
        mobile: false
      });

      await send('Runtime.evaluate', {
        expression: `
          applyAuthenticatedTeam({
            team_id: 'TEAM-01',
            team_name: 'Alpha Squadron',
            current_stage: 1
          });
        `
      });

      await new Promise(r => setTimeout(r, 400));
      const ss = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(path.join(artifactDir, `viewport_${name}.png`), Buffer.from(ss.data, 'base64'));

      edge.kill();
      resolve();
    };
  });
}

async function main() {
  await captureSize('common_laptop_1366x768', 1366, 768);
  await captureSize('scaled_windows_1536x864', 1536, 864);
  await captureSize('large_laptop_1920x1080', 1920, 1080);
  console.log('All screenshots captured!');
}

main().catch(console.error);
