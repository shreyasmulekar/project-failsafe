const { spawn } = require('child_process');
const http = require('http');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function test() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9236',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));
  const tabs = await new Promise((res, rej) => http.get('http://localhost:9236/json', r => {
    let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
  }));
  const page = tabs.find(t => t.type === 'page' && t.url.includes('localhost')) || tabs.find(t => t.type === 'page');
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

    // Authenticate team
    await send('Runtime.evaluate', {
      expression: `
        applyAuthenticatedTeam({
          team_id: 'TEAM-01',
          team_name: 'Test Team',
          current_stage: 16
        });
      `
    });

    const modalIds = [
      'modal-recovery', 'modal-memory', 'modal-acrostic', 'modal-incident-logs',
      'modal-clearance', 'modal-comments', 'modal-font', 'modal-spectro',
      'modal-version-hist', 'modal-honeypot', 'modal-failsafe', 'modal-whiteout',
      'modal-rot4', 'modal-atbash', 'modal-polybius', 'modal-frequency'
    ];

    console.log('Testing coordinate clicks on all 16 modals close buttons...');
    for (const mId of modalIds) {
      // 1. Open modal
      await send('Runtime.evaluate', { expression: `openModal('${mId}')` });
      await new Promise(r => setTimeout(r, 100));

      // 2. Get close button coordinates
      const res = await send('Runtime.evaluate', {
        expression: `
          (() => {
            const m = document.getElementById('${mId}');
            if (!m) return { error: 'Modal not found' };
            const closeBtn = m.querySelector('.mil-modal-close') || m.querySelector('.btn-dossier-back');
            if (!closeBtn) return { error: 'No close button' };
            const r = closeBtn.getBoundingClientRect();
            return {
              x: Math.round(r.left + r.width / 2),
              y: Math.round(r.top + r.height / 2),
              visible: m.classList.contains('active-modal'),
              btnClass: closeBtn.className,
              rect: { top: r.top, left: r.left, width: r.width, height: r.height }
            };
          })()
        `,
        returnByValue: true
      });

      const info = res.result.value;
      if (info.error) {
        console.log(`${mId}: ${info.error}`);
        continue;
      }

      // Check elementFromPoint at those exact coordinates
      const hitTest = await send('Runtime.evaluate', {
        expression: `
          (() => {
            const el = document.elementFromPoint(${info.x}, ${info.y});
            return el ? { tag: el.tagName, id: el.id, className: el.className } : null;
          })()
        `,
        returnByValue: true
      });

      // 3. Dispatch actual mouse click
      await send('Input.dispatchMouseEvent', {
        type: 'mousePressed',
        x: info.x,
        y: info.y,
        button: 'left',
        clickCount: 1
      });
      await send('Input.dispatchMouseEvent', {
        type: 'mouseReleased',
        x: info.x,
        y: info.y,
        button: 'left',
        clickCount: 1
      });

      await new Promise(r => setTimeout(r, 150));

      // 4. Check state after click
      const postState = await send('Runtime.evaluate', {
        expression: `
          (() => {
            const m = document.getElementById('${mId}');
            const authModal = document.getElementById('team-auth-modal');
            const proctorOverlay = document.getElementById('proctor-lockdown-overlay');
            return {
              modalClosed: !m.classList.contains('active-modal'),
              authModalVisible: authModal && authModal.style.display !== 'none',
              proctorVisible: proctorOverlay && proctorOverlay.style.display !== 'none'
            };
          })()
        `,
        returnByValue: true
      });

      console.log(`${mId}: hit=${hitTest.result.value.className} (x:${info.x}, y:${info.y}), closed=${postState.result.value.modalClosed}, authVisible=${postState.result.value.authModalVisible}, proctorVisible=${postState.result.value.proctorVisible}`);
    }

    edge.kill();
    process.exit(0);
  };
}

test().catch(e => { console.error(e); process.exit(1); });
