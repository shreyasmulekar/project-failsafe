import sys
sys.stdout.reconfigure(encoding='utf-8')
import urllib.request
import json
import time

BASE = "http://127.0.0.1:8000"
PIN = "wie-admin-2026"

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

def get_leaderboard():
    with urllib.request.urlopen(f"{BASE}/api/admin/leaderboard?pin={PIN}") as resp:
        return json.loads(resp.read().decode('utf-8'))

print("=== 1. REGISTER SQUAD ===")
team_id = f"TRACK-COMPLETION-{int(time.time())}"
reg = post("/api/teams/register", {
    "team_id": team_id,
    "team_name": "Full Track Squad",
    "password": "pass",
    "leader_name": "Track Master"
})
print("Registered:", reg.get("message"))

# Start round 1
post("/api/admin/start_round_1", {"pin": PIN})

print("\n=== 2. SOLVE ALL 21 ROUND 1 STAGES ===")
R1_KEYS = [
    (1, "ORIGIN"), (2, "629"), (3, "28/02/2025"), (4, "22:45"),
    (5, "SAFE"), (6, "ARIAL"), (7, "CORRUPTED"), (8, "WHITE"),
    (9, "SHADOW_CORE"), (10, "CONTINUE"), (11, "ailnors"), (12, "CLEARANCE_ALPHA"),
    (13, "ADITIS13"), (14, "PROJECT"), (15, "VECTOR"), (16, "1400"),
    (17, "VSLXI"), (18, "GCBGE"), (19, "GAMMA"), (20, "DAHHK"),
    (21, "520")
]

mock_stage_times = {}
simulated_start = time.time() - 1200
for s, k in R1_KEYS:
    res = post("/api/stage/unlock", {
        "team_id": team_id,
        "stage": s,
        "password": k,
        "round": 1
    })
    assert res.get("success"), f"Stage {s} failed: {res}"
    mock_stage_times[str(s)] = {
        "start": simulated_start + (s - 1) * 50,
        "end": simulated_start + s * 50,
        "duration_seconds": 50,
        "duration_str": "0m 50s"
    }

print("All 21 stages solved on backend.")

print("\n=== 3. RECORD ROUND 1 TRACK FINISH ===")
fin_r1 = post("/api/teams/finish", {
    "team_id": team_id,
    "team_name": "Full Track Squad",
    "members": "Track Master",
    "password": "pass",
    "round": 1,
    "elapsed_seconds": 1050,
    "elapsed_str": "17m 30s",
    "stage_times": mock_stage_times
})
print("R1 Finish Result:", fin_r1.get("success"), fin_r1.get("message"))

# Verify state in admin/leaderboard
lb = get_leaderboard()
team_state = next(t for t in lb["leaderboard"] if t["team_id"] == team_id)
print("Team state after R1 Finish:")
print(f"  current_stage: {team_state.get('current_stage')}")
print(f"  is_finished: {team_state.get('is_finished')}")
print(f"  stage_title: {team_state.get('stage_title')}")
assert team_state.get("current_stage") == 21, f"Expected 21, got {team_state.get('current_stage')}"
assert team_state.get("is_finished") is True

print("\n=== 4. PROMOTE SQUAD TO ROUND 2 ===")
post("/api/admin/start_round_2", {"pin": PIN})
promo = post("/api/admin/send_to_round_2", {
    "pin": PIN,
    "team_id": team_id
})
print("Promotion:", promo.get("message"))

print("\n=== 5. SOLVE ALL 17 ROUND 2 STAGES ===")
R2_KEYS = [
    (1, "GUARD"), (2, "C"), (3, "BOTTOM LEFT"), (4, "5"),
    (5, "CIPHER"), (6, "SQUARES"), (7, "011"), (8, "CLEARANCE"),
    (9, "SE"), (10, "NONE"), (11, "RLRCK"), (12, "NODC"),
    (13, "3-EMPTY"), (14, "FINALS"), (15, "ECLIPSE"), (16, "0110")
]

mock_r2_times = {}
for s, k in R2_KEYS:
    res = post("/api/stage/unlock", {
        "team_id": team_id,
        "stage": s,
        "password": k,
        "round": 2
    })
    assert res.get("success"), f"R2 Stage {s} failed: {res}"
    mock_r2_times[str(s)] = {
        "start": simulated_start + (s - 1) * 45,
        "end": simulated_start + s * 45,
        "duration_seconds": 45,
        "duration_str": "0m 45s"
    }

print("All 16 Round 2 stages solved on backend.")

print("\n=== 6. RECORD ROUND 2 TRACK FINISH (GRAND CHAMPION) ===")
fin_r2 = post("/api/teams/finish", {
    "team_id": team_id,
    "team_name": "Full Track Squad",
    "members": "Track Master",
    "password": "pass",
    "round": 2,
    "elapsed_seconds": 720,
    "elapsed_str": "12m 00s",
    "stage_times": mock_r2_times
})
print("R2 Grand Finish Result:", fin_r2)
assert fin_r2.get("prize_code") in ["1ST_PRIZE", "2ND_PRIZE", "3RD_PRIZE", "HONORARY_LAUREATE"]

lb_final = get_leaderboard()
team_final = next(t for t in lb_final["leaderboard"] if t["team_id"] == team_id)
print("\n=== FINAL TEAM LEADERBOARD VERIFICATION ===")
print(f"  Team ID: {team_id}")
print(f"  R1 Finished: {team_final.get('is_finished')} (Stage {team_final.get('current_stage')}/21)")
print(f"  R2 Finished: {team_final.get('round_2_is_finished')} (Stage {team_final.get('round_2_stage')}/16)")
print(f"  Prize: {team_final.get('prize_title')}")
print(f"  Podium Rank: #{team_final.get('podium_rank')}")

assert team_final.get("round_2_is_finished") is True
assert team_final.get("round_2_stage") == 17

print("\n[SUCCESS] FULL TRACK COMPLETION VERIFIED END-TO-END ACROSS BOTH ROUNDS!")
