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

# Master Stage Passwords & Solutions (16 Curated Storyline Stages: 11 Original + 5 from Document)
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
        "next_stage": 12,
        "hints": [
            "The failsafe is encoded in IEEE Women in Engineering's three founding core values.",
            "Count the letters of each core value: Wisdom (6), Integrity (9), Empowerment (11). Enter '6-9-11'."
        ]
    },
    12: {
        "title": "The Whiteout Signature",
        "keys": ["CLEARANCE_ALPHA", "CLEARANCE ALPHA", "CLEARANCEALPHA"],
        "next_stage": 13,
        "hints": [
            "Some messages are not meant to be read; they are meant to be highlighted.",
            "Select all text in Emergency_Log.doc (Ctrl+A) to expose the #FFFFFF font: CLEARANCE_ALPHA."
        ]
    },
    13: {
        "title": "The ROT-4 IEEE Shift",
        "keys": ["ADITIS13", "ADITI-13", "ADITI 13"],
        "next_stage": 14,
        "hints": [
            "Shift every letter backward by the number of letters in the acronym 'IEEE' (4).",
            "EHMXMW13 shifted backward by 4 letters yields ADITIS13."
        ]
    },
    14: {
        "title": "The Atbash Cipher Mirror",
        "keys": ["PROJECT"],
        "next_stage": 15,
        "hints": [
            "Dr. Aditi mirrored her alphabet in times of crisis: A <-> Z, B <-> Y.",
            "KILQVBG reversed across the alphabet maps to PROJECT."
        ]
    },
    15: {
        "title": "The Polybius Coordinate Trail",
        "keys": ["VECTOR"],
        "next_stage": 16,
        "hints": [
            "Map each pair in the 5x5 grid using (Row, Column) order.",
            "(5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R -> VECTOR."
        ]
    },
    16: {
        "title": "The Find-and-Replace Frequency Count",
        "keys": ["1400", "1,400"],
        "next_stage": "COMPLETE",
        "hints": [
            "Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
            "Ctrl+F shows 14 matches. 14 x 100 = 1400."
        ]
    }
}

