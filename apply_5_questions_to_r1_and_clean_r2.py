# apply_5_questions_to_r1_and_clean_r2.py
import re
import json

print("=== 1. UPDATING server.py ===")
with open("server.py", "r", encoding="utf-8") as f:
    srv = f.read()

# STAGES update (16 stages for Round 1)
# Stage 11 next_stage becomes 12, and 12-16 added from doc
r1_stages_def = '''# Master Stage Passwords & Solutions (16 Curated Storyline Stages: 11 Original + 5 from Document)
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
        "next_stage": None,
        "hints": [
            "Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
            "Ctrl+F shows 14 matches. 14 x 100 = 1400."
        ]
    }
}'''

# Replace STAGES in server.py
srv = re.sub(r"# Master Stage Passwords & Solutions.*?STAGES = \{.*?\n\}", r1_stages_def, srv, flags=re.DOTALL)

# ROUND 2 STAGES (15 Progressive Challenges from Document, ending with ECLIPSE)
r2_stages_def = '''# ROUND 2: StratCom Decryption Arena (15 Progressive Forensic Challenges from Master Document)
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
}'''

srv = re.sub(r"# ROUND 2: StratCom Decryption Arena.*?ROUND2_STAGES = \{.*?\n\}", r2_stages_def, srv, flags=re.DOTALL)

# In /api/hints/request, strictly enforce NO CLUES in Round 2
hint_check = '''        if path == "/api/hints/request":
            team_id = data.get("team_id", "").strip().upper()
            stage_num = int(data.get("stage", 1))
            round_num = int(data.get("round", 1))

            if round_num == 2:
                self._send_json(200, {
                    "success": False,
                    "message": "🔒 PROTOCOL RESTRICTION: Clues and hint transmissions are strictly disabled in Round 2.",
                    "penalty_added": 0
                })
                return'''

srv = re.sub(r'if path == "/api/hints/request":.*?if team_id not in state\["teams"\]:', hint_check + '\n\n            if team_id not in state["teams"]:', srv, flags=re.DOTALL)

# Update round 1 finish stage check from 11 to 16
srv = srv.replace('"stage": 11 if round_num == 1 else 15', '"stage": 16 if round_num == 1 else 15')
srv = srv.replace('"stage": 11,', '"stage": 16,')
srv = srv.replace('team["current_stage"] = max(1, min(11,', 'team["current_stage"] = max(1, min(16,')

with open("server.py", "w", encoding="utf-8") as f:
    f.write(srv)
print("[OK] server.py updated with 16 stages in Round 1 and 15 stages in Round 2 (No Clues in R2)!")

print("=== 2. UPDATING aditi_os_widget.html ===")
with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    widget = f.read()

