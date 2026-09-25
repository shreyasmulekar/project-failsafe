import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SCREENSHOT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
GAME_STATE_PATH = r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\data\game_state.json"

# Reset ALFA-1 stage to 1 in game_state.json
with open(GAME_STATE_PATH, "r", encoding="utf-8") as f:
    state = json.load(f)

if "ALFA-1" in state.get("teams", {}):
    state["teams"]["ALFA-1"]["current_stage"] = 1
    state["teams"]["ALFA-1"]["unlocked_stages"] = [1]
    state["teams"]["ALFA-1"]["is_locked"] = False
    state["teams"]["ALFA-1"]["remote_unlock"] = True
    state["teams"]["ALFA-1"]["is_finished"] = False
    state["teams"]["ALFA-1"]["force_logout"] = False
    state["teams"]["ALFA-1"]["hints_count"] = 0
    state["round_1_started"] = True

with open(GAME_STATE_PATH, "w", encoding="utf-8") as f:
    json.dump(state, f, indent=2)

print("[OK] Reset ALFA-1 to Stage 1")

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1366,768")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1366, 768)

try:
    print("[1] Opening Workstation at 1366x768...")
    driver.get("http://localhost:8000")
    time.sleep(2)

    # Fill login form
    team_input = driver.find_element(By.ID, "auth-login-id")
    team_input.clear()
    team_input.send_keys("ALFA-1")

    pw_input = driver.find_element(By.ID, "auth-login-pass")
    pw_input.clear()
    pw_input.send_keys("123456")

    form = driver.find_element(By.ID, "auth-login-form")
    form.submit()
    print("[OK] Submitted login form")
    time.sleep(3)

    # Dismiss any tutorial or popup if present
    driver.execute_script("""
        const tut = document.getElementById('tutorial-modal');
        if (tut) tut.style.display = 'none';
        const guide = document.getElementById('guide-modal');
        if (guide) guide.style.display = 'none';
        if (typeof hideTaraGuideBanner === 'function') hideTaraGuideBanner();
    """)

    # Screenshot 1: Main Desktop at Stage 1
    s1_dash = os.path.join(SCREENSHOT_DIR, "shot_ui_stage1_dash_1366x768.png")
    driver.save_screenshot(s1_dash)
    print(f"[OK] Saved Stage 1 dashboard: {s1_dash}")

    # Open Stage 1 Modal (Farewell.doc)
    driver.execute_script("if (typeof openModal === 'function') openModal('modal-origin');")
    time.sleep(1)
    s1_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage1_modal_farewell_1366x768.png")
    driver.save_screenshot(s1_modal)
    print(f"[OK] Saved Stage 1 Farewell.doc modal: {s1_modal}")

    # Submit ORIGIN in Stage 1 modal direct input
    driver.execute_script("""
        const inp = document.getElementById('input-stage-1');
        if (inp) {
            inp.value = 'ORIGIN';
            submitStageDirectKey(1, 'ORIGIN');
        }
    """)
    print("[OK] Submitted ORIGIN for Stage 1")
    time.sleep(2)

    # Screenshot 2: Stage 2 Dashboard
    s2_dash = os.path.join(SCREENSHOT_DIR, "shot_ui_stage2_dash_1366x768.png")
    driver.save_screenshot(s2_dash)
    print(f"[OK] Saved Stage 2 dashboard: {s2_dash}")

    # Open Stage 2 Modal (README.doc / ASCII)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-origin-readme');
    """)
    time.sleep(1)
    s2_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage2_modal_readme_1366x768.png")
    driver.save_screenshot(s2_modal)
    print(f"[OK] Saved Stage 2 README modal: {s2_modal}")

    # Submit 629 for Stage 2
    driver.execute_script("""
        const inp = document.getElementById('input-stage-2');
        if (inp) {
            inp.value = '629';
            submitStageDirectKey(2, '629');
        }
    """)
    print("[OK] Submitted 629 for Stage 2")
    time.sleep(2)

    # Open Stage 3 Modal (Incident_Logs.doc / Non-leap year)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-incident-logs');
    """)
    time.sleep(1)
    s3_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage3_modal_calendar_1366x768.png")
    driver.save_screenshot(s3_modal)
    print(f"[OK] Saved Stage 3 modal: {s3_modal}")

    # Open Stage 4 Modal (Security_Audit.pdf / Murder Mystery)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-security-audit');
    """)
    time.sleep(1)
    s4_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage4_modal_audit_1366x768.png")
    driver.save_screenshot(s4_modal)
    print(f"[OK] Saved Stage 4 modal: {s4_modal}")

    # Open Stage 5 Modal (Aditi_Memo.doc / Acrostic SAFE)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-acrostic');
    """)
    time.sleep(1)
    s5_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage5_modal_acrostic_1366x768.png")
    driver.save_screenshot(s5_modal)
    print(f"[OK] Saved Stage 5 modal: {s5_modal}")

    # Open Stage 6 Modal (Which Aditi Is Real? Font style)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-font');
    """)
    time.sleep(1)
    s6_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage6_modal_font_1366x768.png")
    driver.save_screenshot(s6_modal)
    print(f"[OK] Saved Stage 6 modal: {s6_modal}")

    # Open Stage 7 Modal (Revision History Conflict)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-version-hist');
    """)
    time.sleep(1)
    s7_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage7_modal_version_1366x768.png")
    driver.save_screenshot(s7_modal)
    print(f"[OK] Saved Stage 7 modal: {s7_modal}")

    # Open Stage 9 Modal (Steganography Mask)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-stego');
    """)
    time.sleep(1)
    s9_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage9_modal_stego_1366x768.png")
    driver.save_screenshot(s9_modal)
    print(f"[OK] Saved Stage 9 modal: {s9_modal}")

    # Open Stage 11 Modal (Binary Master)
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof openModal === 'function') openModal('modal-clearance');
    """)
    time.sleep(1)
    s11_modal = os.path.join(SCREENSHOT_DIR, "shot_ui_stage11_modal_binary_1366x768.png")
    driver.save_screenshot(s11_modal)
    print(f"[OK] Saved Stage 11 modal: {s11_modal}")

    # Request a lifeline clue and verify persistent banner
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof requestClueLifeline === 'function') {
            requestClueLifeline(true);
        }
    """)
    time.sleep(2)
    s_clue = os.path.join(SCREENSHOT_DIR, "shot_ui_persistent_clue_banner_1366x768.png")
    driver.save_screenshot(s_clue)
    print(f"[OK] Saved persistent clue screenshot: {s_clue}")

finally:
    driver.quit()
    print("UI verification finished.")
