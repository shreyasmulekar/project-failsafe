import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_recovery_terminal_test():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,900")
    
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # ==============================================================
        # 1. TEST STANDALONE ADI RECOVERY TERMINAL (adi_recovery_terminal.html)
        # ==============================================================
        print("\n==================================================")
        print("TEST 1: STANDALONE ADI RECOVERY TERMINAL")
        print("==================================================")
        html_path = os.path.abspath(r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\adi_recovery_terminal.html")
        driver.get(f"file:///{html_path.replace(os.sep, '/')}")
        
        # Verify Banner & Status Block
        banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".term-banner")))
        assert "ADI RECOVERY TERMINAL" in banner.text
        print("[PASS] Banner 'ADI RECOVERY TERMINAL' verified.")
        
        screen_text = driver.find_element(By.ID, "term-screen").text
        assert "CRITICAL" in screen_text
        assert "LOCKED" in screen_text
        assert "OFFLINE" in screen_text
        print("[PASS] System status (CRITICAL, LOCKED, OFFLINE) verified.")
        
        # Verify Command History & Recovery Log
        assert "LOGIN" in screen_text
        assert "VERIFY" in screen_text
        assert "██████" in screen_text
        assert "EXECUTE" in screen_text
        assert "LOCK" in screen_text
        print("[PASS] 5-Command history sequence verified.")
        
        assert "Establishes a user session" in screen_text
        assert "Confirms the user's identity" in screen_text
        assert "Gives permission to reach the core" in screen_text
        assert "Runs the requested operation" in screen_text
        assert "Secures the system" in screen_text
        print("[PASS] Recovery log descriptions verified.")
        
        assert "I remember what happened." in screen_text
        assert "One command has been erased." in screen_text
        assert "Recover it." in screen_text
        print("[PASS] ADI monologue verified.")
        
        # Test Invalid Command Rejection
        input_box = driver.find_element(By.ID, "terminal-cmd-input")
        submit_btn = driver.find_element(By.ID, "btn-submit")
        input_box.send_keys("SYSTEM_OVERRIDE")
        submit_btn.click()
        time.sleep(0.4)
        
        err_msg = driver.find_element(By.ID, "term-error-msg")
        assert err_msg.is_displayed()
        print("[PASS] Invalid command correctly rejected.")
        
        # Test Correct Command Submission: ACCESS
        input_box.clear()
        input_box.send_keys("ACCESS")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_terminal_before_access.png")
        submit_btn.click()
        time.sleep(0.8)
        
        # Verify Dramatic Reveal Screen
        reveal_panel = driver.find_element(By.ID, "panel-dramatic-reveal")
        assert reveal_panel.is_displayed()
        reveal_text = reveal_panel.text
        print("\nDramatic Reveal Output:\n" + reveal_text)
        
        assert "COMMAND ACCEPTED." in reveal_text
        assert "That was the command I was looking for." in reveal_text
        assert "Unfortunately, ACCESS is not enough." in reveal_text
        assert "NEW MESSAGE DETECTED." in reveal_text
        assert "RECOVERY TOKEN REQUIRED" in reveal_text
        assert "WHO you're giving access to." in reveal_text
        print("[PASS] Dramatic reveal escape-room narrative verified.")
        
        continue_btn = driver.find_element(By.ID, "btn-continue")
        assert continue_btn.is_displayed()
        print("[PASS] CONTINUE button active.")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_terminal_after_access.png")
        
        # ==============================================================
        # 2. TEST PROJECT FAILSAFE 1.0 (aditi_os_widget.html) WITH ACCESS
        # ==============================================================
        print("\n==================================================")
        print("TEST 2: PROJECT FAILSAFE 1.0 (aditi_os_widget.html)")
        print("==================================================")
        v1_path = os.path.abspath(r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\aditi_os_widget.html")
        driver.get(f"file:///{v1_path.replace(os.sep, '/')}")
        time.sleep(1.0)
        
        # Reset to stage 1
        driver.execute_script("localStorage.setItem('failsafe_stage', '1'); currentStage = 1;")
        
        # Check tactical card present
        rec_card = driver.find_element(By.ID, "card-recovery-term")
        assert rec_card.is_displayed()
        print("[PASS] Found 'ADI_Recovery.term' tactical card on desktop.")
        
        # Run checksum scan with ACCESS
        driver.execute_script("runChecksumScan('ACCESS');")
        time.sleep(0.8)
        
        current_stage = driver.execute_script("return currentStage;")
        print(f"[PASS] Solved Stage 1 with 'ACCESS'! Current stage in V1: {current_stage}")
        assert current_stage == 2, f"Expected Stage 2, got {current_stage}"
        
        # ==============================================================
        # 3. TEST PROJECT FAILSAFE 2.0 (index.html) WITH ACCESS
        # ==============================================================
        print("\n==================================================")
        print("TEST 3: PROJECT FAILSAFE 2.0 (index.html)")
        print("==================================================")
        v2_path = os.path.abspath(r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\project-failsafe-2.0\index.html")
        driver.get(f"file:///{v2_path.replace(os.sep, '/')}")
        time.sleep(1.0)
        
        # Dismiss team auth modal
        driver.execute_script("""
            if (typeof closeV2AuthModal === 'function') closeV2AuthModal();
            const m = document.getElementById('v2-team-auth-modal');
            if (m) m.style.display = 'none';
        """)
        
        # Reset to stage 1
        driver.execute_script("localStorage.setItem('failsafe_stage', '1'); currentStage = 1;")
        
        # Check RECOVERY chip present
        rec_chip = driver.find_element(By.ID, "chip-recovery")
        assert rec_chip.is_displayed()
        print("[PASS] Found '💻 RECOVERY' sector chip.")
        
        # Run checksum scan with ACCESS
        driver.execute_script("runChecksumScan('ACCESS');")
        time.sleep(0.8)
        
        v2_current_stage = driver.execute_script("return currentStage;")
        print(f"[PASS] Solved Stage 1 with 'ACCESS'! Current stage in V2: {v2_current_stage}")
        assert v2_current_stage == 2, f"Expected Stage 2, got {v2_current_stage}"
        
        print("\n==================================================")
        print("ALL TESTS PASSED: ADI RECOVERY TERMINAL 100% OPERATIONAL!")
        print("==================================================")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_recovery_terminal_test()
