import re
import json

def update_server():
    with open("server.py", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update STAGES to 11 curated stages
    curated_stages_code = '''# Master Stage Passwords & Solutions (Curated 11 Storyline Stages)
# Rogue AI: ISHAAN | Companion AI: TARA | Architect: DR. ADITI SHARMA
STAGES = {
    1: {
        "title": "ISHAAN Recovery Terminal",
        "keys": ["ACCESS", "RECOVER ACCESS", "ORIGIN", "ACCESS GRANTED"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "hints": [
            "Review the recovery sequence: LOGIN -> VERIFY -> ? -> EXECUTE -> LOCK.",
            "What command gives permission to reach the core? (ACCESS)."
        ]
    },
    2: {
        "title": "ISHAAN's Memory Core",
        "keys": ["123456", "1-2-3-4-5-6", "MEMORY_RESTORED", "MEMORY RESTORED", "RESTORE", "CHRONOLOGICAL", "INITIATE"],
        "next_stage": 3,
        "hints": [
            "Put the 6 recovered memory fragments in chronological order based on their timestamps.",
            "Order from earliest to latest: 4:17 PM -> 6:45 PM -> 8:10 PM -> 9:32 PM -> 10:03 PM -> 10:15 PM (Sequence: 123456)."
        ]
    },
    3: {
        "title": "The Simple Acrostic Note",
        "keys": ["SAFE", "LOOK BEHIND THE DATE", "LOOKBEHINDTHEDATE"],
        "next_stage": 4,
        "hints": [
            "Read between the lines—or rather, read the start of every sentence in Aditi_Memo.doc.",
            "Take the first letter of each of the 4 sentences: S-A-F-E."
        ]
    },
    4: {
        "title": "The Calendar Anomaly (Non-Leap Year)",
        "keys": ["28/02/2025", "02292025", "29022025", "20250229", "28022025", "29/02/2025", "FEB 29, 2025"],
        "next_stage": 5,
        "hints": [
            "Inspect the dates in Incident_Logs.doc. Check the calendar rules for the year 2025.",
            "2025 is not a leap year. February 29, 2025 does not exist! The corrected date is 28/02/2025."
        ]
    },
    5: {
        "title": "Clearance Elevation (A1Z26 Code)",
        "keys": ["POLARIS"],
        "next_stage": 6,
        "hints": [
            "The key position in the alphabet reveals the directory clearance.",
            "Convert numbers [16-15-12-01-18-09-19] to letters: 1=A, 2=B... 16=P, 15=O, etc. (POLARIS)."
        ]
    },
    6: {
        "title": "Margin Diagnostics (Resolved Comments)",
        "keys": ["MARGIN_KEY", "MARGINKEY", "22:46", "2246"],
        "next_stage": 7,
        "hints": [
            "Dr. Aditi left notes in the margins, resolved before ISHAAN could delete them.",
            "Open System_Diagnostics.doc and click the resolved comments history button."
        ]
    },
    7: {
        "title": "The Font Style Verification",
        "keys": ["ARIAL", "AUTHENTIC"],
        "next_stage": 8,
        "hints": [
            "The real log strictly follows the lab's formatting standard. Check the font.",
            "Dr. Aditi always formats authentic logs in Arial sans-serif. Decoy memos use Times New Roman."
        ]
    },
    8: {
        "title": "Morse Audio Transmission (Bunker Signal)",
        "keys": ["WHITE", "SOS_ADITI", "SOSADITI", "MORSE", "BEACON"],
        "next_stage": 9,
        "hints": [
            "Listen to audio_log_07.mp3 or inspect the audio spectrogram.",
            "Decode the CW audio beeps: .-- .... .. - . spells WHITE."
        ]
    },
    9: {
        "title": "Version Scrub (Git Reflog)",
        "keys": ["HISTORY", "OVERRIDE FAILED", "OVERRIDEFAILED", "7B8A1C9"],
        "next_stage": 10,
        "hints": [
            "ISHAAN force-pushed a forged commit, but the Git reflog preserves the truth.",
            "Check commit 7b8a1c9 at 20:18. The commit message was 'OVERRIDE FAILED'."
        ]
    },
    10: {
        "title": "Psychological Honeypot Trap",
        "keys": ["BYPASS", "SKIP", "DISARM"],
        "next_stage": 11,
        "hints": [
            "DO_NOT_RUN.exe is an active AI honeypot trap! Do not submit credentials into it.",
            "To disarm the honeypot safely without incurring the +5m penalty, type 'BYPASS' in the shell."
        ]
    },
    11: {
        "title": "The Master IEEE WIE Failsafe Protocol",
        "keys": ["6-9-11", "6911", "WISDOM-INTEGRITY-EMPOWERMENT", "WISDOM INTEGRITY EMPOWERMENT", "WISDOM, INTEGRITY, EMPOWERMENT"],
        "next_stage": None,
        "hints": [
            "The failsafe is encoded in IEEE Women in Engineering's three founding core values.",
            "Count the letters of each core value: Wisdom (6), Integrity (9), Empowerment (11). Enter '6-9-11'."
        ]
    }
}'''

    # Replace STAGES block
    stages_pattern = r'# Master Stage Passwords & Solutions[\s\S]*?15: \{[\s\S]*?\}\s*\}'
    content = re.sub(stages_pattern, curated_stages_code, content, count=1)
    print("Replaced STAGES with curated 11 story stages")

    # 2. Add endpoints for team edit and delete in do_POST:
    admin_endpoints_code = '''
        if path == "/api/admin/teams/edit":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            team_id = data.get("team_id", "").strip().upper()
            if not team_id or team_id not in state.get("teams", {}):
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            team = state["teams"][team_id]
            if "team_name" in data and data["team_name"]:
                team["team_name"] = str(data["team_name"]).strip()
            if "members" in data:
                team["members"] = str(data["members"]).strip()
            if "password" in data and data["password"]:
                team["password"] = str(data["password"]).strip()
            if "current_stage" in data:
                team["current_stage"] = max(1, min(11, int(data["current_stage"])))
                team["remote_override_stage"] = team["current_stage"]
            if "round_2_stage" in data:
                team["round_2_stage"] = max(1, min(9, int(data["round_2_stage"])))
            if "current_round" in data:
                team["current_round"] = int(data["current_round"])
            if "hints_count" in data:
                team["hints_count"] = max(0, int(data["hints_count"]))
            if "traps_count" in data:
                team["traps_count"] = max(0, int(data["traps_count"]))
            if "time_adjustment_sec" in data:
                team["time_adjustment_sec"] = int(data["time_adjustment_sec"])
            if "is_finished" in data:
                team["is_finished"] = bool(data["is_finished"])
            if "round_2_is_finished" in data:
                team["round_2_is_finished"] = bool(data["round_2_is_finished"])

            team["last_action"] = f"✏️ Organizer Adjusted Profile & Parameters ({datetime.now().strftime('%H:%M:%S')})"
            save_game_state(state, immediate=True)

            self._send_json(200, {
                "success": True,
                "message": f"Team '{team_id}' parameters updated successfully",
                "team": team
            })
            return

        if path == "/api/admin/teams/delete":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            team_id = data.get("team_id", "").strip().upper()
            if not team_id or team_id not in state.get("teams", {}):
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            del state["teams"][team_id]

            # Remove from shortlist if present
            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            q_ids = shortlist_meta.setdefault("round_2_qualified_team_ids", [])
            if team_id in q_ids:
                q_ids.remove(team_id)

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": f"Team '{team_id}' permanently removed from tournament ledger",
                "remaining_teams_count": len(state["teams"])
            })
            return
'''

    if '/api/admin/teams/edit' not in content:
        insert_marker = 'if path == "/api/admin/shortlist/toggle":'
        content = content.replace(insert_marker, admin_endpoints_code + "\n        " + insert_marker)
        print("Added /api/admin/teams/edit and /api/admin/teams/delete endpoints")

    # 3. Update /api/teams/finish to compute 1st, 2nd, 3rd prize placements
    prize_logic_code = '''
                if round_num == 2:
                    team["round_2_is_finished"] = True
                    team["round_2_stage"] = 9
                    team["round_2_end_time"] = now
                    team["round_2_finish_time_str"] = elapsed_str
                    if stage_times:
                        team["round_2_stage_times"] = stage_times

                    # Count how many teams have finished Round 2
                    r2_finished_count = sum(
                        1 for tid, t in state.get("teams", {}).items()
                        if t.get("round_2_is_finished")
                    )

                    if r2_finished_count == 1:
                        prize_code = "1ST_PRIZE"
                        prize_title = "🥇 1ST PRIZE — GRAND CHAMPION"
                        podium_rank = 1
                    elif r2_finished_count == 2:
                        prize_code = "2ND_PRIZE"
                        prize_title = "🥈 2ND PRIZE — RUNNER-UP LAUREATE"
                        podium_rank = 2
                    elif r2_finished_count == 3:
                        prize_code = "3RD_PRIZE"
                        prize_title = "🥉 3RD PRIZE — SECOND RUNNER-UP"
                        podium_rank = 3
                    else:
                        prize_code = "HONORARY_LAUREATE"
                        prize_title = f"🎖️ HONORARY LAUREATE (#{r2_finished_count})"
                        podium_rank = r2_finished_count

                    team["prize_code"] = prize_code
                    team["prize_title"] = prize_title
                    team["podium_rank"] = podium_rank
                    team["last_action"] = f"🏆 {prize_title} in {elapsed_str}!"
'''
    old_r2_finish_pattern = r'if round_num == 2:\s*team\["round_2_is_finished"\] = True[\s\S]*?team\["last_action"\] = f"🏆 ROUND 2 COMPLETE: Solved 9 Puzzles in \{elapsed_str\}!"'
    content = re.sub(old_r2_finish_pattern, prize_logic_code.strip(), content, count=1)
    print("Updated Round 2 finish logic with 1st, 2nd, 3rd prize detection")

    # 4. In do_GET /api/team/round_status, return prize_info, client telemetry, and forced_stage_override
    old_round_status = '''            self._send_json(200, {
                "team_id": team_id,
                "current_round": current_round,
                "is_qualified_for_round_2": is_qualified,
                "round_2_unlocked": current_round >= 2 and is_qualified,
                "round_2_stage": team.get("round_2_stage", 1),
                "round_2_stages_total": len(ROUND2_STAGES),
                "round_2_is_finished": team.get("round_2_is_finished", False),
                "round_2_finish_time_str": team.get("round_2_finish_time_str", "")
            })'''

    new_round_status = '''            self._send_json(200, {
                "team_id": team_id,
                "current_round": current_round,
                "is_qualified_for_round_2": is_qualified,
                "round_2_unlocked": current_round >= 2 and is_qualified,
                "round_2_stage": team.get("round_2_stage", 1),
                "round_2_stages_total": len(ROUND2_STAGES),
                "round_2_is_finished": team.get("round_2_is_finished", False),
                "round_2_finish_time_str": team.get("round_2_finish_time_str", ""),
                "prize_code": team.get("prize_code", ""),
                "prize_title": team.get("prize_title", ""),
                "podium_rank": team.get("podium_rank", 0),
                "remote_override_stage": team.get("remote_override_stage"),
                "force_logout": team.get("force_logout", False),
                "remote_reset": team.get("remote_reset", False),
                "is_locked": team.get("is_locked", False)
            })'''

    if old_round_status in content:
        content = content.replace(old_round_status, new_round_status)
        print("Updated /api/team/round_status response")

    # 5. In /api/teams/activity, store client_info, active_view, and violations_history
    activity_store_marker = 'if action:\n                team["last_action"] = action'
    new_activity_store = '''if "client_info" in data and data["client_info"]:
                team["client_info"] = data["client_info"]
            if "active_view" in data and data["active_view"]:
                team["active_view"] = data["active_view"]
            if "violations_history" in data and data["violations_history"]:
                team["violations_history"] = data["violations_history"]

            if action:
                team["last_action"] = action'''
    if activity_store_marker in content:
        content = content.replace(activity_store_marker, new_activity_store)
        print("Updated /api/teams/activity to store granular client telemetry")

    with open("server.py", "w", encoding="utf-8") as f:
        f.write(content)

    print("server.py updated successfully!")

if __name__ == '__main__':
    update_server()
