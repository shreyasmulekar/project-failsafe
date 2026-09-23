import urllib.request
import urllib.parse
import json
import time
import subprocess
import sys
import os

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

SERVER_PORT = 8099
BASE_URL = f"http://127.0.0.1:{SERVER_PORT}"
ADMIN_PIN = "wie-admin-2026"

def start_test_server():
    env = os.environ.copy()
    env["PORT"] = str(SERVER_PORT)
    proc = subprocess.Popen(
        [sys.executable, "server.py"],
        cwd=os.getcwd(),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    return proc

def http_get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode('utf-8'))

def http_post(url, data):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode('utf-8'))

def run_tests():
    server_proc = start_test_server()
    try:
        print("=== 1. VERIFYING SERVER & ADMIN AUTH ===")
        status, res = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
        assert status == 200, f"Leaderboard failed: {res}"
        print("✓ Server running, /api/admin/leaderboard OK")

        print("\n=== 2. REGISTERING TEAMS & REPORTING GRANULAR TELEMETRY ===")
        # Register Team 1
        t_suffix = str(int(time.time()))[-4:]
        t1_id = f"T1-{t_suffix}"
        t2_id = f"T2-{t_suffix}"
        t3_id = f"T3-{t_suffix}"
        t4_id = f"T4-{t_suffix}"

        t1_data = {
            "team_id": t1_id,
            "team_name": "Quantum Phantoms",
            "members": "Dr. Alice, Bob, Charlie",
            "password": "pass1"
        }
        status, res = http_post(f"{BASE_URL}/api/teams/register", t1_data)
        assert status == 200, f"Register failed: {res}"
        print("✓ Registered TEAM-01")

        # Report Telemetry with client info, active view, and breach history
        telem_data = {
            "team_id": t1_id,
            "team_name": "Quantum Phantoms",
            "action": "Inspecting ISHAAN Recovery Terminal",
            "current_stage": 1,
            "tamper_incidents": 1,
            "client_info": {
                "resolution": "1920x1080",
                "os": "Windows 11 Pro (x64)",
                "fullscreen": True
            },
            "active_view": "STAGE_01_TERMINAL",
            "violations_history": [
                {"type": "Attempted Right-Click Inspection", "timestamp": "14:22:01"}
            ]
        }
        status, res = http_post(f"{BASE_URL}/api/teams/activity", telem_data)
        assert status == 200, f"Telemetry post failed: {res}"
        print("✓ Telemetry reported with client_info, active_view, and violations_history")

        # Verify telemetry stored in state
        status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
        t1_in_lb = next(t for t in lb_data["leaderboard"] if t["team_id"] == t1_id)
        assert t1_in_lb.get("client_info", {}).get("resolution") == "1920x1080"
        assert t1_in_lb.get("active_view") == "STAGE_01_TERMINAL"
        assert len(t1_in_lb.get("violations_history", [])) == 1
        print("✓ Stored telemetry verified on organizer dashboard feed")

        print("\n=== 3. TESTING 11 CURATED STORYLINE STAGE UNLOCKS ===")
        for s in range(2, 12):
            status, res = http_post(f"{BASE_URL}/api/stage/unlock", {
                "team_id": t1_id,
                "password": "pass1",
                "round": 1,
                "stage": s
            })
            assert status == 200, f"Unlock stage {s} failed: {res}"
            print(f"✓ Advanced to Stage {s:02d}")

        print("\n=== 4. TESTING ORGANIZER TEAM EDIT & MANIPULATION ===")
        edit_payload = {
            "pin": ADMIN_PIN,
            "team_id": t1_id,
            "team_name": "Quantum Phantoms (Prime)",
            "members": "Dr. Alice, Bob, Charlie, Dana",
            "current_stage": 11,
            "hints_count": 2,
            "traps_count": 1,
            "time_adjustment_sec": -120
        }
        status, res = http_post(f"{BASE_URL}/api/admin/teams/edit", edit_payload)
        assert status == 200 and res.get("success") is True, f"Edit failed: {res}"
        edited_team = res.get("team", {})
        assert edited_team.get("team_name") == "Quantum Phantoms (Prime)"
        assert edited_team.get("hints_count") == 2
        assert edited_team.get("traps_count") == 1
        print("✓ Organizer successfully manipulated team parameters")

        print("\n=== 5. TESTING SHORTLIST & ROUND 2 PRIZE RANKINGS ===")
        # Register Teams 2, 3, 4
        for tid, tname in [(t2_id, "Cyber Valkyries"), (t3_id, "Neural Pioneers"), (t4_id, "Binary Ghosts")]:
            http_post(f"{BASE_URL}/api/teams/register", {"team_id": tid, "team_name": tname, "members": "Op1, Op2", "password": "pass"})
        
        # Qualify top 3
        http_post(f"{BASE_URL}/api/admin/shortlist/toggle", {"pin": ADMIN_PIN, "team_id": t1_id, "qualified": True})
        http_post(f"{BASE_URL}/api/admin/shortlist/toggle", {"pin": ADMIN_PIN, "team_id": t2_id, "qualified": True})
        http_post(f"{BASE_URL}/api/admin/shortlist/toggle", {"pin": ADMIN_PIN, "team_id": t3_id, "qualified": True})
        
        # Start Round 2
        status, res = http_post(f"{BASE_URL}/api/admin/start_round_2", {"pin": ADMIN_PIN})
        assert status == 200 and res.get("current_round") == 2, f"Start Round 2 failed: {res}"
        print("✓ Shortlist locked and Round 2 started!")

        # Simulate Round 2 Finishes and verify podium ranks
        # Finish 1st: t1_id -> 1ST_PRIZE
        s1, r1 = http_post(f"{BASE_URL}/api/teams/finish", {
            "team_id": t1_id, "round": 2, "elapsed_seconds": 1200, "elapsed_str": "20m 00s"
        })
        assert s1 == 200 and r1.get("prize_code") == "1ST_PRIZE", f"1st prize mismatch: {r1}"
        print(f"✓ 1st Finish -> {r1.get('prize_title')}")

        # Finish 2nd: t2_id -> 2ND_PRIZE
        s2, r2 = http_post(f"{BASE_URL}/api/teams/finish", {
            "team_id": t2_id, "round": 2, "elapsed_seconds": 1350, "elapsed_str": "22m 30s"
        })
        assert s2 == 200 and r2.get("prize_code") == "2ND_PRIZE", f"2nd prize mismatch: {r2}"
        print(f"✓ 2nd Finish -> {r2.get('prize_title')}")

        # Finish 3rd: t3_id -> 3RD_PRIZE
        s3, r3 = http_post(f"{BASE_URL}/api/teams/finish", {
            "team_id": t3_id, "round": 2, "elapsed_seconds": 1500, "elapsed_str": "25m 00s"
        })
        assert s3 == 200 and r3.get("prize_code") == "3RD_PRIZE", f"3rd prize mismatch: {r3}"
        print(f"✓ 3rd Finish -> {r3.get('prize_title')}")

        print("\n=== 6. TESTING ORGANIZER TEAM DELETION ===")
        status, res = http_post(f"{BASE_URL}/api/admin/teams/delete", {"pin": ADMIN_PIN, "team_id": t4_id})
        assert status == 200 and res.get("success") is True, f"Delete failed: {res}"
        print("✓ Team-04 successfully deleted by organizer")

        print("\n==========================================")
        print("🎉 ALL API & BUSINESS LOGIC TESTS PASSED!")
        print("==========================================")

    finally:
        server_proc.terminate()
        server_proc.wait()

if __name__ == '__main__':
    run_tests()
