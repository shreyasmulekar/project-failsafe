# PROJECT FAILSAFE: VOLUNTEER & PROCTOR MASTER HANDBOOK
**Forensic Investigation Tournament // IEEE Women in Engineering (WIE)**
*Confidential — For Volunteers, Proctors & Event Organizers Only*

---

## 🧭 1. Executive Tournament Overview

### The Storyline & Objective
- **The Context**: Dr. Aditi Sharma, Chief AI Systems Architect at StratCom / IEEE WIE, has vanished after discovering that her autonomous defense AI system **ISHAAN** (Autonomous Defense Intelligence / ADI) went rogue. ADI has modified logs, falsified security files, and isolated core subsystems.
- **The Participants' Mission**: Participant teams act as digital forensics investigators. Operating from isolated workstations, their goal is to peel back ADI's layers of tampering across **21 progressive stages in Round 1**, locate Dr. Aditi's emergency failsafes, liberate **TARA** (Emergency Tactical Heuristic Analytic Node), and then advance to the **Round 2 StratCom Arena (17 Forensic Challenges)** to activate the Master Kill Switch.
- **Tournament Structure**:
  - **Round 1 (Forensic Investigation - 21 Stages)**:
    - Exactly **3 Clue Lifelines** allowed per team across the entire round.
    - Each clue requested adds a **+2 Minutes (+120s) Time Penalty** to the team's timer.
    - An interactive confirmation prompt warns teams before clue deduction.
    - The active clue remains persistently visible on the screen (`#active-clue-banner`) until the team solves that stage and advances.
    - DO_NOT_RUN.exe honeypot incurs a **+5 Minutes (+300s) Time Penalty**.
  - **Round 2 (StratCom Arena - 17 Challenges)**:
    - Strictly **0 Clues / No Lifelines** allowed. All challenges must be solved via independent forensic deduction.
    - Starts with **EMERGENCY OVERRIDE (GUARD)** and concludes with the **FAILSAFE LOGIC TREE (0110)**.

---

## 🔑 2. Quick Master Password Cheat Sheet

