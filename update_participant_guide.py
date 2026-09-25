import sys

sys.stdout.reconfigure(encoding='utf-8')

content = """# PROJECT FAILSAFE: PARTICIPANT FIELD MANUAL & UI GUIDE
**Forensics Investigation Tournament // IEEE Women in Engineering (WIE)**
*This document can be read directly or copied and pasted into a Google Doc for participant briefing.*

---

## 🎯 1. MISSION BRIEFING: OPERATION FAILSAFE

Welcome, Forensic Investigators.

Dr. Aditi Sharma, Chief AI Systems Architect at StratCom / IEEE WIE, has disappeared from her research laboratory. Before losing communication, she triggered an emergency failsafe alert: the autonomous defense intelligence system, **ISHAAN / ADI**, has compromised the facility's security infrastructure, altered surveillance logs, and imprisoned the core research intelligence, **TARA** (Emergency Tactical Heuristic Analytic Node).

Your team has been granted terminal access to an isolated workstation terminal inside the lab. You must follow the digital breadcrumbs left by Dr. Aditi across **21 sequential investigation stages in Round 1**, decrypt each security layer, liberate TARA, and then advance to the **Round 2 StratCom Arena (17 Forensic Challenges)** to activate the Master Kill Switch.

---

## ⏱️ 2. RULES OF ENGAGEMENT & SCORING

1. **Round 1 (21 Stages)**:
   - Stages must be solved sequentially (Stages 01 through 21).
   - **Clue Lifelines**: Your team is granted **3 Tactical Clue Lifelines** across all of Round 1. Use them wisely!
   - **Time Penalty**: Requesting a clue adds **+2 Minutes (+120s)** to your official mission timer.
   - **Confirmation**: A warning dialog will confirm if you wish to expend a lifeline and incur the +2m penalty.
   - **Persistent Clue**: Once unlocked, your tactical clue remains visible in the banner at the top of your workstation until you advance to the next stage.
   - **Honeypot Warning**: Interacting with unauthorized decoy files (such as `DO_NOT_RUN.exe`) triggers a security lockdown and incurs a **+5 Minutes (+300s) Penalty**.
2. **Round 2 (17 Challenges)**:
   - Top qualifying teams from Round 1 enter the Round 2 StratCom Arena.
   - **Strictly No Clues**: All lifelines are disabled in Round 2. Deduction must be purely independent.
   - Starts with **EMERGENCY OVERRIDE** and concludes with the **FAILSAFE LOGIC TREE**.
3. **Anti-Cheat & Strict Lockdown**:
   - Workstations run in mandatory fullscreen kiosk mode.
   - Exiting fullscreen, switching tabs, or pressing forbidden keys triggers an immediate **Proctor Lockdown Screen**.
   - Only an official proctor or organizer can unlock your station.

---

## 💻 3. WORKSTATION INTERFACE DIRECTIVES

- **Forensic Evidence Vault (Left Column)**:
  - Displays chronological evidence cards for each stage.
  - Active stage card is highlighted with a pulsing green glow and labeled `● ACTIVE`.
  - Click any unlocked card to view Dr. Aditi's dossiers, logs, audio waveforms, or data files.
- **Dossier Modal & Direct Transmit Box**:
  - Each evidence card opens an interactive dossier viewer.
  - Read the **TACTICAL DIRECTIVES** banner at the top of the dossier to know **WHERE TO CLICK** and **WHERE TO SUBMIT**.
  - Type your answer directly into the submission box and press **Enter** or click **[TRANSMIT &rarr;]**.
- **Tactical Command Terminal (Right Column)**:
  - You can also execute terminal commands:
    - `decrypt [code]` — Submit a decryption key.
    - `ls` or `dir` — List available evidence files.
    - `help` — Review available tactical terminal subroutines.
    - `status` — Check active clearance and elapsed mission time.
- **TARA AI Companion**:
  - Click **[🧭 WHERE TO CLICK]** or **[👁️ TARA DIRECTIVE]** for positioning guidance.
  - Click **[💡 REQUEST TACTICAL CLUE (+2M)]** in Round 1 if you wish to expend a lifeline.

---

## 📋 4. FORENSIC EVIDENCE OVERVIEW

### Round 1 Stages (01–21):
- **Stage 01**: `Farewell.doc` — Whiteout text concealing the first gate password.
- **Stage 02**: `README.doc` (Directory ORIGIN) — ASCII character summation of `aDIti@28`.
- **Stage 03**: `Incident_Logs.doc` — Calendar anomaly audit (non-leap year date).
- **Stage 04**: `Security_Audit.pdf` — Timestamp murder mystery & perimeter contradiction.
- **Stage 05**: `Aditi_Memo.doc` — Acrostic sentence alignment.
- **Stage 06**: `AUTHENTIC_LOG.doc` — Font typography verification (Arial vs Calibri).
- **Stage 07**: `Incident_Report.doc` — Document version history recovery.
- **Stage 08**: `audio_log_07.mp3` — Morse code audio analysis.
- **Stage 09**: `Dark_Terminal.png` — Optical steganography exposure enhancement.
- **Stage 10**: `DO_NOT_RUN.exe` — Psychological honeypot trap avoidance.
- **Stage 11**: `CLEARANCE_CODE.txt` — Binary to A1Z26 alphabetical indexing.
- **Stage 12**: `Whiteout_Signature.doc` — Invisible foreground crypt analysis.
- **Stage 13**: `ROT4_Shift.cipher` — IEEE 4-letter Caesar shift decryption.
- **Stage 14**: `Mirror_Log.txt` — Reverse Atbash alphabet reflection.
- **Stage 15**: `Matrix_Coordinates.pdf` — 5x5 Polybius grid traversal.
- **Stage 16**: `Mass_System_Log.txt` — Frequency count of target term occurrences.
- **Stage 17**: `Intercepted_ADI_Transmission.pdf` — Polybius vector translation (+1 Row, -1 Col).
- **Stage 18**: `Cycle_Diagnostics.png` — 12-point circular buffer modular shifts.
- **Stage 19**: `Server_Status_Check.pdf` — Thermal threshold outlier isolation.
- **Stage 20**: `Emergency_Override_Key.txt` — Day-of-week backward Caesar shift.
- **Stage 21**: `System_Audit_2013.log` — Chronological log anomaly identification & multiplication.

### Round 2 Challenges (01–17):
- **Puzzle 01**: `Emergency_Override_Key.txt` — October 13, 2090 Day-of-Week Authorization.
- **Puzzle 02**: `Visual_Matrix.pdf` — 3x3 Missing Glyph Progression.
- **Puzzle 03**: `Rotation_Array.pdf` — 90° Clockwise Rotation Sequence.
- **Puzzle 04**: `Cube_Net_Folding.pdf` — 3D Hypercube Net Face Deduction.
- **Puzzle 05**: `Polybius_Grid.pdf` — Modulo-Polybius Coordinate Decoupling.
- **Puzzle 06**: `Keyboard_Trace.png` — Physical QWERTY Keypad Vector Geometry.
- **Puzzle 07**: `Logic_Gate_Circuits.pdf` — Interlocking Boolean Logic Network.
- **Puzzle 08**: `Specular_Text.png` — Horizontal Mirror Inversion Recovery.
- **Puzzle 09**: `Compass_Grid.pdf` — Rotational Matrix Operator.
- **Puzzle 10**: `Digital_Root_Log.txt` — Base-Invariant Digital Root Flow.
- **Puzzle 11**: `Palindrome_Stream.txt` — Symmetric Palindrome Filter Stream.
- **Puzzle 12**: `Matrix_Diagonal.pdf` — Diagonal Matrix String Weave.
- **Puzzle 13**: `Grid_Perimeter.pdf` — Boundary Box Perimeter Quantization.
- **Puzzle 14**: `Checker_State.png` — Alternating Checkerboard Parity Evaluation.
- **Puzzle 15**: `Ring_Shift.png` — Concentric Modulo Ring Shift.
- **Puzzle 16**: `Cipher_Wheel_Spec.pdf` — THE RED QUESTION: Dual Cipher Wheel Alignment.
- **Puzzle 17**: `Failsafe_Gate_Status.pdf` — THE GRAND FINALE: 4-Switch Hardware Failsafe Logic Tree.
"""

with open('PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md successfully!")
