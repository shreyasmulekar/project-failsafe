# PROJECT FAILSAFE 2.0 // STRATCOM QUANTUM REACTOR HUD (2050+)

Welcome to **Project Failsafe 2.0**, an independent standalone edition of the IEEE WIE AI Digital Forensics Escape Room featuring a sci-fi holographic workstation inspired by the reference quantum reactor HUD.

---

## 🚀 How to Run Project Failsafe 2.0

### Option 1: Native Windows Desktop App (Recommended)
Double-click:
```
ProjectFailsafe2.exe
```
This launches the application in native standalone windowed app mode via Microsoft Edge/Chrome with zero browser toolbars or tabs.

### Option 2: One-Click Batch Script
Double-click:
```
run_station.bat
```

### Option 3: Direct Browser File
Double-click:
```
index.html
```

---

## 🎨 Visual Differences: Version 1.0 vs Version 2.0

| Feature | Project Failsafe 1.0 | Project Failsafe 2.0 |
| :--- | :--- | :--- |
| **Theme / Inspiration** | 2050 Military Cyber Command Station (*The Division / Titanfall*) | Holographic Quantum Reactor HUD (*Sci-Fi Holographic Command*) |
| **Centerpiece** | 4 Top Telemetry Gauges (Torus, Horizon, Seismic, Locus) | **Massive Multi-Layered Rotating Quantum Reactor Core** with 24 outer glowing LED bead pips and rotating golden crescent arcs |
| **Color Palette** | Neon Green, Cyan, Amber, Crimson | **Deep Slate Blue, Electric Cyan, Glowing Yellow/Gold, Crimson** |
| **Avatar / Biosignals** | System telemetry bars | **Standing Vector Humanoid Wireframe Silhouette** with orbital resonance rings and vital telemetry |
| **Chronometer** | Header Zulu timestamp | **Large High-Tech Digital Clock (`05:10:36 AM`)** with KP index |
| **Charts** | CSS status tracks | **Hexagonal Columnar Stack Chart** + Segmented Radar + 8x16 Dot Matrix Byte Grid |
| **Framing** | Fixed header & footer borders | **Chamfered 45° Cybernetic Angled Frame Geometry** with top and bottom runners |
| **ETHAN Hunt Core** | Floating bottom-right companion box | **Integrated Quantum Reactor Centerpiece + Docked Companion Panel** |

---

## 🧠 Stage Difficulty Curve & Zero-Spoiler Hint Policy

* **Stage 1 (Easy / Onboarding)**:
  - ETHAN guides operators on interface mechanics: how to access `01_ORIGIN`, how to toggle the UV optical depolarizer to reveal invisible quantum ink, and how to execute `decrypt [code]`.
  - He poses the question: *"Where does Dr. Aditi's foundational work begin?"* without spoiling the answer `"ORIGIN"`.
* **Stage 2 to 8 (Moderate to Hard - Keep Them Guessing)**:
  - **Zero Direct Answers**: Neither ETHAN nor the terminal `hint` command reveals answers or character sequences.
  - **Stage 2**: Gives cryptographic advice only (*"Index numbers map to character positions in the text. STRATCOM rules require manual extraction."*).
  - **Stage 3 & 4**: Rogue AI ADI activates packet jamming. Carrier signal is lost. Operators must solve calendar and audio anomalies unassisted.
  - **Stage 5 to 8**: ETHAN is quarantined in the sandbox buffer. He provides high-level tactical directives and tells players to solve Aditi's evidence independently to free him.
  - **Terminal `hint` command**: Returns atmospheric security protocols rather than direct puzzle solutions.

---

## 🧩 Master Solution Key & Cheatsheet (Organizer Eyes Only)

