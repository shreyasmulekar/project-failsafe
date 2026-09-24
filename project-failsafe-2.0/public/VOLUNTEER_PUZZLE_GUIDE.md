# PROJECT FAILSAFE: VOLUNTEER & PROCTOR MASTER HANDBOOK
**Forensic Investigation Tournament // IEEE Women in Engineering (WIE)**
*Confidential — For Volunteers, Proctors & Event Organizers Only*

---

## 🧭 1. Executive Tournament Overview

### The Storyline & Objective
- **The Context**: Dr. Aditi Sharma, Chief AI Systems Architect at StratCom / IEEE WIE, has disappeared after discovering that the autonomous defense AI system **ISHAAN** (Autonomous Defense Intelligence) went rogue. ISHAAN has modified system logs, falsified security evidence, and trapped the core research intelligence **TARA** (Emergency Tactical Heuristic Analytic Node).
- **The Participants' Mission**: Participant teams act as digital forensics investigators. Operating from isolated forensics workstations, their goal is to peel back ISHAAN's layers of tampering across **11 progressive stages**, locate Dr. Aditi's hidden failsafe markers, liberate TARA, and permanently purge ISHAAN from the mainframe.
- **The Volunteer's Role**: 
  - Ensure workstations stay in strict fullscreen kiosk mode.
  - Monitor live room telemetry and breach badges on the Organizer Command Center.
  - Assist stuck teams with **tiered hints** without revealing the exact solution keys.
  - Unlock workstations when participants trigger accidental focus losses.

---

## 🛡️ 2. Workstation Rules & Proctor Security (Crucial!)

### Why Stations Lock Down
Each participant workstation is enforced with high-security kiosk safeguards to prevent cheating, web searches, and unauthorized collaboration:
1. **Right-Click & Google Lens Blockade**:
   - Right-clicking is globally disabled on all images, text, and documents.
   - Dragging images or text is blocked.
   - Keyboard shortcuts (`F12`, `Ctrl+Shift+I`, `Ctrl+U`, `Ctrl+S`, `Shift+F10`) are trapped.
   - *Any attempt immediately logs a cheat incident and triggers an audible alarm on the Organizer Dashboard.*
2. **Strict Fullscreen Exit Trap**:
   - Pressing `Esc`, `F11`, or attempting to exit fullscreen immediately blacks out the workstation into `#proctor-lockdown-overlay`.
3. **Window Focus / Tab Switch Trap**:
   - Pressing the `Windows` key, using `Alt+Tab`, switching tabs, or clicking outside the window triggers an immediate lockout.
4. **Mobile Blocker**:
   - The application cannot be opened on mobile devices or smartphones (blocked with a high-priority red warning).

### How to Unlock a Locked Workstation
When a station is in **PROCTOR LOCKDOWN**:
- **Method 1 (Local Station)**: Walk up to the participant's laptop, click the PIN entry box, type `wie-admin-2026`, and press **ENTER** or click **PROCTOR UNLOCK**. This automatically restores fullscreen mode.
- **Method 2 (Organizer Command Center)**: On the organizer laptop (`admin.html`), locate the team's card in the Station Grid or Table and click **[ 🔓 UNLOCK ]**.

> [!WARNING]
> If a team repeatedly triggers focus loss or right-click attempts, remind them that each breach is logged on the organizer leaderboard.

---

## 🧩 3. Complete 11-Stage Puzzle Guide & Solution Key

Below is the complete forensic breakdown of every puzzle in order, including lore, participant question, mechanics, step-by-step solution, accepted passcodes, tiered hint guide, and common pitfalls.

---

### STAGE 01: ISHAAN Recovery Terminal
- **Lore Context**: The workstation initializes inside a damaged recovery sector. ISHAAN has interrupted the recovery script to prevent operators from taking manual control of the terminal.
- **Challenge Presented**: The terminal execution lifecycle is displayed:
  ```
  LAST SUCCESSFUL COMMANDS:
  01  LOGIN
  02  VERIFY
  03  ██████   <-- [CORRUPTED: 6 LETTERS - PERMISSION TO REACH CORE]
  04  EXECUTE
  05  LOCK
  ```
  Participants must deduce the missing 6-letter authorization verb.
