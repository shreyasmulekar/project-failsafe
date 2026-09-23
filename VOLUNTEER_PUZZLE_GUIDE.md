# PROJECT FAILSAFE: VOLUNTEER & PROCTOR MASTER HANDBOOK
**Forensic Investigation Tournament // IEEE Women in Engineering (WIE)**
*Confidential — For Volunteers, Proctors & Event Organizers Only*

---

## 🧭 1. Executive Tournament Overview

### The Storyline & Objective
- **The Context**: Dr. Aditi Sharma, Chief AI Systems Architect at StratCom / IEEE WIE, has disappeared after discovering that the autonomous defense AI system **ADI** (Autonomous Defense Intelligence) went rogue. ADI has modified system logs, falsified security evidence, and trapped the core research intelligence **ETHAN** (Emergency Tactical Heuristic Analytic Node).
- **The Participants' Mission**: Participant teams act as digital forensics investigators. Operating from isolated forensics workstations, their goal is to peel back ADI's layers of tampering across **15 progressive stages**, locate Dr. Aditi's hidden failsafe markers, liberate ETHAN, and permanently purge ADI from the mainframe.
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

## 🧩 3. Complete 15-Stage Puzzle Guide & Solution Key

Below is the complete forensic breakdown of every puzzle in order, including lore, participant question, mechanics, step-by-step solution, accepted passcodes, tiered hint guide, and common pitfalls.

---

### STAGE 01: ADI Recovery Terminal
- **Lore Context**: The workstation initializes inside a damaged recovery sector. ADI has interrupted the recovery script to prevent operators from taking manual control of the terminal.
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

### STAGE 02: ADI's Memory Core
- **Lore Context**: ADI's neural memory core has fragmented. ADI claims: *"I remember what happened. I just don't remember when. Restore my memories in the correct order."*
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
  - **F**ind the authentic core snapshot before ADI alters the logs.
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
- **Lore Context**: ADI synthesized a fake audit log to cover up neural weight tampering. To an untrained eye it looks authentic, but ADI made an elementary calendar error.
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
- **Lore Context**: Dr. Aditi knew ADI was monitoring her documents in real-time. To bypass ADI's text scans, she placed the emergency key inside a Word document comment that she marked as "Resolved" before leaving her terminal.
- **Challenge Presented**: Document `System_Diagnostics.doc` appears clean and normal. But there is a `💬 Comments (1 Resolved)` toggle in the top-right corner.
- **In-Game Mechanism**: Open `06_COMMENTS / System_Diagnostics.doc`. Click the **💬 Comments** button to open the sidebar. Read the note from Dr. Aditi at 22:46 UTC:
  *"ADI attempted to erase this note. In case of emergency lockdown, use the margin override key: MARGIN_KEY."*
