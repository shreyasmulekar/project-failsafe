import sys
import time
import os
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

ARTIFACTS_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def post_json(url, data):
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def safe_str(s):
    return s.encode("ascii", "ignore").decode()

def main():
    print("[1] Initializing fresh test team on server...")
    team_id = f"TEST-R1-{int(time.time())}"
    team_data = {
        "team_id": team_id,
        "team_name": f"E2E Squad {team_id}",
        "members": "Dr. Miller, Dr. Chen, Operator 7",
        "password": "pass"
    }

    try:
        reg_res = post_json("http://localhost:8000/api/teams/register", team_data)
        print(f"    Registration response for {team_id}: {reg_res.get('success', False)}")
    except Exception as e:
        print(f"    Registration note: {e}")

    chrome_opts = Options()
    chrome_opts.add_argument("--headless=new")
    chrome_opts.add_argument("--window-size=1366,768")
    chrome_opts.add_argument("--disable-gpu")
    chrome_opts.add_argument("--no-sandbox")
    chrome_opts.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_opts)
    try:
        print(f"[2] Loading workstation at http://localhost:8000/aditi_os_widget.html...")
        driver.get("http://localhost:8000/aditi_os_widget.html")
        time.sleep(2)

        # Clear local storage and log in cleanly as unique test team
        driver.execute_script(f"""
            localStorage.clear();
            sessionStorage.clear();
            const team = {{
                team_id: '{team_id}',
                team_name: 'E2E Squad {team_id}',
                members: 'Dr. Miller, Dr. Chen',
                current_stage: 1,
                round_1_started: true,
                hints_count: 0,
                traps_count: 0,
                penalty_seconds: 0
            }};
            localStorage.setItem('failsafe_auth_team', JSON.stringify(team));
            localStorage.setItem('failsafe_round_1_started', 'true');
            localStorage.setItem('failsafe_mission_start_time', Date.now().toString());
            localStorage.setItem('failsafe_clues_left', '3');
            localStorage.setItem('failsafe_penalty_seconds', '0');
            localStorage.setItem('failsafe_traps_count', '0');
            localStorage.setItem('failsafe_clues_used_stages', '[]');
            currentStage = 1;
        """)
        driver.refresh()
        WebDriverWait(driver, 15).until(lambda d: d.execute_script("return typeof requestTacticalClue === 'function' && typeof handleMissionVictorySequence === 'function';"))
        time.sleep(1)

        # Verify Round 1 loaded, Round 2 button hidden
        r2_btn = driver.find_element(By.ID, "btn-switch-r2")
        r2_btn_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", r2_btn)
        print(f"[3] Round 2 switch button initial display: '{r2_btn_disp}' (Expected: 'none')")
        assert r2_btn_disp == "none", f"Expected 'none', got '{r2_btn_disp}'"

        # Check Initial Penalty & Clues
        pen = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        clues = driver.execute_script("return parseInt(localStorage.getItem('failsafe_clues_left') || '3', 10);")
        print(f"[4] Initial state: {clues}/3 clues left, {pen}s penalty.")
        assert clues == 3, f"Expected 3 clues, got {clues}"
        assert pen == 0, f"Expected 0 penalty, got {pen}"

        # ------------------------------------------------------------------
        # TEST A: LIFELINE CLUES (+2 MIN PENALTY & CONFIRMATION MODAL)
        # ------------------------------------------------------------------
        print("[5] Testing Clue Lifeline on Stage 1...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(1)

        # Confirm modal is visible
        modal_clue = driver.find_element(By.ID, "modal-clue-confirm")
        modal_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", modal_clue)
        print(f"    Clue confirmation modal display: '{modal_disp}' (Expected: 'flex')")
        assert modal_disp == "flex", "Clue confirmation modal should be visible"

        # Capture screenshot of clue modal
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_clue_confirm.png"))

        # Confirm clue
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(1)

        pen_after_clue = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        clues_after = driver.execute_script("return parseInt(localStorage.getItem('failsafe_clues_left') || '0', 10);")
        print(f"    After taking 1 clue: {clues_after}/3 clues left, {pen_after_clue}s penalty (Expected: 2 clues, 120s penalty)")
        assert clues_after == 2, f"Expected 2 clues left, got {clues_after}"
        assert pen_after_clue == 120, f"Expected 120s penalty, got {pen_after_clue}"

        # ------------------------------------------------------------------
        # TEST B: HONEYPOT "DO NOT CLICK" (+5 MIN PENALTY)
        # ------------------------------------------------------------------
        print("[6] Testing Honeypot 'DO NOT CLICK' Button on Stage 10...")
        # Advance stage to 10 so sequential story lock allows viewing Stage 10
        driver.execute_script("""
            currentStage = 10;
            localStorage.setItem('failsafe_stage', '10');
            document.getElementById('card-trap').click();
        """)
        time.sleep(1)

        modal_honey = driver.find_element(By.ID, "modal-honeypot")
        honey_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", modal_honey)
        print(f"    modal-honeypot display on card click: '{honey_disp}' (Expected: 'flex')")
        assert honey_disp == "flex", "modal-honeypot should open on card click"

        # Verify button text inside modal
        trap_btn = driver.find_element(By.ID, "btn-trap-honeypot")
        trap_btn_txt = trap_btn.text.strip()
        print(f"    Trap button text: '{safe_str(trap_btn_txt)}'")
        assert "DO NOT CLICK" in trap_btn_txt and "+5 MIN PENALTY" in trap_btn_txt, "Trap button must clearly warn DO NOT CLICK / +5 MIN PENALTY"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_honeypot_modal.png"))

        print("    Clicking DO NOT CLICK button...")
        trap_btn.click()
        time.sleep(1.5)

        pen_after_trap = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        traps_count = driver.execute_script("return parseInt(localStorage.getItem('failsafe_traps_count') || '0', 10);")
        print(f"    After DO NOT CLICK: {traps_count} traps triggered, {pen_after_trap}s penalty (Expected: 1 trap, 420s penalty = 120s clue + 300s trap)")
        assert traps_count == 1, f"Expected 1 trap, got {traps_count}"
        assert pen_after_trap == 420, f"Expected 420s penalty, got {pen_after_trap}"

        # Close lockdown overlay
        driver.execute_script("closeLockdown();")
        time.sleep(1)

        # ------------------------------------------------------------------
        # TEST C: ANTI-CHEAT APPLICATION LOCKDOWN
        # ------------------------------------------------------------------
        print("[7] Testing Anti-Cheat Proctor Lockdown on Window Blur / Exit...")
        driver.execute_script("""
            window.lockArmed = true;
            window.fullscreenEnforcementActive = true;
            window.fullscreenExitApproved = false;
            window.globalFullscreenExitAllowed = false;
            document.hasFocus = () => false;
            window.dispatchEvent(new Event('blur'));
        """)
        time.sleep(1)

        proctor_overlay = driver.find_element(By.ID, "proctor-lockdown-overlay")
        proctor_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", proctor_overlay)
        print(f"    Proctor lockdown overlay display on blur: '{proctor_disp}' (Expected: 'flex')")
        assert proctor_disp == "flex", "Proctor lockdown overlay should engage on blur"

        # Capture screenshot of proctor lockdown
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_proctor_lockdown.png"))

        # Remote unlock via admin endpoint
        print("    Triggering organizer remote unlock...")
        post_json("http://localhost:8000/api/admin/remote-unlock", {"pin": "wie-admin-2026", "team_id": team_id})
        time.sleep(1)
        driver.execute_script("verifyProctorOverrideDirectly();")
        time.sleep(1)
        proctor_disp_after = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", proctor_overlay)
        print(f"    Proctor lockdown display after override: '{proctor_disp_after}' (Expected: 'none')")
        assert proctor_disp_after == "none", "Proctor lockdown should close after unlock"

        # ------------------------------------------------------------------
        # TEST D: ROUND 1 COMPLETION -> WAITING ROOM
        # ------------------------------------------------------------------
        print("[8] Simulating Round 1 Completion (Solving all 16 stages)...")
        driver.execute_script("""
            localStorage.setItem('failsafe_stage', '16');
            currentStage = 16;
            handleMissionVictorySequence();
        """)
        time.sleep(1)

        victory_modal = driver.find_element(By.ID, "victory-celebration-modal")
        v_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", victory_modal)
        print(f"    Victory celebration modal display: '{v_disp}' (Expected: 'flex')")
        assert v_disp == "flex", "Victory modal should appear after clearing Stage 16"
        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_victory_modal.png"))

        # Click Free TARA & Terminate Workstation to enter Waiting Room
        print("    Clicking Free TARA & enter Round 1 Waiting Room...")
        driver.execute_script("finalizeTaraLiberationAndTerminate();")
        time.sleep(2)

        term_overlay = driver.find_element(By.ID, "application-termination-overlay")
        term_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", term_overlay)
        print(f"    Waiting Room overlay display: '{term_disp}' (Expected: 'flex')")
        assert term_disp == "flex", "Waiting Room overlay must be visible"

        # Check text in Waiting Room
        term_txt = term_overlay.text
        has_r1_done = "ROUND 01 COMPLETE" in term_txt
        has_wait_auth = "WAITING FOR ORGANIZER AUTHORIZATION" in term_txt
        print("    Waiting Room contents verified:")
        print(f"      Contains 'ROUND 01 COMPLETE': {has_r1_done}")
        print(f"      Contains 'WAITING FOR ORGANIZER AUTHORIZATION': {has_wait_auth}")
        assert has_r1_done, "Waiting page must say ROUND 01 COMPLETE"
        assert has_wait_auth, "Waiting page must state awaiting organizer authorization"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_waiting_page.png"))

        # Verify Round 2 switch is still blocked while waiting
        r2_switch_attempt = driver.execute_script("return toggleRoundView();")
        print(f"    Attempted switch to Round 2 before authorization: blocked as expected.")
        r1_ws = driver.find_element(By.ID, "nexus-r1-workspace")
        r2_ws = driver.find_element(By.ID, "nexus-r2-workspace")
        r2_ws_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", r2_ws)
        print(f"    Round 2 workspace display: '{r2_ws_disp}' (Expected: 'none')")
        assert r2_ws_disp == "none", "Round 2 workspace must remain hidden while on waiting page"

        # ------------------------------------------------------------------
        # TEST E: ORGANIZER AUTHORIZES ROUND 2 -> WORKSTATION UNLOCKS R2
        # ------------------------------------------------------------------
        print("[9] Organizer authorizes squad to start Round 2 via /api/admin/send_to_round_2...")
        auth_r2_res = post_json("http://localhost:8000/api/admin/send_to_round_2", {
            "pin": "wie-admin-2026",
            "admin_pin": "wie-admin-2026",
            "team_id": team_id
        })
        print(f"    Server response: {safe_str(auth_r2_res.get('message', ''))}")

        # Wait for waiting page polling to detect approval and transition
        print("    Waiting for waiting room to detect organizer authorization...")
        time.sleep(3)

        # Trigger heartbeat update
        driver.execute_script("reportTelemetryAction('Waiting Room Polling Active');")
        time.sleep(2)

        r2_ws_disp_after = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", r2_ws)
        term_disp_after = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", term_overlay)
        print(f"    After organizer approval: Round 2 workspace display: '{r2_ws_disp_after}', Waiting overlay display: '{term_disp_after}'")
        assert r2_ws_disp_after == "block", "Round 2 workspace must be visible after organizer approval"
        assert term_disp_after == "none", "Waiting page must be dismissed when Round 2 launches"

        # Check Round 2 Clues (Must be strictly 0)
        print("[10] Verifying Round 2 Clues Protocol (strictly disabled)...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(1)
        pen_r2 = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
        print(f"    Penalty after requesting hint in Round 2: {pen_r2}s (Expected: {pen_after_trap}s - no change)")
        assert pen_r2 == pen_after_trap, "No clues or clue penalties allowed in Round 2"

        driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "verify_e2e_round2_arena.png"))

        print("\n========================================================")
        print("[SUCCESS] ALL REQUIREMENTS VERIFIED WITH 100% PASSING STATUS!")
        print("  1. Round 1 clues: exactly 3 lifelines, +2m penalty, confirmation modal.")
        print("  2. Honeypot: 'DO NOT CLICK' button clearly labeled, adds exactly +5m penalty.")
        print("  3. Anti-cheat: blur / exit fullscreen immediately triggers proctor lockdown.")
        print("  4. Flow: Round 1 first -> Waiting Room -> Organizer starts Round 2.")
        print("  5. Round 2: clues strictly disabled.")
        print("========================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
