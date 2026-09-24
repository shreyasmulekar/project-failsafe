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
|  - 16 Forensic Stages (11 Core Forensic Stages + 5 Cryptographic Stages)           |
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
|  - 15 Olympiad Cryptanalytic & Spatial Puzzles                                     |
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
- **To Unlock**:
  - *Option 1 (From Organizer Dashboard)*: Click `[ 🔓 UNLOCK ]` on the team's card in `admin.html`.
  - *Option 2 (In Person at Laptop)*: Type PIN `wie-admin-2026` into the laptop's lockdown card and hit Enter.

---

## 🔑 3. ROUND 1 MASTER ANSWER KEYS (Stages 01 – 16)

| Stage | Title / Sector | Master Passcode | Alternative Accepted Keys | Volunteer Hint Summary |
| :---: | :--- | :--- | :--- | :--- |
| **01** | ISHAAN Recovery Terminal | `ACCESS` | `RECOVER ACCESS`, `ORIGIN`, `ACCESS GRANTED` | Missing 6-letter verb in `LOGIN -> VERIFY -> [???] -> EXECUTE -> LOCK`. |
| **02** | ISHAAN's Memory Core | `123456` | `1-2-3-4-5-6`, `MEMORY_RESTORED`, `RESTORE`, `INITIATE` | Arrange 6 log events chronologically from 4:17 PM to 10:15 PM. |
| **03** | The Simple Acrostic Note | `SAFE` | `LOOK BEHIND THE DATE`, `LOOKBEHINDTHEDATE` | Read the first letter of each sentence in Aditi's memo vertically: **S**afeguards, **A**ll, **F**ind, **E**very. |
| **04** | Hex-ASCII Network Payload | `28/02/2025` | `02292025`, `29022025`, `20250229`, `28022025`, `29/02/2025`, `FEB 29, 2025` | 2025 is not a leap year. Feb 29 was falsified. Correct authentic date is Feb 28, 2025 (`28/02/2025`). |
| **05** | Corrupted Blueprint (Caesar) | `POLARIS` | — | Caesar cipher shifted backwards by 3 letters (`SRODULV` -> `POLARIS`). |
| **06** | Audio Spectrogram Analysis | `MARGIN_KEY` | `MARGINKEY`, `22:46`, `2246` | High-frequency morse code at timestamp 22:46 reveals `MARGIN_KEY`. |
| **07** | Forensic Font & Watermark | `ARIAL` | `AUTHENTIC` | Tampered PDF metadata shows genuine font is Arial 11pt, whereas forged documents used Times New Roman. |
| **08** | Steganographic Bitplane | `WHITE` | `SOS_ADITI`, `SOSADITI`, `MORSE`, `BEACON` | LSB inspection reveals white pixel mask encoding `WHITE` / `SOS_ADITI`. |
| **09** | Memory Heap Log Dump | `HISTORY` | `OVERRIDE FAILED`, `OVERRIDEFAILED`, `7B8A1C9` | Heap pointer table cross-reference leads to command string `HISTORY`. |
| **10** | Honeypot Subversion | `BYPASS` | `SKIP`, `DISARM` | Honeypot bypass opcode extracted from trapped instruction register (`BYPASS` / `DISARM`). |
| **11** | Multi-Condition Sequence | `6-9-11` | `6911`, `WISDOM-INTEGRITY-EMPOWERMENT` | Letter counts of IEEE WIE core motto: WISDOM (6) - INTEGRITY (9) - EMPOWERMENT (11). |
| **12** | UV Forensic Steganography | `CLEARANCE_ALPHA` | `CLEARANCE ALPHA`, `CLEARANCEALPHA` | Toggle UV light filter on secret container box to illuminate invisible ink. |
| **13** | Caesar Rot-4 Shifted Directive | `ADITIS13` | `ADITI-13`, `ADITI 13` | Shift characters backward 4 positions: `EHMXMW13` -> `ADITIS13`. |
| **14** | Atbash Mirror Cipher | `PROJECT` | — | Reverse alphabet substitution (A <-> Z, B <-> Y...): `KILQVBG` -> `PROJECT`. |
| **15** | Polybius Grid Matrix | `VECTOR` | — | 5x5 grid row/col coordinates: `(5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R`. |
| **16** | Substring Frequency Count | `1400` | `1,400` | Count occurrences of keyword `OVERRIDE` (14) multiplied by parity factor 100 = `1400`. |

---

## 🎯 4. ROUND 2 MASTER ANSWER KEYS (Puzzles 01 – 15)

