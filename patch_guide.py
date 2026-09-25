import re

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_guide_pattern = r'<!-- STAGE 01 -->[\s\S]*?<!-- STAGE 12 -->'

new_guide = '''<!-- STAGE 01 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 01: Farewell.doc (The Disappearing Message)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-origin');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click on Card 01 [Farewell.doc] on the left. Highlight all text with Ctrl+A or toggle the UV Optical Filter to reveal the white-on-white text at the bottom.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the revealed clearance key (<code>ORIGIN</code>) into the box inside the popup and click <strong>[⚡ TRANSMIT KEY]</strong> (or enter <code>decrypt ORIGIN</code> into terminal prompt).
            </div>
          </div>

          <!-- STAGE 02 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00ff66; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00ff66; font-weight:900; font-size:13px;">STAGE 02: README.doc (The Wrong Folder / ASCII Sum)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-origin');" style="background:#00ff66; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 02 [README.doc]. Calculate the ASCII sum of <code>aDIti@28</code> (97+68+73+116+105+64+50+56 = 629) or extract letters according to the index legend.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the computed value (<code>629</code>) or directive (<code>LOOK BEHIND THE DATE</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 03 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 03: Incident_Logs.doc (The Date That Doesn't Exist)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-incident-logs');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 03 [Incident_Logs.doc]. Audit the listed launch dates in 2025. Identify that Feb 29, 2025 is an impossible calendar date (2025 is not a leap year).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the corrected date (<code>28/02/2025</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 04 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 04: Security_Audit.pdf (The Timestamp Murder Mystery)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-security-audit');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 04 [Security_Audit.pdf]. Notice Dr. Aditi keycarded out of the building at 22:44, making the local terminal override at 22:46 physically impossible.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the impossible override timestamp (<code>22:46</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 05 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 05: Aditi_Memo.doc (The Simple Acrostic Note)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-acrostic');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 05 [Aditi_Memo.doc]. Extract the first letters of each sentence in Dr. Aditi's 4-line memo: System (S), ADI (A), Failsafe (F), Exit (E).<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the acrostic keyword (<code>SAFE</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 06 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 06: AUTHENTIC_LOG.doc (Which Aditi Is Real? Font Verification)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-font');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 06 [AUTHENTIC_LOG.doc]. Compare formatting against the style guide: Dr. Aditi strictly formats official logs in Arial, 11pt.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the authentic font family (<code>ARIAL</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 07 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 07: Incident_Report.doc (The Revision History Conflict)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-version-hist');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 07 [Incident_Report.doc]. Click on the <strong>[Previous Revision (20:18Z by Dr. Aditi)]</strong> tab to view her genuine un-tampered commit text before ISHAAN's purge.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the recovered warning status (<code>CORRUPTED</code> or <code>FALSE_RECORDS</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 08 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 08: audio_log_07.mp3 (Morse Audio Transmission)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-spectro');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 08 [audio_log_07.mp3]. Click <strong>[▶ PLAY BEACON]</strong> to listen to the Morse beeps (.-- .... .. - .), or decode via the visualizer.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the decoded Morse keyword (<code>WHITE</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 09 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 09: Dark_Terminal.png (The Steganography Mask)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-stego');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 09 [Dark_Terminal.png]. Drag the <strong>Exposure Boost</strong> and <strong>Contrast Gain</strong> sliders to maximum to reveal faint text hidden in the black pixels.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the illuminated terminal code (<code>SHADOW_CORE</code>) into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong>.
            </div>
          </div>

          <!-- STAGE 10 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #ff003c; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#ff003c; font-weight:900; font-size:13px;">STAGE 10: DO_NOT_RUN.exe (Honeypot Trap Disarm)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-honeypot');" style="background:#ff003c; color:#fff; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 10 [DO_NOT_RUN.exe]. <strong>DO NOT CLICK</strong> the red execution trigger (adds +5:00 penalty!). Read the quarantine notes to find the safe bypass keyword.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the bypass command (<code>BYPASS</code>) into the box inside the modal (or type in Tactical Shell) to disarm safely.
            </div>
          </div>

          <!-- STAGE 11 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid #334155; border-left:4px solid #00f0ff; border-radius:6px; padding:14px 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="color:#00f0ff; font-weight:900; font-size:13px;">STAGE 11: CLEARANCE_CODE.txt (The Binary Master A1Z26)</span>
              <button type="button" onclick="closeModal('modal-puzzles-guide'); openModal('modal-clearance');" style="background:#00f0ff; color:#000; font-weight:bold; font-size:11px; padding:3px 10px; border-radius:3px; border:none; cursor:pointer;">⚡ OPEN DOSSIER</button>
            </div>
            <div style="font-size:12.5px; color:#e2e8f0; line-height:1.6;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> Click Card 11 [CLEARANCE_CODE.txt]. Convert the sequence 16-15-12-01-18-09-19 into letters (POLARIS), then sort alphabetically.<br>
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Enter the sorted key (<code>ailnors</code>) or <code>POLARIS</code> into the box inside the modal and click <strong>[⚡ TRANSMIT KEY]</strong> to advance to Stage 12!
            </div>
          </div>

          <!-- STAGE 12 -->'''

if re.search(old_guide_pattern, text):
    text = re.sub(old_guide_pattern, new_guide, text, count=1)
    print("Updated modal-puzzles-guide!")
else:
    print("Pattern not found in modal-puzzles-guide")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated guide in aditi_os_widget.html!")
