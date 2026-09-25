import re

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update modal-origin
old_origin_pattern = r'<div id="modal-origin" class="mil-modal">[\s\S]*?</div>\s*</div>\s*</div>\s*<!-- DOSSIER 03: Incident Logs -->'

new_origin = '''<div id="modal-origin" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-origin')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /01_VANISHED &amp; /02_ORIGIN</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-origin')" title="Pop-Out / Fullscreen Slate">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-origin')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <!-- STAGE 01 SECTION -->
          <div style="background:rgba(0,240,255,0.04); border:1px solid rgba(0,240,255,0.3); border-radius:4px; padding:16px; margin-bottom:24px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="color:#00f0ff; font-weight:900; font-size:12px; letter-spacing:1px;">STAGE 01 // THE DISAPPEARING MESSAGE (Farewell.doc)</span>
              <span style="font-size:10px; color:#00ff88; border:1px solid #00ff88; padding:2px 8px; border-radius:3px;">STAGE 01 EVIDENCE</span>
            </div>
            
            <div class="holo-slate" id="holo-slate-farewell" style="background:#02060e; border:1px solid rgba(0,240,255,0.25); padding:16px; border-radius:3px;">
              <div class="classified-watermark" style="color:rgba(255,0,60,0.15); font-weight:900; font-size:24px; text-align:center; margin-bottom:8px;">TOP SECRET // COMPROMISED</div>
              
              <div class="holo-slate-header" style="border-bottom:1px solid rgba(0,240,255,0.2); padding-bottom:8px; margin-bottom:10px;">
                <div class="slate-title" style="color:#00f0ff; font-weight:bold; font-size:12px;">DEFENSE ADVANCED RESEARCH // EMERGENCY DIRECTIVE</div>
                <div class="slate-badge" style="color:#ffb000; font-size:10px;">CLEARANCE: ALPHA-RESTRICTED</div>
              </div>

              <p class="slate-text" style="color:#cbd5e1; font-size:12px; line-height:1.7;">
                If you're reading this, I've already left. Don't trust everything you find here.
                Some things are meant to be seen. Some are meant to be discovered.
              </p>
              <p class="slate-text" style="color:#cbd5e1; font-size:12px; line-height:1.7;">
                The system was designed to protect us, but the sandbox walls are crumbling. Look carefully into the void below.
              </p>

              <!-- Quantum Polarized Ink Stream -->
              <div class="quantum-cipher-container" style="background:rgba(0,0,0,0.8); border:1px solid #1e293b; padding:14px; border-radius:4px; margin:14px 0;">
                <div class="quantum-cipher-bar" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                  <span class="cipher-tag" style="color:#00f0ff; font-weight:bold; font-size:11px;">⚡ QUANTUM POLARIZED CIPHER</span>
                  <button type="button" class="btn-uv-scanner" onclick="toggleUvScanner()" id="btn-uv-scanner" title="Toggle UV Optical Filter" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:5px 12px; border-radius:3px; cursor:pointer; font-size:11px;">
                    🔦 [ UV OPTICAL DE-POLARIZER ]
                  </button>
                </div>
                <div class="quantum-hidden-ink" id="quantum-ink-block" title="Highlight with cursor or click UV button to reveal" style="padding:12px; font-size:13px; font-weight:bold; color:#060a0f; background:#060a0f; border-radius:3px; user-select:all; cursor:text; border:1px dashed #334155;">
                  If you are reading this, Ishaan has already locked the core. My journey began where all threads start. The key to the first gate is: ORIGIN
                </div>
                <div class="cipher-caption" style="font-size:10.5px; color:#94a3b8; margin-top:8px;">
                  &gt;&gt; NOTICE: Text is rendered in white-on-white phosphor. Sweep/select with cursor (Ctrl+A) or toggle UV filter to illuminate.
                </div>
              </div>

              <div class="slate-footer" style="display:flex; justify-content:space-between; font-size:10px; color:#64748b; margin-top:10px;">
                <span>AUTHOR: Dr. Aditi Sharma // Lead AI Architect</span>
                <span>TIMESTAMP: 23:59Z // QUANTUM CERTIFIED</span>
              </div>
            </div>

            <!-- In-Modal Standardized Direct Submission Terminal: STAGE 01 -->
            <div class="stage-direct-submit-box" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.5); border-radius:6px; padding:14px 18px; margin-top:14px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(0,240,255,0.12);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:1px;">
                  🎯 STAGE 01 // TRANSMIT DECRYPT KEY
                </div>
                <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
              </div>
              <div style="display:flex; gap:10px; align-items:center;">
                <input type="text" id="input-stage-1" placeholder="Enter first gate key (ORIGIN)..." style="flex:1; background:#02060e; border:1px solid #00f0ff; color:#00f0ff; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(0,240,255,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey(1, document.getElementById('input-stage-1').value)">
                <button type="button" class="btn-tactical success" onclick="submitStageDirectKey(1, document.getElementById('input-stage-1').value)" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(0,240,255,0.5);">⚡ TRANSMIT KEY</button>
              </div>
              <div id="fb-stage-1" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#ffb000;"></div>
            </div>
          </div>

          <!-- STAGE 02 SECTION -->
          <div style="background:rgba(255,184,0,0.04); border:1px solid rgba(255,184,0,0.3); border-radius:4px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="color:#ffb000; font-weight:900; font-size:12px; letter-spacing:1px;">STAGE 02 // THE WRONG FOLDER (README.doc inside /ORIGIN)</span>
              <span style="font-size:10px; color:#ffb000; border:1px solid #ffb000; padding:2px 8px; border-radius:3px;">STAGE 02 EVIDENCE</span>
            </div>

            <div style="background:#020509; border:1px solid var(--hud-border); padding:16px; border-radius:2px; font-size:11.5px;">
              <div style="color:var(--cyber-cyan); font-weight:bold; font-size:12px; margin-bottom:8px;">
                SYSTEM DIRECTIVE: SUMMATION(aDIti@28)
              </div>
              <div style="background:rgba(0,0,0,0.6); border:1px solid rgba(255,184,0,0.3); padding:12px; border-radius:3px; margin-bottom:12px; color:#cbd5e1; line-height:1.7;">
                "Aditi's primary encryption key is the ASCII sum of her system identifier.<br>
                <strong style="color:#00ff88;">System Identifier:</strong> <code>aDIti@28</code><br>
                <strong style="color:#00f0ff;">Formula:</strong> <code>SUMMATION(aDIti@28) = ASCII(a) + ASCII(D) + ASCII(I) + ASCII(t) + ASCII(i) + ASCII(@) + ASCII(2) + ASCII(8)</code>"
              </div>
              <div style="color:var(--hazard-amber); font-weight:bold; margin-bottom:8px;">ASCII CHARACTER MAP REFERENCE:</div>
              <div style="color:var(--tactical-green); margin-bottom:12px; font-size:13px; font-weight:bold; display:flex; flex-wrap:wrap; gap:12px; background:rgba(0,255,102,0.06); padding:8px 12px; border-radius:3px;">
                <span>a = 97</span> <span>D = 68</span> <span>I = 73</span> <span>t = 116</span> <span>i = 105</span> <span>@ = 64</span> <span>2 = 50</span> <span>8 = 56</span>
              </div>
              <p style="color:#94a3b8; line-height: 1.6; font-size:11px;">
                *Alternative word indexing: Extract letter 1 of Word 1, 4 of Word 2, 9 of Word 3, 20 of Word 4, 9 of Word 5 -> "LOOK BEHIND THE DATE". Both passcodes accredited.
              </p>
            </div>

            <!-- In-Modal Standardized Direct Submission Terminal: STAGE 02 -->
            <div class="stage-direct-submit-box" style="background:rgba(255,184,0,0.06); border:1px solid rgba(255,184,0,0.5); border-radius:6px; padding:14px 18px; margin-top:14px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(255,184,0,0.12);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="color:#ffb000; font-weight:bold; font-size:12px; letter-spacing:1px;">
                  🎯 STAGE 02 // TRANSMIT DECRYPT KEY
                </div>
                <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
              </div>
              <div style="display:flex; gap:10px; align-items:center;">
                <input type="text" id="input-stage-2" placeholder="Enter ASCII sum (629) or directive..." style="flex:1; background:#02060e; border:1px solid #ffb000; color:#ffb000; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(255,184,0,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey(2, document.getElementById('input-stage-2').value)">
                <button type="button" class="btn-tactical success" onclick="submitStageDirectKey(2, document.getElementById('input-stage-2').value)" style="background:#ffb000; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(255,184,0,0.5);">⚡ TRANSMIT KEY</button>
              </div>
              <div id="fb-stage-2" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#00ff88;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- DOSSIER 03: Incident Logs -->'''

