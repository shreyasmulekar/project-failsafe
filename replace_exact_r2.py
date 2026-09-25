import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_d = text.find('const R2_CLICK_DIRECTIVES = {')
idx_d_end = text.find('};', idx_d) + 2

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

text = text[:idx_d] + new_r2_directives + text[idx_d_end:]

idx_c = text.find('const R2_CARD_DEFINITIONS = [')
idx_c_end = text.find('];', idx_c) + 2

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

text = text[:idx_c] + new_r2_cards + text[idx_c_end:]

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Exact replacement of R2_CLICK_DIRECTIVES and R2_CARD_DEFINITIONS succeeded!")
