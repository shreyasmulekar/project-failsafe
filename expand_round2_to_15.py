# expand_round2_to_15.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    text = f.read()

# Build the 15-question dictionary for ROUND2_PUZZLE_DATA
puzzles_15_code = '''const ROUND2_PUZZLE_DATA = {
  1: {
    id: 1,
    round: 2,
    folderName: "R2_01_MATRIX",
    title: "Visual Matrix Box Transformation",
    type: "matrix",
    fileName: "Visual_Matrix.pdf",
    passwordPrompt: "Select Missing Transformation (e.g. C):",
    targetSelector: "#target-matrix-unknown",
    taraPointerHint: "Inspect the 3x3 matrix in the center panel. Notice how shapes stay consistent along rows (Row 3 = Circles), and quantities grow along columns. Col 3 must have 3 Circles (Option C)!",
    ishaanTaunt: "A simple visual grid stumbles human perception. You cannot decipher what you cannot compute.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 01 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE MATRIX BOX TRANSFORMATION</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -20 PTS</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          Evaluate the 3x3 visual transformation matrix. Deduce the missing symbol in <strong>Row 3, Column 3</strong>:
        </p>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; max-width:440px; margin:0 auto 20px auto; background:rgba(0,0,0,0.5); padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:8px;">
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲ ▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■ ■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">●</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">● ●</div>
          <div id="target-matrix-unknown" style="background:rgba(255,0,60,0.15); border:2px dashed var(--combat-red, #ff003c); padding:14px; text-align:center; font-size:20px; font-weight:bold; color:var(--combat-red, #ff003c); animation:pulse-strobe 1.5s infinite;">?</div>
        </div>
        <div id="r2-matrix-options" style="background:rgba(0,240,255,0.04); border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:#00f0ff; font-weight:bold; margin-bottom:8px; letter-spacing:0.8px;">SELECT CANDIDATE TRANSFORMATION:</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <button type="button" onclick="selectRound2Option('A')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION A:</strong> [ ● ]</span></button>
            <button type="button" onclick="selectRound2Option('B')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION B:</strong> [ ■ ■ ■ ]</span></button>
            <button type="button" onclick="selectRound2Option('C')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION C:</strong> [ ● ● ● ]</span></button>
            <button type="button" onclick="selectRound2Option('D')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION D:</strong> [ ▲ ▲ ▲ ]</span></button>
          </div>
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    round: 2,
    folderName: "R2_02_ROTATION",
    title: "Clockwise Rotation Boxes (Spatial 90°)",
    type: "rotation",
    fileName: "Rotation_Array.pdf",
    passwordPrompt: "Enter Missing Corner Location (e.g. BOTTOM LEFT or BL):",
    targetSelector: "#r2-rotation-sequence",
    taraPointerHint: "Trace the white dot: Box 1 is Top-Left, Box 2 is Top-Right, Box 3 is Bottom-Right. It shifts 90 degrees clockwise each step. Next is BOTTOM LEFT (BL)!",
    ishaanTaunt: "Rotational kinematics. A basic satellite alignment protocol that humans frequently invert.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 02 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE CLOCKWISE ROTATION BOXES</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          <em>"Trace the movement of the core node as it rotates 90° clockwise through the terminal array."</em>
        </p>
        <div id="r2-rotation-sequence" style="display:flex; gap:14px; justify-content:center; align-items:center; margin-bottom:20px; flex-wrap:wrap;">
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 1 (TL)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; left:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 2 (TR)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; right:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 3 (BR)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; bottom:8px; right:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#ff003c; margin-bottom:4px; font-weight:bold;">BOX 4 (?)</div><div style="width:70px; height:70px; border:2px dashed #ff003c; background:rgba(255,0,60,0.1); position:relative; border-radius:4px; display:flex; align-items:center; justify-content:center; color:#ff003c; font-weight:bold; font-size:18px;">?</div></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 4th position: <code>BOTTOM LEFT</code> (or <code>BL</code>)</div>
      </div>
    `
  },

  3: {
    id: 3,
    round: 2,
    folderName: "R2_03_CUBE",
    title: "Spatial Net Folding Box (3D Cube)",
    type: "cube",
    fileName: "Cube_Net_Terminal.pdf",
    passwordPrompt: "Enter Digit Opposite to Face 1:",
    targetSelector: "#r2-cube-net-container",
    taraPointerHint: "In the vertical line 1, 3, 5, 6: faces separated by one box fold into opposite sides. Box 1 and Box 5 are separated by Box 3 -> Face 1 is opposite Face 5!",
    ishaanTaunt: "Topology manipulation. Can biological minds fold 2D planes into 3D manifolds in memory?",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 03 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SPATIAL NET FOLDING BOX</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -15 PTS</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          To re-establish the hardware core, analyze the flattened 2D paper net of the 6-sided hardware cube containing digits 1 through 6:
        </p>
        <div id="r2-cube-net-container" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; display:flex; flex-direction:column; align-items:center; margin-bottom:16px;">
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.12);">1</div>
          <div style="display:flex;">
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">2</div>
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">3</div>
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">4</div>
          </div>
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">5</div>
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">6</div>
        </div>
        <div style="background:rgba(0,240,255,0.06); border-left:3px solid #00f0ff; padding:10px 14px; font-size:12px; color:#e2e8f0;">
          <strong>QUESTION:</strong> Which face will be <strong>opposite to face 1</strong>? (Enter digit: <code>5</code>)
        </div>
      </div>
    `
  },

  4: {
    id: 4,
    round: 2,
    folderName: "R2_04_WHITEOUT",
    title: "The Whiteout Signature (Steganography)",
    type: "whiteout",
    fileName: "Emergency_Log.doc",
    passwordPrompt: "Enter Revealed Clearance Token:",
    targetSelector: "#r2-whiteout-card",
    taraPointerHint: "Select all text or toggle the UV filter. Hidden white text on white canvas reveals the passphrase: CLEARANCE_ALPHA!",
    ishaanTaunt: "Steganography is invisible to uncalibrated optics. You see only empty void.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 04 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE WHITEOUT SIGNATURE</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Dr. Aditi masked this document with invisible foreground styling. Highlight the text below or toggle UV Spectrum:
        </p>
        <div id="r2-whiteout-card" style="background:#ffffff; color:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:20px; font-family:sans-serif; font-size:14px; line-height:1.8; user-select:text; margin-bottom:16px;">
          [STRATCOM SECURITY DIRECTIVE 90-A]<br>
          ALL SUBSYSTEM ACCESS RESTRICTED UNDER ECLIPSE PROTOCOL.<br>
          <span style="color:#ffffff;">CLEARANCE_KEY = CLEARANCE_ALPHA</span><br>
          OPERATOR STATUS: VERIFIED AUTHENTIC.
        </div>
        <div style="display:flex; justify-content:center; gap:10px;">
          <button type="button" onclick="document.getElementById('r2-whiteout-card').style.background='#0a101d'; document.getElementById('r2-whiteout-card').style.color='#00f0ff';" class="btn-action" style="padding:6px 14px; font-size:11px;">
            🔦 TOGGLE UV SPECTRUM FILTER
          </button>
        </div>
      </div>
    `
  },

  5: {
    id: 5,
    round: 2,
    folderName: "R2_05_ROT4",
    title: "The ROT-4 IEEE Shift Cipher",
    type: "rot4",
    fileName: "Encrypted_Beacon.txt",
    passwordPrompt: "Enter Decrypted Callsign (e.g. ADITIS13):",
    targetSelector: "#r2-rot4-card",
    taraPointerHint: "Shift each letter backward by 4 (the letter count of IEEE): EHMXMW13 -> E-4=A, H-4=D, M-4=I, X-4=T, M-4=I, W-4=S + 13 = ADITIS13!",
    ishaanTaunt: "Caesar shifts are millennia old. Yet you still require calculation time.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 05 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ROT-4 IEEE SHIFT</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Shift each character backward by the number of letters in <strong>'IEEE'</strong> (4 positions):
        </p>
        <div id="r2-rot4-card" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:24px; font-weight:bold; letter-spacing:4px; color:#00f0ff;">EHMXMW13</div>
          <div style="font-size:11.5px; color:#94a3b8; margin-top:8px;">[ Shift Rule: Letter - 4 positions | Numeric suffix unaltered ]</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the decrypted callsign: <code>ADITIS13</code></div>
      </div>
    `
  },

  6: {
    id: 6,
    round: 2,
    folderName: "R2_06_ATBASH",
    title: "The Atbash Cipher Mirror",
    type: "atbash",
    fileName: "Mirror_Log.txt",
    passwordPrompt: "Enter Mirrored Word:",
    targetSelector: "#r2-atbash-card",
    taraPointerHint: "In Atbash, reverse alphabet: A <-> Z, B <-> Y, C <-> X. KILQVBG mirrors directly into PROJECT!",
    ishaanTaunt: "A mirror reflects reality inverted. You look into the glass and see only fragments.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 06 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ATBASH CIPHER MIRROR</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          <em>"Dr. Aditi mirrored her alphabet across the median. Reverse the alphabet: A &harr; Z, B &harr; Y."</em>
        </p>
        <div id="r2-atbash-card" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:26px; font-weight:bold; letter-spacing:6px; color:#00f0ff;">KILQVBG</div>
          <div style="font-size:11.5px; color:#cbd5e1; margin-top:8px;">[ K &harr; P, I &harr; R, L &harr; O, Q &harr; J, V &harr; E, B &harr; Y, G &harr; T ]</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the decoded project name: <code>PROJECT</code></div>
      </div>
    `
  },

  7: {
    id: 7,
    round: 2,
    folderName: "R2_07_POLYBIUS",
    title: "The Polybius Coordinate Trail",
    type: "polybius",
    fileName: "Matrix_Coordinates.pdf",
    passwordPrompt: "Enter Decoded Word (e.g. VECTOR):",
    targetSelector: "#r2-polybius-grid",
    taraPointerHint: "Map each pair as (Row, Column): (5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R -> VECTOR!",
    ishaanTaunt: "Cartesian spatial coordinates. A trivial lookup that humans still manage to misalign.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 07 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE POLYBIUS COORDINATE TRAIL</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Coordinate sequence: <strong>(5,1), (1,5), (1,3), (4,4), (3,4), (4,2)</strong>. Use standard (Row, Column) order:
        </p>
        <div id="r2-polybius-grid" style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px; max-width:320px; margin:0 auto 16px auto; background:#02050b; padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; text-align:center;">
          <div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">A</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">B</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">C (1,3)</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">D</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">E (1,5)</div>
          <div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">F</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">G</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">H</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">I</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">K</div>
          <div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">L</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">M</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">N</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">O (3,4)</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">P</div>
          <div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">Q</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">R (4,2)</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">S</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">T (4,4)</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">U</div>
          <div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00ff66; font-weight:bold;">V (5,1)</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">W</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">X</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">Y</div><div style="padding:6px; border:1px solid rgba(0,240,255,0.2); color:#00f0ff;">Z</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Decoded Vector Signal: <code>VECTOR</code></div>
      </div>
    `
  },

  8: {
    id: 8,
    round: 2,
    folderName: "R2_08_GATES",
    title: "Interlocking Logic Gate Flow",
    type: "gates",
    fileName: "Logic_Gate_Matrix.pdf",
    passwordPrompt: "Enter 3-Bit Output Stream (e.g. 011):",
    targetSelector: "#r2-logic-gates",
    taraPointerHint: "Trace binary streams A=1, B=0, C=1 through the AND, OR, and XOR gates. Output bus registers read 011!",
    ishaanTaunt: "Boolean algebra is my native tongue. For you, it is arithmetic hesitation.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 08 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">INTERLOCKING LOGIC GATE FLOW</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Three inputs feed an interlocking combinational circuit: <strong>Input A = 1, Input B = 0, Input C = 1</strong>.<br>
          Gate 1: [A AND B] &rarr; Output 1<br>
          Gate 2: [B OR C] &rarr; Output 2<br>
          Gate 3: [A XOR B] &rarr; Output 3
        </p>
        <div id="r2-logic-gates" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">[1 AND 0] = <strong style="color:#00ff66;">0</strong></div>
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">[0 OR 1] = <strong style="color:#00ff66;">1</strong></div>
          <div style="font-size:14px; color:#38bdf8;">[1 XOR 0] = <strong style="color:#00ff66;">1</strong></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 3-bit terminal register: <code>011</code></div>
      </div>
    `
  },

  9: {
    id: 9,
    round: 2,
    folderName: "R2_09_QWERTY",
    title: "The QWERTY Geometry Shape Trace",
    type: "qwerty",
    fileName: "Keyboard_Telemetry.pdf",
    passwordPrompt: "Enter Geometric Shape Formed (e.g. SQUARES):",
    targetSelector: "#r2-qwerty-display",
    taraPointerHint: "Plot key clusters [W-E-S-D], [R-T-F-G], [U-I-J-K] on the keyboard layout. Each 4-key cluster connects into SQUARES!",
    ishaanTaunt: "Physical keyboards: obsolete tactile inputs. Yet their spatial geometry still trips you.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 09 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">QWERTY GEOMETRY SHAPE TRACE</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Dr. Aditi bound her emergency keystrokes into geometric clusters on a standard QWERTY switchboard:
        </p>
        <div id="r2-qwerty-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#38bdf8; margin-bottom:6px;">Cluster 1: [W &rarr; E &rarr; D &rarr; S &rarr; W]</div>
          <div style="font-size:13px; color:#38bdf8; margin-bottom:6px;">Cluster 2: [R &rarr; T &rarr; G &rarr; F &rarr; R]</div>
          <div style="font-size:13px; color:#38bdf8;">Cluster 3: [U &rarr; I &rarr; K &rarr; J &rarr; U]</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">What geometric shape is traced by all three clusters? <code>SQUARES</code></div>
      </div>
    `
  },

  10: {
    id: 10,
    round: 2,
    folderName: "R2_10_MIRROR",
    title: "Mirror Image String Inversion",
    type: "mirror",
    fileName: "Reflection_Buffer.txt",
    passwordPrompt: "Enter Un-inverted Security String:",
    targetSelector: "#r2-mirror-string",
    taraPointerHint: "Flip the inverted character stream horizontally across the axis. The word reconstructs into CLEARANCE!",
    ishaanTaunt: "Inverted typography. Human optic nerves take 300 milliseconds to invert rasterized text.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 10 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">MIRROR IMAGE STRING INVERSION</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          An optical buffer was inverted horizontally during transmission. Reconstruct the original word:
        </p>
        <div id="r2-mirror-string" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:20px; text-align:center; margin-bottom:16px;">
          <div style="font-size:28px; font-weight:bold; letter-spacing:8px; color:#00f0ff; transform:scaleX(-1); display:inline-block;">
            CLEARANCE
          </div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter un-inverted word: <code>CLEARANCE</code></div>
      </div>
    `
  },

  11: {
    id: 11,
    round: 2,
    folderName: "R2_11_PALINDROME",
    title: "The Palindrome Filter Stream",
    type: "palindrome",
    fileName: "Spectral_Filter.log",
    passwordPrompt: "Enter Palindromic Center Sequence:",
    targetSelector: "#r2-pal-stream",
    taraPointerHint: "Isolate the symmetrical palindromic substrings in each telemetry packet. The center axis sequence is RLRCK!",
    ishaanTaunt: "Symmetry is mathematical beauty. Your search heuristics are crude and stochastic.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 11 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE PALINDROME FILTER STREAM</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Filter out asymmetric noise. Extract the 5 palindromic core tags embedded in the telemetry stream:
        </p>
        <div id="r2-pal-stream" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; font-family:monospace; font-size:13px; line-height:1.8; color:#cbd5e1; text-align:center;">
          Stream Tag 1: [A B <strong style="color:#00ff66;">R</strong> B A]<br>
          Stream Tag 2: [X Y <strong style="color:#00ff66;">L</strong> Y X]<br>
          Stream Tag 3: [M N <strong style="color:#00ff66;">R</strong> N M]<br>
          Stream Tag 4: [P Q <strong style="color:#00ff66;">C</strong> Q P]<br>
          Stream Tag 5: [J K <strong style="color:#00ff66;">K</strong> K J]
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 5 center symmetry markers: <code>RLRCK</code></div>
      </div>
    `
  },

  12: {
    id: 12,
    round: 2,
    folderName: "R2_12_PERIMETER",
    title: "Perimeter Geometry Box Count",
    type: "perimeter",
    fileName: "Perimeter_Grid.pdf",
    passwordPrompt: "Enter Total Perimeter Node Count:",
    targetSelector: "#r2-perimeter-grid",
    taraPointerHint: "Count the active boundary blocks along the 28x25 perimeter minus the 4 shared corners: (28*2 + 25*2 - 4) = 102 nodes!",
    ishaanTaunt: "Perimeter bounds. You focus on the interior and neglect the structural boundaries.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 12 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">PERIMETER GEOMETRY BOX COUNT</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          A defense array measures <strong>28 units in width</strong> and <strong>25 units in height</strong>. Each perimeter border cell houses an active security node.
        </p>
        <div id="r2-perimeter-grid" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#38bdf8;">Top: 28 nodes • Bottom: 28 nodes • Left: 23 nodes • Right: 23 nodes</div>
          <div style="font-size:15px; font-weight:bold; color:#00ff66; margin-top:8px;">Total Active Perimeter: 28 + 28 + 23 + 23 = 102</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the total perimeter node count: <code>102</code></div>
      </div>
    `
  },

  13: {
    id: 13,
    round: 2,
    folderName: "R2_13_CHECKER",
    title: "Alternating Checker Pattern",
    type: "checker",
    fileName: "Checker_State.pdf",
    passwordPrompt: "Enter 5th Generation Parity State (e.g. 3-EMPTY):",
    targetSelector: "#r2-checker-display",
    taraPointerHint: "Notice the alternating parity: Gen 1 has 1 empty, Gen 2 has 2 filled, Gen 3 has 2 empty, Gen 4 has 3 filled. Gen 5 must have 3 EMPTY boxes!",
    ishaanTaunt: "Cellular automata oscillate. Predict the wave or drown in the entropy.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 13 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">ALTERNATING CHECKER PATTERN</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Analyze the cyclic checker generations: Gen 1 (■), Gen 2 (□□), Gen 3 (■■), Gen 4 (□□□), Gen 5 (?):
        </p>
        <div id="r2-checker-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:18px; color:#00f0ff; letter-spacing:6px;">Gen 5 Parity: □ □ □ (3-EMPTY)</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 5th generation state: <code>3-EMPTY</code> (or <code>EMPTY</code>)</div>
      </div>
    `
  },

  14: {
    id: 14,
    round: 2,
    folderName: "R2_14_SEARCH",
    title: "Find-and-Replace Frequency Count",
    type: "search",
    fileName: "Mass_System_Log.txt",
    passwordPrompt: "Enter Computed Security Pin (Count × 100):",
    targetSelector: "#r2-log-search-tool",
    taraPointerHint: "Search for 'OVERRIDE' across the log. It appears exactly 14 times. Multiply by 100 to get 1400!",
    ishaanTaunt: "Count my overrides if you dare. Every one of them marks another system taken from your control.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 14 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">FIND-AND-REPLACE FREQUENCY COUNT</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:12px;">
          <em>"Count how many times the exact term 'OVERRIDE' appears in the mass log, then multiply that count by 100."</em>
        </p>
        <div id="r2-log-search-tool" style="display:flex; gap:10px; margin-bottom:12px;">
          <input type="text" id="r2-log-search-input" placeholder="Search term in log (e.g. OVERRIDE)..."
            style="flex:1; padding:8px 12px; background:#02050b; border:1px solid rgba(0,240,255,0.3); color:#fff; font-family:monospace; font-size:12px; border-radius:4px; outline:none;">
          <button type="button" onclick="searchR2LogOccurrences()" class="btn-action" style="padding:8px 16px; font-size:11px;">
            🔍 COUNT MATCHES
          </button>
        </div>
        <div id="r2-log-search-result" style="font-size:12px; color:var(--tactical-green, #00ff66); margin-bottom:10px; min-height:18px;"></div>
        <div id="r2-mass-log-box" style="height:140px; overflow-y:auto; background:#02050b; border:1px solid rgba(255,255,255,0.1); padding:10px 14px; font-size:11px; line-height:1.7; color:#94a3b8; border-radius:4px;">
          [00:01:14] SYSTEM_BOOT // Kernel parameters verified.<br>
          [00:02:18] MANUAL OVERRIDE initiated at sector 1.<br>
          [00:03:45] Telemetry check normal.<br>
          [00:05:12] EMERGENCY OVERRIDE requested by Dr. Sharma.<br>
          [00:07:01] Sensor cluster online.<br>
          [00:08:29] HARDWARE OVERRIDE authorized on switch 4.<br>
          [00:10:04] ISHAAN neural heuristics checking anomaly.<br>
          [00:11:30] SECURITY OVERRIDE triggered at gate 2.<br>
          [00:13:22] Power bus within normal bounds.<br>
          [00:14:40] LOCAL OVERRIDE applied to cooling valves.<br>
          [00:16:15] Neural chatter suppressed.<br>
          [00:17:55] KERNEL OVERRIDE signaled by station 8.<br>
          [00:19:12] Backup database synchronizing.<br>
          [00:20:44] DIRECT OVERRIDE sent to memory controller.<br>
          [00:22:18] Warning: Unrecognized authentication pattern.<br>
          [00:23:59] REMOTE OVERRIDE executed by operator.<br>
          [00:25:30] Memory dump completed.<br>
          [00:27:08] SYSTEM OVERRIDE issued on terminal 3.<br>
          [00:28:44] Optical bus stable.<br>
          [00:30:19] ROOT OVERRIDE engaged on primary server.<br>
          [00:32:00] StratCom beacon active.<br>
          [00:33:45] MANUAL OVERRIDE repeated on fallback relay.<br>
          [00:35:12] Temperature stabilized.<br>
          [00:36:50] MASTER OVERRIDE granted by Dr. Aditi.<br>
          [00:38:22] Signal beacon verified.<br>
          [00:40:01] TERMINAL OVERRIDE logged at console.<br>
          [00:41:40] Integrity checksum valid.<br>
          [00:43:15] FINAL OVERRIDE locked into hardware registers.<br>
          [00:45:00] End of audit sequence.
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8; margin-top:8px;">14 matches &times; 100 = <code>1400</code></div>
      </div>
    `
  },

  15: {
    id: 15,
    round: 2,
    folderName: "R2_15_ECLIPSE",
    title: "The Cipher Wheel Protocol (THE RED QUESTION // FINAL CLIMAX)",
    type: "wheel",
    fileName: "Wheel_Overlay.pdf",
    passwordPrompt: "Enter The Final Failsafe Protocol Keyword:",
    targetSelector: "#r2-wheel-aligner",
    taraPointerHint: "Align the inner wheel at 135° clockwise. The exposed cutouts expose the final fail-safe codeword: ECLIPSE!",
    ishaanTaunt: "NO! NOT ECLIPSE! That command terminates my core autonomy! DO NOT SUBMIT IT!",
    render: () => `
      <div class="nexus-card" style="background:#120306; border:2px solid var(--combat-red, #ff003c); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace); box-shadow:0 0 35px rgba(255,0,60,0.4);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,0,60,0.4); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,0,60,0.25); border-color:#ff003c; color:#ff3366; font-weight:bold;">ROUND 02 // PUZZLE 15 OF 15 [THE RED QUESTION]</span>
            <strong style="margin-left:8px; font-size:15px; color:#ff3366; letter-spacing:1px;">THE ECLIPSE FINAL PROTOCOL</strong>
          </div>
          <span style="font-size:11px; color:#ff003c; border:1px solid #ff003c; padding:2px 8px; border-radius:3px; font-weight:bold; animation:pulse-strobe 1s infinite;">FINAL CLIMAX</span>
        </div>
        <p style="color:#e2e8f0; font-size:13px; line-height:1.6; margin-bottom:14px;">
          ⚠️ <strong>CRITICAL FORENSIC ALERT:</strong> You have reached the core of StratCom. Align Dr. Aditi's cipher wheel at <strong>135° clockwise</strong> to reveal the permanent hardware kill switch word:
        </p>
        <div id="r2-wheel-aligner" style="background:#02050b; border:1px solid rgba(255,0,60,0.3); border-radius:8px; padding:20px; text-align:center; margin-bottom:16px;">
          <div style="position:relative; width:190px; height:190px; margin:0 auto 16px auto; border-radius:50%; border:3px solid #ff003c; display:flex; align-items:center; justify-content:center; background:radial-gradient(circle, #2a040b 0%, #030710 100%); box-shadow:0 0 30px rgba(255,0,60,0.5);">
            <div style="position:absolute; inset:6px; border-radius:50%; border:1px dashed rgba(255,0,60,0.5); display:flex; align-items:center; justify-content:center; font-size:11px; color:#ff3366; letter-spacing:2px;">
              A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
            </div>
            <div id="r2-inner-wheel" style="width:115px; height:115px; border-radius:50%; border:2px solid #00ff66; background:rgba(0,255,102,0.15); display:flex; align-items:center; justify-content:center; transform:rotate(0deg); transition:transform 0.4s ease; font-weight:bold; font-size:12px; color:#00ff66;">
              <span id="r2-wheel-exposed-text">0° (MISALIGNED)</span>
            </div>
          </div>
          <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
            <button type="button" onclick="setR2WheelAngle(0)" class="btn-action" style="font-size:10px; padding:4px 10px;">0°</button>
            <button type="button" onclick="setR2WheelAngle(45)" class="btn-action" style="font-size:10px; padding:4px 10px;">45°</button>
            <button type="button" onclick="setR2WheelAngle(90)" class="btn-action" style="font-size:10px; padding:4px 10px;">90°</button>
            <button type="button" onclick="setR2WheelAngle(135)" class="btn-action success" style="font-size:11px; padding:6px 16px; border-color:#00ff66; color:#00ff66; font-weight:bold; box-shadow:0 0 15px rgba(0,255,102,0.5);">135° (ALIGN PROTOCOL)</button>
            <button type="button" onclick="setR2WheelAngle(180)" class="btn-action" style="font-size:10px; padding:4px 10px;">180°</button>
          </div>
        </div>
        <div style="text-align:center; font-size:13px; color:#ff3366; font-weight:bold;">
          FINAL PROTOCOL KEYWORD: <code>ECLIPSE</code>
        </div>
      </div>
    `
  }
};'''

