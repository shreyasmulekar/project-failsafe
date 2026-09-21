#!/usr/bin/env python3
"""
PROJECT FAILSAFE: Local Offline Event Server
Zero-dependency HTTP & REST server using Python 3 standard library.
Handles stage progression, password verification, hint penalties,
trap triggers, and organizer leaderboard.
"""

import http.server
import json
import os
import sys
import time
import urllib.parse
from datetime import datetime

PORT = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8000))
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "game_state.json")
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
ADMIN_PIN = "wie-admin-2026"

# Master Stage Passwords & Solutions (faithful to Master Document)
STAGES = {
    1: {
        "title": "The Whiteout Text",
        "keys": ["INITIATE", "ORIGIN"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "hints": [
            "Highlight everything to see what is hidden in plain sight.",
            "Press Ctrl+A or toggle UV light to reveal the hidden white ink in Welcome_Log.doc."
        ]
    },
    2: {
        "title": "The Simple Acrostic Note",
        "keys": ["SAFE", "LOOK BEHIND THE DATE", "LOOKBEHINDTHEDATE"],
        "next_stage": 3,
        "hints": [
            "Read between the lines—or rather, read the start of every sentence.",
            "Take the first letter of each of the 4 sentences in Aditi_Memo.doc."
        ]
    },
    3: {
        "title": "The A1Z26 Alphabet Code",
        "keys": ["POLARIS", "28/02/2025", "02292025", "29022025", "2025-02-29", "FEB 29, 2025", "29/02/2025"],
        "next_stage": 4,
        "hints": [
            "The key position in the alphabet reveals the directory clearance.",
            "Convert numbers [16-15-12-01-18-09-19] to letters: 1=A, 2=B... 16=P, 15=O, etc."
        ]
    },
    4: {
        "title": "The Resolved Comments Log",
        "keys": ["MARGIN_KEY", "MARGINKEY", "22:46", "2246"],
        "next_stage": 5,
        "hints": [
            "Dr. Aditi left notes in the margins, resolved before ADI could delete them.",
            "Open System_Diagnostics.doc and check the resolved comments history."
        ]
    },
    5: {
        "title": "The Font Style Verification",
        "keys": ["ARIAL", "AUTHENTIC"],
        "next_stage": 6,
        "hints": [
            "The real log strictly follows the lab's formatting standard. Check the font.",
            "Dr. Aditi always formats authentic logs in Arial 11pt with 1.15 line spacing."
        ]
    },
    6: {
        "title": "The Steganography Mask",
        "keys": ["SHADOW_CORE", "SHADOWCORE"],
        "next_stage": 7,
        "hints": [
            "The image Dark_Terminal.png appears completely pitch black.",
            "Increase the exposure/brightness to maximum in a photo editor or using the in-console slider to reveal what hides in the shadows."
        ]
    },
    7: {
        "title": "The Embedded QR / Pixel Art",
        "keys": ["7702", "WHITE", "DONOTFOLLOWBLUE"],
        "next_stage": 8,
        "hints": [
            "Zoom out and look at the bigger picture, or enhance the contrast.",
            "Fill in or enhance the dark cells in Corrupted_Image_Block.doc to read the 4-digit code."
        ]
    },
    8: {
        "title": "The Revision History Conflict",
        "keys": ["FALSE_RECORDS", "FALSERECORDS", "THE AI CAN MODIFY WHAT YOU SEE", "THEAICANMODIFYWHATYOUSEE"],
        "next_stage": 9,
        "hints": [
            "Compare the current version edited by 'SYSTEM_ADI' with the draft edited by 'Dr. Aditi' at 20:00.",
            "Look at the Version History in Sanctuary_Inventory.sheet to find the uncorrupted row."
        ]
    },
    9: {
        "title": "Version Scrub (Git Reflog)",
        "keys": ["HISTORY", "OVERRIDE FAILED", "OVERRIDEFAILED"],
        "next_stage": 10,
        "hints": [
            "Look at the Version History of Incident_Report.doc to see what Dr. Aditi originally wrote.",
            "Check commit 7b8a1c9 at 20:18 before ADI modified the commit log."
        ]
    },
    10: {
        "title": "Honeypot Trap Bypass",
        "keys": ["BYPASS", "SKIP"],
        "next_stage": 11,
        "hints": [
            "CRITICAL WARNING: The emergency shutdown executable is an AI honeypot trap!",
            "Do NOT submit credentials into the trap. Type 'decrypt BYPASS' to disarm it safely."
        ]
    },
    11: {
        "title": "The WIE Failsafe",
        "keys": ["6-9-11", "6911", "WISDOM-INTEGRITY-EMPOWERMENT", "WISDOM INTEGRITY EMPOWERMENT"],
        "next_stage": "COMPLETE",
        "hints": [
            "The real failsafe is encoded in WIE's foundational core values.",
            "Count the letter lengths of Wisdom (6), Integrity (9), and Empowerment (11)."
        ]
    }
}

def load_game_state():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        initial_state = {
            "teams": {},
            "broadcasts": [],
            "created_at": datetime.now().isoformat()
        }
        save_game_state(initial_state)
        return initial_state
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data file: {e}, resetting...")
        return {"teams": {}, "broadcasts": [], "created_at": datetime.now().isoformat()}

def save_game_state(state):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

class FailsafeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def _send_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/api/status":
            self._send_json(200, {
                "status": "online",
                "system": "PROJECT FAILSAFE SERVER",
                "server_time": time.time()
            })
            return

        if path in ["/admin", "/admin.html"]:
            admin_file = os.path.join(PUBLIC_DIR, "admin.html")
            if not os.path.exists(admin_file):
                admin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "admin.html")
            if os.path.exists(admin_file):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(admin_file, "rb") as f:
                    self.wfile.write(f.read())
                return

        if path in ["/", "/index.html", "/aditi_os_widget.html"]:
            target_name = "index.html" if path == "/" else os.path.basename(path)
            root_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), target_name)
            if os.path.exists(root_file):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(root_file, "rb") as f:
                    self.wfile.write(f.read())
                return

        if path == "/api/admin/leaderboard":
            pin = params.get("pin", [""])[0]
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            state = load_game_state()
            leaderboard = []
            now = time.time()

            for tid, t in state.get("teams", {}).items():
                start = t.get("start_time", now)
                end = t.get("end_time") or now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec

                cur_stage = t.get("current_stage", 1)
                stage_title = STAGES.get(cur_stage, {}).get("title", f"Stage {cur_stage}")
                last_seen = t.get("last_seen", start)
                last_seen_sec_ago = max(0, int(now - last_seen))

                leaderboard.append({
                    "team_id": tid,
                    "team_name": t.get("team_name", tid),
                    "password": t.get("password", ""),
                    "members": t.get("members", ""),
                    "current_stage": cur_stage,
                    "stage_title": stage_title,
                    "last_action": t.get("last_action", "Initialized Station"),
                    "last_seen_sec_ago": last_seen_sec_ago,
                    "is_online": last_seen_sec_ago < 75,
                    "is_finished": t.get("is_finished", False),
                    "tamper_incidents": t.get("tamper_incidents", 0),
                    "is_locked": t.get("is_locked", False),
                    "activity_log": t.get("activity_log", [])[-15:],
                    "raw_time_sec": raw_time_sec,
                    "adjusted_time_sec": adjusted_sec,
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0),
                    "unlocked_stages": t.get("unlocked_stages", [1])
                })

            # Sort hierarchy:
            # 1. Finished teams first
            # 2. Higher stage
            # 3. Lowest adjusted time
            # 4. Fewest hints
            # 5. Zero traps
            leaderboard.sort(key=lambda x: (
                -1 if x["is_finished"] else 0,
                -x["current_stage"],
                x["adjusted_time_sec"],
                x["hints_count"],
                x["traps_count"]
            ))

            self._send_json(200, {
                "leaderboard": leaderboard,
                "broadcasts": state.get("broadcasts", []),
                "server_time": now
            })
            return

        if path == "/api/teams/state":
            team_id = params.get("team_id", [""])[0]
            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return
            state = load_game_state()
            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": "Team not found"})
                return
            self._send_json(200, {
                "team": team,
                "broadcasts": state.get("broadcasts", [])
            })
            return

        # Serve static files
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        try:
            content_len = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_len).decode("utf-8")
            data = json.loads(body) if body else {}
        except Exception as e:
            self._send_json(400, {"error": f"Invalid JSON payload: {str(e)}"})
            return

        state = load_game_state()

        if path == "/api/teams/login":
            team_id = data.get("team_id", "").strip().upper()
            password = data.get("password", "").strip()

            if not team_id or not password:
                self._send_json(400, {"error": "Team ID and Password are required"})
                return

            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": f"Team ID '{team_id}' not found. Please register first."})
                return

            if team.get("password") and team.get("password") != password:
                self._send_json(401, {"error": "Invalid team password. Please check your credentials."})
                return

            team["last_seen"] = time.time()
            team["last_action"] = "Logged in to Workstation"
            save_game_state(state)

            self._send_json(200, {
                "message": "Login successful",
                "team": team,
                "broadcasts": state.get("broadcasts", [])
            })
            return

        if path == "/api/teams/register":
            team_name = data.get("team_name", "").strip()
            team_id = data.get("team_id", "").strip().upper()
            password = data.get("password", "").strip()
            members = data.get("members", "").strip()

            if not team_name or not team_id or not password:
                self._send_json(400, {"error": "Team Name, Team ID, and Password are required"})
                return

            if team_id in state.get("teams", {}):
                existing = state["teams"][team_id]
                if existing.get("password") and existing.get("password") != password:
                    self._send_json(409, {"error": f"Team ID '{team_id}' already registered with a different password."})
                    return
                existing["last_seen"] = time.time()
                existing["last_action"] = "Re-authenticated station"
                save_game_state(state)
                self._send_json(200, {
                    "message": "Existing team logged in successfully",
                    "team": existing
                })
                return

            now = time.time()
            state["teams"][team_id] = {
                "team_id": team_id,
                "team_name": team_name,
                "password": password,
                "members": members,
                "current_stage": 1,
                "unlocked_stages": [1],
                "hints_count": 0,
                "traps_count": 0,
                "tamper_incidents": 0,
                "is_locked": False,
                "remote_unlock": False,
                "last_action": "Registered station",
                "last_seen": now,
                "activity_log": [{
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": 1,
                    "action": "Registered workstation"
                }],
                "hints_history": [],
                "start_time": now,
                "end_time": None,
                "is_finished": False,
                "created_at": datetime.now().isoformat()
            }
            save_game_state(state)

            self._send_json(200, {
                "message": "Team registered successfully",
                "team": state["teams"][team_id]
            })
            return

        if path == "/api/teams/activity":
            team_id = data.get("team_id", "").strip().upper()
            action = data.get("action", "").strip()
            current_stage = data.get("current_stage")
            tamper_incidents = data.get("tamper_incidents")
            is_locked = data.get("is_locked")

            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return

            if "teams" not in state:
                state["teams"] = {}
            team = state["teams"].get(team_id)
            if not team:
                # Auto-initialize team record if station registered offline or dynamically
                team = {
                    "team_id": team_id,
                    "team_name": data.get("team_name") or f"Team {team_id}",
                    "registered_at": time.time(),
                    "current_stage": int(current_stage) if current_stage is not None else 1,
                    "tamper_incidents": int(tamper_incidents) if tamper_incidents is not None else 0,
                    "is_locked": bool(is_locked) if is_locked is not None else False,
                    "last_seen": time.time(),
                    "last_action": action or "Station online",
                    "activity_log": []
                }
                state["teams"][team_id] = team

            now = time.time()
            team["last_seen"] = now

            if action:
                team["last_action"] = action
                if "activity_log" not in team:
                    team["activity_log"] = []
                team["activity_log"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": current_stage or team.get("current_stage", 1),
                    "action": action
                })
                if len(team["activity_log"]) > 40:
                    team["activity_log"] = team["activity_log"][-40:]

            if current_stage is not None:
                team["current_stage"] = max(team.get("current_stage", 1), int(current_stage))

            if tamper_incidents is not None:
                team["tamper_incidents"] = int(tamper_incidents)

            if is_locked is not None:
                team["is_locked"] = bool(is_locked)

            remote_unlocked = team.get("remote_unlock", False)
            if remote_unlocked:
                team["remote_unlock"] = False
                team["is_locked"] = False

            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "remote_unlock": remote_unlocked,
                "current_stage": team.get("current_stage", 1),
                "broadcasts": state.get("broadcasts", [])
            })
            return

        if path == "/api/admin/remote-unlock":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": "Team not found"})
                return

            team["remote_unlock"] = True
            team["is_locked"] = False
            team["last_action"] = "Remotely Unlocked by Organizer"
            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": team.get("current_stage", 1),
                "action": "Organizer Override PIN applied remotely"
            })
            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "message": f"Workstation for {team_id} successfully unlocked remotely"
            })
            return

        if path == "/api/stage/unlock":
            team_id = data.get("team_id", "").strip().upper()
            stage_num = int(data.get("stage", 1))
            password_input = data.get("password", "").strip().upper()

            if team_id not in state["teams"]:
                self._send_json(404, {"error": "Team not registered"})
                return

            team = state["teams"][team_id]
            stage_info = STAGES.get(stage_num)
            if not stage_info:
                self._send_json(400, {"error": f"Invalid stage {stage_num}"})
                return

            clean_input = "".join(c for c in password_input if c.isalnum())
            matched = False

            for k in stage_info["keys"]:
                clean_k = "".join(c for c in k.upper() if c.isalnum())
                if clean_input == clean_k or password_input == k.upper():
                    matched = True
                    break

            if matched:
                next_stage = stage_info.get("next_stage")
                if next_stage == "COMPLETE":
                    team["is_finished"] = True
                    team["end_time"] = time.time()
                elif isinstance(next_stage, int):
                    if next_stage not in team["unlocked_stages"]:
                        team["unlocked_stages"].append(next_stage)
                    team["current_stage"] = max(team["current_stage"], next_stage)

                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"ACCESS GRANTED TO STAGE {next_stage}",
                    "next_stage": next_stage,
                    "team": team
                })
            else:
                self._send_json(200, {
                    "success": False,
                    "message": "ACCESS DENIED: Invalid Decryption Key. System remains locked."
                })
            return

        if path == "/api/hints/request":
            team_id = data.get("team_id", "").strip().upper()
            stage_num = int(data.get("stage", 1))

            if team_id not in state["teams"]:
                self._send_json(404, {"error": "Team not registered"})
                return

            team = state["teams"][team_id]
            stage_info = STAGES.get(stage_num)
            if not stage_info:
                self._send_json(400, {"error": "Invalid stage"})
                return

            hints_for_stage = [h for h in team.get("hints_history", []) if h["stage"] == stage_num]
            hint_level = len(hints_for_stage) + 1

            if hint_level > len(stage_info["hints"]):
                self._send_json(200, {
                    "success": False,
                    "message": "No additional hints available for this stage.",
                    "penalty_added": 0
                })
                return

            hint_text = stage_info["hints"][hint_level - 1]
            team["hints_count"] += 1
            team["hints_history"].append({
                "stage": stage_num,
                "level": hint_level,
                "hint": hint_text,
                "timestamp": time.time()
            })
            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "hint_level": hint_level,
                "hint": hint_text,
                "penalty_added": 2,
                "total_hints": team["hints_count"]
            })
            return

        if path == "/api/trap/trigger":
            team_id = data.get("team_id", "").strip().upper()
            if team_id not in state["teams"]:
                self._send_json(404, {"error": "Team not registered"})
                return

            team = state["teams"][team_id]
            team["traps_count"] += 1
            save_game_state(state)

            self._send_json(200, {
                "trapped": True,
                "message": "AI OVERRIDE COMPROMISED: You submitted your credentials to ADI! System trapped in reset loop.",
                "penalty_added": 5,
                "total_traps": team["traps_count"]
            })
            return

        if path == "/api/admin/broadcast":
            pin = data.get("pin", "")
            msg = data.get("message", "").strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return
            if msg:
                state.setdefault("broadcasts", []).append({
                    "id": len(state.get("broadcasts", [])) + 1,
                    "message": msg,
                    "timestamp": time.time()
                })
                save_game_state(state)
            self._send_json(200, {"success": True, "broadcasts": state["broadcasts"]})
            return

        self._send_json(404, {"error": "Endpoint not found"})

def run_server():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    load_game_state()

    import socket
    lan_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lan_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass

    server_address = ("", PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, FailsafeHandler)

    print("=" * 65)
    print("      PROJECT FAILSAFE: AI ESCAPE ROOM SERVER ONLINE")
    print("=" * 65)
    print(f"[*] Local Station URL  : http://localhost:{PORT}")
    print(f"[*] LAN Network URL    : http://{lan_ip}:{PORT}")
    print(f"[*] Organizer Console  : http://localhost:{PORT}/admin.html")
    print(f"[*] Organizer Admin PIN: {ADMIN_PIN}")
    print(f"[*] Serving Assets from: {PUBLIC_DIR}")
    print("=" * 65)
    print("Press Ctrl+C to terminate the server.\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down PROJECT FAILSAFE server...")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run_server()
