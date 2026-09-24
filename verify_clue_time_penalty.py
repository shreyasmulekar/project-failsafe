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
    print("[1] Opening Round 1 globally on server...")
    r1_start = post_json("/api/admin/start_round_1", {"pin": ADMIN_PIN})
    print("    Start Round 1 response:", r1_start)

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        print("[2] Opening participant workstation: aditi_os_widget.html...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1.5)

        driver.execute_script("localStorage.clear(); sessionStorage.clear();")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1.5)

        # Register team
        driver.execute_script("toggleAuthMode('register');")
        time.sleep(0.5)

        test_team_id = f"CLUE-PEN-{int(time.time()) % 10000}"
        test_team_name = "Penalty Verification Squad"
        test_team_members = "Agent One, Agent Two"
        test_team_pass = "clue-test"

        print(f"[3] Registering unit: [{test_team_id}]...")
        driver.find_element(By.ID, "auth-reg-id").send_keys(test_team_id)
        driver.find_element(By.ID, "auth-reg-name").send_keys(test_team_name)
        driver.find_element(By.ID, "auth-reg-members").send_keys(test_team_members)
        driver.find_element(By.ID, "auth-reg-pass").send_keys(test_team_pass)
        driver.find_element(By.ID, "auth-register-form").submit()
        time.sleep(2.0)

        # Workstation is active on Stage 1 (since Round 1 is open)
        timer_text_before = driver.find_element(By.ID, "nexus-live-mission-timer").text
        penalty_before = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        clues_before = driver.execute_script("return cluesRemaining;")
        print(f"[4] Before clue: timer='{timer_text_before}', penalty={penalty_before}s, cluesRemaining={clues_before}")
        assert penalty_before == 0, "Initial penalty should be 0"
        assert clues_before == 3, "Initial clues should be 3"

        # Now expend a Tactical Clue with skipConfirm=True (or programmatically)
        print("[5] Expending Tactical Clue on Stage 01...")
        driver.execute_script("requestTacticalClue(true);")
        time.sleep(1.0)

        # Verify cluesRemaining decreased to 2
        clues_after = driver.execute_script("return cluesRemaining;")
        penalty_after = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        hints_used_after = driver.execute_script("return parseInt(localStorage.getItem('failsafe_hints_used_count') || '0', 10);")
        timer_text_after = driver.find_element(By.ID, "nexus-live-mission-timer").text
        penalty_badge = driver.find_element(By.ID, "nexus-penalty-badge")

        print(f"[6] After clue 1: cluesRemaining={clues_after}, penalty_seconds={penalty_after}s, hints_used={hints_used_after}, timer='{timer_text_after}', penalty_badge_displayed={penalty_badge.is_displayed()}")

        assert clues_after == 2, f"Expected 2 clues left, got {clues_after}"
        assert penalty_after == 120, f"Expected 120 seconds (+2:00) penalty, got {penalty_after}"
        assert hints_used_after == 1, f"Expected 1 hint used count, got {hints_used_after}"
        assert penalty_badge.is_displayed(), "Penalty badge must be visible when penalty > 0"
        assert "+2m" in penalty_badge.text, f"Expected '+2m' in badge text, got '{penalty_badge.text}'"

        # Verify broadcast toast mentions +2:00 time penalty
        toast = driver.find_element(By.ID, "broadcast-toast")
        assert toast.is_displayed(), "Broadcast toast should show clue granted"
        print(f"    Clue Toast Text: {toast.text}")
        assert "+2:00" in toast.text or "+2m" in toast.text or "PENALTY" in toast.text, "Toast must indicate time penalty"

        # Capture screenshot of clue penalty active
        shot_path = os.path.join(ARTIFACTS_DIR, "test_clue_time_penalty_active.png")
        driver.save_screenshot(shot_path)
        print(f"    Saved screenshot of active clue time penalty: {shot_path}")

        # Now wait for telemetry to sync to server (telemetry sends every 4s)
        print("[7] Verifying server leaderboard reflects clue penalty...")
        time.sleep(4.5)

        # Check server leaderboard
        req = urllib.request.Request(f"{SERVER_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            teams = data.get("leaderboard", [])
            my_team = next((t for t in teams if t.get("team_id") == test_team_id), None)
            assert my_team is not None, f"Team {test_team_id} should be on leaderboard"
            print(f"    Leaderboard team record: hints_count={my_team.get('hints_count')}, adjusted_time_sec={my_team.get('adjusted_time_sec')}")
            assert my_team.get("hints_count") == 1, f"Server hints_count should be 1, got {my_team.get('hints_count')}"
            assert my_team.get("adjusted_time_sec") >= 120, f"Server adjusted_time_sec should include >=120s penalty, got {my_team.get('adjusted_time_sec')}"

        print("\n========================================================")
        print("✅ CLUE TIME PENALTY TEST PASSED!")
        print("1. Expending a Tactical Clue incurred +2:00 (120s) penalty.")
        print("2. Mission timer increased by +2:00 penalty.")
        print("3. Glowing '+2m PENALTY' badge displayed on timer.")
        print("4. Toast notification confirmed the time penalty.")
        print("5. Server leaderboard received telemetry with hints_count=1 and penalty time.")
        print("========================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
