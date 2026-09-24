import os, sys, time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
ADMIN_URL = "http://127.0.0.1:8000/admin.html"

VIEWPORTS = [
    ("small_720p", 1280, 720),
    ("budget_768p", 1366, 768),
    ("scaled_864p", 1536, 864),
    ("fullhd_1080p", 1920, 1080)
]

def test_admin():
    for name, w, h in VIEWPORTS:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument(f"--window-size={w},{h}")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Edge(options=options)
        try:
            driver.get(ADMIN_URL)
            time.sleep(1.0)
            driver.execute_script("""
                sessionStorage.setItem('failsafe_admin_authenticated', 'true');
                sessionStorage.setItem('admin_pin', 'wie-admin-2026');
                const m = document.getElementById('admin-login-modal');
                if (m) m.style.display = 'none';
            """)
            time.sleep(0.5)
            
            res = driver.execute_script("""
                const bodyW = document.body.scrollWidth;
                const winW = window.innerWidth;
                const winH = window.innerHeight;
                const header = document.querySelector('.header-bar');
                const metrics = document.querySelector('.metric-grid');
                const tableCont = document.querySelector('.table-container');
                return {
                    bodyW, winW, winH,
                    hasHScroll: bodyW > winW,
                    headerH: header ? header.clientHeight : null,
                    tableScrollW: tableCont ? tableCont.scrollWidth : null,
                    tableClientW: tableCont ? tableCont.clientWidth : null
                };
            """)
            print(f"[Admin {name}] bodyW={res['bodyW']}, winW={res['winW']}, hasHScroll={res['hasHScroll']}")
            driver.save_screenshot(os.path.join(ARTIFACT_DIR, f"resp_admin_{name}.png"))
        finally:
            driver.quit()

if __name__ == "__main__":
    test_admin()
