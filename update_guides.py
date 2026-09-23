import re

def update_guides():
    # 1. Update VOLUNTEER_PUZZLE_GUIDE.md
    with open("VOLUNTEER_PUZZLE_GUIDE.md", "r", encoding="utf-8") as f:
        v_content = f.read()

    # Replace ADI with ISHAAN and ETHAN with TARA
    v_content = re.sub(r'\bADI\b', 'ISHAAN', v_content)
    v_content = re.sub(r'\bETHAN\b', 'TARA', v_content)
    v_content = re.sub(r'15-Stage', '11-Stage', v_content)
    v_content = re.sub(r'15 stages', '11 stages', v_content)
    v_content = re.sub(r'15 progressive stages', '11 progressive stages', v_content)
    v_content = re.sub(r'ALL 15', 'ALL 11', v_content)

    # Add Round 2 Operation Olympus section if not present
    if "OPERATION OLYMPUS: THE ORBITAL COUNTERMEASURE" not in v_content:
        r2_guide_text = '''
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
'''
        v_content += r2_guide_text

    with open("VOLUNTEER_PUZZLE_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(v_content)
    print("VOLUNTEER_PUZZLE_GUIDE.md updated successfully!")

    # 2. Update PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md
    with open("PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md", "r", encoding="utf-8") as f:
        p_content = f.read()

    p_content = re.sub(r'\bADI\b', 'ISHAAN', p_content)
    p_content = re.sub(r'\bETHAN\b', 'TARA', p_content)
    p_content = re.sub(r'Ethan', 'Tara', p_content)
    p_content = re.sub(r'15-Stage', '11-Stage', p_content)
    p_content = re.sub(r'15 stages', '11 stages', p_content)
    p_content = re.sub(r'15 Forensic Stages', '11 Forensic Stages', p_content)

    with open("PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md", "w", encoding="utf-8") as f:
        f.write(p_content)
    print("PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md updated successfully!")

if __name__ == '__main__':
    update_guides()
