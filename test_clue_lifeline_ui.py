import sys
sys.stdout.reconfigure(encoding='utf-8')
import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def post(endpoint, data):
    req = urllib.request.Request(
        f"http://localhost:8000{endpoint}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode('utf-8'))

def run_clue_ui_test():
    team_name = "CLUE_VERIFY_TEAM"
    team_id = f"CLUE-{int(time.time())}"

    # Register team directly with server API
    reg = post("/api/teams/register", {
        "team_id": team_id,
        "team_name": team_name,
        "password": "pass",
        "leader_name": "Clue Tester"
    })
    print("Server registration response:", reg.get("message"))

    # Ensure Round 1 is started
    post("/api/admin/start_round_1", {"pin": "admin"})

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        url = "http://localhost:8000"
        print(f"Navigating to {url}...")
        driver.get(url)
        time.sleep(2)

        # Clear localStorage and set registered team credentials
        driver.execute_script(f"""
            localStorage.clear();
            sessionStorage.clear();
            localStorage.setItem('failsafe_current_team', JSON.stringify({{
                team_name: '{team_name}',
                team_id: '{team_id}'
            }}));
            localStorage.setItem('failsafe_current_round', '1');
            localStorage.setItem('failsafe_current_stage', '1');
            localStorage.setItem('failsafe_stage', '1');
            localStorage.setItem('failsafe_clues_left', '3');
            localStorage.setItem('failsafe_clues_used_stages', '[]');
            location.reload();
        """)
        time.sleep(2)

        # Wait for workspace to be active
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nexus-cards-grid"))
        )
        print("Workstation loaded successfully.")

        # Check clue battery count
        battery_count = driver.execute_script("return document.getElementById('clue-battery-count')?.innerText || ''")
        print(f"Initial Clue Battery Display: {battery_count}")
        assert "3/3" in battery_count, f"Expected (3/3), got {battery_count}"

        # Open Stage 01 modal
        print("Opening Stage 01 modal...")
        driver.execute_script("openActiveStageModal(1);")
        time.sleep(2)

        # Check if in-modal clue card exists
        has_clue_btn = driver.execute_script("""
            const modal = document.getElementById('modal-origin');
            const clueBtn = modal?.querySelector('.btn-modal-request-clue');
            return clueBtn !== null && clueBtn !== undefined;
        """)
        print(f"In-Modal Clue Request Button Present: {has_clue_btn}")
        assert has_clue_btn, "In-modal clue request button should be present in Stage 01 modal"

        # Trigger clue request
        print("Triggering clue request...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(1)

        # Verify confirmation modal is visible and check z-index
        confirm_modal_display = driver.execute_script("""
            const m = document.getElementById('modal-clue-confirm');
            const style = window.getComputedStyle(m);
            return {
                display: style.display,
                zIndex: style.zIndex,
                text: m.innerText
            };
        """)
        print(f"Confirmation Modal Display: {confirm_modal_display['display']} | zIndex: {confirm_modal_display['zIndex']}")
        assert confirm_modal_display['display'] != 'none', "Confirm modal should be visible!"
        assert "2:00" in confirm_modal_display['text'] or "2 MINUTES" in confirm_modal_display['text'], "Confirmation modal must mention 2 minutes penalty!"

        # Save screenshot of confirmation modal
        driver.save_screenshot("shot_clue_confirmation_dialog.png")
        print("Saved screenshot: shot_clue_confirmation_dialog.png")

        # Confirm clue expenditure
        print("Executing clue confirmation...")
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(2)

        # Verify state after clue used:
        state_after = driver.execute_script("""
            return {
                cluesRemaining: parseInt(localStorage.getItem('failsafe_clues_left') || '0', 10),
                penaltySeconds: localStorage.getItem('failsafe_penalty_seconds'),
                hintsUsedCount: localStorage.getItem('failsafe_hints_used_count'),
                activeBannerDisplay: document.getElementById('active-clue-banner')?.style.display,
                activeBannerText: document.getElementById('active-clue-text')?.innerText
            };
        """)
        print("State after clue consumption:", json.dumps(state_after, indent=2))
        assert state_after['cluesRemaining'] == 2, f"Expected 2 clues left, got {state_after['cluesRemaining']}"
        assert int(state_after['penaltySeconds']) >= 120, f"Expected penalty >= 120s, got {state_after['penaltySeconds']}"
        assert state_after['activeBannerDisplay'] == 'flex', "Active clue banner must be displayed!"

        # Save screenshot of active clue banner
        driver.save_screenshot("shot_clue_revealed_and_active_banner.png")
        print("Saved screenshot: shot_clue_revealed_and_active_banner.png")

        # Solve Stage 01
        print("Submitting key 'ORIGIN' for Stage 01...")
        driver.execute_script("submitStageDirectKey(1, 'ORIGIN');")
        time.sleep(3)

        # Verify Stage 01 solved and active banner dismissed for Stage 02
        stage_after = driver.execute_script("""
            return {
                stage: parseInt(localStorage.getItem('failsafe_stage') || localStorage.getItem('failsafe_current_stage') || '1', 10),
                activeBannerDisplay: document.getElementById('active-clue-banner')?.style.display
            };
        """)
        print("Stage after solve:", stage_after)
        assert stage_after['stage'] == 2, f"Expected stage 2, got {stage_after['stage']}"
        assert stage_after['activeBannerDisplay'] == 'none', "Active clue banner should dismiss upon advancing to next stage!"

        # Test Round 2: Switch to Round 2 and verify clues are strictly disabled
        print("Testing Round 2 clue protocol...")
        driver.execute_script("""
            localStorage.setItem('failsafe_current_round', '2');
            if (typeof enforceRound2NoCluesProtocol === 'function') enforceRound2NoCluesProtocol();
            if (typeof switchRoundTab === 'function') switchRoundTab(2);
        """)
        time.sleep(1)

        r2_state = driver.execute_script("""
            return {
                clueBtnDisplay: document.getElementById('btn-ethan-clue')?.style.display,
                batteryDisplay: document.getElementById('clue-battery-container')?.style.display
            };
        """)
        print("Round 2 state:", r2_state)
        assert r2_state['clueBtnDisplay'] == 'none', "Clue button must be hidden in Round 2!"

        print("\n[SUCCESS] ALL CLUE LIFELINE AND CONFIRMATION TESTS PASSED 100%!")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_clue_ui_test()
