# patch_frontend_r2_15_and_break.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Fullscreen Exit Request button to Header Toolbar
fs_btn_header = '''      <button id="btn-request-fs-exit" onclick="requestFullscreenExit()" class="btn-action warning" style="display:none; font-size:10.5px; padding:3px 8px; border-color:var(--hazard-amber, #ffb800); color:var(--hazard-amber, #ffb800); margin-left:8px;" title="Request permission from Organizer to exit Chrome fullscreen">
        🔓 REQUEST FULLSCREEN EXIT
      </button>'''

if 'id="btn-request-fs-exit"' not in html:
    # Insert next to top bar actions or fullscreen toggle
    marker = 'id="btn-fullscreen-toggle"'
    if marker in html:
        html = html.replace(marker, 'id="btn-fullscreen-toggle" ' + fs_btn_header)
    else:
        # insert inside top toolbar
        html = html.replace('class="top-nav-actions"', 'class="top-nav-actions">\n' + fs_btn_header)

# 2. Add Fullscreen Exit Request button inside Proctor Lockdown Warning Modal
proctor_req_btn = '''        <div style="margin-top:14px; text-align:center;">
          <button type="button" onclick="requestFullscreenExit()" class="btn-action warning" style="padding:8px 16px; font-size:11px; border-color:var(--hazard-amber, #ffb800); color:var(--hazard-amber, #ffb800); font-weight:bold; cursor:pointer;">
            🔓 REQUEST ORGANIZER APPROVAL TO EXIT FULLSCREEN
          </button>
          <div id="fs-exit-request-status" style="margin-top:6px; font-size:11px; color:#cbd5e1; font-family:var(--font-mono, monospace);"></div>
        </div>'''

if 'id="fs-exit-request-status"' not in html:
    lock_marker = 'id="proctor-override-btn"'
    if lock_marker in html:
        html = html.replace(lock_marker, 'id="proctor-override-btn"' + proctor_req_btn)
    else:
        # Add to proctor overlay
        html = html.replace('id="proctor-lock-overlay"', 'id="proctor-lock-overlay">\n' + proctor_req_btn)

# 3. Add Round 1 Break / Intermission Modal
break_modal_html = '''  <!-- Round 1 Break & Shortlist Intermission Modal -->
  <div id="modal-round1-break" class="mil-modal" style="display:none; position:fixed; inset:0; z-index:9990; background:rgba(2, 6, 14, 0.95); backdrop-filter:blur(14px); align-items:center; justify-content:center; padding:20px;">
    <div style="max-width:680px; width:100%; background:#050914; border:2px solid var(--cyber-cyan, #00f0ff); border-radius:12px; box-shadow:0 0 50px rgba(0,240,255,0.4); padding:30px; text-align:center; font-family:var(--font-mono, monospace); color:#f1f5f9;">
      <div style="font-size:36px; margin-bottom:10px;">🏆</div>
      <div style="font-size:11px; letter-spacing:3px; color:var(--tactical-green, #00ff66); font-weight:bold; margin-bottom:6px;">PHASE 01 FORENSIC AUDIT COMPLETE</div>
      <h2 style="font-size:22px; color:#00f0ff; letter-spacing:1px; margin-bottom:12px;">ROUND 1 EVIDENCE SECURED</h2>
      
      <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.25); border-radius:8px; padding:16px; margin-bottom:20px; font-size:12.5px; line-height:1.6; color:#94a3b8;">
        All 11 narrative breadcrumbs recovered. Primary security baseline established. The initial lock on TARA has been loosened, and ISHAAN's perimeter defenses are disarmed.
      </div>

      <div style="background:rgba(255,184,0,0.12); border:1px solid var(--hazard-amber, #ffb800); border-radius:8px; padding:16px; margin-bottom:24px; text-align:center;">
        <div style="font-size:15px; font-weight:bold; color:var(--hazard-amber, #ffb800); margin-bottom:6px;">
          ⏸️ TOURNAMENT INTERMISSION ACTIVE
        </div>
        <div style="font-size:12px; color:#cbd5e1; line-height:1.5;">
          Organizers and judges are currently evaluating telemetry and finalizing the <strong>Top 12 Shortlist</strong>.<br>
          Round 2 will commence once authorized by Command Center. Stand by.
        </div>
      </div>

      <div id="r1-break-r2-status" style="margin-bottom:20px; font-size:13px; font-weight:bold; color:#38bdf8;">
        STATUS: AWAITING COMMAND CENTER ROUND 2 LAUNCH...
      </div>

      <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
        <button id="btn-enter-r2-from-break" onclick="launchRound2Arena()" class="btn-action success" style="display:none; padding:12px 28px; font-size:13px; font-weight:bold; border-color:#00ff66; color:#00ff66; box-shadow:0 0 25px rgba(0,255,102,0.4); cursor:pointer;">
          🚀 ENTER ROUND 2: CORE RECONSTRUCTION
        </button>
        <button type="button" onclick="document.getElementById('modal-round1-break').style.display='none'" class="btn-action" style="padding:10px 20px; font-size:11.5px; color:#94a3b8; border-color:#64748b;">
          VIEW EVIDENCE SUMMARY
        </button>
      </div>
    </div>
  </div>
'''

