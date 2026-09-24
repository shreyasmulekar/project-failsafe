# scratch/test_browser_reset_and_p2_click.py
import sys
import os
import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.stdout.reconfigure(encoding='utf-8')
ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def run():
    # Ensure test team exists
    try:
        payload = json.dumps({"team_id": "TEAM-01", "team_name": "Phoenix Vanguard", "password": "pass", "members": "Operator"}).encode()
        req = urllib.request.Request("http://127.0.0.1:8000/api/teams/register", data=payload, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=3)
    except Exception:
        pass

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1600,1000")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        print("=== 1. VERIFYING ADMIN COMMAND CENTER (admin.html) ===")
        driver.get("http://127.0.0.1:8000/admin.html")
        time.sleep(2)

        # Enter PIN if login modal is present
        try:
            pin_input = driver.find_element(By.ID, "admin-pin-input")
            if pin_input.is_displayed():
                pin_input.send_keys("wie-admin-2026")
                driver.find_element(By.ID, "btn-admin-login").click()
                time.sleep(1)
        except Exception:
            pass

        # Check top navbar reset buttons
        btn_r1 = driver.find_element(By.XPATH, "//button[contains(., 'RESET ROUND 1')]")
        btn_r2 = driver.find_element(By.XPATH, "//button[contains(., 'RESET ROUND 2')]")
        btn_purge = driver.find_element(By.XPATH, "//button[contains(., 'REMOVE ALL TEAMS')]")
        assert btn_r1 is not None and btn_r1.is_displayed(), "RESET ROUND 1 button missing from top navbar"
        assert btn_r2 is not None and btn_r2.is_displayed(), "RESET ROUND 2 button missing from top navbar"
        assert btn_purge is not None and btn_purge.is_displayed(), "REMOVE ALL TEAMS button missing from top navbar"
        print("  [OK] Top navbar buttons verified: [RESET ROUND 1], [RESET ROUND 2], [REMOVE ALL TEAMS].")

        # Take screenshot of Admin navbar & table
        admin_shot = os.path.join(ARTIFACT_DIR, "screenshot_admin_round_resets.png")
        driver.save_screenshot(admin_shot)
        print(f"  [OK] Saved screenshot: {admin_shot}")

        # Check Edit Team modal reset buttons
        driver.execute_script("openModal('modal-edit-team');")
        time.sleep(1)
        btn_edit_r1 = driver.find_element(By.XPATH, "//button[contains(., 'RESET ROUND 1') and contains(@onclick, 'resetTeamRoundFromModal')]")
        btn_edit_r2 = driver.find_element(By.XPATH, "//button[contains(., 'RESET ROUND 2') and contains(@onclick, 'resetTeamRoundFromModal')]")
        assert btn_edit_r1 is not None and btn_edit_r1.is_displayed(), "Modal RESET ROUND 1 missing"
        assert btn_edit_r2 is not None and btn_edit_r2.is_displayed(), "Modal RESET ROUND 2 missing"
        print("  [OK] Edit Team modal contains independent Round 1 & Round 2 reset buttons.")

        modal_shot = os.path.join(ARTIFACT_DIR, "screenshot_admin_edit_modal_resets.png")
        driver.save_screenshot(modal_shot)
        print(f"  [OK] Saved screenshot: {modal_shot}")
        driver.execute_script("closeModal('modal-edit-team');")

        print("\n=== 2. VERIFYING PARTICIPANT WORKSTATION PUZZLE 2 CLICK GUIDANCE ===")
        driver.get("http://127.0.0.1:8000/aditi_os_widget.html")
        time.sleep(2)

        # Set stage to 2
        driver.execute_script("""
            localStorage.setItem('failsafe_stage', '2');
            currentStage = 2;
            if (typeof applyStageGating === 'function') applyStageGating(2);
        """)
        time.sleep(1)

        # Test Ethan's "Where to click" button on Stage 2
        driver.execute_script("explainWhereToClick();")
        time.sleep(1)
        ethan_text = driver.execute_script("""
            const s = document.getElementById('nexus-tara-speech');
            if (s && s.innerText) return s.innerText;
            const e = document.getElementById('ethan-dialogue-text');
            return e ? (e.innerText || e.textContent) : '';
        """)
        print(f"  [OK] Dialogue on Stage 2:\n      {ethan_text[:120]}...")
        assert "STAGE 02" in ethan_text or "Memory" in ethan_text or "Dossier 02" in ethan_text
        assert "UP" in ethan_text
        assert "RESTORE MEMORY SEQUENCE" in ethan_text

        # Open Dossier 02 (modal-memory)
        driver.execute_script("openModal('modal-memory');")
        time.sleep(1)

        # Verify #v1-memory-click-guide is visible
        guide_banner = driver.find_element(By.ID, "v1-memory-click-guide")
        assert guide_banner is not None and guide_banner.is_displayed(), "Click guidance banner missing from modal-memory"
        guide_text = guide_banner.text
        print(f"  [OK] Dossier 02 Guidance Banner:\n      {guide_text[:150]}...")
        assert "WHERE TO CLICK TO SOLVE THIS PUZZLE" in guide_text
        assert "▲ UP" in guide_text and "▼ DN" in guide_text
        assert "RESTORE MEMORY SEQUENCE" in guide_text

        # Check memory cards have arrow buttons
        up_buttons = driver.find_elements(By.CLASS_NAME, "btn-mem-shift-up")
        dn_buttons = driver.find_elements(By.CLASS_NAME, "btn-mem-shift-dn")
        print(f"  [OK] Found {len(up_buttons)} [▲ UP] buttons and {len(dn_buttons)} [▼ DN] buttons in memory core.")
        assert len(up_buttons) == 6, f"Expected 6 UP buttons, found {len(up_buttons)}"
        assert len(dn_buttons) == 6, f"Expected 6 DOWN buttons, found {len(dn_buttons)}"

        # Check restore sequence button
        restore_btn = driver.find_element(By.ID, "btn-restore-mem-seq")
        assert restore_btn is not None and restore_btn.is_displayed()
        print(f"  [OK] Restore Sequence button verified: '{restore_btn.text}'")

        # Take screenshot of Dossier 02 with Where to Click guidance
        p2_shot = os.path.join(ARTIFACT_DIR, "screenshot_puzzle2_where_to_click_guidance.png")
        driver.save_screenshot(p2_shot)
        print(f"  [OK] Saved screenshot: {p2_shot}")

        print("\n=======================================================")
        print("ALL BROWSER UI TESTS FOR ROUND RESETS & PUZZLE 2 PASSED!")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    run()
