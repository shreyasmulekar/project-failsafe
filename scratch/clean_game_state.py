import json
import time

with open("data/game_state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

state["current_round"] = 1
state["round_2_started"] = False
state["round_2_active"] = False
state["test_mode_unlock_all"] = False
state["broadcasts"] = []

for tid, team in state.get("teams", {}).items():
    team["current_stage"] = 1
    team["unlocked_stages"] = [1]
    team["stages_cleared"] = []
    team["current_round"] = 1
    team["round_2_unlocked"] = False
    team["round_2_stage"] = 1
    team["round2_stages_cleared"] = []
    team["unlock_all_levels"] = False
    team["lock_all_levels"] = False
    team["test_mode_unlocked"] = False
    team["is_finished"] = False
    team["remote_override_stage"] = 1
    team["remote_reset"] = True
    team["remote_reset_r2"] = True
    team["activity_log"] = [{
        "time": time.strftime("%H:%M:%S"),
        "stage": 1,
        "action": "Workstation initialized to Round 1 Stage 01"
    }]

with open("data/game_state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, indent=2)

print("Game state successfully reset to Round 1 Stage 01 for all teams!")