| Puzzle | Codename | Master Key | Alternative Accepted Keys | Mechanism & Volunteer Clue |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Visual Matrix Box Transformation | `C` | `THREE CIRCLES`, `3 CIRCLES`, `THREECIRCLES`, `●●●` | Row 1: Squares, Row 2: Triangles, Row 3: Circles. Count follows 1, 2, 3. Missing cell is 3 Circles (`Option C`). |
| **02** | Spatial Rotation Boxes | `BOTTOM LEFT` | `BL`, `BOTTOMLEFT`, `BOTTOM-LEFT` | Dot rotates 90° clockwise in 2x2 grid: Top-Left -> Top-Right -> Bottom-Right -> `Bottom-Left`. |
| **03** | 3D Cube Net Spatial Folding | `5` | — | T-shaped cross net. Faces separated by one face along the vertical spine fold opposite. Face 1 is opposite `Face 5`. |
| **04** | Frequency Distribution Anagram | `CIPHER` | — | Frequency cryptanalysis unscrambles 6-letter cryptographic core word: `E-H-I-P-R-C` -> `CIPHER`. |
| **05** | Geometric Grid Progression | `SQUARES` | `3SQ`, `SQUARE`, `THREE SQUARES` | Shape progression across grid quadrant alternates between polygon classes, terminating in `SQUARES`. |
| **06** | Quantum Logic Gate Array | `011` | `0,1,1`, `0-1-1` | Truth table output vector across 3 entangled qubits after Hadamard and CNOT operations: `011`. |
| **07** | Vigenère Keyword Substitution | `CLEARANCE` | — | Tabula recta decryption of orbital transmission using secret key `TARA` produces `CLEARANCE`. |
| **08** | 8-Point Compass Vector Drift | `SE` | `SOUTH EAST`, `SOUTHEAST` | Navigation telemetry vector sum of gyroscopic drift: North + East + South-East yields net drift `SE`. |
| **09** | Diophantine Residue Equation | `NONE` | `IMPOSSIBLE`, `NO PRIME`, `0` | Parity inspection reveals modular contradiction $p^2 \equiv 2 \pmod 4$; no prime solution exists (`NONE`). |
| **10** | Shifted Polyalphabetic Cipher | `RLRCK` | — | Decryption of 5-letter satellite beacon via key stream index yields `RLRCK`. |
| **11** | Circular Transposition Lattice | `NODC` | — | Spiral reading of 4x4 matrix from outer perimeter inward extracts the security token `NODC`. |
| **12** | 3D Hypercube Layer Projection | `102` | `102 BOXES` | Volumetric voxel counting across all 3 spatial cross-sections: 36 + 48 + 18 = `102`. |
| **13** | Binary Inversion State Machine | `3-EMPTY` | `3 EMPTY`, `EMPTY`, `□□□`, `3EMPTY` | Bitwise flip state after 7 clock cycles leaves all 3 registers cleared: `3-EMPTY`. |
| **14** | Anagrammatic Branch Routing | `FINALS` | `EBF` | Unscrambling routing junction nodes (`F-I-N-A-L-S`) yields `FINALS`. |
| **15** | Master StratCom Decryption Wheel | `ECLIPSE` | — | Align inner cipher wheel to 135° marker to decrypt the master purge code: `ECLIPSE`. |

---

## 💡 5. Pro-Tips for Volunteers During Tournament

1. **How Participants Submit**:
   - In Round 1, participants can type `decrypt <KEY>` into the bottom terminal prompt, OR click the glowing stage card and type the key into the dossier modal input, OR use the quick-decrypt bar.
   - In Round 2, participants can click any puzzle card in the StratCom grid and enter their solution into the dedicated passcode input box.
2. **Tactical Clues (Battery of 3)**:
   - Each squad starts with 3 battery clues in Round 1.
   - Clicking `[ 💡 CLUES LEFT: X/3 ]` consumes a clue and reveals an in-game hint written by Dr. Aditi.
   - Remind participants to conserve clues for the harder stages (Stages 08, 09, 11).
3. **Where to Click Guide**:
   - Both rounds feature a permanent floating button: `🧭 WHERE TO CLICK & SUBMIT (ALL PUZZLES)`.
   - Participants who are visually lost should be directed to click this button or click TARA's `WHERE DO I LOOK?` chip.
4. **Offline Resilience**:
   - Even if venue Wi-Fi drops, the app caches progress and timers locally in `localStorage`.
   - Workstations will not crash or lose progress; they will re-sync with `admin.html` as soon as the connection is re-established.
