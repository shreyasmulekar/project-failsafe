with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update updateMissionBanner to call updateNexusDashboard and updateActiveClueDisplay
old_mission_banner = """        function updateMissionBanner(stageNum, chapterTitle, forensicObjective) {
      const banner = document.getElementById('active-mission-banner');
      if (!banner) return;
      banner.innerHTML = `
        <div style="color: var(--cyber-cyan); font-weight: 900; font-size: 11px; letter-spacing: 0.8px; display: flex; align-items: center; justify-content: space-between;">
          <span>🎯 [CHAPTER 0${stageNum}: ${chapterTitle}]</span>
          <span style="font-size: 9px; color: var(--tactical-green); border: 1px solid var(--tactical-green); padding: 1px 5px; border-radius: 2px;">ACTIVE SECTOR</span>
        </div>
        <div id="mission-objective-text" style="color: #ffffff; font-size: 12px; margin-top: 5px; line-height: 1.55;">
          <strong>OBJECTIVE:</strong> ${forensicObjective}
        </div>
        <div style="font-size: 10.5px; color: var(--text-dim); margin-top: 4px; border-left: 2px solid var(--cyber-cyan); padding-left: 6px;">
          &gt;&gt; <strong>AWAITING CLEARANCE:</strong> Isolate the cryptographic key from the evidence and enter <code>decrypt &lt;code&gt;</code> in Tactical Shell.
        </div>
      `;
    }"""

new_mission_banner = """        function updateMissionBanner(stageNum, chapterTitle, forensicObjective) {
      const banner = document.getElementById('active-mission-banner');
      if (!banner) return;
      banner.innerHTML = `
        <div style="color: var(--cyber-cyan); font-weight: 900; font-size: 11px; letter-spacing: 0.8px; display: flex; align-items: center; justify-content: space-between;">
          <span>🎯 [CHAPTER 0${stageNum}: ${chapterTitle}]</span>
          <span style="font-size: 9px; color: var(--tactical-green); border: 1px solid var(--tactical-green); padding: 1px 5px; border-radius: 2px;">ACTIVE SECTOR</span>
        </div>
        <div id="mission-objective-text" style="color: #ffffff; font-size: 12px; margin-top: 5px; line-height: 1.55;">
          <strong>OBJECTIVE:</strong> ${forensicObjective}
        </div>
        <div style="font-size: 10.5px; color: var(--text-dim); margin-top: 4px; border-left: 2px solid var(--cyber-cyan); padding-left: 6px;">
          &gt;&gt; <strong>AWAITING CLEARANCE:</strong> Isolate the cryptographic key from the evidence and enter <code>decrypt &lt;code&gt;</code> in Tactical Shell.
        </div>
      `;
      if (typeof updateNexusDashboard === 'function') {
        updateNexusDashboard();
      } else if (typeof updateActiveClueDisplay === 'function') {
        updateActiveClueDisplay();
      }
    }"""

if old_mission_banner in html:
    html = html.replace(old_mission_banner, new_mission_banner, 1)
    print("SUCCESS: updateMissionBanner updated to auto-refresh clue display.")
else:
    print("WARNING: old_mission_banner not found.")

# 2. In startTaraAmbientActivity, keep active clue reinforced
old_ambient = """        if (taraAmbientIdx === 0 && currentRound === 1) {
          text = `👁️ <strong>TARA SCANNING:</strong> Active at Sector 0${currentStage} (${stageInfo.chapter}). Target: <em>${stageInfo.targetText}</em>`;
        } else if (taraAmbientIdx === 4 && currentRound === 1) {
          text = `💡 <strong>TACTICAL LIFELINES:</strong> ${cluesRemaining}/3 clues available. Use wisely!`;
        }"""

new_ambient = """        if (cluesUsedStages && cluesUsedStages.has(currentStage) && stageInfo && stageInfo.hint && currentRound === 1) {
          text = `💡 <strong>ACTIVE CLUE:</strong> "${stageInfo.hint}"`;
        } else if (taraAmbientIdx === 0 && currentRound === 1) {
          text = `👁️ <strong>TARA SCANNING:</strong> Active at Sector 0${currentStage} (${stageInfo.chapter}). Target: <em>${stageInfo.targetText}</em>`;
        } else if (taraAmbientIdx === 4 && currentRound === 1) {
          text = `💡 <strong>TACTICAL LIFELINES:</strong> ${cluesRemaining}/3 clues available. Use wisely!`;
        }"""

if old_ambient in html:
    html = html.replace(old_ambient, new_ambient, 1)
    print("SUCCESS: startTaraAmbientActivity updated to prioritize active clue.")
else:
    print("WARNING: old_ambient not found.")

# 3. Ensure openModal updates clue display
old_open_modal = """      m.style.display = 'flex';
      m.classList.add('active-modal');
      m.scrollTop = 0;"""

new_open_modal = """      m.style.display = 'flex';
      m.classList.add('active-modal');
      m.scrollTop = 0;

      if (typeof updateActiveClueDisplay === 'function') {
        updateActiveClueDisplay();
      }"""

if old_open_modal in html:
    html = html.replace(old_open_modal, new_open_modal, 1)
    print("SUCCESS: openModal updated to refresh clue banner on open.")
else:
    print("WARNING: old_open_modal not found.")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: aditi_os_widget.html written.")
