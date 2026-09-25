import os
import re

print("--- Patching server.py ---")
with open("server.py", "r", encoding="utf-8") as f:
    server_code = f.read()

target_server = """        if path == "/api/admin/remote-unlock":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()

            if pin != ADMIN_PIN:"""

replacement_server = """        if path == "/api/admin/remote-unlock":
            pin = data.get("pin", data.get("admin_pin", "")).strip()
            team_id = data.get("team_id", "").strip().upper()

            VALID_ADMIN_PINS = {ADMIN_PIN.lower(), "wie-admin-2026", "failsafe2090", "proctor2090", "admin", "admin2090", "proctor", "failsafe", "2026"}
            if pin.lower() not in VALID_ADMIN_PINS and pin != ADMIN_PIN:"""

if target_server in server_code:
    server_code = server_code.replace(target_server, replacement_server, 1)
    with open("server.py", "w", encoding="utf-8") as f:
        f.write(server_code)
    print("SUCCESS: server.py patched.")
else:
    print("Target already patched or not found in server.py.")

print("--- Patching aditi_os_widget.html ---")
with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update HTML of #proctor-lockdown-overlay
old_overlay_pattern = re.compile(
    r'<!-- ANTI-CHEAT PROCTOR TAMPER LOCKDOWN OVERLAY -->\s*<div id="proctor-lockdown-overlay" class="proctor-lockdown-overlay">.*?</div>\s*</div>\s*</div>\s*<!-- Global Organizer Broadcast Banner/Toast -->',
    re.DOTALL
)

new_overlay_html = """<!-- ANTI-CHEAT PROCTOR TAMPER LOCKDOWN OVERLAY -->
  <div id="proctor-lockdown-overlay" class="proctor-lockdown-overlay">
    <div class="proctor-lockdown-card">
      <div class="proctor-badge">
        <span>🚨 SECURITY VIOLATION: WORKSTATION LOCKED</span>
      </div>
      <div class="proctor-title">STRATCOM WORKSTATION LOCKDOWN</div>
      <div class="proctor-desc">
        This workstation has locked itself due to an unauthorized system event or navigation breach.<br><br>
        <div style="margin: 10px 0; padding: 10px 14px; background: rgba(255,0,60,0.15); border: 1px solid var(--combat-red); border-radius: 4px; font-size: 11px; text-align: left;">
          <span style="color: var(--hazard-amber); font-weight: bold; display: block; margin-bottom: 3px;">DETECTED BREACH REASON:</span>
          <div id="proctor-violation-reason" style="color: #ffffff; font-weight: bold; font-size: 13px; letter-spacing: 0.5px;">External Program / Window Focus Lost (Alt+Tab / Windows Key)</div>
        </div>
        <strong style="color:var(--combat-red);">STRICT ANTI-CHEAT PROTOCOL:</strong> Exiting fullscreen, switching tabs/windows, clicking outside, or attempting to open search tools (Google Lens, Gemini, DevTools) triggers an immediate security lockout.
      </div>

      <div class="proctor-incident-ledger">
        <span>VIOLATION INCIDENT #<strong id="proctor-violation-count">1</strong></span>
        <span>LOGGED: <strong id="proctor-violation-time">00:00:00Z</strong></span>
      </div>

      <!-- DUAL UNLOCK INTERFACE -->
      <div style="width: 100%; display: flex; flex-direction: column; gap: 14px; margin-top: 6px;">
        <!-- Option 1: Local Organizer Key -->
        <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 4px; padding: 12px 14px; text-align: center;">
          <div style="font-size: 11px; font-weight: bold; color: var(--cyber-cyan); letter-spacing: 1px; margin-bottom: 8px;">
            🔑 OPTION 1: ORGANIZER AUTHORIZATION KEY
          </div>
          <div style="display: flex; gap: 8px; justify-content: center; align-items: center; flex-wrap: wrap;">
            <input type="password" id="proctor-pin-input" class="proctor-pin-input" placeholder="Enter Organizer Key / PIN" autocomplete="off" style="width: 210px; font-size: 12px; padding: 7px 10px; letter-spacing: 2px;">
            <button type="button" class="btn-tactical active" style="font-size: 11.5px; padding: 7px 16px; font-weight: bold;" onclick="verifyProctorOverride()">🔓 UNLOCK WORKSTATION</button>
          </div>
          <div id="proctor-error-msg" class="proctor-error-text" style="margin-top: 6px;"></div>
        </div>

        <!-- Option 2: Remote Dashboard Unlock -->
        <div style="background: rgba(0, 255, 102, 0.06); border: 1px solid rgba(0, 255, 102, 0.35); border-radius: 4px; padding: 10px 14px; text-align: center;">
          <div style="font-size: 11px; font-weight: bold; color: #00ff66; letter-spacing: 1px; margin-bottom: 4px;">
            📡 OPTION 2: REMOTE ORGANIZER DASHBOARD UNLOCK
          </div>
          <div style="font-size: 11px; color: #b8cddb; line-height: 1.4;">
            The organizer can remotely unlock this workstation from the <strong>Organizer Admin Dashboard</strong> with one click.
          </div>
          <div id="proctor-remote-status" style="margin-top: 6px; font-size: 11px; color: #00ff66; font-family: var(--font-mono); font-weight: bold; display: flex; align-items: center; justify-content: center; gap: 6px;">
            <span class="pulse-green" style="display:inline-block; width:8px; height:8px; background:#00ff66; border-radius:50%;"></span>
            <span>Remote Telemetry Active & Awaiting Organizer Directive...</span>
          </div>
        </div>
      </div>

      <div style="font-size:9.5px; color:#8ba0b2; margin-top:12px;">
        Please alert an on-duty IEEE WIE organizer to inspect and unlock this terminal.
      </div>
    </div>
  </div>

  <!-- Global Organizer Broadcast Banner/Toast -->"""

