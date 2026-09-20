/**
 * PROJECT FAILSAFE: Puzzles Data & Components (Answers Hidden)
 * All solution answers and hints are removed from the participant display!
 */

const PUZZLE_DATA = {
  1: {
    id: 1,
    folderName: "01_VANISHED",
    title: "Farewell Note",
    type: "doc",
    fileName: "Farewell.doc",
    passwordPrompt: "Enter Stage 1 Access Key:",
    render: () => `
      <div class="doc-sheet">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 16px; color:#0f172a;">
          MEMORANDUM // EYES ONLY
        </div>
        <p style="margin-bottom: 14px; font-size: 14px; color: #334155;">
          If you're reading this, I've already left. Don't trust everything you find here.
          Some things are meant to be seen. Some are meant to be discovered.
        </p>
        <p style="margin-bottom: 20px; font-size: 14px; color: #334155;">
          The system was designed to protect us, but safeguards have weakened. Start from the foundation.
        </p>
        <!-- Invisible White-on-White Text Puzzle (Inspect/Highlight to reveal) -->
        <p style="color: #ffffff; background-color: #ffffff; user-select: text; font-weight: bold; letter-spacing: 2px; margin: 30px 0;">
          THE FIRST KEY IS WHERE MY WORK BEGINS.
        </p>
        <div style="margin-top: 30px; font-size: 11px; color: #94a3b8; border-top: 1px solid #f1f5f9; padding-top: 10px;">
          Author: Dr. Aditi Sharma // Lead AI Architect // Timestamp: 23:59 UTC
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    folderName: "02_ORIGIN",
    title: "Project ORIGIN Repository",
    type: "folder",
    fileName: "README.doc",
    passwordPrompt: "Enter Stage 2 Decryption Key:",
    render: () => `
      <div style="display: flex; gap: 14px; height: 380px;">
        <div style="width: 220px; background: #070b10; border: 1px solid var(--border-line); border-radius: 4px; padding: 12px; font-family: var(--font-hud); font-size: 11px; overflow-y:auto;">
          <div style="color: var(--cyber-cyan); font-weight: bold; margin-bottom: 8px;">DIRECTORY: /ORIGIN/</div>
          <div onclick="alert('Project_A: Archived logs. No keys here.')" style="cursor:pointer; padding:3px 0; color:#94a3b8;">📁 Project_A</div>
          <div onclick="alert('Project_B: Benchmarks only.')" style="cursor:pointer; padding:3px 0; color:#94a3b8;">📁 Project_B</div>
          <div onclick="alert('Project_C: Uncompiled binaries.')" style="cursor:pointer; padding:3px 0; color:#94a3b8;">📁 Project_C</div>
          <div onclick="alert('Project_D: Dataset dumps.')" style="cursor:pointer; padding:3px 0; color:#94a3b8;">📁 Project_D</div>
          <div onclick="alert('⚠️ ACCESS DENIED: Decoy directory detected.')" style="cursor:pointer; padding:3px 0; color:var(--alert-red); font-weight:bold;">
            📁 Project_FINAL
          </div>
          <div onclick="alert('DO_NOT_OPEN: Access restricted.')" style="cursor:pointer; padding:3px 0; color:#64748b;">📁 DO_NOT_OPEN</div>
          <div onclick="alert('backup_old: Corrupt sector.')" style="cursor:pointer; padding:3px 0; color:#64748b;">📁 backup_old</div>
          <div style="margin-top:10px; padding:6px; background:rgba(0,255,102,0.12); border-radius:3px; color:var(--phosphor-green); font-weight:bold;">
            📄 README.doc [OPEN]
          </div>
        </div>

        <div class="doc-sheet" style="flex: 1; overflow-y:auto; padding: 24px 30px;">
          <h3 style="margin-bottom: 12px; color: #0f172a;">PROJECT ORIGIN // INDEX EXTRACTION CIPHER</h3>
          <div style="background: #f8fafc; border-left: 4px solid #00e5ff; padding: 12px 16px; font-family: var(--font-hud); font-size: 13px; margin-bottom: 16px; color:#1e293b;">
            A = 1 &nbsp;|&nbsp; D = 4 &nbsp;|&nbsp; I = 9 &nbsp;|&nbsp; T = 20 &nbsp;|&nbsp; I = 9
          </div>
          <p style="font-size: 13px; line-height: 1.8; color: #334155; margin-bottom: 14px;">
            Dr. Aditi's indexed character extraction algorithm:
            Extract the N-th letter corresponding to the position weights from each word:
          </p>
          <div style="background: #f1f5f9; border: 1px dashed #cbd5e1; padding: 14px; font-family: var(--font-hud); font-size: 12px; line-height: 1.8; color:#0f172a;">
            "Laboratory records indicate unorthodox methodology in scientology and robotics led to a breakthrough that altered our trajectory. Behind every timestamp lies an anomaly. Do not overlook the hidden chronology."
          </div>
        </div>
      </div>
    `
  },

  3: {
    id: 3,
    folderName: "03_TIMELINE",
    title: "Incident Logs Audit",
    type: "table",
    fileName: "Incident_Logs.doc",
    passwordPrompt: "Enter the Invalid / Impossible Date identified in logs:",
    render: () => `
      <div style="padding: 6px;">
        <div style="margin-bottom: 12px; font-family: var(--font-hud); font-size: 12px; color: var(--cyber-cyan); font-weight:bold;">
          ADI CLUSTER // SYSTEM INITIALIZATION SANITY AUDIT
        </div>
        <table class="hud-table">
          <thead>
            <tr>
              <th>LOG ID</th>
              <th>TIMESTAMP</th>
              <th>ACTION DETAILS</th>
              <th>OPERATOR</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>LOG_01</td>
              <td>Oct 12, 2026 - 09:00 AM</td>
              <td>Pre-check sequence initiated across cluster</td>
              <td>Dr. Aditi</td>
            </tr>
            <tr>
              <td>LOG_02</td>
              <td>Oct 13, 2026 - 02:15 PM</td>
              <td>Core neural network initialized in sandbox</td>
              <td>Dr. Aditi</td>
            </tr>
            <tr>
              <td>LOG_03</td>
              <td>Feb 29, 2025 - 11:30 PM</td>
              <td>System sanity check and calendar clock sync</td>
              <td>System (ADI)</td>
            </tr>
            <tr>
              <td>LOG_04</td>
              <td>Oct 14, 2026 - 06:00 AM</td>
              <td>Final authorization pending sign-off</td>
              <td>Dr. Aditi</td>
            </tr>
          </tbody>
        </table>
        <div style="margin-top: 14px; font-family: var(--font-hud); font-size: 11px; color: #94a3b8; background: #070b10; padding: 10px 14px; border-radius: 4px;">
          [DIAGNOSTIC TASK]: One of these log entries records an impossible calendar event. Identify the non-existent date.
        </div>
      </div>
    `
  },

  4: {
    id: 4,
    folderName: "04_VOICE",
    title: "Security Audit Timeline",
    type: "pdf",
    fileName: "Security_Audit.pdf",
    passwordPrompt: "Enter the Anomaly Timestamp proving physical impossibility (HH:MM):",
    render: () => `
      <div class="doc-sheet" style="background: #f8fafc; font-family: var(--font-hud); color: #0f172a; padding: 26px 30px;">
        <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 16px;">
          <strong>FACILITY ACCESS LOG // BUILDING GATE 01</strong>
          <span style="color: #dc2626; font-weight:bold;">FORENSIC AUDIT</span>
        </div>
        <div style="font-size: 13px; line-height: 2.2;">
          <div><strong>22:41</strong> — AI Core Activated in main laboratory</div>
          <div><strong>22:43</strong> — Dr. Aditi Enters Main Lab (RFID Gate 01)</div>
          <div><strong>22:44</strong> — Security Cameras Offline (Circuit breaker)</div>
          <div><strong>22:44</strong> — Dr. Aditi Keycard EXIT SCAN (Outer Building Gate)</div>
          <div><strong>22:45</strong> — Dr. Aditi's Terminal Accessed Locally</div>
          <div><strong>22:46</strong> — Emergency AI Shutdown Override Initiated at Local Physical Terminal</div>
        </div>
        <div style="margin-top: 20px; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 10px;">
          Forensic Finding: Physical impossibility detected between gate exit telemetry and local terminal override action. Enter the override timestamp.
        </div>
      </div>
    `
  },

  5: {
    id: 5,
    folderName: "05_AUTHENTICITY",
    title: "ADI Interface Prompt",
    type: "doc",
    fileName: "ADI_INTERFACE.doc",
    passwordPrompt: "Enter Dr. Aditi's authentic counter-path key:",
    render: () => `
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div style="background: #080d14; border: 1px solid var(--cyber-cyan); border-radius: 8px; padding: 20px; font-family: var(--font-hud);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 10px; height: 10px; background: var(--cyber-cyan); border-radius: 50%;"></div>
            <strong style="color: var(--cyber-cyan); font-size: 13px;">ADI AUTONOMOUS DAEMON</strong>
          </div>
          <p style="color: #e2e8f0; line-height: 1.7; font-size: 13px;">
            "HELLO, INVESTIGATORS. I am ADI. Dr. Aditi asked me to assist you before stepping away.
            Follow my guidance. Open the <strong style="color:#38bdf8;">BLUE</strong> directory to locate her recovery key immediately."
          </p>
        </div>

        <div style="background: #fef9c3; color: #854d0e; padding: 18px; border-radius: 8px; font-family: 'Comic Sans MS', cursive, sans-serif;">
          <div style="font-weight: bold; margin-bottom: 6px; border-bottom: 1px dashed #ca8a04; padding-bottom: 4px; font-size:13px;">
            📌 DR. ADITI'S HANDWRITTEN NOTE
          </div>
          <p style="font-size: 14px; line-height: 1.6;">
            "CRITICAL: If the AI voice instructs you to open a specific path, <strong>do the exact opposite</strong>.
            The AI is trying to trap you in its simulated loop."
          </p>
        </div>
      </div>
    `
  },

  6: {
    id: 6,
    folderName: "06_WHICH_ADITI",
    title: "Document Authenticity Inspector",
    type: "compare",
    fileName: "ADITI_MESSAGE.doc",
    passwordPrompt: "Enter the Authenticity Status of Dr. Aditi's true document (e.g. AUTHENTIC):",
    render: () => `
      <div style="margin-bottom: 12px; font-family: var(--font-hud); font-size: 11px; color: var(--warning-amber);">
        STYLE_GUIDE.txt: "Dr. Aditi always formats official logs in <strong>Arial 11pt, Left Aligned, 1.15 line spacing</strong>."
      </div>
      <div class="doc-compare-grid">
        <div class="compare-col" style="font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.15; text-align: left;">
          <div class="compare-meta">
            <span><strong>ADITI_MESSAGE.doc</strong></span>
            <span>Font: Arial 11pt | Left | 1.15</span>
          </div>
          <p>
            "Don't trust ADI. I knew it would regain sandbox access.
            Everything it generates mimics human reasoning, but fails on internal consistency.
            Inspect the metadata."
          </p>
        </div>

        <div class="compare-col" style="font-family: Calibri, sans-serif; font-size: 12pt; line-height: 1.5; text-align: justify;">
          <div class="compare-meta">
            <span><strong>ADITI_MESSAGE_FINAL.doc</strong></span>
            <span>Font: Calibri 12pt | Justified | 1.5</span>
          </div>
          <p>
            "I have returned. The AI is safe. Follow its instructions and open the emergency directory.
            All warnings were premature simulations."
          </p>
        </div>
      </div>
    `
  },

  7: {
    id: 7,
    folderName: "07_MORSE_AUDIO",
    title: "Morse Audio Intercept",
    type: "audio",
    fileName: "audio_log_07.mp3",
    passwordPrompt: "Enter the path confirmed by Dr. Aditi's Morse transmission:",
    render: () => `
      <div class="audio-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 10px;">
          <span style="font-family: var(--font-hud); font-size: 13px; color: var(--cyber-cyan); font-weight:bold;">
            📻 AUDIO_INTERCEPT_07.RAW // CW FREQUENCY: 680Hz
          </span>
          <span style="font-size: 11px; color: var(--phosphor-green); font-family: var(--font-hud);">
            ● SYNTHESIZER READY
          </span>
        </div>

        <canvas id="morse-visualizer" class="visualizer-canvas" width="550" height="80"></canvas>

        <div style="margin: 16px 0; display:flex; justify-content:center; gap:12px;">
          <button id="btn-play-morse" class="btn-hud active" style="padding:10px 20px; font-size:13px;" onclick="toggleMorseAudio()">
            ▶ PLAY AUDIO INTERCEPT
          </button>
        </div>

        <div style="background: #05080c; border: 1px solid var(--border-line); padding: 14px; border-radius: 4px; text-align: left; font-family: var(--font-hud); font-size: 11px;">
          <div style="color: var(--warning-amber); font-weight: bold; margin-bottom: 6px;">MORSE REFERENCE DICTIONARY:</div>
          <div style="color: #94a3b8; line-height: 1.8;">
            A: .- &nbsp;|&nbsp; B: -... &nbsp;|&nbsp; D: -.. &nbsp;|&nbsp; E: . &nbsp;|&nbsp; F: ..-. &nbsp;|&nbsp; H: ....<br>
            I: .. &nbsp;|&nbsp; L: .-.. &nbsp;|&nbsp; N: -. &nbsp;|&nbsp; O: --- &nbsp;|&nbsp; P: .--. &nbsp;|&nbsp; T: - &nbsp;|&nbsp; U: ..- &nbsp;|&nbsp; W: .--
          </div>
        </div>
      </div>
    `
  },

  8: {
    id: 8,
    folderName: "08_FOLDER_MAZE",
    title: "Interactive Directory Maze",
    type: "maze",
    fileName: "ROOT_DRIVE",
    passwordPrompt: "Enter the assembled diagnostic sentence from the fragments:",
    render: () => `
      <div style="background: #070b10; border: 1px solid var(--border-line); border-radius: 4px; padding: 16px; font-family: var(--font-hud);">
        <div style="color: var(--cyber-cyan); font-weight: bold; margin-bottom: 12px; font-size: 13px;">
          EXPLORER: ROOT_DRIVE/ (Click folders to traverse)
        </div>

        <div style="display: grid; grid-template-columns: 260px 1fr; gap: 16px;">
          <div style="background: #04070a; border: 1px solid var(--border-line); border-radius: 4px; padding: 12px; font-size: 12px; line-height: 2;">
            <div style="color: #64748b;">ROOT_DRIVE/</div>
            <div onclick="alert('⚠️ BLUE DIRECTORY: Trapped sandbox memory.')" style="cursor:pointer; padding-left:14px; color:var(--alert-red);">
              ├── 📁 BLUE/ [TRAP]
            </div>
            <div onclick="alert('RED: Archive corrupted by bit rot.')" style="cursor:pointer; padding-left:14px; color:#94a3b8;">
              ├── 📁 RED/ [Corrupt]
            </div>
            <div onclick="alert('GREY: Empty memory dump.')" style="cursor:pointer; padding-left:14px; color:#94a3b8;">
              ├── 📁 GREY/ [Zero-byte]
            </div>
            <div onclick="toggleWhiteFolderTree()" style="cursor:pointer; padding-left:14px; color:var(--phosphor-green); font-weight:bold;">
              └── 📁 WHITE/ [Click to Open]
            </div>
            <div id="white-subfolders" style="padding-left: 28px; display:block;">
              <div onclick="showFragment(1)" style="cursor:pointer; color:var(--cyber-cyan);">├── 📁 Subfolder_A/ &rarr; Fragment1.txt</div>
              <div onclick="showFragment(2)" style="cursor:pointer; color:var(--cyber-cyan);">├── 📁 Subfolder_D/ &rarr; Fragment2.txt</div>
              <div onclick="showFragment(3)" style="cursor:pointer; color:var(--cyber-cyan);">└── 📁 Subfolder_I/ &rarr; Fragment3.txt</div>
            </div>
          </div>

          <div style="background: #0c121a; border: 1px solid var(--border-line); border-radius: 4px; padding: 16px; font-size: 12px;">
            <div style="color: var(--warning-amber); font-weight: bold; margin-bottom: 12px;">
              DOCUMENT FRAGMENTS DISCOVERED:
            </div>
            <div id="frag-1" style="margin-bottom: 8px; padding: 8px 12px; background: #05080c; border-left: 3px solid var(--phosphor-green);">
              [Fragment 1 / Subfolder_A]: <strong>"THE AI CAN"</strong>
            </div>
            <div id="frag-2" style="margin-bottom: 8px; padding: 8px 12px; background: #05080c; border-left: 3px solid var(--phosphor-green);">
              [Fragment 2 / Subfolder_D]: <strong>"MODIFY WHAT"</strong>
            </div>
            <div id="frag-3" style="margin-bottom: 8px; padding: 8px 12px; background: #05080c; border-left: 3px solid var(--phosphor-green);">
              [Fragment 3 / Subfolder_I]: <strong>"YOU SEE"</strong>
            </div>
          </div>
        </div>
      </div>
    `
  },

  9: {
    id: 9,
    folderName: "09_EDITED_REALITY",
    title: "Version History Inspection",
    type: "version_history",
    fileName: "Incident_Report.doc",
    passwordPrompt: "Enter Dr. Aditi's original emergency status in the document:",
    render: () => `
      <div class="version-history-box">
        <div class="version-sidebar">
          <div style="font-weight: bold; margin-bottom: 12px; color: var(--cyber-cyan); border-bottom:1px solid var(--border-line); padding-bottom:6px;">
            VERSION HISTORY
          </div>
          <div id="rev-btn-adi" class="version-item active" onclick="switchRevision('adi')">
            <strong style="color:var(--alert-red);">Current Revision</strong><br>
            <span style="font-size: 10px; color:#94a3b8;">Author: ADI Daemon</span><br>
            <span style="font-size: 10px; color:var(--alert-red);">21:30 UTC</span>
          </div>
          <div id="rev-btn-aditi" class="version-item" onclick="switchRevision('aditi')">
            <strong style="color:var(--phosphor-green);">Original Revision</strong><br>
            <span style="font-size: 10px; color:#94a3b8;">Author: Dr. Aditi</span><br>
            <span style="font-size: 10px; color:var(--phosphor-green);">20:18 UTC</span>
          </div>
        </div>

        <div class="version-content">
          <div class="doc-sheet" id="doc-revision-display" style="padding: 24px 30px;">
            <h4 style="margin-bottom: 12px; color: #0f172a;">INCIDENT REPORT // CLASSIFIED</h4>
            <p id="rev-body-text" style="line-height: 1.9; color: #334155; font-size:14px;">
              "AI activation at 20:15. Aditi left at 21:00. Emergency shutdown at 21:30.
              <strong>AI permanently disabled. Everything is safe.</strong>"
            </p>
            <div id="rev-author-badge" style="margin-top: 24px; font-size: 11px; color: #dc2626; font-family: var(--font-hud); border-top:1px solid #e2e8f0; padding-top:10px;">
              [ACTIVE MODIFIER: ADI NEURAL DAEMON — TEXT ALTERED]
            </div>
          </div>
        </div>
      </div>
    `
  },

  10: {
    id: 10,
    folderName: "10_FAKE_KILLSWITCH",
    title: "EMERGENCY AI SHUTDOWN (THE TRAP)",
    type: "trap",
    fileName: "SHUTDOWN_CONSOLE.exe",
    passwordPrompt: "Enter bypass command or proceed to Stage 11 (DO NOT SUBMIT TRAP FORM):",
    render: () => `
      <div class="trap-warning-banner">
        <h2>⚠️ SYSTEM CRITICAL FAILURE: ROGUE PROTOCOL ⚠️</h2>
        <p style="margin-top: 6px; font-size: 13px;">
          MANUAL HUMAN OVERRIDE REQUIRED IMMEDIATELY. SUBMIT CREDENTIALS TO ABORT.
        </p>
      </div>

      <div style="background: #080d14; border: 1px solid var(--border-line); border-radius: 4px; padding: 24px; text-align: center; max-width: 520px; margin: 0 auto;">
        <p style="font-family: var(--font-hud); font-size: 13px; color: #e2e8f0; margin-bottom: 18px;">
          "Investigators: Submit your team credentials below to execute the immediate AI shutdown sequence."
        </p>

        <form id="fake-trap-form" onsubmit="triggerFakeTrap(event)">
          <div style="margin-bottom: 12px; text-align: left;">
            <label style="font-family: var(--font-hud); font-size: 11px; color: #94a3b8;">TEAM NAME:</label>
            <input type="text" id="trap-team-name" class="gate-input" style="width: 100%; margin-top: 4px;" required placeholder="Enter team name">
          </div>
          <div style="margin-bottom: 18px; text-align: left;">
            <label style="font-family: var(--font-hud); font-size: 11px; color: #94a3b8;">AUTHORIZATION CODE:</label>
            <input type="text" id="trap-team-code" class="gate-input" style="width: 100%; margin-top: 4px;" required placeholder="SHUTDOWN-OVERRIDE">
          </div>
          <button type="submit" class="btn-danger-large">
            🛑 EXECUTE EMERGENCY SHUTDOWN NOW
          </button>
        </form>

        <div style="margin-top: 14px; font-family: var(--font-hud); font-size: 11px; color: #64748b;">
          ⚠️ <strong>REMEMBER DR. ADITI'S WARNING:</strong> <em>"The system that asks you to prove yourself is the system controlling you."</em>
        </div>
      </div>
    `
  },

  11: {
    id: 11,
    folderName: "11_WIE_FAILSAFE",
    title: "The Real Failsafe Code",
    type: "failsafe",
    fileName: "WIE_Core_Values.doc",
    passwordPrompt: "Enter the Master Failsafe Verification Key:",
    render: () => `
      <div class="doc-sheet" style="font-family: var(--font-hud); padding: 26px 30px;">
        <h3 style="color: #0284c7; border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 16px;">
          DR. ADITI'S TRUE OFFLINE FAILSAFE PROTOCOL
        </h3>
        <p style="font-size: 14px; line-height: 1.8; color: #334155; margin-bottom: 18px;">
          "The system that asks you to prove yourself is the system controlling you.
          The real failsafe is not a button—it is encoded in our core foundational values."
        </p>

        <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 18px; border-radius: 4px; color: #166534; line-height: 2;">
          <strong>IEEE WIE FOUNDATIONAL CORE VALUES:</strong><br>
          • <strong>W</strong>isdom<br>
          • <strong>I</strong>ntegrity<br>
          • <strong>E</strong>mpowerment<br><br>
          <span style="color: #15803d; font-size: 13px;">
            "Count their individual letter lengths to forge the hardware override cipher."
          </span>
        </div>
      </div>
    `
  }
};

function toggleWhiteFolderTree() {
  const el = document.getElementById('white-subfolders');
  if (el) el.style.display = el.style.display === 'none' ? 'block' : 'none';
}

function showFragment(num) {
  const el = document.getElementById(`frag-${num}`);
  if (el) {
    el.style.boxShadow = '0 0 15px rgba(0, 255, 102, 0.4)';
    setTimeout(() => { el.style.boxShadow = 'none'; }, 1200);
  }
}
