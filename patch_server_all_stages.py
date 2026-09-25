import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update STAGES 16 and add 17..21
old_s16 = '''    16: {
        "title": "The Find-and-Replace Frequency Count",
        "keys": ["1400", "1,400"],
        "next_stage": "COMPLETE",
        "hints": [
            "Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
            "Ctrl+F shows 14 matches. 14 x 100 = 1400."
        ]
    }
}'''

new_stages_16_to_21 = '''    16: {
        "title": "The Find-and-Replace Frequency Count (Mass_System_Log.txt)",
        "keys": ["1400", "1,400"],
        "next_stage": 17,
        "hints": [
            "Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
            "Ctrl+F shows 14 matches. 14 x 100 = 1400."
        ]
    },
    17: {
        "title": "The Rogue Chatbot Polybius Shift (Intercepted_ADI_Transmission.pdf)",
        "keys": ["VSLXI", "vslxi"],
        "next_stage": 18,
        "hints": [
            "Apply vector translation (+1 Row, -1 Col) to the intercepted coordinates before mapping onto the Polybius grid.",
            "Shifted coords: (4,2)->(5,1)=V, (3,4)->(4,3)=S, (2,2)->(3,1)=L, (4,4)->(5,3)=X, (1,5)->(2,4)=I. Enter VSLXI."
        ]
    },
    18: {
        "title": "The Modular Clock Loop (Cycle_Diagnostics.png)",
        "keys": ["GCBGE", "gcbge"],
        "next_stage": 19,
        "hints": [
            "System nodes run on a 12-hour circular buffer (1=A through 12=L). Start at Node L (12) and apply clockwise shifts wrapping modulo 12.",
            "12+7=19->7(G), 7+8=15->3(C), 3+11=14->2(B), 2+5=7(G), 7+10=17->5(E). Enter GCBGE."
        ]
    },
    19: {
        "title": "The Anomaly Checklist (Server_Status_Check.pdf)",
        "keys": ["GAMMA", "gamma"],
        "next_stage": 20,
        "hints": [
            "Compare each node's status reading against its normal range (40°C - 45°C) to locate the outlier node.",
            "Node Gamma registers 47°C, which exceeds the normal 40°C - 45°C operating threshold. Enter GAMMA in ALL CAPS."
        ]
    },
    20: {
        "title": "The Shift Cipher Matrix (Emergency_Override_Key.txt)",
        "keys": ["DAHHK", "dahhk"],
        "next_stage": 21,
        "hints": [
            "ADI went rogue on Sunday, October 13, 2013. Sunday = 7 (7th day of the week). Shift each letter in KHOOR backward by 7 positions.",
            "K(11)-7=4(D), H(8)-7=1(A), O(15)-7=8(H), O(15)-7=8(H), R(18)-7=11(K). Enter DAHHK."
        ]
    },
    21: {
        "title": "The Log Anomaly Timeline (System_Audit_2013.log)",
        "keys": ["520"],
        "next_stage": "COMPLETE",
        "hints": [
            "Track the TIMESTAMP column strictly from top to bottom to find the entry that is out of chronological order.",
            "Log 104 (timestamp 14:08:30) occurs after 14:12:01. Multiply 104 by the 5 total entries in the table: 104 x 5 = 520."
        ]
    }
}'''

if old_s16 in code:
    code = code.replace(old_s16, new_stages_16_to_21)
    print("Replaced STAGES 16..21 in server.py")
else:
    print("Warning: old_s16 not matched exactly, trying regex...")
    code = re.sub(
        r'16:\s*\{\s*"title":\s*"The Find-and-Replace Frequency Count".*?\}\s*\}',
        new_stages_16_to_21,
        code,
        flags=re.DOTALL
    )
    print("Applied regex replacement for STAGES 16..21")

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved stage changes to server.py")