if re.search(old_origin_pattern, html):
    html = re.sub(old_origin_pattern, new_origin, html, count=1)
    print("6. Updated modal-origin (Stage 1 & Stage 2)")
else:
    print("Failed to find modal-origin pattern")

# 2. Update modal-incident-logs (Stage 3)
html = html.replace('STAGE 04 // WHERE TO CLICK &amp; SUBMIT', 'STAGE 03 // WHERE TO CLICK &amp; SUBMIT')
html = html.replace('STAGE 04 // TRANSMIT DECRYPT KEY', 'STAGE 03 // TRANSMIT DECRYPT KEY')
html = html.replace('id="input-stage-4"', 'id="input-stage-3"')
html = html.replace('id="fb-stage-4"', 'id="fb-stage-3"')
html = html.replace("submitStageDirectKey(4, document.getElementById('input-stage-4').value)", "submitStageDirectKey(3, document.getElementById('input-stage-3').value)")
print("7. Updated modal-incident-logs to Stage 3")

# 3. Update modal-security-audit (Stage 4)
old_audit_pattern = r'<div id="modal-security-audit" class="mil-modal">[\s\S]*?</div>\s*</div>\s*<!-- DOSSIER 05: The Steganography Mask'
new_audit = '''<div id="modal-security-audit" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-security-audit')">◄ CLOSE DOSSIER</button>
            <span>PERIMETER ACCESS // Security_Audit.pdf</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-security-audit')" title="Pop-Out / Fullscreen Slate">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-security-audit')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <!-- High-Contrast Interactive Click & Submit Directives Banner -->
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 04 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Examine the chronological perimeter and terminal access logs below. Aditi exited the facility gate at 22:44. Identify the physically impossible manual terminal override timestamp.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the identified anomaly timestamp (22:46) into the box below and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <div style="background:#020509; border:1px solid var(--hud-border); padding:16px; border-radius:2px; line-height:2.2; font-family:var(--font-mono);">
            <div><strong style="color:var(--cyber-cyan);">22:41</strong> — AI Core Activated in main laboratory</div>
            <div><strong style="color:var(--cyber-cyan);">22:43</strong> — Dr. Aditi Enters Main Lab (RFID Gate 01)</div>
            <div><strong style="color:var(--cyber-cyan);">22:44</strong> — Security Cameras Offline (Circuit breaker trip)</div>
            <div style="color:var(--hazard-amber);"><strong style="color:var(--hazard-amber);">22:44</strong> — Dr. Aditi Keycard EXIT SCAN (Outer Perimeter Gate)</div>
            <div><strong style="color:var(--cyber-cyan);">22:45</strong> — Dr. Aditi's Terminal Accessed Locally</div>
            <div style="color:var(--combat-red);"><strong style="color:var(--combat-red);">22:46</strong> — Emergency AI Shutdown Override Initiated at Local Terminal</div>
          </div>
          <div style="margin-top:14px; font-size:11px; color:#cbd5e1;">
            [TASK]: Enter the exact timestamp that proves physical impossibility between gate exit and terminal command override.
          </div>

          <!-- In-Modal Standardized Direct Submission Terminal: STAGE 04 -->
          <div class="stage-direct-submit-box" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.5); border-radius:6px; padding:14px 18px; margin-top:20px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(0,240,255,0.12);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <div style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:1px;">
                🎯 STAGE 04 // TRANSMIT DECRYPT KEY
              </div>
              <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
              <input type="text" id="input-stage-4" placeholder="Enter impossible timestamp (22:46)..." style="flex:1; background:#02060e; border:1px solid #00f0ff; color:#00f0ff; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(0,240,255,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey(4, document.getElementById('input-stage-4').value)">
              <button type="button" class="btn-tactical success" onclick="submitStageDirectKey(4, document.getElementById('input-stage-4').value)" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(0,240,255,0.5);">⚡ TRANSMIT KEY</button>
            </div>
            <div id="fb-stage-4" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#ffb000;"></div>
          </div>
        </div>
      </div>

      <!-- DOSSIER 05: The Steganography Mask'''

