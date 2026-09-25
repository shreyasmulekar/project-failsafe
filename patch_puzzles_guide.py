import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 16 [Mass_System_Log.txt]. Search through the log to count how many times the exact term 'OVERRIDE' appears and multiply by 100.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the calculated frequency value into the in-modal input box (or Quick Decrypt bar) and click <strong>[TRANSMIT &rarr;]</strong> to trigger TARA's final liberation!
            </div>
          </div>'''

replacement = '''            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 16 [Mass_System_Log.txt]. Search through the log to count how many times the exact term 'OVERRIDE' appears and multiply by 100.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the calculated frequency value into the in-modal input box (or Quick Decrypt bar) and click <strong>[TRANSMIT &rarr;]</strong> to advance to Stage 17!
            </div>
          </div>

          <!-- STAGE 17 GUIDE -->
          <div class="guide-stage-card" style="background:#090d16; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; font-family:var(--font-mono, monospace);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 17: Intercepted_ADI_Transmission.pdf (Rogue Polybius Shift)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-polybius-shift');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 17 [Intercepted_ADI_Transmission.pdf]. Apply vector translation (+1 Row, -1 Col) to the coordinate pairs (4,2) (3,4) (2,2) (4,4) (1,5).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Map each translated coordinate to the standard 5x5 Polybius grid and enter the resulting 5-letter key (VSLXI).
            </div>
          </div>

          <!-- STAGE 18 GUIDE -->
          <div class="guide-stage-card" style="background:#090d16; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; font-family:var(--font-mono, monospace);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 18: Cycle_Diagnostics.png (The Modular Clock Loop)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-clock-loop');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 18 [Cycle_Diagnostics.png]. Trace the cyclic jumps across the 12-hour circular buffer starting from Node L (12:00).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Apply shifts +7, +8, +11, +5, +10 modulo 12. Record the 5 landed node letters (GCBGE) and click <strong>[TRANSMIT &rarr;]</strong>.
            </div>
          </div>

          <!-- STAGE 19 GUIDE -->
          <div class="guide-stage-card" style="background:#090d16; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; font-family:var(--font-mono, monospace);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 19: Server_Status_Check.pdf (The Anomaly Checklist)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-status-check');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 19 [Server_Status_Check.pdf]. Compare each server node temperature against the 40°C - 45°C Normal Range.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Find the overheating outlier (Node Gamma at 47°C) and enter its name in ALL CAPS (GAMMA).
            </div>
          </div>

          <!-- STAGE 20 GUIDE -->
          <div class="guide-stage-card" style="background:#090d16; border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:14px; font-family:var(--font-mono, monospace);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 20: Emergency_Override_Key.txt (The Shift Cipher Matrix)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-shift-matrix');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 20 [Emergency_Override_Key.txt]. Sunday, October 13, 2013 corresponds to Day 7.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Shift each letter in ciphertext KHOOR backward by 7 positions in the alphabet to recover the command (DAHHK).
            </div>
          </div>

          <!-- STAGE 21 GUIDE -->
          <div class="guide-stage-card" style="background:#090d16; border:1px solid rgba(0,255,136,0.4); border-radius:6px; padding:14px; font-family:var(--font-mono, monospace);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00ff88; font-weight:900; font-size:13px;">STAGE 21: System_Audit_2013.log (The Log Anomaly Timeline - FINALE)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-audit-timeline');" style="background:#00ff88; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 21 [System_Audit_2013.log]. Identify the out-of-chronological-order log entry (LOG 104 at 14:08:30).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Multiply the LOG_ID (104) by total entries (5) to calculate the final master key: 104 x 5 = 520!
            </div>
          </div>'''

if target in text:
    text = text.replace(target, replacement)
    print("Added Stages 17..21 to modal-puzzles-guide successfully")
else:
    print("Warning: target not found in modal-puzzles-guide")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)
