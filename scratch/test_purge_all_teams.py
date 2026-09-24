# scratch/test_purge_all_teams.py
import urllib.request
import json
import sys

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
    print("=== 1. TESTING REGISTERING TEAMS ===")
    for tid in ["PURGE-TEST-1", "PURGE-TEST-2", "PURGE-TEST-3"]:
        status, data = http_post(f"{BASE_URL}/api/teams/register", {
            "team_id": tid,
            "team_name": f"Unit {tid}",
            "password": "pass",
            "members": "Operator"
        })
        assert status == 200, f"Registration of {tid} failed"
    print("  [OK] 3 Test teams registered.")

    status, all_teams = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    assert status == 200
    count_before = len(all_teams.get("leaderboard", []))
    print(f"  [OK] Ledger has {count_before} teams before purge.")
    assert count_before >= 3

    print("\n=== 2. TESTING PURGE WITH INVALID PIN ===")
    try:
        http_post(f"{BASE_URL}/api/admin/teams/purge-all", {"admin_pin": "wrong-pin"})
        assert False, "Should have failed with 403"
    except urllib.error.HTTPError as e:
        assert e.code == 403
        print("  [OK] Correctly rejected with 403 for invalid PIN.")

    print("\n=== 3. TESTING PURGE-ALL WITH VALID ORGANIZER PIN ===")
    status, purge_res = http_post(f"{BASE_URL}/api/admin/teams/purge-all", {"admin_pin": ADMIN_PIN})
    assert status == 200
    assert purge_res.get("success") is True
    print(f"  [OK] Purge API response: {purge_res.get('message')}")
    print(f"  [OK] Purged count: {purge_res.get('purged_count')}")

    print("\n=== 4. VERIFYING TOURNAMENT LEDGER IS COMPLETELY EMPTY ===")
    status, after_teams = http_get(f"{BASE_URL}/api/admin/leaderboard?pin={ADMIN_PIN}")
    assert status == 200
    remaining = len(after_teams.get("leaderboard", []))
    print(f"  [OK] Remaining teams in ledger: {remaining}")
    assert remaining == 0, f"Expected 0 teams, found {remaining}"

    print("\n=======================================================")
    print("ORGANIZER PURGE ALL TEAMS ENDPOINT TEST PASSED 100%!")
    print("=======================================================")

if __name__ == "__main__":
    run_test()
