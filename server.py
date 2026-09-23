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
import threading
from datetime import datetime

PORT = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8000))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "game_state.json")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ADMIN_PIN = "wie-admin-2026"

# Master Stage Passwords & Solutions (Curated 11 Storyline Stages)
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
}

# ROUND 2: StratCom Decryption Arena (9 Progressive Forensic Challenges)
ROUND2_STAGES = {
    1: {
        "title": "The Matrix Box Transformation",
        "location": "Visual_Matrix.pdf",
        "keys": ["C", "THREE CIRCLES", "3 CIRCLES", "THREECIRCLES", "●●●"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "penalty_points": 20,
        "hints": [
            "Look at the rule across rows: Row 1 = Triangles, Row 2 = Squares, Row 3 = Circles.",
            "Rule across columns: Col 1 has 1 shape, Col 2 has 2 shapes, Col 3 has 3 shapes. Row 3, Column 3 must have 3 Circles (Option C)."
        ]
    },
    2: {
        "title": "The Spatial Net Folding Box",
        "location": "Cube_Net_Terminal.pdf",
        "keys": ["5"],
        "next_stage": 3,
        "penalty_points": 15,
        "hints": [
            "In a standard T-shaped cube net, faces separated by exactly one box along a straight line fold into opposite faces.",
            "In the vertical line 1, 3, 5, 6: Box 1 and Box 5 are separated by Box 3 -> Face 1 is opposite Face 5."
        ]
    },
    3: {
        "title": "The Clockwise Rotation Boxes",
        "location": "Rotation_Array.pdf",
        "keys": ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT"],
        "next_stage": 4,
        "hints": [
            "Trace the movement of the core node as it shifts 90 degrees clockwise.",
            "Box 1: Top-Left -> Box 2: Top-Right -> Box 3: Bottom-Right -> Box 4: Bottom-Left (BL)."
        ]
    },
    4: {
        "title": "The Whiteout Signature",
        "location": "Emergency_Log.doc",
        "keys": ["CLEARANCE_ALPHA", "CLEARANCE ALPHA", "CLEARANCEALPHA"],
        "next_stage": 5,
        "hints": [
            "Some messages are not meant to be read; they are meant to be highlighted.",
            "Select all text (Ctrl+A) or toggle the UV filter to reveal: DECRYPTION KEY IS CLEARANCE_ALPHA."
        ]
    },
    5: {
        "title": "The ROT-4 IEEE Shift",
        "location": "Encrypted_Beacon.txt",
        "keys": ["ADITIS13", "ADITI-13", "ADITI 13"],
        "next_stage": 6,
        "hints": [
            "Shift every letter backward by the number of letters in the acronym 'IEEE' (4).",
            "EHMXMW13 shifted backward by 4 letters: E->A, H->D, M->I, X->T, M->I, W->S + 13 = ADITIS13."
        ]
    },
    6: {
        "title": "The Polybius Coordinate Trail",
        "location": "Matrix_Coordinates.pdf",
        "keys": ["VECTOR"],
        "next_stage": 7,
        "hints": [
            "Map each pair in the 5x5 grid using (Row, Column) order.",
            "(5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R -> VECTOR."
        ]
    },
    7: {
        "title": "The Atbash Cipher Mirror",
        "location": "Mirror_Log.txt",
        "keys": ["PROJECT"],
        "next_stage": 8,
        "hints": [
            "Reverse the alphabet so A <-> Z, B <-> Y, C <-> X.",
            "KILQVBG mirrored: K->P, I->R, L->O, Q->J, V->E, B->Y, G->T -> PROJECT."
        ]
    },
    8: {
        "title": "The Find-and-Replace Frequency Count",
        "location": "Mass_System_Log.txt",
        "keys": ["1400", "1,400"],
        "next_stage": 9,
        "hints": [
            "Count how many times the exact term 'OVERRIDE' appears in the log, then multiply that count by 100.",
            "Searching for OVERRIDE finds 14 matches. 14 x 100 = 1400."
        ]
    },
    9: {
        "title": "The Cipher Wheel Layer Shift",
        "location": "Wheel_Overlay.pdf",
        "keys": ["ECLIPSE"],
        "next_stage": "COMPLETE",
        "hints": [
            "Align the inner wheel over the outer wheel at 135 degrees clockwise.",
            "The exposed cutouts align over the letters: E-C-L-I-P-S-E."
        ]
    }
}

import copy

STATE_LOCK = threading.Lock()
CACHED_STATE = None
STATE_DIRTY = False
DISK_LOCK = threading.Lock()

def save_game_state_to_disk(state):
    with DISK_LOCK:
        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
        except Exception:
            pass

def background_flusher():
    global STATE_DIRTY
    while True:
        time.sleep(1.0)
        to_save = None
        if STATE_DIRTY:
            with STATE_LOCK:
                if STATE_DIRTY and CACHED_STATE is not None:
                    STATE_DIRTY = False
                    to_save = copy.deepcopy(CACHED_STATE)
        if to_save:
            save_game_state_to_disk(to_save)

# Launch background flusher thread
_flusher_thread = threading.Thread(target=background_flusher, daemon=True)
_flusher_thread.start()

def load_game_state():
    global CACHED_STATE
    with STATE_LOCK:
        if CACHED_STATE is not None:
            return CACHED_STATE
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(DATA_FILE):
            CACHED_STATE = {
                "teams": {},
                "broadcasts": [],
                "current_round": 1,
                "shortlist": {
                    "round_2_qualified_team_ids": [],
                    "locked": False
                },
                "created_at": datetime.now().isoformat()
            }
            save_game_state_to_disk(CACHED_STATE)
            return CACHED_STATE
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                CACHED_STATE = json.load(f)
        except Exception as e:
            print(f"Error loading data file: {e}, resetting...")
            CACHED_STATE = {
                "teams": {},
                "broadcasts": [],
                "current_round": 1,
                "shortlist": {"round_2_qualified_team_ids": [], "locked": False},
                "created_at": datetime.now().isoformat()
            }
        if "current_round" not in CACHED_STATE:
            CACHED_STATE["current_round"] = 1
        if "shortlist" not in CACHED_STATE:
            CACHED_STATE["shortlist"] = {"round_2_qualified_team_ids": [], "locked": False}
        return CACHED_STATE

def save_game_state(state, immediate=False):
    global CACHED_STATE, STATE_DIRTY
    with STATE_LOCK:
        CACHED_STATE = state
        STATE_DIRTY = True
    if immediate:
        save_game_state_to_disk(state)

class FailsafeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def log_message(self, format, *args):
        # Silent logger for high-throughput 100-station telemetry
        pass

    def _send_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path in ["/api/status", "/api/server-info"]:
            import socket
            lan_ip = "127.0.0.1"
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                lan_ip = s.getsockname()[0]
                s.close()
            except Exception:
                pass
            state = load_game_state()
            self._send_json(200, {
                "status": "online",
                "system": "PROJECT FAILSAFE SERVER",
                "lan_ip": lan_ip,
                "port": PORT,
                "server_url": f"http://{lan_ip}:{PORT}",
                "total_teams": len(state.get("teams", {})),
                "server_time": time.time()
            })
            return

        if path in ["/admin", "/admin.html"]:
            admin_file = os.path.join(ROOT_DIR, "admin.html")
            if os.path.exists(admin_file):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                with open(admin_file, "rb") as f:
                    self.wfile.write(f.read())
                return

        if path in ["/", "/index.html", "/aditi_os_widget.html"]:
            target_file = os.path.join(ROOT_DIR, "aditi_os_widget.html")
            if os.path.exists(target_file):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                with open(target_file, "rb") as f:
                    self.wfile.write(f.read())
                return

        if path in ["/v2", "/v2/", "/project-failsafe-2.0", "/project-failsafe-2.0/"]:
            v2_file = os.path.join(ROOT_DIR, "project-failsafe-2.0", "index.html")
            if os.path.exists(v2_file):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                with open(v2_file, "rb") as f:
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
                start = t.get("start_time") or now
                end = t.get("end_time") or now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec

                cur_stage = t.get("current_stage", 1)
                stage_title = STAGES.get(cur_stage, {}).get("title", f"Stage {cur_stage}")
                last_seen = t.get("last_seen") or start or now
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
                    "force_logout": t.get("force_logout", False),
                    "remote_reset": t.get("remote_reset", False),
                    "activity_log": t.get("activity_log", [])[-20:],
                    "raw_time_sec": raw_time_sec,
                    "adjusted_time_sec": adjusted_sec,
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0),
                    "unlocked_stages": t.get("unlocked_stages", [1]),
                    "stage_times": t.get("stage_times", {}),
                    "client_info": t.get("client_info", {}),
                    "active_view": t.get("active_view", ""),
                    "violations_history": t.get("violations_history", []),
                    "current_round": t.get("current_round", 1),
                    "round_2_stage": t.get("round_2_stage", 1),
                    "round_2_is_finished": t.get("round_2_is_finished", False),
                    "round_2_finish_time_str": t.get("round_2_finish_time_str", ""),
                    "prize_code": t.get("prize_code", ""),
                    "prize_title": t.get("prize_title", ""),
                    "podium_rank": t.get("podium_rank", 0)
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

        if path == "/api/admin/shortlist":
            pin = params.get("pin", [""])[0]
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            state = load_game_state()
            now = time.time()
            leaderboard = []

            for tid, t in state.get("teams", {}).items():
                start = t.get("start_time") or now
                end = t.get("end_time") or now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec

                cur_stage = t.get("current_stage", 1)
                stage_title = STAGES.get(cur_stage, {}).get("title", f"Stage {cur_stage}")
                last_seen = t.get("last_seen") or start or now
                last_seen_sec_ago = max(0, int(now - last_seen))

                leaderboard.append({
                    "team_id": tid,
                    "team_name": t.get("team_name", tid),
                    "members": t.get("members", ""),
                    "current_stage": cur_stage,
                    "stage_title": stage_title,
                    "is_finished": t.get("is_finished", False),
                    "raw_time_sec": raw_time_sec,
                    "adjusted_time_sec": adjusted_sec,
                    "finish_time_str": t.get("finish_time_str", ""),
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0)
                })

            leaderboard.sort(key=lambda x: (
                -1 if x["is_finished"] else 0,
                -x["current_stage"],
                x["adjusted_time_sec"],
                x["hints_count"],
                x["traps_count"]
            ))

            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            qualified_ids = shortlist_meta.get("round_2_qualified_team_ids", [])

            # Auto-populate top 12 if not yet initialized
            if not qualified_ids and leaderboard:
                qualified_ids = [t["team_id"] for t in leaderboard[:12]]
                shortlist_meta["round_2_qualified_team_ids"] = qualified_ids
                save_game_state(state)

            ranked_teams = []
            for i, t in enumerate(leaderboard):
                tid = t["team_id"]
                ranked_teams.append({
                    **t,
                    "rank": i + 1,
                    "is_qualified": tid in qualified_ids,
                    "auto_top_12": i < 12
                })

            self._send_json(200, {
                "current_round": state.get("current_round", 1),
                "locked": shortlist_meta.get("locked", False),
                "qualified_team_ids": qualified_ids,
                "qualified_count": len(qualified_ids),
                "target_count": 12,
                "ranked_teams": ranked_teams,
                "total_teams": len(ranked_teams),
                "server_time": now
            })
            return

        if path == "/api/team/round_status":
            team_id = params.get("team_id", [""])[0].strip().upper()
            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return
            state = load_game_state()
            team = state.get("teams", {}).get(team_id, {})
            shortlist_meta = state.get("shortlist", {})
            qualified_ids = shortlist_meta.get("round_2_qualified_team_ids", [])
            is_qualified = team_id in qualified_ids
            current_round = state.get("current_round", 1)

            self._send_json(200, {
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
            team["force_logout"] = False
            team["remote_reset"] = False
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
                existing["force_logout"] = False
                existing["remote_reset"] = False
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
                "force_logout": False,
                "remote_reset": False,
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

        if path == "/api/teams/logout":
            team_id = data.get("team_id", "").strip().upper()
            if team_id and team_id in state.get("teams", {}):
                team = state["teams"][team_id]
                team["last_action"] = "Logged out from Workstation"
                team["force_logout"] = False
                if "activity_log" not in team:
                    team["activity_log"] = []
                team["activity_log"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": team.get("current_stage", 1),
                    "action": "Operator voluntarily logged out"
                })
                save_game_state(state)
            self._send_json(200, {"success": True, "message": "Logged out successfully"})
            return

        if path == "/api/teams/finish":
            team_id = data.get("team_id", "").strip().upper()
            elapsed_seconds = data.get("elapsed_seconds", 0)
            elapsed_str = data.get("elapsed_str", "")
            team_name = data.get("team_name", "").strip()
            members = data.get("members", "").strip()
            password = data.get("password", "").strip()
            round_num = int(data.get("round", 1))
            stage_times = data.get("stage_times", {})

            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return

            if "teams" not in state:
                state["teams"] = {}

            now = time.time()
            team = state["teams"].get(team_id)
            if not team:
                team = {
                    "team_id": team_id,
                    "team_name": team_name or f"Team {team_id}",
                    "password": password,
                    "members": members,
                    "registered_at": now - (float(elapsed_seconds) if elapsed_seconds else 0),
                    "start_time": now - (float(elapsed_seconds) if elapsed_seconds else 0),
                    "end_time": now,
                    "current_stage": 15,
                    "unlocked_stages": list(range(1, 16)),
                    "hints_count": 0,
                    "traps_count": 0,
                    "tamper_incidents": 0,
                    "is_locked": False,
                    "force_logout": False,
                    "remote_reset": False,
                    "last_seen": now,
                    "is_finished": True,
                    "finish_time_str": elapsed_str,
                    "stage_times": stage_times,
                    "last_action": f"🏆 MISSION COMPLETE: ETHAN Liberated in {elapsed_str} // Workstation Terminated",
                    "activity_log": []
                }
                state["teams"][team_id] = team
            else:
                if team_name:
                    team["team_name"] = team_name
                if members:
                    team["members"] = members
                if password:
                    team["password"] = password

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
                else:
                    if stage_times:
                        team["stage_times"] = stage_times
                    team["is_finished"] = True
                    team["current_stage"] = 15
                    team["end_time"] = now
                    team["finish_time_str"] = elapsed_str
                    team["last_action"] = f"🏆 MISSION COMPLETE: ETHAN Liberated in {elapsed_str} // Workstation Terminated"
                team["last_seen"] = now

            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": 9 if round_num == 2 else 15,
                "action": f"🏆 VICTORY (Round {round_num}): Solved in {elapsed_str}!"
            })

            # Broadcast announcement
            tname = team.get("team_name") or team_id
            bcast_msg = f"🏆 ROUND {round_num} COMPLETED: Team {tname} [{team_id}] finished in {elapsed_str}!"
            if "broadcasts" not in state:
                state["broadcasts"] = []
            state["broadcasts"].append({
                "id": len(state["broadcasts"]) + 1,
                "message": bcast_msg,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            save_game_state(state)
            self._send_json(200, {
                "success": True,
                "message": "Mission completion recorded successfully",
                "prize_code": team.get("prize_code", ""),
                "prize_title": team.get("prize_title", ""),
                "podium_rank": team.get("podium_rank", 0),
                "team": team
            })
            return

        if path == "/api/teams/activity":
            team_id = data.get("team_id", "").strip().upper()
            action = data.get("action", "").strip()
            current_stage = data.get("current_stage")
            tamper_incidents = data.get("tamper_incidents")
            is_locked = data.get("is_locked")
            team_name = data.get("team_name", "").strip()
            members = data.get("members", "").strip()
            password = data.get("password", "").strip()
            is_finished = data.get("is_finished")
            finish_time_str = data.get("finish_time_str", "")
            stage_times = data.get("stage_times")

            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return

            if "teams" not in state:
                state["teams"] = {}
            team = state["teams"].get(team_id)
            now = time.time()
            if not team:
                # Auto-initialize complete team record on dynamic connect
                team = {
                    "team_id": team_id,
                    "team_name": team_name or f"Team {team_id}",
                    "password": password,
                    "members": members,
                    "registered_at": now,
                    "start_time": now,
                    "end_time": None,
                    "current_stage": int(current_stage) if current_stage is not None else 1,
                    "unlocked_stages": [1],
                    "hints_count": 0,
                    "traps_count": 0,
                    "tamper_incidents": int(tamper_incidents) if tamper_incidents is not None else 0,
                    "is_locked": bool(is_locked) if is_locked is not None else False,
                    "force_logout": False,
                    "remote_reset": False,
                    "last_seen": now,
                    "last_action": action or "Station connected",
                    "stage_times": stage_times or {},
                    "activity_log": [{
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": current_stage or 1,
                        "action": action or "Station connected"
                    }]
                }
                state["teams"][team_id] = team
            else:
                # Update metadata if missing or newly provided
                if team_name and (not team.get("team_name") or team.get("team_name") == f"Team {team_id}"):
                    team["team_name"] = team_name
                if members and not team.get("members"):
                    team["members"] = members
                if password and not team.get("password"):
                    team["password"] = password
                if stage_times:
                    team["stage_times"] = stage_times

            team["last_seen"] = now

            if "client_info" in data and data["client_info"]:
                team["client_info"] = data["client_info"]
            if "active_view" in data and data["active_view"]:
                team["active_view"] = data["active_view"]
            if "violations_history" in data and data["violations_history"]:
                team["violations_history"] = data["violations_history"]

            if "client_info" in data and data["client_info"]:
                team["client_info"] = data["client_info"]
            if "active_view" in data and data["active_view"]:
                team["active_view"] = data["active_view"]
            if "violations_history" in data and data["violations_history"]:
                team["violations_history"] = data["violations_history"]

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

            remote_reset = team.get("remote_reset", False)
            if remote_reset:
                if current_stage is not None and int(current_stage) == 1:
                    team["remote_reset"] = False
                    team["current_stage"] = 1
            elif current_stage is not None:
                team["current_stage"] = max(team.get("current_stage", 1), int(current_stage))

            if tamper_incidents is not None:
                team["tamper_incidents"] = int(tamper_incidents)

            if is_locked is not None:
                team["is_locked"] = bool(is_locked)

            if is_finished is not None and bool(is_finished):
                team["is_finished"] = True
                if finish_time_str:
                    team["finish_time_str"] = finish_time_str
                if not team.get("end_time"):
                    team["end_time"] = now

            remote_unlocked = team.get("remote_unlock", False)
            if remote_unlocked:
                team["remote_unlock"] = False
                team["is_locked"] = False

            remote_reset = team.get("remote_reset", False)
            if remote_reset and int(current_stage or 1) == 1:
                team["remote_reset"] = False

            force_logout = team.get("force_logout", False)

            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "remote_unlock": remote_unlocked,
                "remote_reset": remote_reset,
                "force_logout": force_logout,
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

            if team_id == "ALL":
                count = 0
                for tid, t in state.get("teams", {}).items():
                    t["remote_unlock"] = True
                    t["is_locked"] = False
                    t["last_action"] = "Remotely Unlocked by Organizer (ALL)"
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": t.get("current_stage", 1),
                        "action": "Organizer Remote Unlock applied to ALL stations"
                    })
                    count += 1
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Global unlock transmitted: All {count} workstations unlocked."
                })
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

        if path == "/api/admin/remote-logout":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            if team_id == "ALL":
                count = 0
                for tid, t in state.get("teams", {}).items():
                    t["force_logout"] = True
                    t["last_action"] = "Remotely Logged Out by Organizer (ALL)"
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": t.get("current_stage", 1),
                        "action": "Organizer Remote Logout broadcasted to ALL stations"
                    })
                    count += 1
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Global logout transmitted: All {count} workstations logged out."
                })
                return

            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            team["force_logout"] = True
            team["last_action"] = "Remotely Logged Out by Organizer"
            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": team.get("current_stage", 1),
                "action": "Organizer Remote Logout triggered"
            })
            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "message": f"Workstation for {team_id} successfully logged out remotely"
            })
            return

        if path == "/api/admin/remote-reset":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            now = time.time()
            if team_id == "ALL":
                count = 0
                for tid, t in state.get("teams", {}).items():
                    t["current_stage"] = 1
                    t["unlocked_stages"] = [1]
                    t["hints_count"] = 0
                    t["hints_history"] = []
                    t["traps_count"] = 0
                    t["tamper_incidents"] = 0
                    t["is_locked"] = False
                    t["is_finished"] = False
                    t["start_time"] = now
                    t["end_time"] = None
                    t["remote_reset"] = True
                    t["force_logout"] = False
                    t["last_action"] = "Workstation Remotely Reset by Organizer (ALL)"
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": 1,
                        "action": "Station completely reset to Stage 1 by Organizer (ALL)"
                    })
                    count += 1
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Global reset transmitted: All {count} workstations reset to Stage 01."
                })
                return

            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            team["current_stage"] = 1
            team["unlocked_stages"] = [1]
            team["hints_count"] = 0
            team["hints_history"] = []
            team["traps_count"] = 0
            team["tamper_incidents"] = 0
            team["is_locked"] = False
            team["is_finished"] = False
            team["start_time"] = now
            team["end_time"] = None
            team["remote_reset"] = True
            team["force_logout"] = False
            team["last_action"] = "Workstation Remotely Reset by Organizer"
            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": 1,
                "action": "Station completely reset to Stage 1 by Organizer"
            })
            save_game_state(state)

            self._send_json(200, {
                "success": True,
                "message": f"Workstation for {team_id} successfully reset to Stage 01"
            })
            return

        
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

        if path == "/api/admin/shortlist/toggle":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()
            qualified = data.get("qualified")

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return

            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            q_list = shortlist_meta.setdefault("round_2_qualified_team_ids", [])

            if qualified is None:
                if team_id in q_list:
                    q_list.remove(team_id)
                else:
                    q_list.append(team_id)
            elif qualified:
                if team_id not in q_list:
                    q_list.append(team_id)
            else:
                if team_id in q_list:
                    q_list.remove(team_id)

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "team_id": team_id,
                "is_qualified": team_id in q_list,
                "qualified_count": len(q_list),
                "qualified_team_ids": q_list
            })
            return

        if path == "/api/admin/shortlist/reset":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            now = time.time()
            leaderboard = []
            for tid, t in state.get("teams", {}).items():
                start = t.get("start_time") or now
                end = t.get("end_time") or now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec
                cur_stage = t.get("current_stage", 1)

                leaderboard.append({
                    "team_id": tid,
                    "current_stage": cur_stage,
                    "is_finished": t.get("is_finished", False),
                    "adjusted_time_sec": adjusted_sec,
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0)
                })

            leaderboard.sort(key=lambda x: (
                -1 if x["is_finished"] else 0,
                -x["current_stage"],
                x["adjusted_time_sec"],
                x["hints_count"],
                x["traps_count"]
            ))

            top_12 = [t["team_id"] for t in leaderboard[:12]]
            state.setdefault("shortlist", {})["round_2_qualified_team_ids"] = top_12
            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": f"Shortlist reset to automated top {len(top_12)} teams",
                "qualified_count": len(top_12),
                "qualified_team_ids": top_12
            })
            return

        if path == "/api/admin/start_round_2":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            q_list = shortlist_meta.get("round_2_qualified_team_ids", [])
            state["current_round"] = 2
            shortlist_meta["locked"] = True

            now = time.time()
            for tid in q_list:
                if tid in state.get("teams", {}):
                    t = state["teams"][tid]
                    t["round_2_stage"] = 1
                    t["round_2_unlocked_stages"] = [1]
                    t["round_2_start_time"] = now
                    t["round_2_is_finished"] = False
                    t["round_2_times"] = {}
                    t["round_2_score"] = 0
                    t["last_action"] = "🚀 Round 2 Initialized: StratCom Decryption Arena Unlocked"

            # Global broadcast
            bcast_msg = f"🚀 TOURNAMENT ALERT: ROUND 2 HAS OFFICIALLY BEGUN! {len(q_list)} QUALIFIED STATIONS UNLOCKED."
            state.setdefault("broadcasts", []).append({
                "id": len(state.get("broadcasts", [])) + 1,
                "message": bcast_msg,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": f"Round 2 started with {len(q_list)} qualified teams",
                "current_round": 2,
                "qualified_count": len(q_list)
            })
            return

        if path == "/api/stage/unlock":
            team_id = data.get("team_id", "").strip().upper()
            stage_num = int(data.get("stage", 1))
            round_num = int(data.get("round", 1))
            password_input = data.get("password", "").strip().upper()

            if team_id not in state["teams"]:
                self._send_json(404, {"error": "Team not registered"})
                return

            team = state["teams"][team_id]
            stage_dict = ROUND2_STAGES if round_num == 2 else STAGES
            stage_info = stage_dict.get(stage_num)
            if not stage_info:
                self._send_json(400, {"error": f"Invalid stage {stage_num} in round {round_num}"})
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
                if round_num == 2:
                    team.setdefault("round_2_unlocked_stages", [1])
                    if next_stage == "COMPLETE":
                        team["round_2_is_finished"] = True
                        team["round_2_end_time"] = time.time()
                        team["last_action"] = "🏆 ROUND 2 COMPLETE: Solved all 9 forensic challenges!"
                    elif isinstance(next_stage, int):
                        if next_stage not in team["round_2_unlocked_stages"]:
                            team["round_2_unlocked_stages"].append(next_stage)
                        team["round_2_stage"] = max(team.get("round_2_stage", 1), next_stage)
                        team["last_action"] = f"Round 2 - Stage {stage_num} Solved -> Advanced to Stage {next_stage}"
                else:
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
            round_num = int(data.get("round", 1))

            if team_id not in state["teams"]:
                self._send_json(404, {"error": "Team not registered"})
                return

            team = state["teams"][team_id]
            stage_dict = ROUND2_STAGES if round_num == 2 else STAGES
            stage_info = stage_dict.get(stage_num)
            if not stage_info:
                self._send_json(400, {"error": f"Invalid stage {stage_num} in round {round_num}"})
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

run = run_server

if __name__ == "__main__":
    run_server()