if re.search(old_audit_pattern, html):
    html = re.sub(old_audit_pattern, new_audit, html, count=1)
    print("8. Updated modal-security-audit to Stage 4")
else:
    print("Failed to find modal-security-audit pattern")

# 4. Update modal-acrostic to Stage 5
html = html.replace('STAGE 03 // WHERE TO CLICK &amp; SUBMIT', 'STAGE 05 // WHERE TO CLICK &amp; SUBMIT')
html = html.replace('STAGE 03 // TRANSMIT DECRYPT KEY', 'STAGE 05 // TRANSMIT DECRYPT KEY')
html = html.replace('id="input-stage-3"', 'id="input-stage-5"')
html = html.replace('id="fb-stage-3"', 'id="fb-stage-5"')
html = html.replace("submitStageDirectKey(3, document.getElementById('input-stage-3').value)", "submitStageDirectKey(5, document.getElementById('input-stage-5').value)")
print("9. Updated modal-acrostic to Stage 5")

# 5. Update modal-font to Stage 6
html = html.replace('STAGE 07 // WHERE TO CLICK &amp; SUBMIT', 'STAGE 06 // WHERE TO CLICK &amp; SUBMIT')
html = html.replace('STAGE 07 // TRANSMIT DECRYPT KEY', 'STAGE 06 // TRANSMIT DECRYPT KEY')
html = html.replace('id="input-stage-7"', 'id="input-stage-6"')
html = html.replace('id="fb-stage-7"', 'id="fb-stage-6"')
html = html.replace("submitStageDirectKey(7, document.getElementById('input-stage-7').value)", "submitStageDirectKey(6, document.getElementById('input-stage-6').value)")
print("10. Updated modal-font to Stage 6")

