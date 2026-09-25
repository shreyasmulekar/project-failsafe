import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. ADD modal-active-clue-popup HTML right after modal-clue-confirm
popup_html = '''
      <!-- DEDICATED PERSISTENT CLUE POPUP MODAL (Stays open until dismissed/cleared) -->
      <div id="modal-active-clue-popup" class="mil-modal" style="z-index: 100000 !important; width: min(720px, 95vw) !important; height: auto !important; max-height: 88vh !important; border: 2px solid #ffd700 !important; box-shadow: 0 0 60px rgba(255,215,0,0.4), 0 25px 70px rgba(0,0,0,0.95) !important;">
        <div class="mil-modal-header" style="background: rgba(255,215,0,0.15); border-bottom: 1px solid #ffd700; height: 44px !important; padding: 0 16px !important; display: flex; justify-content: space-between; align-items: center;">
          <div class="dossier-header-left" style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 18px;">💡</span>
            <span id="clue-popup-stage-title" style="color: #ffd700; font-weight: bold; font-size: 13.5px; letter-spacing: 1px;">
              TACTICAL CLUE TRANSMISSION // FORENSIC DOSSIER
            </span>
          </div>
          <div class="dossier-header-actions" style="display: flex; gap: 10px; align-items: center;">
            <button type="button" class="btn-dossier-back" onclick="closeModal('modal-active-clue-popup')" style="padding: 4px 12px; font-size: 11px; background: rgba(255,215,0,0.2); border: 1px solid #ffd700; color: #ffd700; cursor: pointer; border-radius: 3px; font-weight: bold;">
              ◄ MINIMIZE / BACK TO EVIDENCE
            </button>
            <button type="button" class="mil-modal-close" onclick="closeModal('modal-active-clue-popup')" style="color: #ffd700; font-size: 22px;">×</button>
          </div>
        </div>
        <div class="mil-modal-body" style="padding: 22px 26px !important; font-family: var(--font-mono, monospace); color: #f1f5f9;">
          <!-- Status / Lifeline Meter -->
          <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,215,0,0.06); border: 1px solid rgba(255,215,0,0.3); border-radius: 6px; padding: 10px 16px; margin-bottom: 18px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 11px; color: #94a3b8; text-transform: uppercase;">STATUS:</span>
              <span style="font-size: 11px; color: #ff003c; background: rgba(255,0,60,0.15); border: 1px solid #ff003c; padding: 2px 8px; border-radius: 3px; font-weight: bold;">
                ⚠️ +2:00 TIME PENALTY LOGGED
              </span>
            </div>
            <div style="text-align: right; display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; color: #94a3b8; text-transform: uppercase;">LIFELINES LEFT:</span>
              <span id="clue-popup-lifelines-left" style="font-size: 14px; font-weight: 900; color: #ffd700;">2 / 3</span>
            </div>
          </div>

          <!-- Prominent Clue Box -->
          <div style="background: linear-gradient(135deg, rgba(255,215,0,0.16) 0%, rgba(255,165,0,0.08) 100%); border: 2px solid #ffd700; border-radius: 8px; padding: 20px 22px; margin-bottom: 18px; box-shadow: 0 0 35px rgba(255,215,0,0.25);">
            <div style="font-size: 11px; font-weight: 900; color: #ffd700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
              <span>🎯 DR. ADITI / TARA INTELLIGENCE BRIEFING:</span>
            </div>
            <div id="clue-popup-body-text" style="font-size: 16px; color: #ffffff; font-weight: bold; line-height: 1.7; text-shadow: 0 0 12px rgba(255,215,0,0.45); user-select: text;">
              <!-- Dynamic Clue Content -->
            </div>
          </div>

          <!-- Reassurance Notice -->
          <div style="background: rgba(0, 240, 255, 0.05); border: 1px dashed rgba(0, 240, 255, 0.35); border-radius: 6px; padding: 12px 16px; margin-bottom: 20px; font-size: 12px; line-height: 1.6; color: #cbd5e1;">
            <strong style="color: #00f0ff;">📌 UNRESTRICTED ACCESS:</strong>
            This clue will <em>not</em> disappear after 5 seconds. It will remain accessible for this puzzle until you solve it and advance to the next stage. You can reopen this clue popup at any time by clicking the glowing <strong style="color: #ffd700;">[💡 VIEW ACTIVE CLUE]</strong> button.
          </div>

          <!-- Action Buttons -->
          <div style="display: flex; gap: 12px; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <button type="button" class="btn-tactical" onclick="closeModal('modal-active-clue-popup')" style="padding: 10px 20px; font-size: 13px; font-weight: bold; border-color: #64748b; color: #cbd5e1; cursor: pointer;">
              ◄ MINIMIZE (STAY ON EVIDENCE)
            </button>
            <button type="button" class="btn-tactical success" onclick="jumpToActiveStageSubmit()" style="background: #00f0ff; color: #02060e; font-weight: 900; padding: 10px 22px; font-size: 13px; border: none; cursor: pointer; box-shadow: 0 0 16px rgba(0,240,255,0.5);">
              🎯 GO TO DECRYPT INPUT ➔
            </button>
          </div>
        </div>
      </div>
'''