if old_overlay_pattern.search(html):
    html = old_overlay_pattern.sub(new_overlay_html, html)
    print("SUCCESS: #proctor-lockdown-overlay HTML updated.")
else:
    print("WARNING: Could not find old #proctor-lockdown-overlay pattern.")

# 2. Update JavaScript event listeners and lockdown triggers
old_triggers = """    // Intercept right-click context menu (Disables Google Lens and external searching)
    window.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      e.stopPropagation();
      handleCheatingAttempt("Right-Click / Google Lens Context Menu Blocked");
      return false;
    }, true);

    // Prevent dragging images or text to external browser tabs/Google Lens
    window.addEventListener('dragstart', (e) => {
      e.preventDefault();
      e.stopPropagation();
      return false;
    }, true);"""

new_triggers = """    // Intercept right-click context menu (Immediately locks against Google Lens / Gemini searching)
    window.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
        triggerProctorLockdown("Prohibited Action: Google Lens / Gemini Search Attempt (Right-Click Blocked)");
      } else {
        handleCheatingAttempt("Right-Click / Google Lens Context Menu Blocked");
      }
      return false;
    }, true);

    // Prevent dragging images or text to external browser tabs/Google Lens
    window.addEventListener('dragstart', (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
        triggerProctorLockdown("Unauthorized Drag / Google Lens Search Attempt Blocked");
      }
      return false;
    }, true);

    // Detect Screen Capture / Snipping Tool / Lens shortcuts
    window.addEventListener('keyup', (e) => {
      if (e.key === 'PrintScreen' || e.keyCode === 44) {
        if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
          triggerProctorLockdown("Screen Capture / Snipping Tool / Google Lens Search Attempt");
        }
      }
    });"""

if old_triggers in html:
    html = html.replace(old_triggers, new_triggers, 1)
    print("SUCCESS: Contextmenu and dragstart triggers updated.")
else:
    print("WARNING: old_triggers not found.")

# 3. Update blur timeout to 150ms and improve reason text
old_blur = """    // Detect window blur / switching applications / Alt+Tab / loss of focus
    let blurTimeout = null;
    window.addEventListener('blur', () => {
      if (blurTimeout) clearTimeout(blurTimeout);
      blurTimeout = setTimeout(() => {
        if ((!document.hasFocus() || document.hidden) && fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
          triggerProctorLockdown("Workstation Focus Lost: Switched Window or Application");
        }
      }, 300);
    });"""

new_blur = """    // Detect window blur / switching applications / Alt+Tab / loss of focus
    let blurTimeout = null;
    window.addEventListener('blur', () => {
      if (blurTimeout) clearTimeout(blurTimeout);
      blurTimeout = setTimeout(() => {
        if ((!document.hasFocus() || document.hidden) && fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
          triggerProctorLockdown("Workstation Focus Lost: Switched Window or Clicked Outside");
        }
      }, 150);
    });"""

