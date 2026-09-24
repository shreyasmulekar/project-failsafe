const { spawn } = require('child_process');
const http = require('http');

async function test() {
  const edge = spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', [
    '--remote-debugging-port=9235',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  await new Promise(r => setTimeout(r, 1500));
  const tabs = await new Promise((res, rej) => http.get('http://localhost:9235/json', r => {
    let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
  }));
  const ws = new globalThis.WebSocket(tabs[0].webSocketDebuggerUrl);
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
    const r = await send('Runtime.evaluate', {
      expression: `
        (() => {
          openModal('modal-recovery');
          const m = document.getElementById('modal-recovery');
          const rect = m.getBoundingClientRect();
          const closeBtn = m.querySelector('.mil-modal-close');
          const closeRect = closeBtn ? closeBtn.getBoundingClientRect() : null;
          return {
            modalRect: { top: rect.top, left: rect.left, width: rect.width, height: rect.height },
            closeRect: closeRect ? { top: closeRect.top, left: closeRect.left, width: closeRect.width, height: closeRect.height } : null,
            classes: m.className
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Modal & Close Button Rect:', r.result.value);
    edge.kill();
  };
}
test().catch(console.error);
