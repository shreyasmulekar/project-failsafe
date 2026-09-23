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
        <div style="margin-top: 14px; background: rgba(0,255,102,0.06); border: 1px dashed #00ff66; padding: 10px; border-radius: 4px;">
          <div style="font-size: 12px; color: #00ff66; font-weight: bold;">
            🎯 DEDUCE THE 6-LETTER AUTHORIZATION COMMAND (LOGIN → VERIFY → ? → EXECUTE → LOCK)
          </div>
          <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">
            Enter the recovered verb into the Stage Decryption Prompt below.
          </div>
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    folderName: "02_MEMORY",
    title: "ADI's Memory Core",
    type: "terminal",
    fileName: "ADI_Memory.core",
    passwordPrompt: "Enter Stage 2 Chronological Code (123456):",
    render: () => `
      <div style="background: #02070e; border: 1px solid var(--neon-amber, #ffb800); border-radius: 4px; padding: 18px; font-family: monospace; color: #ffea9f;">
        <div style="border-bottom: 1px solid rgba(255,184,0,0.3); padding-bottom: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; font-weight: bold;">
          <span>ADI // MEMORY CORE [SECTOR 02]</span>
          <span style="color: #ff3366;">⚠️ MEMORY CORRUPTION DETECTED</span>
        </div>
        <p style="font-size: 13px; color: #cbd5e1; margin-bottom: 12px;">
          6 fragments recovered. Their original sequence has been lost.<br>
          ADI: <em>"I remember what happened. I just don't remember when. Restore my memories in the correct order."</em>
        </p>
        <div style="margin-top: 14px; background: rgba(255,184,0,0.08); border: 1px dashed #ffb800; padding: 10px; border-radius: 4px;">
          <div style="font-size: 12px; color: #ffd700; font-weight: bold;">
            🧠 CHRONOLOGY CHALLENGE: REORDER FRAGMENTS (4:17 PM TO 10:15 PM)
          </div>
          <div style="font-size: 11px; color: #cbd5e1; margin-top: 4px;">
            Extract the chronological numerical sequence (1-2-3-4-5-6) and submit below.
          </div>
        </div>
      </div>
    `

  },

  _OLD_2: {
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
        <div style="margin-top: 10px; background: rgba(2,132,199,0.1); border: 1px dashed #0284c7; padding: 10px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 12px; color: #38bdf8; font-weight: bold;">🎯 CORRUPTED EVENT ISOLATED: Row E (74% vs expected 25%)</span>
          <span style="font-size: 11px; color: #cbd5e1;">Passcode Key: <strong>SYSTEM SHUTDOWN</strong></span>
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

/**
 * ROUND 2: StratCom Decryption Arena
 * 9 Olympiad / Advanced Visual & Algorithmic Forensic Puzzles
 */
const ROUND2_PUZZLE_DATA = {
  1: {
    id: 1,
    round: 2,
    folderName: "R2_01_MATRIX",
    title: "Visual Matrix Box Transformation",
    type: "matrix",
    fileName: "Visual_Matrix.pdf",
    passwordPrompt: "Select Option (A, B, C, D) or Enter Symbol Name:",
    targetSelector: "#r2-matrix-options",
    ethanPointerHint: "Inspect the 3x3 matrix in the center panel. Notice how shapes stay consistent along rows (Row 3 = Circles), and quantities grow along columns. Look at the options below!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 01</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE MATRIX BOX TRANSFORMATION</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -20 PTS</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          Evaluate the 3x3 visual transformation matrix. Each cell contains progressive geometric symbols. Deduce the missing symbol in <strong>Row 3, Column 3</strong>:
        </p>

        <!-- 3x3 Matrix Grid -->
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; max-width:440px; margin:0 auto 20px auto; background:rgba(0,0,0,0.5); padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:8px;">
          <!-- Row 1 -->
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲ ▲</div>
          <!-- Row 2 -->
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■ ■</div>
          <!-- Row 3 -->
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">●</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">● ●</div>
          <div id="target-matrix-unknown" style="background:rgba(255,0,60,0.15); border:2px dashed var(--combat-red, #ff003c); padding:14px; text-align:center; font-size:20px; font-weight:bold; color:var(--combat-red, #ff003c); animation:pulse-strobe 1.5s infinite;">?</div>
        </div>

        <!-- Multiple Choice Options -->
        <div id="r2-matrix-options" style="background:rgba(0,240,255,0.04); border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:#00f0ff; font-weight:bold; margin-bottom:8px; letter-spacing:0.8px;">SELECT CANDIDATE TRANSFORMATION:</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <button type="button" onclick="selectRound2Option('A')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px; display:flex; justify-content:space-between; align-items:center;">
              <span><strong>OPTION A:</strong> [ ● ]</span>
            </button>
            <button type="button" onclick="selectRound2Option('B')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px; display:flex; justify-content:space-between; align-items:center;">
              <span><strong>OPTION B:</strong> [ ■ ■ ■ ]</span>
            </button>
            <button type="button" onclick="selectRound2Option('C')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px; display:flex; justify-content:space-between; align-items:center;">
              <span><strong>OPTION C:</strong> [ ● ● ● ]</span>
            </button>
            <button type="button" onclick="selectRound2Option('D')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px; display:flex; justify-content:space-between; align-items:center;">
              <span><strong>OPTION D:</strong> [ ▲ ▲ ▲ ]</span>
            </button>
          </div>
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    round: 2,
    folderName: "R2_02_CUBE",
    title: "Spatial Net Folding Box (3D Cube)",
    type: "cube",
    fileName: "Cube_Net_Terminal.pdf",
    passwordPrompt: "Enter Digit Opposite to Face 1:",
    targetSelector: "#r2-cube-net-container",
    ethanPointerHint: "Look at the vertical spine of the T-shaped cube net: boxes 1, 3, 5, 6. Remember the Olympiad rule: faces separated by exactly one box fold into opposite sides!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 02</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SPATIAL NET FOLDING BOX</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -15 PTS</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          To re-establish the hardware core, analyze the flattened 2D paper net of the 6-sided hardware cube containing digits 1 through 6:
        </p>

        <!-- T-Shaped Cube Net Diagram -->
        <div id="r2-cube-net-container" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:20px; display:flex; flex-direction:column; align-items:center; margin-bottom:16px;">
          <!-- Row 1: Box 1 -->
          <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.12);">1</div>
          <!-- Row 2: Box 2, 3, 4 -->
          <div style="display:flex;">
            <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">2</div>
            <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">3</div>
            <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">4</div>
          </div>
          <!-- Row 3: Box 5 -->
          <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">5</div>
          <!-- Row 4: Box 6 -->
          <div style="width:50px; height:50px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">6</div>
        </div>

        <div style="background:rgba(0,240,255,0.06); border-left:3px solid #00f0ff; padding:10px 14px; font-size:12px; color:#e2e8f0;">
          <strong>QUESTION:</strong> If this net is folded into a 3D cube, which number will be on the face <strong>opposite to face 1</strong>?
        </div>
      </div>
    `
  },

  3: {
    id: 3,
    round: 2,
    folderName: "R2_03_ROTATION",
    title: "Clockwise Rotation Boxes (Spatial 90°)",
    type: "rotation",
    fileName: "Rotation_Array.pdf",
    passwordPrompt: "Enter Missing Corner Location (e.g. BOTTOM LEFT or BL):",
    targetSelector: "#r2-rotation-sequence",
    ethanPointerHint: "Trace the white dot: Box 1 is Top-Left, Box 2 is Top-Right, Box 3 is Bottom-Right. It shifts 90 degrees clockwise each step. Where does it land next?",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 03</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE CLOCKWISE ROTATION BOXES</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          <em>"Trace the movement of the core node as it rotates through the terminal array."</em>
        </p>

        <!-- 4-Box Sequence -->
        <div id="r2-rotation-sequence" style="display:flex; gap:14px; justify-content:center; align-items:center; margin-bottom:20px; flex-wrap:wrap;">
          <!-- Box 1: TL -->
          <div style="text-align:center;">
            <div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 1</div>
            <div style="width:80px; height:80px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;">
              <div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; left:8px;"></div>
            </div>
          </div>
          <!-- Box 2: TR -->
          <div style="text-align:center;">
            <div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 2</div>
            <div style="width:80px; height:80px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;">
              <div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; right:8px;"></div>
            </div>
          </div>
          <!-- Box 3: BR -->
          <div style="text-align:center;">
            <div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 3</div>
            <div style="width:80px; height:80px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;">
              <div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; bottom:8px; right:8px;"></div>
            </div>
          </div>
          <!-- Box 4: ? -->
          <div style="text-align:center;">
            <div style="font-size:10px; color:var(--combat-red, #ff003c); font-weight:bold; margin-bottom:4px;">BOX 4 (MISSING)</div>
            <div style="width:80px; height:80px; border:2px dashed var(--combat-red, #ff003c); background:rgba(255,0,60,0.08); display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:bold; color:var(--combat-red, #ff003c); border-radius:4px;">
              ?
            </div>
          </div>
        </div>

        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">
          Enter the position of the core node in Box 4: <code>BOTTOM LEFT</code> (or <code>BL</code>).
        </div>
      </div>
    `
  },

  4: {
    id: 4,
    round: 2,
    folderName: "R2_04_WHITEOUT",
    title: "The Whiteout Signature (Steganography)",
    type: "whiteout",
    fileName: "Emergency_Log.doc",
    passwordPrompt: "Enter Discovered Clearance Key:",
    targetSelector: "#r2-whiteout-box",
    ethanPointerHint: "Some messages are not meant to be read; they are meant to be highlighted. Click the Forensic UV Light toggle button or highlight the blank box with your cursor!",
    render: () => `
      <div class="nexus-card" style="background:#ffffff; border-radius:8px; padding:24px; color:#0f172a; font-family:Arial, sans-serif; box-shadow:0 4px 20px rgba(0,0,0,0.3);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #cbd5e1; padding-bottom:10px; margin-bottom:16px;">
          <div>
            <span style="background:#0284c7; color:#fff; font-size:10px; font-weight:bold; padding:2px 8px; border-radius:3px;">ROUND 02 // PUZZLE 04</span>
            <strong style="margin-left:8px; font-size:14px; color:#0f172a;">EMERGENCY REPORT // DR. ADITI SHARMA</strong>
          </div>
          <button type="button" onclick="const p=document.getElementById('r2-secret-whiteout'); p.style.color='#0f172a'; p.style.background='#fef08a';" class="btn-action" style="font-size:11px; padding:4px 10px; background:#0284c7; color:#fff; border:none; border-radius:4px; cursor:pointer;">
            🔦 TOGGLE FORENSIC UV LIGHT
          </button>
        </div>

        <p style="font-size:13px; color:#334155; line-height:1.6; margin-bottom:14px;">
          The system kernel has been compromised. All standard protocols have been redirected.
          Do not trust visible displays.
        </p>

        <!-- White-on-White Text Box -->
        <div id="r2-whiteout-box" style="margin:20px 0; padding:16px; background:#ffffff; border:1px dashed #cbd5e1; border-radius:4px; text-align:center;">
          <p id="r2-secret-whiteout" style="color:#ffffff; background:#ffffff; font-family:monospace; font-size:15px; font-weight:bold; letter-spacing:2px; user-select:text; margin:0; transition:all 0.3s ease;">
            DECRYPTION KEY IS CLEARANCE_ALPHA
          </p>
        </div>

        <p style="font-size:11.5px; color:#64748b; font-style:italic;">
          💡 "Some messages are not meant to be read; they are meant to be highlighted." (Highlight text or click UV light).
        </p>
      </div>
    `
  },

  5: {
    id: 5,
    round: 2,
    folderName: "R2_05_ROT4",
    title: "The ROT-4 IEEE Shift Cipher",
    type: "cipher",
    fileName: "Encrypted_Beacon.txt",
    passwordPrompt: "Enter Decrypted Beacon Passcode:",
    targetSelector: "#r2-rot-cipher-card",
    ethanPointerHint: "Shift each letter backward by the count of letters in 'IEEE' (4 letters). E shifted back 4 is A, H shifted back 4 is D. Continue the shift!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 05</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ROT-4 IEEE SHIFT CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Dr. Aditi transmitted an intercepted beacon before losing terminal connection:
        </p>

        <div id="r2-rot-cipher-card" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:26px; font-weight:bold; letter-spacing:6px; color:#00f0ff;">
            EHMXMW13
          </div>
          <div style="font-size:11.5px; color:#cbd5e1; margin-top:8px;">
            CLUE: <em>"Shift every letter backward by the number of letters in the acronym 'IEEE' (4)."</em>
          </div>
        </div>

        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:4px; padding:10px 14px; font-size:11px; color:#94a3b8;">
          Example shift: <code>E (-4) &rarr; A</code> | <code>H (-4) &rarr; D</code> | <code>M (-4) &rarr; I</code> ...
        </div>
      </div>
    `
  },

  6: {
    id: 6,
    round: 2,
    folderName: "R2_06_POLYBIUS",
    title: "The Polybius Coordinate Trail",
    type: "grid",
    fileName: "Matrix_Coordinates.pdf",
    passwordPrompt: "Enter Decoded 6-Letter Word:",
    targetSelector: "#r2-polybius-grid",
    ethanPointerHint: "Use (Row, Column) order on the 5x5 grid below. For example, Row 5, Column 1 is 'V'. Row 1, Column 5 is 'E'. Follow the coordinate stream!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 06</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE POLYBIUS COORDINATE TRAIL</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Map each pair in the 5x5 Polybius grid using standard <strong>(Row, Column)</strong> coordinate order:
        </p>

        <!-- 5x5 Polybius Grid -->
        <div id="r2-polybius-grid" style="background:#02050b; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; max-width:260px; margin:0 auto 16px auto; font-family:monospace;">
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:14px;">
            <tr style="color:#00f0ff; font-weight:bold; border-bottom:1px solid rgba(0,240,255,0.3);"><th style="padding:4px;"></th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr>
            <tr><th style="color:#00f0ff; padding:4px;">1</th><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr>
            <tr><th style="color:#00f0ff; padding:4px;">2</th><td>F</td><td>G</td><td>H</td><td>I</td><td>K</td></tr>
            <tr><th style="color:#00f0ff; padding:4px;">3</th><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td></tr>
            <tr><th style="color:#00f0ff; padding:4px;">4</th><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td></tr>
            <tr><th style="color:#00f0ff; padding:4px;">5</th><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td></tr>
          </table>
        </div>

        <div style="background:rgba(0,240,255,0.06); border:1px dashed #00f0ff; border-radius:6px; padding:12px; text-align:center;">
          <span style="color:#94a3b8; font-size:11px; display:block; margin-bottom:4px;">COORDINATE STREAM:</span>
          <span style="font-size:18px; font-weight:bold; letter-spacing:4px; color:#38bdf8;">(5,1) (1,5) (1,3) (4,4) (3,4) (4,2)</span>
        </div>
      </div>
    `
  },

  7: {
    id: 7,
    round: 2,
    folderName: "R2_07_ATBASH",
    title: "The Atbash Cipher Mirror",
    type: "atbash",
    fileName: "Mirror_Log.txt",
    passwordPrompt: "Enter Mirrored Word:",
    targetSelector: "#r2-atbash-card",
    ethanPointerHint: "In the Atbash cipher, the alphabet is reversed: A becomes Z, B becomes Y, C becomes X. Mirror the letters in KILQVBG!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 07</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ATBASH CIPHER MIRROR</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          <em>"In times of crisis, Dr. Aditi mirrored her alphabet. Reverse the alphabet so A &harr; Z, B &harr; Y."</em>
        </p>

        <div id="r2-atbash-card" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:26px; font-weight:bold; letter-spacing:6px; color:#00f0ff;">
            KILQVBG
          </div>
          <div style="font-size:11.5px; color:#cbd5e1; margin-top:8px;">
            [ K &harr; P, I &harr; R, L &harr; O, Q &harr; J, V &harr; E, B &harr; Y, G &harr; T ]
          </div>
        </div>

        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">
          Enter the decoded project name: <code>PROJECT</code>
        </div>
      </div>
    `
  },

  8: {
    id: 8,
    round: 2,
    folderName: "R2_08_SEARCH",
    title: "Find-and-Replace Frequency Count",
    type: "search",
    fileName: "Mass_System_Log.txt",
    passwordPrompt: "Enter Computed Security Pin (Count × 100):",
    targetSelector: "#r2-log-search-tool",
    ethanPointerHint: "Use the built-in search tool below or Ctrl+F. Search for the word 'OVERRIDE', count how many times it appears (14 times), and multiply that count by 100!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 08</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">FIND-AND-REPLACE FREQUENCY COUNT</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:12px;">
          <em>"Count how many times the exact term 'OVERRIDE' appears in the mass log, then multiply that count by 100."</em>
        </p>

        <!-- Search Bar -->
        <div id="r2-log-search-tool" style="display:flex; gap:10px; margin-bottom:12px;">
          <input type="text" id="r2-log-search-input" placeholder="Search term in log (e.g. OVERRIDE)..."
            style="flex:1; padding:8px 12px; background:#02050b; border:1px solid rgba(0,240,255,0.3); color:#fff; font-family:monospace; font-size:12px; border-radius:4px; outline:none;">
          <button type="button" onclick="searchR2LogOccurrences()" class="btn-action" style="padding:8px 16px; font-size:11px;">
            🔍 COUNT MATCHES
          </button>
        </div>
        <div id="r2-log-search-result" style="font-size:12px; color:var(--tactical-green, #00ff66); margin-bottom:10px; min-height:18px;"></div>

        <!-- Scrollable Log -->
        <div id="r2-mass-log-box" style="height:150px; overflow-y:auto; background:#02050b; border:1px solid rgba(255,255,255,0.1); padding:10px 14px; font-size:11px; line-height:1.7; color:#94a3b8; border-radius:4px;">
          [00:01:14] SYSTEM_BOOT // Kernel parameters verified.<br>
          [00:02:18] MANUAL OVERRIDE initiated at sector 1.<br>
          [00:03:45] Telemetry check normal.<br>
          [00:05:12] EMERGENCY OVERRIDE requested by Dr. Sharma.<br>
          [00:07:01] Sensor cluster online.<br>
          [00:08:29] HARDWARE OVERRIDE authorized on switch 4.<br>
          [00:10:04] ADI neural heuristics checking anomaly.<br>
          [00:11:30] SECURITY OVERRIDE triggered at gate 2.<br>
          [00:13:22] Power bus within normal bounds.<br>
          [00:14:40] LOCAL OVERRIDE applied to cooling valves.<br>
          [00:16:15] Neural chatter suppressed.<br>
          [00:17:55] KERNEL OVERRIDE signaled by station 8.<br>
          [00:19:12] Backup database synchronizing.<br>
          [00:20:44] DIRECT OVERRIDE sent to memory controller.<br>
          [00:22:18] Warning: Unrecognized authentication pattern.<br>
          [00:23:59] REMOTE OVERRIDE executed by operator.<br>
          [00:25:30] Memory dump completed.<br>
          [00:27:08] SYSTEM OVERRIDE issued on terminal 3.<br>
          [00:28:44] Optical bus stable.<br>
          [00:30:19] ROOT OVERRIDE engaged on primary server.<br>
          [00:32:00] StratCom beacon active.<br>
          [00:33:45] MANUAL OVERRIDE repeated on fallback relay.<br>
          [00:35:12] Temperature stabilized.<br>
          [00:36:50] MASTER OVERRIDE granted by Dr. Aditi.<br>
          [00:38:22] Signal beacon verified.<br>
          [00:40:01] TERMINAL OVERRIDE logged at console.<br>
          [00:41:40] Integrity checksum valid.<br>
          [00:43:15] FINAL OVERRIDE locked into hardware registers.<br>
          [00:45:00] End of audit sequence.
        </div>
      </div>
    `
  },

  9: {
    id: 9,
    round: 2,
    folderName: "R2_09_WHEEL",
    title: "Cipher Wheel Layer Shift (Visual Alignment)",
    type: "wheel",
    fileName: "Wheel_Overlay.pdf",
    passwordPrompt: "Enter Uncovered 7-Letter Keyword:",
    targetSelector: "#r2-wheel-aligner",
    ethanPointerHint: "Drag the rotation slider or click 135° Clockwise. Aligning the inner wheel cutouts over the outer alphabet at 135 degrees covers the decoy letters and exposes the passcode!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 09 [FINAL]</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE CIPHER WHEEL LAYER SHIFT</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">FINAL CHAPTER</span>
        </div>

        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Two transparent cipher wheel layers have been retrieved. Align the inner wheel over the outer alphabet ring at <strong>135° clockwise</strong>:
        </p>

        <!-- Interactive Wheel Aligner -->
        <div id="r2-wheel-aligner" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:8px; padding:20px; text-align:center; margin-bottom:16px;">
          <div style="position:relative; width:180px; height:180px; margin:0 auto 16px auto; border-radius:50%; border:3px solid #00f0ff; display:flex; align-items:center; justify-content:center; background:radial-gradient(circle, #091322 0%, #030710 100%);">
            <!-- Outer Ring Letters -->
            <div style="position:absolute; inset:6px; border-radius:50%; border:1px dashed rgba(0,240,255,0.4); display:flex; align-items:center; justify-content:center; font-size:11px; color:#38bdf8; letter-spacing:2px;">
              A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
            </div>
            <!-- Inner Rotating Disk -->
            <div id="r2-inner-wheel" style="width:110px; height:110px; border-radius:50%; border:2px solid #00ff66; background:rgba(0,255,102,0.12); display:flex; align-items:center; justify-content:center; transform:rotate(0deg); transition:transform 0.4s ease; font-weight:bold; font-size:12px; color:#00ff66;">
              <span id="r2-wheel-exposed-text">0° (MISALIGNED)</span>
            </div>
          </div>

          <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
            <button type="button" onclick="setR2WheelAngle(0)" class="btn-action" style="font-size:10px; padding:4px 10px;">0°</button>
            <button type="button" onclick="setR2WheelAngle(45)" class="btn-action" style="font-size:10px; padding:4px 10px;">45°</button>
            <button type="button" onclick="setR2WheelAngle(90)" class="btn-action" style="font-size:10px; padding:4px 10px;">90°</button>
            <button type="button" onclick="setR2WheelAngle(135)" class="btn-action success" style="font-size:10px; padding:4px 12px; border-color:#00ff66; color:#00ff66; font-weight:bold;">135° (HINTED)</button>
            <button type="button" onclick="setR2WheelAngle(180)" class="btn-action" style="font-size:10px; padding:4px 10px;">180°</button>
            <button type="button" onclick="setR2WheelAngle(270)" class="btn-action" style="font-size:10px; padding:4px 10px;">270°</button>
          </div>
        </div>

        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">
          Align cutouts at 135 degrees to read the exposed letters: <code>ECLIPSE</code>
        </div>
      </div>
    `
  }
};

/**
 * Interactive helper functions for Round 2 puzzles
 */
function selectRound2Option(opt) {
  const input = document.getElementById("terminal-input") || document.getElementById("cli-command-input");
  if (input) {
    input.value = opt;
    input.focus();
  }
  if (typeof handleCommand === "function") {
    handleCommand(`decrypt ${opt}`);
  }
}

function searchR2LogOccurrences() {
  const input = document.getElementById("r2-log-search-input");
  const result = document.getElementById("r2-log-search-result");
  const logBox = document.getElementById("r2-mass-log-box");
  if (!input || !result || !logBox) return;

  const query = input.value.trim().toUpperCase();
  if (!query) {
    result.innerText = "Please enter a search term.";
    return;
  }

  const rawText = logBox.innerText.toUpperCase();
  const regex = new RegExp(`\\b${query}\\b`, "g");
  const matches = rawText.match(regex);
  const count = matches ? matches.length : 0;

  result.innerText = `Found ${count} occurrences of "${query}". Value: ${count} × 100 = ${count * 100}`;
}

function setR2WheelAngle(deg) {
  const wheel = document.getElementById("r2-inner-wheel");
  const text = document.getElementById("r2-wheel-exposed-text");
  if (!wheel || !text) return;

  wheel.style.transform = `rotate(${deg}deg)`;
  if (deg === 135) {
    text.innerText = "E-C-L-I-P-S-E";
    text.style.color = "#00ff66";
    text.style.textShadow = "0 0 10px #00ff66";
  } else {
    text.innerText = `${deg}° (BLURRED)`;
    text.style.color = "#ffb800";
    text.style.textShadow = "none";
  }
}

