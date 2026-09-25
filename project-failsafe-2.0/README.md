# PROJECT FAILSAFE // IEEE WIE AI Forensic Escape Room Suite
**100% Offline, Zero-Dependency Cyber Forensics Desktop Application**  
*Built for IEEE Women in Engineering (WIE) / Tech Event Hackathons • Target Audience: Freshers (Teams of 3)*

[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Production--Ready-00ff66?style=flat-square)](#)
[![Edition](https://img.shields.io/badge/Editions-v1.0%20Military%20Command%20%7C%20v2.0%20Quantum%20HUD-00e5ff?style=flat-square)](#)
[![Architecture](https://img.shields.io/badge/Architecture-100%25%20Offline%20%7C%20Zero--Dependency-ffaa00?style=flat-square)](#)
[![Security](https://img.shields.io/badge/Anti--Cheat-Proctor%20Focus%20Lockdown-ff003c?style=flat-square)](#)

---

## 📖 Master Answer Keys & Proctor Handbook
- Complete step-by-step master solution keys for **all 21 Round 1 Stages** and **all 17 Round 2 Olympiad Challenges** are documented in:  
  👉 **[`ANSWER_KEYS_AND_PROCTOR_INSTRUCTIONS.md`](ANSWER_KEYS_AND_PROCTOR_INSTRUCTIONS.md)**
- Additional volunteer and participant guidelines:  
  👉 **[`VOLUNTEER_PUZZLE_GUIDE.md`](VOLUNTEER_PUZZLE_GUIDE.md)** and **[`PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md`](PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md)**

---

## ⚡ Quick Start: Click & Play Desktop Apps

You now have **native standalone Windows executables (`.exe`)** ready to double-click on any laptop or lab PC. No browser tabs, no toolbars, no URL bars—it launches directly as a **dedicated fullscreen cyber investigation workstation**!

### 🎮 For Participants (Escape Room Teams):
You can run either of two aesthetic editions:

| Edition | Desktop Launcher | Description |
| :--- | :--- | :--- |
| **Version 1.0 (Standard)** | `ProjectFailsafe.exe` | **ADITI-OS v4.2**: 2050 Military Cyber Command Station (*The Division / Titanfall* theme) with holographic dossiers and optical depolarizer. |
| **Version 2.0 (Reactor HUD)** | `project-failsafe-2.0/ProjectFailsafe2.exe` | **Stratcom Quantum Reactor HUD**: Rotating multi-ring quantum reactor core, 3D vector humanoid avatar, and cybernetic framing. |

*Alternative Launchers*:
- Batch runners: `run_offline_station.bat` (v1.0) or `project-failsafe-2.0/run_station.bat` (v2.0).
- Direct browser files: `aditi_os_widget.html` (v1.0) or `project-failsafe-2.0/index.html` (v2.0).

---

### 🛡️ For Event Organizers & Lab Proctors:
Start the central tracking server and launch the live command center:
1. **Double-click `ProjectFailsafe_Organizer.exe`** (or `project-failsafe-2.0/ProjectFailsafe2_Organizer.exe`).
2. The launcher starts the background telemetry server on port 8000 and opens the **Organizer Command Center** in your browser:
   ```text
   http://localhost:8000/admin.html
   ```
3. **Room LAN / Mobile Monitoring**:
   - The server terminal displays your exact LAN IP on startup (e.g. `http://192.168.1.50:8000/admin.html`).
   - Open this address on your smartphone or tablet connected to the room Wi-Fi to monitor teams and unlock workstations while walking around the room!
4. **Organizer Master Override PIN**:
   ```text
   wie-admin-2026
   ```

---

## 👥 Participant Authentication & Team Login

When participants launch their workstation, they are greeted with the **Team Login Modal**:

1. **Pre-Assigned Accounts**:
   Organizers can distribute pre-generated team credentials. Built-in sample accounts:
   - **Team ID**: `TEAM-01-ALPHA` | **Password**: `strikers-pass-99` (*Quantum Strikers*)
   - **Team ID**: `TEAM-02-BETA`  | **Password**: `shadow-vault-42` (*Cyber Phantoms*)
2. **Self-Registration ("Register New Team")**:
   Teams can click *"Register New Team"* on the login card to create their own custom callsign, squad name, member roster, and security password.
3. **Offline & Session Resilience**:
   - Credentials and progress are stored in the browser's `localStorage` and synchronized to the central server every 5 seconds.
   - If the server is offline or temporarily restarted, participant stations continue running without interruption.
4. **Active HUD Badge**:
   The authenticated unit callsign (`TEAM: [CALLSIGN]`) is pinned to the top HUD bar with a `[ 👥 TEAM ID ]` button to switch teams or review credentials.

---

## 🛰️ Live Organizer Command Center (`admin.html`)

The Organizer Command Center provides complete real-time situational awareness across up to 100 participant stations simultaneously:

* **Simultaneous 100-Station Monitoring & Tactical Grid**:
  - **🎛️ 100-Station Tactical Grid View**: High-density visual matrix of all room stations (Stations 01–100) with color-coded status badges: 🟢 Active, 🟡 Idle, 🔴 Locked (Breach), 🟣 Liberated (Finished), and ⚫ Offline.
  - **📋 Detailed Table View**: Sortable leaderboard ranking all teams by stage, adjusted score, hint count, and breach count.
  - Instantly tracks progression from Stage 01 through Final Stage 21 in real-time.
* **🔍 Detailed Participant Telemetry Inspector (`[ 🔍 TELEMETRY ]`)**:
  - Organizers can click `[ 🔍 TELEMETRY ]` on any team to open the **Deep Hardware & Proctoring Inspector**:
    - **Display & Environment**: Real-time client screen resolution (e.g. `2560x1440`), browser window viewport, and operating system.
    - **Proctored Fullscreen State**: Live status indicating whether the team is in proctored fullscreen mode or in violation.
    - **Integrity Breaches & Violations**: Chronological log of proctoring events, tab switches, Google Lens attempts, and window blur events.
    - **Stage-by-Stage Forensic Solve Times**: Granular solve duration for every stage (Stage 01 through Stage 21).
    - **Penalty & Score Breakdown**: Exact hint penalties (+2m per hint) and honeypot trap penalties (+5m per trap) alongside raw and adjusted finish scores.

* **✏️ Real-Time Team Manipulation & Editing (`[ ✏️ EDIT ]`)**:
  - Organizers can click `[ ✏️ EDIT ]` on any workstation to manipulate active parameters on the fly:
    - **Team Identity**: Rename squad title, update member roster, or reset team passwords.
    - **Stage Advancement / Rollback**: Manually elevate a team to any stage (e.g. Stage 05) or roll them back.
    - **Score & Time Adjustments**: Add bonus time or deduction seconds to adjust for technical difficulties or penalties.
    - **Hint & Trap Overrides**: Reset or manually adjust used hints and triggered honeypot traps.
    - **Completion State**: Manually mark or unmark a team as finished.

* **🗑️ Permanent Team Removal & Disqualification (`[ 🗑️ DELETE ]`)**:
  - Organizers can click `[ 🗑️ DELETE ]` to completely and permanently remove a team from the tournament ledger, active rankings, and Round 2 qualification lists.

* **🏆 Top 12 Shortlist Manager & Round 2 Gating (`[ 🏆 SHORTLIST TOP 12 ]`)**:
  - Auto-ranks the top 12 finishers of Round 1 based on adjusted solve time and accuracy.
  - **Manual Manipulation**: Organizers can freely qualify (`[ + QUALIFY ]`) or remove (`[ ✕ REMOVE ]`) any team before launching Round 2.
  - **Single-Click Round 2 Launch**: Clicking `[ 🚀 LOCK SHORTLIST & START ROUND 2 ]` locks the shortlist and opens the 15-question Round 2 arena exclusively for qualified teams while placing other teams on debriefing standby.

* **🔓 Fullscreen Exit Approval Protocol**:
  - When participants need to leave fullscreen legitimately, they click `[ 🔓 REQUEST FULLSCREEN EXIT ]` on their HUD.
  - The request instantly appears on the Organizer Command Center banner with `[ ✅ APPROVE ]` and `[ ❌ DENY ]` buttons.
  - Approval grants a temporary 90-second proctored exit window without triggering tamper penalties.

* **🚪 Remote Workstation Logout (`[ 🚪 LOGOUT ]` & `[ 🚪 LOGOUT ALL ]`)**:
  - Organizers can remotely log out any individual workstation or perform a room-wide **`[ 🚪 LOGOUT ALL ]`** during intermissions.

* **🔄 Remote Workstation Reset (`[ 🔄 RESET ]` & `[ 🔄 RESET ALL ]`)**:
  - Organizers can remotely reboot any team back to Stage 01 or perform a tournament-wide **`[ 🔄 RESET ALL ]`**.

* **Team Credentials & Password Visibility**:
  Organizers can view all registered team passwords with one-click `[ 👁️ ]` unmasking.

* **Real-Time Action Ticker**:
  Streams granular player actions with timestamps.

* **Global Broadcast Announcement System**:
  Transmit instant alert toasts to all participant screens simultaneously.

* **Full Audit Trail & CSV Export**:
  `[ 📜 AUDIT ]` modal and CSV download for formal tournament reporting.

---

## 🚨 Anti-Cheat Proctor Lockdown Protocol

To ensure competitive integrity during campus events:
1. **Window Blur & Tab Switch Detection**:
   If a participant opens another application, switches tabs, opens an unauthorized browser, or hits `Alt+Tab`, the application immediately triggers an emergency security lockdown.
2. **Lockout Overlay**:
   A fullscreen dark blur modal covers the entire screen, logging the incident count and timestamp.
3. **Two Unlock Methods**:
   - **Local Override**: The organizer or proctor enters the Master PIN (`wie-admin-2026`) directly on the locked workstation.
   - **Remote Override**: The organizer clicks `[ 🔓 UNLOCK ]` on the Organizer Command Center dashboard (`admin.html`).

---

## 🧠 ETHAN Companion AI: Active Navigational Guidance (Zero-Spoiler)

The in-station AI companion (ETHAN Hunt Core) actively guides operators across **all 15 stages** without spoiling passwords:

* **Active Direction Across All 15 Stages**:
  - Whenever participants click **👁️ ETHAN** or type `ethan` / `hint` in the terminal, ETHAN activates a glowing visual radar beacon highlighting the exact dossier sector or card to investigate for 3.5 seconds.
  - Explains the cryptographic mechanism in play (e.g. Command sequence deduction, UV ink filtering, Acrostic cipher, non-leap year calendar rules, A1Z26 mapping, margin comments, typography matching, steganography brightness manipulation, table pixel art, Google Sheets version comparison, Bayesian confidence formula audit, CW Morse radio audio decoding, Git reflog inspection, honeypot neutralization, IEEE WIE value lengths).
  - Even during atmospheric signal jamming or sandbox quarantine, ETHAN transmits emergency intercepted telemetry so participants are never stranded without a compass.
* **Zero Direct Password Spoilers**:
  - ETHAN never divulges the exact password string. Investigators must perform the forensic deductions themselves and enter `decrypt [passcode]`.

---

## 🧩 Master Solution Key & Cheatsheet (Organizer Eyes Only)

| Stage | Puzzle Title | In-Game Mechanism | Master Solution Key |
| :---: | :--- | :--- | :--- |
| **01** | ADI Recovery Terminal | Command sequence deduction (`LOGIN → VERIFY → ? → EXECUTE → LOCK`) | `ACCESS` *(also accepts `RECOVER ACCESS`)* |
| **02** | ADI's Memory Core | Arrange 6 recovered memory fragments in chronological order (4:17 PM → 10:15 PM) | `123456` *(also accepts `1-2-3-4-5-6`, `MEMORY_RESTORED`, `RESTORE`, `INITIATE`)* |
| **03** | The Simple Acrostic Note | First letters of each sentence in `Aditi_Memo.doc` (08:00 memo) | `SAFE` *(also accepts `LOOK BEHIND THE DATE`)* |
| **04** | The Calendar Anomaly | Non-leap year calendar contradiction in `Incident_Logs.doc` (Feb 29, 2025 is impossible) | `28/02/2025` *(also accepts `02292025`, `29022025`, `20250229`)* |
| **05** | A1Z26 Alphabet Code | Alphanumeric position mapping [16-15-12-01-18-09-19] in `Clearance_Code.txt` | `POLARIS` |
| **06** | The Resolved Comments Log | Inspect resolved comment history in `System_Diagnostics.doc` | `MARGIN_KEY` *(also accepts `22:46`)* |
| **07** | Font Style Verification | Compare `AUTHENTIC_LOG.doc` against `STYLE_GUIDE.txt` (Arial 11pt vs Times New Roman) | `ARIAL` *(also accepts `AUTHENTIC`)* |
| **08** | The Steganography Mask | Crank Exposure/Brightness slider on pitch-black `Dark_Terminal.png` | `SHADOW_CORE` |
| **09** | Embedded Table Pixel Art | Zoom out to 50% or enhance contrast on 10x10 table in `Corrupted_Image_Block.doc` | `7702` *(also accepts `WHITE`)* |
| **10** | Revision History Conflict | Google Sheets version comparison in `Sanctuary_Inventory.sheet` (Aditi 20:00 draft) | `FALSE_RECORDS` *(also accepts `THE AI CAN MODIFY WHAT YOU SEE`)* |
| **11** | The Confidence Equation | Reverse engineer ADI formula `(S / T)² × 100` to find corrupted prediction (E: 74% vs 25%) | `SYSTEM SHUTDOWN` *(also accepts `E`, `25%`, `ADITI ENTERED`, `C`)* |
| **12** | Morse Code Audio Transmission | Decode CW radio audio tones (`.-- .... .. - .`) with live oscilloscope | `WHITE` *(also accepts `SOS_ADITI`, `MORSE`)* |
| **13** | Version Scrub (Git Reflog) | Inspect Git reflog commit history in `Incident_Report.doc` (commit `7b8a1c9`) | `OVERRIDE FAILED` *(also accepts `HISTORY`)* |
| **14** | Honeypot Trap Bypass | Disarm ADI's credential-harvesting honeypot at `DO_NOT_RUN.exe` | `BYPASS` *(also accepts `SKIP`, `DISARM`)* |
| **15** | Final WIE Failsafe Protocol | IEEE WIE founding values cipher (Wisdom 6, Integrity 9, Empowerment 11) | `6-9-11` *(also accepts `WISDOM-INTEGRITY-EMPOWERMENT`)* |

### 🗄️ Recovered Classic Forensic Vault Archives & Interactive Tools
All original classic investigation artifacts are preserved and accessible in both Failsafe 1.0 and 2.0:
* **📻 CW Morse Audio Oscilloscope (`modal-spectro` / `12_AUDIO`)**: Real-time animated green audio waveform oscilloscope with dual audio tone beacons: Primary Beacon `WHITE` (`.-- .... .. - .`) and Sub-Carrier Warning `DO NOT FOLLOW THE BLUE PATH`.
* **🗂️ Quarantined Directory Maze (`modal-maze` / `ROOT_MAZE`)**: Interactive subfolder inspection exploring segregated branches: `BLUE/` (honeypot trap warning), `RED/` (decoy logs), `GREY/` (Fragment 1: "THE AI CAN"), and `WHITE/` (Fragments 2 & 3: "MODIFY WHAT" + "YOU SEE" -> *"THE AI CAN MODIFY WHAT YOU SEE"*).
* **🔍 Security Audit Forensic PDF (`modal-security-audit` / `SECURITY_AUDIT`)**: Timeline contradiction identifying physical impossibility between gate exit (22:44) and core terminal override (22:46).
* **💬 Synthetic ADI Directive (`modal-adi-prompt` / `ADI_DIRECTIVE`)**: ADI directive instructing operators to access BLUE vs Dr. Aditi's emergency handwritten bezel warning ("Do the exact opposite").
* **📁 Project ORIGIN Vault (`modal-origin` / `DIR_ORIGIN`)**: Foundational repository containing `Farewell.doc` (whiteout ink) and `README.doc` (indexed extraction `1, 4, 9, 20, 9` -> *"LOOK BEHIND THE DATE"*).

---

## 🌐 LAN Multi-Machine Setup (Scaling to 50+ Teams)

1. **Host Computer (Organizer)**:
   - Connect the host laptop to the room's Wi-Fi router or local Ethernet switch.
   - Run `ProjectFailsafe_Organizer.exe`.
   - Note the LAN IP shown in the console window (e.g. `http://192.168.1.50:8000`).
2. **Participant Computers**:
   - Copy the `project-failsafe` folder to a USB drive and paste it onto participant lab machines.
   - Open `aditi_os_widget.html` or run `ProjectFailsafe.exe`.
   - The station automatically pings the host server on the local network to transmit telemetry and receive global broadcasts.
   - If Wi-Fi drops, stations run in **Offline Autonomous Mode** and synchronize once reconnected.

---

## 📁 Repository Directory Structure

```
project-failsafe/
├── ProjectFailsafe.exe                 # [v1.0] Standalone participant desktop app
├── ProjectFailsafe_Organizer.exe       # [v1.0] Standalone organizer launcher
├── run_offline_station.bat             # [v1.0] One-click participant station batch script
├── run_server.bat                      # [v1.0] Local Python backend server runner
├── aditi_os_widget.html                # [v1.0] Complete standalone cyber command workstation
├── admin.html                          # Live Organizer Command Center & Dashboard
├── server.py                           # Lightweight zero-dependency REST & telemetry server
├── Launcher.cs                         # C# source for participant launcher
├── OrganizerLauncher.cs                # C# source for organizer launcher
├── PROJECT_FAILSAFE_MASTER_SOLUTIONS.pdf # Printable PDF solution booklet
├── solutions_printable.html            # Printable HTML solution booklet
├── data/
│   └── game_state.json                 # Persistent database for teams, scores, and telemetry
│
├── project-failsafe-2.0/               # [v2.0] Standalone Quantum Reactor HUD Edition
│   ├── ProjectFailsafe2.exe            # [v2.0] Standalone participant desktop app
│   ├── ProjectFailsafe2_Organizer.exe  # [v2.0] Standalone organizer launcher
│   ├── run_station.bat                 # [v2.0] Participant station runner
│   ├── run_server.bat                  # [v2.0] Local server runner
│   ├── index.html                      # [v2.0] Quantum Reactor HUD workstation
│   ├── admin.html                      # [v2.0] Organizer Command Center
│   ├── server.py                       # [v2.0] Python REST & telemetry backend
│   ├── README.md                       # [v2.0] Specific edition documentation
│   └── data/
│       └── game_state.json             # [v2.0] Team state database
│
└── public/                             # Assets and modular modules
    ├── admin.html                      # Mirrored admin console
    ├── index.html                      # Modular terminal UI
    ├── css/terminal.css                # Sci-Fi styling and animations
    └── js/
        ├── app.js                      # Core game loop & window manager
        ├── puzzles.js                  # Forensic puzzle engine
        └── audio.js                    # Procedural Web Audio Morse synthesizer
```

---

## 📜 License & Credits

Developed for **IEEE Women in Engineering (WIE)** student branch events and tech symposiums.  
All modules are engineered with vanilla HTML5, CSS3, ES6 JavaScript, and standard Python 3 with **zero external CDN dependencies or npm packages**, ensuring 100% offline air-gapped lab reliability.
