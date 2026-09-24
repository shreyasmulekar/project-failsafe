const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

async function test() {
  const edge = spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', [
    '--remote-debugging-port=9239',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));
  const tabs = await new Promise(res => http.get('http://localhost:9239/json', r => {
    let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
  }));
  const page = tabs.find(t => t.type === 'page' && t.url.includes('localhost'));
  const ws = new globalThis.WebSocket(page.webSocketDebuggerUrl);
  let id = 1;
  const send = (method, params = {}) => new Promise(res => {
    const curId = id++;
    const h = (e) => {
      const d = JSON.parse(e.data);
      if (d.id === curId) { ws.removeEventListener('message', h); res(d.result); }
    };
    ws.addEventListener('message', h);
    ws.send(JSON.stringify({ id: curId, method, params }));
  });
  ws.onopen = async () => {
    await send('Runtime.enable');
    await send('Page.enable');
    
    // Log in with team
    await send('Runtime.evaluate', {
      expression: `
        applyAuthenticatedTeam({ team_id: 'TEAM-01', team_name: 'Alpha Squad', current_stage: 1 });
      `
    });
    await new Promise(r => setTimeout(r, 200));

    // Open modal
    await send('Runtime.evaluate', {
      expression: `openModal('modal-recovery');`
    });
    await new Promise(r => setTimeout(r, 200));

    // Close modal
    await send('Runtime.evaluate', {
      expression: `closeModal('modal-recovery');`
    });
    await new Promise(r => setTimeout(r, 200));

    const ss = await send('Page.captureScreenshot');
    fs.writeFileSync('C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/screen_after_close.png', Buffer.from(ss.data, 'base64'));
    console.log('Saved screen_after_close.png');

    edge.kill();
    process.exit(0);
  };
}
test().catch(e => { console.error(e); process.exit(1); });
