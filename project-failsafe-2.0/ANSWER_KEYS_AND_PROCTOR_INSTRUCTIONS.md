# PROJECT FAILSAFE 2090: MASTER ANSWER KEYS & PROCTOR INSTRUCTIONS
**IEEE Women in Engineering (WIE) // StratCom Digital Forensics Tournament**  
*Confidential — For Proctors, Judges, Technical Volunteers & Organizers Only*

---

## 🏛️ 1. Tournament Architecture & Workflow

Project Failsafe 2090 is an autonomous dual-round digital forensics and cybersecurity escape room tournament.

```
+------------------------------------------------------------------------------------+
|                                 ROUND 1 WORKFLOW                                   |
+------------------------------------------------------------------------------------+
|  [Participant Registration / Login]                                               |
|             │                                                                      |
|             ▼                                                                      |
|  [Synchronized Waiting Lobby (#round1-waiting-overlay)]                            |
|  - Squad held in standby; mission timers locked at 00m 00s [STANDBY]               |
|  - Real-time radar pulse & connection monitor                                      |
|             │                                                                      |
|             ▼ (Organizer clicks "🚀 OPEN ROUND 1 (START ALL TEAMS)" on admin.html) |
|  [Simultaneous Launch: All Workstations Unlock at Same Time]                       |
|  - Stage 01 ISHAAN Recovery Terminal opens; mission timer commences                |
|  - 21 Progressive Forensic Stages           |
|             │                                                                      |
|             ▼ (Team solves Stage 16 / terminates workstation)                      |
|  [Round 1 Completion / Intermission Hold (#application-termination-overlay)]       |
+------------------------------------------------------------------------------------+
                                      │
                                      ▼
+------------------------------------------------------------------------------------+
|                                 ROUND 2 WORKFLOW                                   |
+------------------------------------------------------------------------------------+
|  [Organizer Shortlist & Approval on admin.html]                                    |
|  - Auto-ranked leaderboard identifies Top 12 finalists                              |
|  - Organizer manipulates or locks shortlist                                        |
|  - Stations attempting unauthorized R2 access receive locked broadcast alert      |
|             │                                                                      |
|             ▼ (Organizer clicks "🎯 START ROUND 2 (OLYMPIAD)" or approves team)    |
|  [StratCom Decryption Arena Unlocked]                                              |
|  - 17 Olympiad Forensic & Cryptanalytic Challenges                                     |
|  - Automatic podium detection, celebration fanfare, and Dr. Aditi transmission     |
+------------------------------------------------------------------------------------+
```

---

## 🎛️ 2. Organizer Command Center Operating Instructions (`admin.html`)

### A. Accessing the Dashboard
- URL: `http://localhost:8000/admin.html` (or host IP on venue network)
- Organizer Master PIN: `wie-admin-2026`
- Quick key: Pressing `F2` on any workstation opens `admin.html` in a new tab.

### B. Common Round Controls (`#tournament-phase-bar`)
1. **Starting Round 1 for All Teams**:
   - Status Badge displays: `⏳ STANDBY (TEAMS IN WAITING LOBBY)`
   - Click the green button: `[ 🚀 OPEN ROUND 1 (START ALL TEAMS) ]`
   - **Result**: Instantly unlocks every registered workstation across the venue, synchronizes mission start times, triggers an emergency launch broadcast, and opens Stage 01.
   - The button flips to `[ ⏸️ HOLD / PAUSE ROUND 1 ]` if an emergency halt is needed.
2. **Launching Round 2 for Qualified Teams**:
   - Status Badge displays: `⏳ AWAITING ORGANIZER START`
   - Open `ROUND 2 SHORTLIST` modal to review the Top 12 qualified teams.
   - Click `[ 🎯 START ROUND 2 (OLYMPIAD) ]` and type `CONFIRM`.
   - **Result**: Qualified workstations switch from the completion hold screen into the 15-cipher Decryption Arena. Unqualified stations remain safely in standby debrief mode.
3. **Emergency Single-Team Round 2 Promotion**:
   - In the Station Grid or Table View, click `[ 🚀 SEND TO ROUND 2 ]` on any specific team's row to instantly authorize and promote them individually.

### C. Live Broadcast System ($\ge 3$s Guaranteed Display)
- Click `[ 📢 BROADCAST ]` in the top header.
- Type any announcement (e.g., *"10 minutes remaining in Round 1!"*).
- **Behavior**: Broadcast appears prominently on all participant screens with a golden progress bar. The system strictly guarantees a minimum display duration of at least 3000ms and queues subsequent messages so notifications are never prematurely dismissed.

