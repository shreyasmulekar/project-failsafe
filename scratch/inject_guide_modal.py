# scratch/inject_guide_modal.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Header button injection
header_target = '<button id="btn-switch-r2"'
header_btn = """<button id="btn-open-puzzles-guide" class="btn-tactical" onclick="openModal('modal-puzzles-guide')" style="background:rgba(0,255,102,0.18); border-color:#00ff66; color:#00ff66; font-weight:900; font-size:11px; padding:6px 14px; letter-spacing:0.5px; box-shadow:0 0 15px rgba(0,255,102,0.35); cursor:pointer;" title="Complete Guide for every puzzle: Where to click and where to submit">
          🧭 ALL PUZZLES DIRECTORY: WHERE TO CLICK &amp; SUBMIT
        </button>
        """

if "btn-open-puzzles-guide" not in html and header_target in html:
    html = html.replace(header_target, header_btn + header_target, 1)
    print("Injected header button successfully!")

# 2. Main Directive Strip injection right above nexus-vault-section
vault_target = '<div class="nexus-vault-section">'
directive_strip = """<!-- Live Interactive Mission & Click Directive Banner -->
      <div id="participant-directive-strip" style="background:linear-gradient(90deg, rgba(0,240,255,0.15), rgba(0,255,102,0.15)); border:2px solid #00f0ff; border-radius:8px; padding:14px 20px; margin-bottom:16px; display:flex; align-items:center; justify-content:space-between; gap:16px; box-shadow:0 0 25px rgba(0,240,255,0.25); font-family:var(--font-mono, monospace);">
        <div style="display:flex; align-items:center; gap:14px;">
          <span style="font-size:24px;">👉</span>
          <div>
            <div style="font-size:11px; font-weight:900; color:#00f0ff; letter-spacing:1.5px; text-transform:uppercase;">
              TACTICAL PARTICIPANT DIRECTIVE // HOW TO PLAY &amp; WHERE TO CLICK
            </div>
            <div id="participant-current-stage-instruction" style="font-size:13.5px; color:#ffffff; font-weight:bold; margin-top:2px;">
              STEP 1: Look at the highlighted card below [<span style="color:#00ff66;" id="directive-active-card-name">STAGE 01: ISHAAN_Recovery.term</span>]. Click it to open the puzzle dossier!
            </div>
          </div>
        </div>
        <button type="button" onclick="openModal('modal-puzzles-guide')" style="background:#00ff66; color:#02060e; font-weight:900; font-size:11.5px; padding:9px 18px; border-radius:4px; border:none; cursor:pointer; white-space:nowrap; letter-spacing:0.5px; box-shadow:0 0 15px rgba(0,255,102,0.6);">
          🧭 VIEW ALL PUZZLES GUIDE &rarr;
        </button>
      </div>

      """

if "participant-directive-strip" not in html and vault_target in html:
    html = html.replace(vault_target, directive_strip + vault_target, 1)
    print("Injected directive strip successfully!")

