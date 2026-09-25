import json

with open("data/game_state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

state["broadcasts"] = []
state["round_1_started"] = True
state["round_2_started"] = False
state["current_round"] = 1

for tid, team in state.get("teams", {}).items():
    team["current_stage"] = 1
    team["unlocked_stages"] = [1]
    team["hints_count"] = 0
    team["hints_history"] = []
    team["traps_count"] = 0
    team["tamper_incidents"] = 0
    team["is_locked"] = False
    team["remote_unlock"] = True
    team["force_logout"] = False
    team["remote_reset"] = False
    team["is_finished"] = False
    team["current_round"] = 1
    team["send_to_round_2"] = False
    team["round_2_unlocked"] = False
    team["round_2_ready"] = False
    team["round_2_stage"] = 1
    team["round_2_unlocked_stages"] = [1]
    team["round_2_is_finished"] = False
    team["last_action"] = "Ready in Round 1"

with open("data/game_state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, indent=2)

print("Game state cleaned and ready for Round 1.")
