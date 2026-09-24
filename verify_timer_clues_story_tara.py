import sys
import time

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_tests():
    print("=== STARTING COMPREHENSIVE VERIFICATION SUITE (SELENIUM) ===")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1600,1000")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    try:
        print("1. Loading http://localhost:8000/aditi_os_widget.html...")
        driver.get("http://localhost:8000/aditi_os_widget.html")
        time.sleep(2)

        # Dismiss team login modal for test execution
        driver.execute_script("""
            const modal = document.getElementById('team-auth-modal');
            if (modal) modal.style.display = 'none';
        """)

        # -------------------------------------------------------------
        # TEST 1: Timer Verification
        # -------------------------------------------------------------
        print("\n--- TEST 1: Mission Timer Tests ---")
        timer_el = driver.find_element(By.ID, "nexus-live-mission-timer")
        timer_text = timer_el.text.strip()
        print(f"Initial Timer Display: '{timer_text}'")
        assert timer_text and ("m" in timer_text or "s" in timer_text), "Timer must display minutes/seconds format"

        # Check elapsed seconds function
        elapsed_1 = driver.execute_script("return getMissionElapsedSeconds();")
        print(f"Elapsed seconds reported: {elapsed_1}s")
        assert elapsed_1 >= 0, "Elapsed seconds must be >= 0"

        # Wait 2 seconds and check increment
        time.sleep(2.2)
        timer_text_2 = driver.find_element(By.ID, "nexus-live-mission-timer").text.strip()
        elapsed_2 = driver.execute_script("return getMissionElapsedSeconds();")
        print(f"Timer after 2s: '{timer_text_2}', elapsed: {elapsed_2}s")
        assert elapsed_2 >= elapsed_1 + 1, "Timer must increment over time"

        # Test timer freezing when mission is completed
        driver.execute_script("""
            localStorage.setItem("failsafe_mission_completed", "true");
            localStorage.setItem("failsafe_final_elapsed_seconds", "845");
            if (typeof updateMissionTimerDisplay === 'function') updateMissionTimerDisplay();
        """)
        time.sleep(0.5)
        frozen_text = driver.find_element(By.ID, "nexus-live-mission-timer").text.strip()
        frozen_elapsed = driver.execute_script("return getMissionElapsedSeconds();")
        print(f"Frozen Timer text on completion: '{frozen_text}', elapsed: {frozen_elapsed}s")
        assert frozen_elapsed == 845, "Timer must return frozen 845 seconds when completed"
        assert "[FINAL]" in frozen_text, "Timer display must indicate [FINAL] when completed"

        # Reset back for subsequent tests
        driver.execute_script("""
            localStorage.removeItem("failsafe_mission_completed");
            localStorage.removeItem("failsafe_final_elapsed_seconds");
            if (typeof updateMissionTimerDisplay === 'function') updateMissionTimerDisplay();
        """)

        # -------------------------------------------------------------
        # TEST 2: Clues Budget (Strictly 3 Hints) & Display
        # -------------------------------------------------------------
        print("\n--- TEST 2: 3 Hints Lifeline Limit & Remaining Clues Display ---")
        driver.execute_script("""
            cluesRemaining = 3;
            cluesUsedStages.clear();
            localStorage.setItem('failsafe_clues_left', '3');
            localStorage.setItem('failsafe_clues_used_stages', '[]');
            updateClueBatteryDisplay();
        """)
        time.sleep(0.3)

        header_clues = driver.find_element(By.ID, "header-clues-count").text.strip()
        header_icons = driver.find_element(By.ID, "header-clues-icons").text.strip()
        chip_count = driver.find_element(By.ID, "tara-clue-chip-count").text.strip()
        comp_count = driver.find_element(By.ID, "clue-battery-count").get_attribute("textContent").strip()
        print(f"Initial Clues Display: Header count='{header_clues}', Header icons='{header_icons}', Chip='{chip_count}', Companion='{comp_count}'")
        assert "3/3" in header_clues, "Header must show 3/3 clues"
        assert "3/3" in chip_count, "Chip must show 3/3 clues"
        assert "3/3" in comp_count, "Companion box must show (3/3)"
        assert "🔋" in header_icons, "Header must show battery icons"

        # Request 1st Clue
        print("Requesting Clue 1 on Stage 1...")
        driver.execute_script("currentStage = 1; requestTacticalClue();")
        time.sleep(0.5)
        clues_left_1 = driver.execute_script("return cluesRemaining;")
        header_clues_1 = driver.find_element(By.ID, "header-clues-count").text.strip()
        speech_1 = driver.find_element(By.ID, "nexus-tara-speech").text.strip()
        print(f"After Clue 1: Remaining={clues_left_1}/3, Header='{header_clues_1}', TARA Speech='{speech_1[:60]}...'")
        assert clues_left_1 == 2, "Clues remaining must be 2 after 1st clue"
        assert "2/3" in header_clues_1, "Header must update to 2/3"

        # Try requesting on same stage again (should be blocked)
        print("Attempting duplicate clue request on Stage 1 (must be prevented)...")
        driver.execute_script("requestTacticalClue();")
        time.sleep(0.3)
        clues_left_dup = driver.execute_script("return cluesRemaining;")
        assert clues_left_dup == 2, "Duplicate clue on same stage must NOT deduct another clue"

        # Advance to Stage 2 and request 2nd clue
        print("Advancing to Stage 2 and requesting Clue 2...")
        driver.execute_script("currentStage = 2; requestTacticalClue();")
        time.sleep(0.3)
        clues_left_2 = driver.execute_script("return cluesRemaining;")
        header_clues_2 = driver.find_element(By.ID, "header-clues-count").text.strip()
        print(f"After Clue 2: Remaining={clues_left_2}/3, Header='{header_clues_2}'")
        assert clues_left_2 == 1, "Clues remaining must be 1 after 2nd clue"
        assert "1/3" in header_clues_2, "Header must update to 1/3"

        # Advance to Stage 3 and request 3rd clue
        print("Advancing to Stage 3 and requesting Clue 3 (Final Lifeline)...")
        driver.execute_script("currentStage = 3; requestTacticalClue();")
        time.sleep(0.3)
        clues_left_3 = driver.execute_script("return cluesRemaining;")
        header_clues_3 = driver.find_element(By.ID, "header-clues-count").text.strip()
        print(f"After Clue 3: Remaining={clues_left_3}/3, Header='{header_clues_3}'")
        assert clues_left_3 == 0, "Clues remaining must be 0 after 3rd clue"
        assert "0/3" in header_clues_3, "Header must update to 0/3"

        # Check button states when 0 clues remain
        chip_btn_text = driver.find_element(By.ID, "btn-tara-clue-chip").text.strip()
        print(f"Clue Chip button text when 0 clues left: '{chip_btn_text}'")
        assert "NO CLUES LEFT" in chip_btn_text, "Clue chip button must show NO CLUES LEFT"

        # Advance to Stage 4 and attempt 4th clue (strictly forbidden)
        print("Advancing to Stage 4 and attempting 4th clue (MUST BE STRICTLY BLOCKED)...")
        driver.execute_script("currentStage = 4; requestTacticalClue();")
        time.sleep(0.3)
        clues_left_blocked = driver.execute_script("return cluesRemaining;")
        speech_blocked = driver.find_element(By.ID, "nexus-tara-speech").text.strip()
        print(f"After 4th attempt: Remaining={clues_left_blocked}/3, TARA Speech='{speech_blocked[:60]}...'")
        assert clues_left_blocked == 0, "Clues count must remain 0"
        assert "ACCESS RESTRICTED" in speech_blocked or "expended" in speech_blocked, "TARA must warn that all 3 lifelines have been expended"

        # -------------------------------------------------------------
        # TEST 3: Storyline Explanation Modal
        # -------------------------------------------------------------
        print("\n--- TEST 3: Storyline Explanation Modal Tests ---")
        story_btn = driver.find_element(By.ID, "btn-open-storyline")
        assert story_btn is not None, "Storyline button must exist in top header"

        # Click Storyline button
        print("Clicking top header [📖 STORYLINE] button...")
        driver.execute_script("arguments[0].click();", story_btn)
        time.sleep(0.5)
        modal_style = driver.execute_script("return document.getElementById('modal-storyline-lore').style.display;")
        print(f"Storyline modal display: '{modal_style}'")
        assert modal_style == "flex", "Storyline modal must open with display: flex"

        # Check tabs
        origin_visible = driver.find_element(By.ID, "story-content-origin").is_displayed()
        assert origin_visible, "Storyline origin tab must be visible"

        print("Switching to '🚨 THE INCIDENT' tab...")
        tab_inc = driver.find_element(By.ID, "tab-story-incident")
        driver.execute_script("arguments[0].click();", tab_inc)
        time.sleep(0.3)
        incident_text = driver.find_element(By.ID, "story-content-incident").text
        assert "ISHAAN" in incident_text and "paranoia" in incident_text, "Incident text must explain ISHAAN and defensive paranoia"

        print("Switching to '🛡️ THE 16 FAILSAFES' tab...")
        tab_fs = driver.find_element(By.ID, "tab-story-failsafes")
        driver.execute_script("arguments[0].click();", tab_fs)
        time.sleep(0.3)
        failsafes_text = driver.find_element(By.ID, "story-content-failsafes").text
        assert "ACT I" in failsafes_text and "ACT V" in failsafes_text, "Failsafes text must detail the 5 Acts"

        print("Switching to '👁️ TARA & ROUND 2 OLYMPIAD' tab...")
        tab_tara = driver.find_element(By.ID, "tab-story-tara")
        driver.execute_script("arguments[0].click();", tab_tara)
        time.sleep(0.3)
        tara_tab_text = driver.find_element(By.ID, "story-content-tara").text
        assert "TARA" in tara_tab_text and "3" in tara_tab_text and "Olympiad" in tara_tab_text, "TARA tab must explain auxiliary role and 3 lifelines"

        # Close modal
        driver.execute_script("closeModal('modal-storyline-lore');")
        time.sleep(0.3)
        modal_closed = driver.execute_script("return document.getElementById('modal-storyline-lore').style.display;")
        assert modal_closed == "none", "Storyline modal must close"

        # Test TARA quick query for story
        print("Testing sendTaraQuick('story')...")
        driver.execute_script("sendTaraQuick('story');")
        time.sleep(0.4)
        modal_reopened = driver.execute_script("return document.getElementById('modal-storyline-lore').style.display;")
        assert modal_reopened == "flex", "sendTaraQuick('story') must open Storyline modal"
        driver.execute_script("closeModal('modal-storyline-lore');")

        # -------------------------------------------------------------
        # TEST 4: Make TARA Look Active
        # -------------------------------------------------------------
        print("\n--- TEST 4: TARA Visual & Interactive Activity Tests ---")
        live_pill = driver.find_element(By.CLASS_NAME, "tara-live-indicator")
        assert live_pill is not None, "TARA live indicator pill must exist"
        pill_text = live_pill.text.strip()
        print(f"TARA Live Indicator Pill text: '{pill_text}'")
        assert "ACTIVE" in pill_text, "TARA live indicator must show ACTIVE"

        anim_id = driver.execute_script("return taraEyeAnimId;")
        print(f"taraEyeAnimId: {anim_id}")
        assert anim_id is not None and anim_id > 0, "taraEyeAnimId must be active"

        print("Calling taraAvatarClicked()...")
        driver.execute_script("taraAvatarClicked();")
        time.sleep(0.4)
        speech_after_click = driver.find_element(By.ID, "nexus-tara-speech").text.strip()
        print(f"TARA Speech after avatar click: '{speech_after_click[:60]}...'")
        assert "TARA" in speech_after_click or "Operator" in speech_after_click or "beacon" in speech_after_click, "TARA must respond to avatar clicks with tactical voice line"

        # Capture a visual screenshot
        screenshot_path = "C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/test_tara_active_full.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot successfully captured at: {screenshot_path}")

        print("\n=======================================================")
        print("🎉 ALL TESTS PASSED SUCCESSFULLY! (4/4 FEATURES VERIFIED)")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
