import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update modal-clue-confirm style to include z-index: 99999 !important;
target_style = 'id="modal-clue-confirm" class="mil-modal" style="'
replacement_style = 'id="modal-clue-confirm" class="mil-modal" style="z-index: 99999 !important; '

if target_style in content and replacement_style not in content:
    content = content.replace(target_style, replacement_style, 1)
    print("Updated modal-clue-confirm style with z-index: 99999")
else:
    print("modal-clue-confirm style already has z-index or not found")

# 2. Update updateModalTaraBanner to include the in-modal Request Clue button
old_banner_code = '''      const stageInfo = STAGE_NAVIGATION_DATA[stage] || STAGE_NAVIGATION_DATA[1];
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
      `;'''

new_banner_code = '''      const stageInfo = STAGE_NAVIGATION_DATA[stage] || STAGE_NAVIGATION_DATA[1];
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
      } else if (currentRound === 1) {
        if (typeof cluesRemaining !== 'undefined' && cluesRemaining > 0) {
          clueHtml = `
            <div style="margin-top:10px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; background:rgba(255,215,0,0.08); border:1.5px dashed #ffd700; border-radius:6px; padding:10px 14px;">
              <div style="font-size:12px; color:#ffd700; display:flex; align-items:center; gap:8px;">
                <span>🔋 <strong>ROUND 1 LIFELINES: ${cluesRemaining}/3 LEFT</strong></span>
                <span style="color:#f87171; font-size:11.5px; font-weight:bold;">(+2:00 Time Penalty per clue)</span>
              </div>
              <button type="button" class="btn-modal-request-clue" onclick="requestTacticalClue()" style="background:#ffd700; color:#02060e; font-weight:900; font-size:12px; padding:7px 18px; border-radius:4px; border:none; cursor:pointer; box-shadow:0 0 15px rgba(255,215,0,0.4); letter-spacing:0.5px;">
                💡 REQUEST CLUE (+2 MIN PENALTY)
              </button>
            </div>
          `;
        } else {
          clueHtml = `
            <div style="margin-top:10px; background:rgba(255,0,60,0.08); border:1px solid rgba(255,0,60,0.3); border-radius:6px; padding:10px 14px; font-size:12px; color:#ff4d6d; display:flex; align-items:center; gap:8px;">
              <span>🚫 <strong>0/3 LIFELINES REMAINING:</strong> All 3 tactical clues for Round 1 have been used. You must solve this sector independently.</span>
            </div>
          `;
        }
      } else {
        clueHtml = `
          <div style="margin-top:10px; background:rgba(255,0,60,0.08); border:1px solid rgba(255,0,60,0.3); border-radius:6px; padding:10px 14px; font-size:12px; color:#ff4d6d; display:flex; align-items:center; gap:8px;">
            <span>🔒 <strong>ROUND 2 RESTRICTION:</strong> Strictly zero clues in Round 2. Decrypt using independent analysis.</span>
          </div>
        `;
      }

      banner.innerHTML = `
        <div class="tara-modal-guide-text">
          <strong>🧭 TARA'S GUIDANCE:</strong> ${meta.taraModalGuide || "Analyze the evidence above and submit the decryption key."}
        </div>
        <button type="button" class="btn-tara-point" onclick="scrollToSubmit('${meta.modal}')" style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:6px 14px; border-radius:4px; border:none; cursor:pointer; box-shadow:0 0 10px rgba(0,240,255,0.4);">👇 JUMP TO SUBMIT INPUT</button>
        ${clueHtml}
      `;'''

if old_banner_code in content:
    content = content.replace(old_banner_code, new_banner_code, 1)
    print("Updated updateModalTaraBanner with in-modal clue request UI")
else:
    print("old_banner_code not found verbatim")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved aditi_os_widget.html")
