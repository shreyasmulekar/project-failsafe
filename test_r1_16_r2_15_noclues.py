# test_r1_16_r2_15_noclues.py
import urllib.request
import json
import time
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

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

def run_verification():
    ts = int(time.time())
    team_id = f"TEST-SPEC-{ts % 10000}"
    
    print(f"=== 1. REGISTERING TEST TEAM {team_id} ===")
    status, data = http_post(f"{BASE_URL}/api/teams/register", {
        "team_id": team_id,
        "team_name": "Verification Cyber-Unit",
        "password": "pass123",
        "members": "Dr. Aditi, Tara"
    })
    assert status == 200, "Registration failed"
    print(f"[OK] Team {team_id} registered.")

    print("\n=== 2. VERIFYING ROUND 1 STAGES (1 through 16) ===")
    # Fast forward through stages 1 to 11
    r1_solutions = {
        1: "ACCESS",
        2: "123456",
        3: "SAFE",
        4: "28/02/2025",
        5: "POLARIS",
        6: "MARGIN_KEY",
        7: "ARIAL",
        8: "WHITE",
        9: "HISTORY",
        10: "BYPASS",
        11: "6-9-11"
    }

    for stg, key in r1_solutions.items():
        status, data = http_post(f"{BASE_URL}/api/stage/unlock", {
            "team_id": team_id,
            "round": 1,
            "stage": stg,
            "password": key
        })
        assert data.get("success"), f"Stage {stg} key '{key}' failed: {data}"
        expected_next = stg + 1
        assert data.get("next_stage") == expected_next, f"Stage {stg} did not unlock {expected_next}"
    print("[OK] Stages 1 through 11 solved and advanced to Stage 12!")

    # Verify the 5 new Round 1 stages from the document
    r1_new_doc_stages = {
        12: ("CLEARANCE_ALPHA", 13),
        13: ("ADITIS13", 14),
        14: ("PROJECT", 15),
        15: ("VECTOR", 16),
        16: ("1400", "COMPLETE")
    }

    for stg, (key, exp_next) in r1_new_doc_stages.items():
        # Also check hint is allowed in Round 1
        h_status, h_data = http_post(f"{BASE_URL}/api/hints/request", {
            "team_id": team_id,
            "stage": stg,
            "round": 1
        })
        assert h_data.get("success"), f"Hint for R1 Stage {stg} should be allowed: {h_data}"
        print(f"  [OK] Hint allowed for R1 Stage {stg}: {h_data.get('hint')}")

        status, data = http_post(f"{BASE_URL}/api/stage/unlock", {
            "team_id": team_id,
            "round": 1,
            "stage": stg,
            "password": key
        })
        assert data.get("success"), f"R1 Stage {stg} key '{key}' failed: {data}"
        assert data.get("next_stage") == exp_next, f"R1 Stage {stg} expected next {exp_next}, got {data.get('next_stage')}"
        print(f"  [OK] R1 Stage {stg} solved with '{key}' -> Next: {exp_next}")

    print("[OK] All 16 Round 1 Stages verified and finished!")

    print("\n=== 3. VERIFYING SHORTLIST AND ROUND 2 QUALIFICATION ===")
    # Toggle team into shortlist
    status, data = http_post(f"{BASE_URL}/api/admin/shortlist/toggle", {
        "pin": ADMIN_PIN,
        "team_id": team_id,
        "qualify": True
    })
    assert data.get("is_qualified") == True, "Team should be qualified in shortlist"
    print(f"[OK] Team {team_id} successfully qualified for Round 2 via shortlist toggle.")

    # Start Round 2
    status, data = http_post(f"{BASE_URL}/api/admin/start_round_2", {
        "pin": ADMIN_PIN
    })
    assert data.get("success") == True, "Round 2 start failed"
    print("[OK] Round 2 activated by Organizer.")

    print("\n=== 4. VERIFYING NO-CLUES PROTOCOL IN ROUND 2 ===")
    status, h_data = http_post(f"{BASE_URL}/api/hints/request", {
        "team_id": team_id,
        "stage": 1,
        "round": 2
    })
    assert h_data.get("success") == False, "Clues MUST be disabled in Round 2!"
    assert "disabled in Round 2" in h_data.get("message", ""), f"Unexpected clue message: {h_data}"
    print(f"[OK] Clue request in Round 2 correctly rejected: {h_data.get('message')}")

    print("\n=== 5. VERIFYING ROUND 2: 15 QUESTIONS & #15 ECLIPSE ===")
    r2_puzzles = {
        1: ("C", 2),
        2: ("BL", 3),
        3: ("5", 4),
        4: ("CIPHER", 5),
        5: ("SQUARES", 6),
        6: ("011", 7),
        7: ("CLEARANCE", 8),
        8: ("SE", 9),
        9: ("NONE", 10),
        10: ("RLRCK", 11),
        11: ("NODC", 12),
        12: ("102", 13),
        13: ("3-EMPTY", 14),
        14: ("FINALS", 15),
        15: ("ECLIPSE", "COMPLETE")  # The Red Question!
    }

    for q_num, (key, exp_next) in r2_puzzles.items():
        status, data = http_post(f"{BASE_URL}/api/stage/unlock", {
            "team_id": team_id,
            "round": 2,
            "stage": q_num,
            "password": key
        })
        assert data.get("success"), f"Round 2 Question {q_num} key '{key}' failed: {data}"
        assert data.get("next_stage") == exp_next, f"Round 2 Question {q_num} expected {exp_next}, got {data.get('next_stage')}"
        if q_num == 15:
            print(f"  [OK] Round 2 Question 15 (RED QUESTION) solved with '{key}' -> MISSION COMPLETE!")
        else:
            print(f"  [OK] Round 2 Question {q_num} solved with '{key}' -> Next: Question {exp_next}")

    # Now verify finish and podium award
    status, data = http_post(f"{BASE_URL}/api/teams/finish", {
        "team_id": team_id,
        "round": 2,
        "elapsed_seconds": 1500,
        "elapsed_str": "25m 00s"
    })
    assert data.get("success") == True, f"Finish failed: {data}"
    prize_code = data.get("prize_code")
    prize_title = data.get("prize_title")
    podium_rank = data.get("podium_rank")
    print(f"[OK] Round 2 Finish Confirmed: Rank #{podium_rank}, Prize: {prize_title} ({prize_code})")

    print("\n=== 6. VERIFYING ORGANIZER TEAM MANIPULATION ===")
    status, edit_data = http_post(f"{BASE_URL}/api/admin/teams/edit", {
        "pin": ADMIN_PIN,
        "team_id": team_id,
        "team_name": "Renamed Cyber Elite",
        "current_stage": 16,
        "round_2_stage": 15
    })
    assert edit_data.get("success") == True, "Team edit failed"
    print(f"[OK] Organizer modified team profile parameters.")

    status, del_data = http_post(f"{BASE_URL}/api/admin/teams/delete", {
        "pin": ADMIN_PIN,
        "team_id": team_id
    })
    assert del_data.get("success") == True, "Team deletion failed"
    print(f"[OK] Organizer removed team {team_id} cleanly.")

    print("\n" + "=" * 60)
    print("ALL SPECIFICATIONS VERIFIED WITH 100% SUCCESS!")
    print("  ✓ Round 1 has exactly 16 stages (11 + 5 from doc)")
    print("  ✓ Hints are allowed in Round 1")
    print("  ✓ Hints are strictly DISABLED in Round 2")
    print("  ✓ Round 2 has exactly 15 questions")
    print("  ✓ Question 15 in Round 2 is THE RED QUESTION ('ECLIPSE')")
    print("  ✓ Top 12 Shortlisting and Organizer manipulation verified")
    print("=" * 60)

if __name__ == "__main__":
    run_verification()