if 'id="modal-round1-break"' not in html:
    # Insert right before </body
    body_end = html.rfind('</body>')
    if body_end != -1:
        html = html[:body_end] + break_modal_html + "\n" + html[body_end:]

# 4. In handleMissionVictorySequence, show Round 1 Break Modal
old_vic_show = 'if (modal) modal.style.display = "flex";'
new_vic_show = '''if (modal) modal.style.display = "flex";
      // Trigger Round 1 Break / Intermission Modal
      const breakModal = document.getElementById("modal-round1-break");
      if (breakModal) {
        setTimeout(() => {
          breakModal.style.display = "flex";
        }, 3500);
      }'''
if old_vic_show in html and 'breakModal.style.display = "flex";' not in html:
    html = html.replace(old_vic_show, new_vic_show, 1)

# 5. Add JavaScript functions for Fullscreen Exit Request and R2 status check
frontend_script_additions = '''
    // =========================================================================
    // CONTROLLED FULLSCREEN EXIT PROTOCOL (ORGANIZER AUTHORIZED)
    // =========================================================================
    let fullscreenExitRequestPending = false;

    async function requestFullscreenExit() {
      const statusEl = document.getElementById("fs-exit-request-status");
      const btn = document.getElementById("btn-request-fs-exit");
      if (btn) btn.innerText = "⏳ EXIT REQUESTED...";
      if (statusEl) statusEl.innerText = "Transmitting authorization request to Command Center...";
      fullscreenExitRequestPending = true;

      const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : 'TEAM-01';
      try {
        const res = await fetch(`${getApiBase()}/api/teams/request_fullscreen_exit`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ team_id: teamId })
        });
        const data = await res.json();
        if (statusEl) statusEl.innerText = data.message || "Request sent. Stand by for Organizer clearance.";
        showBroadcastToast("⚠️ Fullscreen exit request submitted to Organizer. Please wait for authorization.");
      } catch (err) {
        if (statusEl) statusEl.innerText = "Cannot contact server. Please alert an in-person volunteer.";
      }
    }

    // Monitor fullscreen state to toggle header request button
    document.addEventListener("fullscreenchange", () => {
      const fsBtn = document.getElementById("btn-request-fs-exit");
      if (fsBtn) {
        if (document.fullscreenElement) {
          fsBtn.style.display = "inline-flex";
        } else {
          fsBtn.style.display = "none";
          fullscreenExitRequestPending = false;
        }
      }
    });
'''

# Insert additions before </script>
insert_pos = html.rfind('</script>')
if insert_pos != -1:
    html = html[:insert_pos] + frontend_script_additions + "\n" + html[insert_pos:]

# 6. In reportTelemetryAction handling, handle fullscreen_exit_approved and round_2_ready
old_handler = '''          if (data.remote_unlock && typeof proctorLockActive !== 'undefined' && proctorLockActive) {
            verifyProctorOverrideDirectly();
          }'''

new_handler = '''          if (data.remote_unlock && typeof proctorLockActive !== 'undefined' && proctorLockActive) {
            verifyProctorOverrideDirectly();
          }
          if (data.fullscreen_exit_approved) {
            window.fullscreenExitExemptUntil = Date.now() + 60000;
            if (typeof proctorLockActive !== 'undefined' && proctorLockActive) {
              verifyProctorOverrideDirectly();
            }
            if (document.fullscreenElement) {
              document.exitFullscreen().catch(() => {});
            }
            const statusEl = document.getElementById("fs-exit-request-status");
            if (statusEl) statusEl.innerText = "✅ Fullscreen Exit Approved by Organizer.";
            showBroadcastToast("✅ Fullscreen Exit Authorized by Organizer.");
          }
          // Check Round 2 Readiness for Break Screen
          const r2StatusEl = document.getElementById("r1-break-r2-status");
          const r2LaunchBtn = document.getElementById("btn-enter-r2-from-break");
          if (r2StatusEl && r2LaunchBtn) {
            if (data.round_2_ready) {
              r2StatusEl.innerHTML = '<span style="color:var(--tactical-green, #00ff66);">✅ SHORTLIST APPROVED! Round 2 Decryption Arena is LIVE.</span>';
              r2LaunchBtn.style.display = 'inline-block';
            } else if (data.round_2_started && !data.is_shortlisted) {
              r2StatusEl.innerHTML = '<span style="color:var(--text-muted, #94a3b8);">Round 2 has commenced for the Top 12 finalists. Your station is on standby in exhibition mode.</span>';
              r2LaunchBtn.style.display = 'none';
            } else {
              r2StatusEl.innerHTML = '<span>STATUS: TOURNAMENT ON BREAK • AWAITING ORGANIZER ROUND 2 LAUNCH...</span>';
              r2LaunchBtn.style.display = 'none';
            }
          }'''

if old_handler in html:
    html = html.replace(old_handler, new_handler)

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)

print("aditi_os_widget.html successfully updated with Fullscreen Exit & Round 1 Break!")
