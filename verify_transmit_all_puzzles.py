import sys
import time

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    results = []

    try:
        print("[TEST] Loading http://localhost:8000/aditi_os_widget.html...")
        driver.get("http://localhost:8000/aditi_os_widget.html")
        time.sleep(2)

        # Authenticate test team and bypass sequential lock for test runner
        driver.execute_script("""
            localStorage.setItem('failsafe_stage', '1');
            localStorage.setItem('failsafe_r2_stage', '1');
            window.__testBypassSequentialLock = true;
            if (typeof applyAuthenticatedTeam === 'function') {
                applyAuthenticatedTeam({ team_id: 'TEST-01', team_name: 'Test Team', members: 'Operator', current_stage: 1 });
            }
        """)
        time.sleep(1)

        print("\n=======================================================")
        print("--- PHASE 1: ROUND 1 STAGES 1 TO 16 TRANSMIT VERIFICATION ---")
        print("=======================================================")

        # ----------------------------------------------------
        # Stage 1: Recovery Terminal (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-recovery');")
        time.sleep(0.4)
        inp1 = driver.find_element(By.ID, "v1-modal-recovery-input")
        inp1.clear()
        inp1.send_keys("ACCESS")
        inp1.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 2, f"Expected currentStage == 2, got {stg}"
        print(f"[PASS] Stage 01: Submitted 'ACCESS' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 01 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 2: Bottom Dock Passcode (Enter Key)
        # ----------------------------------------------------
        dock_inp = driver.find_element(By.ID, "nexus-dock-passcode")
        dock_inp.clear()
        dock_inp.send_keys("123456")
        dock_inp.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 3, f"Expected currentStage == 3, got {stg}"
        print(f"[PASS] Stage 02: Submitted '123456' via Bottom Dock Enter key -> Promoted to Stage {stg}")
        results.append("Stage 02 (Bottom dock Enter key): PASS")

        # ----------------------------------------------------
        # Stage 3: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-acrostic');")
        time.sleep(0.4)
        inp3 = driver.find_element(By.ID, "input-stage-3")
        inp3.clear()
        inp3.send_keys("SAFE")
        btn3 = driver.find_element(By.CSS_SELECTOR, "#modal-acrostic .btn-tactical.success")
        btn3.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 4, f"Expected currentStage == 4, got {stg}"
        print(f"[PASS] Stage 03: Submitted 'SAFE' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 03 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 4: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-incident-logs');")
        time.sleep(0.4)
        inp4 = driver.find_element(By.ID, "input-stage-4")
        inp4.clear()
        inp4.send_keys("28/02/2025")
        inp4.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 5, f"Expected currentStage == 5, got {stg}"
        print(f"[PASS] Stage 04: Submitted '28/02/2025' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 04 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 5: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-clearance');")
        time.sleep(0.4)
        inp5 = driver.find_element(By.ID, "input-stage-5")
        inp5.clear()
        inp5.send_keys("POLARIS")
        btn5 = driver.find_element(By.CSS_SELECTOR, "#modal-clearance .btn-tactical.success")
        btn5.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 6, f"Expected currentStage == 6, got {stg}"
        print(f"[PASS] Stage 05: Submitted 'POLARIS' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 05 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 6: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-comments');")
        time.sleep(0.4)
        inp6 = driver.find_element(By.ID, "input-stage-6")
        inp6.clear()
        inp6.send_keys("MARGIN_KEY")
        inp6.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 7, f"Expected currentStage == 7, got {stg}"
        print(f"[PASS] Stage 06: Submitted 'MARGIN_KEY' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 06 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 7: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-font');")
        time.sleep(0.4)
        inp7 = driver.find_element(By.ID, "input-stage-7")
        inp7.clear()
        inp7.send_keys("ARIAL")
        btn7 = driver.find_element(By.CSS_SELECTOR, "#modal-font .btn-tactical.success")
        btn7.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 8, f"Expected currentStage == 8, got {stg}"
        print(f"[PASS] Stage 07: Submitted 'ARIAL' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 07 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 8: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-spectro');")
        time.sleep(0.4)
        inp8 = driver.find_element(By.ID, "input-stage-8")
        inp8.clear()
        inp8.send_keys("WHITE")
        inp8.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 9, f"Expected currentStage == 9, got {stg}"
        print(f"[PASS] Stage 08: Submitted 'WHITE' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 08 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 9: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-version-hist');")
        time.sleep(0.4)
        inp9 = driver.find_element(By.ID, "input-stage-9")
        inp9.clear()
        inp9.send_keys("OVERRIDE_FAILED")
        btn9 = driver.find_element(By.CSS_SELECTOR, "#modal-version-hist .btn-tactical.success")
        btn9.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 10, f"Expected currentStage == 10, got {stg}"
        print(f"[PASS] Stage 09: Submitted 'OVERRIDE_FAILED' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 09 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 10: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-honeypot');")
        time.sleep(0.4)
        inp10 = driver.find_element(By.ID, "input-honeypot")
        inp10.clear()
        inp10.send_keys("BYPASS")
        inp10.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 11, f"Expected currentStage == 11, got {stg}"
        print(f"[PASS] Stage 10: Submitted 'BYPASS' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 10 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 11: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-failsafe');")
        time.sleep(0.4)
        inp11 = driver.find_element(By.ID, "input-stage-11")
        inp11.clear()
        inp11.send_keys("6-9-11")
        btn11 = driver.find_element(By.CSS_SELECTOR, "#modal-failsafe .btn-tactical.success")
        btn11.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 12, f"Expected currentStage == 12, got {stg}"
        print(f"[PASS] Stage 11: Submitted '6-9-11' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 11 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 12: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-whiteout');")
        time.sleep(0.4)
        inp12 = driver.find_element(By.ID, "input-whiteout")
        inp12.clear()
        inp12.send_keys("CLEARANCE_ALPHA")
        inp12.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 13, f"Expected currentStage == 13, got {stg}"
        print(f"[PASS] Stage 12: Submitted 'CLEARANCE_ALPHA' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 12 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 13: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-rot4');")
        time.sleep(0.4)
        inp13 = driver.find_element(By.ID, "input-rot4")
        inp13.clear()
        inp13.send_keys("ADITIS13")
        btn13 = driver.find_element(By.CSS_SELECTOR, "#modal-rot4 .dossier-btn")
        btn13.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 14, f"Expected currentStage == 14, got {stg}"
        print(f"[PASS] Stage 13: Submitted 'ADITIS13' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 13 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 14: Modal Input (Enter Key)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-atbash');")
        time.sleep(0.4)
        inp14 = driver.find_element(By.ID, "input-atbash")
        inp14.clear()
        inp14.send_keys("PROJECT")
        inp14.send_keys(Keys.ENTER)
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 15, f"Expected currentStage == 15, got {stg}"
        print(f"[PASS] Stage 14: Submitted 'PROJECT' via Enter key -> Promoted to Stage {stg}")
        results.append("Stage 14 (Enter key): PASS")

        # ----------------------------------------------------
        # Stage 15: Modal Input (Transmit Button Click)
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-polybius');")
        time.sleep(0.4)
        inp15 = driver.find_element(By.ID, "input-polybius")
        inp15.clear()
        inp15.send_keys("VECTOR")
        btn15 = driver.find_element(By.CSS_SELECTOR, "#modal-polybius .dossier-btn")
        btn15.click()
        time.sleep(1.0)
        stg = driver.execute_script("return currentStage;")
        assert stg == 16, f"Expected currentStage == 16, got {stg}"
        print(f"[PASS] Stage 15: Submitted 'VECTOR' via Transmit Button -> Promoted to Stage {stg}")
        results.append("Stage 15 (Transmit button): PASS")

        # ----------------------------------------------------
        # Stage 16: Modal Input (Enter Key) - Round 1 Victory!
        # ----------------------------------------------------
        driver.execute_script("openModal('modal-frequency');")
        time.sleep(0.4)
        inp16 = driver.find_element(By.ID, "input-frequency")
        inp16.clear()
        inp16.send_keys("1400")
        inp16.send_keys(Keys.ENTER)
        time.sleep(1.0)
        is_victory_modal = driver.execute_script("""
            const m = document.getElementById('victory-celebration-modal');
            return m && (m.style.display === 'flex' || m.style.display === 'block');
        """)
        assert is_victory_modal, "Expected victory celebration modal to be active after Stage 16"
        print(f"[PASS] Stage 16: Submitted '1400' via Enter key -> Round 1 Victory Modal Displayed: True")
        results.append("Stage 16 (Enter key): PASS")

        # ----------------------------------------------------
        # PHASE 2: ROUND 2 DECRYPTION ARENA (15 PUZZLES)
        # ----------------------------------------------------
        print("\n=======================================================")
        print("--- PHASE 2: ROUND 2 PUZZLES 1 TO 15 TRANSMIT VERIFICATION ---")
        print("=======================================================")
        driver.execute_script("closeAllModals(); launchRound2Arena();")
        time.sleep(1.0)

        r2_answers = {
            1: "C",
            2: "BOTTOM LEFT",
            3: "5",
            4: "CIPHER",
            5: "SQUARES",
            6: "011",
            7: "CLEARANCE",
            8: "SE",
            9: "NONE",
            10: "RLRCK",
            11: "NODC",
            12: "102",
            13: "3-EMPTY",
            14: "FINALS",
            15: "ECLIPSE"
        }

        for pz_idx in range(1, 16):
            driver.execute_script(f"openRound2Modal({pz_idx});")
            time.sleep(0.3)

            modal_inp = driver.find_element(By.ID, "r2-modal-passcode-input")
            modal_inp.clear()
            sol = r2_answers[pz_idx]
            modal_inp.send_keys(sol)

            if pz_idx % 2 == 1:
                # Odd puzzles: Submit via Enter key
                modal_inp.send_keys(Keys.ENTER)
                method = "Enter key"
            else:
                # Even puzzles: Submit via Transmit Answer button click
                btn = driver.find_element(By.CSS_SELECTOR, "#r2-modal-submit-bar .r2-submit-btn")
                btn.click()
                method = "Transmit button"

            # Check immediate feedback (before auto-advance)
            time.sleep(0.25)
            fb_text = driver.find_element(By.ID, "r2-modal-submit-feedback").text
            assert "ACCREDITED" in fb_text or "decrypted successfully" in fb_text, (
                f"Failed for Puzzle {pz_idx} via {method}: feedback '{fb_text}'"
            )

            # Wait for auto-advance to process
            time.sleep(0.9)
            cleared = driver.execute_script("return round2StagesCleared;")
            assert pz_idx in cleared, f"Puzzle {pz_idx} was not recorded in round2StagesCleared: {cleared}"
            print(f"[PASS] Round 2 Puzzle {pz_idx:02d} ({sol}) submitted via {method} -> Feedback: {fb_text}")
            results.append(f"Round 2 Puzzle {pz_idx:02d} ({method}): PASS")

        # Verify Grand Victory celebration at Puzzle 15
        time.sleep(1.2)
        r2_cleared_all = driver.execute_script("return round2StagesCleared.length;")
        assert r2_cleared_all == 15, f"Expected 15 cleared puzzles, got {r2_cleared_all}"
        print(f"\n[PASS] All 15 Round 2 Puzzles Cleared! Championship Victory Triggered!")
        results.append("Round 2 Grand Victory: PASS")

        print("\n=============================================")
        print("ALL TESTS PASSED SUCCESSFULLY! COMPLETE SUMMARY:")
        print("=============================================")
        for r in results:
            print(f"  ✓ {r}")
        print(f"\nTotal Verified Transmits: {len(results)} / {len(results)} passed!")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