target_confirm_end = '''            <button type="button" class="btn-tactical danger" onclick="confirmExecuteTacticalClue()" style="padding:10px 22px; font-size:13px; font-weight:900; background:linear-gradient(135deg, #ff003c 0%, #b3002a 100%); color:#fff; border:none; box-shadow:0 0 16px rgba(255,0,60,0.6); cursor:pointer; letter-spacing:0.5px;">
              ⚡ CONFIRM (+2 MIN PENALTY)
            </button>
          </div>
        </div>
      </div>'''

if target_confirm_end in content and 'id="modal-active-clue-popup"' not in content:
    content = content.replace(target_confirm_end, target_confirm_end + "\n" + popup_html, 1)
    print("Inserted modal-active-clue-popup HTML")
else:
    print("modal-active-clue-popup already present or target not found")


# 2. UPDATE active-clue-banner with a clickable button to open the popup
old_active_banner = '''            <div style="font-size:11px; color:#ffcc66; margin-top:5px; font-weight:600;">
              📌 This clue remains visible on your workstation for reference until you solve this question and advance to the next stage.
            </div>
          </div>
        </div>
      </div>'''

new_active_banner = '''            <div style="font-size:11px; color:#ffcc66; margin-top:5px; font-weight:600;">
              📌 This clue remains visible on your workstation for reference until you solve this question and advance to the next stage.
            </div>
          </div>
          <div style="display:flex; align-items:center; padding-left:10px;">
            <button type="button" onclick="openActiveCluePopup()" style="background:#ffd700; color:#02060e; font-weight:900; font-size:11.5px; padding:8px 16px; border-radius:4px; border:none; cursor:pointer; box-shadow:0 0 15px rgba(255,215,0,0.5); white-space:nowrap; letter-spacing:0.5px;">
              🔍 OPEN CLUE POPUP
            </button>
          </div>
        </div>
      </div>'''

if old_active_banner in content:
    content = content.replace(old_active_banner, new_active_banner, 1)
    print("Updated active-clue-banner with Open Clue Popup button")


# 3. ADD openActiveCluePopup and jumpToActiveStageSubmit functions
functions_js = '''
    function openActiveCluePopup() {
      if (currentRound >= 2) {
        showBroadcastToast("🔒 ROUND 2: Clues are strictly disabled in the Olympiad Arena!");
        return;
      }
      const stage = currentStage || 1;
      const stageInfo = STAGE_NAVIGATION_DATA[stage] || STAGE_NAVIGATION_DATA[1];
      const hasClue = (typeof cluesUsedStages !== 'undefined' && cluesUsedStages && cluesUsedStages.has(stage));

      if (!hasClue || !stageInfo || !stageInfo.hint) {
        requestTacticalClue();
        return;
      }

      const titleEl = document.getElementById("clue-popup-stage-title");
      const lifeEl = document.getElementById("clue-popup-lifelines-left");
      const bodyEl = document.getElementById("clue-popup-body-text");

      if (titleEl) titleEl.innerText = `TACTICAL CLUE TRANSMISSION // ${stageInfo.chapter.toUpperCase()} (${stageInfo.title || 'FORENSIC DOSSIER'})`;
      if (lifeEl) lifeEl.innerText = `${cluesRemaining} / 3`;
      if (bodyEl) bodyEl.innerHTML = `"${stageInfo.hint}"`;

      if (typeof openModal === 'function') {
        openModal('modal-active-clue-popup');
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playAiChirp) tacticalSound.playAiChirp();
      }
    }
    window.openActiveCluePopup = openActiveCluePopup;

    function jumpToActiveStageSubmit() {
      if (typeof closeModal === 'function') closeModal('modal-active-clue-popup');
      const stage = currentStage || 1;
      const meta = typeof NEXUS_STAGES_META !== 'undefined' ? NEXUS_STAGES_META[stage] : null;
      if (meta && meta.modal) {
        if (typeof openModal === 'function') openModal(meta.modal);
        if (typeof scrollToSubmit === 'function') scrollToSubmit(meta.modal);
      }
    }
    window.jumpToActiveStageSubmit = jumpToActiveStageSubmit;
'''