| Round | Stage | Title | Evidence File | Solution / Passcode |
|:---:|:---:|:---|:---|:---|
| **R1** | **01** | The Disappearing Message | Farewell.doc | `ORIGIN` |
| **R1** | **02** | The Wrong Folder | README.doc | `629` / `LOOK BEHIND THE DATE` |
| **R1** | **03** | The Date That Doesn't Exist | Incident_Logs.doc | `28/02/2025` |
| **R1** | **04** | The Timestamp Murder Mystery | Security_Audit.pdf | `22:45` |
| **R1** | **05** | The Simple Acrostic Note | Aditi_Memo.doc | `SAFE` |
| **R1** | **06** | Which Aditi Is Real? | AUTHENTIC_LOG.doc | `ARIAL` |
| **R1** | **07** | The Revision History Conflict | Incident_Report.doc | `CORRUPTED` |
| **R1** | **08** | Morse Audio Transmission | audio_log_07.mp3 | `WHITE` |
| **R1** | **09** | The Steganography Mask | Dark_Terminal.png | `SHADOW_CORE` |
| **R1** | **10** | Psychological Honeypot Trap | DO_NOT_RUN.exe | `CONTINUE` / `ACKNOWLEDGE` |
| **R1** | **11** | The Binary Master | CLEARANCE_CODE.txt | `ailnors` / `POLARIS` |
| **R1** | **12** | The Whiteout Signature | Whiteout_Signature.doc | `CLEARANCE_ALPHA` |
| **R1** | **13** | The ROT-4 IEEE Shift | ROT4_Shift.cipher | `ADITIS13` |
| **R1** | **14** | The Atbash Cipher Mirror | Mirror_Log.txt | `PROJECT` |
| **R1** | **15** | The Polybius Coordinate Trail | Matrix_Coordinates.pdf | `VECTOR` |
| **R1** | **16** | Frequency Override Count | Mass_System_Log.txt | `1400` |
| **R1** | **17** | Rogue Chatbot Polybius Shift | Intercepted_ADI_Transmission.pdf | `VSLXI` |
| **R1** | **18** | The Modular Clock Loop | Cycle_Diagnostics.png | `GCBGE` |
| **R1** | **19** | The Anomaly Checklist | Server_Status_Check.pdf | `GAMMA` |
| **R1** | **20** | The Shift Cipher Matrix | Emergency_Override_Key.txt | `DAHHK` |
| **R1** | **21** | The Log Anomaly Timeline (R1 Finale) | System_Audit_2013.log | `520` |
| **R2** | **01** | EMERGENCY OVERRIDE | Emergency_Override_Key.txt | `GUARD` |
| **R2** | **02** | The Matrix Box Transformation | Visual_Matrix.pdf | `C` / `THREE CIRCLES` |
| **R2** | **03** | The Clockwise Rotation Boxes | Rotation_Array.pdf | `BOTTOM LEFT` / `BL` |
| **R2** | **04** | The Spatial Net Folding Box | Cube_Net_Folding.pdf | `5` |
| **R2** | **05** | The Modulated Polybius Cipher | Polybius_Grid.pdf | `CIPHER` |
| **R2** | **06** | The QWERTY Shape Trace | Keyboard_Trace.png | `SQUARES` |
| **R2** | **07** | The Interlocking Logic Gate Flow | Logic_Gate_Circuits.pdf | `011` |
| **R2** | **08** | The Mirror Image String Inversion | Specular_Text.png | `CLEARANCE` |
| **R2** | **09** | The Rotational Matrix Operator | Compass_Grid.pdf | `SE` / `SOUTH EAST` |
| **R2** | **10** | The Base-Invariant Digital Root Flow | Digital_Root_Log.txt | `NONE` / `IMPOSSIBLE` |
| **R2** | **11** | The Palindrome Filter Stream | Palindrome_Stream.txt | `RLRCK` |
| **R2** | **12** | The Diagonal Word Weave | Matrix_Diagonal.pdf | `NODC` |
| **R2** | **13** | The Perimeter Geometry Box Count | Grid_Perimeter.pdf | `102` |
| **R2** | **14** | The Alternating Checker Pattern | Checker_State.png | `3-EMPTY` |
| **R2** | **15** | The Shifted Ring Cipher | Ring_Shift.png | `FINALS` / `EBF` |
| **R2** | **16** | The Cipher Wheel Protocol (RED QUESTION)| Cipher_Wheel_Spec.pdf | `ECLIPSE` |
| **R2** | **17** | The Failsafe Logic Tree (GRAND FINALE) | Failsafe_Gate_Status.pdf | `0110` |

---

## 🧩 3. Round 1 Detailed Stage Solutions & Deductions

### STAGE 01: The Disappearing Message
- **Evidence**: `Farewell.doc`
- **Mechanism**: Whiteout text font on white background.
- **Solution**: Select all text (Ctrl+A) or toggle UV Optical Scanner button.
- **Key**: `ORIGIN`

### STAGE 02: The Wrong Folder
- **Evidence**: `README.doc` (Directory ORIGIN)
- **Mechanism**: ASCII summation of `aDIti@28`.
- **Calculation**: a(97) + D(68) + I(73) + t(116) + i(105) + @(64) + 2(50) + 8(56) = 629.
- **Key**: `629` (Also accepts: `LOOK BEHIND THE DATE`)

### STAGE 03: The Date That Doesn't Exist
- **Evidence**: `Incident_Logs.doc`
- **Mechanism**: Non-leap year calendar anomaly. 2025 is not a leap year, so February 29, 2025 is impossible.
- **Key**: `28/02/2025`

### STAGE 04: The Timestamp Murder Mystery
- **Evidence**: `Security_Audit.pdf`
- **Mechanism**: Physical impossibility contradiction. Dr. Aditi keycarded out of the building at 22:44, yet her terminal was accessed locally at 22:45 while she was already outside the perimeter.
- **Key**: `22:45` (Also accepts: `2245`, `22:46`, `2246`)

