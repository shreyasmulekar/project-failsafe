import os
import sys
import time
import json
import subprocess
import urllib.request
import urllib.parse

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PORT = 8009
ADMIN_PIN = "wie-admin-2026"

def start_test_server():
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    runner_code = f"""import server
server.PORT = {PORT}
if __name__ == '__main__':
    server.run()
"""
    with open("test_server_runner_r2.py", "w", encoding="utf-8") as f:
        f.write(runner_code)

    proc = subprocess.Popen([sys.executable, "test_server_runner_r2.py"], cwd=os.getcwd(), env=env)
    time.sleep(2)
    return proc

def seed_teams(base_url):
    print("--- 1. Seeding 15 Mock Teams for Round 1 ---")
    teams = []
    for i in range(1, 16):
        tid = f"TEAM-{i:02d}"
        tname = f"Squad {chr(64+i)} ({tid})"
        reg_payload = json.dumps({
            "team_id": tid,
            "team_name": tname,
            "members": f"Member A{i}, Member B{i}",
            "password": f"pass-{i:02d}"
        }).encode("utf-8")
        req = urllib.request.Request(f"{base_url}/api/teams/register", data=reg_payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as res:
            pass

        # Teams 1-13 finished, team 14 at stage 10, team 15 at stage 4
        if i <= 13:
            elapsed = 900 + i * 60  # Team 1 finishes fastest (15m), Team 13 (27m)
            fin_payload = json.dumps({
                "team_id": tid,
                "team_name": tname,
                "members": f"Member A{i}, Member B{i}",
                "password": f"pass-{i:02d}",
                "elapsed_seconds": elapsed,
                "elapsed_str": f"{elapsed//60}m {elapsed%60:02d}s",
                "stage_times": {str(s): {"duration_seconds": 60, "duration_str": "1m 00s"} for s in range(1, 16)}
            }).encode("utf-8")
            req = urllib.request.Request(f"{base_url}/api/teams/finish", data=fin_payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req) as res:
                pass
        else:
            act_payload = json.dumps({
                "team_id": tid,
                "team_name": tname,
                "current_stage": 10 if i == 14 else 4,
                "action": "Investigating Sector",
                "tamper_incidents": 0,
                "is_locked": False
            }).encode("utf-8")
            req = urllib.request.Request(f"{base_url}/api/teams/activity", data=act_payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req) as res:
                pass

    print("15 teams seeded successfully!")

def test_shortlist_api(base_url):
    print("--- 2. Testing Shortlist API & Manipulation ---")
    req = urllib.request.Request(f"{base_url}/api/admin/shortlist?pin={ADMIN_PIN}")
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        qualified_ids = data["qualified_team_ids"]
        print(f"Auto-shortlisted count: {len(qualified_ids)}")
        assert len(qualified_ids) == 12, "Should auto-shortlist exactly top 12"
        assert "TEAM-01" in qualified_ids, "Fastest team TEAM-01 must be qualified"
        assert "TEAM-12" in qualified_ids, "12th team TEAM-12 must be qualified"
        assert "TEAM-13" not in qualified_ids, "13th team TEAM-13 should not be in default top 12"

    print("--- 3. Testing Organizer Shortlist Manipulation (Remove TEAM-12, Add TEAM-13) ---")
    toggle_payload = json.dumps({
        "pin": ADMIN_PIN,
        "team_id": "TEAM-12",
        "qualified": False
    }).encode("utf-8")
    req = urllib.request.Request(f"{base_url}/api/admin/shortlist/toggle", data=toggle_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        assert "TEAM-12" not in data["qualified_team_ids"]

    toggle_payload = json.dumps({
        "pin": ADMIN_PIN,
        "team_id": "TEAM-13",
        "qualified": True
    }).encode("utf-8")
    req = urllib.request.Request(f"{base_url}/api/admin/shortlist/toggle", data=toggle_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        assert "TEAM-13" in data["qualified_team_ids"]
        assert len(data["qualified_team_ids"]) == 12
    print("Manipulation verified: TEAM-12 removed, TEAM-13 added!")

    print("--- 4. Testing Start Round 2 API ---")
    start_payload = json.dumps({"pin": ADMIN_PIN}).encode("utf-8")
    req = urllib.request.Request(f"{base_url}/api/admin/start_round_2", data=start_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        assert data["success"] is True
        assert data["current_round"] == 2
    print("Round 2 successfully initiated by Organizer!")

    print("--- 5. Testing Team Polling Status Endpoint ---")
    req = urllib.request.Request(f"{base_url}/api/team/round_status?team_id=TEAM-01")
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        assert data["round_2_unlocked"] is True
        assert data["is_qualified_for_round_2"] is True

    req = urllib.request.Request(f"{base_url}/api/team/round_status?team_id=TEAM-12")
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        assert data["round_2_unlocked"] is False
        assert data["is_qualified_for_round_2"] is False
    print("Team polling correctly distinguishes qualified and standby teams!")

def test_browser_ui(base_url):
    print("--- 6. Running Headless Edge UI Tests ---")
    edge_options = Options()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=edge_options)
    artifact_dir = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

    try:
        # A. Organizer Dashboard Shortlist Modal
        admin_url = f"{base_url}/admin.html"
        print(f"Loading {admin_url}...")
        driver.get(admin_url)
        time.sleep(2)

        # Authenticate
        pin_input = driver.find_element(By.ID, "admin-auth-pin")
        pin_input.clear()
        pin_input.send_keys(ADMIN_PIN)
        driver.find_element(By.ID, "admin-login-form").submit()
        time.sleep(2)

        # Open Round 2 Shortlist Modal
        print("Opening Round 2 Shortlist Modal in Organizer Dashboard...")
        driver.execute_script("openRound2ShortlistModal();")
        time.sleep(1.5)
        modal = driver.find_element(By.ID, "modal-round2-shortlist")
        assert modal.is_displayed()
        modal_text = modal.text
        assert "ROUND 2 SHORTLIST" in modal_text.upper()
        assert "TEAM-01" in modal_text
        assert "12 TEAMS SELECTED" in modal_text.upper()

        shortlist_screen = os.path.join(artifact_dir, "screenshot_admin_round2_shortlist_modal.png")
        driver.save_screenshot(shortlist_screen)
        print(f"Saved screenshot: {shortlist_screen}")

        # B. Participant Workstation: aditi_os_widget.html
        workstation_url = f"{base_url}/aditi_os_widget.html"
        print(f"Loading participant workstation: {workstation_url}...")
        driver.get(workstation_url)
        time.sleep(2)

        # Set team TEAM-01
        driver.execute_script(f"""
            localStorage.setItem("failsafe_server_url", "{base_url}");
            currentTeam = {{ team_id: "TEAM-01", team_name: "Squad A (TEAM-01)", password: "pass-01", members: "Member A1, Member B1" }};
            localStorage.setItem("failsafe_local_team", JSON.stringify(currentTeam));
            setStage(1);
        """)
        time.sleep(1)

        # C. Test ETHAN "WHERE DO I LOOK?" Guidance on Stage 1
        print("Testing ETHAN 'WHERE DO I LOOK?' Guidance on Round 1 Stage 1...")
        driver.execute_script("triggerEthanWhereToLook();")
        time.sleep(1.5)

        beacon = driver.find_element(By.ID, "ethan-target-beacon")
        assert beacon.is_displayed(), "ETHAN pointer beacon should be displayed"
        beacon_text = beacon.text
        assert "ADI_RECOVERY" in beacon_text.upper() or "FOCUS" in beacon_text.upper()

        ethan_screen = os.path.join(artifact_dir, "screenshot_ethan_where_to_look_beacon.png")
        driver.save_screenshot(ethan_screen)
        print(f"Saved screenshot: {ethan_screen}")

        # D. Test Launching Round 2 Arena
        print("Launching Round 2 Decryption Arena...")
        driver.execute_script("launchRound2Arena();")
        time.sleep(2)

        r2_container = driver.find_element(By.ID, "round2-arena-container")
        assert r2_container.is_displayed(), "Round 2 Arena container must be visible"

        r2_screen = os.path.join(artifact_dir, "screenshot_round2_arena_active.png")
        driver.save_screenshot(r2_screen)
        print(f"Saved screenshot: {r2_screen}")

        # E. Step through and solve all 9 Round 2 Puzzles
        r2_answers = [
            ("Puzzle 1: Matrix Box", "C"),
            ("Puzzle 2: Cube Net", "5"),
            ("Puzzle 3: Rotation", "BOTTOM LEFT"),
            ("Puzzle 4: Whiteout", "CLEARANCE_ALPHA"),
            ("Puzzle 5: ROT-4 Shift", "ADITIS13"),
            ("Puzzle 6: Polybius Matrix", "VECTOR"),
            ("Puzzle 7: Atbash Mirror", "PROJECT"),
            ("Puzzle 8: Substring Count", "1400"),
            ("Puzzle 9: Master Wheel", "ECLIPSE")
        ]

        for idx, (pname, ans) in enumerate(r2_answers, start=1):
            print(f"Solving {pname} with answer: '{ans}'...")
            driver.execute_script(f"submitRound2Code('{ans}');")
            time.sleep(1.2)
            cur_st = driver.execute_script("return round2CurrentStage;")
            cleared = driver.execute_script("return round2StagesCleared;")
            assert idx in cleared, f"Stage {idx} should be marked cleared"

        time.sleep(2)
        # Verify Grand Victory Modal is displayed
        victory_modal = driver.find_element(By.ID, "victory-celebration-modal")
        assert victory_modal.is_displayed(), "Round 2 Grand Victory Modal should be active"
        victory_text = victory_modal.text
        assert "CHAMPIONS" in victory_text.upper()

        victory_screen = os.path.join(artifact_dir, "screenshot_round2_grand_victory_celebration.png")
        driver.save_screenshot(victory_screen)
        print(f"Saved screenshot: {victory_screen}")

        print("All 9 Round 2 Puzzles solved and verified in browser!")

    finally:
        driver.quit()

def main():
    game_state_file = os.path.join("data", "game_state.json")
    backup_file = os.path.join("data", "game_state_test_backup.json")
    if os.path.exists(game_state_file):
        with open(game_state_file, "r", encoding="utf-8") as f:
            backup_data = f.read()
        with open(backup_file, "w", encoding="utf-8") as f:
            f.write(backup_data)

    clean_state = {
        "current_round": 1,
        "shortlist": {"round_2_qualified_team_ids": [], "locked": False},
        "teams": {},
        "broadcasts": []
    }
    with open(game_state_file, "w", encoding="utf-8") as f:
        json.dump(clean_state, f, indent=2)

    proc = start_test_server()
    base_url = f"http://127.0.0.1:{PORT}"
    try:
        seed_teams(base_url)
        test_shortlist_api(base_url)
        test_browser_ui(base_url)
        print("\n=======================================================")
        print("🎉 ALL TESTS PASSED: SHORTLIST, ROUND 2, & ETHAN BEACON!")
        print("=======================================================\n")
    finally:
        proc.terminate()
        try:
            os.remove("test_server_runner_r2.py")
        except Exception:
            pass
        if os.path.exists(backup_file):
            with open(backup_file, "r", encoding="utf-8") as f:
                saved = f.read()
            with open(game_state_file, "w", encoding="utf-8") as f:
                f.write(saved)
            os.remove(backup_file)

if __name__ == '__main__':
    main()