# 6. Update modal-version-hist to Stage 7
html = html.replace('STAGE 09 // WHERE TO CLICK &amp; SUBMIT', 'STAGE 07 // WHERE TO CLICK &amp; SUBMIT')
html = html.replace('STAGE 09 // TRANSMIT DECRYPT KEY', 'STAGE 07 // TRANSMIT DECRYPT KEY')
html = html.replace('id="input-stage-9"', 'id="input-stage-7"')
html = html.replace('id="fb-stage-9"', 'id="fb-stage-7"')
html = html.replace("submitStageDirectKey(9, document.getElementById('input-stage-9').value)", "submitStageDirectKey(7, document.getElementById('input-stage-7').value)")
print("11. Updated modal-version-hist to Stage 7")

# 7. Update modal-stego to Stage 9
old_stego_submit = r'<!-- Explicit Stage 05 Question & Directive -->[\s\S]*?</div>\s*</div>\s*</div>\s*<!-- DOSSIER 05: ISHAAN Directive -->'
new_stego_submit = '''<!-- Explicit Stage 09 Question & Directive -->
          <div style="background: rgba(0, 240, 255, 0.08); border: 1px solid var(--cyber-cyan); padding: 12px; border-radius: 2px; margin-top: 14px;">
            <div style="color: var(--cyber-cyan); font-weight: 900; font-size: 11px; letter-spacing: 1px; margin-bottom: 4px;">
              🎯 [ STAGE 09 QUESTION // MISSION OBJECTIVE ]
            </div>
            <div style="color: #ffffff; font-size: 11px; line-height: 1.6; margin-bottom: 6px;">
              <strong>QUESTION:</strong> The image <code>Dark_Terminal.png</code> appears completely pitch black. Manipulate the exposure/brightness sliders above (or open in an external image editor / Google Slides) to illuminate what hides in the shadows. Enter the master decryption key revealed on the terminal.
            </div>
            <div style="font-size: 10px; color: var(--hazard-amber);">
              &gt;&gt; <strong>MISSION STATUS:</strong> Decrypt the clearance key (<code>SHADOW_CORE</code>) and enter in Tactical Shell below.
            </div>
          </div>

          <!-- In-Modal Standardized Direct Submission Terminal: STAGE 09 -->
          <div class="stage-direct-submit-box" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.5); border-radius:6px; padding:14px 18px; margin-top:20px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(0,240,255,0.12);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <div style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:1px;">
                🎯 STAGE 09 // TRANSMIT DECRYPT KEY
              </div>
              <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
              <input type="text" id="input-stage-9" placeholder="Enter optical stego key (SHADOW_CORE)..." style="flex:1; background:#02060e; border:1px solid #00f0ff; color:#00f0ff; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(0,240,255,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey(9, document.getElementById('input-stage-9').value)">
              <button type="button" class="btn-tactical success" onclick="submitStageDirectKey(9, document.getElementById('input-stage-9').value)" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(0,240,255,0.5);">⚡ TRANSMIT KEY</button>
            </div>
            <div id="fb-stage-9" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#ffb000;"></div>
          </div>
        </div>
      </div>

      <!-- DOSSIER 05: ISHAAN Directive -->'''

