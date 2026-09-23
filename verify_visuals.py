import os
import sys
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
SERVER_PORT = 8096

def run():
    env = os.environ.copy()
    env["PORT"] = str(SERVER_PORT)
    server = subprocess.Popen([sys.executable, "server.py"], cwd=os.getcwd(), env=env)
    time.sleep(2)

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        url = f"http://127.0.0.1:{SERVER_PORT}/aditi_os_widget.html"
        driver.get(url)
        time.sleep(1)

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
            if (typeof currentTeam !== 'undefined') {
                currentTeam = {
                    team_id: 'TEAM-01',
                    team_name: 'Quantum Phantoms',
                    password: 'wie2026',
                    members: 'Alice, Bob, Charlie'
                };
            }
            if (typeof updateHeaderAuthBadge === 'function') updateHeaderAuthBadge();
        """)
        time.sleep(1.5)

        # 1. Screenshot of Workstation (Tara + Ishaan + 11 Stages)
        p1 = os.path.join(ARTIFACT_DIR, "screenshot_workstation_tara_and_ishaan.png")
        driver.save_screenshot(p1)
        print("✓ Saved:", p1)

        # 2. Trigger Dr. Aditi Video Form & 1st Prize Podium Celebration
        driver.execute_script("""
            if (typeof renderPodiumPrizeCelebration === 'function') {
                renderPodiumPrizeCelebration({
                    prize_code: '1ST_PRIZE',
                    prize_title: '🥇 1ST PRIZE — GRAND CHAMPION',
                    podium_rank: 1
                }, 'Quantum Phantoms', '18m 42s');
            }
            if (typeof startDrAditiVoiceOscilloscope === 'function') {
                startDrAditiVoiceOscilloscope();
            }
        """)
        time.sleep(1.5)

        p2 = os.path.join(ARTIFACT_DIR, "screenshot_dr_aditi_video_podium_grand_champion.png")
        driver.save_screenshot(p2)
        print("✓ Saved:", p2)

    finally:
        driver.quit()
        server.terminate()
        server.wait()

if __name__ == '__main__':
    run()
