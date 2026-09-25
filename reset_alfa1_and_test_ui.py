import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SCREENSHOT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
GAME_STATE_PATH = r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\data\game_state.json"

# Reset game state
with open(GAME_STATE_PATH, "r", encoding="utf-8") as f:
    state = json.load(f)

# Clear broadcasts
state["broadcasts"] = []
state["round_1_started"] = True

if "ALFA-1" in state.get("teams", {}):
    team = state["teams"]["ALFA-1"]
    team["current_round"] = 1
    team["current_stage"] = 1
    team["unlocked_stages"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    team["round_2_unlocked"] = False
    team["send_to_round_2"] = False
    team["is_finished"] = False
    team["is_locked"] = False
    team["remote_unlock"] = True
    team["force_logout"] = False
    team["hints_count"] = 0
    team["traps_count"] = 0
    team["last_action"] = "Ready in Round 1"

with open(GAME_STATE_PATH, "w", encoding="utf-8") as f:
    json.dump(state, f, indent=2)

print("[OK] Reset ALFA-1 to Round 1 in game_state.json")

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
    time.sleep(1)

    # Clear all previous local storage
    driver.execute_script("""
        localStorage.clear();
        localStorage.setItem('failsafe_current_round', '1');
    """)
    driver.get("http://localhost:8000")
    time.sleep(2)

    # Fill login form
    team_input = driver.find_element(By.ID, "auth-login-id")
    team_input.clear()
    team_input.send_keys("ALFA-1")

    pw_input = driver.find_element(By.ID, "auth-login-pass")
    pw_input.clear()
    pw_input.send_keys("123456")

    driver.find_element(By.ID, "auth-login-form").submit()
    print("[OK] Submitted login form")
    time.sleep(2)

    # Dismiss any tutorial overlay, ensure round 1 is active
    driver.execute_script("""
        const tut = document.getElementById('tutorial-modal');
        if (tut) tut.style.display = 'none';
        const guide = document.getElementById('guide-modal');
        if (guide) guide.style.display = 'none';
        if (typeof hideTaraGuideBanner === 'function') hideTaraGuideBanner();
        if (typeof switchRound === 'function') switchRound(1);
    """)
    time.sleep(1)

    # 1. Round 1 Dashboard View
    s_r1_dash = os.path.join(SCREENSHOT_DIR, "shot_r1_dash_new_puzzles_1366x768.png")
    driver.save_screenshot(s_r1_dash)
    print(f"[OK] Saved Round 1 dashboard: {s_r1_dash}")

    # Inspect each modal in sequence:
    modals = [
        (1, "modal-origin", "shot_stage1_farewell_doc_1366x768.png"),
        (2, "modal-memory", "shot_stage2_readme_doc_1366x768.png"),
        (3, "modal-incident-logs", "shot_stage3_incident_logs_doc_1366x768.png"),
        (4, "modal-security-audit", "shot_stage4_security_audit_pdf_1366x768.png"),
        (5, "modal-acrostic", "shot_stage5_aditi_memo_doc_1366x768.png"),
        (6, "modal-font", "shot_stage6_font_verification_1366x768.png"),
        (7, "modal-version-hist", "shot_stage7_revision_history_1366x768.png"),
        (8, "modal-spectro", "shot_stage8_morse_audio_1366x768.png"),
        (9, "modal-stego", "shot_stage9_stego_dark_terminal_1366x768.png"),
        (10, "modal-honeypot", "shot_stage10_honeypot_trap_1366x768.png"),
        (11, "modal-clearance", "shot_stage11_binary_clearance_1366x768.png"),
        (99, "modal-puzzles-guide", "shot_modal_puzzles_guide_1366x768.png")
    ]

    for st_num, m_id, img_name in modals:
        driver.execute_script(f"""
            if (typeof closeModal === 'function') closeModal();
            if (typeof openModal === 'function') openModal('{m_id}');
        """)
        time.sleep(1)
        target_path = os.path.join(SCREENSHOT_DIR, img_name)
        driver.save_screenshot(target_path)
        print(f"[OK] Saved Stage {st_num} Modal ({m_id}): {target_path}")

    # Now test clue request & persistent clue banner
    driver.execute_script("""
        if (typeof closeModal === 'function') closeModal();
        if (typeof requestClueLifeline === 'function') {
            requestClueLifeline(true);
        }
    """)
    time.sleep(2)
    s_clue = os.path.join(SCREENSHOT_DIR, "shot_r1_active_clue_banner_1366x768.png")
    driver.save_screenshot(s_clue)
    print(f"[OK] Saved active clue banner: {s_clue}")

finally:
    driver.quit()
    print("All UI checks complete.")
