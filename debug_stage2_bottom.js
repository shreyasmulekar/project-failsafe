const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function run() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9227',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,900',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  
  await new Promise(r => setTimeout(r, 2000));
  
  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9227/json', res => {
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
  
  ws.onopen = async () => {
    await send('Runtime.enable');
    
    // Evaluate in page context
    const code = `
      const authM = document.getElementById('team-auth-modal');
      if (authM) authM.style.display = 'none';
      window.localStorage.setItem('failsafe_auth', 'TEAM-01');
      window.localStorage.setItem('failsafe_team_id', '1');
      window.localStorage.setItem('failsafe_stage', '2');
      currentStage = 2;
      currentRound = 1;
      openModal('modal-memory');
    `;
    await send('Runtime.evaluate', { expression: code });
    await new Promise(r => setTimeout(r, 500));
    
    // Scroll modal-memory to bottom
    await send('Runtime.evaluate', {
      expression: `
        const m = document.getElementById('modal-memory');
        if (m) m.scrollTop = m.scrollHeight;
        const b = m ? m.querySelector('.mil-modal-body') : null;
        if (b) b.scrollTop = b.scrollHeight;
      `
    });
    await new Promise(r => setTimeout(r, 300));
    
    const ss = await send('Page.captureScreenshot');
    fs.writeFileSync('C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/stage2_bottom_screenshot.png', Buffer.from(ss.data, 'base64'));
    
    edge.kill();
    process.exit(0);
  };
}

run().catch(e => { console.error(e); process.exit(1); });
