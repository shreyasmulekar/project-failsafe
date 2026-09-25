import os
import re

print("--- Implementing Persistent Clue Display ---")
with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for .active-clue-banner
clue_css = """
    /* Persistent Tactical Clue Display Banner (Stays on screen until next question) */
    .active-clue-banner {
      background: linear-gradient(90deg, rgba(255, 176, 0, 0.18), rgba(255, 215, 0, 0.08));
      border: 2px solid #ffd700;
      border-radius: 8px;
      padding: 14px 20px;
      margin-bottom: 16px;
      display: none;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 0 30px rgba(255, 215, 0, 0.35), inset 0 0 15px rgba(255, 215, 0, 0.1);
      font-family: var(--font-mono, monospace);
      animation: clue-pulse 3s infinite ease-in-out;
      position: relative;
      z-index: 10;
    }
    @keyframes clue-pulse {
      0%, 100% { box-shadow: 0 0 25px rgba(255, 215, 0, 0.3), inset 0 0 10px rgba(255, 215, 0, 0.1); }
      50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.5), inset 0 0 20px rgba(255, 215, 0, 0.2); }
    }
"""

if ".active-clue-banner" not in html:
    html = html.replace("</style>", clue_css + "\n  </style>", 1)
    print("Added .active-clue-banner CSS.")
else:
    print("CSS already present.")

# 2. Add #active-clue-banner HTML directly below #participant-directive-strip
directive_end = """        </div>
      </div>

      <div class="nexus-vault-section">"""

clue_banner_html = """        </div>
      </div>

      <!-- Persistent Tactical Clue Display Banner (Stays on page until next question) -->
      <div id="active-clue-banner" class="active-clue-banner">
        <div style="display:flex; align-items:flex-start; gap:14px; flex:1;">
          <span style="font-size:28px; line-height:1; filter:drop-shadow(0 0 8px #ffd700);">💡</span>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:4px;">
              <span style="font-size:11px; font-weight:900; color:#ffd700; letter-spacing:1.5px; text-transform:uppercase;">
                TACTICAL LIFELINE CLUE // ACTIVE FOR <span id="active-clue-stage-title" style="color:#ffffff;">STAGE 01</span>
              </span>
              <span style="font-size:10px; color:#ff003c; background:rgba(255,0,60,0.15); border:1px solid #ff003c; padding:2px 8px; border-radius:3px; font-weight:bold;">
                ⚠️ +2:00 TIME PENALTY APPLIED
              </span>
            </div>
            <div id="active-clue-text" style="font-size:15px; color:#ffffff; font-weight:bold; line-height:1.6; text-shadow:0 0 10px rgba(255,215,0,0.4); margin-top:2px;">
              <!-- Dynamic Clue Text -->
            </div>
            <div style="font-size:11px; color:#ffcc66; margin-top:5px; font-weight:600;">
              📌 This clue remains visible on your workstation for reference until you solve this question and advance to the next stage.
            </div>
          </div>
        </div>
      </div>

      <div class="nexus-vault-section">"""

if directive_end in html:
    html = html.replace(directive_end, clue_banner_html, 1)
    print("Added #active-clue-banner HTML.")
else:
    print("WARNING: directive_end not found.")

# 3. Add updateActiveClueDisplay function and update updateModalTaraBanner
target_modal_tara = """    function updateModalTaraBanner(stage, meta) {
      if (!meta || !meta.modal) return;
      const modalEl = document.getElementById(meta.modal);
      if (!modalEl) return;
      
      let banner = modalEl.querySelector(".tara-modal-guide-banner");
      if (!banner) {
        banner = document.createElement("div");
        banner.className = "tara-modal-guide-banner";
        const bodyContent = modalEl.querySelector(".mil-modal-body") || modalEl.querySelector(".modal-body") || modalEl.querySelector(".dossier-body") || modalEl;
        if (bodyContent && bodyContent.firstChild) {
          bodyContent.insertBefore(banner, bodyContent.firstChild);
        } else if (bodyContent) {
          bodyContent.appendChild(banner);
        }
      }

      banner.innerHTML = `
        <div class="tara-modal-guide-text">
          <strong>🧭 TARA'S GUIDANCE:</strong> ${meta.taraModalGuide || "Analyze the evidence above and submit the decryption key."}
        </div>
        <button type="button" class="btn-tara-point" onclick="scrollToSubmit('${meta.modal}')" style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:6px 14px; border-radius:4px; border:none; cursor:pointer; box-shadow:0 0 10px rgba(0,240,255,0.4);">👇 JUMP TO SUBMIT INPUT</button>
      `;
    }"""

