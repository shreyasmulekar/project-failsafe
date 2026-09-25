import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = "http://127.0.0.1:8000"

def post(endpoint, data):
    req = urllib.request.Request(
        f"{BASE}{endpoint}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode('utf-8'))

print("=== 1. REGISTER NEW TEST TEAM ===")
team_id = f"TEST-E2E-{int(time.time())}"
reg = post("/api/teams/register", {
    "team_id": team_id,
    "team_name": "E2E Protocol Verification Unit",
    "password": "pass",
    "leader_name": "Dr. Verification"
})
print("Registered:", reg.get("success"), reg.get("message"))

print("\n=== 2. VERIFY CLUE SYSTEM (3 LIFELINES, +2M PENALTY) ===")
# Start round 1 if waiting
post("/api/admin/start_round_1", {"pin": "admin"})

# Hint 1
h1 = post("/api/hints/request", {"team_id": team_id, "stage": 1, "round": 1})
print("Clue 1:", h1.get("success"), "| total hints:", h1.get("total_hints"), "| pen sec:", h1.get("penalty_seconds"))

# Hint 2
h2 = post("/api/hints/request", {"team_id": team_id, "stage": 2, "round": 1})
print("Clue 2:", h2.get("success"), "| total hints:", h2.get("total_hints"), "| pen sec:", h2.get("penalty_seconds"))

# Hint 3
h3 = post("/api/hints/request", {"team_id": team_id, "stage": 3, "round": 1})
print("Clue 3:", h3.get("success"), "| total hints:", h3.get("total_hints"), "| pen sec:", h3.get("penalty_seconds"))

# Hint 4 (Must be REJECTED)
h4 = post("/api/hints/request", {"team_id": team_id, "stage": 4, "round": 1})
print("Clue 4 (Lifeline exhausted check):", h4.get("success"), "| message:", h4.get("message"))
assert h4.get("success") == False, "Clue 4 should have been rejected!"

print("\n=== 3. VERIFY HONEYPOT TRAP (+5M PENALTY) ===")
trap = post("/api/trap/trigger", {"team_id": team_id})
print("Honeypot Triggered:", trap.get("success"), "| penalty:", trap.get("penalty_seconds"))
# 3 hints * 120s (360s) + 1 trap * 300s (300s) = 660s penalty
assert trap.get("penalty_seconds") == 660, f"Expected 660s penalty, got {trap.get('penalty_seconds')}"

print("\n=== 4. SOLVE ALL 21 ROUND 1 STAGES SEQUENTIALLY ===")
R1_SOLUTIONS = [
    (1, "ORIGIN", 2),
    (2, "629", 3),
    (3, "28/02/2025", 4),
    (4, "22:45", 5),
    (5, "SAFE", 6),
    (6, "ARIAL", 7),
    (7, "CORRUPTED", 8),
    (8, "WHITE", 9),
    (9, "SHADOW_CORE", 10),
    (10, "CONTINUE", 11),
    (11, "ailnors", 12),
    (12, "CLEARANCE_ALPHA", 13),
    (13, "ADITIS13", 14),
    (14, "PROJECT", 15),
    (15, "VECTOR", 16),
    (16, "1400", 17),
    (17, "VSLXI", 18),
    (18, "GCBGE", 19),
    (19, "GAMMA", 20),
    (20, "DAHHK", 21),
    (21, "520", "COMPLETE")
]

for stage_num, key, expected_next in R1_SOLUTIONS:
    res = post("/api/stage/unlock", {
        "team_id": team_id,
        "round": 1,
        "stage": stage_num,
        "password": key
    })
    next_s = res.get("next_stage")
    print(f"  Stage {stage_num:2d} ({key:16s}) -> {res.get('success')} | next: {next_s}")
    assert res.get("success") == True, f"Failed at Stage {stage_num}"
    assert next_s == expected_next, f"Stage {stage_num} expected next {expected_next}, got {next_s}"

print("✓ All 21 Round 1 Stages verified!")

print("\n=== 5. ADVANCE TEAM TO ROUND 2 ===")
adv = post("/api/admin/send_to_round_2", {
    "pin": "admin",
    "team_id": team_id
})
print("Promoted to R2:", adv.get("success"), adv.get("message"))

# Clue request in Round 2 must fail
r2_clue = post("/api/hints/request", {"team_id": team_id, "stage": 1, "round": 2})
print("Round 2 clue request (must fail):", r2_clue.get("success"), "| message:", r2_clue.get("message"))
assert r2_clue.get("success") == False, "Clues must be blocked in Round 2!"

print("\n=== 6. SOLVE ALL 16 ROUND 2 STAGES SEQUENTIALLY ===")
R2_SOLUTIONS = [
    (1, "GUARD", 2),
    (2, "C", 3),
    (3, "BOTTOM LEFT", 4),
    (4, "5", 5),
    (5, "CIPHER", 6),
    (6, "SQUARES", 7),
    (7, "011", 8),
    (8, "CLEARANCE", 9),
    (9, "SE", 10),
    (10, "NONE", 11),
    (11, "RLRCK", 12),
    (12, "NODC", 13),
    (13, "3-EMPTY", 14),
    (14, "FINALS", 15),
    (15, "ECLIPSE", 16),
    (16, "0110", "COMPLETE")
]

for stage_num, key, expected_next in R2_SOLUTIONS:
    res = post("/api/stage/unlock", {
        "team_id": team_id,
        "round": 2,
        "stage": stage_num,
        "password": key
    })
    next_s = res.get("next_stage")
    print(f"  R2 Stage {stage_num:2d} ({key:16s}) -> {res.get('success')} | next: {next_s}")
    assert res.get("success") == True, f"Failed at R2 Stage {stage_num}"
    assert next_s == expected_next, f"R2 Stage {stage_num} expected next {expected_next}, got {next_s}"

print("✓ All 16 Round 2 Stages verified!")
print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! FULL 21-STAGE R1 AND 16-STAGE R2 INTEGRITY CONFIRMED.")
