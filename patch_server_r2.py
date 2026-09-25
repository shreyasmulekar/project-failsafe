import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Current 15 stages of ROUND2_STAGES
# We will shift them to 2..16 and prepend Stage 1 and append Stage 17.

new_round2_stages = '''ROUND2_STAGES = {
    1: {
        "title": "EMERGENCY OVERRIDE (Emergency_Override_Key.txt)",
        "location": "Emergency_Override_Key.txt",
        "keys": ["GUARD", "guard"],
        "unlocked_by_default": True,
        "next_stage": 2,
        "hints": []
    },
    2: {
        "title": "The Matrix Box Transformation",
        "location": "Visual_Matrix.pdf",
        "keys": ["C", "THREE CIRCLES", "3 CIRCLES", "THREECIRCLES", "●●●"],
        "next_stage": 3,
        "hints": []
    },
    3: {
        "title": "The Clockwise Rotation Boxes",
        "location": "Rotation_Array.pdf",
        "keys": ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT"],
        "next_stage": 4,
        "hints": []
    },
    4: {
        "title": "The Spatial Net Folding Box",
        "location": "Cube_Net_Folding.pdf",
        "keys": ["5"],
        "next_stage": 5,
        "hints": []
    },
    5: {
        "title": "The Modulated Polybius Cipher",
        "location": "Polybius_Grid.pdf",
        "keys": ["CIPHER"],
        "next_stage": 6,
        "hints": []
    },
    6: {
        "title": "The QWERTY Shape Trace",
        "location": "Keyboard_Trace.png",
        "keys": ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        "next_stage": 7,
        "hints": []
    },
    7: {
        "title": "The Interlocking Logic Gate Flow",
        "location": "Logic_Gate_Circuits.pdf",
        "keys": ["011", "0,1,1", "0-1-1"],
        "next_stage": 8,
        "hints": []
    },
    8: {
        "title": "The Mirror Image String Inversion",
        "location": "Specular_Text.png",
        "keys": ["CLEARANCE"],
        "next_stage": 9,
        "hints": []
    },
    9: {
        "title": "The Rotational Matrix Operator",
        "location": "Compass_Grid.pdf",
        "keys": ["SE", "SOUTH EAST", "SOUTHEAST"],
        "next_stage": 10,
        "hints": []
    },
    10: {
        "title": "The Base-Invariant Digital Root Flow",
        "location": "Digital_Root_Log.txt",
        "keys": ["NONE", "IMPOSSIBLE", "NO PRIME", "0"],
        "next_stage": 11,
        "hints": []
    },
    11: {
        "title": "The Palindrome Filter Stream",
        "location": "Palindrome_Stream.txt",
        "keys": ["RLRCK"],
        "next_stage": 12,
        "hints": []
    },
    12: {
        "title": "The Diagonal Word Weave",
        "location": "Matrix_Diagonal.pdf",
        "keys": ["NODC"],
        "next_stage": 13,
        "hints": []
    },
    13: {
        "title": "The Perimeter Geometry Box Count",
        "location": "Grid_Perimeter.pdf",
        "keys": ["102", "102 BOXES"],
        "next_stage": 14,
        "hints": []
    },
    14: {
        "title": "The Alternating Checker Pattern",
        "location": "Checker_State.png",
        "keys": ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        "next_stage": 15,
        "hints": []
    },
    15: {
        "title": "The Shifted Ring Cipher",
        "location": "Ring_Shift.png",
        "keys": ["FINALS", "EBF"],
        "next_stage": 16,
        "hints": []
    },
    16: {
        "title": "The Cipher Wheel Protocol (THE RED QUESTION)",
        "location": "Cipher_Wheel_Spec.pdf",
        "keys": ["ECLIPSE"],
        "next_stage": 17,
        "hints": []
    },
    17: {
        "title": "The Failsafe Logic Tree (Failsafe_Gate_Status.pdf)",
        "location": "Failsafe_Gate_Status.pdf",
        "keys": ["0110"],
        "next_stage": "COMPLETE",
        "hints": []
    }
}'''

# Replace ROUND2_STAGES block in code
pattern = r'ROUND2_STAGES = \{.*?\n\}'
code = re.sub(pattern, new_round2_stages, code, flags=re.DOTALL)
print("ROUND2_STAGES replaced")

# Replace stage references in server.py
# In leaderboard / unlock functions:
# Replace checking stage 16 with stage 21 for R1
code = code.replace('>= 16', '>= 21')
code = code.replace('min(16, int(data["current_stage"]))', 'min(21, int(data["current_stage"]))')
code = code.replace('min(15, int(data["round_2_stage"]))', 'min(17, int(data["round_2_stage"]))')

# Unlock all levels endpoint
code = code.replace('t["current_stage"] = 16', 't["current_stage"] = 21')
code = code.replace('t["unlocked_stages"] = list(range(1, 17))', 't["unlocked_stages"] = list(range(1, 22))')
code = code.replace('t["stages_cleared"] = list(range(1, 17))', 't["stages_cleared"] = list(range(1, 22))')
code = code.replace('t["remote_override_stage"] = 16', 't["remote_override_stage"] = 21')

code = code.replace('t["round_2_stage"] = 15', 't["round_2_stage"] = 17')
code = code.replace('t["round2_stages_cleared"] = list(range(1, 16))', 't["round2_stages_cleared"] = list(range(1, 18))')

code = code.replace('Stages 01–16 & Round 2 Arena', 'Stages 01–21 & Round 2 Arena')
code = code.replace('Solved all 15 forensic challenges!', 'Solved all 17 forensic challenges!')
code = code.replace('Solved all 16 stages', 'Solved all 21 stages')

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated server.py successfully!")
