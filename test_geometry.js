const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function run() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9232',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9232/json', res => {
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
    await send('Page.enable');

    const geomRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          applyAuthenticatedTeam({
            team_id: 'TEAM-01',
            team_name: 'Test Team',
            current_stage: 1
          });

          openModal('modal-recovery');
          const m = document.getElementById('modal-recovery');
          const closeBtn = m.querySelector('.mil-modal-close');
          const rect = closeBtn.getBoundingClientRect();
          const cx = rect.left + rect.width / 2;
          const cy = rect.top + rect.height / 2;

          // Now see what elementFromPoint is before closing
          const elBefore = document.elementFromPoint(cx, cy);

          // Close modal
          closeModal('modal-recovery');

          // See what elementFromPoint is after closing at that exact point
          const elAfter = document.elementFromPoint(cx, cy);

          return {
            coords: { cx, cy },
            rect: { top: rect.top, left: rect.left, width: rect.width, height: rect.height },
            elBefore: elBefore ? { tag: elBefore.tagName, id: elBefore.id, className: elBefore.className } : null,
            elAfter: elAfter ? { tag: elAfter.tagName, id: elAfter.id, className: elAfter.className, text: elAfter.innerText } : null
          };
        })()
      `,
      returnByValue: true
    });

    console.log('Geometry analysis:', geomRes.result.value);
    edge.kill();
    process.exit(0);
  };
}

run().catch(e => { console.error(e); process.exit(1); });
