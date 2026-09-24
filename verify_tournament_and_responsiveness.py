import urllib.request
import json
import time
import os

ADMIN_PIN = "wie-admin-2026"
BASE_URL = "http://127.0.0.1:8000"

def post_json(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_json(endpoint):
    url = f"{BASE_URL}{endpoint}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))

def test_tournament_ranking():
    print("\n=======================================================")
    print("   1. TOURNAMENT RANKING & LEAST TIME VERIFICATION")
    print("=======================================================")
    
    test_teams_config = [
        # (team_id, team_name, current_round, cur_stage, is_fin, r2_stage, r2_fin, time_adj)
        ("T-ALPHA", "Alpha Grand Champions", 2, 16, True, 15, True, -200),  # Tier 0: Finished R1+R2 in least time -> Rank 1
        ("T-BETA",  "Beta Laureates",         2, 16, True, 15, True, +400),  # Tier 0: Finished R1+R2 in slower time -> Rank 2
        ("T-GAMMA", "Gamma Decryptors",       2, 16, True, 12, False, 0),    # Tier 1: In R2 at Puzzle 12 -> Rank 3
        ("T-DELTA", "Delta Vanguard",         2, 16, True, 5,  False, 0),    # Tier 1: In R2 at Puzzle 5 -> Rank 4
        ("T-EPSILON","Epsilon Finalists",     1, 16, True, 1,  False, -50),  # Tier 2: Cleared R1 (ready for R2) -> Rank 5
        ("T-ZETA",  "Zeta Operators",         1, 10, False, 1, False, 0),    # Tier 3: In R1 at Stage 10 -> Rank 6
    ]
    
    for tid, tname, cr, cs, fin, r2s, r2fin, adj in test_teams_config:
        # Register team
        post_json("/api/teams/register", {
            "team_id": tid,
            "team_name": tname,
            "password": "Password123!",
            "members": "Cadet A, Cadet B"
        })
        # Edit parameters via Admin API
        post_json("/api/admin/teams/edit", {
            "pin": ADMIN_PIN,
            "team_id": tid,
            "team_name": tname,
            "current_round": cr,
            "current_stage": cs,
            "is_finished": fin,
            "round_2_stage": r2s,
            "round_2_is_finished": r2fin,
            "time_adjustment_sec": adj,
            "hints_count": 0,
            "traps_count": 0
        })
    print("[OK] All 6 test squads registered and configured with distinct tournament statuses.")
    
    # 1. Admin Leaderboard API
    admin_lb = get_json(f"/api/admin/leaderboard?pin={ADMIN_PIN}")
    lb = admin_lb.get("leaderboard", [])
    for t in lb:
        if t["team_id"] in [c[0] for c in test_teams_config]:
            print(f"Team: {t['team_id']} -> cur_rnd={t.get('current_round')} cs={t.get('current_stage')} fin={t.get('is_finished')} r2fin={t.get('round_2_is_finished')} adj_time={t.get('adjusted_time_sec')}")
    
    ranked_ids = [t["team_id"] for t in lb if t["team_id"] in [c[0] for c in test_teams_config]]
    print(f"Admin Leaderboard Rank Order: {ranked_ids}")
    
    expected_order = ["T-ALPHA", "T-BETA", "T-GAMMA", "T-DELTA", "T-EPSILON", "T-ZETA"]
    assert ranked_ids == expected_order, f"Admin ranking failed! Expected {expected_order}, got {ranked_ids}"
    print("✅ TEST 1 PASSED: Admin Leaderboard correctly ranks Grand Champions who completed entire tournament (R1+R2) with least time as #1!")
    
    # Check Grand Champion attributes in admin leaderboard
    top_team = next(t for t in lb if t["team_id"] == "T-ALPHA")
    assert top_team["round_2_is_finished"] is True, "T-ALPHA should have round_2_is_finished == True"
    second_team = next(t for t in lb if t["team_id"] == "T-BETA")
    assert top_team["adjusted_time_sec"] < second_team["adjusted_time_sec"], "T-ALPHA must have lower time than T-BETA"
    print(f"   -> Grand Champion T-ALPHA Adjusted Time: {top_team['adjusted_time_sec']}s")
    print(f"   -> Runner-up     T-BETA  Adjusted Time: {second_team['adjusted_time_sec']}s")
    
    # 2. Teams Public Leaderboard API
    team_lb = get_json("/api/teams/leaderboard")
    team_ranked = [t["team_id"] for t in team_lb.get("leaderboard", []) if t["team_id"] in [c[0] for c in test_teams_config]]
    assert team_ranked == expected_order, f"Team ranking failed! Expected {expected_order}, got {team_ranked}"
    print("✅ TEST 2 PASSED: Participant Leaderboard API strictly mirrors tournament hierarchy!")
    
    # 3. Shortlist Reset API
    reset_res = post_json("/api/admin/shortlist/reset", {"pin": ADMIN_PIN})
    q_ids = reset_res.get("qualified_team_ids", [])
    assert "T-ALPHA" in q_ids and "T-BETA" in q_ids, "Grand Champions must be in qualified list"
    print("✅ TEST 3 PASSED: Shortlist auto-selection respects tournament hierarchy!")

if __name__ == "__main__":
    test_tournament_ranking()
