
    function switchGuideTab(tab) {
      const r1Cont = document.getElementById('guide-container-r1');
      const r2Cont = document.getElementById('guide-container-r2');
      const t1 = document.getElementById('tab-guide-r1');
      const t2 = document.getElementById('tab-guide-r2');
      if (tab === 'r1') {
        if (r1Cont) r1Cont.style.display = 'flex';
        if (r2Cont) r2Cont.style.display = 'none';
        if (t1) { t1.style.background = '#00f0ff'; t1.style.color = '#02060e'; t1.style.border = 'none'; }
        if (t2) { t2.style.background = 'rgba(255,255,255,0.06)'; t2.style.color = '#cbd5e1'; t2.style.border = '1px solid #334155'; }
      } else {
        if (r1Cont) r1Cont.style.display = 'none';
        if (r2Cont) r2Cont.style.display = 'flex';
        if (t2) { t2.style.background = '#ff003c'; t2.style.color = '#ffffff'; t2.style.border = 'none'; }
        if (t1) { t1.style.background = 'rgba(255,255,255,0.06)'; t1.style.color = '#cbd5e1'; t1.style.border = '1px solid #334155'; }
      }
    }
  