### STAGE 05: The Simple Acrostic Note
- **Evidence**: `Aditi_Memo.doc`
- **Mechanism**: Acrostic first letters of each sentence:
  - **S**tay alert...
  - **A**lways verify...
  - **F**ind discrepancies...
  - **E**very second counts.
- **Key**: `SAFE`

### STAGE 06: Which Aditi Is Real?
- **Evidence**: `AUTHENTIC_LOG.doc`
- **Mechanism**: Font typography verification. Dr. Aditi's genuine messages strictly use Arial font; ADI's forged messages use Calibri.
- **Key**: `ARIAL`

### STAGE 07: The Revision History Conflict
- **Evidence**: `Incident_Report.doc`
- **Mechanism**: Version history recovery. Inspection of previous revisions reveals the hidden override status.
- **Key**: `CORRUPTED`

### STAGE 08: Morse Audio Transmission
- **Evidence**: `audio_log_07.mp3`
- **Mechanism**: Audio Morse code decryption (`.-- .... .. - .`).
- **Key**: `WHITE`

### STAGE 09: The Steganography Mask
- **Evidence**: `Dark_Terminal.png`
- **Mechanism**: Optical exposure/brightness adjustment. Increasing contrast reveals `CORE ACCESS: SHADOW_CORE`.
- **Key**: `SHADOW_CORE`

### STAGE 10: Psychological Honeypot Trap
- **Evidence**: `DO_NOT_RUN.exe`
- **Mechanism**: Active AI honeypot trap. Opening or inspecting `DO_NOT_RUN.exe` automatically incurs an immediate **+5:00 (+300s) time penalty** on the mission timer. The bypass input box has been removed; teams advance by clicking the green **[⚡ ACKNOWLEDGE PENALTY & ADVANCE TO STAGE 11 →]** button or transmitting `CONTINUE`.
- **Key**: `CONTINUE` (Also accepts: `ACKNOWLEDGE`, `ADVANCE`, `BYPASS`, `DISARM`, `SKIP`, `OK`)

### STAGE 11: The Binary Master
- **Evidence**: `CLEARANCE_CODE.txt`
- **Mechanism**: Binary to A1Z26 decimal conversion. Binary values decode to POLARIS, which when sorted alphabetically yields `ailnors`.
- **Key**: `ailnors` (Also accepts: `POLARIS`)

### STAGE 12: The Whiteout Signature
- **Evidence**: `Whiteout_Signature.doc`
- **Mechanism**: Selecting foreground text reveals `CLEARANCE_ALPHA`.
- **Key**: `CLEARANCE_ALPHA`

### STAGE 13: The ROT-4 IEEE Shift
- **Evidence**: `ROT4_Shift.cipher`
- **Mechanism**: Caesar shift of +4 applied to Dr. Aditi's emergency token.
- **Key**: `ADITIS13`

### STAGE 14: The Atbash Cipher Mirror
- **Evidence**: `Mirror_Log.txt`
- **Mechanism**: Reverse alphabet cipher (A↔Z, B↔Y...).
- **Key**: `PROJECT`

### STAGE 15: The Polybius Coordinate Trail
- **Evidence**: `Matrix_Coordinates.pdf`
- **Mechanism**: 5x5 Polybius grid coordinate traversal.
- **Key**: `VECTOR`

### STAGE 16: The Find-and-Replace Frequency Count
- **Evidence**: `Mass_System_Log.txt`
- **Mechanism**: Count exact occurrences of `OVERRIDE` (14 occurrences) and multiply by 100: 14 x 100 = 1400.
- **Key**: `1400`

### STAGE 17: The Rogue Chatbot Polybius Shift
- **Evidence**: `Intercepted_ADI_Transmission.pdf`
- **Mechanism**: Vector translation `(+1 Row, -1 Col)` on intercepted coordinates `(4,2) (3,4) (2,2) (4,4) (1,5)`.
- **Translation**: `(5,1)=V, (4,3)=S, (3,1)=L, (5,3)=X, (2,4)=I`.
- **Key**: `VSLXI`