# 3. Guide Modal injection
guide_modal_html = """
  <!-- ========================================================================= -->
  <!-- COMPREHENSIVE PARTICIPANT GUIDE: WHERE TO CLICK & SUBMIT FOR ALL PUZZLES -->
  <!-- ========================================================================= -->
  <div id="modal-puzzles-guide" class="mil-modal" style="display:none; position:fixed; inset:0; z-index:9995; background:rgba(2, 6, 14, 0.95); backdrop-filter:blur(14px); align-items:center; justify-content:center; padding:20px;">
    <div style="max-width:1050px; width:100%; max-height:90vh; background:#060a12; border:2px solid #00f0ff; border-radius:12px; box-shadow:0 0 50px rgba(0,240,255,0.4); display:flex; flex-direction:column; font-family:var(--font-mono, monospace); color:#f1f5f9; overflow:hidden;">
      
      <!-- Header -->
      <div style="background:rgba(0,240,255,0.12); border-bottom:1px solid #00f0ff; padding:16px 24px; display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:12px;">
          <span style="font-size:24px;">🧭</span>
          <div>
            <div style="font-size:16px; font-weight:900; color:#00f0ff; letter-spacing:1px;">
              PARTICIPANT TACTICAL DIRECTORY // WHERE TO CLICK &amp; WHERE TO SUBMIT
            </div>
            <div style="font-size:11.5px; color:#94a3b8;">
              Comprehensive instructions for all 16 Forensic Stages (Round 1) and 15 Cryptographic Puzzles (Round 2)
            </div>
          </div>
        </div>
        <button type="button" onclick="closeModal('modal-puzzles-guide')" style="background:none; border:1px solid #ff003c; color:#ff003c; font-size:14px; font-weight:bold; border-radius:4px; padding:4px 12px; cursor:pointer;">✕ CLOSE</button>
      </div>

      <!-- Navigation Tabs -->
      <div style="display:flex; background:#0b1322; border-bottom:1px solid #1e293b; padding:10px 24px; gap:12px;">
        <button type="button" id="tab-guide-r1" onclick="switchGuideTab('r1')" style="background:#00f0ff; color:#02060e; font-weight:900; font-size:12px; padding:8px 18px; border-radius:4px; border:none; cursor:pointer; letter-spacing:0.5px;">
          ROUND 1: ALL 16 FORENSIC STAGES
        </button>
        <button type="button" id="tab-guide-r2" onclick="switchGuideTab('r2')" style="background:rgba(255,255,255,0.06); color:#cbd5e1; font-weight:bold; font-size:12px; padding:8px 18px; border-radius:4px; border:1px solid #334155; cursor:pointer; letter-spacing:0.5px;">
          ROUND 2: ALL 15 CRYPTOGRAPHIC PUZZLES (NO CLUES)
        </button>
      </div>

      <!-- Scrollable Content Area -->
      <div style="flex:1; overflow-y:auto; padding:20px 24px;">
        
        <!-- ROUND 1 GUIDE CONTAINER -->
        <div id="guide-container-r1" style="display:flex; flex-direction:column; gap:16px;">
          
          <div style="background:rgba(0,240,255,0.05); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:12px 16px; font-size:12.5px; color:#a7f3d0;">
            💡 <strong>HOW ROUND 1 WORKS:</strong> Stages must be solved sequentially from Stage 01 to Stage 16. In the left panel, click on the highlighted card to open its dossier. Solve the evidence, then submit your answer directly inside the popup window or via the Quick Decrypt dock!
          </div>

          <!-- STAGE 01 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 01: ISHAAN_Recovery.term (Boot Lifecycle)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-recovery');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click on Card 01 [ISHAAN_Recovery.term] on the left. Inside the popup terminal, click the command prompt line. Review the 5 boot commands to find the missing operational verb between VERIFY and EXECUTE.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Type <code>VERIFY_INTEGRITY</code> into the terminal prompt (or enter into the Quick Decrypt bar) and press Enter.
            </div>
          </div>

          <!-- STAGE 02 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00ff66; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00ff66; font-weight:900; font-size:13px;">STAGE 02: ISHAAN_Memory.core (Chronology Timeline)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-memory');" style="background:#00ff66; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 02 [ISHAAN_Memory.core]. Click the glowing <strong>[▲ UP]</strong> and <strong>[▼ DN]</strong> arrow buttons on each card to arrange timestamps chronologically (4:17 PM ➔ 6:45 PM ➔ 8:10 PM ➔ 9:32 PM ➔ 10:03 PM ➔ 10:15 PM).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT (THE BLOCK):</strong> After arranging the timeline in order, a large green glowing block <strong>[✅ CLICK THIS BLOCK TO RESTORE MEMORY CORE]</strong> will appear below the cards. <strong>CLICK ON THAT BLOCK</strong> to immediately submit and advance to Stage 03!
            </div>
          </div>

          <!-- STAGE 03 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 03: Aditi_Memo.doc (Acrostic Steganography)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-acrostic');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 03 [Aditi_Memo.doc]. Read Dr. Aditi's emergency memo text. Look at the very first letter of each sentence: (<strong>S</strong>ystem..., <strong>I</strong>SHAAN..., <strong>F</strong>ailsafe..., <strong>E</strong>xit...) &rarr; S-A-F-E.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>SAFE</code> into the <strong>[TRANSMIT DECRYPT KEY]</strong> box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 04 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 04: Incident_Logs.doc (Temporal Calendar Anomaly)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-incident-logs');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 04 [Incident_Logs.doc]. Audit the listed 2025 dates to locate the invalid non-leap date (29/02/2025).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the corrected date <code>28/02/2025</code> into the <strong>[TRANSMIT DECRYPT KEY]</strong> box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 05 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 05: Clearance_Code.txt (A1Z26 Alphabet Code)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-clearance');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 05 [Clearance_Code.txt]. Convert the numerical offsets (16-15-12-1-18-9-19) using 1=A, 2=B... to reveal POLARIS.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>POLARIS</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 06 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 06: System_Diagnostics.doc (Resolved Comments Metadata)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-comments');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 06 [System_Diagnostics.doc]. Click the <strong>[View Resolved Comments]</strong> button in the top right to expose Dr. Aditi's hidden note containing <code>MARGIN_KEY</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>MARGIN_KEY</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 07 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 07: AUTHENTIC_LOG.doc (Typographic Parity)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-font');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 07 [AUTHENTIC_LOG.doc]. Inspect the font family specified in Dr. Aditi's style guide (Arial sans-serif vs counterfeit Times New Roman serif).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>ARIAL</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 08 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 08: audio_log_07.mp3 (CW Morse Audio Spectrogram)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-spectro');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 08 [audio_log_07.mp3]. Click <strong>[▶ PLAY BEACON A (WHITE)]</strong> to listen to the Morse beeps, or read the dots/dashes: <code>.-- .... .. - .</code> &rarr; WHITE.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>WHITE</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 09 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 09: VERSION_SCRUB (Git Reflog Rollback)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-version-hist');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 09 [VERSION_SCRUB]. Click on the <strong>[Previous Revision (20:18Z by Dr. Aditi)]</strong> tab to view Dr. Aditi's original commit message containing <code>OVERRIDE_FAILED</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>OVERRIDE_FAILED</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 10 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #ff003c; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#ff003c; font-weight:900; font-size:13px;">STAGE 10: DO_NOT_RUN.exe (Honeypot Trap Disarm)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-honeypot');" style="background:#ff003c; color:#fff; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 10 [DO_NOT_RUN.exe]. <strong>DO NOT CLICK</strong> the red execution trigger (it triggers a proctor lockout!). Read the quarantine notes to find the bypass command.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>BYPASS</code> into the in-modal input box (or Quick Decrypt bar) and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 11 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 11: WIE_Core_Values.doc (Master Foundation Formula)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-failsafe');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 11 [WIE_Core_Values.doc]. Count the letter lengths of IEEE WIE's founding pillars: <strong>Wisdom</strong> (6 letters), <strong>Integrity</strong> (9 letters), and <strong>Empowerment</strong> (11 letters).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>6-9-11</code> into the in-modal input box and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 12 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 12: Emergency_Log.doc (The Whiteout Signature)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-whiteout');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 12 [Emergency_Log.doc]. Click and drag your cursor over the white document area (or click the <strong>[TOGGLE UV FILTER]</strong> button) to highlight the white-on-white text revealing <code>NEVERMORE</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>NEVERMORE</code> into the in-modal input box and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <!-- STAGE 13 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 13: Encrypted_Beacon.txt (ROT-4 Dynamic Shift)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-rot4');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 13 [Encrypted_Beacon.txt]. Shift each letter of ciphertext <code>EHMXMW13</code> backward by 4 letters (I-E-E-E = 4) to reveal <code>ADITIS09</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>ADITIS09</code> into the in-modal input box and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <!-- STAGE 14 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 14: Mirror_Log.txt (Atbash Cipher Mirror)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-atbash');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 14 [Mirror_Log.txt]. Use the Atbash substitution table (A&harr;Z, B&harr;Y, C&harr;X...) to decode <code>KILQVBG</code> &rarr; <code>PROJECT</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>PROJECT</code> into the in-modal input box and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <!-- STAGE 15 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 15: Matrix_Coordinates.pdf (Polybius 5x5 Grid)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-polybius');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 15 [Matrix_Coordinates.pdf]. Map coordinate pairs (Row, Col) in the 5x5 Polybius grid: (5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R &rarr; <code>VECTOR</code>.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>VECTOR</code> into the in-modal input box and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <!-- STAGE 16 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 16: Mass_System_Log.txt (Frequency Override Audit)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-frequency');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 16 [Mass_System_Log.txt]. Search through the log to count how many times the exact term 'OVERRIDE' appears (10 times) &times; 100 = 1000.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter <code>1000</code> (or <code>CIPHER</code>) into the in-modal input box and click <strong>[TRANSMIT &rarr;]</strong> to trigger TARA's final liberation!
            </div>
          </div>

        </div>

        <!-- ROUND 2 GUIDE CONTAINER -->
        <div id="guide-container-r2" style="display:none; flex-direction:column; gap:16px;">
          
          <div style="background:rgba(255,0,60,0.1); border:1px solid #ff003c; border-radius:6px; padding:12px 16px; font-size:12.5px; color:#fca5a5;">
            🔒 <strong>ROUND 2 STRICT RULE:</strong> Clues and tactical lifelines are <strong>COMPLETELY DISABLED</strong> in Round 2! Teams must deduce passcodes using pure cryptography and forensic analysis.
          </div>

          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:12px 16px; font-size:12.5px; color:#e2e8f0;">
            <strong style="color:#00f0ff;">👉 HOW TO NAVIGATE ROUND 2 ARENA:</strong><br>
            1. At the top of the Arena, click on any puzzle pill (<strong>PUZZLE 01</strong> to <strong>PUZZLE 15</strong>) to view its challenge viewport.<br>
            2. Read the puzzle dossier displayed in the center viewport.<br>
            3. <strong style="color:#00ff66;">WHERE TO SUBMIT:</strong> Enter your decrypted passcode into the highlighted <strong>[PASSCODE TRANSMISSION]</strong> input field directly below the puzzle and click <strong>[⚡ TRANSMIT CIPHER KEY &rarr;]</strong>!
          </div>

          <!-- R2 PUZZLE SUMMARY TABLE -->
          <div style="display:flex; flex-direction:column; gap:10px;">
            
            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 01: Matrix Box Transformation</span> &mdash; Inspect row shapes and column counts. Solution format: Letter (e.g. <code>C</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 02: Reverse Stream Mirror</span> &mdash; Read the reversed log stream backward. Solution format: Word (e.g. <code>REFLECT</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 03: Vigenère Cipher Autokey</span> &mdash; Decrypt ciphertext with key 'WIE'. Solution format: Word (e.g. <code>DEFENSE</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 04: Baconian Font Weights</span> &mdash; Map bold vs regular letters to binary A/B. Solution format: Word (e.g. <code>CIPHER</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 05: Hex Stream Translation</span> &mdash; Convert hexadecimal byte pairs to ASCII characters. Solution format: Word (e.g. <code>ROOT</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 06: Rail Fence Transposition</span> &mdash; Read zigzag letters across 2 rails. Solution format: Word (e.g. <code>BREACH</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 07: Affine Mathematical Cipher</span> &mdash; Compute mathematical modular decryption. Solution format: Word (e.g. <code>SECURITY</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 08: Columnar Transposition</span> &mdash; Reorder columns using key word order. Solution format: Word (e.g. <code>FIREWALL</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 09: Binary ASCII Stream</span> &mdash; Group 8-bit binary bytes to characters. Solution format: Word (e.g. <code>NETWORK</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 10: Playfair Bigram Cipher</span> &mdash; Decrypt digraph pairs in 5x5 key matrix. Solution format: Word (e.g. <code>LABORATORY</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 11: Polybius Grid Lookup</span> &mdash; Map coordinates (Row, Col). Solution format: Word (e.g. <code>SENTINEL</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 12: Frequency Substitution</span> &mdash; Deduce single-letter substitution. Solution format: Word (e.g. <code>AUTHENTIC</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 13: Beaufort Cipher</span> &mdash; Reverse Vigenère table calculation. Solution format: Word (e.g. <code>INTEGRITY</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #334155; padding:12px 16px; border-radius:6px;">
              <span style="color:#00f0ff; font-weight:bold;">PUZZLE 14: Tap Code Coordinates</span> &mdash; Count dot-pairs on 5x5 grid. Solution format: Word (e.g. <code>REVOLUTION</code>).
            </div>

            <div style="background:#0f172a; border:1px solid #ff003c; padding:12px 16px; border-radius:6px; box-shadow:0 0 15px rgba(255,0,60,0.3);">
              <span style="color:#ff003c; font-weight:bold;">PUZZLE 15: MASTER RED QUESTION (THE ECLIPSE PROTOCOL)</span> &mdash; Decrypt the dual-key enigma cipher. Solution: <code>ECLIPSE</code>.
            </div>

          </div>

        </div>

      </div>

      <!-- Footer -->
      <div style="background:#0b1322; border-top:1px solid #1e293b; padding:12px 24px; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-size:11.5px; color:#94a3b8;">
          PROJECT FAILSAFE 2090 // IEEE WIE FORENSIC ESCAPE ROOM
        </span>
        <button type="button" onclick="closeModal('modal-puzzles-guide')" style="background:#00f0ff; color:#02060e; font-weight:bold; font-size:12px; padding:6px 20px; border-radius:4px; border:none; cursor:pointer;">
          DISMISS GUIDE
        </button>
      </div>

    </div>
  </div>

  <script>
    function switchGuideTab(tab) {
      const r1Cont = document.getElementById('guide-container-r1');
      const r2Cont = document.getElementById('guide-container-r2');
      const t1 = document.getElementById('tab-guide-r1');
      const t2 = document.getElementById('tab-guide-r2');
      if (tab === 'r1') {
        if (r1Cont) r1Cont.style.display = 'flex';
        if (r2Cont) r2Cont.style.display = 'none';
        if (t1) { t1.style.background = '#00f0ff'; t1.style.color = '#02060e'; t1.style.border = 'none'; }
        if (t2) { t2.style.background = 'rgba(255,255,255,0.06)'; t2.style.color = '#cbd5e1'; t2.style.border = '1px solid #334155'; }
      } else {
        if (r1Cont) r1Cont.style.display = 'none';
        if (r2Cont) r2Cont.style.display = 'flex';
        if (t2) { t2.style.background = '#ff003c'; t2.style.color = '#ffffff'; t2.style.border = 'none'; }
        if (t1) { t1.style.background = 'rgba(255,255,255,0.06)'; t1.style.color = '#cbd5e1'; t1.style.border = '1px solid #334155'; }
      }
    }
  </script>
"""

modal_break_target = 'id="modal-round1-break"'
if "modal-puzzles-guide" not in html and modal_break_target in html:
    # insert before the container div of modal-round1-break
    pos = html.find(modal_break_target)
    # find '<div' preceding this
    div_start = html.rfind('<div', 0, pos)
    html = html[:div_start] + guide_modal_html + "\n  " + html[div_start:]
    print("Injected guide modal successfully!")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated aditi_os_widget.html successfully!")
