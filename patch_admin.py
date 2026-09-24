# patch_admin.py
import re

with open("admin.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Fullscreen Requests Banner to Admin Container if not present
fs_banner_html = '''    <!-- Live Fullscreen Exit Requests Alert Banner -->
    <div id="fs-requests-banner" style="display:none; background:rgba(255, 0, 60, 0.15); border:1px solid var(--combat-red); padding:12px 18px; border-radius:4px; margin-bottom:16px; box-shadow:0 0 20px rgba(255,0,60,0.3);">
      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <span class="pulse-red" style="width:10px; height:10px;"></span>
          <strong style="color:var(--combat-red); font-family:var(--font-mono); font-size:13px; letter-spacing:1px;">⚠️ FULLSCREEN EXIT REQUESTS PENDING AUTHORIZATION</strong>
        </div>
        <div id="fs-requests-list" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;"></div>
      </div>
    </div>
'''

if 'id="fs-requests-banner"' not in html:
    html = html.replace('<div class="admin-container">', '<div class="admin-container">\n' + fs_banner_html)

# 2. Add functions for Shortlist Modal, Fullscreen Approvals, Remote Logout, Remote Reset
admin_script_additions = '''
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
      const confirmText = prompt("⚠️ DANGER: Force logout ALL 100 workstations?\\n\\nAll participant laptops will be immediately logged out and returned to the station authentication screen.\\n\\nType 'LOGOUT ALL' to confirm:");
      if (confirmText !== "LOGOUT ALL") return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-logout`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: "ALL" })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          alert(`🚪 GLOBAL LOGOUT SUCCESSFUL:\\n\\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || "Failed to trigger global logout"}`);
        }
      } catch (err) {
        alert(`Network error: ${err.message}`);
      }
    }

    async function remoteResetAllTeams() {
      const confirmText = prompt("⚠️ CRITICAL WARNING: Force reset ALL workstations to Stage 01?\\n\\nThis will erase progress on all workstations!\\n\\nType 'RESET ALL' to confirm:");
      if (confirmText !== "RESET ALL") return;

      try {
        const res = await fetch(`${API_BASE}/api/admin/remote-reset`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ pin: ADMIN_PIN, team_id: "ALL" })
        });
        const data = await res.json();
        if (res.ok && data.success) {
          alert(`🔄 GLOBAL RESET SUCCESSFUL:\\n\\n${data.message}`);
          fetchLeaderboardData();
        } else {
          alert(`Error: ${data.error || "Failed to trigger global reset"}`);
        }
      } catch (err) {
        alert(`Network error: ${err.message}`);
      }
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
'''

# Insert additions before </script>
insert_pos = html.rfind('</script>')
if insert_pos != -1:
    html = html[:insert_pos] + admin_script_additions + "\n" + html[insert_pos:]

# In fetchLeaderboardData, call checkPendingFullscreenRequests()
if 'checkPendingFullscreenRequests();' not in html:
    html = html.replace('function renderLeaderboardTable() {', 'checkPendingFullscreenRequests();\n    function renderLeaderboardTable() {')

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(html)

print("admin.html successfully patched!")
