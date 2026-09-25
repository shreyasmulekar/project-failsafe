import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

card_16_block = '''        <!-- Stage 16 -->
        <div class="nexus-clean-card" id="card-frequency" data-act="act5" onclick="openModal('modal-frequency')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 16</span>
            <span style="font-size:10px; color:#00f0ff;">● FREQUENCY</span>
          </div>
          <div class="nexus-card-icon">📊</div>
          <div class="nexus-card-name">Mass_System_Log.txt</div>
          <div class="nexus-card-status">Ctrl+F Word Count x 100 &rarr;</div>
        </div>'''

new_cards_16_to_21 = '''        <!-- Stage 16 -->
        <div class="nexus-clean-card" id="card-frequency" data-act="act5" onclick="openModal('modal-frequency')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 16</span>
            <span style="font-size:10px; color:#00f0ff;">● FREQUENCY</span>
          </div>
          <div class="nexus-card-icon">📊</div>
          <div class="nexus-card-name">Mass_System_Log.txt</div>
          <div class="nexus-card-status">Ctrl+F Word Count x 100 &rarr;</div>
        </div>

        <!-- Stage 17 -->
        <div class="nexus-clean-card" id="card-polybius-shift" data-act="act6" onclick="openModal('modal-polybius-shift')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 17</span>
            <span style="font-size:10px; color:#00f0ff;">● POLYBIUS SHIFT</span>
          </div>
          <div class="nexus-card-icon">📡</div>
          <div class="nexus-card-name">Intercepted_ADI_Transmission.pdf</div>
          <div class="nexus-card-status">Vector Shift (+1, -1) &rarr;</div>
        </div>

        <!-- Stage 18 -->
        <div class="nexus-clean-card" id="card-clock-loop" data-act="act6" onclick="openModal('modal-clock-loop')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 18</span>
            <span style="font-size:10px; color:#00f0ff;">● MODULAR LOOP</span>
          </div>
          <div class="nexus-card-icon">⏱️</div>
          <div class="nexus-card-name">Cycle_Diagnostics.png</div>
          <div class="nexus-card-status">12-Point Clock Jump &rarr;</div>
        </div>

        <!-- Stage 19 -->
        <div class="nexus-clean-card" id="card-status-check" data-act="act6" onclick="openModal('modal-status-check')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 19</span>
            <span style="font-size:10px; color:#00f0ff;">● CHECKLIST</span>
          </div>
          <div class="nexus-card-icon">📋</div>
          <div class="nexus-card-name">Server_Status_Check.pdf</div>
          <div class="nexus-card-status">Overheating Node Outlier &rarr;</div>
        </div>

        <!-- Stage 20 -->
        <div class="nexus-clean-card" id="card-shift-matrix" data-act="act6" onclick="openModal('modal-shift-matrix')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00f0ff;">STAGE 20</span>
            <span style="font-size:10px; color:#00f0ff;">● SHIFT CIPHER</span>
          </div>
          <div class="nexus-card-icon">🔑</div>
          <div class="nexus-card-name">Emergency_Override_Key.txt</div>
          <div class="nexus-card-status">Day-of-Week Caesar Shift &rarr;</div>
        </div>

        <!-- Stage 21 -->
        <div class="nexus-clean-card" id="card-audit-timeline" data-act="act6" onclick="openModal('modal-audit-timeline')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#00ff88; border-color:#00ff88;">STAGE 21</span>
            <span style="font-size:10px; color:#00ff88;">🏆 R1 FINALE</span>
          </div>
          <div class="nexus-card-icon" style="color:#00ff88;">📜</div>
          <div class="nexus-card-name">System_Audit_2013.log</div>
          <div class="nexus-card-status">Timeline Inversion Audit &rarr;</div>
        </div>'''

if card_16_block in html:
    html = html.replace(card_16_block, new_cards_16_to_21)
    print("Nexus cards grid updated with Stages 17..21")
else:
    print("Warning: card_16_block not found exactly!")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)