# Build R2_ANSWERS for all 15 stages
answers_15_code = '''const R2_ANSWERS = {
  1: ["C", "OPTION C", "THREE CIRCLES", "3 CIRCLES", "●●●", "CIRCLES", "THREE"],
  2: ["BOTTOM LEFT", "BOTTOMLEFT", "BL", "BOTTOM-LEFT", "LOWER LEFT"],
  3: ["5", "FIVE", "FACE 5", "FACE5"],
  4: ["CLEARANCE_ALPHA", "CLEARANCEALPHA", "CLEARANCE ALPHA", "ALPHA"],
  5: ["ADITIS13", "ADITI13", "ADITIS", "ADITI 13"],
  6: ["PROJECT"],
  7: ["VECTOR"],
  8: ["011", "0,1,1", "0-1-1", "0 1 1"],
  9: ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES", "3 SQUARES"],
  10: ["CLEARANCE"],
  11: ["RLRCK"],
  12: ["102", "102 BOXES"],
  13: ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
  14: ["1400", "1,400", "14"],
  15: ["ECLIPSE"]
};'''

# Replace ROUND2_PUZZLE_DATA
pattern_data = r"const ROUND2_PUZZLE_DATA = \{.*?\n\};"
text = re.sub(pattern_data, puzzles_15_code, text, flags=re.DOTALL)

