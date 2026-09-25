import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update R2_CLICK_DIRECTIVES
old_r2_directives = '''const R2_CLICK_DIRECTIVES = {
      1: "Inspect the 3x3 symbol transformation matrix. Click one of the candidate options [OPTION A], [OPTION B], [OPTION C], or [OPTION D] to select your deduction.",
      2: "Inspect the 90° clockwise rotation sequence across the boxes. Deduce the 4th corner position.",
      3: "Analyze the 2D unfolded cube net. Mentally fold the faces to identify which numbered face sits opposite to Face 1.",
      4: "Trace the row and column coordinates in the 5x5 Modulo-Polybius grid according to the offset rules to decode the keyword.",
      5: "Trace key clusters on the physical QWERTY keyboard layout to observe the geometric shape they form.",
      6: "Trace binary inputs A=1, B=0, and C=1 through the AND, OR, and XOR combinational gates to deduce the 3-bit output stream.",
      7: "Inspect the horizontally inverted optical buffer text and reflect the characters to read the security phrase.",
      8: "Apply the +45° clockwise rotation matrix transform operators from North-East to determine the final vector direction.",
      9: "Analyze digital root divisibility rules to determine if a 3-digit prime exists, or if none can exist.",
      10: "Scan the log string from both ends simultaneously to isolate the 5-character palindrome segment.",
      11: "Read the 4x4 matrix diagonally along the primary diagonal vectors to extract the 4-letter sequence.",
      12: "Calculate total perimeter boundary boxes on the 10x10 matrix using geometric boundary formula (4n - 4).",
      13: "Analyze alternating checkerboard tile parity rules to deduce the state of the 3 unknown corner cells.",
      14: "Trace dual concentric alphabet ring shifts (+3 outer, -2 inner) to decode the cipher letters.",
      15: "THE RED QUESTION: Align outer and inner cipher wheels by the key offset to recover the master override passphrase."
    };'''

new_r2_directives = '''const R2_CLICK_DIRECTIVES = {
      1: "EMERGENCY OVERRIDE: ADI went rogue on October 13, 2090 (Sunday = 7). Shift each letter in ciphertext N B H Y K backward by 7 to restore the authorization code.",
      2: "Inspect the 3x3 symbol transformation matrix. Click one of the candidate options [OPTION A], [OPTION B], [OPTION C], or [OPTION D] to select your deduction.",
      3: "Inspect the 90° clockwise rotation sequence across the boxes. Deduce the 4th corner position.",
      4: "Analyze the 2D unfolded cube net. Mentally fold the faces to identify which numbered face sits opposite to Face 1.",
      5: "Trace the row and column coordinates in the 5x5 Modulo-Polybius grid according to the offset rules to decode the keyword.",
      6: "Trace key clusters on the physical QWERTY keyboard layout to observe the geometric shape they form.",
      7: "Trace binary inputs A=1, B=0, and C=1 through the AND, OR, and XOR combinational gates to deduce the 3-bit output stream.",
      8: "Inspect the horizontally inverted optical buffer text and reflect the characters to read the security phrase.",
      9: "Apply the +45° clockwise rotation matrix transform operators from North-East to determine the final vector direction.",
      10: "Analyze digital root divisibility rules to determine if a 3-digit prime exists, or if none can exist.",
      11: "Scan the log string from both ends simultaneously to isolate the 5-character palindrome segment.",
      12: "Read the 4x4 matrix diagonally along the primary diagonal vectors to extract the 4-letter sequence.",
      13: "Calculate total perimeter boundary boxes on the 10x10 matrix using geometric boundary formula (4n - 4).",
      14: "Analyze alternating checkerboard tile parity rules to deduce the state of the 3 unknown corner cells.",
      15: "Trace dual concentric alphabet ring shifts (+3 outer, -2 inner) to decode the cipher letters.",
      16: "THE RED QUESTION: Align outer and inner cipher wheels by the key offset to recover the master override passphrase.",
      17: "THE FAILSAFE LOGIC TREE: Set the 4 switches (Alpha, Beta, Gamma, Delta) according to Dr. Aditi's rules and enter the 4-bit state (1=ON, 0=OFF)."
    };'''

if old_r2_directives in text:
    text = text.replace(old_r2_directives, new_r2_directives)
    print("Updated R2_CLICK_DIRECTIVES")
