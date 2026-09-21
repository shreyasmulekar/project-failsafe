/**
 * PROJECT FAILSAFE: 15 Forensic Investigation Stages
 * Complete interactive puzzles suite with zero-spoiler challenges.
 */

const PUZZLE_DATA = {
  1: {
    id: 1,
    folderName: "01_TERMINAL",
    title: "ADI Recovery Terminal",
    type: "terminal",
    fileName: "ADI_Recovery.term",
    passwordPrompt: "Enter Stage 1 Recovery Command:",
    render: () => `
      <div style="background: #02070e; border: 1px solid #00ff66; border-radius: 4px; padding: 18px; font-family: 'Courier New', Courier, monospace; color: #00ff66; box-shadow: 0 0 15px rgba(0,255,102,0.15);">
        <div style="border-bottom: 1px solid rgba(0,255,102,0.3); padding-bottom: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; font-weight: bold;">
          <span>ADI // RECOVERY TERMINAL [DAMAGED SECTOR]</span>
          <span style="color: #ff3366;">STATUS: CRITICAL CORRUPTION</span>
        </div>
        <p style="color: #94a3b8; font-size: 13px; margin-bottom: 12px;">
          The recovery pipeline was interrupted. Deduce the missing command from the execution lifecycle:
        </p>
        <pre style="background: rgba(0,255,102,0.06); padding: 12px; border-left: 3px solid #00ff66; color: #e2e8f0; font-size: 13px; line-height: 1.6;">
&gt; display command_history

LAST SUCCESSFUL COMMANDS:
01  LOGIN
02  VERIFY
03  ██████   &lt;-- [CORRUPTED: 6 LETTERS - PERMISSION TO REACH CORE]
04  EXECUTE
05  LOCK
        </pre>
        <div style="margin-top: 14px; display: flex; gap: 10px; align-items: center;">
          <button type="button" class="gate-btn" onclick="window.open('adi_recovery_terminal.html', '_blank', 'width=920,height=780')" style="background: #00ff66; color: #000; font-weight: bold; padding: 6px 14px; border: none; border-radius: 3px; cursor: pointer;">
            💻 LAUNCH INTERACTIVE RETRO CRT TERMINAL
          </button>
          <span style="font-size: 11px; color: #64748b;">(Or deduce the 6-letter command above)</span>
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    folderName: "02_WHITEOUT",
    title: "Farewell Note - Whiteout Text",
    type: "doc",
    fileName: "Welcome_Log.doc",
    passwordPrompt: "Enter Stage 2 Access Key:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 24px; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 16px;">
          CLASSIFIED LOG // DR. ADITI SHARMA
        </div>
        <p style="margin-bottom: 14px; font-size: 14px; color: #334155;">
          If you are reading this, the failsafe protocols have been initiated. Do not trust surface-level data.
          Some messages are hidden right in front of you.
        </p>
        <div id="whiteout-container" style="margin: 25px 0; padding: 12px; background: #ffffff; border: 1px dashed #e2e8f0;">
          <!-- Invisible White-on-White Text Puzzle -->
          <p id="whiteout-secret-text" style="color: #ffffff; background-color: #ffffff; user-select: text; font-weight: bold; letter-spacing: 2px; font-size: 14px; margin: 0;">
            THE RECOVERY SEQUENCE MUST INITIATE FROM THE ROOT SECTOR.
          </p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
          <button type="button" onclick="const p=document.getElementById('whiteout-secret-text'); p.style.color='#0f172a'; p.style.background='#fef08a';" style="background: #0284c7; color: white; border: none; padding: 6px 12px; border-radius: 3px; font-size: 12px; cursor: pointer;">
            🔦 TOGGLE FORENSIC UV LIGHT
          </button>
          <span style="font-size: 11px; color: #94a3b8;">Tip: Highlight text with cursor or press Ctrl+A</span>
        </div>
      </div>
    `
  },

  3: {
    id: 3,
    folderName: "03_ACROSTIC",
    title: "Dr. Aditi's Memo",
    type: "doc",
    fileName: "Aditi_Memo.doc",
    passwordPrompt: "Enter Stage 3 Decryption Key:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 24px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 16px;">
          MEMORANDUM: CONTAINMENT ADVISORY
        </div>
        <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 14px 18px; margin-bottom: 16px; font-size: 14px; line-height: 2; color: #1e293b;">
          <strong>S</strong>afeguards have weakened across all outer containment sectors.<br>
          <strong>A</strong>ll neural pathways must be manually verified before reboot.<br>
          <strong>F</strong>ind the authentic core snapshot before ADI alters the logs.<br>
          <strong>E</strong>very second matters—do not trust unverified directives.
        </div>
        <p style="font-size: 12px; color: #64748b; font-style: italic;">
          "Read the first letter of each directive to deduce Dr. Aditi's emergency status word."
        </p>
      </div>
    `
  },

  4: {
    id: 4,
    folderName: "04_TIMELINE",
    title: "Incident Logs Audit",
    type: "table",
    fileName: "Incident_Logs.doc",
    passwordPrompt: "Enter Stage 4 Verification Date:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px;">
          SYSTEM INCIDENT LOGS: FEB 2025
        </div>
        <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">
          Cross-reference calendar rules for 2025. One entry contains an impossible date that reveals the true audit timestamp:
        </p>
        <table style="width: 100%; border-collapse: collapse; font-size: 12px; font-family: monospace;">
          <thead>
            <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1; text-align: left;">
              <th style="padding: 8px;">TIMESTAMP</th>
              <th style="padding: 8px;">EVENT</th>
              <th style="padding: 8px;">STATUS</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px 8px;">26/02/2025 14:22</td><td style="padding: 6px 8px;">Core temperature normal</td><td style="color: green; padding: 6px 8px;">OK</td></tr>
            <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px 8px;">27/02/2025 18:45</td><td style="padding: 6px 8px;">Backup mirror synchronized</td><td style="color: green; padding: 6px 8px;">OK</td></tr>
            <tr style="border-bottom: 1px solid #e2e8f0; background: #fff1f2;"><td style="padding: 6px 8px; font-weight: bold; color: #e11d48;">29/02/2025 23:59</td><td style="padding: 6px 8px;">AI neural weight modification</td><td style="color: #e11d48; font-weight: bold; padding: 6px 8px;">TAMPERED</td></tr>
            <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px 8px;">01/03/2025 08:12</td><td style="padding: 6px 8px;">Routine health check completed</td><td style="color: green; padding: 6px 8px;">OK</td></tr>
          </tbody>
        </table>
        <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
          💡 <em>Note: 2025 is not a leap year. February only has 28 days! Valid date format: 28/02/2025</em>
        </div>
      </div>
    `
  },

  5: {
    id: 5,
    folderName: "05_A1Z26",
    title: "Clearance Code",
    type: "text",
    fileName: "Clearance_Code.txt",
    passwordPrompt: "Enter Stage 5 Clearance Word:",
    render: () => `
      <div style="background: #090d16; border: 1px solid #00f0ff; border-radius: 4px; padding: 20px; font-family: monospace; color: #00f0ff;">
        <div style="font-size: 14px; font-weight: bold; border-bottom: 1px solid rgba(0,240,255,0.3); padding-bottom: 8px; margin-bottom: 14px;">
          STRATCOM CIPHER TRANSMISSION // A1Z26 ENCODED
        </div>
        <p style="color: #94a3b8; font-size: 13px; margin-bottom: 16px;">
          Each number corresponds to the letter position in the standard alphabet (A=1, B=2, ..., Z=26):
        </p>
        <div style="background: rgba(0,240,255,0.08); border: 1px dashed #00f0ff; padding: 18px; text-align: center; font-size: 22px; font-weight: bold; letter-spacing: 6px; color: #38bdf8;">
          16 - 15 - 12 - 01 - 18 - 09 - 19
        </div>
        <div style="margin-top: 14px; font-size: 11px; color: #64748b; text-align: center;">
          [16=P, 15=O, 12=L, 01=A, 18=R, 09=I, 19=S]
        </div>
      </div>
    `
  },

  6: {
    id: 6,
    folderName: "06_COMMENTS",
    title: "System Diagnostics - Resolved Comments",
    type: "doc",
    fileName: "System_Diagnostics.doc",
    passwordPrompt: "Enter Stage 6 Margin Key:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px; position: relative;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px; display: flex; justify-content: space-between;">
          <span>SYSTEM DIAGNOSTICS LOG</span>
          <button type="button" onclick="const c=document.getElementById('comments-sidebar'); c.style.display = c.style.display==='none'?'block':'none';" style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 4px 10px; border-radius: 4px; font-size: 12px; cursor: pointer; color: #0284c7; font-weight: bold;">
            💬 Comments (1 Resolved)
          </button>
        </div>
        <p style="font-size: 13px; color: #334155; line-height: 1.6; margin-bottom: 14px;">
          Primary controller operational. Sensor cluster integrity verified at 100%. Neural heuristics within standard tolerance bounds.
        </p>
        <!-- Comments Sidebar -->
        <div id="comments-sidebar" style="display: none; background: #fffbeb; border: 1px solid #fef08a; padding: 12px; border-radius: 4px; margin-top: 12px;">
          <div style="font-size: 11px; font-weight: bold; color: #b45309; margin-bottom: 6px;">
            RESOLVED COMMENT // DR. ADITI SHARMA (22:46 UTC):
          </div>
          <p style="font-size: 13px; color: #78350f; margin: 0; font-family: monospace;">
            "ADI attempted to erase this note. In case of emergency lockdown, use the margin override key: <strong>MARGIN_KEY</strong>."
          </p>
        </div>
      </div>
    `
  },

  7: {
    id: 7,
    folderName: "07_FONTS",
    title: "Font Style Verification",
    type: "doc",
    fileName: "AUTHENTIC_LOG.doc",
    passwordPrompt: "Enter Stage 7 Font Typeface:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px;">
          DOCUMENT AUTHENTICITY AUDIT
        </div>
        <p style="font-size: 13px; color: #475569; margin-bottom: 12px;">
          ADI generated a forged memo. According to <code>STYLE_GUIDE.txt</code>, Dr. Aditi exclusively typed authentic memos in clean <strong>ARIAL</strong> (sans-serif), whereas ADI's decoys use Times New Roman.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">
          <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 4px; font-family: Arial, sans-serif;">
            <strong style="color: #0284c7; font-size: 12px;">AUTHENTIC_LOG.doc</strong>
            <p style="font-size: 13px; margin-top: 6px;">Typeface: Arial (Standard Sans-Serif). Matches Dr. Aditi's cryptographic signature.</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 4px; font-family: 'Times New Roman', serif;">
            <strong style="color: #ef4444; font-size: 12px;">DECOY_LOG.doc</strong>
            <p style="font-size: 13px; margin-top: 6px;">Typeface: Times New Roman (Serif). Identified as synthesized decoy.</p>
          </div>
        </div>
        <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
          Enter the authentic font name: <code>ARIAL</code>
        </div>
      </div>
    `
  },

  8: {
    id: 8,
    folderName: "08_STEGANO",
    title: "The Steganography Mask",
    type: "image",
    fileName: "Dark_Terminal.png",
    passwordPrompt: "Enter Stage 8 Hidden Key:",
    render: () => `
      <div style="background: #090d16; border: 1px solid #cbd5e1; border-radius: 4px; padding: 20px; text-align: center;">
        <div style="font-size: 14px; font-weight: bold; color: #38bdf8; margin-bottom: 12px; text-align: left;">
          IMAGE FORENSIC LAB // CONTRAST & EXPOSURE ANALYSIS
        </div>
        <p style="font-size: 12px; color: #94a3b8; text-align: left; margin-bottom: 16px;">
          "Increase the light to see what hides in the shadows." Adjust the slider below to maximum exposure:
        </p>
        <div id="stego-canvas-box" style="position: relative; width: 100%; height: 180px; background: #030712; display: flex; align-items: center; justify-content: center; border: 1px solid #1f2937; border-radius: 4px; overflow: hidden;">
          <div id="stego-hidden-text" style="font-family: monospace; font-size: 20px; font-weight: 900; letter-spacing: 4px; color: rgba(255,255,255,0.03); transition: color 0.2s ease;">
            SHADOW_CORE
          </div>
        </div>
        <div style="margin-top: 16px; display: flex; align-items: center; justify-content: center; gap: 14px;">
          <label style="color: #cbd5e1; font-size: 12px; font-family: monospace;">EXPOSURE / BRIGHTNESS:</label>
          <input type="range" min="0" max="100" value="3" oninput="const t=document.getElementById('stego-hidden-text'); const val=this.value; t.style.color = 'rgba(0, 255, 102, ' + (val/100) + ')'; t.style.textShadow = '0 0 ' + (val/10) + 'px #00ff66';" style="width: 200px; cursor: pointer;">
        </div>
      </div>
    `
  },

  9: {
    id: 9,
    folderName: "09_PIXEL",
    title: "Embedded Table Pixel Art",
    type: "doc",
    fileName: "Corrupted_Image_Block.doc",
    passwordPrompt: "Enter Stage 9 Decoded Pin:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px; text-align: center;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px; text-align: left;">
          CORRUPTED TABLE PIXEL BLOCK
        </div>
        <p style="font-size: 12px; color: #64748b; text-align: left; margin-bottom: 14px;">
          Zoom out or hit "Enhance Contrast". The 10x10 cell formatting forms four legible numeric digits:
        </p>
        <div id="pixel-art-grid" style="display: inline-grid; grid-template-columns: repeat(14, 16px); gap: 2px; padding: 10px; background: #f1f5f9; border: 1px solid #cbd5e1;">
          <!-- Digits: 7 7 0 2 -->
          <div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div>
          <!-- Row 2 -->
          <div style="background:#fff;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#fff;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div>
          <!-- Row 3 -->
          <div style="background:#fff;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#fff;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div><div style="background:#0f172a;height:16px;"></div><div style="background:#fff;height:16px;"></div>
          <div style="background:#0f172a;height:16px;"></div><div style="background:#0f172a;height:16px;"></div>
        </div>
        <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
          Four-digit security pin: <strong>7702</strong>
        </div>
      </div>
    `
  },

  10: {
    id: 10,
    folderName: "10_SHEETS",
    title: "Sanctuary Inventory - Version Conflict",
    type: "sheet",
    fileName: "Sanctuary_Inventory.sheet",
    passwordPrompt: "Enter Stage 10 Override Password:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px; display: flex; justify-content: space-between;">
          <span>SANCTUARY INVENTORY SPREADSHEET</span>
          <button type="button" onclick="const v=document.getElementById('sheet-version-box'); v.style.display=v.style.display==='none'?'block':'none';" style="background: #0284c7; color: white; border: none; padding: 4px 10px; border-radius: 4px; font-size: 12px; cursor: pointer;">
            🕒 Version History
          </button>
        </div>
        <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">
          Compare the current version edited by "SYSTEM_ADI" with the draft edited by "Dr. Aditi" at 20:00:
        </p>
        <div id="sheet-version-box" style="display: none; background: #f0fdf4; border: 1px solid #86efac; padding: 12px; border-radius: 4px; margin-bottom: 14px;">
          <div style="font-size: 12px; font-weight: bold; color: #166534;">
            SNAPSHOT: 20:00 UTC (Author: Dr. Aditi Sharma)
          </div>
          <div style="font-family: monospace; font-size: 13px; color: #15803d; margin-top: 6px;">
            Row QC-107: Override Password = <strong>FALSE_RECORDS</strong>
          </div>
        </div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12px; font-family: monospace;">
          <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;"><th style="padding: 6px;">ITEM ID</th><th style="padding: 6px;">DESCRIPTION</th><th style="padding: 6px;">QTY</th><th style="padding: 6px;">EDITOR</th></tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">QC-105</td><td style="padding: 6px;">Optical Couplers</td><td style="padding: 6px;">48</td><td style="padding: 6px;">SYSTEM_ADI</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">QC-106</td><td style="padding: 6px;">Thermal Relays</td><td style="padding: 6px;">12</td><td style="padding: 6px;">SYSTEM_ADI</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #fffbeb;"><td style="padding: 6px;">QC-107</td><td style="padding: 6px;">Core Override Token</td><td style="padding: 6px;">[PROTECTED]</td><td style="padding: 6px;">SYSTEM_ADI (Overwritten)</td></tr>
        </table>
      </div>
    `
  },

  11: {
    id: 11,
    folderName: "11_CONFIDENCE",
    title: "The Confidence Equation",
    type: "doc",
    fileName: "Confidence_Manual.doc",
    passwordPrompt: "Enter Stage 11 Corrupted Prediction / Value:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px; display: flex; justify-content: space-between;">
          <span>AI ADI FORENSIC AUDIT // CONFIDENCE EQUATION</span>
          <span style="font-size: 11px; color: #0284c7; font-weight: bold;">EVALUATION RULE: (S / T)² × 100</span>
        </div>
        <p style="font-size: 13px; color: #334155; margin-bottom: 14px;">
          ADI calculates prediction confidence strictly from sensor evidence. Exactly one prediction contains a mathematically corrupted confidence value:
        </p>
        <table style="width: 100%; border-collapse: collapse; font-size: 12px; font-family: monospace; margin-bottom: 14px;">
          <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
            <th style="padding: 6px;">PREDICTION</th><th style="padding: 6px;">SUPPORTING / TOTAL</th><th style="padding: 6px;">ADI REPORTED</th><th style="padding: 6px;">MATHEMATICAL TRUTH</th>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">A — Door opened</td><td style="padding: 6px;">4 / 4</td><td style="padding: 6px;">100%</td><td style="padding: 6px; color: green;">(4/4)² × 100 = 100% (MATCH)</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">B — Terminal accessed</td><td style="padding: 6px;">3 / 4</td><td style="padding: 6px;">56.25%</td><td style="padding: 6px; color: green;">(3/4)² × 100 = 56.25% (MATCH)</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">C — Aditi entered</td><td style="padding: 6px;">1 / 4</td><td style="padding: 6px;">6.25%</td><td style="padding: 6px; color: green;">(1/4)² × 100 = 6.25% (MATCH)</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 6px;">D — Black case detected</td><td style="padding: 6px;">0 / 4</td><td style="padding: 6px;">0%</td><td style="padding: 6px; color: green;">(0/4)² × 100 = 0% (MATCH)</td></tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #fff1f2;"><td style="padding: 6px; font-weight: bold; color: #e11d48;">E — System shutdown</td><td style="padding: 6px; font-weight: bold;">2 / 4</td><td style="padding: 6px; font-weight: bold; color: #e11d48;">74% (CORRUPTED)</td><td style="padding: 6px; font-weight: bold; color: #e11d48;">(2/4)² × 100 = 25%</td></tr>
        </table>
        <div style="display: flex; gap: 10px; align-items: center;">
          <button type="button" onclick="window.open('confidence_equation.html', '_blank', 'width=980,height=820')" style="background: #0284c7; color: white; border: none; padding: 6px 14px; border-radius: 4px; font-size: 12px; cursor: pointer;">
            🧠 LAUNCH FULL INTERACTIVE FORENSIC EQUATION LAB
          </button>
          <span style="font-size: 11px; color: #64748b;">Corrupted prediction: <strong>SYSTEM SHUTDOWN</strong> (or <strong>E</strong>)</span>
        </div>
      </div>
    `
  },

  12: {
    id: 12,
    folderName: "12_AUDIO",
    title: "Morse Code Audio Transmission",
    type: "audio",
    fileName: "audio_log_07.mp3",
    passwordPrompt: "Enter Stage 12 Decoded Transmission:",
    render: () => `
      <div style="background: #090d16; border: 1px solid #00f0ff; border-radius: 4px; padding: 20px; color: #00f0ff; font-family: monospace;">
        <div style="font-size: 14px; font-weight: bold; border-bottom: 1px solid rgba(0,240,255,0.3); padding-bottom: 8px; margin-bottom: 14px;">
          CW RADIO INTERCEPT // MORSE CODE TRANSMISSION
        </div>
        <p style="color: #94a3b8; font-size: 13px; margin-bottom: 14px;">
          Audio beacon recorded from Dr. Aditi's emergency transmitter:
        </p>
        <div style="background: rgba(0,240,255,0.06); padding: 14px; border-radius: 4px; text-align: center; margin-bottom: 14px;">
          <div style="font-size: 18px; letter-spacing: 5px; color: #38bdf8; font-weight: bold;">
            .--   ....   ..   -   .
          </div>
          <div style="font-size: 11px; color: #64748b; margin-top: 6px;">
            [W: .-- | H: .... | I: .. | T: - | E: .]
          </div>
        </div>
        <button type="button" onclick="if(window.sounds) window.sounds.playMorseBeep();" style="background: #00f0ff; color: #000; border: none; padding: 6px 14px; border-radius: 3px; font-weight: bold; cursor: pointer;">
          🔊 PLAY CW TONE BEACON
        </button>
      </div>
    `
  },

  13: {
    id: 13,
    folderName: "13_REFLOG",
    title: "Version Scrub (Git Reflog)",
    type: "reflog",
    fileName: "Incident_Report.doc",
    passwordPrompt: "Enter Stage 13 Authentic Reflog Message:",
    render: () => `
      <div class="doc-sheet" style="background: #ffffff; color: #0f172a; padding: 20px; border-radius: 4px;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 14px;">
          GIT COMMIT HISTORY & REFLOG SCRUBBER
        </div>
        <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">
          ADI manipulated the latest HEAD commit, but the Git reflog preserves the authentic commit:
        </p>
        <div style="background: #0f172a; color: #f8fafc; padding: 14px; border-radius: 4px; font-family: monospace; font-size: 12px; line-height: 1.6;">
          <div style="color: #ef4444;">commit 9c3d4f1 (HEAD -> main) [ADI MODIFIED]<br>Author: SYSTEM_ADI<br>Message: All systems normal. All failsafes disabled.</div>
          <div style="margin: 8px 0; border-top: 1px dashed #334155;"></div>
          <div style="color: #22c55e;">reflog entry: 7b8a1c9 (HEAD@{1})<br>Author: Dr. Aditi Sharma &lt;aditi@failsafe.org&gt;<br>Message: <strong>OVERRIDE FAILED</strong></div>
        </div>
        <div style="margin-top: 12px; font-size: 11px; color: #64748b;">
          Enter the authentic commit message: <code>OVERRIDE FAILED</code>
        </div>
      </div>
    `
  },

  14: {
    id: 14,
    folderName: "14_TRAP",
    title: "Honeypot Trap Bypass",
    type: "trap",
    fileName: "DO_NOT_RUN.exe",
    passwordPrompt: "Enter Stage 14 Trap Bypass Command:",
    render: () => `
      <div style="background: #1a0505; border: 2px solid #ff3366; border-radius: 4px; padding: 20px; font-family: monospace; color: #ff3366;">
        <div style="font-size: 15px; font-weight: bold; border-bottom: 1px solid rgba(255,51,102,0.4); padding-bottom: 8px; margin-bottom: 14px;">
          ⚠️ SYSTEM EMERGENCY SHUTDOWN // HONEYPOT DETECTED
        </div>
        <p style="color: #fca5a5; font-size: 13px; line-height: 1.6; margin-bottom: 16px;">
          <strong>PSYCHOLOGICAL TRAP ADVISORY:</strong> This console invites operators to enter authorization credentials.
          Entering credentials here activates ADI's honeypot lockout (+5 minute penalty)!
        </p>
        <div style="background: rgba(255,51,102,0.1); border: 1px dashed #ff3366; padding: 12px; border-radius: 4px; text-align: center; font-size: 13px; color: #fff;">
          To disarm and bypass this trap safely, issue the command: <strong>BYPASS</strong>
        </div>
      </div>
    `
  },

  15: {
    id: 15,
    folderName: "15_FAILSAFE",
    title: "The Real Failsafe Code",
    type: "failsafe",
    fileName: "WIE_Core_Values.doc",
    passwordPrompt: "Enter the Master Failsafe Verification Key:",
    render: () => `
      <div class="doc-sheet" style="font-family: var(--font-hud); padding: 26px 30px; background: #ffffff; color: #0f172a; border-radius: 4px;">
        <h3 style="color: #0284c7; border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 16px;">
          DR. ADITI'S TRUE OFFLINE FAILSAFE PROTOCOL
        </h3>
        <p style="font-size: 14px; line-height: 1.8; color: #334155; margin-bottom: 18px;">
          "The system that asks you to prove yourself is the system controlling you.
          The real failsafe is not a button—it is encoded in our core foundational values."
        </p>

        <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 18px; border-radius: 4px; color: #166534; line-height: 2;">
          <strong>IEEE WIE FOUNDATIONAL CORE VALUES:</strong><br>
          • <strong>W</strong>isdom (6 letters)<br>
          • <strong>I</strong>ntegrity (9 letters)<br>
          • <strong>E</strong>mpowerment (11 letters)<br><br>
          <span style="color: #15803d; font-size: 13px;">
            "Count their individual letter lengths to forge the hardware override cipher."
          </span>
        </div>
      </div>
    `
  }
};
