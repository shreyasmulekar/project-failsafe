# test_complete_integration.py
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

PORT = 8011
BASE_URL = f"http://localhost:{PORT}"
ADMIN_PIN = "wie-admin-2026"

def start_server():
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    runner_code = f"""import server
server.PORT = {PORT}
if __name__ == '__main__':
    server.run()
"""
    with open("test_integration_runner.py", "w", encoding="utf-8") as f:
        f.write(runner_code)

    proc = subprocess.Popen([sys.executable, "test_integration_runner.py"], cwd=os.getcwd(), env=env)
    time.sleep(2)
    return proc

def http_post(url, data_dict):
    payload = json.dumps(data_dict).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode())

def http_get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode())

def run_tests():
    proc = start_server()
    prefix = f"T{int(time.time())%10000}"
    try:
        print("=== 1. TEST PARTICIPANT REGISTRATION & TELEMETRY ===")
        lead_team = f"{prefix}-01"
        status, data = http_post(f"{BASE_URL}/api/teams/register", {
            "team_id": lead_team,
            "team_name": "Cyber Phantoms",
            "password": "pass-01",
            "members": "Alice, Bob, Carol"
        })
        assert status == 200, "Registration should succeed"
        print(f"✓ {lead_team} registered")

        status, data = http_post(f"{BASE_URL}/api/teams/activity", {
            "team_id": lead_team,
            "current_stage": 1,
            "action": "Investigating Stage 01",
            "tamper_incidents": 0,
            "is_locked": False,
            "client_info": {"resolution": "1920x1080", "fullscreen": True}
        })
        assert status == 200, "Telemetry sync should succeed"
        print("✓ Telemetry sync verified")

        print("=== 2. TEST FULLSCREEN EXIT REQUEST & ORGANIZER APPROVAL ===")
        # Team requests fullscreen exit
        status, data = http_post(f"{BASE_URL}/api/teams/request_fullscreen_exit", {
            "team_id": lead_team
        })
        assert status == 200 and data.get("success"), "Fullscreen exit request should succeed"
        print(f"✓ {lead_team} requested fullscreen exit")

        # Organizer checks pending requests
        status, data = http_post(f"{BASE_URL}/api/admin/pending_fullscreen_requests", {
            "pin": ADMIN_PIN
        })
        assert status == 200, "Admin pending requests should succeed"
        pending_ids = [p["team_id"] for p in data.get("pending", [])]
        assert lead_team in pending_ids, f"{lead_team} must be in pending fullscreen exit requests"
        print(f"✓ Organizer sees {lead_team} in pending fullscreen exit requests")

        # Organizer approves fullscreen exit
        status, data = http_post(f"{BASE_URL}/api/admin/approve_fullscreen_exit", {
            "pin": ADMIN_PIN,
            "team_id": lead_team,
            "action": "approve"
        })
        assert status == 200 and data.get("success"), "Approval should succeed"
        print(f"✓ Organizer approved fullscreen exit for {lead_team}")

        # Team heartbeat verifies approval
        status, data = http_post(f"{BASE_URL}/api/teams/activity", {
            "team_id": lead_team
        })
        assert data.get("fullscreen_exit_approved") == True, "Team must receive fullscreen_exit_approved: true"
        print(f"✓ {lead_team} workstation confirmed fullscreen exit approved!")

        print("=== 3. TEST SHORTLIST & ROUND 2 GATING ===")
        # Ensure at least 12 teams exist
        status, cur_sl = http_get(f"{BASE_URL}/api/admin/shortlist?pin={ADMIN_PIN}")
        ranked = cur_sl.get("ranked_teams", [])
        if len(ranked) < 12:
            for i in range(len(ranked) + 1, 14):
                tid = f"{prefix}-{i:02d}"
                http_post(f"{BASE_URL}/api/teams/register", {
                    "team_id": tid, "team_name": f"Squad {i}", "password": f"pass-{i}", "members": "M1, M2"
                })
                elapsed = 1000 + i * 50
                http_post(f"{BASE_URL}/api/teams/finish", {
                    "team_id": tid, "round": 1, "elapsed_seconds": elapsed, "elapsed_str": f"{elapsed//60}m"
                })

        # Also finish lead team fastest
        http_post(f"{BASE_URL}/api/teams/finish", {
            "team_id": lead_team, "round": 1, "elapsed_seconds": 800, "elapsed_str": "13m 20s"
        })

        # Reset Shortlist to top 12
        status, data = http_post(f"{BASE_URL}/api/admin/shortlist/reset", {"pin": ADMIN_PIN})
        assert status == 200, "Shortlist reset should succeed"
        status, data = http_get(f"{BASE_URL}/api/admin/shortlist?pin={ADMIN_PIN}")
        print(f"Shortlist returned: {len(data.get('qualified_team_ids', []))} teams (status={status})")
        assert len(data.get("qualified_team_ids", [])) == 12, f"Should auto-shortlist top 12, got: {data.get('qualified_team_ids')}"
        print(f"✓ Shortlist contains 12 qualified teams")

        # Organizer launches Round 2
        status, data = http_post(f"{BASE_URL}/api/admin/start_round_2", {
            "pin": ADMIN_PIN
        })
        assert data.get("success"), "Round 2 start should succeed"
        print("✓ Round 2 started by Organizer")

        # Check Team activity response has round_2_ready: true
        status, data = http_post(f"{BASE_URL}/api/teams/activity", {
            "team_id": lead_team
        })
        assert data.get("round_2_started") == True, "Round 2 started flag must be True"
        print(f"✓ {lead_team} confirmed Round 2 is ready and unlocked")

        print("=== 4. TEST ROUND 2 15 PUZZLES & ECLIPSE FINISH ===")
        status, data = http_post(f"{BASE_URL}/api/teams/finish", {
            "team_id": lead_team,
            "round": 2,
            "elapsed_seconds": 1250,
            "elapsed_str": "20m 50s"
        })
        assert status == 200 and data.get("success"), "Round 2 finish should succeed"
        assert data.get("prize_code") in ["1ST_PRIZE", "2ND_PRIZE", "3RD_PRIZE", "HONORARY_LAUREATE"], "Valid prize code must be awarded"
        assert data.get("podium_rank", 0) >= 1, "Podium rank must be assigned"
        print(f"✓ Round 2 Podium/Laureate awarded: {data.get('prize_title')} (Rank #{data.get('podium_rank')})")

        print("=== 5. TEST GLOBAL LOGOUT (ORGANIZER REMOVES ALL PARTICIPANTS) ===")
        status, data = http_post(f"{BASE_URL}/api/admin/remote-logout", {
            "pin": ADMIN_PIN,
            "team_id": "ALL"
        })
        assert status == 200 and data.get("success"), "Global logout must succeed"
        print("✓ Organizer issued global logout to ALL workstations")

        # Check team activity returns force_logout: True
        status, data = http_post(f"{BASE_URL}/api/teams/activity", {
            "team_id": lead_team
        })
        assert data.get("force_logout") == True, "Workstation must receive force_logout: True"
        print(f"✓ {lead_team} workstation received force_logout signal!")

        print("\n=======================================================")
        print("🎉 ALL INTEGRATION TESTS PASSED WITH 100% SUCCESS!")
        print("=======================================================")

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except Exception:
            proc.kill()

if __name__ == "__main__":
    run_tests()