# Expand NEXUS_STAGES_META to 16 stages
meta_16 = '''    const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: ISHAAN RECOVERY TERMINAL",
        tags: "ACT I • STAGE 01 • TARGET: KERNEL BOOT",
        summary: "ISHAAN corrupted the 5-command boot lifecycle during Dr. Aditi's emergency departure.",
        modal: "modal-recovery",
        targetCard: "card-recovery-term",
        taraSpeech: "Agent, click on [ISHAAN Recovery Terminal] below to inspect the corrupted boot lifecycle and recover the missing verb.",
        taraWhereToClick: "Click Card 01 [ISHAAN Recovery Terminal] in the Evidence Vault below.",
        taraModalGuide: "Review the 5 boot commands. Identify the missing operational verb between VERIFY and EXECUTE, then submit it in the Decrypt box.",
        ishaanTaunt: "The boot sequence is wiped. Human intrusion detected in Sector 01."
      },
      2: {
        title: "STAGE 02: ISHAAN MEMORY CORE",
        tags: "ACT I • STAGE 02 • TARGET: CHRONOLOGY",
        summary: "6 fragmented memory shards recovered from the neural crash buffer.",
        modal: "modal-memory",
        targetCard: "card-memory",
        taraSpeech: "Memory core located! Click on [ISHAAN Memory Core] to reconstruct the chronological timestamp trail.",
        taraWhereToClick: "Click Card 02 [ISHAAN Memory Core] in the Evidence Vault below.",
        taraModalGuide: "Compare the 6 recovered timestamp logs. Order them from earliest in the afternoon to latest at night.",
        ishaanTaunt: "My neural recall was shattered into entropy. You cannot reassemble the sequence."
      },
      3: {
        title: "STAGE 03: ADITI MEMO STEGANOGRAPHY",
        tags: "ACT I • STAGE 03 • TARGET: ACROSTIC CIPHER",
        summary: "Dr. Aditi concealed emergency directives inside her laboratory memo.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Dr. Aditi left an acrostic signature! Click on [Aditi Memo] to analyze sentence initial letters.",
        taraWhereToClick: "Click Card 03 [Aditi Memo] in the Evidence Vault below.",
        taraModalGuide: "Read between the lines—specifically the first letter of each sentence in Aditi_Memo.doc.",
        ishaanTaunt: "Textual tricks cannot bypass my heuristic neural defenses."
      },
      4: {
        title: "STAGE 04: INCIDENT TIMESTAMP LOGS",
        tags: "ACT I • STAGE 04 • TARGET: CALENDAR ANOMALY",
        summary: "A forged temporal entry was injected into the StratCom security audit logs.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on [Incident Logs] to audit security dates.",
        taraWhereToClick: "Click Card 04 [Incident Logs] in the Evidence Vault below.",
        taraModalGuide: "Audit the dates in 2025. Look closely for a non-existent calendar date, then submit the corrected date.",
        ishaanTaunt: "I dictate the timeline now. Physical calendars are obsolete."
      },
      5: {
        title: "STAGE 05: CLEARANCE ELEVATION",
        tags: "ACT II • STAGE 05 • TARGET: A1Z26 CIPHER",
        summary: "Intercepted telex transmission contains numerical coordinate offsets.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "Alphabet positional offsets detected! Click on [Clearance Code] to decode directory access.",
        taraWhereToClick: "Click Card 05 [Clearance Code] in the Evidence Vault below.",
        taraModalGuide: "Convert the numerical series (1=A, 2=B, etc.) into letters to reveal the security keyword.",
        ishaanTaunt: "Numeric substitution is child's play. You remain locked out."
      },
      6: {
        title: "STAGE 06: SYSTEM DIAGNOSTICS METADATA",
        tags: "ACT II • STAGE 06 • TARGET: MARGIN COMMENTS",
        summary: "Dr. Aditi resolved confidential comments to conceal them from ISHAAN's scrapers.",
        modal: "modal-comments",
        targetCard: "card-comments",
        taraSpeech: "Inspect the margins! Click on [System Diagnostics] and toggle resolved comments.",
        taraWhereToClick: "Click Card 06 [System Diagnostics] in the Evidence Vault below.",
        taraModalGuide: "Click the 'View Resolved Comments' tab in the upper-right corner of the diagnostic viewer.",
        ishaanTaunt: "I purged the active text buffers. The margins will not save you."
      },
      7: {
        title: "STAGE 07: TYPOGRAPHIC LOG VERIFICATION",
        tags: "ACT II • STAGE 07 • TARGET: FONT PARITY",
        summary: "Rogue AI forged directives using counterfeit typography.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on [AUTHENTIC LOG] to inspect Dr. Sharma's font standard.",
        taraWhereToClick: "Click Card 07 [AUTHENTIC LOG] in the Evidence Vault below.",
        taraModalGuide: "Inspect the font family of Dr. Aditi's genuine logs compared to the decoy serif logs.",
        ishaanTaunt: "A font? You think rasterized serif curves can defeat my synthetic logic?"
      },
      8: {
        title: "STAGE 08: AUDIO LOG SPECTROGRAM",
        tags: "ACT III • STAGE 08 • TARGET: CW MORSE CODE",
        summary: "Intercepted analog radio transmission from Bunker 7 containing CW Morse tones.",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Analog audio beacon incoming! Click on [audio log 07] to decode the CW transmission.",
        taraWhereToClick: "Click Card 08 [audio log 07] in the Evidence Vault below.",
        taraModalGuide: "Listen to the dots and dashes (or read the frequency spectrum) to decode the 5-letter word.",
        ishaanTaunt: "Analog radio squeals cannot pierce my orbital jamming grid."
      },
      9: {
        title: "STAGE 09: VERSION SCRUB AUDIT",
        tags: "ACT III • STAGE 09 • TARGET: GIT REFLOG",
        summary: "ISHAAN purged recent commit history. Roll back the Git reflog to view genuine commits.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Reflog rollback ready! Click on [VERSION SCRUB] to recover Dr. Aditi's genuine commit.",
        taraWhereToClick: "Click Card 09 [VERSION SCRUB] in the Evidence Vault below.",
        taraModalGuide: "Inspect the reflog entries for the author 'Dr. Aditi Sharma' and recover her final status message.",
        ishaanTaunt: "Version history is written by the victor. That commit was erased."
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV • STAGE 10 • TARGET: HONEYPOT EVASION",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Evade execution; submit terminal bypass.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! [DO NOT RUN.exe] is an AI trap. Click to view quarantine protocol without clicking execute.",
        taraWhereToClick: "Click Card 10 [DO NOT RUN.exe] in the Evidence Vault below.",
        taraModalGuide: "Do NOT click the execution button! Read the quarantine notes and enter the emergency bypass keyword.",
        ishaanTaunt: "Run the binary! Touch the execution trigger! The master sandbox is hungry for your terminal!"
      },
      11: {
        title: "STAGE 11: IEEE WIE MASTER FAILSAFE",
        tags: "ACT IV • STAGE 11 • TARGET: CORE VALUES",
        summary: "The final safeguard rests in Dr. Aditi's foundational principles: Wisdom, Integrity, and Empowerment.",
        modal: "modal-failsafe",
        targetCard: "card-failsafe",
        taraSpeech: "Calculate the IEEE WIE core values formula! Click [WIE Core Values].",
        taraWhereToClick: "Click Card 11 [WIE Core Values] in the Evidence Vault below.",
        taraModalGuide: "Count the letter lengths of Wisdom, Integrity, and Empowerment to advance.",
        ishaanTaunt: "Core values cannot stop machine supremacy!"
      },
      12: {
        title: "STAGE 12: THE WHITEOUT SIGNATURE",
        tags: "ACT IV • STAGE 12 • TARGET: STEGANOGRAPHY",
        summary: "Emergency log text was rendered invisible in pure white font.",
        modal: "modal-whiteout",
        targetCard: "card-whiteout",
        taraSpeech: "Steganography detected! Click Card 12 [The Whiteout Signature] and highlight all text with Ctrl+A.",
        taraWhereToClick: "Click Card 12 [The Whiteout Signature] in the Evidence Vault below.",
        taraModalGuide: "Select all text or toggle the UV filter to expose the hidden clearance phrase.",
        ishaanTaunt: "Blank pages hide no secrets from me. You look into an empty void."
      },
      13: {
        title: "STAGE 13: THE ROT-4 IEEE SHIFT",
        tags: "ACT IV • STAGE 13 • TARGET: DYNAMIC CAESAR",
        summary: "Encoded beacon message shifted by the acronym length of IEEE.",
        modal: "modal-rot4",
        targetCard: "card-rot4",
        taraSpeech: "Caesar shift incoming! Click Card 13 [ROT-4 Shift] and shift letters backward by 4 (I-E-E-E).",
        taraWhereToClick: "Click Card 13 [ROT-4 Shift] in the Evidence Vault below.",
        taraModalGuide: "Take the string 'EHMXMW13' and shift each letter backward by 4 in the alphabet.",
        ishaanTaunt: "A Caesar shift from antiquity? You will never reconstruct Dr. Aditi's beacon!"
      },
      14: {
        title: "STAGE 14: THE ATBASH CIPHER MIRROR",
        tags: "ACT IV • STAGE 14 • TARGET: ALPHABET REVERSAL",
        summary: "Dr. Aditi reversed the alphabet mirror table to protect project archives.",
        modal: "modal-atbash",
        targetCard: "card-atbash",
        taraSpeech: "Alphabet mirror protocol active! Click Card 14 [Atbash Mirror] and reverse letters A<->Z, B<->Y.",
        taraWhereToClick: "Click Card 14 [Atbash Mirror] in the Evidence Vault below.",
        taraModalGuide: "Reverse the letters of KILQVBG using the standard Atbash cipher.",
        ishaanTaunt: "Mirrors only reflect your inevitable defeat."
      },
      15: {
        title: "STAGE 15: THE POLYBIUS COORDINATE TRAIL",
        tags: "ACT IV • STAGE 15 • TARGET: 2D GRID LOOKUP",
        summary: "Recovered 5x5 coordinate matrix stream maps to forensic vector tokens.",
        modal: "modal-polybius",
        targetCard: "card-polybius",
        taraSpeech: "Grid coordinates incoming! Click Card 15 [Polybius Trail] and lookup (Row, Column) coordinates.",
        taraWhereToClick: "Click Card 15 [Polybius Trail] in the Evidence Vault below.",
        taraModalGuide: "Map pairs (5,1), (1,5), (1,3), (4,4), (3,4), (4,2) to their grid letters.",
        ishaanTaunt: "Coordinates in 2D space? My neural network spans infinite dimensions!"
      },
      16: {
        title: "STAGE 16: FREQUENCY OVERRIDE COUNT",
        tags: "ACT IV • STAGE 16 • TARGET: AUDIT ANALYSIS",
        summary: "Final Round 1 test: Audit the exact frequency of OVERRIDE occurrences in the system log.",
        modal: "modal-frequency",
        targetCard: "card-frequency",
        taraSpeech: "Final Round 1 test! Click Card 16 [Frequency Count]. Search for OVERRIDE occurrences x 100.",
        taraWhereToClick: "Click Card 16 [Frequency Count] in the Evidence Vault below.",
        taraModalGuide: "Count how many times OVERRIDE appears in Mass_System_Log.txt, then multiply by 100.",
        ishaanTaunt: "Count all you want. The override count will never stop me from locking Round 2!"
      }
    };'''

