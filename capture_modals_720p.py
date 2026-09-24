import os, sys, time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1280,720')
driver = webdriver.Edge(options=options)
try:
    driver.get('http://127.0.0.1:8000/aditi_os_widget.html')
    time.sleep(1)
    driver.execute_script("""
        const auth = document.getElementById('team-auth-modal');
        if (auth) auth.style.display = 'none';
        openModal('modal-recovery');
    """)
    time.sleep(0.5)
    driver.save_screenshot(r'C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\test_modal_recovery_720p.png')
    
    driver.execute_script("""
        closeModal('modal-recovery');
        launchRound2Arena();
        openRound2Modal(1);
    """)
    time.sleep(0.5)
    driver.save_screenshot(r'C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\test_modal_r2_dossier_720p.png')
    print('Screenshots taken successfully')
finally:
    driver.quit()
