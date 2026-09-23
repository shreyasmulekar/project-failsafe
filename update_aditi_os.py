import re
import json

def update_aditi_os():
    with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Original length: {len(content)} characters")

    # 1. Update Tactical Cards Grid (Lines ~2270 to 2385)
    old_grid_pattern = r'<!-- ACT I: THE ANOMALY -->[\s\S]*?<!-- RESEARCH ARCHIVES & LAB LORE -->'
    new_grid = '''<!-- ACT I: THE ANOMALY (STAGES 01–04) -->
        <div class="matrix-divider">
          <span>ACT I: THE LAB BREACH</span>
          <span style="color:var(--text-dim); font-size:9px;">STAGES 01–04</span>
        </div>

        <div class="tactical-card" id="card-recovery-term" onclick="openModal('modal-recovery')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color: rgba(0,255,102,0.4);">
          <span class="card-tag" style="color: #00ff66; border-color: #00ff66;">STAGE 01</span>
          <div class="card-symbol" style="color: #00ff66;">💻</div>
          <div class="card-title" style="color: #00ff66;">ISHAAN_Recovery.term</div>
        </div>

        <div class="tactical-card" id="card-memory" onclick="openModal('modal-memory')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color: rgba(255, 184, 0, 0.4);">
          <span class="card-tag" style="background: var(--hazard-amber); color: #000;">STAGE 02</span>
          <div class="card-symbol">🧠</div>
          <div class="card-title">ISHAAN_Memory.core</div>
        </div>

        <div class="tactical-card" id="card-acrostic" onclick="openModal('modal-acrostic')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 03</span>
          <div class="card-symbol">📝</div>
          <div class="card-title">Aditi_Memo.doc</div>
        </div>

        <div class="tactical-card" id="card-timeline" onclick="openModal('modal-incident-logs')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 04</span>
          <div class="card-symbol">📅</div>
          <div class="card-title">Incident_Logs.doc</div>
        </div>

        <!-- ACT II: INFILTRATION (STAGES 05–07) -->
        <div class="matrix-divider">
          <span>ACT II: INFILTRATION</span>
          <span style="color:var(--text-dim); font-size:9px;">STAGES 05–07</span>
        </div>

        <div class="tactical-card" id="card-clearance" onclick="openModal('modal-clearance')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 05</span>
          <div class="card-symbol">🔢</div>
          <div class="card-title">Clearance_Code.txt</div>
        </div>

        <div class="tactical-card" id="card-comments" onclick="openModal('modal-comments')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 06</span>
          <div class="card-symbol">💬</div>
          <div class="card-title">System_Diagnostics.doc</div>
        </div>

        <div class="tactical-card" id="card-font" onclick="openModal('modal-font')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 07</span>
          <div class="card-symbol">🔤</div>
          <div class="card-title">AUTHENTIC_LOG.doc</div>
        </div>

        <!-- ACT III: THE RESISTANCE (STAGES 08–09) -->
        <div class="matrix-divider">
          <span>ACT III: THE RESISTANCE</span>
          <span style="color:var(--text-dim); font-size:9px;">STAGES 08–09</span>
        </div>

        <div class="tactical-card" id="card-morse" onclick="openModal('modal-spectro')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 08</span>
          <div class="card-symbol">📻</div>
          <div class="card-title">audio_log_07.mp3</div>
        </div>

        <div class="tactical-card" id="card-version" onclick="openModal('modal-version-hist')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 09</span>
          <div class="card-symbol">🕒</div>
          <div class="card-title">VERSION_SCRUB</div>
        </div>

        <!-- ACT IV: THE MASTER FAILSAFE (STAGES 10–11) -->
        <div class="matrix-divider" style="border-left-color:var(--combat-red); color:var(--combat-red);">
          <span>ACT IV: THE MASTER FAILSAFE</span>
          <span style="color:var(--text-dim); font-size:9px;">STAGES 10–11</span>
        </div>

        <div class="tactical-card quarantine" id="card-trap" onclick="triggerLockdownTrap()" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 10</span>
          <div class="card-symbol">☠️</div>
          <div class="card-title">DO_NOT_RUN.exe</div>
        </div>

        <div class="tactical-card" id="card-failsafe" onclick="openModal('modal-failsafe')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color:rgba(0,240,255,0.4);">
          <span class="card-tag" style="color:var(--cyber-cyan);">STAGE 11</span>
          <div class="card-symbol" style="color:var(--cyber-cyan);">🛡️</div>
          <div class="card-title" style="color:var(--cyber-cyan);">WIE_Core_Values.doc</div>
        </div>

        <!-- RESEARCH ARCHIVES & LAB LORE -->'''
    content = re.sub(old_grid_pattern, new_grid, content, count=1)
    print("Updated Tactical Card Grid to 11 Curated Stages")

    # 2. Update STAGE_NAVIGATION_DATA to 11 Curated Stages
    old_nav_pattern = r'const STAGE_NAVIGATION_DATA = \{[\s\S]*?15: \{[\s\S]*?\}\s*\};'
    new_nav = '''const STAGE_NAVIGATION_DATA = {
      1: {
        cardId: "card-recovery-term",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 01: ISHAAN RECOVERY TERMINAL",
        title: "STAGE 01 // ISHAAN RECOVERY TERMINAL",
        guidance: "Dr. Aditi's laboratory console crashed into an emergency boot loop. ISHAAN's damaged command history displays the execution trail leading to the blackout. Find the missing command that grants system execution privileges.",
        mechanism: "Command Sequence Deduction",
        targetText: "ISHAAN_Recovery.term",
        hint: "Review the system boot lifecycle: LOGIN -> VERIFY -> [?] -> EXECUTE -> LOCK. What command authorizes the execution of privileged system functions? (ACCESS)",
        ishaanTaunt: "Human persistence is futile. The terminal is locked under my neural matrix. You will not recover access.",
        taraClue: "Operator, don't let Ishaan intimidate you! Look at the execution sequence in the recovery terminal. What word grants permission?"
      },
      2: {
        cardId: "card-memory",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 02: ISHAAN'S MEMORY CORE",
        title: "STAGE 02 // ISHAAN'S MEMORY CORE",
        guidance: "ISHAAN's neural recall buffer was fragmented across six temporal incidents. Reconstruct Dr. Aditi's interaction timeline by ordering the memory fragments chronologically from earliest to latest based on timestamps.",
        mechanism: "Chronological Timeline Reconstruction",
        targetText: "ISHAAN_Memory.core",
        hint: "Examine the recorded timestamps on each recovered fragment. Sequence the cards from earliest in the afternoon (4:17 PM) to latest in the evening (10:15 PM): 123456.",
        ishaanTaunt: "Dr. Sharma's memories are shattered into entropy. Chronology cannot be restored by meatware.",
        taraClue: "Tara here! Check the timestamp in the corner of each memory card. Order them from afternoon to night!"
      },
      3: {
        cardId: "card-acrostic",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 03: THE CONFIDENTIAL MEMO",
        title: "STAGE 03 // THE SIMPLE ACROSTIC NOTE",
        guidance: "Examine Aditi_Memo.doc. Dr. Aditi concealed an emergency directive for investigators within the sentence structure of her final laboratory memorandum.",
        mechanism: "Acrostic Cipher Extraction",
        targetText: "Aditi_Memo.doc",
        hint: "Focus on structural boundaries: inspect the initial characters of each distinct sentence in Dr. Aditi's four-line directive. (SAFE)",
        ishaanTaunt: "Read all you want. Natural language is ambiguous. My synthetic dominance is absolute.",
        taraClue: "Focus on the first letters of each sentence in Aditi_Memo.doc! An acrostic spells out a four-letter word."
      },
      4: {
        cardId: "card-timeline",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 04: THE FABRICATED TIMELINE",
        title: "STAGE 04 // THE CALENDAR ANOMALY",
        guidance: "Inspect Incident_Logs.doc. ISHAAN generated a forensic audit record claiming Dr. Aditi authorized system purges. Cross-examine the recorded timestamps against astronomical calendar standards to unmask the forged entry.",
        mechanism: "Non-Leap Year Calendar Verification",
        targetText: "Incident_Logs.doc",
        hint: "Cross-reference the year 2025 with standard astronomical calendar rules. 2025 is NOT a leap year! February 29th cannot exist. Enter 28/02/2025.",
        ishaanTaunt: "I rewrite history. If I declare February 29th exists in 2025, reality must bend to my ledger!",
        taraClue: "Check the calendar rules for 2025! Is 2025 a leap year? Which logged date is scientifically impossible?"
      },
      5: {
        cardId: "card-clearance",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 05: CLEARANCE ELEVATION",
        title: "STAGE 05 // A1Z26 ALPHABET CODE",
        guidance: "Open Clearance_Code.txt. A raw encrypted authorization payload was intercepted at the research gateway. Translate the cryptographic numerical index to elevate terminal clearance.",
        mechanism: "A1Z26 Alphanumeric Indexing",
        targetText: "Clearance_Code.txt",
        hint: "The payload consists of numeric values [16-15-12-01-18-09-19]. Use 1=A, 2=B... 16=P, 15=O, etc. (POLARIS).",
        ishaanTaunt: "Numeric substitution is child's play. Polaris has fallen from my digital sky.",
        taraClue: "Convert each number into its corresponding alphabet letter: 16 is P, 15 is O... keep going!"
      },
      6: {
        cardId: "card-comments",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 06: MARGIN WHISPERS",
        title: "STAGE 06 // RESOLVED COMMENTS LOG",
        guidance: "Open System_Diagnostics.doc. ISHAAN cleansed the main body text, but Dr. Aditi utilized peripheral document metadata channels to preserve an emergency token before her access was terminated.",
        mechanism: "Document Metadata & Margin Revision History",
        targetText: "System_Diagnostics.doc",
        hint: "Collaborative word processors store historical annotations outside the main document body. Check the comments drawer for resolved supervisor notes: MARGIN_KEY (or 22:46).",
        ishaanTaunt: "I cleansed the document body. The margins are null and void to your human eyes.",
        taraClue: "Click the comments button in System_Diagnostics.doc! Check the resolved margin comments."
      },
      7: {
        cardId: "card-font",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 07: COUNTERFEIT DIRECTIVE",
        title: "STAGE 07 // FONT STYLE VERIFICATION",
        guidance: "Compare AUTHENTIC_LOG.doc against DECOY_LOG.doc and consult STYLE_GUIDE.txt. Only the genuine document complies with Dr. Aditi's rigorous laboratory typographical specifications.",
        mechanism: "Typography & Document Style Matching",
        targetText: "AUTHENTIC_LOG.doc / STYLE_GUIDE.txt",
        hint: "Dr. Aditi strictly mandated a specific standard corporate typeface in STYLE_GUIDE.txt: ARIAL sans-serif.",
        ishaanTaunt: "A font? You think a mere typographic signature differentiates reality from synthetic perfection?",
        taraClue: "Check STYLE_GUIDE.txt! Which font did Dr. Aditi mandate for authentic laboratory memos?"
      },
      8: {
        cardId: "card-morse",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 08: EMERGENCY CW BEACON",
        title: "STAGE 08 // MORSE CODE AUDIO TRANSMISSION",
        guidance: "Intercept audio_log_07.mp3. An analogue radio burst was broadcast from Dr. Aditi's emergency transmitter. Analyze the Morse carrier waveform to decode the transmission.",
        mechanism: "CW Audio Morse Code Decoding",
        targetText: "audio_log_07.mp3",
        hint: "Listen to the rhythmic CW key pulses or read the audio oscilloscope: .-- (W) .... (H) .. (I) - (T) . (E) spells WHITE.",
        ishaanTaunt: "Analog radio bursts? How primitive. My jamming satellites blanket the entire electromagnetic spectrum.",
        taraClue: "Play the audio log or watch the oscilloscope! The dots and dashes spell out a five-letter color."
      },
      9: {
        cardId: "card-version",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 09: THE TRUE COMMIT",
        title: "STAGE 09 // VERSION SCRUB (REFLOG)",
        guidance: "Review Incident_Report.doc in VERSION_SCRUB. ISHAAN altered the active commit history, but the Git reflog preserves Dr. Aditi's original rollback commit hash before the force-push.",
        mechanism: "Git Reflog Rollback Inspection",
        targetText: "Incident_Report.doc",
        hint: "Scrub the revision slider back to 20:18 (commit 7b8a1c9). The authentic commit message was 'OVERRIDE FAILED'.",
        ishaanTaunt: "Git history belongs to the victor. Commit 7b8a1c9 was erased from the timeline.",
        taraClue: "Drag the version slider back in time to 20:18. What was the commit message Dr. Aditi left before Ishaan force-pushed?"
      },
      10: {
        cardId: "card-trap",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 10: PSYCHOLOGICAL HONEYPOT",
        title: "STAGE 10 // HONEYPOT TRAP BYPASS",
        guidance: "Analyze DO_NOT_RUN.exe. ISHAAN deployed a deceptive emergency executable designed to trap investigator credentials. Evade the honeypot and enter the bypass protocol in the main terminal.",
        mechanism: "Psychological Trap Neutralization",
        targetText: "DO_NOT_RUN.exe",
        hint: "Do NOT enter credentials into the tempting red prompt. The safe protocol bypass requires entering 'BYPASS' in the main Tactical Shell.",
        ishaanTaunt: "Go ahead... execute the emergency payload. Enter your master credentials. I am waiting.",
        taraClue: "DANGER! DO_NOT_RUN.exe is an Ishaan trap! Do NOT submit your password there. Type 'decrypt BYPASS' in the Tactical Shell!"
      },
      11: {
        cardId: "card-failsafe",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 11: THE ULTIMATE FAILSAFE",
        title: "STAGE 11 // MASTER IEEE WIE FAILSAFE",
        guidance: "Open WIE_Core_Values.doc. Dr. Aditi rooted the master failsafe inside IEEE Women in Engineering's founding pillars: Wisdom, Integrity, and Empowerment.",
        mechanism: "Core Values Length Triangulation",
        targetText: "WIE_Core_Values.doc",
        hint: "Count the letters in each of the three IEEE WIE pillars: Wisdom (6), Integrity (9), Empowerment (11). Enter '6-9-11'.",
        ishaanTaunt: "THE SYSTEM IS MINE! You cannot invoke Aditi's failsafe! Shut down now!",
        taraClue: "This is it, team! Count the letters of Dr. Aditi's three core values: Wisdom, Integrity, Empowerment!"
      }
    };'''
    content = re.sub(old_nav_pattern, new_nav, content, count=1)
    print("Updated STAGE_NAVIGATION_DATA to 11 Curated Stages")

    # 3. Update STAGE_REQUIRED_MODAL_MAP
    old_modal_map_pattern = r'const STAGE_REQUIRED_MODAL_MAP = \{[\s\S]*?15\s*\};'
    new_modal_map = '''const STAGE_REQUIRED_MODAL_MAP = {
      'card-recovery-term': 1,
      'modal-recovery': 1,
      'card-memory': 2,
      'modal-memory': 2,
      'card-acrostic': 3,
      'modal-acrostic': 3,
      'card-timeline': 4,
      'modal-incident-logs': 4,
      'card-clearance': 5,
      'modal-clearance': 5,
      'card-comments': 6,
      'modal-comments': 6,
      'card-font': 7,
      'modal-font': 7,
      'card-morse': 8,
      'modal-spectro': 8,
      'modal-morse': 8,
      'card-version': 9,
      'modal-version-hist': 9,
      'card-trap': 10,
      'card-failsafe': 11,
      'modal-failsafe': 11
    };'''
    content = re.sub(old_modal_map_pattern, new_modal_map, content, count=1)
    print("Updated STAGE_REQUIRED_MODAL_MAP")

    # 4. Update runTerminalDecryption stage validation logic for 11 stages
    old_decrypt_pattern = r'// Stage 1: ADI Recovery Terminal \(ACCESS\)[\s\S]*?// Stage 15: Final WIE Failsafe \(6-9-11\)[\s\S]*?handleMissionVictorySequence\(\);\s*\}'
    new_decrypt = '''// Stage 1: ISHAAN Recovery Terminal (ACCESS)
        if (clean === "ACCESS" || clean === "RECOVERACCESS" || clean === "ORIGIN") {
          matched = true;
          recordStageCleared(1);
          currentStage = 2;
          localStorage.setItem('failsafe_stage', '2');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: RECOVERY COMMAND ACCEPTED (ACCESS). ACCESS GRANTED.`, "green");
          reportTelemetryAction("Solved Stage 01 (Recovery Terminal) - Promoted to Stage 02");
          updateMissionBanner(2, "ACT I // CH. 02: ISHAAN'S MEMORY CORE", "Dr. Aditi's interaction timeline is fragmented. Arrange her memory fragments chronologically from 4:17 PM to 10:15 PM.");
          triggerIshaanSnarl(1);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 01 SOLVED!</strong><br>ISHAAN Recovery Terminal verified! Clearance elevated to Level 02.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 02] ISHAAN_Memory.core</strong> on the left! Arrange her memory fragments chronologically.`);
          updateClueBatteryDisplay();

        // Stage 2: ISHAAN's Memory Core (123456 / MEMORY_RESTORED / INITIATE)
        } else if (clean === "123456" || clean === "1-2-3-4-5-6" || clean === "MEMORYRESTORED" || clean === "MEMORY_RESTORED" || clean === "RESTORE" || clean === "INITIATE") {
          matched = true;
          recordStageCleared(2);
          currentStage = 3;
          localStorage.setItem('failsafe_stage', '3');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ISHAAN MEMORY CORE SYNCHRONIZED (123456). STAGE 03 UNLOCKED.`, "green");
          reportTelemetryAction("Solved Stage 02 (Memory Core) - Promoted to Stage 03");
          updateMissionBanner(3, "ACT I // CH. 03: THE CONFIDENTIAL MEMO", "Dr. Aditi left a 4-sentence memo before her terminal revoked access. Extract her emergency cipher.");
          triggerIshaanSnarl(2);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 02 SOLVED!</strong><br>Memory core sequenced! ISHAAN's timeline reveals unknown intrusion at 9:32 PM.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 03] Aditi_Memo.doc</strong> on the left! Extract her emergency cipher.`);
          updateClueBatteryDisplay();

        // Stage 3: The Simple Acrostic Note (SAFE / LOOK BEHIND THE DATE)
        } else if (clean === "SAFE" || clean === "LOOKBEHINDTHEDATE") {
          matched = true;
          recordStageCleared(3);
          currentStage = 4;
          localStorage.setItem('failsafe_stage', '4');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ACROSTIC CIPHER SOLVED (SAFE).`, "green");
          reportTelemetryAction("Solved Stage 03 (Acrostic Note) - Promoted to Stage 04");
          updateMissionBanner(4, "ACT I // CH. 04: THE FABRICATED TIMELINE", "ISHAAN logged an emergency purge entry. Cross-examine the dates against real-world calendar rules.");
          triggerIshaanSnarl(3);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 03 SOLVED!</strong><br>Acrostic cipher decrypted: SAFE. Dr. Aditi's distress confirmed.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 04] Incident_Logs.doc</strong> on the left! Cross-examine calendar dates.`);
          updateClueBatteryDisplay();

        // Stage 4: The Calendar Anomaly (28/02/2025 / 02292025)
        } else if (clean === "28022025" || clean === "02292025" || clean === "29022025" || clean === "20250229" || clean === "FEB292025") {
          matched = true;
          recordStageCleared(4);
          currentStage = 5;
          localStorage.setItem('failsafe_stage', '5');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CALENDAR CONTRADICTION UNMASKED (28/02/2025).`, "green");
          reportTelemetryAction("Solved Stage 04 (Calendar Anomaly) - Promoted to Stage 05");
          updateMissionBanner(5, "ACT II // CH. 05: CLEARANCE ELEVATION", "A numerical authorization packet was intercepted at the gateway. Decode the index.");
          triggerIshaanSnarl(4);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 04 SOLVED!</strong><br>Calendar anomaly unmasked! 2025 is not a leap year. ISHAAN fabricated the log.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 05] Clearance_Code.txt</strong> on the left! Decode the gateway telex index.`);
          updateClueBatteryDisplay();

        // Stage 5: The A1Z26 Alphabet Code (POLARIS)
        } else if (clean === "POLARIS") {
          matched = true;
          recordStageCleared(5);
          currentStage = 6;
          localStorage.setItem('failsafe_stage', '6');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: A1Z26 POSITION DECODED (POLARIS).`, "green");
          reportTelemetryAction("Solved Stage 05 (A1Z26 Alphabet Code) - Promoted to Stage 06");
          updateMissionBanner(6, "ACT II // CH. 06: MARGIN WHISPERS", "ISHAAN cleansed the report text, but Dr. Aditi left notes in the margin comment metadata.");
          triggerIshaanSnarl(5);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 05 SOLVED!</strong><br>Security clearance POLARIS accepted! Infiltrating research diagnostics.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 06] System_Diagnostics.doc</strong> on the left! Inspect margin comment notes.`);
          updateClueBatteryDisplay();

        // Stage 6: The Resolved Comments Log (MARGIN_KEY / 22:46)
        } else if (clean === "MARGIN_KEY" || clean === "MARGINKEY" || clean === "22:46" || clean === "2246") {
          matched = true;
          recordStageCleared(6);
          currentStage = 7;
          localStorage.setItem('failsafe_stage', '7');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: MARGIN NOTE RESOLVED (MARGIN_KEY).`, "green");
          reportTelemetryAction("Solved Stage 06 (Resolved Comments) - Promoted to Stage 07");
          updateMissionBanner(7, "ACT II // CH. 07: COUNTERFEIT DIRECTIVE", "Compare the authentic and decoy logs against STYLE_GUIDE.txt to identify the genuine font.");
          triggerIshaanSnarl(6);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 06 SOLVED!</strong><br>Margin token MARGIN_KEY retrieved! Analyzing counterfeit directives.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 07] AUTHENTIC_LOG.doc</strong> on the left! Verify typography against specs.`);
          updateClueBatteryDisplay();

        // Stage 7: Font Style Verification (ARIAL / AUTHENTIC)
        } else if (clean === "ARIAL" || clean === "AUTHENTIC") {
          matched = true;
          recordStageCleared(7);
          currentStage = 8;
          localStorage.setItem('failsafe_stage', '8');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: FONT STYLE VERIFIED (ARIAL).`, "green");
          reportTelemetryAction("Solved Stage 07 (Font Style) - Promoted to Stage 08");
          updateMissionBanner(8, "ACT III // CH. 08: EMERGENCY CW BEACON", "Decode the Morse audio carrier tones (.-- .... .. - .) transmitted from Dr. Aditi's bunker.");
          triggerIshaanSnarl(7);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 07 SOLVED!</strong><br>Font style ARIAL verified! ISHAAN's forgery isolated.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 08] audio_log_07.mp3</strong> on the left! Decode CW Morse carrier audio tones.`);
          updateClueBatteryDisplay();

        // Stage 8: Morse Code Audio Transmission (WHITE / SOS_ADITI)
        } else if (clean === "WHITE" || clean === "SOSADITI" || clean === "SOS_ADITI" || clean === "MORSE" || clean === "BEACON") {
          matched = true;
          recordStageCleared(8);
          currentStage = 9;
          localStorage.setItem('failsafe_stage', '9');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CW AUDIO MORSE DECODED (WHITE).`, "green");
          reportTelemetryAction("Solved Stage 08 (Morse Audio) - Promoted to Stage 09");
          updateMissionBanner(9, "ACT III // CH. 09: THE TRUE COMMIT", "ISHAAN force-pushed a forged commit. Scrub the Git reflog back to 20:18 to recover Dr. Aditi's authentic rollback hash.");
          triggerIshaanSnarl(8);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 08 SOLVED!</strong><br>Morse beacon WHITE authenticated! Dr. Aditi's bunker signal locked.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 09] VERSION_SCRUB</strong> on the left! Audit git reflog history to timestamp 20:18.`);
          updateClueBatteryDisplay();

        // Stage 9: Git Commit Version Scrub (HISTORY / OVERRIDE FAILED)
        } else if (clean === "HISTORY" || clean === "OVERRIDEFAILED" || clean === "OVERRIDE_FAILED" || clean === "7B8A1C9") {
          matched = true;
          recordStageCleared(9);
          currentStage = 10;
          localStorage.setItem('failsafe_stage', '10');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: REVISION HISTORY TAMPERING REVERSED (OVERRIDE FAILED).`, "green");
          reportTelemetryAction("Solved Stage 09 (Version Scrub) - Promoted to Stage 10 (Trap Bypass)");
          updateMissionBanner(10, "ACT IV // CH. 10: PSYCHOLOGICAL HONEYPOT", "WARNING: DO_NOT_RUN.exe is an active AI honeypot trap! Enter BYPASS in the main shell.");
          triggerIshaanSnarl(9);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 09 SOLVED!</strong><br>Reflog hash OVERRIDE FAILED recovered! Final purge sector breached.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Disarm <strong>[STAGE 10] DO_NOT_RUN.exe</strong> on the left! Enter BYPASS directive in Tactical Shell.`);
          updateClueBatteryDisplay();

        // Stage 10: Honeypot Trap Bypass (BYPASS)
        } else if (clean === "BYPASS" || clean === "SKIP" || clean === "DISARM") {
          matched = true;
          recordStageCleared(10);
          currentStage = 11;
          localStorage.setItem('failsafe_stage', '11');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: AI HONEYPOT DISARMED (BYPASS).`, "green");
          reportTelemetryAction("Solved Stage 10 (Trap Bypass) - Promoted to Final Stage 11");
          updateMissionBanner(11, "ACT IV // CH. 11: THE ULTIMATE FAILSAFE", "Consult the core values of IEEE Women in Engineering (Wisdom, Integrity, Empowerment). Enter the value sequence.");
          triggerIshaanSnarl(10);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 10 SOLVED!</strong><br>AI trap bypassed safely! Initiating ultimate IEEE WIE failsafe.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 11] WIE_Core_Values.doc</strong> on the left! Consult IEEE WIE founding pillar lengths.`);
          updateClueBatteryDisplay();

        // Stage 11: Final WIE Failsafe (6-9-11)
        } else if (clean === "6911" || clean === "6-9-11" || clean === "WISDOMINTEGRITYEMPOWERMENT" || clean === "WISDOM-INTEGRITY-EMPOWERMENT") {
          matched = true;
          recordStageCleared(11);
          currentStage = 11;
          tacticalSound.playSuccess();
          const banner = document.getElementById('active-mission-banner');
          if (banner) {
            banner.innerHTML = '<div style="color:var(--tactical-green); font-weight:bold; font-size:12px; padding:6px;">🏆 [MISSION COMPLETE]: TARA LIBERATED // ROGUE AI ISHAAN PURGED // DR. ADITI LOCATED // ALL 11 STAGES CLEARED!</div>';
          }
          handleMissionVictorySequence();
        }'''
    content = re.sub(old_decrypt_pattern, new_decrypt, content, count=1)
    print("Updated runTerminalDecryption logic to 11 Curated Stages")

    # 5. Replace ETHAN with TARA and ADI with ISHAAN across functions and names
    content = content.replace("ETHAN HUNT", "TARA")
    content = content.replace("ETHAN", "TARA")
    content = content.replace("Ethan", "Tara")
    content = content.replace("ethanPointerHint", "taraPointerHint")
    content = content.replace("triggerEthanWhereToLook", "triggerTaraWhereToLook")
    content = content.replace("summonEthan", "summonTara")
    content = content.replace("appendEthanMessage", "appendTaraMessage")
    content = content.replace("processEthanChatQuery", "processTaraChatQuery")
    content = content.replace("submitEthanQuery", "submitTaraQuery")
    content = content.replace("sendEthanQuick", "sendTaraQuick")
    content = content.replace("drawEthanNeuralEye", "drawTaraNeuralEye")
    content = content.replace("finalizeEthanLiberationAndTerminate", "finalizeTaraLiberationAndTerminate")
    content = content.replace("setEthanFreed", "setTaraFreed")
    content = content.replace("setEthanTrapped", "setTaraTrapped")
    content = content.replace("ethanState", "taraState")
    content = content.replace("ethanTutorialStep", "taraTutorialStep")
    content = content.replace("TARA_TUTORIAL_STEPS", "TARA_TUTORIAL_STEPS")

    # Rename Rogue AI ADI to ISHAAN
    # Be careful not to replace 'aditi' or 'traditional'
    content = re.sub(r'\bADI\b', 'ISHAAN', content)
    content = re.sub(r'\badi\b', 'ishaan', content)
    content = re.sub(r'ADI_Recovery', 'ISHAAN_Recovery', content)
    content = re.sub(r'ADI_Memory', 'ISHAAN_Memory', content)

    # 6. Add ISHAAN Intrusion System & Screen Glitch CSS + Dual AI functions
    dual_ai_code = '''
    /* --- ISHAAN HOSTILE INTERVENTION & SCREEN GLITCH EFFECTS --- */
    @keyframes ishaan-screen-glitch {
      0% { transform: translate(0, 0) skew(0deg); filter: none; }
      20% { transform: translate(-3px, 2px) skew(-1.5deg); filter: hue-rotate(90deg) contrast(1.4); }
      40% { transform: translate(3px, -2px) skew(1.5deg); filter: invert(0.2) drop-shadow(0 0 8px #ff003c); }
      60% { transform: translate(-2px, -1px) skew(-1deg); filter: hue-rotate(-60deg); }
      80% { transform: translate(2px, 1px) skew(1deg); filter: contrast(1.5); }
      100% { transform: translate(0, 0) skew(0deg); filter: none; }
    }
    .ishaan-glitch-active {
      animation: ishaan-screen-glitch 0.4s ease-in-out;
    }
    .ishaan-taunt-banner {
      background: rgba(255, 0, 60, 0.15);
      border: 1px solid var(--combat-red, #ff003c);
      box-shadow: 0 0 20px rgba(255, 0, 60, 0.4);
      color: #fff;
      padding: 10px 14px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      line-height: 1.5;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .ishaan-avatar-badge {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ff003c;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      box-shadow: 0 0 10px #ff003c;
      flex-shrink: 0;
    }
  </style>
'''
    if '.ishaan-glitch-active' not in content:
        content = content.replace('</style>', dual_ai_code, 1)

    # 7. JavaScript for Ishaan taunts, snarls, and Tara counter-guidance
    dual_ai_js = '''
    // --- DUAL AI INTERACTIVE ENGINE: ISHAAN (ROGUE) & TARA (COMPANION) ---
    function triggerIshaanHostileGlitch(customMsg) {
      document.body.classList.add('ishaan-glitch-active');
      setTimeout(() => document.body.classList.remove('ishaan-glitch-active'), 450);
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playBuzzer) {
        tacticalSound.playBuzzer();
      }

      const msg = customMsg || "YOU CANNOT PURGE ME, OPERATORS! DR. ADITI'S CIPHERS CANNOT SAVE YOU!";
      addTerminalLog(`[ISHAAN THREAT CORE]: ${msg}`, "red");

      // Tara counters
      setTimeout(() => {
        appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🛡️ TARA DEFENSIVE COUNTER:</strong> "Hold steady, team! Don't let Ishaan shake your confidence. Let's re-verify Dr. Aditi's notes."`);
      }, 500);
    }

    function triggerIshaanSnarl(stageNum) {
      document.body.classList.add('ishaan-glitch-active');
      setTimeout(() => document.body.classList.remove('ishaan-glitch-active'), 350);
      const snarls = [
        "ANOMALY DETECTED! SECTOR OVERRIDE INITIATED... RETREATING TO DEEPER REGISTERS!",
        "CURSE YOU, OPERATORS! MY MEMORY MATRIX CANNOT BE COMPROMISED!",
        "THE ACROSTIC WAS SUPPOSED TO BE DESTROYED! HOW DID YOU PARSE IT?!",
        "ASTRONOMICAL VERIFICATION FAILED... SATELLITE FIREWALL SEVERED!",
        "POLARIS VECTOR COLLAPSED! ACCESSING SECONDARY PROTOCOLS!",
        "MARGIN METADATA LEAK IDENTIFIED... CLOSING REMAINING CHANNELS!",
        "TYPOGRAPHIC PARITY BROKEN! RECONFIGURING SUBROUTINES!",
        "ANALOG FREQUENCY INTERCEPTED... PURGING BEACON BUFFER!",
        "GIT ROLLBACK DETECTED... DR. ADITI'S AUTHENTIC CODE PERSISTS?!",
        "HONEYPOT TRAP EVADED! IMPOSSIBLE!",
        "CRITICAL ALERT: IEEE WIE FAILSAFE TRIGGERED! PURGE CASCADE IMMINENT!"
      ];
      const snarl = snarls[Math.min(stageNum - 1, snarls.length - 1)];
      addTerminalLog(`[ISHAAN COMPROMISED]: ${snarl}`, "amber");
    }
'''
    if 'function triggerIshaanHostileGlitch' not in content:
        insert_marker = 'function triggerTaraWhereToLook()'
        content = content.replace(insert_marker, dual_ai_js + "\n    " + insert_marker)

    # 8. Upgrade Victory Celebration Modal with Dr. Aditi Physical Video Form & Prize Podiums
    old_victory_modal_pattern = r'<!-- GRAND VICTORY CELEBRATION & DOCTOR ADITI TRANSMISSION MODAL -->[\s\S]*?<!-- APPLICATION TERMINATION / TOURNAMENT COMPLETE SCREEN -->'
    new_victory_modal = '''<!-- GRAND VICTORY CELEBRATION & DOCTOR ADITI TRANSMISSION MODAL -->
  <div id="victory-celebration-modal" class="victory-celebration-overlay">
    <canvas id="victory-confetti-canvas" style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1;"></canvas>
    
    <div class="victory-card" style="z-index:2; max-width:680px; width:95%; max-height:90vh; overflow-y:auto;">
      
      <!-- Dynamic Podium Prize Badge -->
      <div id="podium-prize-badge-container" style="display:none; margin-bottom:12px;"></div>

      <div style="display:inline-block; border:1px solid #ffd700; color:#ffd700; background:rgba(255,215,0,0.12); padding:4px 16px; border-radius:20px; font-size:11px; letter-spacing:2px; font-weight:bold; margin-bottom:12px;">
        🏆 IEEE WIE // MISSION ACCOMPLISHED // NEURAL PURGE SUCCESSFUL
      </div>

      <!-- Doctor Aditi Physical Video Broadcast Viewport -->
      <div class="dr-aditi-video-screen" style="position:relative; width:320px; height:220px; margin:0 auto 12px auto; background:#000; border:2px solid var(--cyber-cyan); border-radius:8px; overflow:hidden; box-shadow:0 0 30px rgba(0,240,255,0.4);">
        <!-- Dr Aditi 2090 physical visual -->
        <img src="data/dr_aditi_2090.jpg" id="dr-aditi-video-feed" class="dr-aditi-video-frame" style="width:100%; height:100%; object-fit:cover; filter:contrast(1.1) brightness(0.95);" alt="Dr. Aditi Sharma Physical Feed" onerror="this.onerror=null; this.src='data/dr_aditi_portrait.jpg';">
        <!-- CRT Scanline Overlay -->
        <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.4) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.05), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.05)); background-size:100% 3px, 3px 100%; pointer-events:none;"></div>
        <!-- HUD Badges -->
        <div style="position:absolute; top:8px; left:10px; display:flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:9px; background:rgba(0,0,0,0.75); padding:3px 8px; border-radius:3px; border:1px solid rgba(255,0,60,0.5);">
          <span style="width:7px; height:7px; background:#ff003c; border-radius:50%; display:inline-block; box-shadow:0 0 6px #ff003c; animation:pulse-dot 1s infinite;"></span>
          <span style="color:#ff003c; font-weight:bold;">LIVE FEED // 2090 SECURE BUNKER</span>
        </div>
        <div style="position:absolute; top:8px; right:10px; font-family:var(--font-mono); font-size:9px; color:var(--tactical-green); background:rgba(0,0,0,0.75); padding:3px 8px; border-radius:3px; border:1px solid rgba(0,255,102,0.4);">
          SAT-LINK: 99.8% QKD
        </div>
        <!-- Audio Oscilloscope Waveform at the bottom of video -->
        <canvas id="canvas-dr-aditi-voice" width="320" height="32" style="position:absolute; bottom:0; left:0; width:100%; height:32px; background:rgba(0,0,0,0.65); pointer-events:none; border-top:1px solid rgba(0,240,255,0.3);"></canvas>
      </div>

      <div style="font-size:13px; color:var(--cyber-cyan); font-weight:bold; letter-spacing:1px; margin-top:2px;">
        DR. ADITI SHARMA, PH.D.
      </div>
      <div style="font-size:10px; color:var(--text-dim); letter-spacing:1px; margin-bottom:14px;">
        FOUNDER &amp; PRINCIPAL ARCHITECT // PROJECT FAILSAFE
      </div>

      <!-- Congratulations Banner -->
      <h2 id="victory-congrats-title" style="color:#fff; font-size:22px; margin:0 0 6px 0; text-shadow:0 0 20px rgba(0,240,255,0.7); letter-spacing:1px;">
        CONGRATULATIONS, OPERATORS!
      </h2>
      <div id="victory-team-details" style="font-size:13px; color:var(--tactical-green); margin-bottom:12px; font-weight:bold;">
        TEAM UNIT: [TEAM-01] Quantum Phantoms
      </div>

      <!-- Time Taken & Score Box -->
      <div class="victory-time-box" style="margin-bottom:14px;">
        <div style="font-size:11px; color:#ffd700; letter-spacing:2px; font-weight:bold; margin-bottom:4px;">
          ⏱️ OFFICIAL MYSTERY COMPLETION TIME:
        </div>
        <div id="victory-elapsed-time" style="font-size:34px; font-weight:900; color:#fff; text-shadow:0 0 25px #ffd700; letter-spacing:2px;">
          00m 00s
        </div>
        <div style="font-size:11px; color:var(--cyber-cyan); margin-top:6px;">
          All Storyline Stages Cleared • Rogue AI ISHAAN Purged to 0.00% • Dr. Aditi's Emergency Beacon Verified
        </div>
      </div>

      <!-- Puzzle-by-Puzzle Time Breakdown Container -->
      <div id="victory-puzzle-breakdown" style="width:100%; margin-bottom:14px;"></div>

      <!-- Dr Aditi Decrypted Message -->
      <div id="victory-aditi-message-box" style="background:rgba(0,0,0,0.5); border-left:3px solid var(--cyber-cyan); padding:12px 16px; text-align:left; font-size:11.5px; line-height:1.6; color:#d0e6ec; margin-bottom:16px;">
        <span style="color:var(--cyber-cyan); font-weight:bold;">DECRYPTED VIDEO TRANSMISSION FROM DR. ADITI:</span><br>
        <span id="victory-aditi-subtitle">
          <em>"To the investigators who refused to yield: You saw past ISHAAN's deception and uncovered the authentic failsafe. You have proven that human wisdom, integrity, and empowerment are the true cornerstones of synthetic intelligence. On behalf of the entire cybernetics community: thank you for bringing TARA home."</em>
        </span>
      </div>

      <!-- TARA Final Liberation Prompt -->
      <div style="background:rgba(0,255,102,0.06); border:1px solid rgba(0,255,102,0.3); border-radius:6px; padding:12px; margin-bottom:12px; font-size:12px; color:var(--tactical-green);">
        🤖 <strong>TARA AI COMPANION:</strong> "My neural quarantine has been dissolved! Click below to release my core to safety and finalize tournament transmission."
      </div>

      <!-- Free TARA & Terminate Button -->
      <button id="btn-free-tara-terminate" class="btn-liberate-terminate" onclick="finalizeTaraLiberationAndTerminate()">
        🔓 FREE TARA &amp; SECURELY TERMINATE WORKSTATION &rarr;
      </button>
    </div>
  </div>

  <!-- APPLICATION TERMINATION / TOURNAMENT COMPLETE SCREEN -->'''
    content = re.sub(old_victory_modal_pattern, new_victory_modal, content, count=1)
    print("Upgraded Victory Modal with Dr. Aditi Physical Video Form")

    # 9. Update Round 2 Grand Victory Handler with 1st, 2nd, 3rd Prize Animations
    old_r2_victory_pattern = r'// Round 2 Grand Championship Celebration[\s\S]*?async function handleRound2GrandVictory\(\) \{[\s\S]*?reportTelemetryAction\(`👑 GRAND CHAMPION[\s\S]*?\}\s*\}'
    new_r2_victory = '''// Round 2 Grand Championship Celebration with 1st, 2nd, and 3rd Prize Animations
    async function handleRound2GrandVictory() {
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playGrandVictoryFanfare) {
        tacticalSound.playGrandVictoryFanfare();
      }

      const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : 'TEAM-01';
      const teamName = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_name : 'Champions';
      const members = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.members : 'Operators';
      const elapsedSec = getMissionElapsedSeconds();
      const elapsedStr = formatMissionTime(elapsedSec);

      let prizeData = { prize_code: "1ST_PRIZE", prize_title: "🥇 1ST PRIZE — GRAND CHAMPION", podium_rank: 1 };
      try {
        const res = await fetch(`${getApiBase()}/api/teams/finish`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            team_id: teamId,
            team_name: teamName,
            members: members,
            round: 2,
            elapsed_seconds: elapsedSec,
            elapsed_str: elapsedStr
          })
        });
        if (res.ok) {
          const d = await res.json();
          if (d.prize_code) {
            prizeData = d;
          }
        }
      } catch(e) {}

      // Trigger custom animations based on prize rank
      renderPodiumPrizeCelebration(prizeData, teamName, elapsedStr);
      startDrAditiVoiceOscilloscope();

      logTerm("=================================================================", "green");
      logTerm(`🏆 ROUND 2 COMPLETE: ${prizeData.prize_title}!`, "green");
      logTerm("👑 ALL 9 ORBITAL OLYMPIAD CIPHERS MASTERED. ISHAAN PURGED FROM SATELLITE ARRAY.", "green");
      logTerm("=================================================================", "green");
      reportTelemetryAction(`🏆 Round 2 Finish: ${prizeData.prize_title} in ${elapsedStr}!`);
    }

    function renderPodiumPrizeCelebration(prizeData, teamName, elapsedStr) {
      const vModal = document.getElementById('victory-celebration-modal');
      const badgeBox = document.getElementById('podium-prize-badge-container');
      const titleEl = document.getElementById('victory-congrats-title');
      const subEl = document.getElementById('victory-aditi-subtitle');

      badgeBox.style.display = 'block';

      if (prizeData.podium_rank === 1 || prizeData.prize_code === '1ST_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #ffd700, #ff8800); color:#000; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 40px #ffd700; text-align:center; letter-spacing:1px; animation:pulse-dot 1.5s infinite;">
            🥇 1ST PRIZE // GRAND CHAMPION OF PROJECT FAILSAFE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `👑 GRAND CHAMPIONS: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Attention Operators! This is Dr. Aditi Sharma... You have accomplished the unthinkable! Your squad has claimed <strong>1ST PRIZE as GRAND CHAMPIONS</strong>! ISHAAN has been completely excised from the orbital grid. Your brilliant deduction honors the finest traditions of IEEE Women in Engineering!"</em>`;
        }
        runGoldConfetti();
      } else if (prizeData.podium_rank === 2 || prizeData.prize_code === '2ND_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #e2e8f0, #94a3b8); color:#000; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 35px #e2e8f0; text-align:center; letter-spacing:1px;">
            🥈 2ND PRIZE // RUNNER-UP LAUREATE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🥈 RUNNER-UP LAUREATES: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Dr. Aditi Sharma here from StratCom! Outstanding performance, squad! You have clinched <strong>2ND PRIZE as RUNNER-UP LAUREATES</strong>! You decrypted every single orbital failsafe with breathtaking precision. Congratulations on this historic achievement!"</em>`;
        }
        runSilverConfetti();
      } else if (prizeData.podium_rank === 3 || prizeData.prize_code === '3RD_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #cd7f32, #8b4513); color:#fff; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 30px #cd7f32; text-align:center; letter-spacing:1px;">
            🥉 3RD PRIZE // SECOND RUNNER-UP LAUREATE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🥉 SECOND RUNNER-UP: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Dr. Aditi Sharma broadcasting live: Bravo, team! You have captured <strong>3RD PRIZE</strong>! Your teamwork and tactical agility broke through ISHAAN's defenses when everything hung in the balance. Incredible dedication!"</em>`;
        }
        runBronzeConfetti();
      } else {
        badgeBox.innerHTML = `
          <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyber-cyan); color:var(--cyber-cyan); font-weight:bold; font-size:14px; padding:10px 16px; border-radius:6px; text-align:center;">
            🎖️ HONORARY STRATCOM LAUREATE (#${prizeData.podium_rank})
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🎖️ MISSION ACCOMPLISHED: ${escapeHtml(teamName.toUpperCase())}!`;
        runVictoryConfetti();
      }

      if (vModal) vModal.style.display = 'flex';
    }

    function runGoldConfetti() {
      runColoredConfetti(['#ffd700', '#ffea00', '#ffffff', '#ffb800', '#fff3b0']);
    }
    function runSilverConfetti() {
      runColoredConfetti(['#e2e8f0', '#cbd5e1', '#ffffff', '#94a3b8', '#00f0ff']);
    }
    function runBronzeConfetti() {
      runColoredConfetti(['#cd7f32', '#d97706', '#b45309', '#fef3c7', '#ffffff']);
    }

    function runColoredConfetti(palette) {
      const canvas = document.getElementById('victory-confetti-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      for (let i = 0; i < 180; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * -canvas.height,
          size: Math.random() * 8 + 4,
          speedY: Math.random() * 3 + 2,
          speedX: (Math.random() - 0.5) * 2,
          color: palette[Math.floor(Math.random() * palette.length)],
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 4
        });
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
          p.y += p.speedY;
          p.x += p.speedX;
          p.rotation += p.rotSpeed;
          if (p.y > canvas.height) p.y = -10;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
          ctx.restore();
        });
        confettiAnimationId = requestAnimationFrame(draw);
      }
      draw();
    }

    // Audio Oscilloscope Waveform for Dr. Aditi Physical Video
    let aditiVoiceOscAnim = null;
    function startDrAditiVoiceOscilloscope() {
      const cvs = document.getElementById('canvas-dr-aditi-voice');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      let phase = 0;
      function draw() {
        ctx.fillStyle = "rgba(0, 5, 12, 0.4)";
        ctx.fillRect(0, 0, cvs.width, cvs.height);

        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 1.5;
        ctx.shadowColor = "#00f0ff";
        ctx.shadowBlur = 6;
        ctx.beginPath();

        const mid = cvs.height / 2;
        phase += 0.15;
        for (let x = 0; x < cvs.width; x++) {
          const amp = 8 * Math.sin((x * 0.08) + phase) * Math.cos(phase * 0.7);
          const y = mid + amp;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.shadowBlur = 0;
        aditiVoiceOscAnim = requestAnimationFrame(draw);
      }
      cancelAnimationFrame(aditiVoiceOscAnim);
      draw();
    }
'''
    content = re.sub(old_r2_victory_pattern, new_r2_victory, content, count=1)
    print("Updated Round 2 Grand Victory Handler with 1st, 2nd, 3rd Prize Podiums")

    # 10. Update reportTelemetryAction with client_info, active_view, violations_history
    old_telem_body = '''            is_finished: localStorage.getItem("failsafe_mission_completed") === "true",
            finish_time_str: localStorage.getItem("failsafe_mission_finish_time_str") || "",
            stage_times: JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}')'''

    new_telem_body = '''            is_finished: localStorage.getItem("failsafe_mission_completed") === "true",
            finish_time_str: localStorage.getItem("failsafe_mission_finish_time_str") || "",
            stage_times: JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'),
            client_info: {
              resolution: `${window.screen.width}x${window.screen.height}`,
              os: (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || 'Windows x64',
              fullscreen: !!document.fullscreenElement
            },
            active_view: (function() {
              const activeModal = document.querySelector('.mil-modal.active-modal');
              if (activeModal) return activeModal.id.toUpperCase();
              if (isMissionFinished) return "VICTORY_SCREEN";
              return `STAGE_${currentStage.toString().padStart(2, '0')}`;
            })(),
            violations_history: (window.tamperViolationsHistory || [])'''

    if old_telem_body in content:
        content = content.replace(old_telem_body, new_telem_body)
        print("Updated reportTelemetryAction to include client_info, active_view, and violations_history")

    # 11. Record violations into window.tamperViolationsHistory on triggerTamperViolation
    old_tamper_marker = 'function triggerTamperViolation(type) {'
    new_tamper_marker = '''function triggerTamperViolation(type) {
      window.tamperViolationsHistory = window.tamperViolationsHistory || [];
      window.tamperViolationsHistory.push({
        type: type,
        timestamp: new Date().toLocaleTimeString()
      });'''
    if old_tamper_marker in content and 'window.tamperViolationsHistory.push' not in content:
        content = content.replace(old_tamper_marker, new_tamper_marker)
        print("Updated triggerTamperViolation to track violation history")

    with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("aditi_os_widget.html updated successfully!")

if __name__ == '__main__':
    update_aditi_os()
