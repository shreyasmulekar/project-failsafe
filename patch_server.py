# patch_server.py
import re

with open("server.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace ROUND2_STAGES with complete 15-question dictionary
r2_dict = '''# ROUND 2: StratCom Decryption Arena (15 Progressive Forensic Challenges)
# Clues are strictly disabled in Round 2 per tournament protocol.
ROUND2_STAGES = {
    1: {
        "title": "The Matrix Box Transformation",
        "location": "Visual_Matrix.pdf",
        "keys": ["C", "THREE CIRCLES", "3 CIRCLES", "THREECIRCLES", "●●●"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "hints": ["Look at the rule across rows: Row 1 = Triangles, Row 2 = Squares, Row 3 = Circles. Col 3 must have 3 Circles (Option C)."]
    },
    2: {
        "title": "The Clockwise Rotation Boxes",
        "location": "Rotation_Array.pdf",
        "keys": ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT"],
        "next_stage": 3,
        "hints": ["Trace the movement of the core node as it shifts 90 degrees clockwise. Box 4 is Bottom-Left (BL)."]
    },
    3: {
        "title": "The Spatial Net Folding Box",
        "location": "Cube_Net_Terminal.pdf",
        "keys": ["5"],
        "next_stage": 4,
        "hints": ["In a standard T-shaped cube net, faces separated by one box fold into opposite faces. Face 1 is opposite Face 5."]
    },
    4: {
        "title": "The Whiteout Signature",
        "location": "Emergency_Log.doc",
        "keys": ["CLEARANCE_ALPHA", "CLEARANCE ALPHA", "CLEARANCEALPHA"],
        "next_stage": 5,
        "hints": ["Select all text (Ctrl+A) or toggle UV filter to reveal: DECRYPTION KEY IS CLEARANCE_ALPHA."]
    },
    5: {
        "title": "The ROT-4 IEEE Shift",
        "location": "Encrypted_Beacon.txt",
        "keys": ["ADITIS13", "ADITI-13", "ADITI 13"],
        "next_stage": 6,
        "hints": ["Shift every letter backward by the number of letters in the acronym 'IEEE' (4): EHMXMW13 -> ADITIS13."]
    },
    6: {
        "title": "The Atbash Cipher Mirror",
        "location": "Mirror_Log.txt",
        "keys": ["PROJECT"],
        "next_stage": 7,
        "hints": ["Reverse the alphabet so A <-> Z, B <-> Y. KILQVBG -> PROJECT."]
    },
    7: {
        "title": "The Polybius Coordinate Trail",
        "location": "Matrix_Coordinates.pdf",
        "keys": ["VECTOR"],
        "next_stage": 8,
        "hints": ["Map each pair in the 5x5 grid using (Row, Column) order: (5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R -> VECTOR."]
    },
    8: {
        "title": "The Interlocking Logic Gate Flow",
        "location": "Logic_Gate_Matrix.pdf",
        "keys": ["011", "0,1,1", "0-1-1"],
        "next_stage": 9,
        "hints": ["Trace binary inputs through AND, OR, and XOR gates. Final terminal bus reads 011."]
    },
    9: {
        "title": "The QWERTY Geometry Shape Trace",
        "location": "Keyboard_Telemetry.pdf",
        "keys": ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        "next_stage": 10,
        "hints": ["Connecting key clusters across the mechanical switchboard forms three geometric squares."]
    },
    10: {
        "title": "The Mirror Image String Inversion",
        "location": "Reflection_Buffer.txt",
        "keys": ["CLEARANCE"],
        "next_stage": 11,
        "hints": ["Reflect the inverted vertical glyphs along the horizontal axis to reconstruct 'CLEARANCE'."]
    },
    11: {
        "title": "The Palindrome Filter Stream",
        "location": "Spectral_Filter.log",
        "keys": ["RLRCK"],
        "next_stage": 12,
        "hints": ["Extract the center symmetry markers from the recursive buffer sequences: RLRCK."]
    },
    12: {
        "title": "The Perimeter Geometry Box Count",
        "location": "Perimeter_Grid.pdf",
        "keys": ["102", "102 BOXES"],
        "next_stage": 13,
        "hints": ["Sum the active outer perimeter structural nodes: 102."]
    },
    13: {
        "title": "The Alternating Checker Pattern",
        "location": "Checker_State.pdf",
        "keys": ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        "next_stage": 14,
        "hints": ["Predict the 5th generation parity cycle: exactly three empty containment blocks."]
    },
    14: {
        "title": "The Find-and-Replace Frequency Count",
        "location": "Mass_System_Log.txt",
        "keys": ["1400", "1,400"],
        "next_stage": 15,
        "hints": ["Searching for OVERRIDE finds 14 matches. 14 x 100 = 1400."]
    },
    15: {
        "title": "The Cipher Wheel Protocol (THE RED QUESTION)",
        "location": "Wheel_Overlay.pdf",
        "keys": ["ECLIPSE"],
        "next_stage": "COMPLETE",
        "hints": ["Align the inner wheel over the outer wheel at 135 degrees clockwise. Exposed cutouts spell: ECLIPSE."]
    }
}'''

# Replace ROUND2_STAGES definition
pattern = r"# ROUND 2: StratCom Decryption Arena.*?ROUND2_STAGES = \{.*?\n\}"
code = re.sub(pattern, r2_dict, code, flags=re.DOTALL)

# In /api/teams/finish, update round 2 finish check from 9 to 15
code = code.replace('"stage": 9 if round_num == 2 else 15,', '"stage": 15,')
code = code.replace('team["round_2_stage"] = 9', 'team["round_2_stage"] = 15')

# Add /api/teams/request_fullscreen_exit and /api/admin/approve_fullscreen_exit
new_endpoints = '''        if path == "/api/teams/request_fullscreen_exit":
            team_id = data.get("team_id", "").strip().upper()
            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return
            if "teams" not in state:
                state["teams"] = {}
            team = state["teams"].get(team_id)
            if not team:
                self._send_json(404, {"error": "Team not found"})
                return
            team["fullscreen_exit_requested"] = True
            team["fullscreen_exit_requested_at"] = time.time()
            team["last_action"] = "⚠️ Requested Fullscreen Exit from Organizer"
            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": team.get("current_stage", 1),
                "action": "Requested Fullscreen Exit authorization"
            })
            save_game_state(state)
            self._send_json(200, {
                "success": True,
                "message": "Fullscreen exit request transmitted to Command Center. Awaiting Organizer approval."
            })
            return

        if path == "/api/admin/approve_fullscreen_exit":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()
            action = data.get("action", "approve").lower()

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            if "teams" not in state or team_id not in state["teams"]:
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            team = state["teams"][team_id]
            now = time.time()
            if action == "approve":
                team["fullscreen_exit_requested"] = False
                team["fullscreen_exit_approved"] = True
                team["fullscreen_exit_approved_until"] = now + 90 # 90 seconds window
                team["last_action"] = "Organizer APPROVED Fullscreen Exit"
                if "activity_log" not in team:
                    team["activity_log"] = []
                team["activity_log"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": team.get("current_stage", 1),
                    "action": "Organizer APPROVED Fullscreen Exit (90s window)"
                })
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Fullscreen exit approved for {team_id}"
                })
            else:
                team["fullscreen_exit_requested"] = False
                team["fullscreen_exit_approved"] = False
                team["last_action"] = "Organizer DENIED Fullscreen Exit"
                if "activity_log" not in team:
                    team["activity_log"] = []
                team["activity_log"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": team.get("current_stage", 1),
                    "action": "Organizer DENIED Fullscreen Exit"
                })
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Fullscreen exit denied for {team_id}"
                })
            return

        if path == "/api/admin/pending_fullscreen_requests":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return
            pending = []
            for tid, t in state.get("teams", {}).items():
                if t.get("fullscreen_exit_requested"):
                    pending.append({
                        "team_id": tid,
                        "team_name": t.get("team_name", tid),
                        "requested_at": t.get("fullscreen_exit_requested_at", 0),
                        "current_stage": t.get("current_stage", 1)
                    })
            self._send_json(200, {"success": True, "pending": pending})
            return
'''

# Insert new endpoints right after path == "/api/teams/finish": ... return
insert_marker = 'if path == "/api/teams/activity":'
if insert_marker in code:
    code = code.replace(insert_marker, new_endpoints + "\n        " + insert_marker)

# In /api/teams/activity, enhance response with fullscreen and round 2 gating info
old_activity_resp = '''            self._send_json(200, {
                "success": True,
                "remote_unlock": remote_unlocked,
                "remote_reset": remote_reset,
                "force_logout": force_logout,
                "current_stage": team.get("current_stage", 1),
                "broadcasts": state.get("broadcasts", [])
            })'''

new_activity_resp = '''            now_ts = time.time()
            fs_approved = bool(team.get("fullscreen_exit_approved", False) and (team.get("fullscreen_exit_approved_until", 0) > now_ts))
            r2_started = bool(state.get("round_2_started", False))
            shortlist = state.get("shortlist", [])
            is_short = bool(team_id in shortlist)

            self._send_json(200, {
                "success": True,
                "remote_unlock": remote_unlocked,
                "remote_reset": remote_reset,
                "force_logout": force_logout,
                "fullscreen_exit_requested": team.get("fullscreen_exit_requested", False),
                "fullscreen_exit_approved": fs_approved,
                "round_2_started": r2_started,
                "is_shortlisted": is_short,
                "round_2_ready": bool(r2_started and is_short),
                "current_stage": team.get("current_stage", 1),
                "broadcasts": state.get("broadcasts", [])
            })'''

code = code.replace(old_activity_resp, new_activity_resp)

with open("server.py", "w", encoding="utf-8") as f:
    f.write(code)

print("server.py successfully patched!")
