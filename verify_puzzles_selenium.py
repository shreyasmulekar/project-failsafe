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

try:
    print("[1] Opening Workstation...")
    driver.get("http://localhost:8000")
    time.sleep(2)

    # Check if login overlay is displayed or bypass it
    driver.execute_script("""
        localStorage.setItem('failsafe_auth_token', 'DEV_BYPASS_TOKEN');
        localStorage.setItem('failsafe_team_id', 'ALFA-1');
        localStorage.setItem('failsafe_team_name', 'TEAM ALFA');
        localStorage.setItem('failsafe_current_stage', '1');
        if (typeof showSystemNotice === 'function') {
            console.log('App ready');
        }
    """)
    driver.get("http://localhost:8000")
    time.sleep(2)

    # Close any login modal if open, ensure main desktop visible
    driver.execute_script("""
        const loginModal = document.getElementById('login-modal');
        if (loginModal) loginModal.style.display = 'none';
        const desk = document.getElementById('main-desktop') || document.body;
        if (desk) desk.style.display = 'block';
        if (typeof updateMissionHeader === 'function') updateMissionHeader();
        if (typeof renderNexusCards === 'function') renderNexusCards();
    """)
    time.sleep(1)

    # Take screenshot of Stage 1 Dashboard
    s1_path = os.path.join(SCREENSHOT_DIR, "shot_stage1_new_doc_1366x768.png")
    driver.save_screenshot(s1_path)
    print(f"[OK] Saved Stage 1 dashboard: {s1_path}")

    # Open Stage 1 Modal (Farewell.doc)
    driver.execute_script("if (typeof openModal === 'function') openModal('modal-origin');")
    time.sleep(1)
    s1_modal_path = os.path.join(SCREENSHOT_DIR, "shot_stage1_modal_origin_1366x768.png")
    driver.save_screenshot(s1_modal_path)
    print(f"[OK] Saved Stage 1 modal: {s1_modal_path}")

    # Test direct submission in Stage 1 modal
    res = driver.execute_script("""
        const input = document.getElementById('input-stage-1');
        if (input) {
            input.value = 'ORIGIN';
            if (typeof submitStageDirectKey === 'function') {
                submitStageDirectKey(1, 'ORIGIN');
                return 'Submitted ORIGIN via submitStageDirectKey';
            }
        }
        return 'submitStageDirectKey not found or input missing';
    """)
    print("[Stage 1 Direct Submission]:", res)
    time.sleep(2)

    # Take screenshot after Stage 1 solve
    s2_path = os.path.join(SCREENSHOT_DIR, "shot_stage2_new_puzzles_1366x768.png")
    driver.save_screenshot(s2_path)
    print(f"[OK] Saved post-solve screenshot: {s2_path}")

    # Open Stage 2 Modal (README.doc / ASCII)
    driver.execute_script("if (typeof openModal === 'function') openModal('modal-origin-readme');")
    time.sleep(1)
    s2_modal_path = os.path.join(SCREENSHOT_DIR, "shot_stage2_modal_readme_1366x768.png")
    driver.save_screenshot(s2_modal_path)
    print(f"[OK] Saved Stage 2 modal: {s2_modal_path}")

    # Open Stage 3 Modal (Incident_Logs.doc)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-incident-logs');
    """)
    time.sleep(1)
    s3_modal_path = os.path.join(SCREENSHOT_DIR, "shot_stage3_modal_calendar_1366x768.png")
    driver.save_screenshot(s3_modal_path)
    print(f"[OK] Saved Stage 3 modal: {s3_modal_path}")

    # Open Stage 9 Modal (Dark_Terminal.png Steganography)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-stego');
    """)
    time.sleep(1)
    s9_modal_path = os.path.join(SCREENSHOT_DIR, "shot_stage9_modal_stego_1366x768.png")
    driver.save_screenshot(s9_modal_path)
    print(f"[OK] Saved Stage 9 Steganography modal: {s9_modal_path}")

    # Open Stage 11 Modal (CLEARANCE_CODE.txt Binary)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-clearance');
    """)
    time.sleep(1)
    s11_modal_path = os.path.join(SCREENSHOT_DIR, "shot_stage11_modal_binary_1366x768.png")
    driver.save_screenshot(s11_modal_path)
    print(f"[OK] Saved Stage 11 Binary modal: {s11_modal_path}")

    # Open Puzzle Guide Modal
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-puzzles-guide');
    """)
    time.sleep(1)
    guide_path = os.path.join(SCREENSHOT_DIR, "shot_puzzles_guide_modal_1366x768.png")
    driver.save_screenshot(guide_path)
    print(f"[OK] Saved Puzzles Guide modal: {guide_path}")

finally:
    driver.quit()
    print("Selenium verification finished.")