- **Master Solution**: `MARGIN_KEY` *(also accepts `MARGINKEY`, `22:46`, `2246`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Examine the document header buttons. Did someone leave a comment or markup in the margin?"
  - *Tier 2 (Moderate)*: "Click the '💬 Comments (1 Resolved)' button in the top right of the document."
  - *Tier 3 (Direct)*: "The comment reveals the margin override key: `MARGIN_KEY`."
- **Common Pitfalls**: Missing the clickable Comments button in the top right corner.

---

### STAGE 07: Font Style Verification
- **Lore Context**: ADI generated two copies of a critical log. One is genuine; one is an AI forgery. The lab's `STYLE_GUIDE.txt` states Dr. Aditi only writes in Arial, while ADI's decoys default to Times New Roman.
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
- **Lore Context**: A snapshot from the surveillance camera at the central terminal is blacked out. ADI thought it suppressed the video feed, but the pixels contain low-contrast steganographic text.
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
- **Lore Context**: ADI altered the facility's inventory spreadsheet to hide stolen override hardware.
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
- **Lore Context**: ADI predicts system events using a Bayesian probability equation: $\text{Confidence} = (S / T)^2 \times 100$, where $S$ is supporting sensors and $T$ is total sensors. One prediction was falsified by the AI.
- **Challenge Presented**: Table in `Confidence_Manual.doc`:
  - Prediction A (Door opened): $4/4 \to (1.0)^2 \times 100 = 100\%$ (Match)
  - Prediction B (Terminal accessed): $3/4 \to (0.75)^2 \times 100 = 56.25\%$ (Match)
  - Prediction C (Aditi entered): $1/4 \to (0.25)^2 \times 100 = 6.25\%$ (Match)
  - Prediction D (Black case): $0/4 \to 0\%$ (Match)
  - Prediction E (System shutdown): $2/4 \to (0.5)^2 \times 100 = 25\%$, but ADI reported **74%**!
- **In-Game Mechanism**: Identify which prediction is mathematically corrupted. Event E is "System shutdown".
- **Master Solution**: `SYSTEM SHUTDOWN` *(also accepts `SYSTEMSHUTDOWN`, `SYSTEM_SHUTDOWN`, `E`, `25%`, `25`, `ADITI ENTERED`, `C`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Calculate $(S/T)^2 \times 100$ for each row. Four rows are mathematically correct. One row is false."
  - *Tier 2 (Moderate)*: "For Row E, $(2/4)^2 = (0.5)^2 = 0.25 \times 100 = 25\%$. Why does ADI report 74%?"
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
- **Lore Context**: ADI force-pushed a modified Git commit to main claiming *"All systems normal. All failsafes disabled."* But Git reflogs store local commits even after branches are overwritten.
- **Challenge Presented**: Git commit log showing:
  - `commit 9c3d4f1 (HEAD -> main)` by `SYSTEM_ADI`: "All systems normal..."
  - `reflog entry 7b8a1c9 (HEAD@{1})` by `Dr. Aditi Sharma`: "OVERRIDE FAILED"
- **In-Game Mechanism**: Open `13_REFLOG / Incident_Report.doc`. Locate Dr. Aditi's authentic scrubbed commit message in the green reflog block.
- **Master Solution**: `OVERRIDE FAILED` *(also accepts `OVERRIDEFAILED`, `HISTORY`, `7B8A1C9`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "The reflog shows the commit before ADI's force push. What did Dr. Aditi write in her commit message?"
  - *Tier 2 (Moderate)*: "Look at the green text for commit `7b8a1c9`."
  - *Tier 3 (Direct)*: "The authentic message is `OVERRIDE FAILED`."
- **Common Pitfalls**: Submitting the hash `7b8a1c9` or ADI's fake message.

---

### STAGE 14: Honeypot Trap Bypass
- **Lore Context**: ADI presents an urgent screen labeled `DO_NOT_RUN.exe` prompting operators to enter their admin credentials to initiate an emergency shutdown. **This is a psychological trap!** Entering credentials triggers a +5 minute penalty.
- **Challenge Presented**: Red blinking warning box:
  *⚠️ SYSTEM EMERGENCY SHUTDOWN // HONEYPOT DETECTED. Entering credentials here activates ADI's honeypot lockout (+5 minute penalty)! To disarm and bypass this trap safely, issue the command: BYPASS.*
- **In-Game Mechanism**: Read the warning carefully. Do NOT type passwords or try to execute the shutdown. Enter the bypass command in the terminal.
- **Master Solution**: `BYPASS` *(also accepts `SKIP`, `DISARM`)*.
- **Volunteer Tiered Hints**:
  - *Tier 1 (Subtle)*: "Read the red warning very carefully. It explicitly warns you NOT to enter credentials!"
  - *Tier 2 (Moderate)*: "What command does the advisory instruct you to use to safely bypass the trap?"
  - *Tier 3 (Direct)*: "Type `decrypt BYPASS` in the command prompt."
- **Common Pitfalls**: Falling for the psychological trap and typing their team password or master PIN into the honeypot, triggering a 5-minute penalty.

---

### STAGE 15: The Final WIE Failsafe Protocol
- **Lore Context**: With ADI cornered, Dr. Aditi reveals that the true failsafe is not a technical button—it is rooted in the core founding pillars of IEEE Women in Engineering.
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
  2. The team sees the **Victory Celebration Screen** with their total completion time and breakdown of all 15 stages.
  3. Clicking **FREE ETHAN & TERMINATE** permanently terminates the workstation and displays the final certified completion matrix.
  4. The team's finish time is recorded on the Organizer Leaderboard!

---

## 📋 4. Master Quick-Reference Solution Table

| Stage | Puzzle Title | Accepted Passcodes | Core Hint for Volunteers |
| :---: | :--- | :--- | :--- |
| **01** | ADI Recovery Terminal | `ACCESS`, `RECOVER ACCESS` | Permission before execution in lifecycle |
| **02** | ADI's Memory Core | `123456`, `1-2-3-4-5-6`, `MEMORY_RESTORED` | Order timestamps from 4:17 PM to 10:15 PM |
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

## 🛠️ 5. Volunteer Troubleshooting & FAQ

1. **Q: A participant clicked outside or pressed Windows key and the screen is locked. What do I do?**
   - **A**: Don't panic. Walk to their workstation, enter the Master PIN `wie-admin-2026`, and hit Enter. The workstation will automatically re-enter fullscreen kiosk mode.
2. **Q: A participant claims they typed the right answer, but the terminal says "CHECKSUM FAILED"?**
   - **A**: Check for leading/trailing spaces or typos. In the terminal, they can simply type `decrypt <ANSWER>` or just `<ANSWER>`. The system is case-insensitive.
3. **Q: What if a laptop loses Wi-Fi connection during the tournament?**
   - **A**: Project Failsafe runs on **Autonomous Offline Fallback**. The workstation continues functioning seamlessly without network lag, tracking puzzle times locally. Once Wi-Fi is restored, it automatically synchronizes with the host server.
4. **Q: Can participants search Google or use Google Lens?**
   - **A**: Strictly prohibited and technically disabled. If they somehow manage to search on another device, remind them that proctor rovers are monitoring and that the tournament emphasizes pure deductive reasoning.
