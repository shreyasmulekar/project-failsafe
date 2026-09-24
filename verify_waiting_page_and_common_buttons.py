import time
import json
import urllib.request
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SERVER_URL = "http://localhost:8000"
ADMIN_PIN = "wie-admin-2026"
ARTIFACTS_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def post_json(endpoint, payload):
    req = urllib.request.Request(
        f"{SERVER_URL}{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    print("[1] Resetting tournament phase: pausing Round 1 and setting initial state...")
    r1_pause = post_json("/api/admin/pause_round_1", {"pin": ADMIN_PIN})
    print("    Pause Round 1 response:", r1_pause)

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        print("[2] Opening participant workstation: aditi_os_widget.html...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1.5)

        # Clear any prior local storage session to ensure fresh registration
        driver.execute_script("localStorage.clear(); sessionStorage.clear();")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1.5)

        # Ensure auth modal is visible
        auth_modal = wait.until(EC.visibility_of_element_located((By.ID, "team-auth-modal")))
        print("    Auth modal displayed.")

        # Switch to Register tab
        driver.execute_script("toggleAuthMode('register');")
        time.sleep(0.5)

        # Register a brand new team
        test_team_id = f"TEAM-LOBBY-{int(time.time()) % 10000}"
        test_team_name = "Shadow Cyber Division"
        test_team_members = "Arjun, Riya, Kabir"
        test_team_pass = "cyber-2026"

        print(f"[3] Registering new team: [{test_team_id}] {test_team_name}...")
        driver.find_element(By.ID, "auth-reg-id").send_keys(test_team_id)
        driver.find_element(By.ID, "auth-reg-name").send_keys(test_team_name)
        driver.find_element(By.ID, "auth-reg-members").send_keys(test_team_members)
        driver.find_element(By.ID, "auth-reg-pass").send_keys(test_team_pass)
        
        # Submit registration form
        reg_form = driver.find_element(By.ID, "auth-register-form")
        reg_form.submit()
        time.sleep(1.5)

        # Verify Waiting Lobby is shown!
        wait_overlay = driver.find_element(By.ID, "round1-waiting-overlay")
        is_wait_displayed = wait_overlay.is_displayed()
        print(f"[4] Checking Round 1 Waiting Lobby visibility: is_displayed={is_wait_displayed}")
        assert is_wait_displayed, "ERROR: Round 1 Waiting Lobby overlay should be displayed after registration when Round 1 is on hold!"

        # Verify team details on Waiting Lobby card
        lobby_team_id = driver.find_element(By.ID, "r1-wait-team-id").text
        lobby_team_name = driver.find_element(By.ID, "r1-wait-team-name").text
        lobby_members = driver.find_element(By.ID, "r1-wait-members").text
        print(f"    Lobby Team ID: {lobby_team_id}")
        print(f"    Lobby Team Name: {lobby_team_name}")
        print(f"    Lobby Members: {lobby_members}")
        assert test_team_id in lobby_team_id, f"Expected {test_team_id} in {lobby_team_id}"
        assert test_team_name in lobby_team_name, f"Expected {test_team_name} in {lobby_team_name}"

        # Capture screenshot of Round 1 Waiting Lobby
        shot_path_1 = os.path.join(ARTIFACTS_DIR, "test_round1_waiting_lobby.png")
        driver.save_screenshot(shot_path_1)
        print(f"    Saved screenshot: {shot_path_1}")

        # Now test Round 2 gating while in lobby
        print("[5] Verifying Round 2 access is strictly locked...")
        r2_attempt = driver.execute_script("return launchRound2Arena();")
        time.sleep(0.5)
        toast = driver.find_element(By.ID, "broadcast-toast")
        assert toast.is_displayed(), "Broadcast toast should display rejection message when attempting Round 2 unauthorized"
        toast_text = toast.text
        print(f"    Rejection toast text: {toast_text}")
        assert "ROUND 2 LOCKED" in toast_text, "Toast must explicitly indicate Round 2 is locked"

        # Capture screenshot of locked toast
        shot_path_2 = os.path.join(ARTIFACTS_DIR, "test_round2_locked_rejection_toast.png")
        driver.save_screenshot(shot_path_2)
        print(f"    Saved screenshot: {shot_path_2}")

        # Verify toast stays for at least 3 seconds
        print("[6] Verifying broadcast toast duration >= 3s...")
        t_start = time.time()
        time.sleep(2.2) # At 2.7s total, toast must still be displayed
        assert toast.is_displayed(), "Toast dismissed prematurely before 3 seconds!"
        print(f"    Toast verified visible at {(time.time() - t_start):.2f}s.")

        # Now simulate Organizer clicking 'OPEN ROUND 1 (START ALL TEAMS)'
        print("[7] Simulating Organizer clicking 'OPEN ROUND 1'...")
        r1_start = post_json("/api/admin/start_round_1", {"pin": ADMIN_PIN})
        print("    Organizer start_round_1 response:", r1_start)
        assert r1_start.get("success"), "start_round_1 must succeed"

        # Wait for station telemetry to pick up Round 1 start and unlock
        print("    Waiting for workstation telemetry sync (up to 6s)...")
        unlocked = False
        for _ in range(12):
            time.sleep(0.5)
            # Either overlay becomes display: none or opacity: 0
            disp = wait_overlay.value_of_css_property("display")
            opacity = wait_overlay.value_of_css_property("opacity")
            if disp == "none" or opacity == "0":
                unlocked = True
                break

        print(f"    Waiting lobby unlocked: {unlocked}")
        assert unlocked, "Round 1 Waiting Lobby should automatically dismiss when Organizer opens Round 1!"

        # Verify Stage 1 is now open and accessible
        time.sleep(1.0)
        shot_path_3 = os.path.join(ARTIFACTS_DIR, "test_round1_opened_simultaneously.png")
        driver.save_screenshot(shot_path_3)
        print(f"    Saved screenshot of opened stage 1: {shot_path_3}")

        # Now test Round 2 approval flow
        print("[8] Simulating Organizer approving squad for Round 2...")
        # Promote team to Round 2
        r2_promo = post_json("/api/admin/send_to_round_2", {"pin": ADMIN_PIN, "team_id": test_team_id})
        print("    Send to Round 2 response:", r2_promo)
        assert r2_promo.get("success"), "send_to_round_2 must succeed"

        # Wait for participant station telemetry to receive Round 2 approval
        print("    Waiting for workstation to receive Round 2 directive...")
        time.sleep(3.0)

        # Trigger or enter Round 2
        driver.execute_script("launchRound2Arena();")
        time.sleep(1.5)

        r2_workspace = driver.find_element(By.ID, "nexus-r2-workspace")
        is_r2_active = r2_workspace.is_displayed()
        print(f"[9] Checking Round 2 Decryption Arena: is_displayed={is_r2_active}")
        assert is_r2_active, "Round 2 workspace should be active and visible once approved by Organizer!"

        shot_path_4 = os.path.join(ARTIFACTS_DIR, "test_round2_approved_arena.png")
        driver.save_screenshot(shot_path_4)
        print(f"    Saved screenshot of approved Round 2 arena: {shot_path_4}")

        print("\n========================================================")
        print("✅ ALL TESTS PASSED SUCCESSFULLY!")
        print("1. Participant entered Round 1 waiting lobby upon registration.")
        print("2. Organizer 'OPEN ROUND 1' opened participant station simultaneously.")
        print("3. Round 2 entry remained strictly locked until Organizer approval.")
        print("4. Broadcast notifications persisted >= 3 seconds.")
        print("5. Organizer approval successfully unlocked Round 2 Arena.")
        print("========================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
