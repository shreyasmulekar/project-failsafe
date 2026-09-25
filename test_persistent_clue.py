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
    driver.get("http://localhost:8000")
    time.sleep(1)

    driver.execute_script("localStorage.clear(); localStorage.setItem('failsafe_current_round', '1');")
    driver.get("http://localhost:8000")
    time.sleep(2)

    team_inp = driver.find_element(By.ID, "auth-login-id")
    team_inp.clear()
    team_inp.send_keys("ALFA-1")

    pw_inp = driver.find_element(By.ID, "auth-login-pass")
    pw_inp.clear()
    pw_inp.send_keys("123456")

    login_btn = driver.find_element(By.CSS_SELECTOR, "#auth-login-form button[type='submit']")
    login_btn.click()
    time.sleep(3)

    # Dismiss tutorial
    driver.execute_script("""
        const tut = document.getElementById('tutorial-modal');
        if (tut) tut.style.display = 'none';
        const guide = document.getElementById('guide-modal');
        if (guide) guide.style.display = 'none';
        if (typeof hideTaraGuideBanner === 'function') hideTaraGuideBanner();
    """)
    time.sleep(1)

    # Trigger confirmClueUse() directly
    driver.execute_script("""
        if (typeof confirmClueUse === 'function') {
            confirmClueUse();
        }
    """)
    time.sleep(2)

    # Screenshot of persistent clue banner on desktop
    clue_desk_path = os.path.join(SCREENSHOT_DIR, "shot_verified_active_clue_on_desktop.png")
    driver.save_screenshot(clue_desk_path)
    print(f"[OK] Saved persistent clue on desktop: {clue_desk_path}")

    # Now open Stage 1 modal to verify clue banner is inside modal too
    driver.execute_script("if (typeof openModal === 'function') openModal('modal-origin');")
    time.sleep(1)
    clue_modal_path = os.path.join(SCREENSHOT_DIR, "shot_verified_active_clue_in_modal.png")
    driver.save_screenshot(clue_modal_path)
    print(f"[OK] Saved persistent clue in modal: {clue_modal_path}")

finally:
    driver.quit()
