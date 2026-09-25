import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ARTIFACTS_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def get_driver(width=1366, height=768):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument(f'--window-size={width},{height}')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:8000/aditi_os_widget.html')
    time.sleep(1.5)
    # Login
    try:
        driver.find_element(By.ID, 'auth-login-id').send_keys('T-ALPHA')
        driver.find_element(By.ID, 'auth-login-pass').send_keys('Password123!')
        driver.find_element(By.ID, 'auth-login-form').submit()
        time.sleep(1.5)
    except Exception as e:
        print("Login exception or already logged in:", e)
    return driver

print("Capturing 1366x768 views...")
driver = get_driver(1366, 768)

# 1. Round 1 Dashboard
driver.execute_script("if(typeof currentRoundView !== 'undefined' && currentRoundView === 2) toggleRoundView();")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_r1_dash_1366x768.png"))

# 2. Stage 1 (Ishaan Recovery) Modal
driver.execute_script("openModal('modal-recovery');")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_stage1_1366x768.png"))

# 3. Stage 5 (Stego) Modal
driver.execute_script("closeModal('modal-recovery'); openModal('modal-stego');")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_stage5_stego_1366x768.png"))

# 4. Stage 10 (Honeypot) Modal
driver.execute_script("closeModal('modal-stego'); openModal('modal-honeypot');")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_stage10_honeypot_1366x768.png"))

# 5. Clue Confirm Modal
driver.execute_script("closeModal('modal-honeypot'); requestTacticalClue('modal-whiteout');")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_clue_confirm_1366x768.png"))

# 6. Round 2 Dashboard & Matrix
driver.execute_script("closeModal('modal-clue-confirm'); toggleRoundView();")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_r2_dash_1366x768.png"))

# 7. Round 2 Matrix / Puzzle Modal
driver.execute_script("openRound2Modal(1);")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_r2_matrix_1366x768.png"))

# 8. Round 2 3D Rotation Cube (puzzle 5)
driver.execute_script("openRound2Modal(5);")
time.sleep(1)
driver.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_r2_cube_1366x768.png"))

driver.quit()

print("Capturing 1280x720 views...")
driver720 = get_driver(1280, 720)
driver720.execute_script("if(typeof currentRoundView !== 'undefined' && currentRoundView === 2) toggleRoundView();")
time.sleep(1)
driver720.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_r1_dash_1280x720.png"))

driver720.execute_script("openModal('modal-stego');")
time.sleep(1)
driver720.save_screenshot(os.path.join(ARTIFACTS_DIR, "shot_laptop_stage5_stego_1280x720.png"))

driver720.quit()
print("All screenshots captured successfully.")
