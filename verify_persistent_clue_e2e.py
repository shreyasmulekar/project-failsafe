import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Ensure stdout doesn't crash on emoji in Windows console
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def setup_driver(width=1366, height=768):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument(f"--window-size={width},{height}")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        'width': width,
        'height': height,
        'deviceScaleFactor': 1,
        'mobile': False
    })
    return driver

def main():
    print("==================================================")
    print("STARTING E2E VERIFICATION: PERSISTENT CLUE DISPLAY")
    print("==================================================")
    
    driver = setup_driver(1366, 768)
    try:
        url = "http://localhost:8000/aditi_os_widget.html"
        driver.get(url)
        time.sleep(2)
        
        # 1. Reset state & Login team
        print("[1] Initializing Stage 01 team session...")
        driver.execute_script("""
            localStorage.clear();
            const team = {
                team_id: 'CLUE_SQUAD',
                team_name: 'Tactical Clue Squad',
                password: 'pass',
                members: 'Detective A, Detective B',
                round_1_started: true
            };
            localStorage.setItem('failsafe_server_url', 'http://localhost:8000');
            localStorage.setItem('failsafe_auth_team', JSON.stringify(team));
            localStorage.setItem('failsafe_team_id', 'CLUE_SQUAD');
            localStorage.setItem('failsafe_team_name', 'Tactical Clue Squad');
            localStorage.setItem('failsafe_round_1_started', 'true');
            localStorage.setItem('failsafe_stage', '1');
            localStorage.setItem('failsafe_clues_left', '3');
            localStorage.setItem('failsafe_clues_used_stages', '[]');
            applyAuthenticatedTeam(team);
            window.fullscreenExitApproved = false;
            fullscreenEnforcementActive = true;
            lockArmed = true;
            proctorLockActive = false;
        """)
        time.sleep(2)
        
        # 2. Verify initial state: Clue banner is NOT visible
        print("[2] Verifying initial clue banner is hidden...")
        banner = driver.find_element(By.ID, "active-clue-banner")
        is_visible = banner.is_displayed()
        print(f"Clue banner visible initially: {is_visible}")
        assert not is_visible, "Clue banner must be hidden before a clue is used!"

        # 3. Expend Clue on Stage 01
        print("[3] Expending a clue on Stage 01...")
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(1)

        is_visible = banner.is_displayed()
        print(f"Clue banner visible after clue request: {is_visible}")
        assert is_visible, "Clue banner must now be displayed on the page!"

        clue_text = driver.find_element(By.ID, "active-clue-text").text
        print(f"Clue banner text: {repr(clue_text)}")
        assert "boot lifecycle" in clue_text or "LOGIN -> VERIFY" in clue_text, "Clue banner must show Stage 01 hint!"

        # Take screenshot of page with active clue banner
        shot_on_page = os.path.join(ARTIFACT_DIR, "shot_active_clue_on_page_1366x768.png")
        driver.save_screenshot(shot_on_page)
        print(f"Saved screenshot: {shot_on_page}")

        # 4. Open Stage 01 Evidence Modal and verify clue is also pinned inside modal
        print("[4] Opening Stage 01 evidence modal...")
        driver.execute_script("openActiveStageModal();")
        time.sleep(1)

        modal_banner = driver.find_element(By.CLASS_NAME, "tara-modal-guide-banner")
        modal_banner_text = modal_banner.text
        print(f"Modal banner content contains clue: {'UNLOCKED TACTICAL CLUE' in modal_banner_text}")
        assert "UNLOCKED TACTICAL CLUE" in modal_banner_text or "boot lifecycle" in modal_banner_text, "Modal must also display the unlocked clue!"

        shot_in_modal = os.path.join(ARTIFACT_DIR, "shot_active_clue_in_modal_1366x768.png")
        driver.save_screenshot(shot_in_modal)
        print(f"Saved screenshot: {shot_in_modal}")

        # Close modal
        driver.execute_script("closeModal('modal-recovery-term');")
        time.sleep(1)

        # 5. Check Persistence: wait 4 seconds to verify it doesn't disappear like a toast
        print("[5] Waiting 4 seconds to verify clue remains persistently visible on the page...")
        time.sleep(4)
        is_still_visible = banner.is_displayed()
        print(f"Clue banner still visible after waiting: {is_still_visible}")
        assert is_still_visible, "Clue banner MUST stay visible on page while working on this question!"

        # 6. Advance to Next Question (Solve Stage 01 -> Stage 02)
        print("[6] Submitting correct answer 'ACCESS' to advance to Stage 02...")
        driver.execute_script("handleCommand('decrypt ACCESS');")
        time.sleep(1.5)

        curr_stage = driver.execute_script("return currentStage;")
        print(f"Current stage after solving Stage 01: {curr_stage}")
        assert curr_stage == 2, f"Should advance to Stage 2, got {curr_stage}"

        # 7. Verify clue banner automatically disappears when advancing to next question
        print("[7] Verifying clue banner is now hidden on Stage 02...")
        is_visible_stage2 = banner.is_displayed()
        print(f"Clue banner visible on Stage 02: {is_visible_stage2}")
        assert not is_visible_stage2, "Clue banner MUST hide when participant goes to the next question!"

        shot_stage2_clean = os.path.join(ARTIFACT_DIR, "shot_stage2_no_clue_1366x768.png")
        driver.save_screenshot(shot_stage2_clean)
        print(f"Saved screenshot: {shot_stage2_clean}")

        # 8. Request clue on Stage 02 and verify Stage 02's clue stays on page
        print("[8] Requesting clue on Stage 02...")
        driver.execute_script("confirmExecuteTacticalClue();")
        time.sleep(1)

        is_visible_stage2_clue = banner.is_displayed()
        print(f"Clue banner visible after Stage 02 clue request: {is_visible_stage2_clue}")
        assert is_visible_stage2_clue, "Clue banner must display Stage 02 clue!"

        clue_text_stage2 = driver.find_element(By.ID, "active-clue-text").text
        print(f"Stage 02 Clue text: {repr(clue_text_stage2)}")
        assert "timestamps" in clue_text_stage2 or "chronologically" in clue_text_stage2, "Clue banner must show Stage 02 hint!"

        shot_stage2_clue = os.path.join(ARTIFACT_DIR, "shot_stage2_clue_active_1366x768.png")
        driver.save_screenshot(shot_stage2_clue)
        print(f"Saved screenshot: {shot_stage2_clue}")

        # 9. Verify on 1280x720 small laptop screen
        print("[9] Testing 1280x720 small laptop screen fit...")
        driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 1280,
            'height': 720,
            'deviceScaleFactor': 1,
            'mobile': False
        })
        time.sleep(1)
        shot_laptop_1280 = os.path.join(ARTIFACT_DIR, "shot_active_clue_1280x720.png")
        driver.save_screenshot(shot_laptop_1280)
        print(f"Saved screenshot: {shot_laptop_1280}")

        print("\n==================================================")
        print("PERSISTENT CLUE VERIFICATION PASSED (100%)!")
        print("==================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