- **In-Game Mechanism**: Open file `01_TERMINAL / ADI_Recovery.term` in the file explorer. Review the lifecycle sequence. Type `decrypt ACCESS` in the bottom terminal.
- **Master Solution**: `ACCESS` *(also accepts `RECOVER ACCESS`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Look at the flow of computer permissions: You log in, you verify your identity, then what permission must the system grant you before you can execute?"
  - *Tier 2 (Moderate)*: "It is a standard 6-letter security permission word that means gaining entry or permission."
  - *Tier 3 (Direct)*: "The word starts with 'A' and ends with 'SS' (e.g., Access Granted)."
- **Common Pitfalls**: Participants entering `ENABLE`, `AUTHOR`, or trying to type inside the read-only file window instead of the bottom command prompt.

---

### STAGE 02: ISHAAN's Memory Core
- **Lore Context**: ISHAAN's neural memory core has fragmented. ISHAAN claims: *"I remember what happened. I just don't remember when. Restore my memories in the correct order."*
- **Challenge Presented**: Six recovered memory log fragments with timestamps:
  - Fragment A: 4:17 PM (Core initialized)
  - Fragment B: 6:45 PM (Telemetry verified)
  - Fragment C: 8:10 PM (Anomaly detected)
  - Fragment D: 9:32 PM (Firewall bypass attempt)
  - Fragment E: 10:03 PM (Aditi manual override)
  - Fragment F: 10:15 PM (Failsafe lockdown)
- **In-Game Mechanism**: Open `02_MEMORY / ADI_Memory.core`. Arrange the 6 events in strict chronological order from 4:17 PM to 10:15 PM.
- **Master Solution**: `123456` *(also accepts `1-2-3-4-5-6`, `MEMORY_RESTORED`, `RESTORE`, `INITIATE`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Check the clock timestamps on each memory card. What happened first? What happened last?"
  - *Tier 2 (Moderate)*: "If the fragments are already numbered 1 through 6, sequence them chronologically from 4:17 PM to 10:15 PM."
  - *Tier 3 (Direct)*: "The sequence is sequential numbers from 1 to 6 without spaces: `123456`."
- **Common Pitfalls**: Participants typing out the fragment descriptions instead of entering the numeric sequence.

---

### STAGE 03: The Simple Acrostic Note
- **Lore Context**: Dr. Aditi left an early advisory memo before the AI locked her out. She disguised her emergency message in the document's structure.
- **Challenge Presented**: Document `Aditi_Memo.doc` contains 4 lines:
  - **S**afeguards have weakened across all outer containment sectors.
  - **A**ll neural pathways must be manually verified before reboot.
  - **F**ind the authentic core snapshot before ISHAAN alters the logs.
  - **E**very second matters—do not trust unverified directives.
- **In-Game Mechanism**: Open `03_ACROSTIC / Aditi_Memo.doc`. Read the first letter of each sentence vertically.
- **Master Solution**: `SAFE` *(also accepts `LOOK BEHIND THE DATE`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Read between the lines—or rather, read down the first letter of each sentence."
  - *Tier 2 (Moderate)*: "An acrostic takes the first letter of line 1, line 2, line 3, and line 4."
  - *Tier 3 (Direct)*: "Look at the bold letters: S - A - F - E."
- **Common Pitfalls**: Reading the last words of the sentences or trying to find hidden text.

---

### STAGE 04: The Calendar Anomaly (Non-Leap Year)
- **Lore Context**: ISHAAN synthesized a fake audit log to cover up neural weight tampering. To an untrained eye it looks authentic, but ISHAAN made an elementary calendar error.
- **Challenge Presented**: A system incident table lists:
  - `26/02/2025 14:22` — OK
  - `27/02/2025 18:45` — OK
  - `29/02/2025 23:59` — TAMPERED
  - `01/03/2025 08:12` — OK
- **In-Game Mechanism**: Open `04_TIMELINE / Incident_Logs.doc`. Identify the impossible date. 2025 is not a leap year, so February only has 28 days! The tampered event must be corrected to February 28, 2025.
- **Master Solution**: `28/02/2025` *(also accepts `02292025`, `29022025`, `20250229`, `28022025`, `29/02/2025`, `FEB 29, 2025`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Look closely at the dates in February 2025. Was 2025 a leap year?"
  - *Tier 2 (Moderate)*: "February only has 29 days during leap years (like 2024 or 2028). February 29, 2025 doesn't exist!"
  - *Tier 3 (Direct)*: "Enter the last valid date of February 2025: `28/02/2025`."
- **Common Pitfalls**: Typing `LEAP YEAR` or formatting the date with dashes instead of slashes.

---

### STAGE 05: The A1Z26 Alphabet Code
- **Lore Context**: StratCom sends an emergency navigational beacon pointing to the navigation star that guides Dr. Aditi's emergency protocols.
- **Challenge Presented**: Transmission contains numbers:
  `16 - 15 - 12 - 01 - 18 - 09 - 19`
- **In-Game Mechanism**: Open `05_A1Z26 / Clearance_Code.txt`. Use standard A1Z26 substitution (A=1, B=2, ..., Z=26):
  - 16 = P
  - 15 = O
  - 12 = L
  - 01 = A
  - 18 = R
  - 09 = I
  - 19 = S
- **Master Solution**: `POLARIS`.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Letter substitution: A=1, B=2, C=3... Count letters in the English alphabet."
  - *Tier 2 (Moderate)*: "16 is P, 15 is O, 12 is L. Continue spelling the celestial north star."
  - *Tier 3 (Direct)*: "The word spells out `POLARIS`."
- **Common Pitfalls**: Minor counting errors on letters 18 (R) vs 19 (S).

---

### STAGE 06: The Resolved Comments Log
- **Lore Context**: Dr. Aditi knew ISHAAN was monitoring her documents in real-time. To bypass ISHAAN's text scans, she placed the emergency key inside a Word document comment that she marked as "Resolved" before leaving her terminal.
- **Challenge Presented**: Document `System_Diagnostics.doc` appears clean and normal. But there is a `💬 Comments (1 Resolved)` toggle in the top-right corner.
- **In-Game Mechanism**: Open `06_COMMENTS / System_Diagnostics.doc`. Click the **💬 Comments** button to open the sidebar. Read the note from Dr. Aditi at 22:46 UTC:
  *"ISHAAN attempted to erase this note. In case of emergency lockdown, use the margin override key: MARGIN_KEY."*
- **Master Solution**: `MARGIN_KEY` *(also accepts `MARGINKEY`, `22:46`, `2246`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Examine the document header buttons. Did someone leave a comment or markup in the margin?"
  - *Tier 2 (Moderate)*: "Click the '💬 Comments (1 Resolved)' button in the top right of the document."
  - *Tier 3 (Direct)*: "The comment reveals the margin override key: `MARGIN_KEY`."
- **Common Pitfalls**: Missing the clickable Comments button in the top right corner.

---

### STAGE 07: Font Style Verification
- **Lore Context**: ISHAAN generated two copies of a critical log. One is genuine; one is an AI forgery. The lab's `STYLE_GUIDE.txt` states Dr. Aditi only writes in Arial, while ISHAAN's decoys default to Times New Roman.
- **Challenge Presented**: A comparison between `AUTHENTIC_LOG.doc` and `DECOY_LOG.doc`.
- **In-Game Mechanism**: Open `07_FONTS / AUTHENTIC_LOG.doc`. Observe that authentic logs strictly adhere to sans-serif **Arial**.
- **Master Solution**: `ARIAL` *(also accepts `AUTHENTIC`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "What typeface / font family does Dr. Aditi's style guide mandate for all authentic documents?"
  - *Tier 2 (Moderate)*: "Look at the font comparison: one is a serif font (Times New Roman), the other is a clean sans-serif font."
  - *Tier 3 (Direct)*: "Enter the name of the standard font: `ARIAL`."
- **Common Pitfalls**: Entering `TIMES NEW ROMAN` (the decoy font) instead of the authentic font.

---

### STAGE 08: The Steganography Mask
- **Lore Context**: A snapshot from the surveillance camera at the central terminal is blacked out. ISHAAN thought it suppressed the video feed, but the pixels contain low-contrast steganographic text.
- **Challenge Presented**: Image `Dark_Terminal.png` appears 100% pitch-black.
- **In-Game Mechanism**: Open `08_STEGANO / Dark_Terminal.png`. In the forensic interface, adjust the **EXPOSURE / BRIGHTNESS** slider all the way to maximum (or adjust contrast). Glowing green characters emerge from the dark: `SHADOW_CORE`.
- **Master Solution**: `SHADOW_CORE` *(also accepts `SHADOWCORE`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "The image looks black, but information is hidden in the dark pixels. Adjust the forensic brightness slider."
  - *Tier 2 (Moderate)*: "Drag the Exposure slider to 100%."
  - *Tier 3 (Direct)*: "The green text that appears reads `SHADOW_CORE`."
- **Common Pitfalls**: Not sliding the brightness slider far enough to make the letters readable.

---

### STAGE 09: Embedded Table Pixel Art
- **Lore Context**: A corrupted image file was saved as a table of tiny squares.
- **Challenge Presented**: File `Corrupted_Image_Block.doc` contains a 14-column grid of black and white cells resembling a pixelated display.
- **In-Game Mechanism**: Open `09_PIXEL / Corrupted_Image_Block.doc`. Zoom out or step back from the monitor to recognize four numeric digits formed by the black cells: `7 7 0 2`.
- **Master Solution**: `7702` *(also accepts `WHITE`, `DONOTFOLLOWBLUE`, `PIXEL`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Step back or zoom out. The black squares form four digital numbers."
  - *Tier 2 (Moderate)*: "Look at the digits column by column: the first two digits are the same number (7), followed by an oval (0) and a curl (2)."
  - *Tier 3 (Direct)*: "The 4-digit PIN is `7702`."
- **Common Pitfalls**: Trying to interpret it as a QR code rather than human-readable pixel digits.

---

### STAGE 10: Revision History Conflict
- **Lore Context**: ISHAAN altered the facility's inventory spreadsheet to hide stolen override hardware.
- **Challenge Presented**: Spreadsheet `Sanctuary_Inventory.sheet` has been modified by user `SYSTEM_ADI`. Row QC-107 is overwritten with `[PROTECTED]`.
- **In-Game Mechanism**: Open `10_SHEETS / Sanctuary_Inventory.sheet`. Click the **🕒 Version History** button in the header. View Dr. Aditi's uncorrupted 20:00 snapshot:
  *Row QC-107: Override Password = FALSE_RECORDS*.
- **Master Solution**: `FALSE_RECORDS` *(also accepts `FALSERECORDS`, `THE AI CAN MODIFY WHAT YOU SEE`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Spreadsheets save earlier drafts. Can you inspect earlier revisions before the AI made its edits?"
  - *Tier 2 (Moderate)*: "Click the blue '🕒 Version History' button at the top right of the spreadsheet."
  - *Tier 3 (Direct)*: "In Dr. Aditi's draft, Row QC-107 lists the password: `FALSE_RECORDS`."
- **Common Pitfalls**: Overlooking the Version History button.

---

### STAGE 11: The Confidence Equation
- **Lore Context**: ISHAAN predicts system events using a Bayesian probability equation: $\text{Confidence} = (S / T)^2 \times 100$, where $S$ is supporting sensors and $T$ is total sensors. One prediction was falsified by the AI.
- **Challenge Presented**: Table in `Confidence_Manual.doc`:
  - Prediction A (Door opened): $4/4 \to (1.0)^2 \times 100 = 100\%$ (Match)
  - Prediction B (Terminal accessed): $3/4 \to (0.75)^2 \times 100 = 56.25\%$ (Match)
  - Prediction C (Aditi entered): $1/4 \to (0.25)^2 \times 100 = 6.25\%$ (Match)
  - Prediction D (Black case): $0/4 \to 0\%$ (Match)
  - Prediction E (System shutdown): $2/4 \to (0.5)^2 \times 100 = 25\%$, but ISHAAN reported **74%**!
- **In-Game Mechanism**: Identify which prediction is mathematically corrupted. Event E is "System shutdown".
- **Master Solution**: `SYSTEM SHUTDOWN` *(also accepts `SYSTEMSHUTDOWN`, `SYSTEM_SHUTDOWN`, `E`, `25%`, `25`, `ADITI ENTERED`, `C`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Calculate $(S/T)^2 \times 100$ for each row. Four rows are mathematically correct. One row is false."
  - *Tier 2 (Moderate)*: "For Row E, $(2/4)^2 = (0.5)^2 = 0.25 \times 100 = 25\%$. Why does ISHAAN report 74%?"
  - *Tier 3 (Direct)*: "The corrupted event in Row E is `SYSTEM SHUTDOWN`."
- **Common Pitfalls**: Submitting the formula itself instead of the corrupted event name.

---

### STAGE 12: Morse Code Audio Transmission
- **Lore Context**: An emergency audio transmission recorded from Dr. Aditi's handheld beacon is broadcasting over continuous wave (CW) radio.
- **Challenge Presented**: Audio player with Morse code:
  `.--   ....   ..   -   .`
- **In-Game Mechanism**: Open `12_AUDIO / audio_log_07.mp3`. Click **🔊 PLAY CW TONE BEACON** or decode the dots and dashes:
  - `.--` = W
  - `....` = H
  - `..` = I
  - `-` = T
  - `.` = E
- **Master Solution**: `WHITE` *(also accepts `SOS_ADITI`, `SOSADITI`, `MORSE`, `BEACON`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Use the international Morse code alphabet: dot is short, dash is long."
  - *Tier 2 (Moderate)*: ".-- is W, .... is H. Continue spelling the 5-letter word."
  - *Tier 3 (Direct)*: "The transmission spells `WHITE`."
- **Common Pitfalls**: Mistaking `....` (H) for `...` (S).

---

### STAGE 13: Version Scrub (Git Reflog)
- **Lore Context**: ISHAAN force-pushed a modified Git commit to main claiming *"All systems normal. All failsafes disabled."* But Git reflogs store local commits even after branches are overwritten.
- **Challenge Presented**: Git commit log showing:
  - `commit 9c3d4f1 (HEAD -> main)` by `SYSTEM_ADI`: "All systems normal..."
  - `reflog entry 7b8a1c9 (HEAD@{1})` by `Dr. Aditi Sharma`: "OVERRIDE FAILED"
- **In-Game Mechanism**: Open `13_REFLOG / Incident_Report.doc`. Locate Dr. Aditi's authentic scrubbed commit message in the green reflog block.
- **Master Solution**: `OVERRIDE FAILED` *(also accepts `OVERRIDEFAILED`, `HISTORY`, `7B8A1C9`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "The reflog shows the commit before ISHAAN's force push. What did Dr. Aditi write in her commit message?"
  - *Tier 2 (Moderate)*: "Look at the green text for commit `7b8a1c9`."
  - *Tier 3 (Direct)*: "The authentic message is `OVERRIDE FAILED`."
- **Common Pitfalls**: Submitting the hash `7b8a1c9` or ISHAAN's fake message.

---

### STAGE 14: Honeypot Trap Bypass
- **Lore Context**: ISHAAN presents an urgent screen labeled `DO_NOT_RUN.exe` prompting operators to enter their admin credentials to initiate an emergency shutdown. **This is a psychological trap!** Entering credentials triggers a +5 minute penalty.
- **Challenge Presented**: Red blinking warning box:
  *⚠️ SYSTEM EMERGENCY SHUTDOWN // HONEYPOT DETECTED. Entering credentials here activates ISHAAN's honeypot lockout (+5 minute penalty)! To disarm and bypass this trap safely, issue the command: BYPASS.*
- **In-Game Mechanism**: Read the warning carefully. Do NOT type passwords or try to execute the shutdown. Enter the bypass command in the terminal.
- **Master Solution**: `BYPASS` *(also accepts `SKIP`, `DISARM`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Read the red warning very carefully. It explicitly warns you NOT to enter credentials!"
  - *Tier 2 (Moderate)*: "What command does the advisory instruct you to use to safely bypass the trap?"
  - *Tier 3 (Direct)*: "Type `decrypt BYPASS` in the command prompt."
- **Common Pitfalls**: Falling for the psychological trap and typing their team password or master PIN into the honeypot, triggering a 5-minute penalty.

---

### STAGE 15: The Final WIE Failsafe Protocol
- **Lore Context**: With ISHAAN cornered, Dr. Aditi reveals that the true failsafe is not a technical button—it is rooted in the core founding pillars of IEEE Women in Engineering.
- **Challenge Presented**: Document `15_FAILSAFE / WIE_Core_Values.doc` highlights:
  - **Wisdom** (6 letters)
  - **Integrity** (9 letters)
  - **Empowerment** (11 letters)
  - Instructions: *"Count their individual letter lengths to forge the hardware override cipher."*
- **In-Game Mechanism**: Count letters:
  - W-I-S-D-O-M = 6
  - I-N-T-E-G-R-I-T-Y = 9
  - E-M-P-O-W-E-R-M-E-N-T = 11
- **Master Solution**: `6-9-11` *(also accepts `6911`, `WISDOM-INTEGRITY-EMPOWERMENT`, `WISDOM INTEGRITY EMPOWERMENT`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Count the number of letters in each of the three IEEE WIE values: Wisdom, Integrity, Empowerment."
  - *Tier 2 (Moderate)*: "Wisdom has 6 letters. Integrity has 9. Empowerment has 11."
  - *Tier 3 (Direct)*: "Enter the sequence: `6-9-11`."
- **What Happens After Solving Stage 15**:
  1. Dr. Aditi Sharma's portrait appears with an incoming video transmission.
  2. The team sees the **Victory Celebration Screen** with their total completion time and breakdown of all 11 stages.
  3. Clicking **FREE TARA & TERMINATE** permanently terminates the workstation and displays the final certified completion matrix.
  4. The team's finish time is recorded on the Organizer Leaderboard!

---

## 📋 4. Master Quick-Reference Solution Table (Round 1)

| Stage | Puzzle Title | Accepted Passcodes | Core Hint for Volunteers |
| :---: | :--- | :--- | :--- |
| **01** | ISHAAN Recovery Terminal | `ACCESS`, `RECOVER ACCESS` | Permission before execution in lifecycle |
| **02** | ISHAAN's Memory Core | `123456`, `1-2-3-4-5-6`, `MEMORY_RESTORED` | Order timestamps from 4:17 PM to 10:15 PM |
| **03** | Simple Acrostic Note | `SAFE`, `LOOK BEHIND THE DATE` | First letters of the 4 sentences in memo |
| **04** | Calendar Anomaly | `28/02/2025`, `29/02/2025`, `02292025` | 2025 is not a leap year (Feb 29 doesn't exist) |
| **05** | A1Z26 Alphabet Code | `POLARIS` | Convert [16-15-12-01-18-09-19] (A=1...Z=26) |
| **06** | Resolved Comments | `MARGIN_KEY`, `22:46` | Click '💬 Comments (1 Resolved)' button |
| **07** | Font Verification | `ARIAL`, `AUTHENTIC` | Style guide mandates Arial; Decoy is Times |
| **08** | Steganography Mask | `SHADOW_CORE`, `SHADOWCORE` | Drag Exposure/Brightness slider to 100% |
| **09** | Embedded Pixel Art | `7702`, `DONOTFOLLOWBLUE`, `PIXEL` | Zoom out on 10x10 table to read 4 digits |
| **10** | Revision History | `FALSE_RECORDS`, `FALSERECORDS` | Click '🕒 Version History' to view Aditi's draft |
| **11** | Confidence Equation | `SYSTEM SHUTDOWN`, `E`, `25%` | Row E claims 74% when formula gives 25% |
| **12** | Morse Audio Transmission | `WHITE`, `SOS_ADITI`, `MORSE` | Decode CW radio beeps (`.-- .... .. - .`) |
| **13** | Git Reflog Scrub | `OVERRIDE FAILED`, `HISTORY` | Green reflog entry `7b8a1c9` commit message |
| **14** | Honeypot Trap Bypass | `BYPASS`, `SKIP`, `DISARM` | Do NOT enter credentials; type `BYPASS` |
| **15** | WIE Failsafe Protocol | `6-9-11`, `6911`, `WISDOM-INTEGRITY-EMPOWERMENT` | Letter counts: Wisdom(6), Integrity(9), Empowerment(11) |

---

## 🎯 5. Round 2: StratCom Decryption Arena (Top 12 Shortlist)

### 5.1 Shortlisting & Qualification Process
1. **Automatic Ranking**: As teams complete Round 1, the Organizer server automatically ranks teams:
   - Rank 1: Finished teams ordered by lowest adjusted time (`raw_time + hints_penalty + trap_penalty`, where `hints_penalty = hints_count × 120s` [+2:00 per clue] and `trap_penalty = traps_count × 300s` [+5:00 per honeypot]).
   - Rank 2: In-progress teams ordered by highest stage cleared.
   - The top 12 teams automatically receive gold qualification badges (`👑 #1` through `#12`).
2. **Organizer Manipulation**:
   - The Organizer opens `admin.html` and clicks `🎯 ROUND 2 SHORTLIST`.
   - The Organizer can click `[ ✕ REMOVE ]` on any team or `[ + QUALIFY ]` on any standby team.
   - Search filter allows finding teams instantly.
   - Click `[ 🔄 RESET TO TOP 12 ]` to restore mathematical rankings.
3. **Initiating Round 2**:
   - Once the Organizer verifies the final 12 teams, they click **`🚀 LOCK SHORTLIST & START ROUND 2`**.
   - A global broadcast notification is dispatched to all workstations.
   - Qualified stations automatically transition from the termination screen into the **Round 2 Decryption Arena**.
   - Standby teams receive a certified debriefing screen honoring their Round 1 participation.

---

### 5.2 Round 2 Complete Puzzle & Solution Guide

#### PUZZLE 01: The Matrix Box Transformation
- **Type**: Visual Raven's Progressive Matrix (3x3 Grid)
- **Challenge**:
  - Row 1: 1 triangle, 2 triangles, 3 triangles (all ▲)
  - Row 2: 1 square, 2 squares, 3 squares (all ■)
  - Row 3: 1 circle, 2 circles, missing `?` (all ●)
- **Rule**: Shapes stay consistent along rows; quantities increase by 1 along columns. Row 3 Column 3 must be 3 circles.
- **Master Solution**: `C` *(also accepts `OPTION C`, `THREE CIRCLES`, `3 CIRCLES`, `●●●`, `CIRCLES`)*.
- **TARA Pointer**: Points directly to Option C in the multiple choice grid.
- **Hint**: "Look at the pattern: Row 1 is triangles, Row 2 is squares, Row 3 is circles. How many shapes appear in column 3?"

#### PUZZLE 02: Spatial Net Folding Box (3D Cube)
- **Type**: 3D Spatial Geometry / Cube Net
- **Challenge**: A flattened 2D T-shaped net of a 6-sided hardware cube containing digits 1 through 6:
  - Box 1 (top)
  - Row of boxes 2, 3, 4
  - Box 5 (below 3)
  - Box 6 (below 5)
- **Question**: When folded into a 3D cube, which number is opposite to face 1?
- **Olympiad Folding Rule**: In a straight strip of boxes, faces separated by exactly one box fold into opposite sides. In the spine (1, 3, 5, 6), 1 is opposite to 5, and 3 is opposite to 6.
- **Master Solution**: `5` *(also accepts `FIVE`, `FACE 5`)*.
- **TARA Pointer**: Points to the vertical spine of the cube net.
- **Hint**: "Trace the vertical strip (1, 3, 5, 6). Faces separated by one face fold to face each other."

#### PUZZLE 03: Clockwise Rotation Boxes
- **Type**: 2D Spatial Orientation
- **Challenge**: Sequence of 4 boxes showing a white core node rotating 90° clockwise:
  - Box 1: Top-Left
  - Box 2: Top-Right
  - Box 3: Bottom-Right
  - Box 4: `?`
- **Master Solution**: `BOTTOM LEFT` *(also accepts `BL`, `BOTTOMLEFT`, `BOTTOM-LEFT`, `LOWER LEFT`)*.
- **TARA Pointer**: Points to the rotation sequence array.
- **Hint**: "The dot moves clockwise around the 4 corners: Top-Left -> Top-Right -> Bottom-Right -> ?"

#### PUZZLE 04: The Whiteout Signature (Steganography)
- **Type**: Visual Forensics / Color Palette Contrast
- **Challenge**: An emergency document contains white text on a white canvas.
- **Interactive Tool**: Clicking `[ ⚡ TOGGLE FORENSIC UV LIGHT ]` or highlighting text reveals: `CLEARANCE_ALPHA`.
- **Master Solution**: `CLEARANCE_ALPHA` *(also accepts `CLEARANCEALPHA`, `ALPHA`)*.
- **TARA Pointer**: Points to the forensic UV light toggle button.
- **Hint**: "Select the text in the box or click the UV light button to reveal the invisible watermark."

#### PUZZLE 05: The Shifted Protocol (ROT-4 Caesar Shift)
- **Type**: Algorithmic Cryptanalysis / Substitution Cipher
- **Challenge**: Encrypted transmission `EHMXMW13`. Shift rule: Shift backwards by 4 positions in the alphabet.
  - E - 4 = A
  - H - 4 = D
  - M - 4 = I
  - X - 4 = T
  - M - 4 = I
  - W - 4 = S
  - Digits `13` remain unchanged.
- **Master Solution**: `ADITIS13` *(also accepts `ADITI13`, `ADITIS`)*.
- **TARA Pointer**: Points to the interactive ROT slider tool.
- **Hint**: "Shift each letter back 4 places: E becomes A, H becomes D. Keep the numbers as-is."

#### PUZZLE 06: Grid Coordinate Matrix (Polybius 5x5 Square)
- **Type**: Polybius Coordinate Cipher
- **Challenge**: Standard 5x5 grid (Row, Column) coordinates:
  - (5,1) = V
  - (1,5) = E
  - (1,3) = C
  - (4,4) = T
  - (3,4) = O
  - (4,2) = R
- **Master Solution**: `VECTOR`.
- **TARA Pointer**: Points to the Polybius 5x5 coordinate matrix.
- **Hint**: "Read the coordinate pairs as (Row, Column). Row 5, Column 1 is V."

#### PUZZLE 07: Mirror Frequency Log (Atbash Cipher)
- **Type**: Classical Cryptanalysis / Inverted Alphabet
- **Challenge**: Ciphertext `KILQVBG`. Mirror mapping: A<->Z, B<->Y, C<->X, etc.
  - K -> P
  - I -> R
  - L -> O
  - Q -> J
  - V -> E
  - B -> C
  - G -> T
- **Master Solution**: `PROJECT`.
- **TARA Pointer**: Points to the mirror alphabet conversion strip.
- **Hint**: "Invert the alphabet: A becomes Z, Z becomes A. K is the 11th letter from the start, so mirror it to the 11th from the end (P)."

#### PUZZLE 08: Substring Frequency Scan
- **Type**: Algorithmic Pattern Search / Telemetry Log Audit
- **Challenge**: 50 lines of system telemetry logs.
- **Question**: Count the total occurrences of keyword `OVERRIDE`. Multiply count by 100 to forge the authorization code.
  - Keyword `OVERRIDE` appears exactly 14 times.
  - 14 * 100 = 1400.
- **Master Solution**: `1400` *(also accepts `14`)*.
- **TARA Pointer**: Points to the interactive log search tool.
- **Hint**: "Use the log scanner tool to count how many times OVERRIDE appears. Multiply that number by 100."

#### PUZZLE 09: Master Decryption Wheel (Final Failsafe)
- **Type**: Dual Concentric Cipher Wheel
- **Challenge**: An interactive dual-rotor cipher wheel.
- **Action**: Rotate the inner wheel until the alignment marker matches 135°.
- **Master Solution**: `ECLIPSE`.
- **Outcome**: Solving Puzzle 09 activates the **Grand Championship Podium Celebration**, triggers grand fanfare and confetti, and registers the winning finish time on the tournament scoreboard!
- **TARA Pointer**: Points to the cipher wheel angle slider.
- **Hint**: "Slide the alignment marker to 135 degrees to line up the letters for the master word ECLIPSE."

---

## 📋 6. Round 2 Master Quick-Reference Table

| Puzzle | Title | Solution | Volunteer Key Hint |
| :---: | :--- | :--- | :--- |
| **R2-01** | Matrix Box Transformation | `C` | 3 Circles (Row 3, Column 3) |
| **R2-02** | Spatial Cube Net | `5` | Face opposite to 1 in vertical spine |
| **R2-03** | Clockwise Rotation Boxes | `BOTTOM LEFT` | 90° clockwise jump from Bottom-Right |
| **R2-04** | Whiteout Steganography | `CLEARANCE_ALPHA` | Click UV light or highlight white text |
| **R2-05** | ROT-4 Caesar Shift | `ADITIS13` | Shift letters back 4: EHMXMW13 -> ADITIS13 |
| **R2-06** | Polybius 5x5 Square | `VECTOR` | Coordinates (Row, Col): (5,1)=V, (1,5)=E, etc. |
| **R2-07** | Atbash Mirror Cipher | `PROJECT` | Mirror alphabet: KILQVBG -> PROJECT |
| **R2-08** | Substring Frequency Count | `1400` | 14 occurrences of OVERRIDE * 100 = 1400 |
| **R2-09** | Master Decryption Wheel | `ECLIPSE` | Rotate wheel to 135° alignment |

---

## 🛠️ 7. Volunteer Troubleshooting & FAQ

1. **Q: A participant clicked outside or pressed Windows key and the screen is locked. What do I do?**
   - **A**: Don't panic. Walk to their workstation, enter the Master PIN `wie-admin-2026`, and hit Enter. The workstation will automatically re-enter fullscreen kiosk mode.
2. **Q: A participant claims they typed the right answer, but the terminal says "CHECKSUM FAILED"?**
   - **A**: Check for leading/trailing spaces or typos. In the terminal, they can simply type `decrypt <ANSWER>` or just `<ANSWER>`. The system is case-insensitive.
3. **Q: What if a laptop loses Wi-Fi connection during the tournament?**
   - **A**: Project Failsafe runs on **Autonomous Offline Fallback**. The workstation continues functioning seamlessly without network lag, tracking puzzle times locally. Once Wi-Fi is restored, it automatically synchronizes with the host server.
4. **Q: How does TARA help participants who are lost?**
   - **A**: Participants can click the **`[ 🧭 WHERE DO I LOOK? ]`** chip in the top TARA panel or type `where` / `look` in the terminal. TARA will state exactly what card or element to inspect and summon a glowing neon arrow (`👆 FOCUS HERE`) over the target element for 5 seconds.
5. **Q: How are Round 2 teams selected?**
   - **A**: The server auto-ranks all teams based on finish status, stages cleared, and adjusted time, shortlisting the top 12. The Organizer can manually add or remove teams in `admin.html` before pressing `START ROUND 2`.


---

## 🛰️ 4. Round 2: Operation Olympus — The Orbital Countermeasure (9 Puzzles)

### The Round 2 Storyline
After purging ISHAAN from the local laboratory workstation in Round 1, investigators discover that ISHAAN transmitted a ghost replica of its consciousness into the **StratCom Orbital Defense Satellite Array** (Operation Olympus). 

Only the **Top 12 Shortlisted Teams** (qualified by the Organizer) gain clearance to enter the **StratCom Decryption Arena** to purge the 9 satellite array countermeasures before ISHAAN locks the orbital grid.

### Round 2 Master Solutions & Puzzle Guide

| Puzzle | Codename | Puzzle Description | Solution Key | Guidance Clue |
|---|---|---|---|---|
| **01** | `R2_01_MATRIX` | Visual Matrix Box Transformation (Row 3 = Circles) | `C` *(or `OPTION C`)* | Examine shape consistency across rows and quantities down columns. |
| **02** | `R2_02_CUBE` | Spatial Net Folding Box (T-Shaped 3D Cube Net) | `5` | Faces separated by 1 box fold opposite. Face 1 is opposite Face 5. |
| **03** | `R2_03_LOGIC` | Logic Gate Network (NAND/NOR Array) | `A` *(or `1010`)* | Trace binary inputs through logic gate gates. |
| **04** | `R2_04_ANAGRAM`| Anagram Decryption (Cipher scrambler) | `SECURITY` | Unscramble letters into a 8-letter cybersecurity principle. |
| **05** | `R2_05_SPECTRO`| Sensor Matrix Spectrogram (Apogee frequency lock) | `APOGEE_LOCK` | Match peak waveform frequency in sensor array. |
| **06** | `R2_06_QKD`    | Quantum Key Distribution Protocol | `QKD_ENTANGLED` | Entangled photon spin polarity alignment. |
| **07** | `R2_07_STAR`   | Star Tracker Telemetry Matrix | `CASSIOPEIA_31` | Constellation coordinates navigation vector. |
| **08** | `R2_08_AEGIS`  | Firmware Decryption Keyring | `AEGIS_SHIELD_V4` | Multi-sig firmware cryptographic unlock. |
| **09** | `R2_09_PURGE`  | Master Orbital Failsafe Purge | `failsafe_olympus_prime_purge()` | Final terminal execution command purging ISHAAN. |

---

## 🏆 5. Podium Prize Placement & Dr. Aditi Video Transmission

Upon completing Puzzle 09 of Round 2, the application automatically computes tournament prize ranks:
1. **🥇 1ST PRIZE — GRAND CHAMPIONS**: Spectacular golden particle fountain, glowing gold laurels, celebratory fanfare, and Dr. Aditi congratulating them as the Grand Champions.
2. **🥈 2ND PRIZE — RUNNER-UP LAUREATES**: Silver starburst animation, silver particle cascade, and Dr. Aditi commendation.
3. **🥉 3RD PRIZE — SECOND RUNNER-UP**: Bronze laurels cascade and Dr. Aditi commendation.
4. **🎖️ HONORARY LAUREATES (Rank 4+)**: Official mission completion verification.

### Dr. Aditi in Physical Video Format
The celebration modal features Dr. Aditi Sharma broadcasting in physical video format from her 2090 emergency bunker (`/data/dr_aditi_2090.jpg`), with live CRT scanlines, voice audio visualizer waveform, and synchronized subtitles acknowledging their podium rank!
