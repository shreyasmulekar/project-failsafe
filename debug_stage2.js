const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function run() {
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9226',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,900',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  
  await new Promise(r => setTimeout(r, 2000));
  
  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9226/json', res => {
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
    await send('Console.enable');
    
    ws.addEventListener('message', (ev) => {
      const data = JSON.parse(ev.data);
      if (data.method === 'Runtime.consoleAPICalled') {
        console.log('CONSOLE:', data.params.type, data.params.args.map(a => a.value || a.description).join(' '));
      }
      if (data.method === 'Runtime.exceptionThrown') {
        console.error('EXCEPTION:', data.params.exceptionDetails.text, data.params.exceptionDetails.exception);
      }
    });
    
    // Evaluate in page context
    const code = `
      try {
        const authM = document.getElementById('team-auth-modal');
        if (authM) authM.style.display = 'none';
        window.localStorage.setItem('failsafe_auth', 'TEAM-01');
        window.localStorage.setItem('failsafe_team_id', '1');
        window.localStorage.setItem('failsafe_stage', '2');
        currentStage = 2;
        currentRound = 1;
        openModal('modal-memory');
        const box = document.getElementById('v1-memory-cards-box');
        const cardsCount = box ? box.children.length : 0;
        const html = box ? box.innerHTML : 'no box';
        ({ cardsCount, htmlPreview: html.substring(0, 200) });
      } catch (err) {
        ({ error: err.message, stack: err.stack });
      }
    `;
    
    const res = await send('Runtime.evaluate', {
      expression: code,
      returnByValue: true
    });
    console.log('Open modal evaluate:', JSON.stringify(res, null, 2));
    
    await new Promise(r => setTimeout(r, 500));
    
    // Check buttons and test clicking
    const testClickCode = `
      try {
        const box = document.getElementById('v1-memory-cards-box');
        const upBtns = document.querySelectorAll('.btn-mem-shift-up');
        const dnBtns = document.querySelectorAll('.btn-mem-shift-dn');
        const initialOrder = v1MemOrder.map(m => m.time);
        
        // Click first down button
        let clickResult = 'no button';
        if (dnBtns.length > 0) {
          dnBtns[0].click();
          clickResult = 'clicked dnBtn[0]';
        }
        const afterOrder = v1MemOrder.map(m => m.time);
        ({ upCount: upBtns.length, dnCount: dnBtns.length, initialOrder, afterOrder, clickResult });
      } catch (err) {
        ({ error: err.message, stack: err.stack });
      }
    `;
    const clickRes = await send('Runtime.evaluate', {
      expression: testClickCode,
      returnByValue: true
    });
    console.log('Click test evaluate:', JSON.stringify(clickRes, null, 2));
    
    // Now let's check what is in modal-memory below the cards
    const checkBottomCode = `
      (() => {
        const modal = document.getElementById('modal-memory');
        const body = modal ? modal.querySelector('.mil-modal-body') : null;
        if (!body) return 'no body';
        const children = Array.from(body.children).map(c => ({
          tag: c.tagName,
          id: c.id,
          class: c.className,
          textPreview: c.innerText.substring(0, 80).replace(/\\n/g, ' ')
        }));
        return { children };
      })()
    `;
    const bottomRes = await send('Runtime.evaluate', {
      expression: checkBottomCode,
      returnByValue: true
    });
    console.log('Bottom elements:', JSON.stringify(bottomRes, null, 2));

    // Also check for any errors when clicking submit or sorting
    const sortAllCode = `
      (() => {
        v1MemOrder.sort((a,b) => a.min - b.min);
        renderV1MemoryCards();
        const fixedBlock = document.getElementById('v1-timeline-fixed-block');
        const pendingBlock = document.getElementById('v1-timeline-pending-block');
        return {
          fixedBlock: !!fixedBlock,
          pendingBlock: !!pendingBlock,
          fixedBlockHtml: fixedBlock ? fixedBlock.innerHTML : null
        };
      })()
    `;
    const sortRes = await send('Runtime.evaluate', {
      expression: sortAllCode,
      returnByValue: true
    });
    console.log('Sort all test:', JSON.stringify(sortRes, null, 2));
    
    const ss = await send('Page.captureScreenshot');
    fs.writeFileSync('C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/stage2_cdp_debug.png', Buffer.from(ss.data, 'base64'));
    
    edge.kill();
    process.exit(0);
  };
}

run().catch(e => { console.error(e); process.exit(1); });