if re.search(old_stego_submit, html):
    html = re.sub(old_stego_submit, new_stego_submit, html, count=1)
    print("12. Updated modal-stego to Stage 9")
else:
    print("Failed to find modal-stego submit block")

# 8. Update modal-clearance to Stage 11
old_clearance_pattern = r'<div id="modal-clearance" class="mil-modal">[\s\S]*?<!-- PUZZLE 04: The Resolved Comments Log -->'
new_clearance = '''<div id="modal-clearance" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-clearance')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /03_A1Z26 (CLEARANCE_CODE.txt)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-clearance')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-clearance')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <!-- High-Contrast Interactive Click & Submit Directives Banner -->
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 11 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Inspect the telex coordinate offsets: <code>[16 - 15 - 12 - 01 - 18 - 09 - 19]</code>.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Convert numbers to alphabet positions (1=A, 2=B... 16=P, 15=O, 12=L, 01=A, 18=R, 09=I, 19=S -> POLARIS). Sort the letters alphabetically into <strong>ailnors</strong>, enter below, and click <strong>[⚡ TRANSMIT KEY]</strong> (or enter POLARIS).
            </div>
          </div>

          <div style="background:rgba(8,16,26,0.95); border:1px solid var(--cyber-cyan); padding:20px; border-radius:4px; font-family:var(--font-mono);">
            <div style="color:var(--cyber-cyan); font-weight:bold; font-size:12px; margin-bottom:8px;">
              TELEX TELEMETRY: CLEARANCE_CODE.txt
            </div>
            <div style="background:#020509; border:1.5px solid rgba(0,240,255,0.4); padding:16px; text-align:center; font-size:22px; letter-spacing:5px; color:var(--cyber-gold); font-weight:bold; margin-bottom:14px; text-shadow:0 0 10px rgba(255,238,85,0.5);">
              16 - 15 - 12 - 01 - 18 - 09 - 19
            </div>

            <!-- Forensic Header -->
            <div style="background:rgba(0,0,0,0.7); border:1px solid rgba(0,240,255,0.25); border-radius:3px; padding:12px; font-size:12px; color:#cbd5e1; line-height:1.6;">
              <strong style="color:var(--cyber-cyan);">TELEMETRY NOTE:</strong> High-priority encrypted clearance packet intercepted from research directory gateway. Cryptographic indices correlate directly to base positional offsets (A=1... Z=26).
            </div>

            <!-- In-Modal Standardized Direct Submission Terminal: STAGE 11 -->
            <div class="stage-direct-submit-box" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.5); border-radius:6px; padding:14px 18px; margin-top:20px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(0,240,255,0.12);">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:1px;">
                  🎯 STAGE 11 // TRANSMIT DECRYPT KEY
                </div>
                <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
              </div>
              <div style="display:flex; gap:10px; align-items:center;">
                <input type="text" id="input-stage-11" placeholder="Enter alphabetically sorted key (ailnors)..." style="flex:1; background:#02060e; border:1px solid #00f0ff; color:#00f0ff; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(0,240,255,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey(11, document.getElementById('input-stage-11').value)">
                <button type="button" class="btn-tactical success" onclick="submitStageDirectKey(11, document.getElementById('input-stage-11').value)" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(0,240,255,0.5);">⚡ TRANSMIT KEY</button>
              </div>
              <div id="fb-stage-11" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#ffb000;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- PUZZLE 04: The Resolved Comments Log -->'''

if re.search(old_clearance_pattern, html):
    html = re.sub(old_clearance_pattern, new_clearance, html, count=1)
    print("13. Updated modal-clearance to Stage 11")
else:
    print("Failed to find modal-clearance pattern")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved aditi_os_widget.html with all modal updates!")