| Stage | Puzzle Title | In-Game Mechanism | Master Solution Key |
| :---: | :--- | :--- | :--- |
| **1** | The Whiteout Text (Invisible Ink) | Highlight all text (`Ctrl + A`) or UV light in `Welcome_Log.doc` | `INITIATE` *(also accepts `ORIGIN`)* |
| **2** | The Simple Acrostic Note | Read first letter of each sentence in `Aditi_Memo.doc` (08:00 memo) | `SAFE` *(also accepts `LOOK BEHIND THE DATE`)* |
| **3** | The A1Z26 Alphabet Code | Alphanumeric mapping [16-15-12-01-18-09-19] in `Clearance_Code.txt` | `POLARIS` *(also accepts `28/02/2025`)* |
| **4** | The Resolved Comments Log | Inspect resolved comment history in `System_Diagnostics.doc` | `MARGIN_KEY` *(also accepts `22:46`)* |
| **5** | The Font Style Verification | Compare `AUTHENTIC_LOG.doc` against `STYLE_GUIDE.txt` (Arial 11pt) | `ARIAL` *(also accepts `AUTHENTIC`)* |
| **6** | The Steganography Mask | Crank Exposure/Brightness slider on pitch-black `Dark_Terminal.png` | `SHADOW_CORE` |
| **7** | Embedded QR / Pixel Art | Zoom out to 50% or enhance contrast on 10x10 table in `Corrupted_Image_Block.doc` | `7702` *(also accepts `WHITE`)* |
| **8** | Revision History Conflict | Google Sheets version comparison in `Sanctuary_Inventory.sheet` (Aditi 20:00) | `FALSE_RECORDS` *(also accepts `THE AI CAN MODIFY WHAT YOU SEE`)* |
| **9** | Version Scrub (Git Reflog) | Inspect VCS commit history in `Incident_Report.doc` (commit `7b8a1c9`) | `HISTORY` or `OVERRIDE FAILED` |
| **10** | Honeypot Trap Bypass | Disarm ADI's credential-harvesting honeypot at `10_TRAP.exe` | `BYPASS` *(Do not submit credentials in trap!)* |
| **11** | Final WIE Failsafe | IEEE WIE founding values cipher (Wisdom 6, Integrity 9, Empowerment 11) | `6-9-11` or `WISDOM-INTEGRITY-EMPOWERMENT` |

---

## 👥 Participant Login & Organizer Command Center

### Participant Station Login:
- On launch, players enter their assigned **Team ID** and **Team Password** (or register a new unit).
- Header badge displays `TEAM: [CALLSIGN]` and enables switching teams via `[ 👥 TEAM ID ]`.
- Stations stream live telemetry every 5 seconds (current sector, level, tamper incidents, and status).

### Organizer Command Center:
- **Desktop Launcher**: Double-click `ProjectFailsafe2_Organizer.exe` or run `run_server.bat`.
- **Browser URL**: `http://localhost:8000/admin.html` (or on LAN: `http://<HOST_IP>:8000/admin.html`).
- **Organizer Master PIN**: `wie-admin-2026`
- **Features**:
  - Live table of all participating teams and their current level/stage.
  - Team Passwords with show/hide toggle (`••••••••` + `[ 👁️ ]`).
  - Real-time action ticker (e.g. *"Inspecting 01_ORIGIN"*, *"Submitted Code: ORIGIN"*, *"Quarantined in Sandbox"*).
  - Anti-cheat focus loss alerts and **One-Click Remote Unlock** (`[ 🔓 UNLOCK ]`).
  - Full audit log per team, global broadcast announcements, and CSV export.

---

## 📁 File Structure

```
project-failsafe-2.0/
├── ProjectFailsafe2.exe            # Native standalone participant desktop executable
├── ProjectFailsafe2_Organizer.exe  # Native one-click Organizer Command Center launcher
├── run_station.bat                 # One-click participant station batch runner
├── run_server.bat                  # Organizer local background server runner
├── index.html                      # 100% offline standalone single-file HUD application
├── admin.html                      # Dedicated Organizer Command Center & Live Dashboard
├── server.py                       # Python zero-dependency REST & telemetry server
├── README.md                       # Documentation & comparison guide
└── data/
    └── game_state.json             # Live teams, credentials, and telemetry database
```

---

*Project Failsafe 2.0 is 100% offline, requires zero internet access or external package dependencies, and runs side-by-side with Project Failsafe 1.0.*
