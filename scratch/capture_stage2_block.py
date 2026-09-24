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
    currentStage = 2;
    updateNexusDashboard();
    openModal('modal-memory');
    v1MemOrder.sort((a, b) => a.min - b.min);
    renderV1MemoryCards();
    const modal = document.getElementById('modal-memory');
    const block = document.getElementById('v1-timeline-fixed-block');
    if (block) block.scrollIntoView({ behavior: 'instant', block: 'center' });
""")
time.sleep(1)

driver.save_screenshot("C:/Users/shrey\.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/screenshot_stage2_submission_block_visible.png")
driver.quit()
print("Saved screenshot_stage2_submission_block_visible.png successfully!")
