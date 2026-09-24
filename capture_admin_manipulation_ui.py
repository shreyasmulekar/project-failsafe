import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
URL = "http://127.0.0.1:8000/admin.html"

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

        # Authenticate admin
        driver.execute_script("""
            sessionStorage.setItem('failsafe_admin_authenticated', 'true');
            sessionStorage.setItem('admin_pin', 'wie-admin-2026');
            const m = document.getElementById('admin-login-modal');
            if (m) m.style.display = 'none';
            if (typeof fetchLeaderboardData === 'function') fetchLeaderboardData();
        """)
        time.sleep(2)

        # 1. Main Admin Console Table
        path1 = os.path.join(ARTIFACT_DIR, "screenshot_admin_command_center_table.png")
        driver.save_screenshot(path1)
        print("Captured:", path1)

        # 2. Open Team Telemetry Inspector for first available team
        driver.execute_script("""
            if (cachedTeams && cachedTeams.length > 0) {
                showTeamTelemetry(cachedTeams[0].team_id);
            }
        """)
        time.sleep(1)
        path2 = os.path.join(ARTIFACT_DIR, "screenshot_admin_telemetry_modal.png")
        driver.save_screenshot(path2)
        print("Captured:", path2)

        # 3. Open Team Edit Manipulation Modal
        driver.execute_script("""
            closeModal('modal-team-telemetry');
            if (cachedTeams && cachedTeams.length > 0) {
                openEditTeamModal(cachedTeams[0].team_id);
            }
        """)
        time.sleep(1)
        path3 = os.path.join(ARTIFACT_DIR, "screenshot_admin_edit_team_modal.png")
        driver.save_screenshot(path3)
        print("Captured:", path3)

        # 4. Open Shortlist Modal
        driver.execute_script("""
            closeModal('modal-edit-team');
            if (typeof openShortlistModal === 'function') {
                openShortlistModal();
            }
        """)
        time.sleep(1.5)
        path4 = os.path.join(ARTIFACT_DIR, "screenshot_admin_shortlist_modal.png")
        driver.save_screenshot(path4)
        print("Captured:", path4)

    finally:
        driver.quit()

if __name__ == "__main__":
    capture()
