# scratch/test_stage2_and_guide.py
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1400,900")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://localhost:8000/aditi_os_widget.html")
    time.sleep(2)

    # 1. Close auth modal and set team session
    driver.execute_script("""
        const auth = document.getElementById('team-auth-modal');
        if (auth) auth.style.display = 'none';
        currentTeam = { team_id: 'TEAM-01', team_name: 'Alpha Cyber Unit' };
        currentStage = 2;
        updateNexusDashboard();
        openModal('modal-memory');
    """)
    time.sleep(1)

    # 2. Sort the timeline in chronological order
    driver.execute_script("""
        // Set v1MemOrder to strict sorted order
        v1MemOrder.sort((a, b) => a.min - b.min);
        renderV1MemoryCards();
    """)
    time.sleep(1)

    shot1 = os.path.join(ARTIFACT_DIR, "screenshot_stage2_timeline_submission_block.png")
    driver.save_screenshot(shot1)
    print("Saved Stage 2 submission block screenshot:", shot1)

    # 3. Open All Puzzles Guide Modal
    driver.execute_script("""
        closeModal('modal-memory');
        openModal('modal-puzzles-guide');
    """)
    time.sleep(1)

    shot2 = os.path.join(ARTIFACT_DIR, "screenshot_all_puzzles_guide_modal.png")
    driver.save_screenshot(shot2)
    print("Saved All Puzzles Guide modal screenshot:", shot2)

finally:
    driver.quit()