replacement_modal_tara = """    function updateActiveClueDisplay() {
      const banner = document.getElementById("active-clue-banner");
      const titleEl = document.getElementById("active-clue-stage-title");
      const textEl = document.getElementById("active-clue-text");

      const stage = currentStage || 1;
      const stageInfo = STAGE_NAVIGATION_DATA[stage] || STAGE_NAVIGATION_DATA[1];
      const hasClue = (typeof cluesUsedStages !== 'undefined' && cluesUsedStages && cluesUsedStages.has(stage));

      if (hasClue && stageInfo && stageInfo.hint && currentRound === 1) {
        if (banner) {
          banner.style.display = "flex";
          if (titleEl) titleEl.innerText = `STAGE ${stage < 10 ? '0' + stage : stage}: ${stageInfo.title || stageInfo.chapter}`;
          if (textEl) textEl.innerHTML = `"${stageInfo.hint}"`;
        }
        const speech = document.getElementById("nexus-tara-speech");
        if (speech && !speech.dataset.userActive) {
          speech.innerHTML = `<strong style="color:#ffd700;">💡 ACTIVE CLUE [STAGE 0${stage}]:</strong> "${stageInfo.hint}"`;
        }
      } else {
        if (banner) {
          banner.style.display = "none";
        }
      }

      // Also refresh the modal clue banner for the current stage
      const meta = typeof NEXUS_STAGES_META !== 'undefined' ? NEXUS_STAGES_META[stage] : null;
      if (meta && typeof updateModalTaraBanner === 'function') {
        updateModalTaraBanner(stage, meta);
      }
    }
    window.updateActiveClueDisplay = updateActiveClueDisplay;

    function updateModalTaraBanner(stage, meta) {
      if (!meta || !meta.modal) return;
      const modalEl = document.getElementById(meta.modal);
      if (!modalEl) return;
      
      let banner = modalEl.querySelector(".tara-modal-guide-banner");
      if (!banner) {
        banner = document.createElement("div");
        banner.className = "tara-modal-guide-banner";
        const bodyContent = modalEl.querySelector(".mil-modal-body") || modalEl.querySelector(".modal-body") || modalEl.querySelector(".dossier-body") || modalEl;
        if (bodyContent && bodyContent.firstChild) {
          bodyContent.insertBefore(banner, bodyContent.firstChild);
        } else if (bodyContent) {
          bodyContent.appendChild(banner);
        }
      }

      const stageInfo = STAGE_NAVIGATION_DATA[stage] || STAGE_NAVIGATION_DATA[1];
      const hasClue = (typeof cluesUsedStages !== 'undefined' && cluesUsedStages && cluesUsedStages.has(stage));

      let clueHtml = "";
      if (hasClue && stageInfo && stageInfo.hint && currentRound === 1) {
        clueHtml = `
          <div style="margin-top:10px; padding:12px 16px; background:linear-gradient(90deg, rgba(255,215,0,0.18), rgba(255,176,0,0.08)); border:2px solid #ffd700; border-radius:6px; box-shadow:0 0 25px rgba(255,215,0,0.35);">
            <div style="font-size:11px; font-weight:900; color:#ffd700; letter-spacing:1px; display:flex; align-items:center; gap:8px; margin-bottom:4px;">
              <span>💡 UNLOCKED TACTICAL CLUE (+2:00 PENALTY LOGGED):</span>
            </div>
            <div style="font-size:15px; color:#ffffff; font-weight:bold; line-height:1.6; text-shadow:0 0 10px rgba(255,215,0,0.4);">
              "${stageInfo.hint}"
            </div>
            <div style="font-size:10.5px; color:#ffcc66; margin-top:4px;">
              📌 This clue stays active for reference until this stage is solved.
            </div>
          </div>
        `;
      }

      banner.innerHTML = `
        <div class="tara-modal-guide-text">
          <strong>🧭 TARA'S GUIDANCE:</strong> ${meta.taraModalGuide || "Analyze the evidence above and submit the decryption key."}
        </div>
        <button type="button" class="btn-tara-point" onclick="scrollToSubmit('${meta.modal}')" style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:6px 14px; border-radius:4px; border:none; cursor:pointer; box-shadow:0 0 10px rgba(0,240,255,0.4);">👇 JUMP TO SUBMIT INPUT</button>
        ${clueHtml}
      `;
    }"""