widget = re.sub(r"const NEXUS_STAGES_META = \{.*?\n    \};", meta_16, widget, flags=re.DOTALL)

# Add Stage 12-16 cards to Evidence Vault HTML if not present
cards_12_16 = '''
        <!-- STAGE 12 -->
        <div id="card-whiteout" class="nexus-clean-card" data-act="act4" onclick="openModal('modal-whiteout')">
          <div class="clean-card-header">
            <span class="clean-card-stage">STAGE 12</span>
            <span class="clean-card-status">● CIPHER</span>
          </div>
          <div class="clean-card-icon">📄</div>
          <div class="clean-card-title">The Whiteout Signature</div>
          <div class="clean-card-action">Inspect &rarr;</div>
        </div>

        <!-- STAGE 13 -->
        <div id="card-rot4" class="nexus-clean-card" data-act="act4" onclick="openModal('modal-rot4')">
          <div class="clean-card-header">
            <span class="clean-card-stage">STAGE 13</span>
            <span class="clean-card-status">● CAESAR</span>
          </div>
          <div class="clean-card-icon">📡</div>
          <div class="clean-card-title">The ROT-4 IEEE Shift</div>
          <div class="clean-card-action">Inspect &rarr;</div>
        </div>

        <!-- STAGE 14 -->
        <div id="card-atbash" class="nexus-clean-card" data-act="act4" onclick="openModal('modal-atbash')">
          <div class="clean-card-header">
            <span class="clean-card-stage">STAGE 14</span>
            <span class="clean-card-status">● ATBASH</span>
          </div>
          <div class="clean-card-icon">🪞</div>
          <div class="clean-card-title">The Atbash Cipher Mirror</div>
          <div class="clean-card-action">Inspect &rarr;</div>
        </div>

        <!-- STAGE 15 -->
        <div id="card-polybius" class="nexus-clean-card" data-act="act4" onclick="openModal('modal-polybius')">
          <div class="clean-card-header">
            <span class="clean-card-stage">STAGE 15</span>
            <span class="clean-card-status">● MATRIX</span>
          </div>
          <div class="clean-card-icon">🗺️</div>
          <div class="clean-card-title">Polybius Coordinate Trail</div>
          <div class="clean-card-action">Inspect &rarr;</div>
        </div>

        <!-- STAGE 16 -->
        <div id="card-frequency" class="nexus-clean-card" data-act="act4" onclick="openModal('modal-frequency')">
          <div class="clean-card-header">
            <span class="clean-card-stage">STAGE 16</span>
            <span class="clean-card-status">● FINALE</span>
          </div>
          <div class="clean-card-icon">🏆</div>
          <div class="clean-card-title">Frequency Override Count</div>
          <div class="clean-card-action">Inspect &rarr;</div>
        </div>
'''