else:
    print("Warning: old_r2_directives not found")

# 2. Update R2_CARD_DEFINITIONS
old_r2_cards = '''const R2_CARD_DEFINITIONS = [
      { id: 1, act: "act1", icon: "🔲", tag: "MATRIX BOX", name: "Visual_Matrix.pdf", desc: "3x3 Missing Glyph Analysis" },
      { id: 2, act: "act1", icon: "🎲", tag: "CUBE NET", name: "Hypercube_Net.geom", desc: "3D Face Deductions" },
      { id: 3, act: "act1", icon: "🔄", tag: "ROTATION", name: "Orbital_Rotation.sys", desc: "90° Grid Transformation" },
      { id: 4, act: "act1", icon: "🗺️", tag: "MOD-POLYBIUS", name: "Polybius_Grid.mat", desc: "Coord Decoupling" },
      { id: 5, act: "act1", icon: "⌨️", tag: "QWERTY", name: "Physical_Keypad.hw", desc: "Keystroke Vector" },
      { id: 6, act: "act2", icon: "⚡", tag: "LOGIC GATE", name: "Boolean_Network.circ", desc: "XOR/AND Pulse Evaluation" },
      { id: 7, act: "act2", icon: "🪞", tag: "MIRROR TEXT", name: "Specular_Reflection.doc", desc: "Axis Inversion Recovery" },
      { id: 8, act: "act2", icon: "🧭", tag: "ROT-MATRIX", name: "Caesar_Substitution.mat", desc: "Index Shift Substitution" },
      { id: 9, act: "act2", icon: "🔢", tag: "DIGITAL ROOT", name: "Digital_Root_Log.txt", desc: "Base-Invariant Arithmetic" },
      { id: 10, act: "act2", icon: "🔁", tag: "PALINDROME", name: "Palindrome_Stream.txt", desc: "Symmetric String Filter" },
      { id: 11, act: "act3", icon: "📐", tag: "DIAGONAL", name: "Matrix_Diagonal.pdf", desc: "Diagonal String Weave" },
      { id: 12, act: "act3", icon: "📏", tag: "PERIMETER", name: "Grid_Perimeter.pdf", desc: "Boundary Box Quant" },
      { id: 13, act: "act3", icon: "🏁", tag: "CHECKER", name: "Checker_State.png", desc: "Grid Parity Evaluation" },
      { id: 14, act: "act3", icon: "⭕", tag: "RING CIPHER", name: "Ring_Shift.png", desc: "Concentric Modulo Shift" },
      { id: 15, act: "act3", icon: "🔴", tag: "RED QUESTION", name: "Cipher_Wheel_Spec.pdf", desc: "Grand Master Protocol" }
    ];'''

new_r2_cards = '''const R2_CARD_DEFINITIONS = [
      { id: 1, act: "act1", icon: "🚨", tag: "OVERRIDE", name: "Emergency_Override_Key.txt", desc: "Day-of-Week Shift Authorization" },
      { id: 2, act: "act1", icon: "🔲", tag: "MATRIX BOX", name: "Visual_Matrix.pdf", desc: "3x3 Missing Glyph Analysis" },
      { id: 3, act: "act1", icon: "🎲", tag: "CUBE NET", name: "Hypercube_Net.geom", desc: "3D Face Deductions" },
      { id: 4, act: "act1", icon: "🔄", tag: "ROTATION", name: "Orbital_Rotation.sys", desc: "90° Grid Transformation" },
      { id: 5, act: "act1", icon: "🗺️", tag: "MOD-POLYBIUS", name: "Polybius_Grid.mat", desc: "Coord Decoupling" },
      { id: 6, act: "act1", icon: "⌨️", tag: "QWERTY", name: "Physical_Keypad.hw", desc: "Keystroke Vector" },
      { id: 7, act: "act2", icon: "⚡", tag: "LOGIC GATE", name: "Boolean_Network.circ", desc: "XOR/AND Pulse Evaluation" },
      { id: 8, act: "act2", icon: "🪞", tag: "MIRROR TEXT", name: "Specular_Reflection.doc", desc: "Axis Inversion Recovery" },
      { id: 9, act: "act2", icon: "🧭", tag: "ROT-MATRIX", name: "Caesar_Substitution.mat", desc: "Index Shift Substitution" },
      { id: 10, act: "act2", icon: "🔢", tag: "DIGITAL ROOT", name: "Digital_Root_Log.txt", desc: "Base-Invariant Arithmetic" },
      { id: 11, act: "act2", icon: "🔁", tag: "PALINDROME", name: "Palindrome_Stream.txt", desc: "Symmetric String Filter" },
      { id: 12, act: "act3", icon: "📐", tag: "DIAGONAL", name: "Matrix_Diagonal.pdf", desc: "Diagonal String Weave" },
      { id: 13, act: "act3", icon: "📏", tag: "PERIMETER", name: "Grid_Perimeter.pdf", desc: "Boundary Box Quant" },
      { id: 14, act: "act3", icon: "🏁", tag: "CHECKER", name: "Checker_State.png", desc: "Grid Parity Evaluation" },
      { id: 15, act: "act3", icon: "⭕", tag: "RING CIPHER", name: "Ring_Shift.png", desc: "Concentric Modulo Shift" },
      { id: 16, act: "act3", icon: "🔴", tag: "RED QUESTION", name: "Cipher_Wheel_Spec.pdf", desc: "Grand Master Protocol" },
      { id: 17, act: "act3", icon: "🌳", tag: "FAILSAFE LOGIC", name: "Failsafe_Gate_Status.pdf", desc: "Final 4-Switch Hardware Gate" }
    ];'''

