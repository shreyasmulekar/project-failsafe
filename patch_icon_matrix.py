with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_matrix = '''        <div class="tactical-card" id="card-recovery-term" onclick="openModal('modal-recovery')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color: rgba(0,255,102,0.4);">
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
        </div>'''

new_matrix = '''        <div class="tactical-card" id="card-origin" onclick="openModal('modal-origin')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color: rgba(0,255,102,0.4);">
          <span class="card-tag" style="color: #00ff66; border-color: #00ff66;">STAGE 01</span>
          <div class="card-symbol" style="color: #00ff66;">📄</div>
          <div class="card-title" style="color: #00ff66;">Farewell.doc</div>
        </div>

        <div class="tactical-card" id="card-memory" onclick="openModal('modal-origin')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color: rgba(255, 184, 0, 0.4);">
          <span class="card-tag" style="background: var(--hazard-amber); color: #000;">STAGE 02</span>
          <div class="card-symbol">📁</div>
          <div class="card-title">README.doc</div>
        </div>

        <div class="tactical-card" id="card-timeline" onclick="openModal('modal-incident-logs')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 03</span>
          <div class="card-symbol">📅</div>
          <div class="card-title">Incident_Logs.doc</div>
        </div>

        <div class="tactical-card" id="card-audit" onclick="openModal('modal-security-audit')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 04</span>
          <div class="card-symbol">⏱️</div>
          <div class="card-title">Security_Audit.pdf</div>
        </div>'''

text = text.replace(old_matrix, new_matrix)

# Also update Stages 05-09 in icon-matrix
old_matrix_p2 = '''        <div class="tactical-card" id="card-clearance" onclick="openModal('modal-clearance')" onmouseenter="tacticalSound.playHoverBlip()">
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
        </div>'''

new_matrix_p2 = '''        <div class="tactical-card" id="card-acrostic" onclick="openModal('modal-acrostic')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 05</span>
          <div class="card-symbol">📝</div>
          <div class="card-title">Aditi_Memo.doc</div>
        </div>

        <div class="tactical-card" id="card-font" onclick="openModal('modal-font')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 06</span>
          <div class="card-symbol">🔤</div>
          <div class="card-title">AUTHENTIC_LOG.doc</div>
        </div>

        <div class="tactical-card" id="card-version" onclick="openModal('modal-version-hist')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 07</span>
          <div class="card-symbol">🕒</div>
          <div class="card-title">Incident_Report.doc</div>
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

        <div class="tactical-card" id="card-stego" onclick="openModal('modal-stego')" onmouseenter="tacticalSound.playHoverBlip()">
          <span class="card-tag">STAGE 09</span>
          <div class="card-symbol">🖼️</div>
          <div class="card-title">Dark_Terminal.png</div>
        </div>'''

text = text.replace(old_matrix_p2, new_matrix_p2)

# Also update Stage 11 in icon-matrix
old_matrix_p3 = '''        <div class="tactical-card" id="card-failsafe" onclick="openModal('modal-failsafe')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color:rgba(0,240,255,0.4);">
          <span class="card-tag" style="color:var(--cyber-cyan);">STAGE 11</span>
          <div class="card-symbol" style="color:var(--cyber-cyan);">🛡️</div>
          <div class="card-title" style="color:var(--cyber-cyan);">WIE_Core_Values.doc</div>
        </div>'''

new_matrix_p3 = '''        <div class="tactical-card" id="card-clearance" onclick="openModal('modal-clearance')" onmouseenter="tacticalSound.playHoverBlip()" style="border-color:rgba(0,240,255,0.4);">
          <span class="card-tag" style="color:var(--cyber-cyan);">STAGE 11</span>
          <div class="card-symbol" style="color:var(--cyber-cyan);">🔢</div>
          <div class="card-title" style="color:var(--cyber-cyan);">CLEARANCE_CODE.txt</div>
        </div>'''

text = text.replace(old_matrix_p3, new_matrix_p3)

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated legacy icon-matrix cards!")
