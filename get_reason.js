const { spawn } = require('child_process');
const http = require('http');

async function test() {
  const edge = spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', [
    '--remote-debugging-port=9238',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));
  const tabs = await new Promise(res => http.get('http://localhost:9238/json', r => {
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
    
    // Log in
    await send('Runtime.evaluate', {
      expression: `
        applyAuthenticatedTeam({ team_id: 'TEAM-01' });
        openModal('modal-recovery');
      `
    });
    await new Promise(r => setTimeout(r, 300));

    // Listen to who calls triggerProctorLockdown
    await send('Runtime.evaluate', {
      expression: `
        const origTrigger = triggerProctorLockdown;
        window.__lastCallStack = '';
        window.__lastReason = '';
        triggerProctorLockdown = function(reason) {
          window.__lastReason = reason;
          window.__lastCallStack = new Error().stack;
          console.log('triggerProctorLockdown called with:', reason, window.__lastCallStack);
          return origTrigger.apply(this, arguments);
        };
      `
    });

    // Click close button
    await send('Runtime.evaluate', {
      expression: `
        const btn = document.querySelector('#modal-recovery .mil-modal-close');
        btn.click();
      `
    });
    await new Promise(r => setTimeout(r, 500));

    const result = await send('Runtime.evaluate', {
      expression: `
        ({
          reason: window.__lastReason,
          stack: window.__lastCallStack,
          lockActive: typeof proctorLockActive !== 'undefined' ? proctorLockActive : null,
          reasonEl: document.getElementById('proctor-violation-reason') ? document.getElementById('proctor-violation-reason').innerText : ''
        })
      `,
      returnByValue: true
    });

    console.log('LOCKDOWN INSPECTION RESULT:', JSON.stringify(result.result.value, null, 2));
    edge.kill();
    process.exit(0);
  };
}
test().catch(e => { console.error(e); process.exit(1); });
