import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--window-size=1600,1050")
driver = webdriver.Chrome(options=opts)
try:
    driver.get("http://localhost:8000/aditi_os_widget.html")
    time.sleep(2)
    driver.execute_script("""
        const auth = document.getElementById('team-auth-modal');
        if (auth) auth.style.display = 'none';
        openStorylineModal();
    """)
    time.sleep(1)
    driver.save_screenshot("C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/storyline_modal_overview.png")
    print("Screenshot saved successfully.")
finally:
    driver.quit()
