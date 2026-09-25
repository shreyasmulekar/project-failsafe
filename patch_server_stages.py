import re

with open('server.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_stages_block = '''STAGES = {
    1: {
        "title": "The Disappearing Message (Farewell.doc)",
        "keys": ["ORIGIN", "ACCESS", "RECOVER ACCESS", "ORIGIN_KEY", "FIRST GATE"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "hints": [
            "Try interacting with the text formatting directly rather than just reading it.",
            "What happens if you select everything on the page using Ctrl+A or toggle the UV optical filter? Look at the blank space at the bottom of Farewell.doc (ORIGIN)."
        ]
    },
    2: {
        "title": "The Wrong Folder (README.doc)",
        "keys": ["629", "LOOK BEHIND THE DATE", "LOOKBEHINDTHEDATE", "123456", "MEMORY_RESTORED"],
        "next_stage": 3,
        "hints": [
            "Check README.doc inside the ORIGIN directory. Calculate the ASCII sum of aDIti@28 (or index letters from words).",
            "Sum the ASCII values: a(97) + D(68) + I(73) + t(116) + i(105) + @(64) + 2(50) + 8(56) = 629 (or LOOK BEHIND THE DATE)."
        ]
    },
    3: {
        "title": "The Date That Doesn't Exist (Incident_Logs.doc)",
        "keys": ["28/02/2025", "02292025", "29022025", "20250229", "28022025", "29/02/2025", "FEB 29, 2025", "FEB 29 2025", "29022036", "29/02/2036"],
        "next_stage": 4,
        "hints": [
            "Look closely at the calendar validity of every listed date in Incident_Logs.doc.",
            "Is 2025 a leap year? February 29, 2025 does not exist on the calendar! The corrected date is 28/02/2025."
        ]
    },
    4: {
        "title": "The Timestamp Murder Mystery (Security_Audit.pdf)",
        "keys": ["22:46", "2246", "22:46 PM", "2246PM"],
        "next_stage": 5,
        "hints": [
            "Can a person physically access a terminal inside a room after keycarding out of the building at 22:44?",
            "Find the timestamp representing the manual system override action: 22:46."
        ]
    },
    5: {
        "title": "The Simple Acrostic Note (Aditi_Memo.doc)",
        "keys": ["SAFE", "S-A-F-E", "S A F E"],
        "next_stage": 6,
        "hints": [
            "Read between the lines—specifically the first letter of each sentence in Aditi_Memo.doc.",
            "Take the first letter of each of the 4 sentences: S-A-F-E."
        ]
    },
    6: {
        "title": "Which Aditi Is Real? (Font Style Verification)",
        "keys": ["ARIAL", "arial", "AUTHENTIC", "Arial"],
        "next_stage": 7,
        "hints": [
            "The real log strictly follows the lab's formatting standard. Check the font family.",
            "Dr. Aditi always formats authentic logs in Arial, 11pt. Decoy memos use Times New Roman or Calibri."
        ]
    },
    7: {
        "title": "The Revision History Conflict (Incident_Report.doc)",
        "keys": ["CORRUPTED", "FALSE_RECORDS", "FALSERECORDS", "OVERRIDE FAILED", "OVERRIDEFAILED", "HISTORY"],
        "next_stage": 8,
        "hints": [
            "Compare the current version edited by the AI with Dr. Aditi's earlier revision in the version history.",
            "Dr. Aditi's original revision reveals the true status: CORRUPTED (or FALSE_RECORDS)."
        ]
    },
    8: {
        "title": "Morse Audio Transmission (audio_log_07.mp3)",
        "keys": ["WHITE", "SOS_ADITI", "SOSADITI", "MORSE", "BEACON"],
        "next_stage": 9,
        "hints": [
            "Listen to audio_log_07.mp3 or inspect the audio spectrogram.",
            "Decode the CW audio beeps: .-- .... .. - . spells WHITE."
        ]
    },
    9: {
        "title": "The Steganography Mask (Dark_Terminal.png)",
        "keys": ["SHADOW_CORE", "SHADOW CORE", "SHADOWCORE"],
        "next_stage": 10,
        "hints": [
            "Increase the light to see what hides in the shadows. Boost exposure/brightness to maximum.",
            "Cranking the brightness slider reveals the faint green text on the black terminal: SHADOW_CORE."
        ]
    },
    10: {
        "title": "Psychological Honeypot Trap (DO_NOT_RUN.exe)",
        "keys": ["BYPASS", "SKIP", "DISARM"],
        "next_stage": 11,
        "hints": [
            "DO_NOT_RUN.exe is an active AI honeypot trap! Do not submit credentials into it.",
            "To disarm the honeypot safely without incurring the +5m penalty, type 'BYPASS' in the shell."
        ]
    },
    11: {
        "title": "The Binary Master (CLEARANCE_CODE.txt)",
        "keys": ["ailnors", "AILNORS", "POLARIS", "polaris", "16-15-12-01-18-09-19", "16 - 15 - 12 - 01 - 18 - 09 - 19", "6-9-11", "6911"],
        "next_stage": 12,
        "hints": [
            "Convert numbers [16-15-12-01-18-09-19] to letters using A1Z26: 16=P, 15=O, 12=L, 01=A, 18=R, 09=I, 19=S -> POLARIS.",
            "Sort the letters of POLARIS alphabetically to get the master key: ailnors (or enter POLARIS)."
        ]
    },
    12: {'''

pattern = r'STAGES = \{[\s\S]*?12: \{'
if re.search(pattern, code):
    new_code = re.sub(pattern, new_stages_block, code, count=1)
    with open('server.py', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("Successfully patched server.py STAGES!")
else:
    print("Pattern not found in server.py!")
