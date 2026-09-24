import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
URL = "http://127.0.0.1:8000/aditi_os_widget.html"

def capture():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        driver.get(URL)
        time.sleep(1.5)

        # Authenticate and dismiss login modal
        driver.execute_script("""
            localStorage.setItem('failsafe_auth_team', JSON.stringify({
                team_id: 'TEAM-01',
                team_name: 'Quantum Phantoms',
                password: 'wie2026',
                members: 'Alice, Bob, Charlie'
            }));
            const m = document.getElementById('team-auth-modal');
            if (m) m.style.display = 'none';
            if (typeof updateNexusDashboard === 'function') updateNexusDashboard();
        """)
        time.sleep(1)

        # 1. Capture Main Nexus Dashboard
        path1 = os.path.join(ARTIFACT_DIR, "screenshot_nexus_2090_dashboard.png")
        driver.save_screenshot(path1)
        print("Captured:", path1)

        # 2. Trigger Tara Where to Look
        driver.execute_script("""
            if (typeof triggerTaraWhereToLook === 'function') triggerTaraWhereToLook();
        """)
        time.sleep(1)
        path2 = os.path.join(ARTIFACT_DIR, "screenshot_tara_guidance_beacon.png")
        driver.save_screenshot(path2)
        print("Captured:", path2)

        # 3. Open Stage 01 Modal (Click to expand)
        driver.execute_script("""
            if (typeof openActiveStageModal === 'function') openActiveStageModal();
        """)
        time.sleep(1)
        path3 = os.path.join(ARTIFACT_DIR, "screenshot_nexus_expanded_dossier_modal.png")
        driver.save_screenshot(path3)
        print("Captured:", path3)

    finally:
        driver.quit()

if __name__ == "__main__":
    capture()