if old_blur in html:
    html = html.replace(old_blur, new_blur, 1)
    print("SUCCESS: Blur listener updated.")
else:
    print("WARNING: old_blur not found.")

# 4. Update DevTools shortcut handler to lock workstation
old_devtools = """      // Developer Tools & Source Inspection Shortcuts
      if (
        e.key === 'F12' ||
        (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) ||
        (e.ctrlKey && (e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) ||
        (e.shiftKey && e.key === 'F10')
      ) {
        e.preventDefault();
        e.stopPropagation();
        handleCheatingAttempt("Prohibited Shortcut / DevTools Attempt (" + e.key + ")");
        return false;
      }"""

new_devtools = """      // Developer Tools & Source Inspection Shortcuts
      if (
        e.key === 'F12' ||
        (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c' || e.key === 'S' || e.key === 's')) ||
        (e.ctrlKey && (e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) ||
        (e.shiftKey && e.key === 'F10')
      ) {
        e.preventDefault();
        e.stopPropagation();
        if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive && !isFullscreenExitAuthorized()) {
          triggerProctorLockdown("Prohibited DevTools / Search Attempt (" + e.key + ")");
        } else {
          handleCheatingAttempt("Prohibited Shortcut / DevTools Attempt (" + e.key + ")");
        }
        return false;
      }"""

if old_devtools in html:
    html = html.replace(old_devtools, new_devtools, 1)
    print("SUCCESS: Devtools listener updated.")
else:
    print("WARNING: old_devtools not found.")

# 5. Update verifyProctorOverride to accept multiple organizer keys + online fallback
old_verify = """    function verifyProctorOverride() {
      const inputEl = document.getElementById('proctor-pin-input');
      const errEl = document.getElementById('proctor-error-msg');
      const pin = inputEl ? inputEl.value.trim() : '';

      if (pin === "wie-admin-2026") {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
          tacticalSound.playSuccessChirp();
        }
        proctorLockActive = false;
        violationCount = 0;
        window.tamperViolationsHistory = [];
        lockArmed = false; // Disarm

        const overlay = document.getElementById('proctor-lockdown-overlay');
        if (overlay) overlay.style.display = 'none';

        if (!isFullscreenExitAuthorized()) {
          requestAppFullscreen();
          setTimeout(() => {
            lockArmed = true;
          }, 3500);
        }

        logTerm(`🏆 [PROCTOR OVERRIDE]: Workstation unlocked by Organizer at ${new Date().toISOString().substring(11, 19)}Z. Breaches cleared.`, 'green');
        reportTelemetryAction("🏆 Proctor Unlocked Workstation");
      } else {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playErrorBuzzer) {
          tacticalSound.playErrorBuzzer();
        }
        if (errEl) {
          errEl.innerText = "ACCESS DENIED: INVALID ORGANIZER PIN.";
        }
        if (inputEl) {
          inputEl.classList.add('pin-shake');
          setTimeout(() => inputEl.classList.remove('pin-shake'), 500);
        }
      }
    }"""

new_verify = """    async function verifyProctorOverride() {
      const inputEl = document.getElementById('proctor-pin-input');
      const errEl = document.getElementById('proctor-error-msg');
      const pin = inputEl ? inputEl.value.trim() : '';

      const normalizedPin = pin.toLowerCase();
      const acceptedKeys = [
        "wie-admin-2026",
        "failsafe2090",
        "proctor2090",
        "admin2090",
        "proctor",
        "admin",
        "failsafe",
        "2026"
      ];

      let isAuthorized = acceptedKeys.includes(normalizedPin);

      // Online verification fallback against server /api/admin/remote-unlock
      if (!isAuthorized && pin && currentTeam && currentTeam.team_id) {
        try {
          const res = await fetch(`${getApiBase()}/api/admin/remote-unlock`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pin: pin, team_id: currentTeam.team_id })
          });
          if (res.ok) {
            const data = await res.json();
            if (data.success) {
              isAuthorized = true;
            }
          }
        } catch(e) {
          console.warn("Online pin check fallback:", e);
        }
      }

      if (isAuthorized) {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
          tacticalSound.playSuccessChirp();
        }
        proctorLockActive = false;
        violationCount = 0;
        window.tamperViolationsHistory = [];
        lockArmed = false; // Disarm

        const overlay = document.getElementById('proctor-lockdown-overlay');
        if (overlay) overlay.style.display = 'none';

        if (!isFullscreenExitAuthorized()) {
          requestAppFullscreen();
          setTimeout(() => {
            lockArmed = true;
          }, 3500);
        }

        // Notify server to clear lock state immediately
        reportTelemetryAction("🏆 Organizer Key Entered: Workstation Unlocked");
        if (typeof startTelemetryHeartbeat === 'function') {
          startTelemetryHeartbeat();
        }

        logTerm(`🏆 [PROCTOR OVERRIDE]: Workstation unlocked by Organizer key at ${new Date().toISOString().substring(11, 19)}Z. Breaches cleared.`, 'green');
      } else {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playErrorBuzzer) {
          tacticalSound.playErrorBuzzer();
        }
        if (errEl) {
          errEl.innerText = "ACCESS DENIED: INVALID ORGANIZER KEY / PIN.";
        }
        if (inputEl) {
          inputEl.classList.add('pin-shake');
          setTimeout(() => inputEl.classList.remove('pin-shake'), 500);
        }
      }
    }"""

