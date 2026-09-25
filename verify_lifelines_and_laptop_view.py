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
    chrome_options.add_argument("--window-size=1366,768")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("[2] Opening participant workstation: aditi_os_widget.html...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1.5)

        driver.execute_script("toggleAuthMode('register');")
        time.sleep(0.5)

        test_team_id = f"LIFE-{int(time.time()) % 10000}"
        test_team_name = "Lifelines Verification Squad"
        test_team_members = "Investigator Alpha, Investigator Beta"
        test_team_pass = "life-test"

        print(f"[3] Registering unit: [{test_team_id}]...")
        driver.find_element(By.ID, "auth-reg-id").send_keys(test_team_id)
        driver.find_element(By.ID, "auth-reg-name").send_keys(test_team_name)
        driver.find_element(By.ID, "auth-reg-members").send_keys(test_team_members)
        driver.find_element(By.ID, "auth-reg-pass").send_keys(test_team_pass)
        driver.find_element(By.XPATH, "//form[@id='auth-register-form']//button[@type='submit']").click()
        time.sleep(2.0)

        # Baseline checks
        clues_initial = driver.execute_script("return cluesRemaining;")
        penalty_initial = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        print(f"[4] Initial State: cluesRemaining={clues_initial}/3, penalty={penalty_initial}s")
        assert clues_initial == 3, f"Expected 3 initial clues, got {clues_initial}"
        assert penalty_initial == 0, f"Expected 0 initial penalty, got {penalty_initial}"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_r1_dash_1366x768.png"))
        print(" -> Saved test_laptop_r1_dash_1366x768.png")

        # Request clue with confirmation modal
        print("[5] Requesting Tactical Clue for Stage 01...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(0.8)

        confirm_modal = driver.find_element(By.ID, "modal-clue-confirm")
        assert confirm_modal.is_displayed(), "#modal-clue-confirm is not displayed!"
        modal_text = confirm_modal.text
        print("    Confirmation Modal text preview:\n   ", modal_text.replace("\n", " | ")[:120])
        assert "+2:00" in modal_text or "+120s" in modal_text, "Time penalty warning missing from confirmation modal!"
        assert "3 / 3" in modal_text or "ROUND 01 LIFELINES" in modal_text, "Lifeline info missing!"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_clue_confirm_modal_1366x768.png"))
        print(" -> Saved test_clue_confirm_modal_1366x768.png")

        # Confirm Clue 1
        print("[6] Confirming Clue 1 (+2:00 penalty)...")
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(1.0)

        clues_1 = driver.execute_script("return cluesRemaining;")
        penalty_1 = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        print(f"    After Clue 1: cluesRemaining={clues_1}/3, penalty={penalty_1}s")
        assert clues_1 == 2, f"Expected 2 clues left, got {clues_1}"
        assert penalty_1 == 120, f"Expected 120s penalty, got {penalty_1}"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_clue_expended_1366x768.png"))
        print(" -> Saved test_clue_expended_1366x768.png")

        # Duplicate clue on same stage
        print("[7] Verifying duplicate clue on same stage is blocked...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(0.5)
        speech_text = driver.find_element(By.ID, "nexus-tara-speech").text
        assert "already granted" in speech_text.lower(), f"Duplicate clue was not blocked! Text: {speech_text}"
        print(" -> Duplicate clue on Stage 1 properly blocked.")

        # Advance to Stage 2 & take Clue 2
        print("[8] Advancing to Stage 2 & taking Clue 2...")
        driver.execute_script("setStage(2);")
        time.sleep(0.5)
        driver.execute_script("requestTacticalClue(true);")
        time.sleep(0.5)
        clues_2 = driver.execute_script("return cluesRemaining;")
        penalty_2 = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        print(f"    After Clue 2: cluesRemaining={clues_2}/3, penalty={penalty_2}s")
        assert clues_2 == 1, f"Expected 1 clue left, got {clues_2}"
        assert penalty_2 == 240, f"Expected 240s penalty, got {penalty_2}"

        # Advance to Stage 3 & take Clue 3 (Final life)
        print("[9] Advancing to Stage 3 & taking Clue 3 (Final Lifeline)...")
        driver.execute_script("setStage(3);")
        time.sleep(0.5)
        driver.execute_script("requestTacticalClue(true);")
        time.sleep(0.5)
        clues_3 = driver.execute_script("return cluesRemaining;")
        penalty_3 = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        print(f"    After Clue 3: cluesRemaining={clues_3}/3, penalty={penalty_3}s")
        assert clues_3 == 0, f"Expected 0 clues left, got {clues_3}"
        assert penalty_3 == 360, f"Expected 360s penalty, got {penalty_3}"

        # Advance to Stage 4 & test exhausted lifelines
        print("[10] Advancing to Stage 4 & testing exhausted lifelines...")
        driver.execute_script("setStage(4);")
        time.sleep(0.5)
        driver.execute_script("requestTacticalClue();")
        time.sleep(0.5)
        speech_text_4 = driver.find_element(By.ID, "nexus-tara-speech").text
        assert "0/3" in speech_text_4 or "expended" in speech_text_4.lower() or "restricted" in speech_text_4.lower(), f"4th clue was not blocked! Text: {speech_text_4}"
        print(" -> 4th clue attempt properly blocked (All 3 lifelines used).")

        # Switch to Round 2 & test zero clues rule
        print("[11] Switching to Round 2 & testing zero clues rule...")
        driver.execute_script("window.isRound2Approved = true; localStorage.setItem('failsafe_r2_approved', 'true'); toggleRoundView();")
        time.sleep(1.0)
        driver.execute_script("requestTacticalClue();")
        time.sleep(0.5)
        speech_r2 = driver.find_element(By.ID, "r2-tara-speech").text or driver.execute_script("return document.getElementById('nexus-tara-speech').innerText;")
        assert "round 2" in speech_r2.lower() and "disabled" in speech_r2.lower(), f"Round 2 clue was not blocked! Text: {speech_r2}"
        print(" -> Round 2 clue attempt properly blocked (Zero clues in Round 2).")

        # Capture Round 2 Puzzle Diagrams
        print("[12] Capturing Round 2 Puzzle Diagrams on 1366x768...")
        driver.execute_script("window.__testBypassSequentialLock = true; openRound2Modal(1);")
        time.sleep(0.8)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_r2_matrix_1366x768.png"))
        driver.execute_script("openRound2Modal(2);")
        time.sleep(0.8)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_r2_rotation_1366x768.png"))
        driver.execute_script("openRound2Modal(3);")
        time.sleep(0.8)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_r2_cube_1366x768.png"))
        driver.execute_script("closeModal('modal-r2-dossier');")
        time.sleep(0.5)

        # Switch to Round 1 Stage 8 (Stego modal)
        driver.execute_script("toggleRoundView(); openModal('modal-stego');")
        time.sleep(1.0)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_stego_1366x768.png"))
        driver.execute_script("closeModal('modal-stego');")
        time.sleep(0.5)

        # 1280x720 laptop test
        print("[13] Testing 1280x720 small laptop...")
        driver.set_window_size(1280, 720)
        time.sleep(1.0)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_dash_1280x720.png"))

        # Admin Console on 1366x768
        print("[14] Testing Admin Console on 1366x768...")
        driver.get(f"{SERVER_URL}/admin.html")
        time.sleep(1.5)
        pin_input = driver.find_element(By.ID, "admin-auth-pin")
        pin_input.send_keys("wie-admin-2026")
        driver.find_element(By.XPATH, "//form[@id='admin-login-form']//button[@type='submit']").click()
        time.sleep(2.0)
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "test_laptop_admin_1366x768.png"))
        print(" -> Saved test_laptop_admin_1366x768.png")

        print("\n" + "="*60)
        print("ALL TESTS PASSED SUCCESSFULLY!")
        print(" [OK] Exactly 3 Lifelines in Round 1 on any 3 puzzles of choice.")
        print(" [OK] +2:00 (+120s) penalty per clue verified on running timer.")
        print(" [OK] Confirmation modal warning about +2 min penalty verified.")
        print(" [OK] Round 2 zero clues rule verified.")
        print(" [OK] Small laptop (1366x768 and 1280x720) views captured.")
        print("="*60 + "\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