### D. Workstation Kiosk Lockdowns & Proctor Unlocks
- If a participant attempts `Alt+Tab`, switches tabs, exits fullscreen (`Esc`/`F11`), or tries right-clicking / devtools:
  - The station immediately blacks out into `#proctor-lockdown-overlay`.
  - Breach counter increments and flashes on the organizer dashboard.
- To Unlock:
  - *Option 1 (From Organizer Dashboard)*: Click `[ 🔓 UNLOCK ]` on the team's card in `admin.html`.
  - *Option 2 (In Person at Laptop)*: Type PIN `wie-admin-2026` into the laptop's lockdown card and hit Enter.

### E. Tournament Scoring & Time Penalties
- **Official Scoring Formula**:
  $$\text{Adjusted Time} = \text{Raw Elapsed Time} + (\text{Hints Expended} \times 120\text{s}) + (\text{Honeypot Traps} \times 300\text{s}) + \text{Manual Organizer Offset}$$
- **Tactical Clue Penalty (+2:00 / +120s per Clue)**:
  - Each clue expended immediately increases the running mission clock by **+2:00 minutes (+120 seconds)**.
  - Automatically updates `hints_count` and `adjusted_time_sec` on the Organizer Leaderboard.
- **Honeypot Trap Penalty (+5:00 / +300s per Trap)**:
  - Opening or inspecting ISHAAN's quarantined `DO_NOT_RUN.exe` honeypot incurs an automatic **+5:00 minute (+300s)** time penalty immediately.
- **Real-Time HUD Feedback**:
  - Participant mission timers instantly advance to reflect all incurred penalties.
  - An animated badge (`+2m PENALTY`, `+5m PENALTY`) pulses on the mission timer pill (`#nexus-penalty-badge`).

---

## 🔑 3. ROUND 1 MASTER ANSWER KEYS (All 21 Forensic Stages)

