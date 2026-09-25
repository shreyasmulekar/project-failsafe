with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """    function enforceRound2NoCluesProtocol() {
      if (currentRound >= 2) {"""

replacement = """    function enforceRound2NoCluesProtocol() {
      const activeRound = Math.max(currentRound || 1, parseInt(localStorage.getItem('failsafe_current_round') || '1', 10));
      if (activeRound >= 2) {"""

if target in content and replacement not in content:
    content = content.replace(target, replacement, 1)
    print("Updated enforceRound2NoCluesProtocol to check activeRound")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved aditi_os_widget.html")
