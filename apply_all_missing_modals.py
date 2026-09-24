# apply_all_missing_modals.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update modal-whiteout with Stage 12 details & input
modal_whiteout_new = '''      <!-- ================================================================= -->
      <!-- DOSSIER 12: THE WHITEOUT SIGNATURE (Emergency_Log.doc) -->
      <!-- ================================================================= -->
      <div id="modal-whiteout" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-whiteout')">◄ ARCHIVE [ESC]</button>
            <span>TOP SECRET // /12_WHITEOUT (Emergency_Log.doc)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-whiteout')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-whiteout')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:#ffffff; color:#1e293b; padding:24px; border-radius:4px; box-shadow:0 6px 24px rgba(0,0,0,0.6); font-family:'Segoe UI', Arial, sans-serif; position:relative; min-height:220px;" id="whiteout-doc-container">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #e2e8f0; padding-bottom:8px; margin-bottom:14px;">
              <span style="font-weight:bold; font-size:13px; color:#0f172a;">📄 Emergency_Log.doc // DR. ADITI SANCTUARY DISPATCH</span>
              <span style="font-size:11px; color:#64748b;">FORMAT: GOOGLE DOCS v4</span>
            </div>
            <p style="font-size:13.5px; line-height:1.75; color:#334155; margin-bottom:14px;">
              "If you are reading this, I have gone into hiding. My workspace has been secured. Nothing is quite as empty as it appears."
            </p>
            
            <!-- Hidden White-on-White Text Layer -->
            <div id="whiteout-secret-box" style="color:#ffffff; background:#ffffff; font-size:14px; font-weight:bold; letter-spacing:1.5px; user-select:all; padding:12px 16px; border-radius:3px; transition:all 0.3s; margin-top:14px; border:1px dashed #f1f5f9;">
              CLASSIFIED EMERGENCY ACCESS: CLEARANCE_ALPHA
            </div>

            <div style="margin-top:18px; display:flex; gap:10px; align-items:center;">
              <button type="button" class="btn-tactical active" onclick="toggleWhiteoutSelection()" style="font-size:11px; padding:6px 14px;">🔦 HIGHLIGHT ALL (CTRL + A)</button>
              <button type="button" class="btn-tactical" onclick="toggleWhiteoutUv()" style="font-size:11px; padding:6px 14px;">⚡ UV DEPOLARIZER</button>
            </div>
          </div>

          <div style="background:rgba(0,240,255,0.08); border:1px solid var(--cyber-cyan); padding:12px 16px; border-radius:4px; margin-top:16px;">
            <div style="color:var(--cyber-cyan); font-weight:bold; font-size:12px; margin-bottom:6px;">
              🎯 STAGE 12 // TRANSMIT DECRYPTED CLEARANCE
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
              <input type="text" id="input-whiteout" placeholder="Enter hidden clearance phrase (CLEARANCE_ALPHA)..." style="flex:1; background:#000; border:1px solid var(--cyber-cyan); color:#00f0ff; padding:8px 12px; font-family:var(--font-mono); font-size:13px; border-radius:3px; outline:none;" onkeydown="if(event.key==='Enter') submitStageDirectKey(12, document.getElementById('input-whiteout').value)">
              <button type="button" class="dossier-btn" onclick="submitStageDirectKey(12, document.getElementById('input-whiteout').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:8px 18px; border-radius:3px; cursor:pointer;">
                TRANSMIT &rarr;
              </button>
            </div>
          </div>
        </div>
      </div>'''

# Replace existing modal-whiteout
content = re.sub(r'<!-- =+\s*-->\s*<!-- PUZZLE 01: The Whiteout.*?</div>\s*</div>\s*</div>|<div id="modal-whiteout" class="mil-modal">.*?</div>\s*</div>\s*</div>', modal_whiteout_new, content, count=1, flags=re.DOTALL)

