const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const artifactDir = 'C:\\Users\\shrey\\.gemini\\antigravity\\brain\\17c36665-51d0-4b98-8e9d-7e8fd18fcd27';

async function run() {
  const port = 9380;
  const edge = spawn(edgeExe, [
    `--remote-debugging-port=${port}`,
    '--headless',
    '--disable-gpu',
    '--window-size=1280,720',
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

  ws.onopen = async () => {
    await send('Runtime.enable');
    await send('Page.enable');

    console.log('--- 1. Authenticating team & Checking initial timer ---');
    const initRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          localStorage.clear();
          applyAuthenticatedTeam({
            team_id: 'TEAM-01',
            team_name: 'Alpha Squadron',
            current_stage: 1
          });
          updateMissionTimerDisplay();
          const timerEl = document.getElementById('nexus-live-mission-timer');
          const penaltyEl = document.getElementById('nexus-penalty-badge');
          return {
            team: currentTeam.team_id,
            elapsedSec: getMissionElapsedSeconds(),
            timerText: timerEl ? timerEl.innerText : null,
            penaltyVisible: penaltyEl ? (penaltyEl.style.display !== 'none') : false
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Initial Timer State:', initRes.result.value);

    console.log('\n--- 2. Clicking DO_NOT_RUN.exe (Card 10) ---');
    const trapRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const cardTrap = document.getElementById('card-trap');
          if (cardTrap) cardTrap.click();
          
          updateMissionTimerDisplay();
          const timerEl = document.getElementById('nexus-live-mission-timer');
          const penaltyEl = document.getElementById('nexus-penalty-badge');
          const penaltySec = parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);
          const elapsedSec = getMissionElapsedSeconds();
          const lockdownOverlay = document.getElementById('lockdown-overlay');

          return {
            penaltySec,
            elapsedSec,
            timerText: timerEl ? timerEl.innerText : null,
            penaltyBadgeText: penaltyEl ? penaltyEl.innerText : null,
            penaltyBadgeDisplay: penaltyEl ? penaltyEl.style.display : null,
            lockdownVisible: lockdownOverlay ? (lockdownOverlay.style.display !== 'none') : false
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Post-Trap State:', trapRes.result.value);

    // Wait for the lockdown animation to complete (1200ms)
    await new Promise(r => setTimeout(r, 1400));

    const ssLockdown = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path.join(artifactDir, 'do_not_run_penalty_verified.png'), Buffer.from(ssLockdown.data, 'base64'));
    console.log('Saved do_not_run_penalty_verified.png');

    console.log('\n--- 3. Dismissing Lockdown Overlay and checking persistent timer ---');
    const rebootRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          closeLockdown();
          updateMissionTimerDisplay();
          const timerEl = document.getElementById('nexus-live-mission-timer');
          const penaltyEl = document.getElementById('nexus-penalty-badge');
          const lockdownOverlay = document.getElementById('lockdown-overlay');
          return {
            lockdownDismissed: lockdownOverlay ? (lockdownOverlay.style.display === 'none') : true,
            elapsedSec: getMissionElapsedSeconds(),
            timerText: timerEl ? timerEl.innerText : null,
            penaltyBadgeText: penaltyEl ? penaltyEl.innerText : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Reboot State:', rebootRes.result.value);

    console.log('\n--- 4. Testing Responsive Fitting across Laptop Viewports ---');
    const testViewports = [
      { name: '1280x720 (Small Budget Laptop / 150% Scale)', width: 1280, height: 720 },
      { name: '1366x768 (Standard 14" College Lab Laptop)', width: 1366, height: 768 },
      { name: '1440x900 (MacBook Air 13")', width: 1440, height: 900 },
      { name: '1536x864 (Windows 1080p @ 125% Scale)', width: 1536, height: 864 },
      { name: '1920x1080 (Large 15.6"+ FHD Laptop)', width: 1920, height: 1080 }
    ];

    for (const vp of testViewports) {
      await send('Emulation.setDeviceMetricsOverride', {
        width: vp.width,
        height: vp.height,
        deviceScaleFactor: 1,
        mobile: false
      });
      await new Promise(r => setTimeout(r, 300));

      const vpMetrics = await send('Runtime.evaluate', {
        expression: `
          (() => {
            const doc = document.documentElement;
            const body = document.body;
            const header = document.querySelector('.nexus-header');
            const container = document.querySelector('.nexus-dashboard-container');
            const cards = document.querySelectorAll('.nexus-clean-card');
            
            // Open modal to verify modal fit
            openModal('modal-recovery');
            const modal = document.getElementById('modal-recovery');
            const modalH = modal ? modal.offsetHeight : 0;
            const modalW = modal ? modal.offsetWidth : 0;
            closeModal('modal-recovery');

            return {
              hasHScrollDoc: doc.scrollWidth > doc.clientWidth,
              hasHScrollBody: body.scrollWidth > body.clientWidth,
              headerHeight: header ? header.offsetHeight : 0,
              modalH,
              modalW,
              modalFitsV: modalH <= (window.innerHeight * 0.94),
              modalFitsH: modalW <= (window.innerWidth * 0.96),
              totalCards: cards.length
            };
          })()
        `,
        returnByValue: true
      });

      const m = vpMetrics.result.value;
      const hScrollOk = !m.hasHScrollDoc && !m.hasHScrollBody;
      const modalOk = m.modalFitsV && m.modalFitsH;
      console.log(`[${vp.name}]`);
      console.log(`  Horizontal Fit: ${hScrollOk ? '✅ PERFECT (0 overflow)' : '❌ OVERFLOW'}`);
      console.log(`  Modal Fit (${m.modalW}x${m.modalH}): ${modalOk ? '✅ FITS VIEWPORT' : '❌ EXCEEDS VIEWPORT'}`);
      console.log(`  Cards Visible: ${m.totalCards}/16`);

      if (vp.width === 1280 || vp.width === 1366) {
        const ss = await send('Page.captureScreenshot', { format: 'png' });
        const ssFile = path.join(artifactDir, `laptop_${vp.width}x${vp.height}_responsive.png`);
        fs.writeFileSync(ssFile, Buffer.from(ss.data, 'base64'));
        console.log(`  Saved screenshot: ${ssFile}`);
      }
    }

    edge.kill();
    process.exit(0);
  };
}

run().catch(e => {
  console.error(e);
  process.exit(1);
});