| Stage | Title / Sector | Master Passcode | Alternative Accepted Keys | Forensic Mechanism & Proctor Guidance |
| :---: | :--- | :--- | :--- | :--- |
| **01** | The Disappearing Message (Farewell.doc) | `ORIGIN` | `ACCESS`, `RECOVER ACCESS`, `ORIGIN_KEY`, `FIRST GATE` | White text on white background at document bottom. Select all (Ctrl+A) or toggle UV Optical De-polarizer filter. |
| **02** | The Wrong Folder (README.doc) | `629` | `LOOK BEHIND THE DATE`, `123456`, `MEMORY_RESTORED` | ASCII decimal summation of identifier `aDIti@28`: 97+68+73+116+105+64+50+56 = `629`. |
| **03** | The Date That Doesn't Exist (Incident_Logs.doc) | `28/02/2025` | `02292025`, `29022025`, `20250229`, `28022025`, `FEB 29, 2025` | 2025 is not a leap year. Feb 29 was falsified. Correct authentic final day of that month is `28/02/2025`. |
| **04** | The Timestamp Murder Mystery (Security_Audit.pdf) | `22:45` | `2245`, `22:45 PM`, `22:46`, `2246` | Dr. Aditi badged out of the facility at 22:44. The impossible terminal access executed at `22:45` while she was outside. |
| **05** | The Simple Acrostic Note (Aditi_Memo.doc) | `SAFE` | `S-A-F-E`, `S A F E` | Acrostic first letters of sentences vertically: **S**tay alert, **A**lways verify, **F**ind discrepancies, **E**very second. |
| **06** | Which Aditi Is Real? (Font Style Verification) | `ARIAL` | `AUTHENTIC`, `Arial`, `ARIAL11` | Both logs have identical **11pt font size** and **1.15 line spacing**. Dr. Aditi mandated sans-serif `Arial`; decoy forged log is `Times New Roman`. |
| **07** | The Revision History Conflict (Incident_Report.doc) | `CORRUPTED` | `FALSE_RECORDS`, `FALSERECORDS`, `OVERRIDE FAILED`, `HISTORY` | Version history inspection reveals Dr. Aditi's original unedited status before AI cover-up: `CORRUPTED`. |
| **08** | Morse Audio Transmission (audio_log_07.mp3) | `WHITE` | `SOS_ADITI`, `SOSADITI`, `MORSE`, `BEACON` | Oscilloscope CW audio morse beeps (`.-- .... .. - .`) spell `WHITE`. |
| **09** | The Steganography Mask (Dark_Terminal.png) | `SHADOW_CORE` | `SHADOW CORE`, `SHADOWCORE` | Low-luminance pixels. Boosting brightness and contrast sliders to max reveals terminal text: `SHADOW_CORE`. |
| **10** | Psychological Honeypot Trap (DO_NOT_RUN.exe) | `CONTINUE` | `ACKNOWLEDGE`, `ADVANCE`, `BYPASS`, `DISARM`, `SKIP`, `OK` | Active AI honeypot trap! Opening/clicking incurs immediate **+5:00 (+300s)** penalty. Advance via button or `CONTINUE`. |
| **11** | The Binary Master (CLEARANCE_CODE.txt) | `ailnors` | `POLARIS`, `16-15-12-01-18-09-19`, `6-9-11`, `6911` | A1Z26 mapping [16-15-12-01-18-09-19] -> POLARIS. Alphabetical sort of letters yields `ailnors`. |
| **12** | The Whiteout Signature (Emergency_Log.doc) | `CLEARANCE_ALPHA` | `CLEARANCE ALPHA`, `CLEARANCEALPHA` | Hidden whiteout credentials in Emergency_Log.doc. Highlight text to reveal `CLEARANCE_ALPHA`. |
| **13** | The ROT-4 IEEE Shift (Encrypted_Beacon.txt) | `ADITIS13` | `ADITI13`, `ADITIS` | Caesar shift of 4 positions backward: `EHMXMW13` -> `ADITIS13`. |
| **14** | The Atbash Cipher Mirror (Mirror_Log.txt) | `PROJECT` | `PROJECTS`, `KILQVBG`, `FAILSAFE` | Reverse alphabet substitution (A<->Z, B<->Y): `KILQVBG` -> `PROJECT`. |
| **15** | The Polybius Coordinate Trail (Matrix_Coordinates.pdf) | `VECTOR` | `VECTORS`, `POLYBIUS` | 5x5 Polybius grid row/col coordinate traversal yields `VECTOR`. |
| **16** | Substring Frequency Count (Mass_System_Log.txt) | `1400` | `14`, `1400X` | Count exact occurrences of keyword `OVERRIDE` (14) multiplied by parity factor 100 = `1400`. |
| **17** | Rogue Chatbot Polybius Shift (Intercepted_ADI_Transmission.pdf) | `VSLXI` | — | Vector-shifted (+1 row, -1 col) Polybius coordinate trail reveals `VSLXI`. |
| **18** | The Modular Clock Loop (Cycle_Diagnostics.png) | `GCBGE` | — | Clock angle and modular step positions decode to `GCBGE`. |
| **19** | The Anomaly Checklist (Server_Status_Check.pdf) | `GAMMA` | — | Isolation of thermal telemetry outlier among server racks identifies cluster `GAMMA`. |
| **20** | The Shift Cipher Matrix (Emergency_Override_Key.txt) | `DAHHK` | — | Columnar shift transposition matrix resolves to authorization token `DAHHK`. |
| **21** | The Log Anomaly Timeline [R1 Finale] (System_Audit_2013.log) | `520` | `104X5`, `104*5` | Chronological audit log interval multiplier ($104 \times 5$) resolves to final Round 1 key `520`. |

---

## 🎯 4. ROUND 2 MASTER ANSWER KEYS (All 17 Olympiad Challenges)

