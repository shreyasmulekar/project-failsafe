import re
import json

def update_admin():
    with open("admin.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Master Keys Modal
    old_master_keys_pattern = r'<div id="modal-master-keys" class="modal-backdrop">[\s\S]*?<!-- Audit Log Modal -->'
    new_master_keys = '''<div id="modal-master-keys" class="modal-backdrop">
    <div class="modal-box" style="max-width:760px; width:95%;">
      <div class="modal-header">
        <span style="font-size:15px; font-weight:bold; color:var(--cyber-cyan); letter-spacing:1px;">🔑 MASTER PASSWORDS &amp; SOLUTIONS // OPERATION FAILSAFE</span>
        <button class="modal-close" onclick="closeModal('modal-master-keys')">✕</button>
      </div>
      
      <div style="max-height:480px; overflow-y:auto; padding-right:6px; font-family:var(--font-mono); font-size:11.5px; display:flex; flex-direction:column; gap:12px;">
        <div style="background:rgba(0,240,255,0.08); border-left:3px solid var(--cyber-cyan); padding:8px 12px; font-weight:bold; color:var(--cyber-cyan);">
          ROUND 1: THE LAB RESCUE &amp; ISHAAN PURGE (11 CURATED STORYLINE STAGES)
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <div class="audit-entry"><span>Stage 01: ISHAAN Recovery Terminal (01_TERMINAL)</span><strong style="color:var(--tactical-green);">ACCESS</strong></div>
          <div class="audit-entry"><span>Stage 02: ISHAAN's Memory Core — 6 fragments chronologically (4:17 PM → 10:15 PM)</span><strong style="color:var(--tactical-green);">123456</strong></div>
          <div class="audit-entry"><span>Stage 03: The Simple Acrostic Note (Aditi_Memo.doc) — First letter of 4 sentences</span><strong style="color:var(--tactical-green);">SAFE</strong></div>
          <div class="audit-entry"><span>Stage 04: The Calendar Anomaly (Incident_Logs.doc) — 2025 is NOT a leap year</span><strong style="color:var(--tactical-green);">28/02/2025</strong></div>
          <div class="audit-entry"><span>Stage 05: Clearance Elevation (Clearance_Code.txt) — A1Z26: 16-15-12-01-18-09-19</span><strong style="color:var(--tactical-green);">POLARIS</strong></div>
          <div class="audit-entry"><span>Stage 06: Margin Diagnostics (System_Diagnostics.doc) — Resolved comments</span><strong style="color:var(--tactical-green);">MARGIN_KEY (or 22:46)</strong></div>
          <div class="audit-entry"><span>Stage 07: Font Style Verification (AUTHENTIC_LOG.doc) — Dr. Aditi's authentic font</span><strong style="color:var(--tactical-green);">ARIAL</strong></div>
          <div class="audit-entry"><span>Stage 08: Morse Audio Transmission (audio_log_07.mp3) — .-- .... .. - .</span><strong style="color:var(--tactical-green);">WHITE</strong></div>
          <div class="audit-entry"><span>Stage 09: Git Reflog Version Scrub (Incident_Report.doc) — Commit 7b8a1c9</span><strong style="color:var(--tactical-green);">OVERRIDE FAILED</strong></div>
          <div class="audit-entry"><span>Stage 10: Psychological Honeypot Trap (DO_NOT_RUN.exe) — Type BYPASS in shell</span><strong style="color:var(--hazard-amber);">BYPASS (Do NOT run exe)</strong></div>
          <div class="audit-entry"><span>Stage 11: Master IEEE WIE Failsafe — Wisdom(6) + Integrity(9) + Empowerment(11)</span><strong style="color:var(--tactical-green);">6-9-11</strong></div>
        </div>

        <div style="background:rgba(255,176,0,0.1); border-left:3px solid var(--hazard-amber); padding:8px 12px; font-weight:bold; color:var(--hazard-amber); margin-top:8px;">
          ROUND 2: OPERATION OLYMPUS — ORBITAL COUNTERMEASURE (9 STRATCOM STAGES)
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <div class="audit-entry"><span>Puzzle 01: StratCom Terminal Uplink (Network Handshake)</span><strong style="color:var(--tactical-green);">ORBITAL_SYN</strong></div>
          <div class="audit-entry"><span>Puzzle 02: Orbital Frequency Triangulation (Hydrogen Line)</span><strong style="color:var(--tactical-green);">1420.405</strong></div>
          <div class="audit-entry"><span>Puzzle 03: Satellite Logic Gate Array (NAND/NOR Circuit)</span><strong style="color:var(--tactical-green);">GATE_ALPHA_ONLINE</strong></div>
          <div class="audit-entry"><span>Puzzle 04: Memory Buffer Overrun Defusal (Hex Address)</span><strong style="color:var(--tactical-green);">0xDEADBEEF</strong></div>
          <div class="audit-entry"><span>Puzzle 05: Sensor Matrix Spectrogram (Spectral Peak)</span><strong style="color:var(--tactical-green);">APOGEE_LOCK</strong></div>
          <div class="audit-entry"><span>Puzzle 06: Quantum Key Distribution Protocol (Entanglement State)</span><strong style="color:var(--tactical-green);">QKD_ENTANGLED</strong></div>
          <div class="audit-entry"><span>Puzzle 07: Star Tracker Telemetry Matrix (Navigation Fix)</span><strong style="color:var(--tactical-green);">CASSIOPEIA_31</strong></div>
          <div class="audit-entry"><span>Puzzle 08: Firmware Decryption Keyring (Aegis Decrypt)</span><strong style="color:var(--tactical-green);">AEGIS_SHIELD_V4</strong></div>
          <div class="audit-entry"><span>Puzzle 09: Master Orbital Failsafe Purge (Terminal Command)</span><strong style="color:var(--tactical-green);">failsafe_olympus_prime_purge()</strong></div>
        </div>
      </div>

      <div style="display:flex; justify-content:flex-end; margin-top:12px; border-top:1px solid var(--border-subtle); padding-top:10px;">
        <button class="btn-action" onclick="closeModal('modal-master-keys')">CLOSE</button>
      </div>
    </div>
  </div>

  <!-- Audit Log Modal -->'''
    content = re.sub(old_master_keys_pattern, new_master_keys, content, count=1)
    print("Updated Master Keys Modal")

    # 2. Add Edit Team Modal and Telemetry Modal before Puzzle Times modal
    modals_to_add = '''
  <!-- Edit / Manipulate Team Modal -->
  <div id="modal-edit-team" class="modal-backdrop">
    <div class="modal-box" style="max-width: 620px; width: 95%;">
      <div class="modal-header">
        <span style="font-size:15px; font-weight:bold; color:var(--cyber-cyan); letter-spacing:1px;">✏️ EDIT &amp; MANIPULATE TEAM PARAMETERS</span>
        <button class="modal-close" onclick="closeModal('modal-edit-team')">✕</button>
      </div>
      <p style="font-size:11.5px; color:var(--text-dim); margin-bottom:14px; line-height:1.5;">
        Override live team progression, stage allocation, penalty counts, or assign Round 2 participation directly.
      </p>

      <form id="edit-team-form" onsubmit="submitTeamEdit(event)" style="display:flex; flex-direction:column; gap:12px; font-family:var(--font-mono); font-size:12px;">
        <input type="hidden" id="edit-team-id">

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
          <div>
            <label style="color:var(--text-muted); font-size:10px;">TEAM IDENTIFIER:</label>
            <input type="text" id="edit-team-id-display" readonly style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:var(--cyber-cyan); font-weight:bold; border-radius:3px; outline:none;">
          </div>
          <div>
            <label style="color:var(--text-muted); font-size:10px;">PASSWORD:</label>
            <input type="text" id="edit-team-password" required style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px; outline:none;">
          </div>
        </div>

        <div>
          <label style="color:var(--text-muted); font-size:10px;">TEAM NAME:</label>
          <input type="text" id="edit-team-name" required style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px; outline:none;">
        </div>

        <div>
          <label style="color:var(--text-muted); font-size:10px;">MEMBERS (COMMA SEPARATED):</label>
          <input type="text" id="edit-team-members" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px; outline:none;">
        </div>

        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px; background:rgba(0,240,255,0.04); padding:10px; border-radius:4px; border:1px solid var(--border-subtle);">
          <div>
            <label style="color:var(--text-muted); font-size:10px;">ACTIVE ROUND:</label>
            <select id="edit-team-round" style="width:100%; padding:8px; background:#070d14; border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
              <option value="1">Round 1 (Lab)</option>
              <option value="2">Round 2 (StratCom)</option>
            </select>
          </div>
          <div>
            <label style="color:var(--text-muted); font-size:10px;">ROUND 1 STAGE (1-11):</label>
            <input type="number" id="edit-team-stage" min="1" max="11" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
          </div>
          <div>
            <label style="color:var(--text-muted); font-size:10px;">ROUND 2 STAGE (1-9):</label>
            <input type="number" id="edit-team-r2-stage" min="1" max="9" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
          </div>
        </div>

        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px;">
          <div>
            <label style="color:var(--text-muted); font-size:10px;">HINTS TAKEN (+2m ea):</label>
            <input type="number" id="edit-team-hints" min="0" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
          </div>
          <div>
            <label style="color:var(--text-muted); font-size:10px;">TRAPS TRIGGERED (+5m ea):</label>
            <input type="number" id="edit-team-traps" min="0" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
          </div>
          <div>
            <label style="color:var(--text-muted); font-size:10px;">TIME ADJUST (SEC):</label>
            <input type="number" id="edit-team-time-adj" style="width:100%; padding:8px; background:rgba(0,0,0,0.6); border:1px solid var(--border-subtle); color:#fff; border-radius:3px;">
          </div>
        </div>

        <div style="display:flex; gap:20px; align-items:center; margin-top:4px;">
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
            <input type="checkbox" id="edit-team-finished">
            <span style="color:var(--tactical-green); font-size:11px;">Mark Round 1 Finished / Liberated</span>
          </label>
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
            <input type="checkbox" id="edit-team-r2-finished">
            <span style="color:var(--hazard-amber); font-size:11px;">Mark Round 2 Complete (Podium)</span>
          </label>
        </div>

        <div id="edit-team-error" style="color:var(--combat-red); font-size:11px; min-height:16px;"></div>

        <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:10px; border-top:1px solid var(--border-subtle); padding-top:12px;">
          <button type="button" class="btn-action" onclick="closeModal('modal-edit-team')">CANCEL</button>
          <button type="submit" class="btn-action success">💾 SAVE CHANGES</button>
        </div>
      </form>
    </div>
  </div>

  <!-- Detailed Participant Telemetry Modal -->
  <div id="modal-team-telemetry" class="modal-backdrop">
    <div class="modal-box" style="max-width: 820px; width: 95%;">
      <div class="modal-header">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:15px; font-weight:bold; color:var(--cyber-cyan); letter-spacing:1px;">🔍 PARTICIPANT WORKSTATION TELEMETRY</span>
          <span id="telem-team-badge" class="badge-organizer">TEAM-01</span>
        </div>
        <button class="modal-close" onclick="closeModal('modal-team-telemetry')">✕</button>
      </div>

      <div style="max-height: 520px; overflow-y:auto; padding-right:6px; display:flex; flex-direction:column; gap:14px; font-family:var(--font-mono);">
        
        <!-- Hardware & Client Environment -->
        <div style="background:rgba(0,240,255,0.05); border:1px solid var(--border-subtle); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:var(--cyber-cyan); font-weight:bold; margin-bottom:8px; letter-spacing:0.8px;">
            💻 HARDWARE &amp; CLIENT ENVIRONMENT
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:10px; font-size:11px;">
            <div><span style="color:var(--text-muted);">Screen Resolution:</span> <span id="telem-resolution" style="color:#fff; font-weight:bold;">1920x1080</span></div>
            <div><span style="color:var(--text-muted);">OS / Platform:</span> <span id="telem-os" style="color:#fff; font-weight:bold;">Windows 11</span></div>
            <div><span style="color:var(--text-muted);">Fullscreen Active:</span> <span id="telem-fullscreen" style="color:var(--tactical-green); font-weight:bold;">YES</span></div>
            <div><span style="color:var(--text-muted);">Current Active View:</span> <span id="telem-active-view" style="color:var(--hazard-amber); font-weight:bold;">STAGE_06_DOC</span></div>
            <div><span style="color:var(--text-muted);">Network Latency / Seen:</span> <span id="telem-latency" style="color:#fff;">Active (2s ago)</span></div>
            <div><span style="color:var(--text-muted);">Station Status:</span> <span id="telem-status" style="color:var(--tactical-green); font-weight:bold;">UNLOCKED</span></div>
          </div>
        </div>

        <!-- Tamper & Integrity Violations History -->
        <div style="background:rgba(255,0,60,0.05); border:1px solid rgba(255,0,60,0.25); border-radius:6px; padding:12px 16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <div style="font-size:11px; color:var(--combat-red); font-weight:bold; letter-spacing:0.8px;">
              🚨 PROCTOR INTEGRITY &amp; BREACH CHRONICLE
            </div>
            <div id="telem-breach-total" style="font-size:11px; font-weight:bold; color:var(--combat-red);">0 BREACHES DETECTED</div>
          </div>
          <div id="telem-breaches-list" style="max-height:140px; overflow-y:auto; font-size:10.5px; display:flex; flex-direction:column; gap:4px;">
            <!-- Dynamically populated -->
          </div>
        </div>

        <!-- Per-Stage Solve Times -->
        <div style="background:rgba(0,240,255,0.05); border:1px solid var(--border-subtle); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:var(--cyber-cyan); font-weight:bold; margin-bottom:8px; letter-spacing:0.8px;">
            ⏱️ STAGE SOLVE DURATION TABLE
          </div>
          <div id="telem-stages-table" style="font-size:11px;">
            <!-- Dynamically populated -->
          </div>
        </div>

        <!-- Live Action Stream -->
        <div style="background:rgba(0,0,0,0.4); border:1px solid var(--border-subtle); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:var(--text-muted); font-weight:bold; margin-bottom:6px; letter-spacing:0.8px;">
            📜 RECENT ACTIVITY LOG
          </div>
          <div id="telem-activity-stream" style="font-size:11px; color:var(--text-dim); line-height:1.6;">
            <!-- Dynamically populated -->
          </div>
        </div>

      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; border-top:1px solid var(--border-subtle); padding-top:10px;">
        <span style="font-size:10.5px; color:var(--text-muted); font-family:var(--font-mono);">Real-time telemetry stream synchronized via WebSocket / HTTP Polling.</span>
        <button class="btn-action" onclick="closeModal('modal-team-telemetry')">CLOSE</button>
      </div>
    </div>
  </div>
'''

    if 'id="modal-edit-team"' not in content:
        puzzle_marker = '<!-- Puzzle Times Breakdown Modal -->'
        content = content.replace(puzzle_marker, modals_to_add + "\n  " + puzzle_marker)
        print("Added modal-edit-team and modal-team-telemetry")

    # 3. Update renderTeamsTable to add [ ✏️ EDIT ], [ 🔍 TELEMETRY ], [ 🗑️ DELETE ]
    old_actions = '''<button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')" title="View per-puzzle solve times">⏱️ TIMES</button>
                ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')" title="Unlock station">🔓 UNLOCK</button>` : ''}
                <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')" title="Force logout workstation">🚪 LOGOUT</button>
                <button class="btn-table danger" onclick="remoteResetTeam('${escapeHtml(t.team_id)}')" title="Reset workstation to Stage 01">🔄 RESET</button>
                <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜 AUDIT</button>'''

    new_actions = '''<button class="btn-table" onclick="showTeamTelemetry('${escapeHtml(t.team_id)}')" title="View detailed participant telemetry" style="border-color:var(--cyber-cyan); color:var(--cyber-cyan);">🔍 TELEMETRY</button>
                <button class="btn-table" onclick="openEditTeamModal('${escapeHtml(t.team_id)}')" title="Edit team parameters" style="border-color:var(--tactical-green); color:var(--tactical-green);">✏️ EDIT</button>
                <button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')" title="View per-puzzle solve times">⏱️ TIMES</button>
                ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')" title="Unlock station">🔓 UNLOCK</button>` : ''}
                <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')" title="Force logout workstation">🚪 LOGOUT</button>
                <button class="btn-table danger" onclick="remoteResetTeam('${escapeHtml(t.team_id)}')" title="Reset workstation to Stage 01">🔄 RESET</button>
                <button class="btn-table danger" onclick="promptDeleteTeam('${escapeHtml(t.team_id)}')" title="Permanently delete team" style="background:rgba(255,0,60,0.15); border-color:var(--combat-red); color:var(--combat-red);">🗑️ DELETE</button>
                <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜 AUDIT</button>'''

    if old_actions in content:
        content = content.replace(old_actions, new_actions)
        print("Updated table actions in renderTeamsTable")

    # 4. Update station grid actions in renderStationGrid
    old_grid_actions = '''<div class="station-card-actions">
              <button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')">⏱️ TIMES</button>
              ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')">🔓</button>` : ''}
              <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')">🚪 LOGOUT</button>
              <button class="btn-table danger" onclick="remoteResetTeam('${escapeHtml(t.team_id)}')">🔄 RESET</button>
              <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜 AUDIT</button>
            </div>'''

    new_grid_actions = '''<div class="station-card-actions">
              <button class="btn-table" onclick="showTeamTelemetry('${escapeHtml(t.team_id)}')">🔍</button>
              <button class="btn-table" onclick="openEditTeamModal('${escapeHtml(t.team_id)}')">✏️</button>
              <button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')">⏱️</button>
              ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')">🔓</button>` : ''}
              <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')">🚪</button>
              <button class="btn-table danger" onclick="remoteResetTeam('${escapeHtml(t.team_id)}')">🔄</button>
              <button class="btn-table danger" onclick="promptDeleteTeam('${escapeHtml(t.team_id)}')">🗑️</button>
              <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜</button>
            </div>'''

    if old_grid_actions in content:
        content = content.replace(old_grid_actions, new_grid_actions)
        print("Updated grid actions in renderStationGrid")

    # 5. Add JavaScript functions for edit, delete, and telemetry
    js_to_add = '''
    // --- TEAM EDIT & MANIPULATION FUNCTIONS ---
    function openEditTeamModal(teamId) {
      const team = cachedTeams.find(t => t.team_id === teamId);
      if (!team) return;

      document.getElementById('edit-team-id').value = team.team_id;
      document.getElementById('edit-team-id-display').value = team.team_id;
      document.getElementById('edit-team-password').value = team.password || '';
      document.getElementById('edit-team-name').value = team.team_name || '';
      document.getElementById('edit-team-members').value = team.members || '';
      document.getElementById('edit-team-round').value = team.current_round || 1;
      document.getElementById('edit-team-stage').value = team.current_stage || 1;
      document.getElementById('edit-team-r2-stage').value = team.round_2_stage || 1;
      document.getElementById('edit-team-hints').value = team.hints_count || 0;
      document.getElementById('edit-team-traps').value = team.traps_count || 0;
      document.getElementById('edit-team-time-adj').value = team.time_adjustment_sec || 0;
      document.getElementById('edit-team-finished').checked = !!team.is_finished;
      document.getElementById('edit-team-r2-finished').checked = !!team.round_2_is_finished;
      document.getElementById('edit-team-error').textContent = '';

      openModal('modal-edit-team');
    }

    async function submitTeamEdit(e) {
      e.preventDefault();
      const teamId = document.getElementById('edit-team-id').value;
      const errorEl = document.getElementById('edit-team-error');
      errorEl.textContent = '';

      const payload = {
        admin_pin: sessionStorage.getItem('admin_pin') || ADMIN_PIN,
        team_id: teamId,
        team_name: document.getElementById('edit-team-name').value.trim(),
        password: document.getElementById('edit-team-password').value.trim(),
        members: document.getElementById('edit-team-members').value.trim(),
        current_round: parseInt(document.getElementById('edit-team-round').value) || 1,
        current_stage: parseInt(document.getElementById('edit-team-stage').value) || 1,
        round_2_stage: parseInt(document.getElementById('edit-team-r2-stage').value) || 1,
        hints_count: parseInt(document.getElementById('edit-team-hints').value) || 0,
        traps_count: parseInt(document.getElementById('edit-team-traps').value) || 0,
        time_adjustment_sec: parseInt(document.getElementById('edit-team-time-adj').value) || 0,
        is_finished: document.getElementById('edit-team-finished').checked,
        round_2_is_finished: document.getElementById('edit-team-r2-finished').checked
      };

      try {
        const res = await fetch(`${getApiBase()}/api/admin/teams/edit`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (res.ok && data.success) {
          closeModal('modal-edit-team');
          fetchLeaderboardData();
        } else {
          errorEl.textContent = data.error || 'Failed to update team';
        }
      } catch (err) {
        errorEl.textContent = 'Server connection error: ' + err.message;
      }
    }

    async function promptDeleteTeam(teamId) {
      const team = cachedTeams.find(t => t.team_id === teamId);
      const name = team ? team.team_name : teamId;
      if (!confirm(`⚠️ PERMANENT TEAM REMOVAL ⚠️\\n\\nAre you sure you want to permanently delete team ${teamId} ("${name}") from the tournament ledger?\\n\\nThis action cannot be undone.`)) {
        return;
      }

      try {
        const res = await fetch(`${getApiBase()}/api/admin/teams/delete`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            admin_pin: sessionStorage.getItem('admin_pin') || ADMIN_PIN,
            team_id: teamId
          })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          fetchLeaderboardData();
        } else {
          alert('Error deleting team: ' + (data.error || 'Unknown failure'));
        }
      } catch (err) {
        alert('Server communication error: ' + err.message);
      }
    }

    // --- DETAILED PARTICIPANT TELEMETRY INSPECTOR ---
    function showTeamTelemetry(teamId) {
      const team = cachedTeams.find(t => t.team_id === teamId);
      if (!team) return;

      document.getElementById('telem-team-badge').textContent = `${team.team_id} — ${team.team_name}`;
      
      const clientInfo = team.client_info || {};
      document.getElementById('telem-resolution').textContent = clientInfo.resolution || `${screen.width}x${screen.height} (Standard)`;
      document.getElementById('telem-os').textContent = clientInfo.os || navigator.platform || 'Windows (x64)';
      
      const isFs = clientInfo.fullscreen !== undefined ? clientInfo.fullscreen : true;
      document.getElementById('telem-fullscreen').textContent = isFs ? 'YES (Proctored)' : 'NO (Violating)';
      document.getElementById('telem-fullscreen').style.color = isFs ? 'var(--tactical-green)' : 'var(--combat-red)';

      document.getElementById('telem-active-view').textContent = team.active_view || (team.is_finished ? 'VICTORY_SCREEN' : `STAGE_${team.current_stage}`);
      document.getElementById('telem-latency').textContent = team.is_online ? `Online (${team.last_seen_sec_ago}s ago)` : `Offline (${Math.floor(team.last_seen_sec_ago/60)}m ago)`;
      document.getElementById('telem-status').textContent = team.is_locked ? '🚨 LOCKED (TAMPER)' : (team.is_finished ? '🏆 LIBERATED' : 'ACTIVE IN RUN');
      document.getElementById('telem-status').style.color = team.is_locked ? 'var(--combat-red)' : (team.is_finished ? 'var(--cyber-cyan)' : 'var(--tactical-green)');

      // Violations History
      const breachListEl = document.getElementById('telem-breaches-list');
      const vHistory = team.violations_history || [];
      const totalBreaches = team.tamper_incidents || vHistory.length;
      document.getElementById('telem-breach-total').textContent = `${totalBreaches} BREACH${totalBreaches === 1 ? '' : 'ES'} RECORDED`;

      if (vHistory.length === 0 && totalBreaches === 0) {
        breachListEl.innerHTML = '<div style="color:var(--tactical-green); padding:6px 0;">✓ Clean station record. No proctoring or fullscreen breaches recorded.</div>';
      } else {
        let bHtml = '';
        if (vHistory.length > 0) {
          vHistory.slice().reverse().forEach(v => {
            bHtml += `<div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,0,60,0.15); padding:4px 0;">
              <span style="color:var(--combat-red);">🚨 ${escapeHtml(v.type || 'Integrity Violation')}</span>
              <span style="color:var(--text-muted);">${escapeHtml(v.timestamp || '')}</span>
            </div>`;
          });
        } else {
          bHtml = `<div style="color:var(--hazard-amber);">⚠️ ${totalBreaches} tamper incident(s) logged by proctor guard.</div>`;
        }
        breachListEl.innerHTML = bHtml;
      }

      // Stage solve times table
      const stEl = document.getElementById('telem-stages-table');
      const times = team.stage_times || {};
      const stageKeys = Object.keys(times);
      if (stageKeys.length === 0) {
        stEl.innerHTML = '<div style="color:var(--text-muted);">No stage solve times recorded yet.</div>';
      } else {
        let tTable = '<div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap:6px;">';
        stageKeys.forEach(k => {
          const sec = times[k];
          const m = Math.floor(sec / 60);
          const s = sec % 60;
          tTable += `<div style="background:rgba(0,0,0,0.4); border:1px solid var(--border-subtle); padding:6px 8px; border-radius:3px;">
            <div style="color:var(--text-muted); font-size:10px;">STAGE ${k}</div>
            <div style="color:var(--cyber-cyan); font-weight:bold;">${m}m ${s.toString().padStart(2, '0')}s</div>
          </div>`;
        });
        tTable += '</div>';
        stEl.innerHTML = tTable;
      }

      // Activity Stream
      document.getElementById('telem-activity-stream').innerHTML = `
        <div><strong>Current Activity:</strong> ${escapeHtml(team.last_action || 'Idle')}</div>
        <div style="margin-top:4px;"><strong>Penalty Breakdown:</strong> Hints Taken: ${team.hints_count || 0} (+${(team.hints_count||0)*2}m) | Honeypot Traps: ${team.traps_count || 0} (+${(team.traps_count||0)*5}m)</div>
        <div style="margin-top:4px;"><strong>Score / Adjusted Time:</strong> ${Math.floor(team.adjusted_time_sec / 60)}m ${team.adjusted_time_sec % 60}s</div>
      `;

      openModal('modal-team-telemetry');
    }
'''

    if 'function openEditTeamModal' not in content:
        insert_marker = 'function showTeamPuzzleTimes(teamId) {'
        content = content.replace(insert_marker, js_to_add + "\n    " + insert_marker)
        print("Added JS functions for edit, delete, and telemetry")

    with open("admin.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("admin.html updated successfully!")

if __name__ == '__main__':
    update_admin()
