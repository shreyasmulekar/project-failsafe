import json

print("--- Fixing server.py remote-unlock logic ---")
with open("server.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace in team_id == "ALL" block
old_all = """                    t["remote_unlock"] = True
                    t["is_locked"] = False
                    t["tamper_incidents"] = 0
                    t["violations_history"] = []
                    t["fullscreen_exit_approved"] = True
                    t["fullscreen_exit_approved_until"] = time.time() + 86400"""

new_all = """                    t["remote_unlock"] = True
                    t["is_locked"] = False
                    t["tamper_incidents"] = 0
                    t["violations_history"] = []"""

# Replace in single team block
old_single = """            team["remote_unlock"] = True
            team["is_locked"] = False
            team["tamper_incidents"] = 0
            team["violations_history"] = []
            team["fullscreen_exit_approved"] = True
            team["fullscreen_exit_approved_until"] = time.time() + 86400"""

new_single = """            team["remote_unlock"] = True
            team["is_locked"] = False
            team["tamper_incidents"] = 0
            team["violations_history"] = []"""

# Replace in /api/teams/activity
old_activity = """            remote_unlocked = team.get("remote_unlock", False)
            if remote_unlocked or fs_approved:
                team["remote_unlock"] = False
                team["is_locked"] = False
                team["tamper_incidents"] = 0
                team["violations_history"] = []"""

new_activity = """            remote_unlocked = team.get("remote_unlock", False)
            if remote_unlocked:
                team["remote_unlock"] = False
                team["is_locked"] = False
                team["tamper_incidents"] = 0
                team["violations_history"] = []"""

if old_all in code:
    code = code.replace(old_all, new_all, 1)
    print("Fixed ALL block in server.py")
else:
    print("WARNING: old_all not found")

if old_single in code:
    code = code.replace(old_single, new_single, 1)
    print("Fixed single team block in server.py")
else:
    print("WARNING: old_single not found")

if old_activity in code:
    code = code.replace(old_activity, new_activity, 1)
    print("Fixed activity block in server.py")
else:
    print("WARNING: old_activity not found")

with open("server.py", "w", encoding="utf-8") as f:
    f.write(code)

# Clean up TEST_SEC in data/game_state.json and game_state.json
for p in ["data/game_state.json", "game_state.json"]:
    try:
        with open(p, "r", encoding="utf-8") as f:
            d = json.load(f)
        if "teams" in d and "TEST_SEC" in d["teams"]:
            del d["teams"]["TEST_SEC"]
            print(f"Removed TEST_SEC from {p}")
        d["global_fullscreen_exit_allowed"] = False
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2)
        print(f"Cleaned {p}")
    except Exception as e:
        print(f"Error on {p}: {e}")

print("SUCCESS: fix_remote_unlock_logic.py finished")
