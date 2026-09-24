# scratch/capture_stage1_proof.py
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
    
    # Open Stage 01 modal
    driver.execute_script("""
        const authModal = document.getElementById('team-auth-modal');
        if (authModal) authModal.style.display = 'none';
        currentTeam = { team_id: 'TEAM-01', team_name: 'Alpha Squad' };
        openModal('modal-recovery');
    """)
    time.sleep(1.5)
    
    modal_shot = os.path.join(ARTIFACT_DIR, "screenshot_stage1_guidance_and_submit.png")
    driver.save_screenshot(modal_shot)
    print("Saved Stage 1 modal screenshot:", modal_shot)

finally:
    driver.quit()