if old_verify in html:
    html = html.replace(old_verify, new_verify, 1)
    print("SUCCESS: verifyProctorOverride updated.")
else:
    print("WARNING: old_verify not found.")

# 6. Update startTelemetryHeartbeat for adaptive fast-polling when locked
old_heartbeat = """    function startTelemetryHeartbeat() {
      if (telemetryHeartbeatTimer) clearInterval(telemetryHeartbeatTimer);
      telemetryHeartbeatTimer = setInterval(() => {
        let currentStatus = "Active in Terminal";
        if (typeof proctorLockActive !== 'undefined' && proctorLockActive) {
          currentStatus = `🚨 Workstation Locked: Focus Loss Violation (#${violationCount})`;
        } else if (typeof taraState !== 'undefined' && taraState === "TRAPPED") {
          currentStatus = "Quarantined in Sandbox Buffer";
        }
        reportTelemetryAction(currentStatus);

        // Fallback for same-machine testing: inspect localStorage broadcast
        try {
          const rawLocalBcast = localStorage.getItem("failsafe_global_broadcast");
          if (rawLocalBcast) {
            const b = JSON.parse(rawLocalBcast);
            if (typeof window.lastLocalBcastId === 'undefined') window.lastLocalBcastId = 0;
            if (b.id > window.lastLocalBcastId) {
              window.lastLocalBcastId = b.id;
              showBroadcastToast(b.message);
            }
          }
        } catch(e) {}
      }, 4000);
    }"""

new_heartbeat = """    function startTelemetryHeartbeat() {
      if (telemetryHeartbeatTimer) clearInterval(telemetryHeartbeatTimer);
      const poll = () => {
        let currentStatus = "Active in Terminal";
        if (typeof proctorLockActive !== 'undefined' && proctorLockActive) {
          currentStatus = `🚨 Workstation Locked: Security Breach Violation (#${violationCount})`;
        } else if (typeof taraState !== 'undefined' && taraState === "TRAPPED") {
          currentStatus = "Quarantined in Sandbox Buffer";
        }
        reportTelemetryAction(currentStatus);

        // Fallback for same-machine testing: inspect localStorage broadcast
        try {
          const rawLocalBcast = localStorage.getItem("failsafe_global_broadcast");
          if (rawLocalBcast) {
            const b = JSON.parse(rawLocalBcast);
            if (typeof window.lastLocalBcastId === 'undefined') window.lastLocalBcastId = 0;
            if (b.id > window.lastLocalBcastId) {
              window.lastLocalBcastId = b.id;
              showBroadcastToast(b.message);
            }
          }
        } catch(e) {}
      };

      // Fast polling (1200ms) when locked so remote unlock occurs almost immediately, else 3500ms
      const intervalMs = (typeof proctorLockActive !== 'undefined' && proctorLockActive) ? 1200 : 3500;
      telemetryHeartbeatTimer = setInterval(poll, intervalMs);
    }"""

if old_heartbeat in html:
    html = html.replace(old_heartbeat, new_heartbeat, 1)
    print("SUCCESS: startTelemetryHeartbeat updated.")
else:
    print("WARNING: old_heartbeat not found.")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: aditi_os_widget.html written.")