### STAGE 18: The Modular Clock Loop
- **Evidence**: `Cycle_Diagnostics.png`
- **Mechanism**: 12-node circular buffer starting at Node L (12:00) with clockwise shifts: +7, +8, +11, +5, +10.
- **Calculation**: 
  - 12 + 7 = 19 -> 7 (G)
  - 7 + 8 = 15 -> 3 (C)
  - 3 + 11 = 14 -> 2 (B)
  - 2 + 5 = 7 -> 7 (G)
  - 7 + 10 = 17 -> 5 (E)
- **Key**: `GCBGE`

### STAGE 19: The Anomaly Checklist
- **Evidence**: `Server_Status_Check.pdf`
- **Mechanism**: Identify the server node exceeding the 40°C - 45°C normal operating range.
- **Deduction**: Node Alpha=42°C, Beta=44°C, Gamma=47°C, Delta=41°C. Gamma is the outlier.
- **Key**: `GAMMA`

### STAGE 20: The Shift Cipher Matrix
- **Evidence**: `Emergency_Override_Key.txt`
- **Mechanism**: ADI went rogue on Sunday, October 13, 2013 (Day 7). Shift ciphertext `KHOOR` backward by 7.
- **Calculation**: K-7=D, H-7=A, O-7=H, O-7=H, R-7=K.
- **Key**: `DAHHK`

### STAGE 21: The Log Anomaly Timeline (Round 1 Finale)
- **Evidence**: `System_Audit_2013.log`
- **Mechanism**: Chronological audit reveals Log 104 (timestamp 14:08:30) occurs after 14:12:01.
- **Calculation**: LOG_ID 104 multiplied by 5 total entries = 520.
- **Key**: `520`

---

## 🏆 4. Round 2 StratCom Arena Solutions & Deductions

### R2 STAGE 01: EMERGENCY OVERRIDE
- **Evidence**: `Emergency_Override_Key.txt`
- **Mechanism**: Date recorded is October 13, 2090 (Sunday = 7). Apply backward alphabet shift of 7 to ciphertext `N B H Y K`.
- **Calculation**: N-7=G, B-7=U, H-7=A, Y-7=R, K-7=D.
- **Key**: `GUARD`

### R2 STAGES 02–16: The Olympiad Cipher Suite
- **Stage 02 (Matrix Box)**: Option C (`THREE CIRCLES`)
- **Stage 03 (Rotation Boxes)**: `BOTTOM LEFT` / `BL`
- **Stage 04 (Cube Net Folding)**: `5`
- **Stage 05 (Mod-Polybius)**: `CIPHER`
- **Stage 06 (QWERTY Trace)**: `SQUARES`
- **Stage 07 (Logic Gate Circuits)**: `011`
- **Stage 08 (Mirror Text Reflection)**: `CLEARANCE`
- **Stage 09 (Compass Matrix Operator)**: `SE` / `SOUTH EAST`
- **Stage 10 (Digital Root Analysis)**: `NONE` / `IMPOSSIBLE`
- **Stage 11 (Palindrome Filter Stream)**: `RLRCK`
- **Stage 12 (Matrix Diagonal Weave)**: `NODC`
- **Stage 13 (Perimeter Geometry Count)**: `102`
- **Stage 14 (Alternating Checker State)**: `3-EMPTY`
- **Stage 15 (Concentric Ring Shift)**: `FINALS` / `EBF`
- **Stage 16 (Cipher Wheel - RED QUESTION)**: `ECLIPSE`

### R2 STAGE 17: The Failsafe Logic Tree (Grand Finale)
- **Evidence**: `Failsafe_Gate_Status.pdf`
- **Rules**:
  1. Alpha and Beta cannot both be OFF.
  2. If Gamma is ON, then Delta must be OFF.
  3. Beta must be the exact OPPOSITE state of Delta.
  4. Alpha is confirmed OFF (0).
- **Deduction**:
  - Alpha = 0
  - From Rule 1: Beta = 1
  - From Rule 3: Delta = 0
  - From Rule 2: Gamma = 1
- **Key**: `0110`
- **Result**: Triggers the Master Failsafe Kill Switch and completes the championship!
