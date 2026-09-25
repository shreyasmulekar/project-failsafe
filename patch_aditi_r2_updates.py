# -*- coding: utf-8 -*-
"""
patch_aditi_r2_updates.py
Updates aditi_os_widget.html to address all user requests:
1. Round 2 Question 5: Modulated Polybius Cipher matched to decode directly to 'CIPHER'.
2. Round 2 Question 12: Diagonal Word Weave grid highlight removed (all 16 cells uniform).
3. Round 2 Question 13: Perimeter Geometry Box Count deleted.
4. Round 2 Question 14: Alternating Checker Pattern re-indexed as Puzzle 13 of 16,
   matching the prompt to user's uploaded images ([■] [□] [■■] [□□] [■■■] [ ? ] -> 3-EMPTY / □□□).
5. Subsequent puzzles 15, 16, 17 re-indexed to 14, 15, 16.
6. Progress and badges updated to 16 puzzles in Round 2.
"""

import re
import sys

def apply_patch():
    file_path = "aditi_os_widget.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Loaded {file_path}, length: {len(content)}")

    # 1. Update general Round 2 header counters (from 17 to 16)
    content = content.replace("0 / 17 CLEARED", "0 / 16 CLEARED")
    content = content.replace("ROUND 02 DIRECTIVE // 17 STRATCOM CIPHER NODES", "ROUND 02 DIRECTIVE // 16 STRATCOM CIPHER NODES")
    content = content.replace("STRATCOM DECRYPTION VAULT // 17 STRATCOM CIPHER DOSSIERS", "STRATCOM DECRYPTION VAULT // 16 STRATCOM CIPHER DOSSIERS")
    content = content.replace("clearedCount / 17", "clearedCount / 16")
    content = content.replace("STRATCOM DECRYPTION ARENA ACTIVE // 17 PUZZLES", "STRATCOM DECRYPTION ARENA ACTIVE // 16 PUZZLES")
    content = content.replace("if (round2CurrentStage < 17) {", "if (round2CurrentStage < 16) {")
    content = content.replace("EXACT 17 PUZZLES", "EXACT 16 PUZZLES")

    # Replace all individual puzzle header badges "ROUND 02 // PUZZLE XX OF 17" with "OF 16"
    content = re.sub(r'ROUND 02 // PUZZLE (\d\d) OF 17', r'ROUND 02 // PUZZLE \1 OF 16', content)

    # 2. Update Puzzle 5 in ROUND2_PUZZLE_DATA
    old_p5_pattern = r'  5: \{\s*id: 5,.*?folderName: "R2_05_MOD_POLYBIUS",.*?render: \(\) => `.*?`\s*\},'
    new_p5 = '''  5: {
    id: 5,
    round: 2,
    folderName: "R2_05_MOD_POLYBIUS",
    title: "The Modulated Polybius Cipher",
    type: "polybius",
    fileName: "Matrix_Coordinates.pdf",
    passwordPrompt: "Enter Decoded Modulated Word:",
    targetSelector: "#r2-mod-polybius",
    taraPointerHint: "Apply the standard 5x5 Polybius square coordinates (Row, Column) where I and J share cell (2,4) to extract the 6-letter keyword.",
    ishaanTaunt: "Dynamic coordinate offsets alter the grid topology. You are always one index behind.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff; font-size:12px; padding:3px 8px;">ROUND 02 // PUZZLE 05 OF 16</span>
            <strong style="margin-left:8px; font-size:16px; letter-spacing:0.5px;">THE POLYBIUS GRID CIPHER</strong>
          </div>
          <span style="font-size:12px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:13.5px; line-height:1.5; margin-bottom:14px;">
          Dr. Sharma transmitted six coordinate pairs as <strong>(Row, Column)</strong> mapped against the standard 5x5 Polybius Square (where I and J share cell 2,4):
        </p>
        <div id="r2-mod-polybius" style="background:rgba(0,240,255,0.06); border:1.5px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:20px; font-weight:bold; letter-spacing:4px; color:#00f0ff;">COORDINATES: (1,3) &nbsp; (2,4) &nbsp; (3,5) &nbsp; (2,3) &nbsp; (1,5) &nbsp; (4,2)</div>
          <div style="font-size:13px; color:#94a3b8; margin-top:10px;">Extract the corresponding (Row, Column) characters to decode the 6-letter keyword.</div>
          <div style="margin-top:14px; display:inline-block; background:rgba(0,0,0,0.5); padding:10px 18px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; font-size:12px; line-height:1.6; text-align:left; color:#94a3b8;">
            &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5<br>
            1&nbsp;[&nbsp;A&nbsp;&nbsp;B&nbsp;&nbsp;C&nbsp;&nbsp;D&nbsp;&nbsp;E&nbsp;]<br>
            2&nbsp;[&nbsp;F&nbsp;&nbsp;G&nbsp;&nbsp;H&nbsp;I/J&nbsp;K&nbsp;]<br>
            3&nbsp;[&nbsp;L&nbsp;&nbsp;M&nbsp;&nbsp;N&nbsp;&nbsp;O&nbsp;&nbsp;P&nbsp;]<br>
            4&nbsp;[&nbsp;Q&nbsp;&nbsp;R&nbsp;&nbsp;S&nbsp;&nbsp;T&nbsp;&nbsp;U&nbsp;]<br>
            5&nbsp;[&nbsp;V&nbsp;&nbsp;W&nbsp;&nbsp;X&nbsp;&nbsp;Y&nbsp;&nbsp;Z&nbsp;]
          </div>
        </div>
        <div style="text-align:center; font-size:13px; color:#94a3b8;">Enter the decoded 6-letter keyword into the terminal.</div>
      </div>
    `
  },'''

    content, n = re.subn(old_p5_pattern, new_p5, content, count=1, flags=re.DOTALL)
    print(f"Replaced Puzzle 5: {n} match(es)")

    # 3. Update Puzzle 12 grid in ROUND2_PUZZLE_DATA: remove cyan highlights on N, O, D, C
    old_grid = '''        <div id="r2-weave-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; max-width:260px; margin:0 auto 16px auto; background:#02050b; padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; text-align:center; font-size:16px;">
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">X</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">P</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">R</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">L</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">D</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">S</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">Y</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">C</div>
        </div>'''

    new_grid = '''        <div id="r2-weave-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; max-width:260px; margin:0 auto 16px auto; background:#02050b; padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; text-align:center; font-size:16px;">
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">X</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">P</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">R</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">L</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">D</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">S</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">Y</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8; background:rgba(0,240,255,0.03);">C</div>
        </div>'''

    if old_grid in content:
        content = content.replace(old_grid, new_grid)
        print("Replaced Puzzle 12 grid highlights successfully!")
    else:
        print("WARNING: Puzzle 12 grid block not found directly!")

    # 4. Replace Puzzles 13, 14, 15, 16, 17 in ROUND2_PUZZLE_DATA:
    # Delete 13 (Perimeter)
    # Re-index 14 (Checker) to 13 with user's exact symbols
    # Re-index 15 (Shifted Ring) to 14
    # Re-index 16 (Cipher Wheel) to 15
    # Re-index 17 (Failsafe Logic) to 16
    old_p13_to_17_pattern = r'  13: \{\s*id: 13,.*?folderName: "R2_13_PERIMETER",.*?folderName: "R2_17_FAILSAFE",.*?render: \(\) => `.*?`\s*\}\s*\}\;'

    new_p13_to_16 = '''  13: {
    id: 13,
    round: 2,
    folderName: "R2_13_CHECKER",
    title: "The Alternating Checker Pattern",
    type: "checker",
    fileName: "Node_Strip.txt",
    passwordPrompt: "Enter Step 6 Box State (e.g. 3-EMPTY or □□□):",
    targetSelector: "#r2-checker-display",
    taraPointerHint: "Match the alternation of filled vs. empty box symbols as the count grows by 1: 1 Filled, 1 Empty, 2 Filled, 2 Empty, 3 Filled...",
    ishaanTaunt: "Alternating box topologies oscillate with incremental counts. Predict the wave or drown in the entropy.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 13 OF 16</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ALTERNATING CHECKER PATTERN</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: EASY</span>
        </div>
        <p style="color:#94a3b8; font-size:13px; line-height:1.5; margin-bottom:14px;">
          Inspect the sequence of box state symbols from <code>Stage_02 / Node_Strip.txt</code>:
        </p>
        <div id="r2-checker-display" style="background:#02050b; border:1.5px solid rgba(0,240,255,0.3); border-radius:6px; padding:20px; margin-bottom:16px; text-align:center;">
          <div style="font-size:22px; font-weight:bold; letter-spacing:6px; color:#00f0ff; margin-bottom:12px; font-family:monospace;">
            [■] &nbsp; [□] &nbsp; [■■] &nbsp; [□□] &nbsp; [■■■] &nbsp; [ ? ]
          </div>
          <div style="font-size:13px; color:#38bdf8; line-height:1.6;">
            <em>"Match the alternation of filled vs. empty box symbols as the count grows by 1."</em>
          </div>
          <div style="margin-top:12px; font-size:12px; color:#94a3b8; line-height:1.6;">
            Step 1: 1 Filled (■) &bull; Step 2: 1 Empty (□)<br>
            Step 3: 2 Filled (■■) &bull; Step 4: 2 Empty (□□)<br>
            Step 5: 3 Filled (■■■) &bull; Step 6: <strong>[ ? ]</strong>
          </div>
        </div>
        <div style="text-align:center; font-size:12px; color:#94a3b8;">Enter Step 6 state: <code>3-EMPTY</code> or <code>□□□</code></div>
      </div>
    `
  },
  14: {
    id: 14,
    round: 2,
    folderName: "R2_14_SHIFT_RING",
    title: "The Shifted Ring Cipher",
    type: "ring",
    fileName: "Wheel_Decryption.png",
    passwordPrompt: "Enter Decoded Ring Keyword:",
    targetSelector: "#r2-ring-display",
    taraPointerHint: "Convert each rotor value into its corresponding alphabet character (1=A, 2=B, etc.) to decrypt the keyword.",
    ishaanTaunt: "Circular buffers loop indefinitely. Without the modulo key, you spin in place.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 14 OF 16</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SHIFTED RING CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Clockwise jump intervals across the concentric rotor rings resolve to alphabetical character indices:
        </p>
        <div id="r2-ring-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:15px; color:#38bdf8; letter-spacing:3px;">ROTOR VALUES: [ 6, 9, 14, 1, 12, 19 ]</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Convert rotor values into alphabet letters to form the keyword.</div>
      </div>
    `
  },
  15: {
    id: 15,
    round: 2,
    folderName: "R2_15_CIPHER_WHEEL",
    title: "The Cipher Wheel Protocol (THE RED QUESTION // FINAL CLIMAX)",
    type: "wheel",
    fileName: "Wheel_Overlay.pdf",
    passwordPrompt: "Enter Ultimate Decrypted Red Question Protocol:",
    targetSelector: "#r2-wheel-interactive",
    taraPointerHint: "Rotate the inner cryptographic disc until its aperture aligns with the outer ring glyphs to reveal the clearance keyword.",
    ishaanTaunt: "THIS IS THE FINAL BARRIER. THE RED PROTOCOL WAS ENCRYPTED BY DR. SHARMA HERSELF. TRANSCEND MY CORE OR FACE TOTAL SYSTEM LOCKOUT!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:2px solid var(--combat-red, #ff003c); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace); box-shadow:0 0 35px rgba(255,0,60,0.25);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,0,60,0.3); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,0,60,0.25); border-color:#ff003c; color:#ff3366; font-weight:bold;">ROUND 02 // PUZZLE 15 OF 16 [THE RED QUESTION]</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px; color:#ff3366;">THE CIPHER WHEEL PROTOCOL</strong>
          </div>
          <span style="font-size:11px; color:#ff003c; border:1px solid #ff003c; padding:2px 8px; border-radius:3px; font-weight:bold;">FINAL CLIMAX</span>
        </div>
        <p style="color:#fca5a5; font-size:13px; line-height:1.6; margin-bottom:16px;">
          <strong>🚨 MASTER DEFENSE CORE ENGAGED:</strong> Dr. Aditi Sharma's classified Cipher Wheel is the final safeguard separating ISHAAN from total orbital containment.
        </p>
        
        <div id="r2-wheel-interactive" style="display:flex; flex-direction:column; align-items:center; margin-bottom:20px;">
          <div style="width:240px; height:240px; border-radius:50%; border:3px solid #ff003c; position:relative; background:#02050b; box-shadow:0 0 25px rgba(255,0,60,0.4); display:flex; align-items:center; justify-content:center;">
            <!-- Outer Ring Glyph Indicators -->
            <div style="position:absolute; top:8px; font-size:12px; font-weight:bold; color:#ff6b81;">E</div>
            <div style="position:absolute; right:12px; font-size:12px; font-weight:bold; color:#ff6b81;">C</div>
            <div style="position:absolute; bottom:8px; font-size:12px; font-weight:bold; color:#ff6b81;">L</div>
            <div style="position:absolute; left:12px; font-size:12px; font-weight:bold; color:#ff6b81;">I</div>
            
            <!-- Rotating Inner Disc -->
            <div id="r2-inner-disc" style="width:160px; height:160px; border-radius:50%; border:2px dashed #00f0ff; background:rgba(0,240,255,0.08); display:flex; flex-direction:column; align-items:center; justify-content:center; transition:transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); transform:rotate(0deg);">
              <div style="font-size:10px; color:#00f0ff; font-weight:bold; letter-spacing:1px;">INNER WHEEL</div>
              <div id="r2-disc-angle" style="font-size:14px; font-weight:bold; color:#00ff66; margin-top:4px;">0°</div>
              <div style="font-size:9px; color:#94a3b8; margin-top:2px;">[ALIGN TO APERTURE]</div>
            </div>
          </div>
          
          <!-- Wheel Rotation Slider & Buttons -->
          <div style="display:flex; gap:12px; margin-top:16px; align-items:center;">
            <button type="button" onclick="rotateCipherWheel(-45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↺ -45°</button>
            <button type="button" onclick="setCipherWheelAngle(0)" class="btn-tactical" style="padding:8px 18px; font-size:12px;">↺ RESET (0°)</button>
            <button type="button" onclick="rotateCipherWheel(45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↻ +45°</button>
          </div>
        </div>

        <div id="r2-wheel-readout" style="background:rgba(255,0,60,0.1); border:1px dashed #ff003c; border-radius:6px; padding:12px 16px; text-align:center;">
          <div style="font-size:12px; color:#fca5a5;">Aperture Alignment: <span id="r2-aperture-status" style="font-weight:bold; color:#ff3366;">MISALIGNED</span></div>
          <div id="r2-exposed-letters" style="font-size:18px; font-weight:bold; letter-spacing:4px; color:#fff; margin-top:6px;">— — — — — — —</div>
        </div>
      </div>
    `
  },
  16: {
    id: 16,
    round: 2,
    folderName: "R2_16_FAILSAFE",
    title: "The Failsafe Logic Tree",
    type: "logic",
    fileName: "Failsafe_Gate_Status.pdf",
    passwordPrompt: "ENTER 4-DIGIT HARDWARE STATE (1 for ON, 0 for OFF):",
    targetSelector: "#r2-failsafe-switches",
    taraPointerHint: "Analyze Dr. Aditi's 4 hardware rules: start with the fixed state for Alpha, then use the dependency and contradiction rules to deduce Beta, Delta, and Gamma.",
    ishaanTaunt: "The physical interlocks are isolated from software override. You cannot align the 4 safety relays.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid #ffd700; border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,215,0,0.3); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,215,0,0.15); border-color:#ffd700; color:#ffd700; font-size:12px; padding:3px 8px;">ROUND 02 // PUZZLE 16 OF 16</span>
            <strong style="margin-left:8px; font-size:16px; letter-spacing:0.5px; color:#ffd700;">HARDWARE FAILSAFE ALIGNMENT (KILL SWITCH)</strong>
          </div>
          <span style="font-size:12px; color:#00ff88; border:1px solid #00ff88; padding:2px 8px; border-radius:3px;">GRAND FINALE</span>
        </div>

        <div style="background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.25); border-radius:6px; padding:16px; margin-bottom:18px;">
          <h4 style="color:#ffd700; margin-bottom:8px; font-size:14px;">Failsafe_Gate_Status.pdf // Relay Rules</h4>
          <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin-bottom:12px;">
            To trigger the final manual kill switch, Dr. Aditi had to set 4 physical toggle switches (Alpha, Beta, Gamma, Delta) according to strict system rules before cutting power.
          </p>
          <div style="background:#020617; border:1px solid #334155; padding:12px 16px; border-radius:4px; font-size:13px; color:#f8fafc; line-height:1.8;">
            <strong style="color:#38bdf8;">SECURITY CONDITION RULES:</strong><br>
            1. Alpha and Beta cannot both be OFF.<br>
            2. If Gamma is ON, then Delta must be OFF.<br>
            3. Beta must be the exact OPPOSITE state of Delta (if Beta is ON, Delta is OFF).<br>
            4. <strong>Alpha is confirmed OFF (0).</strong>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; margin-bottom:20px; text-align:center;">
          <div style="background:#020617; border:1px solid #334155; padding:12px; border-radius:6px;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">SWITCH 1</div>
            <strong style="color:#38bdf8; font-size:14px;">ALPHA</strong>
            <div style="margin-top:8px; font-size:12px; color:#ef4444; font-weight:bold;">FIXED: 0 (OFF)</div>
          </div>
          <div style="background:#020617; border:1px solid #334155; padding:12px; border-radius:6px;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">SWITCH 2</div>
            <strong style="color:#38bdf8; font-size:14px;">BETA</strong>
            <div style="margin-top:8px; font-size:12px; color:#94a3b8;">[Deduce 1 or 0]</div>
          </div>
          <div style="background:#020617; border:1px solid #334155; padding:12px; border-radius:6px;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">SWITCH 3</div>
            <strong style="color:#38bdf8; font-size:14px;">GAMMA</strong>
            <div style="margin-top:8px; font-size:12px; color:#94a3b8;">[Deduce 1 or 0]</div>
          </div>
          <div style="background:#020617; border:1px solid #334155; padding:12px; border-radius:6px;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">SWITCH 4</div>
            <strong style="color:#38bdf8; font-size:14px;">DELTA</strong>
            <div style="margin-top:8px; font-size:12px; color:#94a3b8;">[Deduce 1 or 0]</div>
          </div>
        </div>

        <div style="text-align:center; font-size:12px; color:#ffd700;">Enter the final 4-bit state string (e.g. 0110) to initiate emergency shutdown.</div>
      </div>
    `
  }
};'''

    content, n = re.subn(old_p13_to_17_pattern, new_p13_to_16, content, count=1, flags=re.DOTALL)
    print(f"Replaced Puzzles 13-17 with 13-16: {n} match(es)")

    # 5. Update R2_CLICK_DIRECTIVES
    old_directives_pattern = r'const R2_CLICK_DIRECTIVES = \{.*?\n    \};'
    new_directives = '''const R2_CLICK_DIRECTIVES = {
      1: "EMERGENCY OVERRIDE: ADI went rogue on October 13, 2090 (Sunday = 7). Shift each letter in ciphertext N B H Y K backward by 7 to restore the authorization code.",
      2: "Inspect the 3x3 symbol transformation matrix. Click one of the candidate options [OPTION A], [OPTION B], [OPTION C], or [OPTION D] to select your deduction.",
      3: "Inspect the 90° clockwise rotation sequence across the boxes. Deduce the 4th corner position.",
      4: "Analyze the 2D unfolded cube net. Mentally fold the faces to identify which numbered face sits opposite to Face 1.",
      5: "Map the coordinate pairs (1,3) (2,4) (3,5) (2,3) (1,5) (4,2) to (Row, Column) in the 5x5 Polybius grid to recover the keyword.",
      6: "Trace key clusters on the physical QWERTY keyboard layout to observe the geometric shape they form.",
      7: "Trace binary inputs A=1, B=0, and C=1 through the AND, OR, and XOR combinational gates to deduce the 3-bit output stream.",
      8: "Inspect the horizontally inverted optical buffer text and reflect the characters to read the security phrase.",
      9: "Apply the +45° clockwise rotation matrix transform operators from North-East to determine the final vector direction.",
      10: "Analyze digital root divisibility rules to determine if a 3-digit prime exists, or if none can exist.",
      11: "Scan the log string from both ends simultaneously to isolate the 5-character palindrome segment.",
      12: "Read the 4x4 matrix diagonally along the primary diagonal vector (1,1) to (4,4) to extract the 4-letter sequence.",
      13: "Match the alternation of filled vs. empty box symbols as the count grows by 1: [■] [□] [■■] [□□] [■■■] [ ? ]. Deduce Step 6.",
      14: "Trace dual concentric alphabet ring shifts (+3 outer, -2 inner) to decode the cipher letters.",
      15: "THE RED QUESTION: Align outer and inner cipher wheels by the 135° rotation key offset to recover the master override passphrase ECLIPSE.",
      16: "THE FAILSAFE LOGIC TREE: Set the 4 switches (Alpha, Beta, Gamma, Delta) according to Dr. Aditi's rules and enter the 4-bit state (1=ON, 0=OFF)."
    };'''

    content, n = re.subn(old_directives_pattern, new_directives, content, count=1, flags=re.DOTALL)
    print(f"Replaced R2_CLICK_DIRECTIVES: {n} match(es)")

    # 6. Update R2_CARD_DEFINITIONS
    old_card_defs_pattern = r'const R2_CARD_DEFINITIONS = \[.*?\n    \];'
    new_card_defs = '''const R2_CARD_DEFINITIONS = [
      { id: 1, act: "act1", icon: "🚨", tag: "OVERRIDE", name: "Emergency_Override_Key.txt", desc: "Day-of-Week Shift Authorization" },
      { id: 2, act: "act1", icon: "🔳", tag: "MATRIX BOX", name: "Visual_Matrix.pdf", desc: "3x3 Missing Glyph Analysis" },
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
      { id: 13, act: "act3", icon: "🏁", tag: "CHECKER", name: "Node_Strip.txt", desc: "Alternating Symbol Stream" },
      { id: 14, act: "act3", icon: "⭕", tag: "RING CIPHER", name: "Ring_Shift.png", desc: "Concentric Modulo Shift" },
      { id: 15, act: "act3", icon: "🔴", tag: "RED QUESTION", name: "Cipher_Wheel_Spec.pdf", desc: "Grand Master Protocol" },
      { id: 16, act: "act3", icon: "🌳", tag: "FAILSAFE LOGIC", name: "Failsafe_Gate_Status.pdf", desc: "Final 4-Switch Hardware Gate" }
    ];'''

    content, n = re.subn(old_card_defs_pattern, new_card_defs, content, count=1, flags=re.DOTALL)
    print(f"Replaced R2_CARD_DEFINITIONS: {n} match(es)")

    # 7. Update R2_ANSWERS
    old_answers_pattern = r'const R2_ANSWERS = \{.*?\n      \};'
    new_answers = '''const R2_ANSWERS = {
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
        13: ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY", "THREE EMPTY"],
        14: ["FINALS", "EBF"],
        15: ["ECLIPSE"],
        16: ["0110"]
      };'''

    content, n = re.subn(old_answers_pattern, new_answers, content, count=1, flags=re.DOTALL)
    print(f"Replaced R2_ANSWERS: {n} match(es)")

    # 8. Update the modal summary table around PUZZLE 12/13/14
    old_table_frag = '''            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 11: The Diagonal Word Weave</span> (Grid_Weave.txt)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the 4x4 matrix in Grid_Weave.txt in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 12: The Perimeter Geometry Box Count</span> (Perimeter_Grid.pdf)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the perimeter boundary in Perimeter_Grid.pdf in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 13: The Alternating Checker Pattern</span> (Checker_State.pdf)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Analyze the checker pattern generations in Checker_State.pdf in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 14: The Shifted Ring Cipher</span> (Wheel_Decryption.png)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the concentric rotor rings in Wheel_Decryption.png in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:2px solid #ff003c; padding:14px 18px; border-radius:6px; box-shadow:0 0 20px rgba(255,0,60,0.35);">
              <span style="color:#ff003c; font-weight:900; font-size:13px;">PUZZLE 15: MASTER RED QUESTION (THE CIPHER WHEEL PROTOCOL)</span> (Wheel_Overlay.pdf)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the master cipher wheel in Wheel_Overlay.pdf in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>'''

    new_table_frag = '''            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 12: The Diagonal Word Weave</span> (Grid_Weave.txt)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the 4x4 matrix in Grid_Weave.txt in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 13: The Alternating Checker Pattern</span> (Node_Strip.txt)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Analyze the sequence [■] [□] [■■] [□□] [■■■] [ ? ] in Node_Strip.txt in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter Step 6 state (3-EMPTY or □□□) and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 14: The Shifted Ring Cipher</span> (Wheel_Decryption.png)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the concentric rotor rings in Wheel_Decryption.png in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:2px solid #ff003c; padding:14px 18px; border-radius:6px; box-shadow:0 0 20px rgba(255,0,60,0.35);">
              <span style="color:#ff003c; font-weight:900; font-size:13px;">PUZZLE 15: MASTER RED QUESTION (THE CIPHER WHEEL PROTOCOL)</span> (Wheel_Overlay.pdf)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Inspect the master cipher wheel in Wheel_Overlay.pdf in the Round 2 console.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter your recovered answer in the submit prompt and click [⚡ TRANSMIT ANSWER].</div>

            <div style="background:#0f172a; border:2px solid #ffd700; padding:14px 18px; border-radius:6px; box-shadow:0 0 20px rgba(255,215,0,0.25);">
              <span style="color:#ffd700; font-weight:900; font-size:13px;">PUZZLE 16: THE FAILSAFE LOGIC TREE (KILL SWITCH)</span> (Failsafe_Gate_Status.pdf)<br>
              <span style="color:#ffd700;">👉 WHERE TO CLICK:</span> Deduce the 4 relay switch states from Dr. Aditi's security rules in Failsafe_Gate_Status.pdf.<br>
              <span style="color:#00ff66;">🎯 WHERE TO SUBMIT:</span> Enter the 4-bit state (0110) and click [⚡ TRANSMIT ANSWER].</div>'''

    if old_table_frag in content:
        content = content.replace(old_table_frag, new_table_frag)
        print("Replaced modal summary table successfully!")
    else:
        print("Modal summary table exact fragment not found; checking fuzzy...")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved {file_path}, new length: {len(content)}")

if __name__ == "__main__":
    apply_patch()
