import os
import sys
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
SERVER_PORT = 8094

def capture_video_celebration():
    env = os.environ.copy()
    env["PORT"] = str(SERVER_PORT)
    server = subprocess.Popen([sys.executable, "server.py"], cwd=os.getcwd(), env=env)
    time.sleep(2)

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1600,1050")
    opts.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    driver = webdriver.Edge(options=opts)

    try:
        url = f"http://127.0.0.1:{SERVER_PORT}/aditi_os_widget.html"
        driver.get(url)
        time.sleep(2)

        # Check console logs
        for entry in driver.get_log("browser"):
            if entry["level"] == "SEVERE":
                print("JS ERROR:", entry["message"])

        # Hide auth modal and display victory modal
        res = driver.execute_script("""
            const authModal = document.getElementById('team-auth-modal');
            if (authModal) authModal.style.display = 'none';

            const modal = document.getElementById('victory-celebration-modal');
            if (!modal) return 'modal-not-found';
            
            // Call renderPodiumPrizeCelebration
            if (typeof renderPodiumPrizeCelebration === 'function') {
                renderPodiumPrizeCelebration({
                    prize_code: '1ST_PRIZE',
                    prize_title: '🥇 1ST PRIZE — GRAND CHAMPION',
                    podium_rank: 1
                }, 'Quantum Phantoms', '18m 42s');
            } else {
                modal.style.display = 'flex';
            }
            if (typeof startDrAditiVoiceOscilloscope === 'function') {
                startDrAditiVoiceOscilloscope();
            }
            modal.style.display = 'flex';
            return modal.style.display;
        """)
        print("Modal display state:", res)
        time.sleep(1)

        p = os.path.join(ARTIFACT_DIR, "screenshot_dr_aditi_video_podium_grand_champion.png")
        driver.save_screenshot(p)
        print("✓ Captured:", p)

    finally:
        driver.quit()
        server.terminate()
        server.wait()

if __name__ == '__main__':
    capture_video_celebration()