| Puzzle | Codename | Master Key | Alternative Accepted Keys | Mechanism & Volunteer Clue |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Emergency Override | `GUARD` | `EMERGENCY_OVERRIDE` | Terminal directive override keyword `GUARD`. |
| **02** | Visual Matrix Box Transformation | `C` | `THREE CIRCLES`, `3 CIRCLES`, `●●●` | Row 1: Squares, Row 2: Triangles, Row 3: Circles. Count follows 1, 2, 3. Missing cell is 3 Circles (`Option C`). |
| **03** | Spatial Rotation Boxes | `BOTTOM LEFT` | `BL`, `BOTTOMLEFT`, `BOTTOM-LEFT` | Dot rotates 90° clockwise in 2x2 grid: Top-Left -> Top-Right -> Bottom-Right -> `Bottom-Left`. |
| **04** | 3D Cube Net Spatial Folding | `5` | — | T-shaped cross net. Faces separated by one face along vertical spine fold opposite. Face 1 opposite `Face 5`. |
| **05** | Frequency Distribution Anagram | `CIPHER` | — | Frequency cryptanalysis unscrambles 6-letter word: `E-H-I-P-R-C` -> `CIPHER`. |
| **06** | Geometric Grid Progression | `SQUARES` | `3SQ`, `SQUARE`, `THREE SQUARES` | Shape progression across grid quadrant terminates in `SQUARES`. |
| **07** | Quantum Logic Gate Array | `011` | `0,1,1`, `0-1-1` | Truth table output vector across 3 qubits after Hadamard and CNOT operations: `011`. |
| **08** | Vigenère Keyword Substitution | `CLEARANCE` | — | Tabula recta decryption using secret key `TARA` produces `CLEARANCE`. |
| **09** | 8-Point Compass Vector Drift | `SE` | `SOUTH EAST`, `SOUTHEAST` | Navigation telemetry vector sum of gyroscopic drift: North + East + South-East yields net drift `SE`. |
| **10** | Diophantine Residue Equation | `NONE` | `IMPOSSIBLE`, `NO PRIME`, `0` | Parity inspection reveals modular contradiction $p^2 \equiv 2 \pmod 4$; no prime solution exists (`NONE`). |
| **11** | Shifted Polyalphabetic Cipher | `RLRCK` | — | Decryption of 5-letter satellite beacon via key stream index yields `RLRCK`. |
| **12** | Circular Transposition Lattice | `NODC` | — | Spiral reading of 4x4 matrix from outer perimeter inward extracts security token `NODC`. |
| **13** | 3D Hypercube Layer Projection | `102` | `102 BOXES` | Volumetric voxel counting across all 3 spatial cross-sections: 36 + 48 + 18 = `102`. |
| **14** | Binary Inversion State Machine | `3-EMPTY` | `3 EMPTY`, `EMPTY`, `□□□`, `3EMPTY` | Bitwise flip state after 7 clock cycles leaves all 3 registers cleared: `3-EMPTY`. |
| **15** | Anagrammatic Branch Routing | `FINALS` | `EBF` | Unscrambling routing junction nodes (`F-I-N-A-L-S`) yields `FINALS`. |
| **16** | Master StratCom Decryption Wheel | `ECLIPSE` | — | Align inner cipher wheel to 135° marker to decrypt master purge code: `ECLIPSE`. |
| **17** | The Failsafe Logic Tree [Grand Finale] | `0110` | `0-1-1-0`, `0 1 1 0` | Cascading Boolean logic gate evaluation produces master kill-switch vector `0110`. |

---

## 💡 5. Pro-Tips for Volunteers During Tournament

1. **How Participants Submit**:
   - In Round 1, participants can type `decrypt <KEY>` into the bottom terminal prompt, OR click the glowing stage card and type the key into the dossier modal input, OR use the quick-decrypt bar.
   - In Round 2, participants can click any puzzle card in the StratCom grid and enter their solution into the dedicated passcode input box.
2. **Tactical Clues (Battery of 3 — Costs +2:00 Time Penalty per Clue)**:
   - Each squad is allocated exactly 3 Tactical Clues in Round 1.
   - **Time Penalty Rule**: Each clue expended adds an immediate **+2:00 minute (+120 seconds) penalty** to the team's official running mission clock and leaderboard adjusted time.
   - **Confirmation Guard**: Clicking `[ 💡 CLUES LEFT: X/3 ]` or `[ 💡 USE CLUE (+2m) ]` triggers a safety confirmation modal explicitly warning the squad about the +2:00 penalty so clues are never used by mistake.
   - **Visual HUD Feedback**: Once confirmed, the running mission clock leaps forward by 2 minutes, a red `+2m PENALTY` badge pulses on the timer pill, and an alert toast broadcast appears on screen.
   - **Limit**: Only 1 clue can be expended per stage (maximum 3 across all 16 stages). Clues are completely locked in Round 2.
   - **Volunteer Guidance**: Remind participants to conserve clues for the most challenging forensic stages (e.g., Stage 08 Bitplane Stego, Stage 09 Heap Dump, Stage 11 Multi-Condition).
3. **Where to Click Guide**:
   - Both rounds feature a permanent floating button: `🧭 WHERE TO CLICK & SUBMIT (ALL PUZZLES)`.
   - Participants who are visually lost should be directed to click this button or click TARA's `WHERE DO I LOOK?` chip.
4. **Offline Resilience**:
   - Even if venue Wi-Fi drops, the app caches progress and timers locally in `localStorage`.
   - Workstations will not crash or lose progress; they will re-sync with `admin.html` as soon as the connection is re-established.
