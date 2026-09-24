# scratch/capture_proofs.py
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1400,900")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Capture admin.html with new buttons
    driver.get("http://localhost:8000/admin.html")
    time.sleep(2)
    try:
        driver.execute_script("""
            localStorage.setItem('failsafe_admin_auth', 'true');
            const pinModal = document.getElementById('modal-admin-pin');
            if (pinModal) pinModal.style.display = 'none';
            fetchLeaderboardData();
        """)
        time.sleep(1)
    except:
        pass
    
    admin_shot = os.path.join(ARTIFACT_DIR, "screenshot_admin_test_controls.png")
    driver.save_screenshot(admin_shot)
    print("Saved admin screenshot:", admin_shot)

    # 2. Capture aditi_os_widget.html with Stage 03 modal open
    driver.get("http://localhost:8000/aditi_os_widget.html")
    time.sleep(2)
    
    # Bypass auth modal and open modal-acrostic (Stage 3)
    driver.execute_script("""
        const authModal = document.getElementById('team-auth-modal');
        if (authModal) authModal.style.display = 'none';
        currentTeam = { team_id: 'TEAM-ALPHA', team_name: 'Cyber Unit Alpha' };
        openModal('modal-acrostic');
    """)
    time.sleep(1.5)
    
    modal_shot = os.path.join(ARTIFACT_DIR, "screenshot_stage3_guidance_and_submit.png")
    driver.save_screenshot(modal_shot)
    print("Saved Stage 3 modal screenshot:", modal_shot)

    # 3. Capture Round 2 with no clues
    driver.execute_script("""
        closeModal('modal-acrostic');
        currentRound = 2;
        round2CurrentStage = 1;
        launchRound2Arena();
    """)
    time.sleep(1.5)
    
    r2_shot = os.path.join(ARTIFACT_DIR, "screenshot_round2_no_clues_guidance.png")
    driver.save_screenshot(r2_shot)
    print("Saved Round 2 screenshot:", r2_shot)

finally:
    driver.quit()
    print("Done capturing proofs.")
