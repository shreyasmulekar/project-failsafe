import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("toggleR2Switch in text?", 'toggleR2Switch' in text)
# Add toggleR2Switch function if not present
if 'toggleR2Switch' not in text:
    switch_func = '''
    // R2 Stage 17: Interactive Relay Switch Logic
    let r2SwitchStates = { alpha: 0, beta: 1, gamma: 1, delta: 0 };
    function toggleR2Switch(name) {
      r2SwitchStates[name] = r2SwitchStates[name] === 1 ? 0 : 1;
      const valEl = document.getElementById(`val-${name}`);
      const btnEl = document.getElementById(`switch-${name}`);
      if (valEl && btnEl) {
        const is1 = r2SwitchStates[name] === 1;
        valEl.innerText = is1 ? '1' : '0';
        valEl.style.color = is1 ? '#22c55e' : '#ef4444';
        btnEl.style.borderColor = is1 ? '#22c55e' : '#64748b';
        const sub = btnEl.querySelector('div:last-child');
        if (sub) {
          sub.innerText = is1 ? 'ON' : 'OFF';
          sub.style.color = is1 ? '#22c55e' : '#64748b';
        }
      }
      const code = `${r2SwitchStates.alpha}${r2SwitchStates.beta}${r2SwitchStates.gamma}${r2SwitchStates.delta}`;
      const inp = document.getElementById('r2-modal-passcode-input');
      if (inp) inp.value = code;
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playKeyClick) {
        tacticalSound.playKeyClick();
      }
    }
    window.toggleR2Switch = toggleR2Switch;
'''
    idx_script = text.find('</script>')
    text = text[:idx_script] + switch_func + text[idx_script:]
    with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added toggleR2Switch helper function")
