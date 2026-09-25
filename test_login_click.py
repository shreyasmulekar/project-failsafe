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

    # Click the submit button
    btn = driver.find_element(By.CSS_SELECTOR, "#auth-login-form button[type='submit']")
    btn.click()
    print("Clicked login button, waiting for workstation...")
    time.sleep(3)

    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "shot_test_desktop_after_login.png"))
    print("Saved shot_test_desktop_after_login.png")

finally:
    driver.quit()
