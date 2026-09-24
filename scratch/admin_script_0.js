
    const ADMIN_PIN = "wie-admin-2026";

    function isAdminAuthenticated() {
      return sessionStorage.getItem("failsafe_admin_authenticated") === "true";
    }

    function checkAdminAuthOnLoad() {
      const modal = document.getElementById("admin-login-modal");
      if (isAdminAuthenticated()) {
        if (modal) modal.style.display = "none";
        fetchLeaderboardData();
      } else {
        if (modal) {
          modal.style.display = "flex";
          const input = document.getElementById("admin-auth-pin");
          if (input) setTimeout(() => input.focus(), 200);
        }
      }
    }

    async function handleAdminLogin(e) {
      if (e) e.preventDefault();
      const input = document.getElementById("admin-auth-pin");
      const errEl = document.getElementById("admin-login-error");
      const pin = input ? input.value.trim() : "";
      if (!pin) return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/leaderboard?pin=${encodeURIComponent(pin)}`);
        if (res.ok) {
          sessionStorage.setItem("failsafe_admin_authenticated", "true");
          const modal = document.getElementById("admin-login-modal");
          if (modal) modal.style.display = "none";
          if (errEl) errEl.innerText = "";
          fetchLeaderboardData();
          return;
        }
      } catch(err) {}

      if (pin === ADMIN_PIN) {
        sessionStorage.setItem("failsafe_admin_authenticated", "true");
        const modal = document.getElementById("admin-login-modal");
        if (modal) modal.style.display = "none";
        if (errEl) errEl.innerText = "";
        fetchLeaderboardData();
        return;
      }

      if (errEl) errEl.innerText = "ACCESS DENIED: Invalid Organizer PIN.";
      if (input) {
        input.classList.add("pin-shake");
        setTimeout(() => input.classList.remove("pin-shake"), 500);
      }
    }

    function handleAdminLogout() {
      sessionStorage.removeItem("failsafe_admin_authenticated");
      const modal = document.getElementById("admin-login-modal");
      if (modal) {
        modal.style.display = "flex";
        const input = document.getElementById("admin-auth-pin");
        if (input) {
          input.value = "";
          input.focus();
        }
      }
    }

    function toggleAdminPinVisibility() {
      const input = document.getElementById("admin-auth-pin");
      if (input) input.type = input.type === "password" ? "text" : "password";
    }

    function getApiBase() {
      const custom = localStorage.getItem("failsafe_server_url");
      if (custom && custom.trim()) return custom.trim().replace(/\/+$/, '');
      if (window.location.protocol.startsWith("http") && window.location.origin && window.location.origin !== "null") {
        return window.location.origin;
      }
      return "http://localhost:8000";
    }
    let API_BASE = getApiBase();
    let cachedTeams = [];
    let currentFilter = "ALL";
    let revealedPasswords = new Set();
    let isServerOnline = false;

    // Clock
    setInterval(() => {
      const now = new Date();
      document.getElementById('clock-zulu').innerText = now.toISOString().substring(11, 19) + 'Z';
    }, 1000);

    async function checkServerStatus() {
      API_BASE = getApiBase();
      const label = document.getElementById('server-status-label');
      const offlineBanner = document.getElementById('server-offline-banner');
      const onlineBanner = document.getElementById('server-online-banner');
      const urlDisplay = document.getElementById('server-lan-url-display');

      try {
        const res = await fetch(`${API_BASE}/api/status`);
        if (res.ok) {
          const data = await res.json();
          isServerOnline = true;
          if (label) {
            label.innerText = `ONLINE (${data.lan_ip || 'PORT 8000'}:${data.port || 8000})`;
            label.style.color = "var(--tactical-green)";
          }
          if (offlineBanner) offlineBanner.style.display = "none";
          if (onlineBanner) {
            onlineBanner.style.display = "flex";
            if (urlDisplay && data.server_url) {
              urlDisplay.innerText = data.server_url;
            }
          }
          return true;
        }
      } catch(e) {}
      
      isServerOnline = false;
      if (label) {
        label.innerText = "OFFLINE (PORT 8000)";
        label.style.color = "var(--neon-red)";
      }
      if (offlineBanner) offlineBanner.style.display = "block";
      if (onlineBanner) onlineBanner.style.display = "none";
      return false;
    }

    function copyServerLanUrl() {
      const url = document.getElementById("server-lan-url-display").innerText;
      navigator.clipboard.writeText(url).then(() => {
        alert(`📋 COPIED TOURNAMENT SERVER URL:\n\n${url}\n\nEnter this URL on participant stations so their scores appear live!`);
      }).catch(() => {
        prompt("Tournament Server URL (copy below):", url);
      });
    }

    function openServerConfigModal() {
      const cur = getApiBase();
      const next = prompt("Enter Tournament Server URL or IP (e.g. http://192.168.1.15:8000):", cur);
      if (next !== null && next.trim()) {
        localStorage.setItem("failsafe_server_url", next.trim().replace(/\/+$/, ''));
        API_BASE = getApiBase();
        fetchLeaderboardData();
      }
    }

    let alertedBreachKeys = new Set();
    function playOrganizerBreachAlert() {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = "sawtooth";
        osc.frequency.setValueAtTime(880, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(440, ctx.currentTime + 0.35);
        gain.gain.setValueAtTime(0.25, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.35);
      } catch(e) {}
    }

    function checkAndAlertBreaches(teams) {
      let newBreachFound = false;
      teams.forEach(t => {
        const act = t.last_action || '';
        if (act.includes("Google") || act.includes("Lens") || act.includes("Right-Click") || act.includes("Fullscreen") || act.includes("Esc") || act.includes("Focus") || act.includes("Alt-Tab") || act.includes("Windows Key")) {
          const key = `${t.team_id}_${act}`;
          if (!alertedBreachKeys.has(key)) {
            alertedBreachKeys.add(key);
            newBreachFound = true;
          }
        }
      });
      if (newBreachFound) {
        playOrganizerBreachAlert();
      }
    }

    async function fetchLeaderboardData() {
      if (!isAdminAuthenticated()) return;
      await checkServerStatus();
      try {
        const res = await fetch(`${API_BASE}/api/admin/leaderboard?pin=${encodeURIComponent(ADMIN_PIN)}`);
        if (!res.ok) throw new Error("Server communication error");
        const data = await res.json();
        cachedTeams = data.leaderboard || [];
        checkAndAlertBreaches(cachedTeams);
        updateKpis(cachedTeams);
        if (currentViewMode === 'GRID') {
          renderStationGrid();
        } else {
          renderTeamsTable();
        }
      } catch (err) {
        console.error("Leaderboard fetch error:", err);
        // Fallback for single-machine standalone testing
        try {
          const rawLocal = localStorage.getItem("failsafe_auth_team");
          if (rawLocal && cachedTeams.length === 0) {
            const parsed = JSON.parse(rawLocal);
            cachedTeams = [{
              team_id: parsed.team_id,
              team_name: parsed.team_name || parsed.team_id,
              password: parsed.password || '',
              members: parsed.members || '',
              current_stage: parsed.current_stage || 1,
              stage_title: `Stage ${parsed.current_stage || 1}`,
              last_action: "Locally Active",
              last_seen_sec_ago: 0,
              is_online: true,
              is_finished: false,
              is_locked: false,
              tamper_incidents: 0,
              activity_log: []
            }];
            updateKpis(cachedTeams);
            if (currentViewMode === 'GRID') {
              renderStationGrid();
            } else {
              renderTeamsTable();
            }
          }
        } catch(e) {}
      }
    }

    function updateKpis(teams) {
      document.getElementById('kpi-total-teams').innerText = teams.length;
      document.getElementById('kpi-active-online').innerText = teams.filter(t => t.is_online).length;
      document.getElementById('kpi-breached-teams').innerText = teams.filter(t => t.is_locked || t.tamper_incidents > 0).length;
      document.getElementById('kpi-finished-teams').innerText = teams.filter(t => t.is_finished).length;
    }

    let currentViewMode = "TABLE";

    function setViewMode(mode) {
      currentViewMode = mode;
      const btnTable = document.getElementById('btn-view-table');
      const btnGrid = document.getElementById('btn-view-grid');
      const tableContainer = document.getElementById('table-container');
      const gridContainer = document.getElementById('station-grid-container');

      if (btnTable) btnTable.classList.toggle('active', mode === 'TABLE');
      if (btnGrid) btnGrid.classList.toggle('active', mode === 'GRID');
      if (tableContainer) tableContainer.style.display = (mode === 'TABLE') ? 'block' : 'none';
      if (gridContainer) gridContainer.style.display = (mode === 'GRID') ? 'grid' : 'none';

      if (mode === 'GRID') {
        renderStationGrid();
      } else {
        renderTeamsTable();
      }
    }

    function setFilter(filterType, element) {
      currentFilter = filterType;
      document.querySelectorAll('.filter-chips .chip').forEach(c => c.classList.remove('active'));
      if (element) element.classList.add('active');
      if (currentViewMode === 'GRID') {
        renderStationGrid();
      } else {
        renderTeamsTable();
      }
    }

    function filterTeams() {
      if (currentViewMode === 'GRID') {
        renderStationGrid();
      } else {
        renderTeamsTable();
      }
    }

    function togglePasswordVisibility(teamId) {
      if (revealedPasswords.has(teamId)) {
        revealedPasswords.delete(teamId);
      } else {
        revealedPasswords.add(teamId);
      }
      if (currentViewMode === 'GRID') {
        renderStationGrid();
      } else {
        renderTeamsTable();
      }
    }

    function renderTeamsTable() {
      const tbody = document.getElementById('teams-table-body');
      if (!tbody) return;
      const searchQuery = (document.getElementById('team-search-input').value || '').trim().toLowerCase();

      let filtered = cachedTeams.filter(t => {
        // Filter chips
        if (currentFilter === "ACTIVE" && !t.is_online) return false;
        if (currentFilter === "LOCKED" && (!t.is_locked && t.tamper_incidents === 0)) return false;
        if (currentFilter === "FINISHED" && !t.is_finished) return false;
        if (currentFilter === "OFFLINE" && t.is_online) return false;

        // Search text
        if (searchQuery) {
          const matchId = (t.team_id || '').toLowerCase().includes(searchQuery);
          const matchName = (t.team_name || '').toLowerCase().includes(searchQuery);
          const matchMem = (t.members || '').toLowerCase().includes(searchQuery);
          const matchStage = (t.stage_title || '').toLowerCase().includes(searchQuery);
          if (!matchId && !matchName && !matchMem && !matchStage) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding:30px; color:var(--text-muted); font-family:var(--font-mono);">No teams found matching current criteria.</td></tr>`;
        return;
      }

      let html = "";
      filtered.forEach((t, idx) => {
        const rank = idx + 1;
        let rankClass = "rank-cell";
        let rankSymbol = `#${rank}`;
        if (rank === 1) { rankClass += " rank-1"; rankSymbol = "🥇 1"; }
        else if (rank === 2) { rankClass += " rank-2"; rankSymbol = "🥈 2"; }
        else if (rank === 3) { rankClass += " rank-3"; rankSymbol = "🥉 3"; }

        // Password reveal
        const isPwRevealed = revealedPasswords.has(t.team_id);
        const pwDisplay = isPwRevealed ? (t.password || 'none') : '••••••••';
        const pwIcon = isPwRevealed ? '🙈' : '👁️';

        // Presence
        let presenceBadge = `<span class="pulse-green"></span> <span style="font-size:11px; color:var(--tactical-green);">Active now</span>`;
        if (!t.is_online) {
          presenceBadge = `<span class="pulse-red"></span> <span style="font-size:11px; color:var(--text-muted);">${Math.floor(t.last_seen_sec_ago / 60)}m ago</span>`;
        } else if (t.last_seen_sec_ago > 60) {
          presenceBadge = `<span class="pulse-amber"></span> <span style="font-size:11px; color:var(--hazard-amber);">${t.last_seen_sec_ago}s ago</span>`;
        }

        // Action ticker pulse
        let actionPulse = `<span class="pulse-green"></span>`;
        if (t.is_locked) {
          actionPulse = `<span class="pulse-red"></span>`;
        } else if (t.last_action && t.last_action.includes("Trap")) {
          actionPulse = `<span class="pulse-amber"></span>`;
        }

        // Format time
        const formatTime = (sec) => {
          const m = Math.floor(sec / 60);
          const s = sec % 60;
          return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        };

        const stageTitle = t.is_finished 
          ? `<span class="stage-badge finished">🏆 LIBERATED ${t.finish_time_str ? `[${escapeHtml(t.finish_time_str)}]` : ''}</span>`
          : `<span class="stage-badge">Stage ${t.current_stage.toString().padStart(2, '0')}: ${escapeHtml(t.stage_title)}</span>`;

        let specificBreachBadge = '';
        const act = (t.last_action || '');
        if (act.includes("Google") || act.includes("Lens") || act.includes("Right-Click")) {
          specificBreachBadge = `<div class="tamper-badge google-lens" style="margin-top:4px;">🔍 GOOGLE SEARCH DETECTED</div>`;
        } else if (act.includes("Fullscreen") || act.includes("Esc")) {
          specificBreachBadge = `<div class="tamper-badge fullscreen-exit" style="margin-top:4px;">🚨 FULLSCREEN EXITED</div>`;
        } else if (act.includes("Focus") || act.includes("Alt-Tab") || act.includes("Windows Key")) {
          specificBreachBadge = `<div class="tamper-badge focus-lost" style="margin-top:4px;">🚨 FOCUS LOST (ALT-TAB / WIN)</div>`;
        }

        const tamperCol = (t.tamper_incidents > 0 || t.is_locked || specificBreachBadge)
          ? `<div>
               <span class="tamper-badge">${t.is_locked ? '🚨 LOCKED' : '⚠️'} ${t.tamper_incidents || 1} Breach${(t.tamper_incidents || 1) > 1 ? 'es' : ''}</span>
               ${specificBreachBadge}
             </div>`
          : `<span style="font-size:11px; color:var(--text-muted); font-family:var(--font-mono);">0 (Clean)</span>`;

        html += `
          <tr>
            <td class="${rankClass}">${rankSymbol}</td>
            <td>
              <div class="team-meta">
                <div class="team-name">${escapeHtml(t.team_name)}</div>
                <div class="team-id-badge">[${escapeHtml(t.team_id)}]</div>
                <div class="team-members">${escapeHtml(t.members || 'No members listed')}</div>
              </div>
            </td>
            <td>
              <div class="password-cell">
                <span>${escapeHtml(pwDisplay)}</span>
                <button class="btn-toggle-pw" onclick="togglePasswordVisibility('${escapeHtml(t.team_id)}')" title="Toggle password visibility">${pwIcon}</button>
              </div>
            </td>
            <td>${stageTitle}</td>
            <td>
              <div class="action-ticker" title="${escapeHtml(t.last_action)}">
                ${actionPulse}
                <span>${escapeHtml(t.last_action)}</span>
              </div>
            </td>
            <td>${presenceBadge}</td>
            <td>${tamperCol}</td>
            <td>
              <div style="font-family:var(--font-mono); font-size:11px;">
                <div style="color:var(--text-dim);">Elapsed: ${formatTime(t.raw_time_sec)}</div>
                <div style="color:${t.hints_count > 0 || t.traps_count > 0 ? 'var(--hazard-amber)' : 'var(--text-muted)'};">
                  Penalties: +${(t.hints_count * 2) + (t.traps_count * 5)}m
                </div>
                <div style="font-weight:bold; color:var(--tactical-green); margin-top:2px;">
                  Score: ${formatTime(t.adjusted_time_sec)}
                </div>
              </div>
            </td>
            <td style="text-align:center;">
              <div style="display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
                <button class="btn-table" onclick="showTeamTelemetry('${escapeHtml(t.team_id)}')" title="View detailed participant telemetry" style="border-color:var(--cyber-cyan); color:var(--cyber-cyan);">🔍 TELEMETRY</button>
                <button class="btn-table" onclick="openEditTeamModal('${escapeHtml(t.team_id)}')" title="Edit team parameters" style="border-color:var(--tactical-green); color:var(--tactical-green);">✏️ EDIT</button>
                <button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')" title="View per-puzzle solve times">⏱️ TIMES</button>
                ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')" title="Unlock station">🔓 UNLOCK</button>` : ''}
                <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')" title="Force logout workstation">🚪 LOGOUT</button>
                <button class="btn-table danger" onclick="promptResetRoundTeam('${escapeHtml(t.team_id)}', 1)" title="Reset Round 1 to Stage 01 for this team">🔄 R1 RESET</button>
                <button class="btn-table warning" onclick="promptResetRoundTeam('${escapeHtml(t.team_id)}', 2)" title="Reset Round 2 to Puzzle 01 for this team" style="border-color:var(--hazard-amber); color:var(--hazard-amber);">🎯 R2 RESET</button>
                <button class="btn-table danger" onclick="promptDeleteTeam('${escapeHtml(t.team_id)}')" title="Permanently delete team" style="background:rgba(255,0,60,0.15); border-color:var(--combat-red); color:var(--combat-red);">🗑️ DELETE</button>
                <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜 AUDIT</button>
              </div>
            </td>
          </tr>
        `;
      });

      tbody.innerHTML = html;
    }

    function renderStationGrid() {
      const grid = document.getElementById('station-grid-container');
      if (!grid) return;
      const searchQuery = (document.getElementById('team-search-input').value || '').trim().toLowerCase();

      let filtered = cachedTeams.filter(t => {
        if (currentFilter === "ACTIVE" && !t.is_online) return false;
        if (currentFilter === "LOCKED" && (!t.is_locked && t.tamper_incidents === 0)) return false;
        if (currentFilter === "FINISHED" && !t.is_finished) return false;
        if (currentFilter === "OFFLINE" && t.is_online) return false;
        if (searchQuery) {
          const matchId = (t.team_id || '').toLowerCase().includes(searchQuery);
          const matchName = (t.team_name || '').toLowerCase().includes(searchQuery);
          const matchMem = (t.members || '').toLowerCase().includes(searchQuery);
          const matchStage = (t.stage_title || '').toLowerCase().includes(searchQuery);
          if (!matchId && !matchName && !matchMem && !matchStage) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = `<div style="grid-column: 1 / -1; text-align:center; padding:40px; color:var(--text-muted); font-family:var(--font-mono);">No workstations found matching current criteria.</div>`;
        return;
      }

      const formatTime = (sec) => {
        const m = Math.floor(sec / 60);
        const s = sec % 60;
        return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
      };

      let html = "";
      filtered.forEach((t, idx) => {
        const rank = idx + 1;
        let cardStatusClass = "";
        let pulseIndicator = `<span class="pulse-green"></span> <span style="color:var(--tactical-green); font-weight:bold;">ACTIVE</span>`;
        
        if (t.is_locked) {
          cardStatusClass = "locked";
          pulseIndicator = `<span class="pulse-red"></span> <span style="color:var(--combat-red); font-weight:bold;">LOCKED</span>`;
        } else if (t.is_finished) {
          cardStatusClass = "finished";
          pulseIndicator = `<span class="pulse-green"></span> <span style="color:var(--tactical-green); font-weight:bold;">LIBERATED</span>`;
        } else if (!t.is_online) {
          cardStatusClass = "offline";
          pulseIndicator = `<span style="color:var(--text-muted); font-weight:bold;">⚫ OFFLINE</span>`;
        } else if (t.last_seen_sec_ago > 60) {
          pulseIndicator = `<span class="pulse-amber"></span> <span style="color:var(--hazard-amber); font-weight:bold;">IDLE</span>`;
        }

        let specificBreachBadge = '';
        const act = (t.last_action || '');
        if (act.includes("Google") || act.includes("Lens") || act.includes("Right-Click")) {
          specificBreachBadge = `<div class="tamper-badge google-lens" style="margin-top:4px;">🔍 GOOGLE SEARCH DETECTED</div>`;
        } else if (act.includes("Fullscreen") || act.includes("Esc")) {
          specificBreachBadge = `<div class="tamper-badge fullscreen-exit" style="margin-top:4px;">🚨 FULLSCREEN EXITED</div>`;
        } else if (act.includes("Focus") || act.includes("Alt-Tab") || act.includes("Windows Key")) {
          specificBreachBadge = `<div class="tamper-badge focus-lost" style="margin-top:4px;">🚨 FOCUS LOST (ALT-TAB / WIN)</div>`;
        }

        const stageText = t.is_finished 
          ? `🏆 FINISHED ${t.finish_time_str ? `(${escapeHtml(t.finish_time_str)})` : ''}` 
          : `STAGE ${t.current_stage.toString().padStart(2, '0')}`;

        html += `
          <div class="station-card ${cardStatusClass}">
            <div class="station-card-top">
              <span style="font-weight:bold; color:var(--cyber-cyan);">#${rank} [${escapeHtml(t.team_id)}]</span>
              <div style="display:flex; align-items:center; gap:4px; font-size:10.5px;">${pulseIndicator}</div>
            </div>
            <div class="station-card-title" title="${escapeHtml(t.team_name)}">${escapeHtml(t.team_name)}</div>
            <div class="station-card-mid">
              <div class="station-card-stage">${stageText}</div>
              <div class="station-card-time">${formatTime(t.adjusted_time_sec)}</div>
            </div>
            <div style="font-size:10.5px; color:var(--text-dim); font-family:var(--font-mono); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="${escapeHtml(t.stage_title)}">
              ${escapeHtml(t.stage_title)}
            </div>
            <div style="font-size:10px; color:var(--text-muted); font-family:var(--font-mono); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="${escapeHtml(t.last_action)}">
              ${escapeHtml(t.last_action)}
            </div>
            ${specificBreachBadge ? `<div style="margin: 4px 0;">${specificBreachBadge}</div>` : ''}
            <div class="station-card-actions">
              <button class="btn-table" onclick="showTeamTelemetry('${escapeHtml(t.team_id)}')">🔍</button>
              <button class="btn-table" onclick="openEditTeamModal('${escapeHtml(t.team_id)}')">✏️</button>
              <button class="btn-table" onclick="showTeamPuzzleTimes('${escapeHtml(t.team_id)}')">⏱️</button>
              ${t.is_locked ? `<button class="btn-table danger" onclick="remoteUnlockTeam('${escapeHtml(t.team_id)}')">🔓</button>` : ''}
              <button class="btn-table warning" onclick="remoteLogoutTeam('${escapeHtml(t.team_id)}')">🚪</button>
              <button class="btn-table danger" onclick="promptResetRoundTeam('${escapeHtml(t.team_id)}', 1)" title="Reset Round 1 to Stage 01">🔄 R1</button>
              <button class="btn-table warning" onclick="promptResetRoundTeam('${escapeHtml(t.team_id)}', 2)" title="Reset Round 2 to Puzzle 01" style="border-color:var(--hazard-amber); color:var(--hazard-amber);">🎯 R2</button>
              <button class="btn-table danger" onclick="promptDeleteTeam('${escapeHtml(t.team_id)}')">🗑️</button>
              <button class="btn-table" onclick="showTeamAuditLog('${escapeHtml(t.team_id)}')">📜</button>
            </div>
          </div>
        `;
      });
      grid.innerHTML = html;
    }

    async function remoteUnlockTeam(teamId) {
      if (!confirm(`Are you sure you want to remotely unlock workstation for ${teamId}?`)) return;
      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-unlock`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: teamId })
        });
        const data = await res.json();
        if (data.success) {
          alert(`Success: Workstation for ${teamId} has been remotely unlocked!`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to unlock'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server at " + (API_BASE || "localhost:8000") + ".\nPlease ensure ProjectFailsafe_Organizer.exe or run_server.bat is running.");
      }
    }

    async function remoteLogoutTeam(teamId) {
      if (!confirm(`⚠️ REMOTE LOGOUT CONFIRMATION:\n\nAre you sure you want to log out team [${teamId}] from their workstation?\nTheir session will be terminated and returned to the team login screen.`)) return;
      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-logout`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: teamId })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ Success: ${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to log out team'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server at " + (API_BASE || "localhost:8000") + ".");
      }
    }

    async function remoteLogoutAllTeams() {
      const conf = prompt(`⚠️ CRITICAL: GLOBAL LOGOUT COMMAND\n\nType 'LOGOUT ALL' to immediately terminate sessions across all connected workstations:`);
      if (conf !== 'LOGOUT ALL') return;
      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-logout`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: 'ALL' })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ Success: ${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed global logout'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server at " + (API_BASE || "localhost:8000") + ".");
      }
    }

    async function promptResetRound(roundNum) {
      const roundLabel = roundNum === 2 ? "ROUND 2 (STRATCOM ARENA)" : "ROUND 1 (EVIDENCE VAULT)";
      const promptPhrase = roundNum === 2 ? "RESET ROUND 2" : "RESET ROUND 1";
      const details = roundNum === 2 
        ? "• Clear all Round 2 progress, times, and completions back to Puzzle 01\n• Re-open and unlock the Round 2 shortlist\n• Retain all Round 1 scores, qualifications, and team registrations"
        : "• Reset all workstations back to Stage 01\n• Reset Round 1 mission timers and clue batteries [⚡ ⚡ ⚡]\n• Clear finish flags and penalties\n• Retain team logins and registrations";

      const conf = prompt(`⚠️ CRITICAL ORGANIZER OVERRIDE: ${roundLabel} RESET\n\n${details}\n\nTo confirm, type '${promptPhrase}' below:`);
      if (conf !== promptPhrase) return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/round/reset`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, admin_pin: ADMIN_PIN, round: roundNum, team_id: 'ALL' })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ ${roundLabel} RESET COMPLETE:\n\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to reset round'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server at " + (API_BASE || "localhost:8000") + ".");
      }
    }

    async function promptResetRoundTeam(teamId, roundNum) {
      const roundLabel = roundNum === 2 ? "ROUND 2 (Puzzle 01)" : "ROUND 1 (Stage 01)";
      const msg = roundNum === 2
        ? `⚠️ RESET ROUND 2 FOR [${teamId}]?\n\nThis will:\n- Reset team's Round 2 progress back to Puzzle 01\n- Reset Round 2 solve times and score\n- Clear Round 2 podium finish status\n- Retain team's Round 1 record\n\nProceed?`
        : `⚠️ RESET ROUND 1 FOR [${teamId}]?\n\nThis will:\n- Reset workstation back to Stage 01\n- Reset elapsed mission timer and penalties\n- Refill clue battery to 3 [⚡ ⚡ ⚡]\n- Relock future stages 02–16\n\nProceed?`;

      if (!confirm(msg)) return;
      try {
        const res = await fetch(`${API_BASE}/api/admin/round/reset`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, admin_pin: ADMIN_PIN, round: roundNum, team_id: teamId })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ Success: ${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to reset round for team'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server at " + (API_BASE || "localhost:8000") + ".");
      }
    }

    async function resetTeamRoundFromModal(roundNum) {
      const teamId = document.getElementById('edit-team-id')?.value;
      if (!teamId) return;
      await promptResetRoundTeam(teamId, roundNum);
      closeModal('modal-edit-team');
    }

    // Backward-compatible aliases
    async function remoteResetTeam(teamId) {
      return promptResetRoundTeam(teamId, 1);
    }

    async function remoteResetAllTeams() {
      return promptResetRound(1);
    }

    function showTeamAuditLog(teamId) {
      const team = cachedTeams.find(t => t.team_id === teamId);
      if (!team) return;

      document.getElementById('audit-modal-title').innerText = `📜 AUDIT LOG: ${team.team_name} [${team.team_id}]`;
      const container = document.getElementById('audit-log-container');
      const logs = team.activity_log || [];

      if (logs.length === 0) {
        container.innerHTML = `<div style="color:var(--text-muted); text-align:center; padding:20px;">No forensic entries logged yet.</div>`;
      } else {
        let html = "";
        logs.slice().reverse().forEach(log => {
          html += `
            <div class="audit-entry">
              <span><strong>[${escapeHtml(log.time || '')}]</strong> Stage ${log.stage}: ${escapeHtml(log.action || '')}</span>
            </div>
          `;
        });
        container.innerHTML = html;
      }

      openModal('modal-audit');
    }

        const STAGE_TITLES = {
      1: "Ch 01: ISHAAN Recovery Terminal",
      2: "Ch 02: ISHAAN's Memory Core",
      3: "Ch 03: The Confidential Memo",
      4: "Ch 04: The Fabricated Timeline",
      5: "Ch 05: Clearance Elevation",
      6: "Ch 06: Margin Whispers",
      7: "Ch 07: Counterfeit Directive",
      8: "Ch 08: Phosphor Steganography",
      9: "Ch 09: Corrupted Sensor Array",
      10: "Ch 10: Psychological Honeypot",
      11: "Ch 11: The WIE Core Failsafe",
      12: "Ch 12: The Whiteout Signature",
      13: "Ch 13: The ROT-4 IEEE Shift",
      14: "Ch 14: The Atbash Cipher Mirror",
      15: "Ch 15: The Polybius Coordinate Trail",
      16: "Ch 16: Frequency Override Count"
    };

    
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
      if (!confirm(`⚠️ PERMANENT TEAM REMOVAL ⚠️\n\nAre you sure you want to permanently delete team ${teamId} ("${name}") from the tournament ledger?\n\nThis action cannot be undone.`)) {
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

    async function promptPurgeAllTeams() {
      const count = cachedTeams.length;
      if (count === 0) {
        alert("⚠️ Tournament ledger is already empty. No teams to remove.");
        return;
      }

      const conf = prompt(
        `🚨 DANGER: PERMANENT PURGE OF ALL TEAMS 🚨\n\n` +
        `You are about to permanently DELETE ALL ${count} TEAMS from the tournament database!\n\n` +
        `This will:\n` +
        `• Permanently delete all team profiles, credentials, and passwords\n` +
        `• Wipe all elapsed times, stage progress, and audit logs\n` +
        `• Clear all shortlist qualifications for Round 2\n` +
        `• Reset the tournament ledger to 0 teams\n\n` +
        `THIS ACTION CANNOT BE UNDONE!\n\n` +
        `To confirm, type 'PURGE ALL TEAMS' below:`
      );

      if (conf !== 'PURGE ALL TEAMS') {
        if (conf !== null) {
          alert("❌ Action cancelled. Verification phrase was incorrect.");
        }
        return;
      }

      try {
        const res = await fetch(`${getApiBase()}/api/admin/teams/purge-all`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            admin_pin: sessionStorage.getItem('admin_pin') || ADMIN_PIN
          })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          alert(`✅ GLOBAL PURGE COMPLETE:\n\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert('Error executing global purge: ' + (data.error || 'Unknown failure'));
        }
      } catch (err) {
        alert('Server communication error: ' + err.message);
      }
    }
    window.promptPurgeAllTeams = promptPurgeAllTeams;

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

    function showTeamPuzzleTimes(teamId) {
      const team = cachedTeams.find(t => t.team_id === teamId);
      if (!team) return;

      document.getElementById('puzzle-times-modal-title').innerText = `⏱️ PUZZLE SOLVE TIMES: ${team.team_name} [${team.team_id}]`;
      const container = document.getElementById('puzzle-times-container');
      const stageTimes = team.stage_times || {};

      let totalSec = team.raw_time_sec || 0;
      let html = `
        <div style="background:rgba(5,12,20,0.95); border:1px solid rgba(0,240,255,0.3); border-radius:4px; padding:14px; font-family:var(--font-mono);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(0,240,255,0.2); padding-bottom:8px;">
            <span style="color:var(--cyber-cyan); font-weight:bold; font-size:12px;">STAGE / OBJECTIVE</span>
            <span style="color:var(--cyber-cyan); font-weight:bold; font-size:12px;">SOLVE TIME</span>
          </div>
      `;

      let hasAny = false;
      for (let i = 1; i <= 15; i++) {
        const info = stageTimes[i] || stageTimes[String(i)];
        const title = STAGE_TITLES[i] || `Stage ${i}`;
        if (info && (info.duration_str || info.duration_seconds)) {
          hasAny = true;
          const durStr = info.duration_str || `${info.duration_seconds}s`;
          html += `
            <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-bottom:1px solid rgba(255,255,255,0.06); font-size:11.5px;">
              <span style="color:var(--text-white);"><span style="color:var(--tactical-green); font-weight:bold;">[STAGE ${i < 10 ? '0' + i : i}]</span> ${escapeHtml(title)}</span>
              <span style="color:var(--tactical-green); font-weight:bold;">${escapeHtml(durStr)}</span>
            </div>
          `;
        } else {
          const isCleared = team.current_stage > i || team.is_finished;
          html += `
            <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-bottom:1px solid rgba(255,255,255,0.04); font-size:11.5px; opacity:0.6;">
              <span style="color:var(--text-dim);"><span style="color:var(--text-muted);">[STAGE ${i < 10 ? '0' + i : i}]</span> ${escapeHtml(title)}</span>
              <span style="color:var(--text-muted); font-size:10px;">${isCleared ? 'CLEARED' : (team.current_stage === i ? '⏳ IN PROGRESS' : '🔒 LOCKED')}</span>
            </div>
          `;
        }
      }

      const m = Math.floor(totalSec / 60);
      const s = totalSec % 60;
      const totalStr = `${m}m ${s < 10 ? '0' + s : s}s`;

      html += `
          <div style="margin-top:12px; padding-top:8px; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; font-weight:bold; font-size:12px;">
            <span style="color:var(--text-white);">TOTAL RAW TIME:</span>
            <span style="color:var(--cyber-cyan);">${team.finish_time_str || totalStr}</span>
          </div>
        </div>
      `;

      container.innerHTML = html;
      openModal('modal-puzzle-times');
    }

    function openBroadcastModal() { openModal('modal-broadcast'); }
    function openMasterKeysModal() { openModal('modal-master-keys'); }

    async function submitBroadcast() {
      const input = document.getElementById('broadcast-input');
      const msg = input.value.trim();
      if (!msg) return;

      const online = await checkServerStatus();
      if (!online) {
        // Fallback: save to localStorage for same-machine stations
        try {
          const payload = { id: Date.now(), message: msg, time: new Date().toLocaleTimeString() };
          localStorage.setItem("failsafe_global_broadcast", JSON.stringify(payload));
        } catch(e) {}

        alert("⚠️ SERVER OFFLINE:\n\nThe local background server is not currently running on port 8000.\n\nTo broadcast across all LAN team laptops, please start the server:\n1. Double-click 'ProjectFailsafe_Organizer.exe' (or run 'run_server.bat')\n2. Open http://localhost:8000/admin.html\n\n(Saved to local workstation storage as offline fallback).");
        input.value = "";
        closeModal('modal-broadcast');
        return;
      }

      try {
        const res = await fetch(`${API_BASE}/api/admin/broadcast`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, message: msg })
        });
        if (res.ok) {
          // Mirror to localStorage
          try {
            localStorage.setItem("failsafe_global_broadcast", JSON.stringify({ id: Date.now(), message: msg, time: new Date().toLocaleTimeString() }));
          } catch(e) {}
          alert("✅ Broadcast transmitted successfully to all active stations!");
          input.value = "";
          closeModal('modal-broadcast');
        } else {
          const errData = await res.json().catch(() => ({}));
          alert("Server Error: " + (errData.error || "Failed to send broadcast"));
        }
      } catch(e) {
        alert("⚠️ Network Error: Unable to reach server at " + (API_BASE || "localhost:8000") + ".\nPlease verify ProjectFailsafe_Organizer.exe is running.");
      }
    }

    function exportCsv() {
      if (cachedTeams.length === 0) {
        alert("No team data available to export.");
        return;
      }
      let csv = [
        ["Rank", "Team ID", "Team Name", "Password", "Members", "Current Stage", "Stage Title", "Last Action", "Status", "Tamper Incidents", "Raw Time (s)", "Adjusted Score (s)", "Hints Count", "Traps Count"].join(",")
      ];

      cachedTeams.forEach((t, i) => {
        csv.push([
          i + 1,
          `"${(t.team_id || '').replace(/"/g, '""')}"`,
          `"${(t.team_name || '').replace(/"/g, '""')}"`,
          `"${(t.password || '').replace(/"/g, '""')}"`,
          `"${(t.members || '').replace(/"/g, '""')}"`,
          t.current_stage,
          `"${(t.stage_title || '').replace(/"/g, '""')}"`,
          `"${(t.last_action || '').replace(/"/g, '""')}"`,
          t.is_finished ? "FINISHED" : (t.is_online ? "ACTIVE" : "INACTIVE"),
          t.tamper_incidents || 0,
          t.raw_time_sec || 0,
          t.adjusted_time_sec || 0,
          t.hints_count || 0,
          t.traps_count || 0
        ].join(","));
      });

      const blob = new Blob([csv.join("\n")], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `failsafe_organizer_leaderboard_${Date.now()}.csv`;
      a.click();
    }

    let cachedShortlistTeams = [];

    async function openRound2ShortlistModal() {
      openModal('modal-round2-shortlist');
      await fetchShortlistData();
    }

    async function fetchShortlistData() {
      try {
        const res = await fetch(`${API_BASE}/api/admin/shortlist?pin=${encodeURIComponent(ADMIN_PIN)}`);
        if (!res.ok) throw new Error("Could not fetch shortlist");
        const data = await res.json();
        cachedShortlistTeams = data.ranked_teams || [];

        const countEl = document.getElementById("shortlist-qualified-count");
        if (countEl) countEl.innerText = data.qualified_count || 0;

        const badgeEl = document.getElementById("shortlist-round-badge");
        if (badgeEl) {
          if (data.current_round >= 2) {
            badgeEl.innerText = "ROUND 2 IN PROGRESS";
            badgeEl.style.color = "var(--combat-red)";
            badgeEl.style.borderColor = "var(--combat-red)";
            badgeEl.style.background = "rgba(255,0,60,0.15)";
          } else {
            badgeEl.innerText = "ROUND 1 ACTIVE";
            badgeEl.style.color = "var(--tactical-green)";
            badgeEl.style.borderColor = "var(--tactical-green)";
            badgeEl.style.background = "rgba(0,255,102,0.15)";
          }
        }

        const btnStart = document.getElementById("btn-start-round-2");
        if (btnStart) {
          if (data.current_round >= 2) {
            btnStart.innerHTML = "<span>⚡</span> ROUND 2 RUNNING";
            btnStart.disabled = true;
            btnStart.style.opacity = "0.6";
          } else {
            btnStart.innerHTML = "<span>🚀</span> LOCK SHORTLIST & START ROUND 2";
            btnStart.disabled = false;
            btnStart.style.opacity = "1";
          }
        }

        renderShortlistTable();
      } catch (err) {
        console.error("Shortlist fetch error:", err);
      }
    }

    function renderShortlistTable() {
      const tbody = document.getElementById("shortlist-table-body");
      if (!tbody) return;

      const filterVal = (document.getElementById("shortlist-search-input")?.value || "").toLowerCase().trim();
      const filtered = cachedShortlistTeams.filter(t => {
        if (!filterVal) return true;
        return (t.team_id || "").toLowerCase().includes(filterVal) ||
               (t.team_name || "").toLowerCase().includes(filterVal);
      });

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" style="text-align:center; padding:24px; color:var(--text-muted);">No teams match the filter.</td></tr>`;
        return;
      }

      let html = "";
      filtered.forEach((t) => {
        const isQualified = t.is_qualified;
        const isAutoTop = t.rank <= 12;
        const rankBadge = isAutoTop 
          ? `<span style="background:rgba(255,184,0,0.18); border:1px solid var(--hazard-amber); color:var(--hazard-amber); padding:2px 8px; border-radius:3px; font-weight:bold;">👑 #${t.rank}</span>`
          : `<span style="color:var(--text-muted); padding:2px 6px;">#${t.rank}</span>`;

        const statusPill = isQualified
          ? `<span style="background:rgba(0,255,102,0.15); border:1px solid var(--tactical-green); color:var(--tactical-green); padding:3px 10px; border-radius:12px; font-weight:bold; font-size:10.5px;">✅ QUALIFIED</span>`
          : `<span style="background:rgba(100,116,139,0.2); border:1px solid var(--text-muted); color:var(--text-dim); padding:3px 10px; border-radius:12px; font-size:10.5px;">⏸️ STANDBY</span>`;

        const actionBtn = isQualified
          ? `<button class="btn-action danger" onclick="toggleTeamQualification('${escapeHtml(t.team_id)}', true)" style="font-size:10.5px; padding:4px 10px; border-color:var(--combat-red); color:var(--combat-red);">✕ REMOVE</button>`
          : `<button class="btn-action success" onclick="toggleTeamQualification('${escapeHtml(t.team_id)}', false)" style="font-size:10.5px; padding:4px 10px; border-color:var(--tactical-green); color:var(--tactical-green);">+ QUALIFY</button>`;

        const timeStr = t.finish_time_str || `${Math.floor(t.adjusted_time_sec/60)}m ${t.adjusted_time_sec%60}s`;

        html += `
          <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:${isQualified ? 'rgba(0,240,255,0.02)' : 'transparent'};">
            <td style="padding:10px 12px;">${rankBadge}</td>
            <td style="padding:10px 12px;">
              <strong style="color:var(--text-white); font-size:12px;">${escapeHtml(t.team_id)}</strong>
              <div style="font-size:10.5px; color:var(--text-dim);">${escapeHtml(t.team_name)}</div>
            </td>
            <td style="padding:10px 12px;">
              <span style="color:${t.is_finished ? 'var(--tactical-green)' : 'var(--hazard-amber)'}; font-weight:bold;">
                ${t.is_finished ? '🏆 FINISHED ALL 15' : `STAGE ${t.current_stage}`}
              </span>
            </td>
            <td style="padding:10px 12px; font-weight:bold; color:var(--cyber-cyan);">${escapeHtml(timeStr)}</td>
            <td style="padding:10px 12px; text-align:center;">${statusPill}</td>
            <td style="padding:10px 12px; text-align:right;">${actionBtn}</td>
          </tr>
        `;
      });

      tbody.innerHTML = html;
    }

    function filterShortlistDisplay() {
      renderShortlistTable();
    }

    async function toggleTeamQualification(teamId, curQualified) {
      try {
        const res = await fetch(`${API_BASE}/api/admin/shortlist/toggle`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            pin: ADMIN_PIN,
            team_id: teamId,
            qualified: !curQualified
          })
        });
        if (res.ok) {
          await fetchShortlistData();
        } else {
          alert("Failed to toggle team qualification.");
        }
      } catch (err) {
        console.error(err);
      }
    }

    async function resetShortlistToTop12() {
      if (!confirm("Reset shortlist to the automated Top 12 teams based on current Round 1 standings?")) return;
      try {
        const res = await fetch(`${API_BASE}/api/admin/shortlist/reset`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN })
        });
        if (res.ok) {
          await fetchShortlistData();
        }
      } catch (err) {
        console.error(err);
      }
    }

    async function promptStartRound2() {
      const qCount = document.getElementById("shortlist-qualified-count")?.innerText || "0";
      const confirmMsg = `⚠️ ARE YOU READY TO START ROUND 2?\\n\\n` +
        `• ${qCount} qualified teams will be unlocked into the StratCom Decryption Arena.\\n` +
        `• All other workstations will enter Standby / Debriefing mode.\\n` +
        `• This action broadcasts an emergency alert to all workstations in the venue.\\n\\n` +
        `Type 'CONFIRM' to launch Round 2:`;
      const reply = prompt(confirmMsg);
      if (reply !== "CONFIRM") return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/start_round_2`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          alert(`🚀 ROUND 2 HAS OFFICIALLY COMMENCED!\\n\\n${data.qualified_count} stations unlocked into the Decryption Arena.`);
          await fetchShortlistData();
          fetchLeaderboardData();
        } else {
          alert(`Error launching Round 2: ${data.error || "Unknown error"}`);
        }
      } catch (err) {
        alert(`Network error: ${err.message}`);
      }
    }

    async function promptUnlockAllLevels(teamId = 'ALL') {
      const targetLabel = teamId === 'ALL' ? 'ALL WORKSTATIONS' : `TEAM [${teamId}]`;
      const conf = prompt(`🔓 TEST MODE OVERRIDE: UNLOCK ALL LEVELS\n\nThis will instantly unlock all 16 Round 1 Stages and all 15 Round 2 Puzzles for ${targetLabel} so the organizer can test any puzzle.\n\nType 'UNLOCK' to confirm:`);
      if (conf !== 'UNLOCK') return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/levels/unlock_all`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, admin_pin: ADMIN_PIN, team_id: teamId })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ ALL LEVELS UNLOCKED FOR TESTING:\n\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to unlock levels'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server: " + err.message);
      }
    }

    async function promptLockAllLevels(teamId = 'ALL') {
      const targetLabel = teamId === 'ALL' ? 'ALL WORKSTATIONS' : `TEAM [${teamId}]`;
      const conf = prompt(`🔒 RESTORE TOURNAMENT LOCK: LOCK ALL LEVELS\n\nThis will lock all levels back and return ${targetLabel} to Stage 01 with competitive sequential progression restored.\n\nType 'LOCK' to confirm:`);
      if (conf !== 'LOCK') return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/levels/lock_all`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, admin_pin: ADMIN_PIN, team_id: teamId })
        });
        const data = await res.json();
        if (data.success) {
          alert(`✅ ALL LEVELS LOCKED:\n\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || 'Failed to lock levels'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server: " + err.message);
      }
    }

    async function promptClearBroadcasts() {
      if (!confirm("🧹 Clear all broadcast history?\n\nThis will purge past broadcasts so participant workstations do not see stale announcement toasts on launch.")) return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/broadcast/clear`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ pin: ADMIN_PIN, admin_pin: ADMIN_PIN })
        });
        const data = await res.json();
        if (data.success) {
          localStorage.removeItem("failsafe_global_broadcast");
          alert("✅ All broadcasts cleared successfully!");
          closeModal('modal-broadcast');
        } else {
          alert(`Error: ${data.error || 'Failed to clear broadcasts'}`);
        }
      } catch (err) {
        alert("⚠️ Failed to communicate with server: " + err.message);
      }
    }

    async function unlockTeamLevelsFromModal() {
      const teamId = document.getElementById("edit-team-id")?.value;
      if (!teamId) return;
      await promptUnlockAllLevels(teamId);
      closeModal('modal-edit-team');
    }

    async function lockTeamLevelsFromModal() {
      const teamId = document.getElementById("edit-team-id")?.value;
      if (!teamId) return;
      await promptLockAllLevels(teamId);
      closeModal('modal-edit-team');
    }

    function openModal(id) {
      const m = document.getElementById(id);
      if (m) m.style.display = 'flex';
    }

    function closeModal(id) {
      const m = document.getElementById(id);
      if (m) m.style.display = 'none';
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/[&<>'"]/g, tag => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
      }[tag] || tag));
    }

    // Auto-poll every 2.5 seconds if authenticated
    checkAdminAuthOnLoad();
    setInterval(() => {
      if (isAdminAuthenticated()) {
        fetchLeaderboardData();
      }
    }, 2500);
  
    // =========================================================================
    // ROUND 2 SHORTLIST & FULLSCREEN CONTROL FUNCTIONS
    // =========================================================================

    function openRound2ShortlistModal() {
      openModal("modal-shortlist-r2");
      fetchShortlistData();
    }

    async function fetchShortlistData() {
      try {
        const res = await fetch(`${API_BASE}/api/admin/shortlist?pin=${encodeURIComponent(ADMIN_PIN)}`);
        if (res.ok) {
          const data = await res.json();
          allShortlistTeams = data.teams || [];
          const qCountEl = document.getElementById("shortlist-qualified-count");
          if (qCountEl) {
            const qCount = allShortlistTeams.filter(t => t.is_qualified).length;
            qCountEl.innerText = qCount;
          }
          renderShortlistTable();
        }
      } catch (err) {
        console.error("Error fetching shortlist:", err);
      }
    }

    async function remoteLogoutAllTeams() {
      const confirmText = prompt("⚠️ DANGER: Force logout ALL 100 workstations?\n\nAll participant laptops will be immediately logged out and returned to the station authentication screen.\n\nType 'LOGOUT ALL' to confirm:");
      if (confirmText !== "LOGOUT ALL") return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-logout`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: "ALL" })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          alert(`🚪 GLOBAL LOGOUT SUCCESSFUL:\n\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || "Failed to trigger global logout"}`);
        }
      } catch (err) {
        alert(`Network error: ${err.message}`);
      }
    }

    // Alias for remoteResetAllTeams
    async function remoteResetAllTeams() {
      return promptResetRound(1);
    }

    async function checkPendingFullscreenRequests() {
      try {
        const res = await fetch(`${API_BASE}/api/admin/pending_fullscreen_requests`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN })
        });
        if (res.ok) {
          const data = await res.json();
          renderFullscreenRequests(data.pending || []);
        }
      } catch (err) {}
    }

    function renderFullscreenRequests(pendingList) {
      const banner = document.getElementById("fs-requests-banner");
      const listEl = document.getElementById("fs-requests-list");
      if (!banner || !listEl) return;

      if (!pendingList || pendingList.length === 0) {
        banner.style.display = "none";
        listEl.innerHTML = "";
        return;
      }

      banner.style.display = "block";
      let html = "";
      pendingList.forEach(p => {
        html += `
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,0,60,0.6); padding:4px 10px; border-radius:3px; display:inline-flex; align-items:center; gap:8px; font-family:var(--font-mono); font-size:11.5px;">
            <span style="color:#fff; font-weight:bold;">${escapeHtml(p.team_id)} (${escapeHtml(p.team_name)})</span>
            <span style="color:var(--hazard-amber);">[Stage 0${p.current_stage || 1}]</span>
            <button onclick="respondFullscreenExit('${escapeHtml(p.team_id)}', 'approve')" style="background:var(--tactical-green); color:#000; border:none; padding:3px 8px; border-radius:2px; font-weight:bold; cursor:pointer; font-size:10.5px;">✅ APPROVE</button>
            <button onclick="respondFullscreenExit('${escapeHtml(p.team_id)}', 'deny')" style="background:var(--combat-red); color:#fff; border:none; padding:3px 8px; border-radius:2px; font-weight:bold; cursor:pointer; font-size:10.5px;">❌ DENY</button>
          </div>
        `;
      });
      listEl.innerHTML = html;
    }

    async function respondFullscreenExit(teamId, action) {
      try {
        const res = await fetch(`${API_BASE}/api/admin/approve_fullscreen_exit`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: teamId, action: action })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          checkPendingFullscreenRequests();
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || "Failed to process fullscreen exit response"}`);
        }
      } catch (err) {
        alert(`Network error: ${err.message}`);
      }
    }