if 'function openActiveCluePopup' not in content:
    content = content.replace('function requestTacticalClue(skipConfirm = false) {', functions_js + '\n    function requestTacticalClue(skipConfirm = false) {', 1)
    print("Added openActiveCluePopup and jumpToActiveStageSubmit functions")


# 4. UPDATE requestTacticalClue when already granted to open popup
old_already_granted = '''      if (cluesUsedStages.has(currentStage)) {
        const msg = `Operator, a tactical clue was already granted for ${stageInfo.chapter}. Re-read Dr. Aditi's intelligence in the dossier. Multiple clues cannot be expended on the same sector!`;
        appendTaraMessage("AI", msg);
        setTaraSpeech(`<span style="color:var(--hazard-amber); font-weight:bold;">${msg}</span>`);
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playWarning) tacticalSound.playWarning();
        showBroadcastToast(`⚠️ Clue already granted for ${stageInfo.chapter}!`);
        return;
      }'''

new_already_granted = '''      if (cluesUsedStages.has(currentStage)) {
        // Re-open the dedicated Clue Popup immediately so the user can read it anytime
        openActiveCluePopup();
        return;
      }'''

if old_already_granted in content:
    content = content.replace(old_already_granted, new_already_granted, 1)
    print("Updated requestTacticalClue to re-open clue popup if already granted")


# 5. UPDATE confirmExecuteTacticalClue to immediately trigger openActiveCluePopup
old_clue_confirm_toast = '''showBroadcastToast(`💡 CLUE GRANTED (+2:00 TIME PENALTY | ${cluesRemaining}/3 left): ${stageInfo.hint}`, 5000);
      reportTelemetryAction(`Clue Expended on Stage ${currentStage} (+2:00 time penalty applied, ${cluesRemaining} lifelines remaining)`);
      if (typeof updateActiveClueDisplay === 'function') updateActiveClueDisplay();'''

new_clue_confirm_toast = '''showBroadcastToast(`💡 CLUE GRANTED (+2:00 TIME PENALTY | ${cluesRemaining}/3 left) — Popup Opened!`, 8000);
      reportTelemetryAction(`Clue Expended on Stage ${currentStage} (+2:00 time penalty applied, ${cluesRemaining} lifelines remaining)`);
      if (typeof updateActiveClueDisplay === 'function') updateActiveClueDisplay();
      // Immediately display the dedicated persistent Clue Popup Modal
      setTimeout(() => {
        openActiveCluePopup();
      }, 200);'''

if old_clue_confirm_toast in content:
    content = content.replace(old_clue_confirm_toast, new_clue_confirm_toast, 1)
    print("Updated confirmExecuteTacticalClue to open clue popup on unlock")


# 6. UPDATE updateClueBatteryDisplay to change button to VIEW CLUE (ACTIVE) if already unlocked
old_ethan_btn = '''      const ethanClueBtn = document.getElementById('btn-ethan-clue');
      if (ethanClueBtn) {
        if (cluesRemaining <= 0) {
          ethanClueBtn.innerHTML = `🚫 NO CLUES (0/3)`;
          ethanClueBtn.style.borderColor = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.color = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.opacity = "0.7";
        } else {
          ethanClueBtn.innerHTML = `💡 USE CLUE (+2m)`;
          ethanClueBtn.title = `Expend a Tactical Clue (+2:00 Time Penalty added to running clock)`;
          ethanClueBtn.style.borderColor = "var(--cyber-cyan)";
          ethanClueBtn.style.color = "var(--cyber-cyan)";
          ethanClueBtn.style.opacity = "1";
        }
      }'''