if target_modal_tara in html:
    html = html.replace(target_modal_tara, replacement_modal_tara, 1)
    print("Replaced updateModalTaraBanner and added updateActiveClueDisplay.")
else:
    print("WARNING: target_modal_tara not found.")

# 4. In confirmExecuteTacticalClue(), call updateActiveClueDisplay()
old_confirm = """      setTaraSpeech(`<strong style="color:#ffd700;">💡 TARA CLUE [${cluesRemaining}/3 LEFT | +2m PENALTY]:</strong> "${stageInfo.hint}"`);
      showBroadcastToast(`💡 CLUE GRANTED (+2:00 TIME PENALTY | ${cluesRemaining}/3 left): ${stageInfo.hint}`, 5000);
      reportTelemetryAction(`Clue Expended on Stage ${currentStage} (+2:00 time penalty applied, ${cluesRemaining} lifelines remaining)`);"""

new_confirm = """      setTaraSpeech(`<strong style="color:#ffd700;">💡 TARA CLUE [${cluesRemaining}/3 LEFT | +2m PENALTY]:</strong> "${stageInfo.hint}"`);
      showBroadcastToast(`💡 CLUE GRANTED (+2:00 TIME PENALTY | ${cluesRemaining}/3 left): ${stageInfo.hint}`, 5000);
      reportTelemetryAction(`Clue Expended on Stage ${currentStage} (+2:00 time penalty applied, ${cluesRemaining} lifelines remaining)`);
      if (typeof updateActiveClueDisplay === 'function') updateActiveClueDisplay();"""

if old_confirm in html:
    html = html.replace(old_confirm, new_confirm, 1)
    print("Updated confirmExecuteTacticalClue with updateActiveClueDisplay().")
else:
    print("WARNING: old_confirm not found.")

# 5. In updateNexusDashboard(), call updateActiveClueDisplay()
old_dashboard_end = """      if (btnDirectOpen) {
        btnDirectOpen.innerHTML = `⚡ OPEN STAGE ${stage < 10 ? '0' + stage : stage} DOSSIER &rarr;`;
      }
    }"""

new_dashboard_end = """      if (btnDirectOpen) {
        btnDirectOpen.innerHTML = `⚡ OPEN STAGE ${stage < 10 ? '0' + stage : stage} DOSSIER &rarr;`;
      }

      // Update persistent clue display (stays visible until next stage)
      if (typeof updateActiveClueDisplay === 'function') {
        updateActiveClueDisplay();
      }
    }"""

if old_dashboard_end in html:
    html = html.replace(old_dashboard_end, new_dashboard_end, 1)
    print("Updated updateNexusDashboard with updateActiveClueDisplay().")
else:
    print("WARNING: old_dashboard_end not found.")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: aditi_os_widget.html updated with persistent clue display.")
