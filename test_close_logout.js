const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function run() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9231',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9231/json', res => {
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

    // 1. Authenticate team
    const authRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          // Log in with team
          applyAuthenticatedTeam({
            team_id: 'TEAM-01',
            team_name: 'Test Team',
            current_stage: 1
          });

          // Check modals state
          const authModal = document.getElementById('team-auth-modal');
          const proctorOverlay = document.getElementById('proctor-lockdown-overlay');
          return {
            authModalDisplay: authModal ? authModal.style.display : null,
            proctorDisplay: proctorOverlay ? proctorOverlay.style.display : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Post-auth state:', authRes.result.value);

    // 2. Open a modal
    const openRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          openModal('modal-recovery');
          const m = document.getElementById('modal-recovery');
          return {
            modalVisible: m.classList.contains('active-modal'),
            rect: m.getBoundingClientRect()
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Open modal state:', openRes.result.value);

    // 3. Click the close button
    const clickRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const m = document.getElementById('modal-recovery');
          const closeBtn = m.querySelector('.mil-modal-close');
          console.log('Clicking closeBtn:', closeBtn);
          if (closeBtn) closeBtn.click();
          
          const authModal = document.getElementById('team-auth-modal');
          const proctorOverlay = document.getElementById('proctor-lockdown-overlay');
          return {
            modalVisibleAfter: m.classList.contains('active-modal'),
            authModalDisplay: authModal ? authModal.style.display : null,
            authModalComputed: authModal ? window.getComputedStyle(authModal).display : null,
            proctorDisplay: proctorOverlay ? proctorOverlay.style.display : null,
            proctorActive: typeof proctorLockActive !== 'undefined' ? proctorLockActive : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('After close click state:', clickRes.result.value);

    // Also test modal-memory
    const testMemory = await send('Runtime.evaluate', {
      expression: `
        (() => {
          openModal('modal-memory');
          const m = document.getElementById('modal-memory');
          const closeBtn = m.querySelector('.mil-modal-close');
          if (closeBtn) closeBtn.click();
          
          const authModal = document.getElementById('team-auth-modal');
          return {
            authModalDisplay: authModal ? authModal.style.display : null,
            authModalComputed: authModal ? window.getComputedStyle(authModal).display : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('After modal-memory close click:', testMemory.result.value);

    edge.kill();
    process.exit(0);
  };
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
