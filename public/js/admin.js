/**
 * PROJECT FAILSAFE: Organizer Admin Dashboard & Live Leaderboard
 */

const ADMIN_PIN_DEFAULT = "wie-admin-2026";
let adminPollInterval = null;

function showAdminModal() {
  const currentPin = localStorage.getItem("failsafe_admin_pin") || "";
  const win = document.getElementById("admin-window");
  win.style.display = "flex";
  bringWindowToFront(win);

  if (currentPin === ADMIN_PIN_DEFAULT) {
    loadLeaderboard();
  } else {
    document.getElementById("admin-login-view").style.display = "block";
    document.getElementById("admin-dashboard-view").style.display = "none";
  }
}

function verifyAdminPin(e) {
  e.preventDefault();
  const inputPin = document.getElementById("admin-pin-input").value.trim();
  if (inputPin === ADMIN_PIN_DEFAULT) {
    localStorage.setItem("failsafe_admin_pin", inputPin);
    document.getElementById("admin-login-view").style.display = "none";
    document.getElementById("admin-dashboard-view").style.display = "block";
    loadLeaderboard();
  } else {
    alert("Incorrect Admin PIN. Access Denied.");
  }
}

async function loadLeaderboard() {
  const pin = localStorage.getItem("failsafe_admin_pin") || ADMIN_PIN_DEFAULT;
  const container = document.getElementById("leaderboard-table-body");

  try {
    const res = await fetch(`/api/admin/leaderboard?pin=${encodeURIComponent(pin)}`);
    if (!res.ok) throw new Error("Server error or offline mode");
    const data = await res.json();
    renderLeaderboard(data.leaderboard);
  } catch (err) {
    // Standalone fallback: Load from local state
    const localTeam = JSON.parse(localStorage.getItem("failsafe_team") || "null");
    if (localTeam) {
      const now = Date.now() / 1000;
      const rawSec = localTeam.endTime ? (localTeam.endTime - localTeam.startTime) : (now - localTeam.startTime);
      const hintsSec = (localTeam.hintsCount || 0) * 120;
      const trapsSec = (localTeam.trapsCount || 0) * 300;
      renderLeaderboard([{
        team_id: localTeam.teamId,
        team_name: localTeam.teamName,
        members: localTeam.members,
        current_stage: localTeam.currentStage,
        is_finished: localTeam.isFinished,
        raw_time_sec: Math.max(0, Math.floor(rawSec)),
        adjusted_time_sec: Math.max(0, Math.floor(rawSec + hintsSec + trapsSec)),
        hints_count: localTeam.hintsCount || 0,
        traps_count: localTeam.trapsCount || 0
      }]);
    } else {
      container.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:20px; color:#64748b;">No registered teams found.</td></tr>`;
    }
  }

  if (!adminPollInterval) {
    adminPollInterval = setInterval(loadLeaderboard, 5000);
  }
}

function renderLeaderboard(teams) {
  const tbody = document.getElementById("leaderboard-table-body");
  if (!teams || teams.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:20px; color:#64748b;">No teams active yet.</td></tr>`;
    return;
  }

  let html = "";
  teams.forEach((t, idx) => {
    const rank = idx + 1;
    const formatTime = (sec) => {
      const m = Math.floor(sec / 60);
      const s = sec % 60;
      return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    };

    const statusBadge = t.is_finished 
      ? `<span style="color:var(--accent-green); font-weight:bold;">🏆 CONTAINED</span>`
      : `<span style="color:var(--accent-gold);">Stage ${t.current_stage}/11</span>`;

    html += `
      <tr>
        <td style="font-weight:bold; color:var(--accent-cyan); text-align:center;">#${rank}</td>
        <td><strong>${escapeHtml(t.team_name)}</strong> <br><span style="font-size:10px; color:#64748b;">[${escapeHtml(t.team_id)}]</span></td>
        <td>${escapeHtml(t.members || "—")}</td>
        <td>${statusBadge}</td>
        <td>${formatTime(t.raw_time_sec)}</td>
        <td style="color:${t.hints_count > 0 ? 'var(--accent-gold)' : '#64748b'}">${t.hints_count} (+${t.hints_count * 2}m)</td>
        <td style="color:${t.traps_count > 0 ? 'var(--accent-red)' : '#64748b'}">${t.traps_count} (+${t.traps_count * 5}m)</td>
        <td style="font-weight:bold; color:var(--accent-green);">${formatTime(t.adjusted_time_sec)}</td>
      </tr>
    `;
  });

  tbody.innerHTML = html;
}

async function sendOrganizerBroadcast(e) {
  e.preventDefault();
  const msgInput = document.getElementById("broadcast-msg-input");
  const msg = msgInput.value.trim();
  if (!msg) return;

  const pin = localStorage.getItem("failsafe_admin_pin") || ADMIN_PIN_DEFAULT;
  try {
    await fetch("/api/admin/broadcast", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pin, message: msg })
    });
    alert("Broadcast sent successfully to all participant screens!");
    msgInput.value = "";
  } catch (err) {
    alert("Could not send broadcast. Ensure server is running.");
  }
}

function exportLeaderboardCSV() {
  const table = document.getElementById("admin-leaderboard-table");
  let csv = [];
  for (let row of table.rows) {
    let rowData = [];
    for (let cell of row.cells) {
      rowData.push('"' + cell.innerText.replace(/"/g, '""').replace(/\n/g, ' ') + '"');
    }
    csv.push(rowData.join(","));
  }

  const blob = new Blob([csv.join("\n")], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `failsafe_leaderboard_${Date.now()}.csv`;
  a.click();
}

function toggleMasterKeys() {
  const el = document.getElementById("master-solutions-sheet");
  el.style.display = el.style.display === "none" ? "block" : "none";
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.innerText = text || '';
  return div.innerHTML;
}
