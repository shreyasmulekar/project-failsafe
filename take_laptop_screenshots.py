import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1366,768')
driver = webdriver.Chrome(options=options)
driver.get('http://localhost:8000/aditi_os_widget.html')
time.sleep(1.5)

# Login
driver.find_element(By.ID, 'auth-login-id').send_keys('T-ALPHA')
driver.find_element(By.ID, 'auth-login-pass').send_keys('Password123!')
driver.find_element(By.ID, 'auth-login-form').submit()
time.sleep(2)

# Switch to Round 1
driver.execute_script("toggleRoundView();")
time.sleep(1.0)

# Open Stage 1 modal
driver.execute_script("openModal('modal-recovery');")
time.sleep(1.5)
driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\test_current_laptop_recovery_1366x768.png")

# Close and open Stage 8 (Stego)
driver.execute_script("closeModal('modal-recovery'); openModal('modal-stego');")
time.sleep(1.5)
driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\test_current_laptop_stego_1366x768.png")

# Close and open Puzzles Guide
driver.execute_script("closeModal('modal-stego'); openModal('modal-puzzles-guide');")
time.sleep(1.5)
driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\test_current_laptop_guide_1366x768.png")

driver.quit()
print("Done capturing modal screenshots.")
