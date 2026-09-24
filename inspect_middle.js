const { spawn } = require('child_process');
const http = require('http');

async function test() {
  const edge = spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', [
    '--remote-debugging-port=9241',
    '--headless',
    '--disable-gpu',
    '--window-size=1400,950',
    'http://localhost:8000/aditi_os_widget.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));
  const tabs = await new Promise(res => http.get('http://localhost:9241/json', r => {
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
    const r = await send('Runtime.evaluate', {
      expression: `
        (() => {
          applyAuthenticatedTeam({ team_id: 'TEAM-01' });
          const el = document.elementFromPoint(500, 300);
          const el2 = document.elementFromPoint(500, 600);
          
          function getAncestors(node) {
            const list = [];
            while (node && node !== document.body) {
              list.push({ tag: node.tagName, id: node.id, className: node.className, display: window.getComputedStyle(node).display });
              node = node.parentElement;
            }
            return list;
          }

          return {
            at300: el ? { tag: el.tagName, id: el.id, className: el.className, text: el.innerText ? el.innerText.slice(0, 100) : '', chain: getAncestors(el) } : null,
            at600: el2 ? { tag: el2.tagName, id: el2.id, className: el2.className, text: el2.innerText ? el2.innerText.slice(0, 100) : '', chain: getAncestors(el2) } : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log('Result:', JSON.stringify(r.result.value, null, 2));
    edge.kill();
    process.exit(0);
  };
}
test().catch(e => { console.error(e); process.exit(1); });