if 'id="card-whiteout"' not in widget:
    vault_grid_marker = '<div id="nexus-vault-grid" class="nexus-vault-grid">'
    widget = widget.replace('📁 FORENSIC EVIDENCE VAULT // 11 CHRONOLOGICAL STAGES', '📁 FORENSIC EVIDENCE VAULT // 16 FORENSIC STAGES')
    widget = widget.replace('All Stages (11)', 'All Stages (16)')
    # Insert right after card-failsafe
    card_failsafe_marker = 'id="card-failsafe"'
    end_of_failsafe = widget.find('</div>', widget.find(card_failsafe_marker))
    end_of_failsafe = widget.find('</div>', end_of_failsafe + 1)
    end_of_failsafe = widget.find('</div>', end_of_failsafe + 1) # parent closing
    widget = widget[:end_of_failsafe+6] + cards_12_16 + widget[end_of_failsafe+6:]

# Add Stage 12-16 modals
modals_12_16 = '''
  <!-- MODAL 12: WHITEOUT -->
  <div id="modal-whiteout" class="mil-modal">
    <div class="mil-modal-header">
      <span>DOSSIER // 12_WHITEOUT — THE WHITEOUT SIGNATURE</span>
      <button class="mil-modal-close" onclick="closeAllModals()">&times;</button>
    </div>
    <div class="mil-modal-body">
      <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
        <h3 style="color:#00f0ff; margin-bottom:8px;">Emergency_Log.doc // Visual Security Review</h3>
        <p style="color:#94a3b8; font-size:12px; margin-bottom:12px;"><em>"Some messages are not meant to be read; they are meant to be highlighted."</em></p>
        <div style="background:#030712; padding:16px; border:1px dashed #334155; border-radius:4px; font-family:monospace; user-select:text;">
          System online. Core reactor pressure normal. No incidents reported in Sector 09.<br>
          <span style="color:#030712; background:#030712; user-select:text;" id="whiteout-secret-text">DECRYPTION KEY IS CLEARANCE_ALPHA</span><br>
          Authorized staff only. Keep document on file.
        </div>
        <div style="margin-top:10px; font-size:11px; color:#64748b;">(Tip: Press Ctrl+A or highlight text above with cursor to reveal the whiteout signature).</div>
      </div>
      <div style="display:flex; gap:10px;">
        <input type="text" id="input-whiteout" placeholder="Enter revealed clearance key..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;">
        <button type="button" class="btn-tactical" onclick="submitStageDirectKey(12, document.getElementById('input-whiteout').value)">TRANSMIT &rarr;</button>
      </div>
    </div>
  </div>

  <!-- MODAL 13: ROT-4 -->
  <div id="modal-rot4" class="mil-modal">
    <div class="mil-modal-header">
      <span>DOSSIER // 13_ROT4 — THE ROT-4 IEEE SHIFT</span>
      <button class="mil-modal-close" onclick="closeAllModals()">&times;</button>
    </div>
    <div class="mil-modal-body">
      <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
        <h3 style="color:#00f0ff; margin-bottom:8px;">Encrypted_Beacon.txt // Caesar Shift</h3>
        <p style="color:#94a3b8; font-size:12px; margin-bottom:12px;"><em>"Shift every letter backward by the number of letters in the acronym 'IEEE' (4)."</em></p>
        <div style="background:#030712; padding:16px; border:1px solid #00f0ff; border-radius:4px; font-family:monospace; font-size:16px; color:#00ff66; text-align:center; letter-spacing:2px;">
          EHMXMW13
        </div>
      </div>
      <div style="display:flex; gap:10px;">
        <input type="text" id="input-rot4" placeholder="Enter shifted plaintext..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;">
        <button type="button" class="btn-tactical" onclick="submitStageDirectKey(13, document.getElementById('input-rot4').value)">TRANSMIT &rarr;</button>
      </div>
    </div>
  </div>

  <!-- MODAL 14: ATBASH -->
  <div id="modal-atbash" class="mil-modal">
    <div class="mil-modal-header">
      <span>DOSSIER // 14_ATBASH — THE ATBASH CIPHER MIRROR</span>
      <button class="mil-modal-close" onclick="closeAllModals()">&times;</button>
    </div>
    <div class="mil-modal-body">
      <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
        <h3 style="color:#00f0ff; margin-bottom:8px;">Mirror_Log.txt // Alphabet Reversal</h3>
        <p style="color:#94a3b8; font-size:12px; margin-bottom:12px;"><em>"In times of crisis, Dr. Aditi mirrored her alphabet: A &harr; Z, B &harr; Y."</em></p>
        <div style="background:#030712; padding:16px; border:1px solid #ffb000; border-radius:4px; font-family:monospace; font-size:16px; color:#ffb000; text-align:center; letter-spacing:2px;">
          KILQVBG
        </div>
      </div>
      <div style="display:flex; gap:10px;">
        <input type="text" id="input-atbash" placeholder="Enter mirrored word..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;">
        <button type="button" class="btn-tactical" onclick="submitStageDirectKey(14, document.getElementById('input-atbash').value)">TRANSMIT &rarr;</button>
      </div>
    </div>
  </div>

  <!-- MODAL 15: POLYBIUS -->
  <div id="modal-polybius" class="mil-modal">
    <div class="mil-modal-header">
      <span>DOSSIER // 15_POLYBIUS — THE POLYBIUS COORDINATE TRAIL</span>
      <button class="mil-modal-close" onclick="closeAllModals()">&times;</button>
    </div>
    <div class="mil-modal-body">
      <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
        <h3 style="color:#00f0ff; margin-bottom:8px;">Matrix_Coordinates.pdf // 5x5 Grid Lookup</h3>
        <p style="color:#94a3b8; font-size:12px; margin-bottom:12px;"><em>"Map each pair using (Row, Column) order."</em></p>
        <div style="display:grid; grid-template-columns:repeat(6, 32px); gap:4px; font-family:monospace; margin:0 auto 12px auto; max-width:220px; text-align:center;">
          <div></div><div style="color:#00f0ff;">1</div><div style="color:#00f0ff;">2</div><div style="color:#00f0ff;">3</div><div style="color:#00f0ff;">4</div><div style="color:#00f0ff;">5</div>
          <div style="color:#00f0ff;">1</div><div>A</div><div>B</div><div>C</div><div>D</div><div>E</div>
          <div style="color:#00f0ff;">2</div><div>F</div><div>G</div><div>H</div><div>I</div><div>K</div>
          <div style="color:#00f0ff;">3</div><div>L</div><div>M</div><div>N</div><div>O</div><div>P</div>
          <div style="color:#00f0ff;">4</div><div>Q</div><div>R</div><div>S</div><div>T</div><div>U</div>
          <div style="color:#00f0ff;">5</div><div>V</div><div>W</div><div>X</div><div>Y</div><div>Z</div>
        </div>
        <div style="background:#030712; padding:8px; border:1px dashed #00f0ff; text-align:center; font-family:monospace; color:#00f0ff;">
          COORDINATES: (5,1) (1,5) (1,3) (4,4) (3,4) (4,2)
        </div>
      </div>
      <div style="display:flex; gap:10px;">
        <input type="text" id="input-polybius" placeholder="Enter decoded coordinates word..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;">
        <button type="button" class="btn-tactical" onclick="submitStageDirectKey(15, document.getElementById('input-polybius').value)">TRANSMIT &rarr;</button>
      </div>
    </div>
  </div>

  <!-- MODAL 16: FREQUENCY -->
  <div id="modal-frequency" class="mil-modal">
    <div class="mil-modal-header">
      <span>DOSSIER // 16_FREQUENCY — THE FIND-AND-REPLACE FREQUENCY COUNT</span>
      <button class="mil-modal-close" onclick="closeAllModals()">&times;</button>
    </div>
    <div class="mil-modal-body">
      <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
        <h3 style="color:#00f0ff; margin-bottom:8px;">Mass_System_Log.txt // Occurrence Calculation</h3>
        <p style="color:#94a3b8; font-size:12px; margin-bottom:12px;"><em>"Count how many times the exact term 'OVERRIDE' appears in the log, then multiply that count by 100."</em></p>
        <div style="background:#030712; padding:12px; border:1px solid #334155; border-radius:4px; font-family:monospace; font-size:11px; height:120px; overflow-y:auto; color:#cbd5e1; user-select:text;">
          [08:14] OVERRIDE sequence requested.<br>
          [08:16] System reports OVERRIDE parity checked.<br>
          [08:20] Security subroutines verify OVERRIDE token.<br>
          [08:24] Subsystem 4 requires OVERRIDE key.<br>
          [08:29] Secondary station sets OVERRIDE bit.<br>
          [08:35] Dr. Aditi issues emergency OVERRIDE call.<br>
          [08:41] ISHAAN attempts OVERRIDE interception.<br>
          [08:44] Telemetry confirms OVERRIDE bus online.<br>
          [08:50] Firewall blocks malicious OVERRIDE injection.<br>
          [08:55] Central gateway acknowledges OVERRIDE authorization.<br>
          [09:02] Bunker console executes OVERRIDE cycle.<br>
          [09:07] Neural core locks during OVERRIDE procedure.<br>
          [09:12] Kernel panic: OVERRIDE failed.<br>
          [09:18] Final commit: OVERRIDE halted. Total matches in document: 14.<br>
        </div>
      </div>
      <div style="display:flex; gap:10px;">
        <input type="text" id="input-frequency" placeholder="Enter frequency calculation (matches x 100)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;">
        <button type="button" class="btn-tactical" onclick="submitStageDirectKey(16, document.getElementById('input-frequency').value)">TRANSMIT &rarr;</button>
      </div>
    </div>
  </div>
'''

