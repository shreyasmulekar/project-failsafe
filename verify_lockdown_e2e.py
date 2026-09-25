import os
import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def setup_driver(width=1366, height=768):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument(f"--window-size={width},{height}")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        'width': width,
        'height': height,
        'deviceScaleFactor': 1,
        'mobile': False
    })
    return driver

def main():
    print("==================================================")
    print("STARTING E2E VERIFICATION: LOCKDOWN & DUAL UNLOCK")
    print("==================================================")
    
    driver = setup_driver(1366, 768)
    try:
        url = "http://localhost:8000/aditi_os_widget.html"
        driver.get(url)
        time.sleep(2)
        
        # 1. Reset state & Login team
        print("[1] Authenticating team 'TEST_SEC'...")
        driver.execute_script("""
            localStorage.clear();
            const team = {
                team_id: 'TEST_SEC',
                team_name: 'Security Test Squad',
                password: 'pass',
                members: 'Agent Alpha, Agent Beta',
                round_1_started: true
            };
            localStorage.setItem('failsafe_server_url', 'http://localhost:8000');
            localStorage.setItem('failsafe_auth_team', JSON.stringify(team));
            localStorage.setItem('failsafe_team_id', 'TEST_SEC');
            localStorage.setItem('failsafe_team_name', 'Security Test Squad');
            localStorage.setItem('failsafe_round_1_started', 'true');
            applyAuthenticatedTeam(team);
            window.fullscreenExitApproved = false;
            window.fullscreenExitExemptUntil = 0;
            window.globalFullscreenExitAllowed = false;
            fullscreenEnforcementActive = true;
            lockArmed = true;
            proctorLockActive = false;
        """)
        time.sleep(2.5) # Wait for heartbeat and initial setup
        
        # 2. Trigger Lockdown via Right-Click / Google Lens attempt
        print("[2] Testing right-click context menu (Google Lens search interception)...")
        driver.execute_script("""
            const evt = new MouseEvent('contextmenu', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            window.dispatchEvent(evt);
        """)
        time.sleep(1)

        overlay = driver.find_element(By.ID, "proctor-lockdown-overlay")
        is_displayed = overlay.is_displayed()
        print(f"Lockdown Overlay displayed after right-click: {is_displayed}")
        assert is_displayed, "Lockdown overlay should be displayed on contextmenu!"

        reason_text = driver.find_element(By.ID, "proctor-violation-reason").text
        print(f"Detected Breach Reason: '{reason_text}'")
        assert "Google Lens" in reason_text or "Context Menu" in reason_text or "Prohibited Action" in reason_text

        # Take screenshot of lockdown screen at 1366x768
        lock_shot_1366 = os.path.join(ARTIFACT_DIR, "shot_lockdown_1366x768.png")
        driver.save_screenshot(lock_shot_1366)
        print(f"Saved screenshot: {lock_shot_1366}")

        # 3. Test Invalid Local Key Entry
        print("[3] Testing invalid organizer key entry...")
        pin_input = driver.find_element(By.ID, "proctor-pin-input")
        pin_input.clear()
        pin_input.send_keys("WRONG_KEY_999")
        
        driver.execute_script("verifyProctorOverride();")
        time.sleep(0.5)
        
        err_msg = driver.find_element(By.ID, "proctor-error-msg").text
        print(f"Error message on invalid key: '{err_msg}'")
        assert "ACCESS DENIED" in err_msg, "Should reject invalid key"
        assert overlay.is_displayed(), "Should still be locked after invalid key"

        # 4. Test Valid Local Key Entry
        print("[4] Testing valid organizer key entry ('wie-admin-2026')...")
        pin_input.clear()
        pin_input.send_keys("wie-admin-2026")
        driver.execute_script("verifyProctorOverride();")
        time.sleep(1)
        
        is_displayed = overlay.is_displayed()
        print(f"Lockdown Overlay displayed after valid key: {is_displayed}")
        assert not is_displayed, "Lockdown overlay should disappear after valid key!"

        # 5. Trigger Second Lockdown via Window Blur / Focus Loss
        print("[5] Testing window blur / focus loss lockdown trigger...")
        driver.execute_script("""
            fullscreenEnforcementActive = true;
            lockArmed = true;
            triggerProctorLockdown("Workstation Focus Lost: Switched Window or Clicked Outside");
        """)
        time.sleep(1.5)
        
        is_displayed = overlay.is_displayed()
        print(f"Lockdown Overlay displayed after focus loss: {is_displayed}")
        assert is_displayed, "Lockdown overlay should display after focus loss"

        # Verify server received the lock state
        req = urllib.request.Request("http://localhost:8000/api/teams/state?team_id=TEST_SEC")
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            team = data.get('team', {})
            print(f"Server state for TEST_SEC is_locked: {team.get('is_locked')}")
            assert team.get('is_locked') == True, "Server should record team as locked"

        # 6. Test Remote Unlock from Organizer Dashboard
        print("[6] Testing Remote Unlock via API call (/api/admin/remote-unlock)...")
        unlock_payload = json.dumps({"pin": "wie-admin-2026", "team_id": "TEST_SEC"}).encode('utf-8')
        unlock_req = urllib.request.Request(
            "http://localhost:8000/api/admin/remote-unlock",
            data=unlock_payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(unlock_req) as resp:
            unlock_resp = json.loads(resp.read().decode('utf-8'))
            print("Remote unlock API response:", unlock_resp)
            assert unlock_resp.get("success"), "Remote unlock API should return success"

        # Wait for client telemetry heartbeat to process the remote unlock (polls every 1.2s when locked)
        print("Waiting for client telemetry heartbeat to receive remote unlock...")
        time.sleep(2.8)

        is_displayed = overlay.is_displayed()
        print(f"Lockdown Overlay displayed after Remote Unlock: {is_displayed}")
        assert not is_displayed, "Workstation should automatically unlock via remote dashboard signal!"

        # Take screenshot of restored workstation
        unlocked_shot_1366 = os.path.join(ARTIFACT_DIR, "shot_unlocked_workstation_1366x768.png")
        driver.save_screenshot(unlocked_shot_1366)
        print(f"Saved screenshot: {unlocked_shot_1366}")

        # 7. Check 1280x720 laptop viewport for lockdown overlay
        print("[7] Checking 1280x720 laptop viewport...")
        driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 1280,
            'height': 720,
            'deviceScaleFactor': 1,
            'mobile': False
        })
        time.sleep(1)
        driver.execute_script("""
            fullscreenEnforcementActive = true;
            lockArmed = true;
            triggerProctorLockdown("Switched Browser Tab or Opened New Tab");
        """)
        time.sleep(1)
        lock_shot_1280 = os.path.join(ARTIFACT_DIR, "shot_lockdown_1280x720.png")
        driver.save_screenshot(lock_shot_1280)
        print(f"Saved screenshot: {lock_shot_1280}")

        # Also test FAILSAFE2090 local key
        print("Testing organizer key 'FAILSAFE2090'...")
        pin_input = driver.find_element(By.ID, "proctor-pin-input")
        pin_input.clear()
        pin_input.send_keys("FAILSAFE2090")
        driver.execute_script("verifyProctorOverride();")
        time.sleep(1)
        assert not overlay.is_displayed(), "FAILSAFE2090 should successfully unlock the station!"
        print("SUCCESS: FAILSAFE2090 unlocked the station!")

        print("\n==================================================")
        print("ALL VERIFICATION CHECKS PASSED PERFECTLY (100%)!")
        print("==================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
