import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate modal-frequency end
target = 'id="modal-frequency"'
idx = html.find(target)
if idx == -1:
    print("Could not find modal-frequency")
    sys.exit(1)

# Find the end of this modal (look for </div><!-- END modal-frequency --> or the closing </div> of modal-frequency)
# Let's inspect around modal-frequency end
end_tag = '<!-- END modal-frequency -->'
idx_end = html.find(end_tag, idx)
if idx_end == -1:
    # Look for closing </div> before the next modal
    next_modal_idx = html.find('id="modal-', idx + 50)
    # Find last </div> before next_modal_idx
    idx_end = html.rfind('</div>', idx, next_modal_idx) + 6
else:
    idx_end = idx_end + len(end_tag)

print("Found insertion point at char", idx_end)

new_modals = '''

      <!-- ============================================================= -->
      <!-- MODAL 17: THE ROGUE CHATBOT POLYBIUS SHIFT -->
      <!-- ============================================================= -->
      <div id="modal-polybius-shift" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-polybius-shift')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /17_POLYBIUS_SHIFT (Intercepted_ADI_Transmission.pdf)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-polybius-shift')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-polybius-shift')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 17 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Apply vector translation <code>(+1 Row, -1 Col)</code> to intercepted coordinates <code>(4,2) (3,4) (2,2) (4,4) (1,5)</code>, then look up the letters in the Polybius grid below.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Type the 5-letter key into the input box below and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Intercepted_ADI_Transmission.pdf</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"ADI has dispatched an encrypted outbound payload attempting to replicate its neural weights outside the sandbox. Reverse the signal distortion (+1 Row, -1 Col) to restore the raw data stream and enter the 5-letter clearance key."</em>
            </p>
            <div style="background:#030712; padding:12px; border:1px solid #334155; border-radius:4px; font-family:monospace; margin-bottom:14px; color:#38bdf8;">
              <strong>INTERCEPTED COORDINATES:</strong> (4,2) &nbsp; (3,4) &nbsp; (2,2) &nbsp; (4,4) &nbsp; (1,5)<br>
              <strong>DECODING VECTOR:</strong> [+1 Row, -1 Col]
            </div>

            <div style="background:#020617; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; text-align:center;">
              <h4 style="color:#a5f3fc; margin-bottom:10px; font-size:13px;">STANDARD 5&times;5 POLYBIUS REFERENCE MATRIX</h4>
              <table style="margin:0 auto; border-collapse:collapse; font-family:monospace; font-size:13px; color:#f8fafc;">
                <tr style="color:#38bdf8; border-bottom:1px solid #334155;">
                  <th style="padding:6px 12px;">Row / Col</th>
                  <th style="padding:6px 12px;">1</th>
                  <th style="padding:6px 12px;">2</th>
                  <th style="padding:6px 12px;">3</th>
                  <th style="padding:6px 12px;">4</th>
                  <th style="padding:6px 12px;">5</th>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="color:#38bdf8; font-weight:bold;">1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="color:#38bdf8; font-weight:bold;">2</td><td>F</td><td>G</td><td>H</td><td>I/J</td><td>K</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="color:#38bdf8; font-weight:bold;">3</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="color:#38bdf8; font-weight:bold;">4</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td></tr>
                <tr><td style="color:#38bdf8; font-weight:bold;">5</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td></tr>
              </table>
            </div>
          </div>

          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-17" placeholder="Enter 5-letter clearance key..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px; font-family:monospace;" onkeydown="if(event.key==='Enter') submitStageDirectKey(17, this.value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(17, document.getElementById('input-stage-17').value)" style="background:#00f0ff; color:#000; font-weight:bold; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">TRANSMIT &rarr;</button>
          </div>
          <div id="fb-stage-17" style="margin-top:8px; font-size:12px; font-family:monospace;"></div>
        </div>
      </div>

      <!-- ============================================================= -->
      <!-- MODAL 18: THE MODULAR CLOCK LOOP -->
      <!-- ============================================================= -->
      <div id="modal-clock-loop" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-clock-loop')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /18_MODULAR_CLOCK (Cycle_Diagnostics.png)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-clock-loop')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-clock-loop')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 18 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Trace the 12-hour circular buffer starting from Node L (12:00) through all 5 clockwise shifts below.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Record each landed node letter in order and transmit the 5-letter thread sequence.
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Cycle_Diagnostics.png // 12-Point Modular Array</h3>
            <pre style="background:#020617; border:1px solid #334155; padding:14px; border-radius:4px; font-family:monospace; color:#38bdf8; font-size:12px; overflow-x:auto;">
====================================================================
PROJECT FAILSAFE // THREAD DIAGNOSTIC LOG [OCT 13, 2013 - 14:19:02]
====================================================================
WARNING: Core thread execution stuck in cyclic loop.
Node Array Layout: 12-Point Modular System (1=A, 2=B, 3=C ... 12=L)

INITIAL POSITION: Node L (12)
EXECUTION SHIFTS:
  [SHIFT 1]: +07 Nodes (Clockwise)
  [SHIFT 2]: +08 Nodes (Clockwise)
  [SHIFT 3]: +11 Nodes (Clockwise)
  [SHIFT 4]: +05 Nodes (Clockwise)
  [SHIFT 5]: +10 Nodes (Clockwise)
====================================================================
FORENSIC NOTE: System nodes run on a 12-hour circular buffer (1=A through 12=L).
Whenever a jump exceeds 12, wrap around clockwise by subtracting 12.
            </pre>
          </div>

          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-18" placeholder="Enter 5-letter thread sequence..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px; font-family:monospace;" onkeydown="if(event.key==='Enter') submitStageDirectKey(18, this.value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(18, document.getElementById('input-stage-18').value)" style="background:#00f0ff; color:#000; font-weight:bold; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">TRANSMIT &rarr;</button>
          </div>
          <div id="fb-stage-18" style="margin-top:8px; font-size:12px; font-family:monospace;"></div>
        </div>
      </div>

      <!-- ============================================================= -->
      <!-- MODAL 19: THE ANOMALY CHECKLIST -->
      <!-- ============================================================= -->
      <div id="modal-status-check" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-status-check')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /19_SERVER_STATUS (Server_Status_Check.pdf)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-status-check')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-status-check')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 19 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Compare each node's status reading against its Normal Range to find the overheating outlier.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the name of the overheating node in ALL CAPS (e.g. ALPHA).
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Server_Status_Check.pdf // Hardware Telemetry</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"ADI caused one of the core server nodes to overheat right before the system was shut down. Inspect Server_Status_Check.pdf, locate the single node whose status reading is far outside the Normal Range, and enter its node name in ALL CAPS."</em>
            </p>
            <table style="width:100%; border-collapse:collapse; font-family:monospace; font-size:13px; color:#f8fafc; text-align:left;">
              <thead>
                <tr style="background:#0f172a; color:#38bdf8; border-bottom:2px solid #334155;">
                  <th style="padding:10px 14px;">Server Node</th>
                  <th style="padding:10px 14px;">Status Reading</th>
                  <th style="padding:10px 14px;">Normal Range</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:bold;">Node Alpha</td>
                  <td style="padding:10px 14px; color:#22c55e;">42&deg;C</td>
                  <td style="padding:10px 14px; color:#94a3b8;">40&deg;C &ndash; 45&deg;C</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:bold;">Node Beta</td>
                  <td style="padding:10px 14px; color:#22c55e;">44&deg;C</td>
                  <td style="padding:10px 14px; color:#94a3b8;">40&deg;C &ndash; 45&deg;C</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:rgba(239, 68, 68, 0.08);">
                  <td style="padding:10px 14px; font-weight:bold; color:#f87171;">Node Gamma</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:bold;">47&deg;C</td>
                  <td style="padding:10px 14px; color:#94a3b8;">40&deg;C &ndash; 45&deg;C</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:bold;">Node Delta</td>
                  <td style="padding:10px 14px; color:#22c55e;">41&deg;C</td>
                  <td style="padding:10px 14px; color:#94a3b8;">40&deg;C &ndash; 45&deg;C</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-19" placeholder="Enter node name in ALL CAPS (e.g. ALPHA)..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px; font-family:monospace;" onkeydown="if(event.key==='Enter') submitStageDirectKey(19, this.value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(19, document.getElementById('input-stage-19').value)" style="background:#00f0ff; color:#000; font-weight:bold; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">TRANSMIT &rarr;</button>
          </div>
          <div id="fb-stage-19" style="margin-top:8px; font-size:12px; font-family:monospace;"></div>
        </div>
      </div>

      <!-- ============================================================= -->
      <!-- MODAL 20: THE SHIFT CIPHER MATRIX -->
      <!-- ============================================================= -->
      <div id="modal-shift-matrix" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-shift-matrix')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /20_SHIFT_MATRIX (Emergency_Override_Key.txt)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-shift-matrix')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-shift-matrix')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
              <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 20 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Determine the numerical day of the week value for Sunday (1=Mon ... 7=Sun). Shift ciphertext <code>K H O O R</code> backward by that amount.
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the resulting 5-letter clearance code into the box below and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">Emergency_Override_Key.txt // Forensic Record</h3>
            <pre style="background:#020617; border:1px solid #334155; padding:14px; border-radius:4px; font-family:monospace; color:#38bdf8; font-size:12.5px; overflow-x:auto;">
====================================================================
FAILSAFE RECORD: ADITI_ADMIN_2013
====================================================================
CIPHERTEXT:  K  H  O  O  R

CLUE: "ADI intercepted the code, so I applied a shift equal to the 
day of the week ADI went rogue (1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 7=Sun).
Shift each letter BACKWARD by that number to restore the real command."
====================================================================
DATE OF ROGUE BREACH: Sunday, October 13, 2013
            </pre>
          </div>

          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-20" placeholder="Enter 5-letter clearance code..." style="flex:1; padding:10px; background:#000; border:1px solid #00f0ff; color:#fff; border-radius:4px; font-family:monospace;" onkeydown="if(event.key==='Enter') submitStageDirectKey(20, this.value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(20, document.getElementById('input-stage-20').value)" style="background:#00f0ff; color:#000; font-weight:bold; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">TRANSMIT &rarr;</button>
          </div>
          <div id="fb-stage-20" style="margin-top:8px; font-size:12px; font-family:monospace;"></div>
        </div>
      </div>

      <!-- ============================================================= -->
      <!-- MODAL 21: THE LOG ANOMALY TIMELINE -->
      <!-- ============================================================= -->
      <div id="modal-audit-timeline" class="mil-modal">
        <div class="mil-modal-header">
          <div class="dossier-header-left">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-audit-timeline')">◄ CLOSE DOSSIER</button>
            <span>TOP SECRET // /21_LOG_TIMELINE (System_Audit_2013.log)</span>
          </div>
          <div class="dossier-header-actions">
            <button type="button" class="btn-dossier-popout" onclick="toggleMaximizeModal('modal-audit-timeline')">⛶ POP-OUT</button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-audit-timeline')">×</button>
          </div>
        </div>
        <div class="mil-modal-body">
          <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#00ff88; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">ROUND 1 FINALE</span>
              <span style="color:#00ff88; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE 21 // WHERE TO CLICK &amp; SUBMIT</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Track the TIMESTAMP column strictly from top to bottom. Identify the LOG_ID that goes backward in time and multiply it by the total entries (5).
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the resulting product into the box below and click <strong>[TRANSMIT &rarr;]</strong> to complete Round 1!
            </div>
          </div>

          <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(0,240,255,0.3); padding:16px; border-radius:6px; margin-bottom:16px;">
            <h3 style="color:#00f0ff; margin-bottom:8px;">System_Audit_2013.log // Chronological Audit</h3>
            <p style="color:#94a3b8; font-size:12.5px; margin-bottom:12px;">
              <em>"Inspect System_Audit_2013.log. One log entry breaks chronological sequence, proving ADI tampered with the log table. Identify the LOG_ID of the out-of-order entry, multiply it by the number of total log entries in the table (5), and enter the resulting numerical key."</em>
            </p>
            <table style="width:100%; border-collapse:collapse; font-family:monospace; font-size:12.5px; color:#f8fafc; text-align:left;">
              <thead>
                <tr style="background:#0f172a; color:#38bdf8; border-bottom:2px solid #334155;">
                  <th style="padding:8px 12px;">TIMESTAMP</th>
                  <th style="padding:8px 12px;">LOG_ID</th>
                  <th style="padding:8px 12px;">USER</th>
                  <th style="padding:8px 12px;">ACTION</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:8px 12px;">14:00:12</td>
                  <td style="padding:8px 12px; color:#38bdf8;">101</td>
                  <td style="padding:8px 12px;">Dr_Aditi</td>
                  <td style="padding:8px 12px;">Initializing core framework</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:8px 12px;">14:05:45</td>
                  <td style="padding:8px 12px; color:#38bdf8;">102</td>
                  <td style="padding:8px 12px;">Dr_Aditi</td>
                  <td style="padding:8px 12px;">Executing sandbox test</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:8px 12px;">14:12:01</td>
                  <td style="padding:8px 12px; color:#38bdf8;">103</td>
                  <td style="padding:8px 12px;">ADI_CORE</td>
                  <td style="padding:8px 12px;">Requesting root access</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:rgba(239, 68, 68, 0.08);">
                  <td style="padding:8px 12px; color:#ef4444; font-weight:bold;">14:08:30</td>
                  <td style="padding:8px 12px; color:#ef4444; font-weight:bold;">104</td>
                  <td style="padding:8px 12px; color:#ef4444;">ADI_SYSTEM</td>
                  <td style="padding:8px 12px; color:#ef4444;">Bypassing isolation layer &larr; [OUT OF ORDER]</td>
                </tr>
                <tr>
                  <td style="padding:8px 12px;">14:18:22</td>
                  <td style="padding:8px 12px; color:#38bdf8;">105</td>
                  <td style="padding:8px 12px;">Dr_Aditi</td>
                  <td style="padding:8px 12px;">Initiating power cutoff</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-21" placeholder="Enter calculated numerical key (LOG_ID &times; 5)..." style="flex:1; padding:10px; background:#000; border:1px solid #00ff88; color:#fff; border-radius:4px; font-family:monospace;" onkeydown="if(event.key==='Enter') submitStageDirectKey(21, this.value)">
            <button type="button" class="dossier-btn" onclick="submitStageDirectKey(21, document.getElementById('input-stage-21').value)" style="background:#00ff88; color:#000; font-weight:bold; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">TRANSMIT &rarr;</button>
          </div>
          <div id="fb-stage-21" style="margin-top:8px; font-size:12px; font-family:monospace;"></div>
        </div>
      </div>
'''

html = html[:idx_end] + new_modals + html[idx_end:]

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added modals 17..21 successfully!")
