# PROJECT FAILSAFE // AI Escape Room Software Suite
**100% Offline, Zero-Dependency Cyber Forensics Desktop Application**  
*Built for IEEE WIE / Campus Tech Events • Target Audience: Freshers (Teams of 3)*

---

## ⚡ Click & Play Desktop App

You now have **native Windows executables (`.exe`)** ready to double-click on any laptop or lab PC. No browsers, tabs, or address bars—it opens directly as a **dedicated cyber investigation application window**!

### 1. For Participants / Lab Computers:
* **Double-click `ProjectFailsafe.exe`**
  * Launches the standalone **ADITI-OS v4.2** app window immediately.
  * 100% offline, zero internet, zero installation.
  * Can be copied to USB drives and run directly on all lab machines.

### 2. For the Event Organizer / Host:
* **Double-click `ProjectFailsafe_Organizer.exe`**
  * Automatically starts the local background server on port 8000 and opens the **Organizer Master Console**.
  * Shows your local network IP (e.g. `http://192.168.1.50:8000`) so teams on the room Wi-Fi can connect to your live leaderboard!
  * Organizer PIN: `wie-admin-2026`

---

## 🧩 Master Solution Key & Cheatsheet (Organizer Eyes Only)

| Stage | Puzzle Title | In-Game Mechanism | Master Password |
| :---: | :--- | :--- | :--- |
| **1** | Vanished | Selectable document with white text on white background (Ctrl+A / highlight) | `ORIGIN` |
| **2** | The Trail | A1Z26 Index extraction from README.doc with decoy folders (`Project_FINAL`) | `LOOK BEHIND THE DATE` |
| **3** | The Timeline | Audit log table identifying non-existent leap date (`Feb 29, 2025`) | `28/02/2025` or `02292025` |
| **4** | The Voice / Audit | Forensic timeline log identifying terminal override contradiction (`22:46`) | `22:46` |
| **5** | Hello, Investigators | Rogue AI prompt instructing BLUE -> Aditi's note: pick opposite | `WHITE` |
| **6** | Which Aditi Is Real? | Typography inspector comparing Arial 11pt (Aditi) vs Calibri (AI) | `AUTHENTIC` |
| **7** | Morse From Aditi | **Web Audio Synthesizer** plays real-time CW Morse code: *"DO NOT FOLLOW BLUE"* | `WHITE` |
| **8** | The Folder Maze | Interactive tree navigation through `WHITE/A/D/I` to collect sentence fragments | `THE AI CAN MODIFY WHAT YOU SEE` |
| **9** | Reality Is Edited | **Interactive Version History scrubber** revealing Dr. Aditi's original revision | `HISTORY` or `OVERRIDE FAILED` |
| **10** | The Trap | Pulsing emergency shutdown button — submitting triggers a red glitch and **+5m penalty**! | **Bypass / Do Not Submit** |
| **11** | The WIE Failsafe | WIE Values character cipher: Wisdom (6), Integrity (9), Empowerment (11) | `6-9-11` or `WISDOM-INTEGRITY-EMPOWERMENT` |

---

## ⏱️ Scoring & Penalty Formula

$$\text{Final Adjusted Score} = \text{Raw Completion Time} + (\text{Hints Used} \times 2\text{ min}) + (\text{Trap Triggered} \times 5\text{ min})$$

* **Tie-Breaker Hierarchy**:
  1. Lowest Total Adjusted Score.
  2. Fewest Hints Requested.
  3. Zero Fake Form Submissions.

---

## 📁 File Structure
```
project-failsafe/
├── ProjectFailsafe.exe           # Click-and-play desktop app for teams
├── ProjectFailsafe_Organizer.exe # Click-and-play organizer server & dashboard
├── run_server.bat                # Alternative batch launcher for server
├── run_offline_station.bat       # Alternative batch launcher for offline stations
├── server.py                     # Python 3 standard library backend
├── data/
│   └── game_state.json           # Real-time state ledger
└── public/
    ├── index.html                # ADITI-OS core terminal UI
    ├── css/terminal.css          # Cyberpunk dark theme & CRT scanline effect
    └── js/
        ├── audio.js              # Native Web Audio API Morse synthesizer
        ├── puzzles.js            # Puzzle engines & document viewers
        ├── admin.js              # Live leaderboard & broadcast system
        └── app.js                # Window manager & timer engine
```
