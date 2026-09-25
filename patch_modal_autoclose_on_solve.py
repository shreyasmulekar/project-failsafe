with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

old_func = """    function recordStageCleared(stageNum) {
      const now = Date.now();"""

new_func = """    function recordStageCleared(stageNum) {
      // Auto-close completed stage evidence modal to reveal newly unlocked stage
      document.querySelectorAll('.mil-modal.active-modal, .evidence-modal').forEach(m => {
        if (m.id !== 'team-auth-modal' && m.id !== 'proctor-lockdown-overlay' && m.id !== 'victory-celebration-modal') {
          m.style.display = 'none';
          m.classList.remove('active-modal');
        }
      });

      const now = Date.now();"""

if old_func in html:
    html = html.replace(old_func, new_func, 1)
    print("SUCCESS: recordStageCleared updated with modal auto-close.")
else:
    print("WARNING: old_func not found.")

# Also ensure recordStageCleared triggers updateNexusDashboard
old_end = """      localStorage.setItem('failsafe_stage_times', JSON.stringify(stageTimes));
      return stageTimes;
    }"""

new_end = """      localStorage.setItem('failsafe_stage_times', JSON.stringify(stageTimes));
      if (typeof updateNexusDashboard === 'function') {
        setTimeout(updateNexusDashboard, 50);
      }
      return stageTimes;
    }"""

if old_end in html:
    html = html.replace(old_end, new_end, 1)
    print("SUCCESS: recordStageCleared updated to refresh dashboard & clue banner.")
else:
    print("WARNING: old_end not found.")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: aditi_os_widget.html saved.")
