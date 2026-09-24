# scratch/capture_test_mode_proof.py
import time
import os
import urllib.request, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

# First trigger unlock_all via API
req = urllib.request.Request(
    "http://localhost:8000/api/admin/levels/unlock_all",
    data=json.dumps({"pin": "wie-admin-2026", "team_id": "ALL"}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
with urllib.request.urlopen(req) as resp:
    print("API unlock all:", json.loads(resp.read().decode('utf-8')))

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1400,900")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://localhost:8000/aditi_os_widget.html")
    time.sleep(2.5)
    
    # Bypass auth and open Stage 03 modal
    driver.execute_script("""
        const authModal = document.getElementById('team-auth-modal');
        if (authModal) authModal.style.display = 'none';
        currentTeam = { team_id: 'TEAM-01', team_name: 'Alpha Squad' };
        handleUnlockAllLevelsTriggered();
        openModal('modal-acrostic');
    """)
    time.sleep(1.5)
    
    modal_shot = os.path.join(ARTIFACT_DIR, "screenshot_test_mode_stage3_unlocked.png")
    driver.save_screenshot(modal_shot)
    print("Saved test mode Stage 3 screenshot:", modal_shot)

    # Now lock all levels back via API
    req_lock = urllib.request.Request(
        "http://localhost:8000/api/admin/levels/lock_all",
        data=json.dumps({"pin": "wie-admin-2026", "team_id": "ALL"}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req_lock) as resp:
        print("API lock all:", json.loads(resp.read().decode('utf-8')))

    # Clear broadcasts
    req_clear = urllib.request.Request(
        "http://localhost:8000/api/admin/broadcast/clear",
        data=json.dumps({"pin": "wie-admin-2026"}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req_clear) as resp:
        print("API clear broadcasts:", json.loads(resp.read().decode('utf-8')))

finally:
    driver.quit()
