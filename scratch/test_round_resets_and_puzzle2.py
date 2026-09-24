# scratch/test_round_resets_and_puzzle2.py
import urllib.request
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')
BASE_URL = "http://127.0.0.1:8000"
ADMIN_PIN = "wie-admin-2026"

def http_post(url, data_dict):
    payload = json.dumps(data_dict).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode())

def http_get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as res:
        return res.status, json.loads(res.read().decode())

def run_test():
    print("=== 1. REGISTERING TEST TEAMS ===")
    http_post(f"{BASE_URL}/api/teams/register", {
        "team_id": "RESET-T1",
        "team_name": "Phoenix Vanguard",
        "password": "pass",
        "members": "Operator Alpha"
    })
    http_post(f"{BASE_URL}/api/teams/register", {
        "team_id": "RESET-T2",
        "team_name": "Cyber Aegis",
        "password": "pass",
        "members": "Operator Beta"
    })
    print("  [OK] Teams RESET-T1 and RESET-T2 registered.")

    print("\n=== 2. ADVANCING TEAMS & SIMULATING PROGRESS ===")
    # Simulate RESET-T1 at Stage 5 with hints/traps
    http_post(f"{BASE_URL}/api/admin/teams/edit", {
        "admin_pin": ADMIN_PIN,
        "team_id": "RESET-T1",
        "current_stage": 5,
        "hints_count": 2,
        "traps_count": 1,
        "is_finished": False
    })
    
    # Simulate RESET-T2 in Round 2 at Puzzle 4
    http_post(f"{BASE_URL}/api/admin/teams/edit", {
        "admin_pin": ADMIN_PIN,
        "team_id": "RESET-T2",
        "current_round": 2,
        "round_2_stage": 4,
        "round_2_is_finished": True
    })

    # Verify initial progress in leaderboard
    status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    t1 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T1")
    t2 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T2")
    assert t1["current_stage"] == 5, f"Expected stage 5, got {t1['current_stage']}"
    assert t1["hints_count"] == 2
    assert t2["round_2_stage"] == 4
    assert t2["round_2_is_finished"] is True
    print("  [OK] Simulation verified: T1 at Stage 5, T2 at R2 Puzzle 4.")

    print("\n=== 3. TESTING PIN VALIDATION ===")
    try:
        http_post(f"{BASE_URL}/api/admin/round/reset", {
            "admin_pin": "wrong-pin",
            "round": 1,
            "team_id": "RESET-T1"
        })
        assert False, "Should have failed with 403"
    except urllib.error.HTTPError as e:
        assert e.code == 403
        print("  [OK] Correctly rejected with 403 for wrong PIN.")

    print("\n=== 4. TESTING RESET ROUND 1 FOR SPECIFIC TEAM (RESET-T1) ===")
    status, res = http_post(f"{BASE_URL}/api/admin/round/reset", {
        "admin_pin": ADMIN_PIN,
        "round": 1,
        "team_id": "RESET-T1"
    })
    assert status == 200
    assert res.get("success") is True
    print(f"  [OK] API Response: {res.get('message')}")

    # Verify T1 is reset to stage 1 and penalties cleared
    status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    t1 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T1")
    t2 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T2")
    assert t1["current_stage"] == 1, f"Expected stage 1, got {t1['current_stage']}"
    assert t1["hints_count"] == 0
    assert t1["traps_count"] == 0
    # T2 should remain unaffected
    assert t2["round_2_stage"] == 4, f"T2 should still be at R2 stage 4, got {t2['round_2_stage']}"
    print("  [OK] RESET-T1 reset to Stage 1. RESET-T2 remained untouched.")

    print("\n=== 5. TESTING RESET ROUND 2 FOR SPECIFIC TEAM (RESET-T2) ===")
    status, res = http_post(f"{BASE_URL}/api/admin/round/reset", {
        "admin_pin": ADMIN_PIN,
        "round": 2,
        "team_id": "RESET-T2"
    })
    assert status == 200
    assert res.get("success") is True
    print(f"  [OK] API Response: {res.get('message')}")

    status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    t2 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T2")
    assert t2["round_2_stage"] == 1, f"Expected R2 stage 1, got {t2['round_2_stage']}"
    assert t2["round_2_is_finished"] is False, "Expected round_2_is_finished to be False"
    print("  [OK] RESET-T2 Round 2 reset back to Puzzle 01.")

    print("\n=== 6. ADVANCING MULTIPLE TEAMS FOR GLOBAL RESET TESTS ===")
    http_post(f"{BASE_URL}/api/admin/teams/edit", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T1", "current_stage": 8})
    http_post(f"{BASE_URL}/api/admin/teams/edit", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T2", "current_stage": 12})
    http_post(f"{BASE_URL}/api/admin/teams/edit", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T1", "round_2_stage": 7, "current_round": 2})
    http_post(f"{BASE_URL}/api/admin/teams/edit", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T2", "round_2_stage": 10, "current_round": 2})

    print("\n=== 7. TESTING GLOBAL RESET ROUND 2 (ALL) ===")
    status, res = http_post(f"{BASE_URL}/api/admin/round/reset", {
        "admin_pin": ADMIN_PIN,
        "round": 2,
        "team_id": "ALL"
    })
    assert status == 200
    assert res.get("success") is True
    print(f"  [OK] API Response: {res.get('message')}")

    status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    t1 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T1")
    t2 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T2")
    assert t1["round_2_stage"] == 1, f"Expected R2 stage 1, got {t1['round_2_stage']}"
    assert t2["round_2_stage"] == 1, f"Expected R2 stage 1, got {t2['round_2_stage']}"
    # Round 1 stages should still be intact
    assert t1["current_stage"] == 8, f"Round 1 stage should be 8, got {t1['current_stage']}"
    assert t2["current_stage"] == 12, f"Round 1 stage should be 12, got {t2['current_stage']}"
    print("  [OK] Global Round 2 reset verified: All teams returned to R2 Puzzle 01, Round 1 intact.")

    print("\n=== 8. TESTING GLOBAL RESET ROUND 1 (ALL) ===")
    status, res = http_post(f"{BASE_URL}/api/admin/round/reset", {
        "admin_pin": ADMIN_PIN,
        "round": 1,
        "team_id": "ALL"
    })
    assert status == 200
    assert res.get("success") is True
    print(f"  [OK] API Response: {res.get('message')}")

    status, lb_data = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    t1 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T1")
    t2 = next(t for t in lb_data["leaderboard"] if t["team_id"] == "RESET-T2")
    assert t1["current_stage"] == 1, f"Expected R1 stage 1, got {t1['current_stage']}"
    assert t2["current_stage"] == 1, f"Expected R1 stage 1, got {t2['current_stage']}"
    print("  [OK] Global Round 1 reset verified: All teams returned to Stage 01.")

    print("\n=== 9. CLEANUP TEST TEAMS WITH PURGE ===")
    http_post(f"{BASE_URL}/api/admin/teams/delete", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T1"})
    http_post(f"{BASE_URL}/api/admin/teams/delete", {"admin_pin": ADMIN_PIN, "team_id": "RESET-T2"})
    print("  [OK] Test teams deleted.")

    print("\n=================================================================")
    print("ALL ROUND 1 & ROUND 2 INDEPENDENT RESET TESTS PASSED 100%!")
    print("=================================================================")

if __name__ == "__main__":
    run_test()