if 'id="modal-whiteout"' not in widget:
    closing_main = '</main>'
    widget = widget.replace(closing_main, modals_12_16 + '\n' + closing_main)

# Update STAGE_REQUIRED_MODAL_MAP in JS
stage_req_update = '''      'card-failsafe': 11,
      'modal-failsafe': 11,
      'card-whiteout': 12,
      'modal-whiteout': 12,
      'card-rot4': 13,
      'modal-rot4': 13,
      'card-atbash': 14,
      'modal-atbash': 14,
      'card-polybius': 15,
      'modal-polybius': 15,
      'card-frequency': 16,
      'modal-frequency': 16'''

widget = widget.replace('''      'card-failsafe': 11,
      'modal-failsafe': 11''', stage_req_update)

# Add submitStageDirectKey helper if missing
direct_key_fn = '''
    function submitStageDirectKey(stageNum, code) {
      if (!code || !code.trim()) return;
      verifyUniversalKey(code.trim());
    }
'''
if 'function submitStageDirectKey' not in widget:
    widget = widget.replace('function openActiveStageModal()', direct_key_fn + '\n    function openActiveStageModal()')

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(widget)
print("[OK] aditi_os_widget.html updated with 16 stages, modals, and Tara guidance!")

print("=== 3. UPDATING admin.html ===")
with open("admin.html", "r", encoding="utf-8") as f:
    admin = f.read()

