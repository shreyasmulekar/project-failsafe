with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """      const ethanClueBtn = document.getElementById('btn-ethan-clue');
      if (ethanClueBtn) {
        if (cluesRemaining <= 0) {
          ethanClueBtn.innerHTML = `🚫 NO CLUES (0/3)`;
          ethanClueBtn.style.borderColor = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.color = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.opacity = "0.7";
        } else {
          ethanClueBtn.innerHTML = `💡 USE CLUE (${cluesRemaining}/3 | +2m)`;
          ethanClueBtn.title = `Expend a Tactical Clue (+2:00 Time Penalty added to running clock)`;
          ethanClueBtn.style.borderColor = "var(--cyber-cyan)";
          ethanClueBtn.style.color = "var(--cyber-cyan)";
          ethanClueBtn.style.opacity = "1";
        }
      }"""

replacement = """      const ethanClueBtn = document.getElementById('btn-ethan-clue');
      if (ethanClueBtn) {
        if (typeof cluesUsedStages !== 'undefined' && cluesUsedStages && cluesUsedStages.has(currentStage)) {
          ethanClueBtn.innerHTML = `💡 VIEW CLUE (ACTIVE)`;
          ethanClueBtn.title = `Click to re-open the tactical clue popup for Stage ${currentStage}`;
          ethanClueBtn.style.borderColor = "#ffd700";
          ethanClueBtn.style.color = "#ffd700";
          ethanClueBtn.style.boxShadow = "0 0 12px rgba(255,215,0,0.5)";
          ethanClueBtn.style.opacity = "1";
        } else if (cluesRemaining <= 0) {
          ethanClueBtn.innerHTML = `🚫 NO CLUES (0/3)`;
          ethanClueBtn.style.borderColor = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.color = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.boxShadow = "none";
          ethanClueBtn.style.opacity = "0.7";
        } else {
          ethanClueBtn.innerHTML = `💡 USE CLUE (${cluesRemaining}/3 | +2m)`;
          ethanClueBtn.title = `Expend a Tactical Clue (+2:00 Time Penalty added to running clock)`;
          ethanClueBtn.style.borderColor = "var(--cyber-cyan)";
          ethanClueBtn.style.color = "var(--cyber-cyan)";
          ethanClueBtn.style.boxShadow = "none";
          ethanClueBtn.style.opacity = "1";
        }
      }"""

if target in content:
    content = content.replace(target, replacement, 1)
    print("Replaced ethanClueBtn block successfully")
else:
    print("target block not found")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved aditi_os_widget.html")