if old_r2_cards in text:
    text = text.replace(old_r2_cards, new_r2_cards)
    print("Updated R2_CARD_DEFINITIONS")
else:
    print("Warning: old_r2_cards not found")

# 3. Update R2_ANSWERS in submitRound2Code
old_r2_answers = '''      const R2_ANSWERS = {
        1: ["C", "OPTION C", "THREE CIRCLES", "3 CIRCLES", "●●●", "CIRCLES", "THREE", "THREECIRCLES"],
        2: ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT", "LOWER LEFT"],
        3: ["5", "FIVE", "FACE 5", "FACE5"],
        4: ["CIPHER"],
        5: ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        6: ["011", "0,1,1", "0-1-1"],
        7: ["CLEARANCE"],
        8: ["SE", "SOUTH EAST", "SOUTHEAST"],
        9: ["NONE", "IMPOSSIBLE", "NO PRIME", "0"],
        10: ["RLRCK"],
        11: ["NODC"],
        12: ["102", "102 BOXES"],
        13: ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        14: ["FINALS", "EBF"],
        15: ["ECLIPSE"]
      };'''

new_r2_answers = '''      const R2_ANSWERS = {
        1: ["GUARD"],
        2: ["C", "OPTION C", "THREE CIRCLES", "3 CIRCLES", "●●●", "CIRCLES", "THREE", "THREECIRCLES"],
        3: ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT", "LOWER LEFT"],
        4: ["5", "FIVE", "FACE 5", "FACE5"],
        5: ["CIPHER"],
        6: ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        7: ["011", "0,1,1", "0-1-1"],
        8: ["CLEARANCE"],
        9: ["SE", "SOUTH EAST", "SOUTHEAST"],
        10: ["NONE", "IMPOSSIBLE", "NO PRIME", "0"],
        11: ["RLRCK"],
        12: ["NODC"],
        13: ["102", "102 BOXES"],
        14: ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        15: ["FINALS", "EBF"],
        16: ["ECLIPSE"],
        17: ["0110"]
      };'''

if old_r2_answers in text:
    text = text.replace(old_r2_answers, new_r2_answers)
    print("Updated R2_ANSWERS")
else:
    print("Warning: old_r2_answers not found")

# 4. Update round2CurrentStage < 15 to < 17
text = text.replace('if (round2CurrentStage < 15) {', 'if (round2CurrentStage < 17) {')

# 5. Update R2 progress and headers from 15 to 17
text = text.replace('Math.round((clearedCount / 15) * 100)', 'Math.round((clearedCount / 17) * 100)')
text = text.replace('${clearedCount} / 15 CLEARED', '${clearedCount} / 17 CLEARED')
text = text.replace('0 / 15 CLEARED', '0 / 17 CLEARED')
text = text.replace('15 OLYMPIAD CIPHER', '17 STRATCOM CIPHER')
text = text.replace('15 PUZZLES', '17 PUZZLES')

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved R2 base updates to aditi_os_widget.html")
