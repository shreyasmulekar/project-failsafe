import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
URL = "http://127.0.0.1:8000/aditi_os_widget.html"
ADMIN_URL = "http://127.0.0.1:8000/admin.html"

VIEWPORTS = [
    ("small_720p", 1280, 720),
    ("budget_768p", 1366, 768),
    ("scaled_864p", 1536, 864),
    ("fullhd_1080p", 1920, 1080)
]

def run_tests():
    for name, w, h in VIEWPORTS:
        print(f"\n==========================================")
        print(f"Testing Viewport: {name} ({w}x{h})")
        print(f"==========================================")
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument(f"--window-size={w},{h}")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Edge(options=options)
        try:
            driver.get(URL)
            time.sleep(1.5)

            # Check Login Modal
            login_info = driver.execute_script("""
                const modal = document.getElementById('team-auth-modal');
                const card = modal ? modal.querySelector('.proctor-lockdown-card') : null;
                const bodyW = document.body.scrollWidth;
                const winW = window.innerWidth;
                const winH = window.innerHeight;
                let cardRect = null;
                if (card) {
                    const r = card.getBoundingClientRect();
                    cardRect = {top: r.top, bottom: r.bottom, height: r.height, width: r.width};
                }
                return {
                    winW, winH, bodyW,
                    hasHorizontalScroll: bodyW > winW,
                    cardRect
                };
            """)
            print(f"[{name}] Login Screen: winW={login_info['winW']}, winH={login_info['winH']}, bodyW={login_info['bodyW']}")
            print(f"[{name}] Login Card Rect: {login_info['cardRect']}")
            if login_info['cardRect']:
                overflow_bottom = login_info['cardRect']['bottom'] > login_info['winH']
                print(f"[{name}] Login Card overflows bottom viewport? {overflow_bottom} (bottom={login_info['cardRect']['bottom']}, winH={login_info['winH']})")

            driver.save_screenshot(os.path.join(ARTIFACT_DIR, f"resp_login_{name}.png"))

            # Log in and check Round 1
            driver.execute_script("""
                const authModal = document.getElementById('team-auth-modal');
                if (authModal) authModal.style.display = 'none';
                localStorage.setItem('failsafe_auth_team', JSON.stringify({
                    id: 'TEAM-RESP',
                    name: 'Responsive Squad',
                    members: 'Tester',
                    current_round: 1,
                    unlocked_stage: 1
                }));
                if (typeof applyAuthenticatedTeam === 'function') {
                    applyAuthenticatedTeam({
                        id: 'TEAM-RESP',
                        name: 'Responsive Squad',
                        members: 'Tester',
                        current_round: 1,
                        unlocked_stage: 1
                    });
                }
            """)
            time.sleep(1.0)

            r1_info = driver.execute_script("""
                const bodyW = document.body.scrollWidth;
                const winW = window.innerWidth;
                const winH = window.innerHeight;
                const dash = document.querySelector('.nexus-dashboard-container');
                const topRow = document.querySelector('.nexus-top-row');
                const hero = document.querySelector('.nexus-hero-card');
                const tara = document.querySelector('.nexus-assistant-card');
                const dock = document.querySelector('.nexus-bottom-dock');
                const vault = document.querySelector('.nexus-vault-section');

                return {
                    bodyW, winW, winH,
                    hasHScroll: bodyW > winW,
                    dashScrollH: dash ? dash.scrollHeight : null,
                    dashClientH: dash ? dash.clientHeight : null,
                    heroH: hero ? hero.clientHeight : null,
                    taraH: tara ? tara.clientHeight : null,
                    dockBottom: dock ? dock.getBoundingClientRect().bottom : null,
                    dockTop: dock ? dock.getBoundingClientRect().top : null
                };
            """)
            print(f"[{name}] Round 1: bodyW={r1_info['bodyW']}, winW={r1_info['winW']}, hasHScroll={r1_info['hasHScroll']}")
            print(f"[{name}] Round 1: heroH={r1_info['heroH']}, taraH={r1_info['taraH']}, dockTop={r1_info['dockTop']}")
            driver.save_screenshot(os.path.join(ARTIFACT_DIR, f"resp_r1_{name}.png"))

            # Check Puzzles Guide modal
            driver.execute_script("""
                if (typeof openModal === 'function') openModal('modal-puzzles-guide');
            """)
            time.sleep(0.8)
            guide_info = driver.execute_script("""
                const m = document.getElementById('modal-puzzles-guide');
                if (!m) return null;
                const r = m.getBoundingClientRect();
                return {
                    top: r.top, bottom: r.bottom, left: r.left, right: r.right,
                    height: r.height, width: r.width,
                    winW: window.innerWidth, winH: window.innerHeight
                };
            """)
            print(f"[{name}] Puzzles Guide Rect: {guide_info}")
            driver.save_screenshot(os.path.join(ARTIFACT_DIR, f"resp_guide_{name}.png"))
            driver.execute_script("if (typeof closeModal === 'function') closeModal('modal-puzzles-guide');")

            # Check Round 2 Arena
            driver.execute_script("""
                if (typeof launchRound2Arena === 'function') launchRound2Arena();
            """)
            time.sleep(1.0)
            r2_info = driver.execute_script("""
                const bodyW = document.body.scrollWidth;
                const winW = window.innerWidth;
                const winH = window.innerHeight;
                const r2ws = document.getElementById('nexus-r2-workspace');
                const r2Grid = document.getElementById('nexus-r2-grid');
                return {
                    bodyW, winW, winH,
                    hasHScroll: bodyW > winW,
                    r2wsDisplay: r2ws ? r2ws.style.display : null,
                    r2GridChildCount: r2Grid ? r2Grid.children.length : null
                };
            """)
            print(f"[{name}] Round 2: bodyW={r2_info['bodyW']}, winW={r2_info['winW']}, hasHScroll={r2_info['hasHScroll']}, gridCards={r2_info['r2GridChildCount']}")
            driver.save_screenshot(os.path.join(ARTIFACT_DIR, f"resp_r2_{name}.png"))

        finally:
            driver.quit()

if __name__ == "__main__":
    run_tests()
