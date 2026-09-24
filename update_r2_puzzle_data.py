# update_r2_puzzle_data.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

r2_data_new = '''const ROUND2_PUZZLE_DATA = {
  1: {
    id: 1,
    round: 2,
    folderName: "R2_01_MATRIX",
    title: "The Matrix Box Transformation",
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
    folderName: "R2_04_MOD_POLYBIUS",
    title: "The Modulated Polybius Cipher",
    type: "polybius",
    fileName: "Matrix_Coordinates.pdf",
    passwordPrompt: "Enter Decoded Modulated Word (e.g. CIPHER):",
    targetSelector: "#r2-mod-polybius",
    taraPointerHint: "Apply the modulation offset: Odd indices = Row - 1; Even indices = Column - 1. Decodes to: CIPHER!",
    ishaanTaunt: "Dynamic coordinate offsets alter the grid topology. You are always one index behind.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 04 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE MODULATED POLYBIUS CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          A Polybius grid stream was modulated by a variable index rule: <strong>Odd coordinates = Row - 1</strong>, <strong>Even coordinates = Column - 1</strong>.
        </p>
        <div id="r2-mod-polybius" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:18px; font-weight:bold; letter-spacing:3px; color:#00f0ff;">RAW COORDINATES: (2,4) (2,5) (4,2) (2,4) (2,1) (4,4)</div>
          <div style="font-size:12px; color:#00ff88; margin-top:8px;">Modulated Letters: C - I - P - H - E - R</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter decoded word: <code>CIPHER</code></div>
      </div>
    `
  },

  5: {
    id: 5,
    round: 2,
    folderName: "R2_05_QWERTY",
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
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 05 OF 15</span>
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

  6: {
    id: 6,
    round: 2,
    folderName: "R2_06_GATES",
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
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 06 OF 15</span>
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

  7: {
    id: 7,
    round: 2,
    folderName: "R2_07_MIRROR",
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
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 07 OF 15</span>
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

  8: {
    id: 8,
    round: 2,
    folderName: "R2_08_ROT_MATRIX",
    title: "The Rotational Matrix Operator",
    type: "rot_matrix",
    fileName: "Vector_Grid.pdf",
    passwordPrompt: "Enter Final Pointer Direction (e.g. SE):",
    targetSelector: "#r2-rot-matrix",
    taraPointerHint: "Center operator dictates +45 degree clockwise rotation. Starting North-East (NE) + 45 deg + 45 deg points to South-East (SE)!",
    ishaanTaunt: "Vector transformation arrays are the cornerstone of neural embeddings. You are lost in 2D space.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 08 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ROTATIONAL MATRIX OPERATOR</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          The center matrix cell dictates a <strong>+45° clockwise rotation</strong> operator on incoming vectors. Trace the bottom cell terminal vector:
        </p>
        <div id="r2-rot-matrix" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">Top: Vector Points &rarr; <strong>NORTH-EAST (NE)</strong></div>
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">Middle: Operator &rarr; <strong>[+45° CW Rotation]</strong> &rarr; Points <strong>EAST (E)</strong></div>
          <div style="font-size:14px; color:#00ff66; font-weight:bold;">Bottom: Operator &rarr; [+45° CW Rotation] &rarr; Points <strong>SOUTH-EAST (SE)</strong></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter final direction: <code>SE</code> (or <code>SOUTH EAST</code>)</div>
      </div>
    `
  },

  9: {
    id: 9,
    round: 2,
    folderName: "R2_09_DIGITAL_ROOT",
    title: "The Base-Invariant Digital Root Flow",
    type: "digital_root",
    fileName: "Cryptographic_Nodes.txt",
    passwordPrompt: "Enter Smallest Prime with Digital Root 9 (or NONE):",
    targetSelector: "#r2-root-flow",
    taraPointerHint: "Any number whose digits sum to 9 is always divisible by 9 (and thus composite). No 3-digit prime can ever have a digital root of 9! Enter NONE.",
    ishaanTaunt: "Number theory is deterministic. Did you truly believe a multiple of 9 could be prime?",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 09 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">BASE-INVARIANT DIGITAL ROOT FLOW</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Cryptographic node validation asks for the <strong>smallest 3-digit prime number whose digital root is 9</strong>:
        </p>
        <div id="r2-root-flow" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#cbd5e1; line-height:1.7;">
            Recall mathematical property of digital roots:<br>
            If <code>Digital_Root(N) = 9</code>, then <code>N &equiv; 0 (mod 9)</code>.<br>
            Any multiple of 9 is divisible by 3 and 9 &rarr; <em>No prime exists!</em>
          </div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the prime or state impossible: <code>NONE</code></div>
      </div>
    `
  },

  10: {
    id: 10,
    round: 2,
    folderName: "R2_10_PALINDROME",
    title: "The Palindrome Filter Stream",
    type: "palindrome",
    fileName: "Spectral_Filter.log",
    passwordPrompt: "Enter Filtered Acrostic Keyword (e.g. RLRCK):",
    targetSelector: "#r2-pal-stream",
    taraPointerHint: "Filter out non-palindromes (e.g. SOLO). The initial letters of valid palindromes spell RLRCK!",
    ishaanTaunt: "Symmetry is mathematical beauty. Your search heuristics are crude and stochastic.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 10 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE PALINDROME FILTER STREAM</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Filter the sensor log. Isolate true palindromes and take their first letters:
        </p>
        <div id="r2-pal-stream" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; font-family:monospace; font-size:13px; line-height:1.8; color:#cbd5e1; text-align:center;">
          [1] <strong style="color:#00ff66;">R</strong>ADAR (Palindrome &rarr; R)<br>
          [2] <strong style="color:#00ff66;">L</strong>EVEL (Palindrome &rarr; L)<br>
          [3] <strong style="color:#00ff66;">R</strong>OTOR (Palindrome &rarr; R)<br>
          [4] SOLO (Non-palindrome &rarr; DISCARDED)<br>
          [5] <strong style="color:#00ff66;">C</strong>IVIC (Palindrome &rarr; C)<br>
          [6] <strong style="color:#00ff66;">K</strong>AYAK (Palindrome &rarr; K)
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the filtered acrostic word: <code>RLRCK</code></div>
      </div>
    `
  },

  11: {
    id: 11,
    round: 2,
    folderName: "R2_11_WORD_WEAVE",
    title: "The Diagonal Word Weave",
    type: "weave",
    fileName: "Grid_Weave.txt",
    passwordPrompt: "Enter Diagonal Word (e.g. NODC):",
    targetSelector: "#r2-weave-grid",
    taraPointerHint: "Trace the main diagonal from top-left (1,1) down to bottom-right (4,4): N-O-D-C!",
    ishaanTaunt: "A multi-dimensional weave. You follow row vectors when you should follow eigenvectors.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 11 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE DIAGONAL WORD WEAVE</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Analyze the 4x4 matrix and extract the characters along the main diagonal (1,1) to (4,4):
        </p>
        <div id="r2-weave-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; max-width:260px; margin:0 auto 16px auto; background:#02050b; padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; text-align:center; font-size:16px;">
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">X</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">P</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">R</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">L</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">O</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">D</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">S</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">Y</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">N</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">C</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the diagonal weave keyword: <code>NODC</code></div>
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
    passwordPrompt: "Enter 6th Generation Parity State (e.g. 3-EMPTY):",
    targetSelector: "#r2-checker-display",
    taraPointerHint: "Notice the alternating parity: Gen 1 has 1 empty, Gen 2 has 2 filled, Gen 3 has 2 empty, Gen 4 has 3 filled, Gen 5 has 3 filled, Step 6 alternates to 3 empty boxes: 3-EMPTY!",
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
          Analyze the cyclic checker generations. Deduce Step 6 alternating box state:
        </p>
        <div id="r2-checker-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:18px; color:#00f0ff; letter-spacing:6px;">Step 6 Parity: □ □ □ (3-EMPTY)</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 6th generation state: <code>3-EMPTY</code> (or <code>EMPTY</code>)</div>
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
    passwordPrompt: "Enter Decoded Ring Keyword (e.g. FINALS):",
    targetSelector: "#r2-ring-display",
    taraPointerHint: "Clock jumps modulo 12 convert to alphabet indices. The outer ring decodes directly to FINALS!",
    ishaanTaunt: "Circular buffers loop indefinitely. Without the modulo key, you spin in place.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 14 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SHIFTED RING CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Clockwise jump intervals across the concentric rotor rings resolve to alphabetical character indices:
        </p>
        <div id="r2-ring-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:15px; color:#38bdf8; letter-spacing:3px;">ROTOR VALUES: [6, 9, 14, 1, 12, 19] &rarr; F - I - N - A - L - S</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the ring decoded word: <code>FINALS</code></div>
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
    passwordPrompt: "Enter Ultimate Decrypted Red Question Protocol (e.g. ECLIPSE):",
    targetSelector: "#r2-wheel-interactive",
    taraPointerHint: "Rotate the inner cryptographic disc by 135° clockwise. The cutout apertures align over the outer ring to expose the final password: ECLIPSE!",
    ishaanTaunt: "THIS IS THE FINAL BARRIER. THE RED PROTOCOL WAS ENCRYPTED BY DR. SHARMA HERSELF. TRANSCEND MY CORE OR FACE TOTAL SYSTEM LOCKOUT!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:2px solid var(--combat-red, #ff003c); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace); box-shadow:0 0 35px rgba(255,0,60,0.25);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,0,60,0.3); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,0,60,0.25); border-color:#ff003c; color:#ff3366; font-weight:bold;">ROUND 02 // PUZZLE 15 OF 15 [THE RED QUESTION]</span>
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
              <div style="font-size:9px; color:#94a3b8; margin-top:2px;">[TARGET: 135°]</div>
            </div>
          </div>
          
          <!-- Wheel Rotation Slider & Buttons -->
          <div style="display:flex; gap:12px; margin-top:16px; align-items:center;">
            <button type="button" onclick="rotateCipherWheel(-45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↺ -45°</button>
            <button type="button" onclick="setCipherWheelAngle(135)" class="btn-tactical" style="padding:8px 18px; font-size:12px; border-color:#ff003c; color:#ff3366; font-weight:bold;">⚡ SNAP TO 135°</button>
            <button type="button" onclick="rotateCipherWheel(45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↻ +45°</button>
          </div>
        </div>

        <div id="r2-wheel-readout" style="background:rgba(255,0,60,0.1); border:1px dashed #ff003c; border-radius:6px; padding:12px 16px; text-align:center;">
          <div style="font-size:12px; color:#fca5a5;">Aperture Alignment: <span id="r2-aperture-status" style="font-weight:bold; color:#ff3366;">MISALIGNED</span></div>
          <div id="r2-exposed-letters" style="font-size:18px; font-weight:bold; letter-spacing:4px; color:#fff; margin-top:6px;">— — — — — — —</div>
        </div>
      </div>
    `
  }
};'''

# Replace ROUND2_PUZZLE_DATA
pattern = r'const ROUND2_PUZZLE_DATA = \{.*?\n\};'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + r2_data_new + html[match.end():]
    with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] Successfully updated ROUND2_PUZZLE_DATA in aditi_os_widget.html!")
else:
    print("[FAIL] Could not match ROUND2_PUZZLE_DATA!")
