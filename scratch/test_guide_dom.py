import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=1400,900')
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost:8000/aditi_os_widget.html')
time.sleep(1.5)

driver.execute_script("""
    const auth = document.getElementById("team-auth-modal");
    if (auth) auth.style.display = "none";
    currentTeam = { team_id: 'TEAM-01', team_name: 'Alpha Cyber Unit' };
    openModal("modal-puzzles-guide");
""")
time.sleep(1)

driver.save_screenshot("C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/screenshot_guide_modal_direct.png")
driver.quit()
print("Saved screenshot_guide_modal_direct.png successfully!")
