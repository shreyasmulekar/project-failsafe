const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const artifactDir = 'C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27';

async function run() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9230',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9230/json', res => {
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

    // Switch to Round 2 and render each puzzle
    const auditRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const authM = document.getElementById('team-auth-modal');
          if (authM) authM.style.display = 'none';
          
          launchRound2Arena();

          const results = [];
          for (let i = 1; i <= 15; i++) {
            round2CurrentStage = i;
            renderRound2Arena();
            
            const pz = ROUND2_PUZZLE_DATA[i];
            const input = document.getElementById('r2-passcode-input');
            const placeholder = input ? input.placeholder : '';
            const dirBanner = document.querySelector('.r2-puzzle-direction-banner');
            const dirText = dirBanner ? dirBanner.innerText.replace(/\\s+/g, ' ') : '';
            
            results.push({
              id: i,
              title: pz ? pz.title : '',
              placeholder,
              dirText
            });
          }
          return results;
        })()
      `,
      returnByValue: true
    });

    console.log('--- ROUND 2 ALL 15 PUZZLES AUDIT ---');
    const items = auditRes.result.value || [];
    for (const item of items) {
      console.log(`\nPUZZLE ${item.id < 10 ? '0' + item.id : item.id}: ${item.title}`);
      console.log(`  INPUT PLACEHOLDER: "${item.placeholder}"`);
      console.log(`  DIRECTIVES BANNER: "${item.dirText}"`);
    }

    // Capture screenshot of Round 2 Arena with Puzzle 01
    await send('Runtime.evaluate', {
      expression: `
        round2CurrentStage = 1;
        renderRound2Arena();
      `
    });
    await new Promise(r => setTimeout(r, 400));
    const ss1 = await send('Page.captureScreenshot');
    fs.writeFileSync(`${artifactDir}/round2_puzzle01_arena_verified.png`, Buffer.from(ss1.data, 'base64'));
    console.log('\nSaved round2_puzzle01_arena_verified.png');

    // Capture screenshot of Round 2 Arena with Puzzle 15
    await send('Runtime.evaluate', {
      expression: `
        round2CurrentStage = 15;
        renderRound2Arena();
      `
    });
    await new Promise(r => setTimeout(r, 400));
    const ss15 = await send('Page.captureScreenshot');
    fs.writeFileSync(`${artifactDir}/round2_puzzle15_arena_verified.png`, Buffer.from(ss15.data, 'base64'));
    console.log('Saved round2_puzzle15_arena_verified.png');

    edge.kill();
    process.exit(0);
  };
}

run().catch(e => {
  console.error('Audit error:', e);
  process.exit(1);
});