# 2. Modals for Stage 10, 13, 14, 15, 16
other_modals = '''
      <!-- ================================================================= -->
      <!-- DOSSIER 10: QUARANTINE HONEYPOT TRAP (DO_NOT_RUN.exe) -->
      <!-- ================================================================= -->
      <div id="modal-honeypot" class="mil-modal">
        <div class="mil-modal-header" style="background:rgba(255,0,60,0.15); border-bottom:1px solid #ff003c;">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-honeypot')">◄ ARCHIVE [ESC]</button>
            <span style="color:#ff3366;">⚠️ QUARANTINE PROTOCOL // DO_NOT_RUN.exe [HONEYPOT]</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-honeypot')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-honeypot')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:rgba(255,0,60,0.1); border-left:4px solid #ff003c; padding:12px 16px; margin-bottom:14px; color:#fca5a5; font-size:13px;">
            <strong>🚨 ACTIVE MALICIOUS HONEYPOT DETECTED</strong><br>
            ISHAAN has staged an automated sandbox trap designed to simulate a credentials prompt and lock down your workstation for 5 minutes.
          </div>
          <div style="background:#030712; border:1px solid rgba(255,0,60,0.3); border-radius:4px; padding:16px; margin-bottom:16px; font-family:var(--font-mono);">
            <div style="color:#ff3366; font-weight:bold; font-size:13px; margin-bottom:8px;">[SYSTEM QUARANTINE ADVISORY]</div>
            <p style="color:#cbd5e1; font-size:12px; line-height:1.7;">
              Executable file <code>DO_NOT_RUN.exe</code> contains a weaponized watchdog hook.<br>
              <strong>RULE OF ENGAGEMENT:</strong> Do NOT click the execution trigger! To safely disarm the honeypot without tripping the lockdown alarm, enter the emergency tactical bypass keyword: <code>BYPASS</code>.
            </p>
            <div style="margin-top:12px;">
              <button type="button" class="btn-tactical" onclick="triggerLockdownTrap()" style="background:rgba(255,0,60,0.2); border-color:#ff003c; color:#ff6b81;">
                ☠️ EXECUTE BINARY (DANGEROUS // +5M LOCKDOWN)
              </button>
            </div>
          </div>
          <div style="background:rgba(255,255,255,0.03); border:1px dashed #475569; border-radius:4px; padding:12px 16px;">
            <div style="color:var(--cyber-cyan); font-weight:bold; font-size:12px; margin-bottom:8px;">
              🎯 STAGE 10 DISARM // TRANSMIT BYPASS KEY
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
              <input type="text" id="input-honeypot" placeholder="Enter emergency disarm key (e.g. BYPASS)..." style="flex:1; background:#000; border:1px solid var(--cyber-cyan); color:#00f0ff; padding:8px 12px; font-family:var(--font-mono); font-size:13px; border-radius:3px; outline:none;" onkeydown="if(event.key==='Enter') submitStageDirectKey(10, document.getElementById('input-honeypot').value)">
              <button type="button" class="dossier-btn" onclick="submitStageDirectKey(10, document.getElementById('input-honeypot').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:8px 18px; border-radius:3px; cursor:pointer;">
                DISARM &rarr;
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- ================================================================= -->
      <!-- DOSSIER 13: THE ROT-4 IEEE SHIFT (Encrypted_Beacon.txt) -->
      <!-- ================================================================= -->
      <div id="modal-rot4" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-rot4')">◄ ARCHIVE [ESC]</button>
            <span>TOP SECRET // /13_ROT4 (Encrypted_Beacon.txt)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-rot4')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-rot4')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Encrypted_Beacon.txt // ROT-4 Shift Protocol</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"Dr. Aditi shifted each letter of her emergency beacon forward by the length of the acronym 'IEEE' (4 letters). Reverse the shift to recover her callsign."</em>
            </p>
            <div style="background:#030712; padding:14px; border:1px solid #00f0ff; border-radius:4px; font-family:monospace; font-size:15px; text-align:center; color:#00ff88; letter-spacing:3px;">
              ENCRYPTED STRING: EHMXMW13
            </div>
            <div style="margin-top:10px; color:#cbd5e1; font-size:11px; text-align:center;">
              RULE: Shift each alphabetical character backward by 4 positions (Numbers remain unchanged).
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-rot4" placeholder="Enter decoded beacon string (e.g. ADITIS13)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;" onkeydown="if(event.key==='Enter') submitStageDirectKey(13, document.getElementById('input-rot4').value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(13, document.getElementById('input-rot4').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:10px 20px; border-radius:4px; cursor:pointer;">
              TRANSMIT &rarr;
            </button>
          </div>
        </div>
      </div>

      <!-- ================================================================= -->
      <!-- DOSSIER 14: THE ATBASH CIPHER MIRROR (Mirror_Log.txt) -->
      <!-- ================================================================= -->
      <div id="modal-atbash" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-atbash')">◄ ARCHIVE [ESC]</button>
            <span>TOP SECRET // /14_ATBASH (Mirror_Log.txt)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-atbash')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-atbash')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Mirror_Log.txt // Atbash Alphabet Reversal</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"Dr. Aditi mirrored her alphabet across the axis (A &harr; Z, B &harr; Y, C &harr; X...). Invert the string to reveal the mission clearance."</em>
            </p>
            <div style="background:#030712; padding:14px; border:1px solid #00f0ff; border-radius:4px; font-family:monospace; font-size:15px; text-align:center; color:#ffd700; letter-spacing:3px;">
              MIRRORED CIPHERTEXT: KILQVBG
            </div>
            <div style="margin-top:10px; font-size:11px; color:#cbd5e1; text-align:center;">
              A B C D E F G H I J K L M &harr; Z Y X W V U T S R Q P O N
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-atbash" placeholder="Enter decrypted mirror word (e.g. PROJECT)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;" onkeydown="if(event.key==='Enter') submitStageDirectKey(14, document.getElementById('input-atbash').value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(14, document.getElementById('input-atbash').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:10px 20px; border-radius:4px; cursor:pointer;">
              TRANSMIT &rarr;
            </button>
          </div>
        </div>
      </div>

      <!-- ================================================================= -->
      <!-- DOSSIER 15: THE POLYBIUS COORDINATE TRAIL (Matrix_Coordinates.pdf) -->
      <!-- ================================================================= -->
      <div id="modal-polybius" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-polybius')">◄ ARCHIVE [ESC]</button>
            <span>TOP SECRET // /15_POLYBIUS (Matrix_Coordinates.pdf)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-polybius')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-polybius')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Matrix_Coordinates.pdf // 5x5 Polybius Grid</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"Look up each coordinate pair as (Row, Column) in the 5x5 Polybius Square (I and J share a cell)."</em>
            </p>
            <div style="display:grid; grid-template-columns:repeat(6, 1fr); max-width:280px; margin:0 auto 12px auto; text-align:center; font-family:monospace; font-weight:bold; gap:4px; font-size:13px;">
              <div></div><div style="color:#00f0ff;">1</div><div style="color:#00f0ff;">2</div><div style="color:#00f0ff;">3</div><div style="color:#00f0ff;">4</div><div style="color:#00f0ff;">5</div>
              <div style="color:#00f0ff;">1</div><div>A</div><div>B</div><div>C</div><div>D</div><div>E</div>
              <div style="color:#00f0ff;">2</div><div>F</div><div>G</div><div>H</div><div>I/J</div><div>K</div>
              <div style="color:#00f0ff;">3</div><div>L</div><div>M</div><div>N</div><div>O</div><div>P</div>
              <div style="color:#00f0ff;">4</div><div>Q</div><div>R</div><div>S</div><div>T</div><div>U</div>
              <div style="color:#00f0ff;">5</div><div>V</div><div>W</div><div>X</div><div>Y</div><div>Z</div>
            </div>
            <div style="background:#030712; padding:10px; border:1px dashed #00f0ff; text-align:center; font-family:monospace; font-size:14px; color:#00f0ff; letter-spacing:2px;">
              COORDINATES: (5,1) (1,5) (1,3) (4,4) (3,4) (4,2)
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-polybius" placeholder="Enter decoded word (e.g. VECTOR)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;" onkeydown="if(event.key==='Enter') submitStageDirectKey(15, document.getElementById('input-polybius').value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(15, document.getElementById('input-polybius').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:10px 20px; border-radius:4px; cursor:pointer;">
              TRANSMIT &rarr;
            </button>
          </div>
        </div>
      </div>

      <!-- ================================================================= -->
      <!-- DOSSIER 16: THE FREQUENCY OVERRIDE COUNT (Mass_System_Log.txt) -->
      <!-- ================================================================= -->
      <div id="modal-frequency" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-frequency')">◄ ARCHIVE [ESC]</button>
            <span>TOP SECRET // /16_FREQUENCY (Mass_System_Log.txt)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-frequency')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-frequency')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Mass_System_Log.txt // Occurrence Calculation</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"Count how many times the exact term 'OVERRIDE' appears in the log, then multiply that count by 100 to calculate the frequency bypass value."</em>
            </p>
            <div style="background:#030712; padding:14px; border:1px solid #334155; border-radius:4px; font-family:monospace; font-size:12px; height:150px; overflow-y:auto; color:#cbd5e1; user-select:text; line-height:1.6;">
              [08:14] OVERRIDE sequence requested.<br>
              [08:16] System reports OVERRIDE parity checked.<br>
              [08:20] Security subroutines verify OVERRIDE token.<br>
              [08:24] Subsystem 4 requires OVERRIDE key.<br>
              [08:29] Secondary station sets OVERRIDE bit.<br>
              [08:35] Dr. Aditi issues emergency OVERRIDE call.<br>
              [08:41] ISHAAN attempts OVERRIDE interception.<br>
              [08:44] Telemetry confirms OVERRIDE bus online.<br>
              [08:50] Firewall blocks malicious OVERRIDE injection.<br>
              [08:55] Central gateway acknowledges OVERRIDE authorization.<br>
              [09:02] Bunker console executes OVERRIDE cycle.<br>
              [09:07] Neural core locks during OVERRIDE procedure.<br>
              [09:12] Kernel panic: OVERRIDE failed.<br>
              [09:18] Final commit: OVERRIDE halted.<br>
            </div>
            <div style="margin-top:10px; font-size:11px; color:#cbd5e1; text-align:center;">
              Ctrl+F or count manually: Total 'OVERRIDE' occurrences &times; 100
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-frequency" placeholder="Enter frequency calculation (matches x 100)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px;" onkeydown="if(event.key==='Enter') submitStageDirectKey(16, document.getElementById('input-frequency').value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(16, document.getElementById('input-frequency').value)" style="background:var(--cyber-cyan); color:#000; font-weight:bold; border:none; padding:10px 20px; border-radius:4px; cursor:pointer;">
              TRANSMIT &rarr;
            </button>
          </div>
        </div>
      </div>
'''

# Insert other_modals right after modal-whiteout
target_anchor = '      </div>\n      </div>\n\n      <!-- ================================================================= -->\n      <!-- PUZZLE 02: The Simple Acrostic Note -->'
if 'id="modal-honeypot"' not in content:
    if target_anchor in content:
        content = content.replace(target_anchor, '      </div>\n      </div>\n' + other_modals + '\n      <!-- ================================================================= -->\n      <!-- PUZZLE 02: The Simple Acrostic Note -->')
    else:
        # Fallback to </main>
        content = content.replace('</main>', other_modals + '\n</main>')

# Update STAGE_REQUIRED_MODAL_MAP to include 'modal-honeypot': 10
if "'modal-honeypot': 10" not in content:
    content = content.replace("'card-trap': 10,", "'card-trap': 10,\n      'modal-honeypot': 10,")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] Successfully updated all modals in aditi_os_widget.html")