# ROUND 2: StratCom Decryption Arena (15 Progressive Forensic Challenges from Master Document)
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
        "title": "The Modulated Polybius Cipher",
        "location": "Matrix_Coordinates.pdf",
        "keys": ["CIPHER"],
        "next_stage": 5,
        "hints": ["Odd coordinates: Row - 1; Even coordinates: Column - 1. Decodes to CIPHER."]
    },
    5: {
        "title": "The QWERTY Shape Trace",
        "location": "Keyboard_Telemetry.pdf",
        "keys": ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        "next_stage": 6,
        "hints": ["Connecting key clusters across the mechanical switchboard forms three geometric squares."]
    },
    6: {
        "title": "The Interlocking Logic Gate Flow",
        "location": "Logic_Gate_Matrix.pdf",
        "keys": ["011", "0,1,1", "0-1-1"],
        "next_stage": 7,
        "hints": ["Trace binary inputs through AND, OR, and XOR gates. Final terminal bus reads 011."]
    },
    7: {
        "title": "The Mirror Image String Inversion",
        "location": "Reflection_Buffer.txt",
        "keys": ["CLEARANCE"],
        "next_stage": 8,
        "hints": ["Reflect the inverted vertical glyphs along the horizontal axis to reconstruct 'CLEARANCE'."]
    },
    8: {
        "title": "The Rotational Matrix Operator",
        "location": "Vector_Grid.pdf",
        "keys": ["SE", "SOUTH EAST", "SOUTHEAST"],
        "next_stage": 9,
        "hints": ["The center cell dictates +45 degree rotation. Bottom row terminates pointing SE."]
    },
    9: {
        "title": "The Base-Invariant Digital Root Flow",
        "location": "Cryptographic_Nodes.txt",
        "keys": ["NONE", "IMPOSSIBLE", "NO PRIME", "0"],
        "next_stage": 10,
        "hints": ["A number with a digital root of 9 is divisible by 9, therefore no such 3-digit prime exists (NONE)."]
    },
    10: {
        "title": "The Palindrome Filter Stream",
        "location": "Spectral_Filter.log",
        "keys": ["RLRCK"],
        "next_stage": 11,
        "hints": ["Discard SOLO (non-palindrome). Initial letters of valid palindromes spell: RLRCK."]
    },
    11: {
        "title": "The Diagonal Word Weave",
        "location": "Grid_Weave.txt",
        "keys": ["NODC"],
        "next_stage": 12,
        "hints": ["Read along the main diagonal from top-left (1,1) to bottom-right (4,4): N-O-D-C."]
    },
    12: {
        "title": "The Perimeter Geometry Box Count",
        "location": "Perimeter_Grid.pdf",
        "keys": ["102", "102 BOXES"],
        "next_stage": 13,
        "hints": ["Sum the 12 outer perimeter structural boundary nodes: 102."]
    },
    13: {
        "title": "The Alternating Checker Pattern",
        "location": "Checker_State.pdf",
        "keys": ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        "next_stage": 14,
        "hints": ["Step 6 alternates to 3 empty boxes: 3-EMPTY."]
    },
    14: {
        "title": "The Shifted Ring Cipher",
        "location": "Wheel_Decryption.png",
        "keys": ["FINALS", "EBF"],
        "next_stage": 15,
        "hints": ["Clock jumps modulo 12 convert to alphabet letters: FINALS."]
    },
    15: {
        "title": "The Cipher Wheel Protocol (THE RED QUESTION)",
        "location": "Wheel_Overlay.pdf",
        "keys": ["ECLIPSE"],
        "next_stage": "COMPLETE",
        "hints": ["Align the inner wheel over the outer wheel at 135 degrees clockwise. Exposed cutouts spell: ECLIPSE."]
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
        if "round_1_started" not in CACHED_STATE:
            CACHED_STATE["round_1_started"] = False
        if "round_1_start_time" not in CACHED_STATE:
            CACHED_STATE["round_1_start_time"] = None
        if "round_2_started" not in CACHED_STATE:
            CACHED_STATE["round_2_started"] = False
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

def tournament_team_sort_key(t):
    """
    Tournament ranking logic:
    'who takes the least time to complete the entire round1 and round2 wins'
    - Tier 0: Finished entire tournament (both Round 1 and Round 2) -> Sorted strictly by least adjusted_time_sec (least time wins!)
    - Tier 1: In Round 2 (actively solving 15 puzzles) -> Sorted by highest round_2_stage (descending), then least adjusted_time_sec
    - Tier 2: Finished Round 1 (cleared all 16 stages) -> Sorted by least adjusted_time_sec
    - Tier 3: Active in Round 1 -> Sorted by highest current_stage (descending), then least adjusted_time_sec
    Tie-breakers: fewest hints, fewest traps.
    """
    is_r2_fin = bool(t.get("round_2_is_finished"))
    cur_rnd = int(t.get("current_round", 1) or 1)
    is_r2_unlocked = bool(t.get("round_2_unlocked")) or bool(t.get("send_to_round_2"))
    r2_stage = int(t.get("round_2_stage", 1) or 1)
    is_r1_fin = bool(t.get("is_finished")) or (int(t.get("current_stage", 1) or 1) >= 16)
    r1_stage = int(t.get("current_stage", 1) or 1)
    adj_time = float(t.get("adjusted_time_sec", 0) or 0)
    hints = int(t.get("hints_count", 0) or 0)
    traps = int(t.get("traps_count", 0) or 0)

    if is_r2_fin:
        return (0, 0, adj_time, hints, traps)
    if cur_rnd >= 2 or is_r2_unlocked:
        return (1, -r2_stage, adj_time, hints, traps)
    if is_r1_fin:
        return (2, 0, adj_time, hints, traps)
    return (3, -r1_stage, adj_time, hints, traps)


class FailsafeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def log_message(self, format, *args):
        client_ip = self.client_address[0] if self.client_address else "unknown"
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {client_ip} - {format % args}")

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
                if t.get("round_2_is_finished"):
                    end = t.get("round_2_end_time") or t.get("end_time") or now
                elif int(t.get("current_round", 1) or 1) >= 2 or t.get("round_2_unlocked") or t.get("send_to_round_2"):
                    end = now
                elif t.get("is_finished") or int(t.get("current_stage", 1) or 1) >= 16:
                    end = t.get("end_time") or now
                else:
                    end = now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                computed_traps = max(t.get("traps_count", 0), int(t.get("penalty_seconds", 0) // 300))
                trap_penalty_sec = max(computed_traps * 300, t.get("penalty_seconds", 0))
                time_adj_sec = t.get("time_adjustment_sec", 0)
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec + time_adj_sec

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
                    "time_adjustment_sec": time_adj_sec,
                    "adjusted_time_sec": adjusted_sec,
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": computed_traps,
                    "unlocked_stages": t.get("unlocked_stages", [1]),
                    "stage_times": t.get("stage_times", {}),
                    "client_info": t.get("client_info", {}),
                    "active_view": t.get("active_view", ""),
                    "violations_history": t.get("violations_history", []),
                    "current_round": t.get("current_round", 1),
                    "round_2_stage": t.get("round_2_stage", 1),
                    "round_2_unlocked": t.get("round_2_unlocked", False) or t.get("current_round", 1) >= 2,
                    "send_to_round_2": t.get("send_to_round_2", False),
                    "round_2_is_finished": t.get("round_2_is_finished", False),
                    "round_2_finish_time_str": t.get("round_2_finish_time_str", ""),
                    "prize_code": t.get("prize_code", ""),
                    "prize_title": t.get("prize_title", ""),
                    "podium_rank": t.get("podium_rank", 0)
                })

            # Sort by tournament victory hierarchy: least time to complete Round 1 & Round 2 wins
            leaderboard.sort(key=tournament_team_sort_key)

            self._send_json(200, {
                "leaderboard": leaderboard,
                "broadcasts": state.get("broadcasts", []),
                "server_time": now,
                "round_1_started": bool(state.get("round_1_started", False)),
                "round_1_start_time": state.get("round_1_start_time"),
                "round_2_started": bool(state.get("round_2_started", False)),
                "shortlist": state.get("shortlist", {})
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
                if t.get("round_2_is_finished"):
                    end = t.get("round_2_end_time") or t.get("end_time") or now
                elif int(t.get("current_round", 1) or 1) >= 2 or t.get("round_2_unlocked") or t.get("send_to_round_2"):
                    end = now
                elif t.get("is_finished") or int(t.get("current_stage", 1) or 1) >= 16:
                    end = t.get("end_time") or now
                else:
                    end = now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                time_adj_sec = t.get("time_adjustment_sec", 0)
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec + time_adj_sec

                cur_stage = t.get("current_stage", 1)
                stage_title = STAGES.get(cur_stage, {}).get("title", f"Stage {cur_stage}")
                last_seen = t.get("last_seen") or start or now
                last_seen_sec_ago = max(0, int(now - last_seen))

                leaderboard.append({
                    "team_id": tid,
                    "team_name": t.get("team_name", tid),
                    "members": t.get("members", ""),
                    "current_round": t.get("current_round", 1),
                    "current_stage": cur_stage,
                    "stage_title": stage_title,
                    "is_finished": t.get("is_finished", False),
                    "round_2_unlocked": bool(t.get("round_2_unlocked") or t.get("send_to_round_2") or int(t.get("current_round", 1) or 1) >= 2),
                    "round_2_stage": t.get("round_2_stage", 1),
                    "round_2_is_finished": bool(t.get("round_2_is_finished")),
                    "round_2_finish_time_str": t.get("round_2_finish_time_str", ""),
                    "raw_time_sec": raw_time_sec,
                    "adjusted_time_sec": adjusted_sec,
                    "finish_time_str": t.get("finish_time_str", ""),
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0)
                })

            leaderboard.sort(key=tournament_team_sort_key)

            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            qualified_ids = shortlist_meta.get("round_2_qualified_team_ids", [])

            # Auto-populate top 12 if not yet locked or fewer than 12
            if (not qualified_ids or (not shortlist_meta.get("locked", False) and len(qualified_ids) < 12)) and leaderboard:
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

            test_mode = bool(state.get("test_mode_unlock_all", False) or team.get("unlock_all_levels", False))
            r1_completed = bool(team.get("is_finished", False) or int(team.get("current_stage", 1)) >= 16)
            is_promoted = bool(team.get("round_2_unlocked", False) or int(team.get("current_round", 1)) >= 2 or team.get("send_to_round_2", False))
            round_2_unlocked = bool(test_mode or is_promoted or (current_round >= 2 and is_qualified and r1_completed))

            self._send_json(200, {
                "team_id": team_id,
                "current_round": max(current_round, team.get("current_round", 1)),
                "is_qualified_for_round_2": is_qualified or test_mode or is_promoted,
                "round_2_unlocked": round_2_unlocked,
                "send_to_round_2": is_promoted,
                "test_mode_unlock_all": test_mode,
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
                "remote_reset_r2": team.get("remote_reset_r2", False),
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
                "broadcasts": state.get("broadcasts", []),
                "round_1_started": bool(state.get("round_1_started", False)),
                "round_1_start_time": state.get("round_1_start_time"),
                "round_2_started": bool(state.get("round_2_started", False))
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
                    "team": existing,
                    "round_1_started": bool(state.get("round_1_started", False)),
                    "round_1_start_time": state.get("round_1_start_time"),
                    "round_2_started": bool(state.get("round_2_started", False))
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
                "team": state["teams"][team_id],
                "round_1_started": bool(state.get("round_1_started", False)),
                "round_1_start_time": state.get("round_1_start_time"),
                "round_2_started": bool(state.get("round_2_started", False))
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
                    "last_action": f"🏆 MISSION COMPLETE: TARA Liberated in {elapsed_str} // Workstation Terminated",
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
                    team["round_2_stage"] = 15
                    team["round_2_end_time"] = now
                    team["end_time"] = now
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
                    team["last_action"] = f"🏆 MISSION COMPLETE: TARA Liberated in {elapsed_str} // Workstation Terminated"
                team["last_seen"] = now

            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": 15,
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

        if path == "/api/teams/request_fullscreen_exit":
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

            if "teams" not in state:
                state["teams"] = {}

            now = time.time()
            is_approve = (action == "approve")

            if team_id == "ALL":
                state["global_fullscreen_exit_allowed"] = is_approve
                for tid, t in state.get("teams", {}).items():
                    t["fullscreen_exit_requested"] = False
                    t["fullscreen_exit_approved"] = is_approve
                    t["fullscreen_exit_approved_until"] = (now + 86400) if is_approve else 0
                    if is_approve:
                        t["is_locked"] = False
                        t["remote_unlock"] = True
                        t["tamper_incidents"] = 0
                        t["violations_history"] = []
                    t["last_action"] = "Organizer APPROVED Fullscreen Exit (All Teams)" if is_approve else "Organizer ENFORCED Fullscreen (All Teams)"
                    if "activity_log" not in t:
                        t["activity_log"] = []
                    t["activity_log"].append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": t.get("current_stage", 1),
                        "action": "Organizer APPROVED Fullscreen Exit (All Teams)" if is_approve else "Organizer ENFORCED Fullscreen (All Teams)"
                    })
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": "Fullscreen exit " + ("approved and all stations unlocked" if is_approve else "denied") + " for ALL teams",
                    "global_fullscreen_exit_allowed": is_approve
                })
                return

            if team_id not in state["teams"]:
                self._send_json(404, {"error": f"Team '{team_id}' not found"})
                return

            team = state["teams"][team_id]
            if is_approve:
                team["fullscreen_exit_requested"] = False
                team["fullscreen_exit_approved"] = True
                team["fullscreen_exit_approved_until"] = now + 86400 # 24 hour window
                team["is_locked"] = False
                team["remote_unlock"] = True
                team["tamper_incidents"] = 0
                team["violations_history"] = []
                team["last_action"] = "Organizer APPROVED Fullscreen Exit & Unlocked Workstation"
                if "activity_log" not in team:
                    team["activity_log"] = []
                team["activity_log"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": team.get("current_stage", 1),
                    "action": "Organizer APPROVED Fullscreen Exit (Workstation Unlocked)"
                })
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Fullscreen exit approved and workstation unlocked for {team_id}"
                })
                return
            else:
                team["fullscreen_exit_requested"] = False
                team["fullscreen_exit_approved"] = False
                team["fullscreen_exit_approved_until"] = 0
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
            self._send_json(200, {
                "success": True,
                "pending": pending,
                "global_fullscreen_exit_allowed": bool(state.get("global_fullscreen_exit_allowed", False))
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

            now_ts = time.time()
            global_fs_allowed = bool(state.get("global_fullscreen_exit_allowed", False))
            fs_approved = bool(global_fs_allowed or (team.get("fullscreen_exit_approved", False) and (team.get("fullscreen_exit_approved_until", 0) > now_ts)))

            remote_unlocked = team.get("remote_unlock", False)
            if remote_unlocked or fs_approved:
                team["remote_unlock"] = False
                team["is_locked"] = False
                team["tamper_incidents"] = 0
                team["violations_history"] = []
            else:
                if tamper_incidents is not None:
                    team["tamper_incidents"] = int(tamper_incidents)
                if is_locked is not None:
                    team["is_locked"] = bool(is_locked)

            traps_from_client = data.get("traps_count")
            if traps_from_client is not None:
                team["traps_count"] = max(team.get("traps_count", 0), int(traps_from_client))

            pen_from_client = data.get("penalty_seconds")
            if pen_from_client is not None:
                team["penalty_seconds"] = max(team.get("penalty_seconds", 0), int(pen_from_client))

            if is_finished is not None and bool(is_finished):
                team["is_finished"] = True
                if finish_time_str:
                    team["finish_time_str"] = finish_time_str
                if not team.get("end_time"):
                    team["end_time"] = now

            remote_reset = team.get("remote_reset", False)
            if remote_reset and int(current_stage or 1) == 1:
                team["remote_reset"] = False

            remote_reset_r2 = team.get("remote_reset_r2", False)
            if remote_reset_r2 and int(team.get("round_2_stage", 1)) == 1:
                team["remote_reset_r2"] = False

            force_logout = team.get("force_logout", False)

            save_game_state(state)
            r2_started = bool(state.get("round_2_started", False) or state.get("current_round", 1) == 2)
            shortlist_meta = state.get("shortlist", {})
            if isinstance(shortlist_meta, dict):
                shortlist_ids = shortlist_meta.get("round_2_qualified_team_ids", [])
            elif isinstance(shortlist_meta, list):
                shortlist_ids = shortlist_meta
            else:
                shortlist_ids = []
            is_short = bool(team_id in shortlist_ids)

            unlock_all = bool(state.get("test_mode_unlock_all", False) or team.get("unlock_all_levels", False))
            lock_all = bool(team.get("lock_all_levels", False))
            if lock_all:
                team["lock_all_levels"] = False

            self._send_json(200, {
                "success": True,
                "remote_unlock": remote_unlocked,
                "remote_reset": remote_reset,
                "remote_reset_r2": remote_reset_r2,
                "force_logout": force_logout,
                "fullscreen_exit_requested": team.get("fullscreen_exit_requested", False),
                "fullscreen_exit_approved": fs_approved,
                "global_fullscreen_exit_allowed": global_fs_allowed,
                "round_1_started": bool(state.get("round_1_started", False)),
                "round_1_start_time": state.get("round_1_start_time"),
                "round_2_started": r2_started or bool(team.get("round_2_unlocked", False)),
                "is_shortlisted": is_short or bool(team.get("round_2_unlocked", False)),
                "round_2_ready": bool((r2_started and is_short) or team.get("round_2_unlocked", False) or team.get("send_to_round_2", False) or int(team.get("current_round", 1)) >= 2 or unlock_all),
                "send_to_round_2": bool(team.get("send_to_round_2", False) or team.get("round_2_unlocked", False) or int(team.get("current_round", 1)) >= 2),
                "current_stage": team.get("current_stage", 1),
                "unlock_all_levels": unlock_all,
                "lock_all_levels": lock_all,
                "test_mode_unlock_all": bool(state.get("test_mode_unlock_all", False)),
                "traps_count": team.get("traps_count", 0),
                "penalty_seconds": team.get("penalty_seconds", 0),
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
                    t["tamper_incidents"] = 0
                    t["violations_history"] = []
                    t["fullscreen_exit_approved"] = True
                    t["fullscreen_exit_approved_until"] = time.time() + 86400
                    t["last_action"] = "Remotely Unlocked by Organizer (ALL)"
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": t.get("current_stage", 1),
                        "action": "Organizer Remote Unlock & Breach Reset applied to ALL stations"
                    })
                    count += 1
                save_game_state(state)
                self._send_json(200, {
                    "success": True,
                    "message": f"Global unlock transmitted: All {count} workstations unlocked and breaches reset."
                })
                return

            team = state.get("teams", {}).get(team_id)
            if not team:
                self._send_json(404, {"error": "Team not found"})
                return

            team["remote_unlock"] = True
            team["is_locked"] = False
            team["tamper_incidents"] = 0
            team["violations_history"] = []
            team["fullscreen_exit_approved"] = True
            team["fullscreen_exit_approved_until"] = time.time() + 86400
            team["last_action"] = "Remotely Unlocked by Organizer"
            if "activity_log" not in team:
                team["activity_log"] = []
            team["activity_log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": team.get("current_stage", 1),
                "action": "Organizer Override PIN applied remotely (Breaches cleared)"
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

        if path in ["/api/admin/remote-reset", "/api/admin/round/reset", "/api/admin/round-reset"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()
            try:
                round_num = int(data.get("round", 1))
            except Exception:
                round_num = 1

            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            now = time.time()
            if round_num == 2:
                # ==================== RESET ROUND 2 ====================
                if team_id == "ALL":
                    count = 0
                    for tid, t in state.get("teams", {}).items():
                        t["round_2_stage"] = 1
                        t["round_2_unlocked_stages"] = [1]
                        t["round_2_start_time"] = now
                        t["round_2_is_finished"] = False
                        t["round_2_times"] = {}
                        t["round_2_stage_times"] = {}
                        t["round_2_score"] = 0
                        t["round_2_finish_time_str"] = ""
                        t["prize_code"] = ""
                        t["podium_rank"] = None
                        t["remote_reset_r2"] = True
                        t["last_action"] = "Round 2 Reset by Organizer (ALL)"
                        t.setdefault("activity_log", []).append({
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "stage": 1,
                            "action": "Round 2 reset to Puzzle 01 by Organizer (ALL)"
                        })
                        count += 1
                    state["round_2_started"] = False
                    state["round_2_active"] = False
                    shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
                    shortlist_meta["locked"] = False
                    bcast_msg = "🔄 TOURNAMENT ALERT: ROUND 2 HAS BEEN RESET BY THE ORGANIZER. StratCom Arena re-initialized."
                    state.setdefault("broadcasts", []).append({
                        "id": len(state.get("broadcasts", [])) + 1,
                        "message": bcast_msg,
                        "time": datetime.now().strftime("%H:%M:%S")
                    })
                    save_game_state(state, immediate=True)
                    self._send_json(200, {
                        "success": True,
                        "round": 2,
                        "team_id": "ALL",
                        "affected_count": count,
                        "message": f"Global Round 2 reset executed: All {count} workstations reset to Round 2 Puzzle 01. Arena re-initialized."
                    })
                    return

                team = state.get("teams", {}).get(team_id)
                if not team:
                    self._send_json(404, {"error": f"Team '{team_id}' not found"})
                    return

                team["round_2_stage"] = 1
                team["round_2_unlocked_stages"] = [1]
                team["round_2_start_time"] = now
                team["round_2_is_finished"] = False
                team["round_2_times"] = {}
                team["round_2_stage_times"] = {}
                team["round_2_score"] = 0
                team["round_2_finish_time_str"] = ""
                team["prize_code"] = ""
                team["podium_rank"] = None
                team["remote_reset_r2"] = True
                team["last_action"] = f"Round 2 Reset by Organizer ({datetime.now().strftime('%H:%M:%S')})"
                team.setdefault("activity_log", []).append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": 1,
                    "action": "Round 2 reset to Puzzle 01 by Organizer"
                })
                save_game_state(state, immediate=True)
                self._send_json(200, {
                    "success": True,
                    "round": 2,
                    "team_id": team_id,
                    "message": f"Round 2 for team '{team_id}' successfully reset to Puzzle 01."
                })
                return

            else:
                # ==================== RESET ROUND 1 ====================
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
                        t["finish_time_str"] = ""
                        t["remote_reset"] = True
                        t["force_logout"] = False
                        t["remote_override_stage"] = 1
                        t["current_round"] = 1
                        t["last_action"] = "Round 1 Reset by Organizer (ALL)"
                        t.setdefault("activity_log", []).append({
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "stage": 1,
                            "action": "Round 1 reset to Stage 1 by Organizer (ALL)"
                        })
                        count += 1
                    state["current_round"] = 1
                    bcast_msg = "🔄 TOURNAMENT ALERT: ROUND 1 HAS BEEN RESET BY THE ORGANIZER. All stations returned to Stage 01."
                    state.setdefault("broadcasts", []).append({
                        "id": len(state.get("broadcasts", [])) + 1,
                        "message": bcast_msg,
                        "time": datetime.now().strftime("%H:%M:%S")
                    })
                    save_game_state(state, immediate=True)
                    self._send_json(200, {
                        "success": True,
                        "round": 1,
                        "team_id": "ALL",
                        "affected_count": count,
                        "message": f"Global Round 1 reset executed: All {count} workstations reset to Stage 01."
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
                team["finish_time_str"] = ""
                team["remote_reset"] = True
                team["force_logout"] = False
                team["remote_override_stage"] = 1
                team["current_round"] = 1
                team["last_action"] = f"Round 1 Reset by Organizer ({datetime.now().strftime('%H:%M:%S')})"
                team.setdefault("activity_log", []).append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": 1,
                    "action": "Round 1 reset to Stage 1 by Organizer"
                })
                save_game_state(state, immediate=True)
                self._send_json(200, {
                    "success": True,
                    "round": 1,
                    "team_id": team_id,
                    "message": f"Round 1 for team '{team_id}' successfully reset to Stage 01."
                })
                return

        if path == "/api/admin/levels/unlock_all":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            team_id = data.get("team_id", "ALL").strip().upper()
            state["test_mode_unlock_all"] = True
            count = 0
            now = time.time()
            if team_id == "ALL":
                for tid, t in state.get("teams", {}).items():
                    t["unlock_all_levels"] = True
                    t["lock_all_levels"] = False
                    t["test_mode_unlocked"] = True
                    t["current_stage"] = 16
                    t["unlocked_stages"] = list(range(1, 17))
                    t["stages_cleared"] = list(range(1, 17))
                    t["current_round"] = 2
                    t["round_2_unlocked"] = True
                    t["round_2_stage"] = 15
                    t["round2_stages_cleared"] = list(range(1, 16))
                    t["remote_override_stage"] = 16
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": 16,
                        "action": "All levels unlocked for organizer testing"
                    })
                    count += 1
            else:
                t = state.get("teams", {}).get(team_id)
                if t:
                    t["unlock_all_levels"] = True
                    t["lock_all_levels"] = False
                    t["test_mode_unlocked"] = True
                    t["current_stage"] = 16
                    t["unlocked_stages"] = list(range(1, 17))
                    t["stages_cleared"] = list(range(1, 17))
                    t["current_round"] = 2
                    t["round_2_unlocked"] = True
                    t["round_2_stage"] = 15
                    t["round2_stages_cleared"] = list(range(1, 16))
                    count = 1

            state.setdefault("broadcasts", []).append({
                "id": len(state.get("broadcasts", [])) + 1,
                "message": "🛠️ TEST MODE: Organizer unlocked all levels (Stages 01–16 & Round 2 Arena).",
                "time": datetime.now().strftime("%H:%M:%S"),
                "timestamp": now
            })
            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "test_mode_unlock_all": True,
                "affected_count": count,
                "message": f"Organizer Test Mode: All levels unlocked across {count} workstations."
            })
            return

        if path == "/api/admin/levels/lock_all":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            team_id = data.get("team_id", "ALL").strip().upper()
            state["test_mode_unlock_all"] = False
            count = 0
            now = time.time()
            if team_id == "ALL":
                for tid, t in state.get("teams", {}).items():
                    t["unlock_all_levels"] = False
                    t["lock_all_levels"] = True
                    t["test_mode_unlocked"] = False
                    t["current_stage"] = 1
                    t["unlocked_stages"] = [1]
                    t["stages_cleared"] = []
                    t["current_round"] = 1
                    t["round_2_unlocked"] = False
                    t["round_2_stage"] = 1
                    t["round2_stages_cleared"] = []
                    t["remote_override_stage"] = 1
                    t["remote_reset"] = True
                    t["remote_reset_r2"] = True
                    t.setdefault("activity_log", []).append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "stage": 1,
                        "action": "All levels locked by organizer - restored to Stage 01"
                    })
                    count += 1
            else:
                t = state.get("teams", {}).get(team_id)
                if t:
                    t["unlock_all_levels"] = False
                    t["lock_all_levels"] = True
                    t["test_mode_unlocked"] = False
                    t["current_stage"] = 1
                    t["unlocked_stages"] = [1]
                    t["stages_cleared"] = []
                    t["current_round"] = 1
                    t["round_2_unlocked"] = False
                    t["round_2_stage"] = 1
                    t["round2_stages_cleared"] = []
                    t["remote_override_stage"] = 1
                    t["remote_reset"] = True
                    t["remote_reset_r2"] = True
                    count = 1

            state.setdefault("broadcasts", []).append({
                "id": len(state.get("broadcasts", [])) + 1,
                "message": "🔒 TEST MODE DEACTIVATED: All levels locked by Organizer. Stations reset to Stage 01.",
                "time": datetime.now().strftime("%H:%M:%S"),
                "timestamp": now
            })
            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "test_mode_unlock_all": False,
                "affected_count": count,
                "message": f"Organizer Test Mode Deactivated: All levels locked, stations reset to Stage 01."
            })
            return

        if path in ["/api/admin/broadcast/clear", "/api/admin/broadcast/reset"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return
            state["broadcasts"] = []
            save_game_state(state, immediate=True)
            self._send_json(200, {"success": True, "message": "All broadcasts cleared successfully."})
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
                team["current_stage"] = max(1, min(16, int(data["current_stage"])))
                team["remote_override_stage"] = team["current_stage"]
            if "round_2_stage" in data:
                team["round_2_stage"] = max(1, min(15, int(data["round_2_stage"])))
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

        if path in ["/api/admin/teams/purge-all", "/api/admin/teams/delete-all", "/api/admin/teams/clear-all"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            purged_count = len(state.get("teams", {}))
            state["teams"] = {}

            # Reset shortlist
            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            shortlist_meta["round_2_qualified_team_ids"] = []
            shortlist_meta["locked"] = False
            state["round_2_active"] = False

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": f"Global purge executed: All {purged_count} teams permanently removed from tournament database.",
                "purged_count": purged_count,
                "remaining_teams_count": 0
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
                if t.get("round_2_is_finished"):
                    end = t.get("round_2_end_time") or t.get("end_time") or now
                elif int(t.get("current_round", 1) or 1) >= 2 or t.get("round_2_unlocked") or t.get("send_to_round_2"):
                    end = now
                elif t.get("is_finished") or int(t.get("current_stage", 1) or 1) >= 16:
                    end = t.get("end_time") or now
                else:
                    end = now
                raw_time_sec = max(0, int(end - start))
                hints_penalty_sec = t.get("hints_count", 0) * 120
                trap_penalty_sec = t.get("traps_count", 0) * 300
                time_adj_sec = t.get("time_adjustment_sec", 0)
                adjusted_sec = raw_time_sec + hints_penalty_sec + trap_penalty_sec + time_adj_sec
                cur_stage = t.get("current_stage", 1)

                leaderboard.append({
                    "team_id": tid,
                    "current_round": t.get("current_round", 1),
                    "current_stage": cur_stage,
                    "is_finished": t.get("is_finished", False),
                    "round_2_unlocked": bool(t.get("round_2_unlocked") or t.get("send_to_round_2") or int(t.get("current_round", 1) or 1) >= 2),
                    "round_2_stage": t.get("round_2_stage", 1),
                    "round_2_is_finished": bool(t.get("round_2_is_finished")),
                    "adjusted_time_sec": adjusted_sec,
                    "hints_count": t.get("hints_count", 0),
                    "traps_count": t.get("traps_count", 0)
                })

            leaderboard.sort(key=tournament_team_sort_key)

            top_12 = [t["team_id"] for t in leaderboard[:12]]
            state.setdefault("shortlist", {})["round_2_qualified_team_ids"] = top_12
            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": f"Shortlist reset to automated top {len(top_12)} teams",
                "qualified_count": len(top_12),
                "qualified_team_ids": top_12
            })
        if path in ["/api/admin/start_round_1", "/api/admin/open_round_1", "/api/admin/round_1/start"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            now = time.time()
            state["round_1_started"] = True
            state["round_1_start_time"] = now
            state["current_round"] = 1

            # Synchronize start_time for all registered teams
            for tid, t in state.get("teams", {}).items():
                if not t.get("is_finished") and int(t.get("current_stage", 1)) <= 1:
                    t["start_time"] = now
                    t["last_action"] = "🚀 Round 1 Officially Launched by Organizer"

            # Global broadcast alert
            bcast_msg = "🚀 TOURNAMENT ALERT: ROUND 1 IS OFFICIALLY OPEN! All workstations unlocked simultaneously. Good luck, agents!"
            state.setdefault("broadcasts", []).append({
                "id": len(state.get("broadcasts", [])) + 1,
                "message": bcast_msg,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": "Round 1 opened successfully for all teams",
                "round_1_started": True,
                "round_1_start_time": state["round_1_start_time"]
            })
            return

        if path in ["/api/admin/pause_round_1", "/api/admin/hold_round_1", "/api/admin/round_1/pause"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            state["round_1_started"] = False

            # Global broadcast alert
            bcast_msg = "⏸️ TOURNAMENT NOTICE: Round 1 placed on standby by Organizer. All workstations returned to waiting lobby."
            state.setdefault("broadcasts", []).append({
                "id": len(state.get("broadcasts", [])) + 1,
                "message": bcast_msg,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            save_game_state(state, immediate=True)
            self._send_json(200, {
                "success": True,
                "message": "Round 1 held in standby lobby",
                "round_1_started": False
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
            state["round_2_started"] = True
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

        if path in ["/api/admin/send_to_round_2", "/api/admin/send-to-round-2", "/api/admin/advance_to_round_2"]:
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            if pin != ADMIN_PIN:
                self._send_json(403, {"error": "Invalid Admin PIN"})
                return

            target_team_id = data.get("team_id", "").strip().upper()
            shortlist_meta = state.setdefault("shortlist", {"round_2_qualified_team_ids": [], "locked": False})
            q_list = shortlist_meta.setdefault("round_2_qualified_team_ids", [])
            now = time.time()
            promoted_teams = []

            if target_team_id in ["ALL_FINISHED", "FINISHED", "ALL"]:
                for tid, t in state.get("teams", {}).items():
                    is_r1_done = (target_team_id == "ALL") or bool(t.get("is_finished", False) or int(t.get("current_stage", 1)) >= 16)
                    if is_r1_done:
                        t["current_round"] = 2
                        t["round_2_unlocked"] = True
                        t["send_to_round_2"] = True
                        if not t.get("round_2_stage"):
                            t["round_2_stage"] = 1
                        if not t.get("round_2_unlocked_stages"):
                            t["round_2_unlocked_stages"] = [1]
                        if not t.get("round_2_start_time"):
                            t["round_2_start_time"] = now
                        t["round_2_is_finished"] = False
                        t["last_action"] = "🚀 Sent to Round 2 by Organizer"
                        t.setdefault("activity_log", []).append({
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "stage": t.get("current_stage", 16),
                            "action": "Organizer sent station to Round 2: StratCom Decryption Arena"
                        })
                        if tid not in q_list:
                            q_list.append(tid)
                        promoted_teams.append(tid)

                state["round_2_started"] = True
                bcast_msg = f"🚀 TOURNAMENT ALERT: Organizer has promoted {len(promoted_teams)} qualified squads to Round 2: StratCom Decryption Arena!"
                state.setdefault("broadcasts", []).append({
                    "id": len(state.get("broadcasts", [])) + 1,
                    "message": bcast_msg,
                    "time": datetime.now().strftime("%H:%M:%S")
                })
                save_game_state(state, immediate=True)
                self._send_json(200, {
                    "success": True,
                    "count": len(promoted_teams),
                    "promoted_teams": promoted_teams,
                    "message": f"Successfully promoted {len(promoted_teams)} stations to Round 2!"
                })
                return
            else:
                if not target_team_id:
                    self._send_json(400, {"error": "Missing team_id"})
                    return
                t = state.get("teams", {}).get(target_team_id)
                if not t:
                    for tid, team_obj in state.get("teams", {}).items():
                        if tid.upper() == target_team_id:
                            t = team_obj
                            target_team_id = tid
                            break
                if not t:
                    t = {
                        "team_id": target_team_id,
                        "team_name": f"Team {target_team_id}",
                        "password": "",
                        "members": "",
                        "current_stage": 16,
                        "is_finished": True,
                        "hints_count": 0,
                        "traps_count": 0,
                        "tamper_incidents": 0,
                        "is_locked": False,
                        "start_time": now,
                        "last_seen": now,
                        "last_action": "Registered by Organizer"
                    }
                    state.setdefault("teams", {})[target_team_id] = t
                t["current_round"] = 2
                t["round_2_unlocked"] = True
                t["send_to_round_2"] = True
                if not t.get("round_2_stage"):
                    t["round_2_stage"] = 1
                if not t.get("round_2_unlocked_stages"):
                    t["round_2_unlocked_stages"] = [1]
                if not t.get("round_2_start_time"):
                    t["round_2_start_time"] = now
                t["round_2_is_finished"] = False
                t["last_action"] = "🚀 Sent to Round 2 by Organizer"
                t.setdefault("activity_log", []).append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "stage": t.get("current_stage", 16),
                    "action": "Organizer sent station to Round 2: StratCom Decryption Arena"
                })
                if target_team_id not in q_list:
                    q_list.append(target_team_id)
                state["round_2_started"] = True
                bcast_msg = f"🚀 TOURNAMENT ALERT: Squad [{t.get('team_name', target_team_id)}] has been promoted to Round 2 by the Organizer!"
                state.setdefault("broadcasts", []).append({
                    "id": len(state.get("broadcasts", [])) + 1,
                    "message": bcast_msg,
                    "time": datetime.now().strftime("%H:%M:%S")
                })
                save_game_state(state, immediate=True)
                self._send_json(200, {
                    "success": True,
                    "team_id": target_team_id,
                    "message": f"Squad [{target_team_id}] successfully promoted to Round 2!"
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
                        team["last_action"] = "🏆 ROUND 2 COMPLETE: Solved all 15 forensic challenges!"
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

            if round_num == 2:
                self._send_json(200, {
                    "success": False,
                    "message": "🔒 PROTOCOL RESTRICTION: Clues and hint transmissions are strictly disabled in Round 2.",
                    "penalty_added": 0
                })
                return

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
            if not team_id:
                self._send_json(400, {"error": "Missing team_id"})
                return

            if "teams" not in state:
                state["teams"] = {}

            team = state["teams"].get(team_id)
            if not team:
                for tid, t in state["teams"].items():
                    if tid.upper() == team_id:
                        team = t
                        team_id = tid
                        break

            if not team:
                now_t = time.time()
                team = {
                    "team_id": team_id,
                    "team_name": f"Team {team_id}",
                    "password": "",
                    "members": "",
                    "current_stage": 1,
                    "traps_count": 0,
                    "hints_count": 0,
                    "tamper_incidents": 0,
                    "is_locked": False,
                    "start_time": now_t,
                    "last_seen": now_t,
                    "last_action": "DO_NOT_RUN Honeypot Trap Triggered"
                }
                state["teams"][team_id] = team

            team["traps_count"] = team.get("traps_count", 0) + 1
            team["penalty_seconds"] = max(team.get("penalty_seconds", 0), team["traps_count"] * 300)
            team["last_action"] = f"🚨 DO_NOT_RUN Honeypot Executed (+5m Penalty, Trap #{team['traps_count']})"
            team.setdefault("activity_log", []).append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "stage": team.get("current_stage", 1),
                "action": f"🚨 DO_NOT_RUN Honeypot Trap Triggered (+5m penalty applied, total traps: {team['traps_count']})"
            })
            save_game_state(state)

            self._send_json(200, {
                "trapped": True,
                "message": "AI OVERRIDE COMPROMISED: You submitted your credentials to ISHAAN! System trapped in reset loop.",
                "penalty_added": 5,
                "total_traps": team["traps_count"],
                "penalty_seconds": team["penalty_seconds"]
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