new_ethan_btn = '''      const ethanClueBtn = document.getElementById('btn-ethan-clue');
      if (ethanClueBtn) {
        if (typeof cluesUsedStages !== 'undefined' && cluesUsedStages && cluesUsedStages.has(currentStage)) {
          ethanClueBtn.innerHTML = `💡 VIEW CLUE (ACTIVE)`;
          ethanClueBtn.title = `Click to re-open the tactical clue popup for Stage ${currentStage}`;
          ethanClueBtn.style.borderColor = "#ffd700";
          ethanClueBtn.style.color = "#ffd700";
          ethanClueBtn.style.boxShadow = "0 0 12px rgba(255,215,0,0.5)";
          ethanClueBtn.style.opacity = "1";
        } else if (cluesRemaining <= 0) {
          ethanClueBtn.innerHTML = `🚫 NO CLUES (0/3)`;
          ethanClueBtn.style.borderColor = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.color = "var(--combat-red, #ff003c)";
          ethanClueBtn.style.opacity = "0.7";
        } else {
          ethanClueBtn.innerHTML = `💡 USE CLUE (+2m)`;
          ethanClueBtn.title = `Expend a Tactical Clue (+2:00 Time Penalty added to running clock)`;
          ethanClueBtn.style.borderColor = "var(--cyber-cyan)";
          ethanClueBtn.style.color = "var(--cyber-cyan)";
          ethanClueBtn.style.boxShadow = "none";
          ethanClueBtn.style.opacity = "1";
        }
      }'''

if old_ethan_btn in content:
    content = content.replace(old_ethan_btn, new_ethan_btn, 1)
    print("Updated ethanClueBtn display logic to show VIEW CLUE (ACTIVE)")


# 7. UPDATE updateModalTaraBanner to include button to open popup
old_modal_clue_banner = '''            <div style="font-size:10.5px; color:#ffcc66; margin-top:4px;">
              📌 This clue stays active for reference until this stage is solved.
            </div>
          </div>'''

new_modal_clue_banner = '''            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-top:6px;">
              <span style="font-size:10.5px; color:#ffcc66;">📌 Stays active until this stage is solved.</span>
              <button type="button" onclick="openActiveCluePopup()" style="background:#ffd700; color:#02060e; font-weight:900; font-size:11px; padding:4px 12px; border-radius:3px; border:none; cursor:pointer; box-shadow:0 0 10px rgba(255,215,0,0.4);">
                🔍 EXPAND CLUE POPUP
              </button>
            </div>
          </div>'''

if old_modal_clue_banner in content:
    content = content.replace(old_modal_clue_banner, new_modal_clue_banner, 1)
    print("Updated updateModalTaraBanner with Expand Clue Popup button")


# 8. Close modal-active-clue-popup when stage is cleared
old_record_cleared = '''function recordStageCleared(stageNum) {
      // Auto-close completed stage evidence modal to reveal newly unlocked stage
      document.querySelectorAll('.mil-modal.active-modal, .evidence-modal').forEach(m => {
        if (m.id !== 'team-auth-modal' && m.id !== 'proctor-lockdown-overlay' && m.id !== 'victory-celebration-modal') {
          m.style.display = 'none';
          m.classList.remove('active-modal');
        }
      });'''

new_record_cleared = '''function recordStageCleared(stageNum) {
      if (typeof closeModal === 'function') {
        closeModal('modal-active-clue-popup');
      }
      // Auto-close completed stage evidence modal to reveal newly unlocked stage
      document.querySelectorAll('.mil-modal.active-modal, .evidence-modal').forEach(m => {
        if (m.id !== 'team-auth-modal' && m.id !== 'proctor-lockdown-overlay' && m.id !== 'victory-celebration-modal') {
          m.style.display = 'none';
          m.classList.remove('active-modal');
        }
      });'''

if old_record_cleared in content:
    content = content.replace(old_record_cleared, new_record_cleared, 1)
    print("Updated recordStageCleared to close modal-active-clue-popup")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved aditi_os_widget.html successfully")
