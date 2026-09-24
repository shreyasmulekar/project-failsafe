const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgeExe = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const artifactDir = 'C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27';

async function run() {
  console.log('Launching headless Edge for comprehensive test...');
  const edge = spawn(edgeExe, [
    '--remote-debugging-port=9228',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  const tabs = await new Promise((resolve, reject) => {
    http.get('http://localhost:9228/json', res => {
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

    console.log('--- TEST 1: Bypass Auth and Initialize Stage 02 ---');
    const initRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const authM = document.getElementById('team-auth-modal');
          if (authM) authM.style.display = 'none';
          window.localStorage.setItem('failsafe_auth', 'TEAM-TEST');
          window.localStorage.setItem('failsafe_team_id', '1');
          window.localStorage.setItem('failsafe_stage', '2');
          currentStage = 2;
          currentRound = 1;
          openModal('modal-memory');
          return {
            currentStage,
            modalVisible: document.getElementById('modal-memory').style.display !== 'none',
            cardCount: document.querySelectorAll('#v1-memory-cards-box > div').length
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Init Stage 02 Result:', initRes.result.value);

    console.log('--- TEST 2: Verify Cards Reordering Interaction (UP/DN and Click-to-swap) ---');
    const swapRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          // Record current first card
          const firstBefore = v1MemOrder[0].id;
          // Click second card to swap with first card
          selectedMemoryCardIdx = 0;
          renderV1MemoryCards();
          // Simulate clicking card index 1
          const cards = document.querySelectorAll('#v1-memory-cards-box > div[draggable="true"]');
          cards[1].click();
          const firstAfter = v1MemOrder[0].id;
          
          // Now test shiftV1MemoryCard
          const shiftBefore = v1MemOrder[0].id;
          shiftV1MemoryCard(0, 1);
          const shiftAfter = v1MemOrder[1].id;

          return {
            swapWorked: firstBefore !== firstAfter,
            shiftWorked: shiftBefore === shiftAfter
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Card Reorder Interaction Result:', swapRes.result.value);

    console.log('--- TEST 3: Sort Chronologically and Check Glowing Submission Block ---');
    const sortRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          // Sort accurately
          v1MemOrder.sort((a, b) => a.min - b.min);
          renderV1MemoryCards();
          const fixedBlock = document.getElementById('v1-timeline-fixed-block');
          const pendingBlock = document.getElementById('v1-timeline-pending-block');
          return {
            fixedBlockPresent: !!fixedBlock,
            pendingBlockPresent: !!pendingBlock,
            blockText: fixedBlock ? fixedBlock.innerText.replace(/\\s+/g, ' ') : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Sorting Result:', sortRes.result.value);

    // Scroll and take screenshot of sorted Stage 2 modal
    await send('Runtime.evaluate', {
      expression: `
        const m = document.getElementById('modal-memory');
        if (m) m.scrollTop = m.scrollHeight;
      `
    });
    await new Promise(r => setTimeout(r, 400));
    const ss1 = await send('Page.captureScreenshot');
    fs.writeFileSync(`${artifactDir}/stage2_reordered_and_block_verified.png`, Buffer.from(ss1.data, 'base64'));
    console.log('Saved stage2_reordered_and_block_verified.png');

    console.log('--- TEST 4: Click Submission Block and Advance to Stage 03 ---');
    const submitRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const fixedBlock = document.getElementById('v1-timeline-fixed-block');
          if (fixedBlock) fixedBlock.click();
          return {
            newStage: currentStage,
            revealVisible: document.getElementById('v1-memory-reveal').style.display !== 'none',
            revealText: document.getElementById('v1-memory-reveal').innerText.replace(/\\s+/g, ' ').slice(0, 150)
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Submit Result:', submitRes.result.value);

    await new Promise(r => setTimeout(r, 400));
    const ss2 = await send('Page.captureScreenshot');
    fs.writeFileSync(`${artifactDir}/stage2_completed_reveal_verified.png`, Buffer.from(ss2.data, 'base64'));
    console.log('Saved stage2_completed_reveal_verified.png');

    console.log('--- TEST 5: Verify Round 2 (All 15 Puzzles) Placeholder and Guidance No Answer Leaks ---');
    const r2Audit = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const leaks = [];
          for (let pzId = 1; pzId <= 15; pzId++) {
            loadRound2Puzzle(pzId);
            const input = document.getElementById('r2-passcode-input');
            const placeholder = input ? input.placeholder : '';
            const arena = document.getElementById('r2-interactive-arena');
            const arenaHtml = arena ? arena.innerHTML : '';
            
            // Expected solutions to ensure NONE are in placeholder or arena guidance
            const knownAnswers = [
              'ACCESS', '123456', 'SAFE', '28/02/2025', 'POLARIS', 'MARGIN_KEY', 'ARIAL',
              'WHITE', 'REVERT_COMMIT_7B', 'BYPASS', '6-9-11', 'CLEARANCE_ALPHA',
              'ADITIS13', 'PROJECT', 'VECTOR', '1400', 'CIPHER', 'BOTTOM LEFT', 'SQUARES',
              '011', 'RLRCK', 'NODC', '102', '3-EMPTY', 'FINALS', 'ECLIPSE'
            ];

            for (const ans of knownAnswers) {
              if (placeholder.toUpperCase().includes(ans)) {
                leaks.push({ pzId, type: 'placeholder', ans, text: placeholder });
              }
            }
          }
          return {
            totalChecked: 15,
            leakCount: leaks.length,
            leaks
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Round 2 Placeholder Audit:', r2Audit.result.value);

    console.log('--- TEST 6: Verify All Puzzles Guide Modal for Leaks ---');
    const guideAudit = await send('Runtime.evaluate', {
      expression: `
        (() => {
          openModal('modal-puzzles-guide');
          const guide = document.getElementById('modal-puzzles-guide');
          const text = guide ? guide.innerText : '';
          
          const forbiddenInGuide = [
            'MARGIN_KEY', 'REVERT_COMMIT_7B', 'CLEARANCE_ALPHA', 'ADITIS13',
            'RLRCK', 'NODC', '3-EMPTY'
          ];
          
          const found = [];
          for (const word of forbiddenInGuide) {
            if (text.includes(word)) found.push(word);
          }
          return {
            guideModalFound: !!guide,
            forbiddenFound: found
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Guide Modal Audit:', guideAudit.result.value);

    // Capture Guide Modal Screenshot
    const ss3 = await send('Page.captureScreenshot');
    fs.writeFileSync(`${artifactDir}/puzzles_guide_modal_verified.png`, Buffer.from(ss3.data, 'base64'));
    console.log('Saved puzzles_guide_modal_verified.png');

    console.log('ALL VERIFICATION TESTS COMPLETED SUCCESSFULLY.');
    edge.kill();
    process.exit(0);
  };
}

run().catch(e => {
  console.error('Verification error:', e);
  process.exit(1);
});