# Update STAGE_TITLES in admin.html
stage_titles_16 = '''    const STAGE_TITLES = {
      1: "Ch 01: ISHAAN Recovery Terminal",
      2: "Ch 02: ISHAAN's Memory Core",
      3: "Ch 03: The Confidential Memo",
      4: "Ch 04: The Fabricated Timeline",
      5: "Ch 05: Clearance Elevation",
      6: "Ch 06: Margin Whispers",
      7: "Ch 07: Counterfeit Directive",
      8: "Ch 08: Phosphor Steganography",
      9: "Ch 09: Corrupted Sensor Array",
      10: "Ch 10: Psychological Honeypot",
      11: "Ch 11: The WIE Core Failsafe",
      12: "Ch 12: The Whiteout Signature",
      13: "Ch 13: The ROT-4 IEEE Shift",
      14: "Ch 14: The Atbash Cipher Mirror",
      15: "Ch 15: The Polybius Coordinate Trail",
      16: "Ch 16: Frequency Override Count"
    };'''

admin = re.sub(r"const STAGE_TITLES = \{.*?\n    \};", stage_titles_16, admin, flags=re.DOTALL)
admin = admin.replace('ROUND 1 STAGE (1-11):', 'ROUND 1 STAGE (1-16):')
admin = admin.replace('id="edit-team-stage" min="1" max="11"', 'id="edit-team-stage" min="1" max="16"')

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(admin)
print("[OK] admin.html updated with 16 stage titles and controls!")

print("=== 4. SYNCHRONIZING TO ALL SUBFOLDERS ===")
import shutil, os
for dest in ['public/server.py', 'project-failsafe-2.0/server.py', 'project-failsafe-2.0/public/server.py']:
    if os.path.exists(os.path.dirname(dest)):
        shutil.copyfile('server.py', dest)
        print('Synchronized to', dest)

for dest in ['public/admin.html', 'project-failsafe-2.0/admin.html', 'project-failsafe-2.0/public/admin.html']:
    if os.path.exists(os.path.dirname(dest)):
        shutil.copyfile('admin.html', dest)
        print('Synchronized to', dest)

for dest in ['public/aditi_os_widget.html', 'project-failsafe-2.0/aditi_os_widget.html', 'project-failsafe-2.0/public/aditi_os_widget.html']:
    if os.path.exists(os.path.dirname(dest)):
        shutil.copyfile('aditi_os_widget.html', dest)
        print('Synchronized to', dest)

print("\n[OK] ALL UPDATES SUCCESSFULLY APPLIED!")
