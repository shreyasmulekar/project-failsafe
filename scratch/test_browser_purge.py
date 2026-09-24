# scratch/test_browser_purge.py
import sys
import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

URL = "http://127.0.0.1:8000/admin.html"
BASE_URL = "http://127.0.0.1:8000"

def register_team(tid):
    payload = json.dumps({
        "team_id": tid,
        "team_name": f"Unit {tid}",
        "password": "pass",
        "members": "Operator"
    }).encode("utf-8")
    req = urllib.request.Request(f"{BASE_URL}/api/teams/register", data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        return res.status

def test_admin_purge():
    # Register 2 test teams first
    register_team("UI-PURGE-1")
    register_team("UI-PURGE-2")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        print("=== 1. LOADING ORGANIZER COMMAND CENTER ===")
        driver.get(URL)
        time.sleep(1.5)

        # Authenticate organizer
        driver.execute_script("""
            sessionStorage.setItem('admin_pin', 'wie-admin-2026');
            const pinModal = document.getElementById('pin-entry-modal');
            if (pinModal) pinModal.style.display = 'none';
            if (typeof fetchLeaderboardData === 'function') fetchLeaderboardData();
        """)
        time.sleep(1.5)

        # Verify REMOVE ALL TEAMS button exists
        btn_info = driver.execute_script("""
            const btns = Array.from(document.querySelectorAll('button'));
            const purgeBtn = btns.find(b => b.innerText.includes('REMOVE ALL TEAMS') || b.innerText.includes('PURGE'));
            return {
                found: !!purgeBtn,
                text: purgeBtn ? purgeBtn.innerText.trim() : '',
                visible: purgeBtn ? (purgeBtn.offsetWidth > 0 && purgeBtn.offsetHeight > 0) : false
            };
        """)
        print(f"  [OK] 'REMOVE ALL TEAMS' Button detected: {btn_info.get('found')}, text: '{btn_info.get('text')}'")
        assert btn_info.get("found"), "REMOVE ALL TEAMS button not found in UI!"

        # Trigger purge through window.promptPurgeAllTeams
        print("=== 2. EXECUTING PURGE ACTION IN UI ===")
        driver.execute_script("""
            // Override window.prompt and window.alert to automatically simulate typing 'PURGE ALL TEAMS'
            window.prompt = function() { return 'PURGE ALL TEAMS'; };
            window.alert = function(msg) { console.log('ALERT:', msg); };
            promptPurgeAllTeams();
        """)
        time.sleep(2.0)

        # Verify table has 0 teams
        kpi_count = driver.execute_script("""
            return {
                kpiTotal: document.getElementById('kpi-total-teams').innerText.trim(),
                cachedCount: cachedTeams.length
            };
        """)
        print(f"  [OK] After UI purge, KPI Total Teams: {kpi_count.get('kpiTotal')}, cachedTeams: {kpi_count.get('cachedCount')}")
        assert kpi_count.get("kpiTotal") == "0", "KPI Total was not 0 after purge!"
        assert kpi_count.get("cachedCount") == 0, "cachedTeams was not 0 after purge!"

        print("\n=======================================================")
        print("ORGANIZER UI PURGE ALL TEAMS VERIFIED WITH 100% SUCCESS!")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_admin_purge()
