# PROJECT FAILSAFE // IEEE WIE AI Forensic Escape Room Suite
**100% Offline, Zero-Dependency Cyber Forensics Desktop Application**  
*Built for IEEE Women in Engineering (WIE) / Tech Event Hackathons • Target Audience: Freshers (Teams of 3)*

[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Production--Ready-00ff66?style=flat-square)](#)
[![Edition](https://img.shields.io/badge/Editions-v1.0%20Military%20Command%20%7C%20v2.0%20Quantum%20HUD-00e5ff?style=flat-square)](#)
[![Architecture](https://img.shields.io/badge/Architecture-100%25%20Offline%20%7C%20Zero--Dependency-ffaa00?style=flat-square)](#)
[![Security](https://img.shields.io/badge/Anti--Cheat-Proctor%20Focus%20Lockdown-ff003c?style=flat-square)](#)

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

The Organizer Command Center provides complete real-time situational awareness across all participant stations:

* **Live Leaderboard & Stage Progression**:
  Instantly view which level/stage each team is on (Stage 1 through Final Stage 11).
* **Team Credentials & Password Visibility**:
  Organizers can view all registered team passwords. Passwords default to masked (`••••••••`) and can be unmasked with the one-click `[ 👁️ ]` toggle button.
* **Real-Time Action Ticker**:
  Streams granular player actions with timestamps:
  - *"Inspecting Sector: 01_ORIGIN (Farewell.doc)"*
  - *"Toggled UV Optical Depolarizer: ACTIVE"*
  - *"Submitted Decrypt Code: 'ORIGIN'"*
  - *"Quarantined in Sandbox Buffer"*
  - *"🚨 Workstation Locked: Focus Loss Violation (#2)"*
* **Anti-Cheat Alerts & One-Click Remote Unlock**:
  When a team triggers the anti-cheat proctor lock, their row flashes a red `🚨 LOCKED` badge. Organizers can click **`[ 🔓 UNLOCK ]`** to unlock their terminal remotely from the organizer dashboard without walking to their desk.
* **Global Broadcast Announcement System**:
  Type an urgent message or announcement and transmit to all stations. All connected participant workstations instantly display a flashing cyberpunk broadcast toast.
* **Full Audit Trail**:
  Clicking `[ 📜 AUDIT ]` opens a chronological modal showing every key attempt, hint request, and tamper breach for that team.
* **CSV Export**:
  Export the entire session to `failsafe_organizer_leaderboard_[timestamp].csv` with raw times, hint counts, penalties, and final rankings for awards.

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
| **02** | The Whiteout Text (Invisible Ink) | Highlight white-on-white text in `Welcome_Log.doc` (`Ctrl + A` or UV light) | `INITIATE` *(also accepts `ORIGIN`)* |
| **03** | The Simple Acrostic Note | First letters of each sentence in `Aditi_Memo.doc` (08:00 memo) | `SAFE` *(also accepts `LOOK BEHIND THE DATE`)* |
| **04** | The Calendar Anomaly | Non-leap year calendar contradiction in `Incident_Logs.doc` (Feb 29, 2025 is impossible) | `28/02/2025` *(also accepts `02292025`, `29022025`, `20250229`)* |
| **05** | A1Z26 Alphabet Code | Alphanumeric position mapping [16-15-12-01-18-09-19] in `Clearance_Code.txt` | `POLARIS` |
| **06** | The Resolved Comments Log | Inspect resolved comment history in `System_Diagnostics.doc` | `MARGIN_KEY` *(also accepts `22:46`)* |
| **07** | Font Style Verification | Compare `AUTHENTIC_LOG.doc` against `STYLE_GUIDE.txt` (Arial 11pt vs Times New Roman) | `ARIAL` *(also accepts `AUTHENTIC`)* |
| **08** | The Steganography Mask | Crank Exposure/Brightness slider on pitch-black `Dark_Terminal.png` | `SHADOW_CORE` |
| **09** | Embedded Table Pixel Art | Zoom out to 50% or enhance contrast on 10x10 table in `Corrupted_Image_Block.doc` | `7702` *(also accepts `WHITE`)* |
| **10** | Revision History Conflict | Google Sheets version comparison in `Sanctuary_Inventory.sheet` (Aditi 20:00 draft) | `FALSE_RECORDS` *(also accepts `THE AI CAN MODIFY WHAT YOU SEE`)* |
| **11** | The Confidence Equation | Reverse engineer ADI formula `(S / T)² × 100` to find corrupted prediction (E: 74% vs 25%) | `SYSTEM SHUTDOWN` *(also accepts `E`, `25%`, `ADITI ENTERED`, `C`)* |
| **12** | Morse Code Audio Transmission | Decode CW radio audio tones (`.-- .... .. - .`) from Dr. Aditi's emergency beacon | `WHITE` *(also accepts `SOS_ADITI`, `MORSE`)* |
| **13** | Version Scrub (Git Reflog) | Inspect Git reflog commit history in `Incident_Report.doc` (commit `7b8a1c9`) | `OVERRIDE FAILED` *(also accepts `HISTORY`)* |
| **14** | Honeypot Trap Bypass | Disarm ADI's credential-harvesting honeypot at `DO_NOT_RUN.exe` | `BYPASS` *(also accepts `SKIP`, `DISARM`)* |
| **15** | Final WIE Failsafe Protocol | IEEE WIE founding values cipher (Wisdom 6, Integrity 9, Empowerment 11) | `6-9-11` *(also accepts `WISDOM-INTEGRITY-EMPOWERMENT`)* |

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
