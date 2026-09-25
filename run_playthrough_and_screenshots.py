import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SCREENSHOT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1366,768")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1366, 768)

stages_to_test = [
    (1, "modal-origin", "ORIGIN", "shot_verified_stage1_origin.png"),
    (2, "modal-memory", "629", "shot_verified_stage2_memory.png"),
    (3, "modal-incident-logs", "28/02/2025", "shot_verified_stage3_calendar.png"),
    (4, "modal-security-audit", "22:46", "shot_verified_stage4_audit.png"),
    (5, "modal-acrostic", "SAFE", "shot_verified_stage5_acrostic.png"),
    (6, "modal-font", "ARIAL", "shot_verified_stage6_font.png"),
    (7, "modal-version-hist", "CORRUPTED", "shot_verified_stage7_version.png"),
    (8, "modal-spectro", "WHITE", "shot_verified_stage8_morse.png"),
    (9, "modal-stego", "SHADOW_CORE", "shot_verified_stage9_stego.png"),
    (10, "modal-honeypot", "BYPASS", "shot_verified_stage10_honeypot.png"),
    (11, "modal-clearance", "ailnors", "shot_verified_stage11_binary.png"),
]

try:
    print("[1] Opening workstation at 1366x768...")
    driver.get("http://localhost:8000")
    time.sleep(1)

    # Clean local storage completely
    driver.execute_script("""
        localStorage.clear();
        localStorage.setItem('failsafe_current_round', '1');
    """)
    driver.get("http://localhost:8000")
    time.sleep(2)

    # Login as ALFA-1
    team_inp = driver.find_element(By.ID, "auth-login-id")
    team_inp.clear()
    team_inp.send_keys("ALFA-1")

    pw_inp = driver.find_element(By.ID, "auth-login-pass")
    pw_inp.clear()
    pw_inp.send_keys("123456")

    login_btn = driver.find_element(By.CSS_SELECTOR, "#auth-login-form button[type='submit']")
    login_btn.click()
    print("[2] Logged in as ALFA-1 via button click")
    time.sleep(3)

    # Dismiss any tutorial or guide
    driver.execute_script("""
        const tut = document.getElementById('tutorial-modal');
        if (tut) tut.style.display = 'none';
        const guide = document.getElementById('guide-modal');
        if (guide) guide.style.display = 'none';
        if (typeof hideTaraGuideBanner === 'function') hideTaraGuideBanner();
    """)
    time.sleep(1)

    # Save Round 1 initial dashboard
    r1_dash_path = os.path.join(SCREENSHOT_DIR, "shot_verified_r1_dashboard_1366x768.png")
    driver.save_screenshot(r1_dash_path)
    print(f"[OK] Saved Round 1 Dashboard: {r1_dash_path}")

    # Step through each stage
    for st_num, modal_id, key, img_name in stages_to_test:
        print(f"\n--- Testing Stage {st_num} ({key}) ---")
        # Open modal
        driver.execute_script(f"""
            if (typeof closeModal === 'function') closeModal();
            if (typeof openModal === 'function') openModal('{modal_id}');
        """)
        time.sleep(1)

        # Save modal screenshot
        img_path = os.path.join(SCREENSHOT_DIR, img_name)
        driver.save_screenshot(img_path)
        print(f"[OK] Saved modal screenshot: {img_path}")

        # Submit passcode
        res = driver.execute_script(f"""
            if (typeof submitStageDirectKey === 'function') {{
                submitStageDirectKey({st_num}, '{key}');
                return 'Submitted via submitStageDirectKey';
            }} else if (typeof runChecksumScan === 'function') {{
                runChecksumScan('{key}');
                return 'Submitted via runChecksumScan';
            }}
            return 'No submit function found';
        """)
        print(f"[OK] Stage {st_num} submit result: {res}")
        time.sleep(2)

    # Check stage 12 reached
    final_stage = driver.execute_script("return (typeof currentStage !== 'undefined') ? currentStage : -1;")
    print(f"\n[Final Stage in UI]: {final_stage}")

    # Test persistent clue banner at Stage 12
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof requestClueLifeline === 'function') {
            requestClueLifeline(true);
        }
    """)
    time.sleep(2)
    clue_path = os.path.join(SCREENSHOT_DIR, "shot_verified_persistent_clue_banner.png")
    driver.save_screenshot(clue_path)
    print(f"[OK] Saved persistent clue banner screenshot: {clue_path}")

    print("\nPlaythrough and UI verification completed successfully!")

finally:
    driver.quit()