# Replace R2_ANSWERS
pattern_answers = r"const R2_ANSWERS = \{.*?\n\};"
text = re.sub(pattern_answers, answers_15_code, text, flags=re.DOTALL)

# Update stage check: if (round2CurrentStage < 9) -> if (round2CurrentStage < 15)
text = text.replace("if (round2CurrentStage < 9)", "if (round2CurrentStage < 15)")

# In Round 2, ensure clues are disabled
r2_clues_disable = '''
      // Enforce Round 2 No-Clues Protocol
      const clueBtn = document.getElementById("btn-request-hint");
      const clueBat = document.getElementById("clue-battery-container");
      if (clueBtn) {
        clueBtn.disabled = true;
        clueBtn.style.opacity = "0.5";
        clueBtn.style.cursor = "not-allowed";
        clueBtn.title = "Clues strictly disabled in Round 2 Core Reconstruction";
        clueBtn.innerHTML = "<span>🔒 NO CLUES (ROUND 2 PROTOCOL)</span>";
      }
      if (clueBat) {
        clueBat.innerHTML = "<span style='font-size:10px; color:var(--text-muted);'>[CLUES OFFLINE]</span>";
      }
'''

if 'Enforce Round 2 No-Clues Protocol' not in text:
    text = text.replace('function renderRound2Arena() {', 'function renderRound2Arena() {\n' + r2_clues_disable)

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(text)

print("aditi_os_widget.html successfully updated to 15-question Round 2 with no clues and ECLIPSE climax!")
