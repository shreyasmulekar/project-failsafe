import sys
sys.stdout.reconfigure(encoding='utf-8')
import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "http://localhost:8000"

def post(endpoint, data):
    req = urllib.request.Request(
        f"{BASE}{endpoint}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode('utf-8'))

def run_test():
    team_name = "Clue Popup Verification Squad"
    team_id = f"CLUE-POPUP-{int(time.time())}"

    # Register team
    post("/api/teams/register", {
        "team_id": team_id,
        "team_name": team_name,
        "password": "pass",
        "leader_name": "Dr. Clue"
    })
    post("/api/admin/start_round_1", {"pin": "wie-admin-2026"})

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(BASE)
        time.sleep(2)

        # Set session
        driver.execute_script(f"""
            localStorage.clear();
            sessionStorage.clear();
            localStorage.setItem('failsafe_current_team', JSON.stringify({{
                team_name: '{team_name}',
                team_id: '{team_id}'
            }}));
            localStorage.setItem('failsafe_current_round', '1');
            localStorage.setItem('failsafe_current_stage', '1');
            localStorage.setItem('failsafe_stage', '1');
            localStorage.setItem('failsafe_clues_left', '3');
            localStorage.setItem('failsafe_clues_used_stages', '[]');
            location.reload();
        """)
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nexus-cards-grid"))
        )
        print("Workstation loaded.")

        # 1. Open Stage 1 modal
        print("Opening Stage 01 modal...")
        driver.execute_script("openActiveStageModal(1);")
        time.sleep(1)

        # 2. Trigger Clue Request & Confirm
        print("Requesting clue...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(1)

        print("Confirming clue expenditure (+2m penalty)...")
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(1)

        # 3. Verify Dedicated Clue Popup is open!
        popup_info = driver.execute_script("""
            const p = document.getElementById('modal-active-clue-popup');
            const style = window.getComputedStyle(p);
            return {
                display: style.display,
                zIndex: style.zIndex,
                title: document.getElementById('clue-popup-stage-title')?.innerText,
                body: document.getElementById('clue-popup-body-text')?.innerText,
                lifelines: document.getElementById('clue-popup-lifelines-left')?.innerText
            };
        """)
        print("Clue Popup Info:", json.dumps(popup_info, indent=2))
        assert popup_info['display'] != 'none', "Dedicated Clue Popup must be visible!"
        assert popup_info['zIndex'] == '100000', f"Expected zIndex 100000, got {popup_info['zIndex']}"
        assert "ORIGIN" in popup_info['body'], f"Expected clue text in popup body, got: {popup_info['body']}"

        # 4. CRITICAL: Test that it stays open longer than 5 seconds!
        print("Waiting 6 seconds to prove popup does NOT disappear...")
        time.sleep(6)
        is_still_open = driver.execute_script("""
            const p = document.getElementById('modal-active-clue-popup');
            return window.getComputedStyle(p).display !== 'none';
        """)
        print(f"Is Clue Popup still open after 6 seconds? {is_still_open}")
        assert is_still_open, "Clue Popup must remain open and NOT disappear after 5 seconds!"
        driver.save_screenshot("shot_clue_popup_open_unlimited.png")
        print("Saved screenshot: shot_clue_popup_open_unlimited.png")

        # 5. Minimize / Close the Popup
        print("Minimizing / Closing Clue Popup...")
        driver.execute_script("closeModal('modal-active-clue-popup');")
        time.sleep(1)

        # 6. Verify companion button now shows "VIEW CLUE (ACTIVE)"
        btn_text = driver.execute_script("return document.getElementById('btn-ethan-clue')?.innerText || ''")
        print(f"Companion Button text while clue active: '{btn_text}'")
        assert "VIEW CLUE" in btn_text, f"Expected VIEW CLUE in button text, got: {btn_text}"

        # 7. Re-open clue popup anytime!
        print("Clicking VIEW CLUE (ACTIVE) to re-open popup anytime...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(1)

        is_reopened = driver.execute_script("""
            const p = document.getElementById('modal-active-clue-popup');
            return window.getComputedStyle(p).display !== 'none';
        """)
        print(f"Is Clue Popup re-opened successfully? {is_reopened}")
        assert is_reopened, "Clue Popup must re-open when requested anytime!"
        driver.save_screenshot("shot_clue_popup_reopened_anytime.png")
        print("Saved screenshot: shot_clue_popup_reopened_anytime.png")

        # 8. Solve Stage 01 (ORIGIN)
        print("Submitting key 'ORIGIN' to clear Stage 01...")
        driver.execute_script("submitStageDirectKey(1, 'ORIGIN');")
        time.sleep(3)

        # 9. Verify Clue Popup and Banner are cleared for Stage 02!
        after_solve = driver.execute_script("""
            return {
                stage: parseInt(localStorage.getItem('failsafe_stage') || '1', 10),
                popupDisplay: window.getComputedStyle(document.getElementById('modal-active-clue-popup')).display,
                bannerDisplay: document.getElementById('active-clue-banner')?.style.display,
                btnText: document.getElementById('btn-ethan-clue')?.innerText
            };
        """)
        print("State after solving Stage 01:", after_solve)
        assert after_solve['stage'] == 2, f"Expected stage 2, got {after_solve['stage']}"
        assert after_solve['popupDisplay'] == 'none', "Clue Popup must close when puzzle is cleared!"
        assert after_solve['bannerDisplay'] == 'none', "Clue banner must hide when puzzle is cleared!"
        assert "USE CLUE" in after_solve['btnText'], f"Button should revert to USE CLUE for next stage, got: {after_solve['btnText']}"

        driver.save_screenshot("shot_stage02_clue_cleared.png")
        print("Saved screenshot: shot_stage02_clue_cleared.png")

        print("\n[SUCCESS] PERSISTENT CLUE POPUP (UNLIMITED TIME, REOPEN ANYTIME, CLEARED ON SOLVE) FULLY VERIFIED!")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
