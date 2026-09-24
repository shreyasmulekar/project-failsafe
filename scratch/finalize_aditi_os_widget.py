# scratch/finalize_aditi_os_widget.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Original length: {len(text)}")

# 1. Update submitStageDirectKey and define verifyUniversalKey
old_submit_key = """    function submitStageDirectKey(stageNum, code) {
      if (!code || !code.trim()) return;
      verifyUniversalKey(code.trim());
    }"""

new_submit_key = """    function submitStageDirectKey(stageNum, code) {
      if (!code || !code.trim()) return;
      const cleanCode = code.trim();
      const fbEl = document.getElementById(`fb-stage-${stageNum}`) || document.getElementById(`v1-modal-recovery-fb`);
      if (fbEl) {
        fbEl.innerHTML = `<span style="color:#00f0ff;">⏳ Transmitting key <code>${escapeHtml(cleanCode)}</code> to AI core...</span>`;
      }
      const termInput = document.getElementById("tactical-term-input");
      if (termInput) {
        termInput.value = `decrypt ${cleanCode}`;
        handleTermSubmit();
      } else if (typeof runChecksumScan === 'function') {
        runChecksumScan(cleanCode);
      }
    }
    window.submitStageDirectKey = submitStageDirectKey;

    function verifyUniversalKey(code) {
      submitStageDirectKey(currentStage || 1, code);
    }
    window.verifyUniversalKey = verifyUniversalKey;"""

if old_submit_key in text:
    text = text.replace(old_submit_key, new_submit_key)
    print("Updated submitStageDirectKey and defined verifyUniversalKey.")
else:
    print("Notice: old_submit_key not found verbatim, finding by regex.")
    text = re.sub(
        r'function submitStageDirectKey\(stageNum,\s*code\)\s*\{[^}]*verifyUniversalKey[^}]*\}',
        new_submit_key,
        text
    )

# 2. Add enforceRound2NoCluesProtocol and R2 guidance to renderRound2Arena
old_r2_no_clues = """      // Enforce Round 2 No-Clues Protocol
      const clueBtn = document.getElementById("btn-request-hint");
      const clueBat = document.getElementById("clue-battery-container");
      if (clueBtn) {
        clueBtn.disabled = true;
        clueBtn.style.opacity = "0.5";
        clueBtn.style.cursor = "not-allowed";
        clueBtn.title = "Clues strictly disabled in Round 2 Core Reconstruction";
        clueBtn.innerHTML = "<span>🔒 NO CLUES (ROUND 2 PROTOCOL)</span>";
      }
      if (clueBat) {
        clueBat.innerHTML = "<span style='font-size:10px; color:var(--text-muted);'>[CLUES OFFLINE]</span>";
      }"""

new_r2_no_clues = """      // Enforce Round 2 Strict No-Clues Protocol (Completely Hidden)
      enforceRound2NoCluesProtocol();"""

if old_r2_no_clues in text:
    text = text.replace(old_r2_no_clues, new_r2_no_clues)
    print("Replaced old_r2_no_clues.")

# Add enforceRound2NoCluesProtocol definition before renderRound2Arena
r2_helper_code = """
    function enforceRound2NoCluesProtocol() {
      if (currentRound >= 2) {
        // Completely remove all clue options from view in Round 2
        document.querySelectorAll('.clue-chip').forEach(el => {
          el.style.setProperty('display', 'none', 'important');
        });
        const clueBtn = document.getElementById("btn-request-hint");
        if (clueBtn) clueBtn.style.setProperty('display', 'none', 'important');
        const clueBat = document.getElementById("clue-battery-container");
        if (clueBat) clueBat.style.setProperty('display', 'none', 'important');
        const clueModal = document.getElementById("modal-hint");
        if (clueModal) clueModal.style.setProperty('display', 'none', 'important');
      } else {
        // Round 1: clues available
        document.querySelectorAll('.clue-chip').forEach(el => {
          el.style.display = '';
        });
        const clueBtn = document.getElementById("btn-request-hint");
        if (clueBtn) clueBtn.style.display = '';
        const clueBat = document.getElementById("clue-battery-container");
        if (clueBat) clueBat.style.display = '';
      }
    }
    window.enforceRound2NoCluesProtocol = enforceRound2NoCluesProtocol;

    const R2_CLICK_DIRECTIVES = {
      1: "Inspect the 3x3 symbol transformation matrix. Click one of the candidate options [OPTION A], [OPTION B], [OPTION C], or [OPTION D] to test the pattern.",
      2: "Inspect the 90° clockwise rotation sequence. Click the candidate transformation cards to inspect orientation.",
      3: "Analyze the 2D unfolded cube net. Mentally fold the faces to identify which opposite face aligns with Face E.",
      4: "Trace the row and column coordinates in the 5x5 Modulo-Polybius grid to decode the 6-letter keyword.",
      5: "Trace key positions on the physical QWERTY keyboard layout shifted 1 key rightward to restore the original letters.",
      6: "Click the toggle switches on Input Gate A, Input Gate B, and Input Gate C to achieve Output Q = 1 through the AND/OR/XOR gates.",
      7: "Inspect the mirrored horizontal text reflection. Click the [REFLECT / INVERT] button to flip and read the cleartext.",
      8: "Click the 90° and 180° rotation matrix transform buttons to deduce the required transformation angle.",
      9: "Sum the digits of the security token and repeatedly reduce to a single digital root value.",
      10: "Scan the hex sequence from left-to-right and right-to-left to locate the symmetric palindromic substring.",
      11: "Unweave the two interleaved string strands by separating odd and even character index positions.",
      12: "Calculate the total active perimeter nodes along the 28x25 grid boundary (Top 28 + Bottom 28 + Left 23 + Right 23).",
      13: "Inspect the cyclic checker generations. Deduce whether Step 6 results in 3-EMPTY or 3-FILLED blocks.",
      14: "Trace the concentric rotor dials and convert the modulo 12 jump offsets into alphabetical indices (6, 9, 14, 1, 12, 19).",
      15: "🚨 <strong>FINAL CLIMAX (THE RED QUESTION):</strong> Click the <strong>[⚡ SNAP TO 135°]</strong> button (or ↺ / ↻ buttons) to rotate Dr. Aditi's cipher wheel until the apertures expose the ultimate protocol password."
    };
"""

pos_render = text.find('function renderRound2Arena()')
if pos_render != -1 and 'enforceRound2NoCluesProtocol' not in text[:pos_render]:
    text = text[:pos_render] + r2_helper_code + "\n" + text[pos_render:]
    print("Inserted enforceRound2NoCluesProtocol and R2_CLICK_DIRECTIVES.")

# Update renderActivePuzzle in renderRound2Arena
old_render_viewport = """      // Render Active Puzzle
      const activePz = ROUND2_PUZZLE_DATA[round2CurrentStage];
      if (activePz && activePz.render) {
        viewport.innerHTML = activePz.render();
      }"""

new_render_viewport = """      // Render Active Puzzle with Illuminated Click & Submit Guidance Banner
      const activePz = ROUND2_PUZZLE_DATA[round2CurrentStage];
      if (activePz && activePz.render) {
        const clickDir = R2_CLICK_DIRECTIVES[round2CurrentStage] || "Interact with the puzzle controls in the viewport above.";
        const guideBanner = `
          <div class="r2-puzzle-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:14px; border-radius:6px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">ROUND 02 DIRECTIVES</span>
                <span style="color:#00f0ff; font-weight:bold; font-size:12px;">PUZZLE ${round2CurrentStage < 10 ? '0' + round2CurrentStage : round2CurrentStage} OF 15 // ${escapeHtml(activePz.title || '')}</span>
              </div>
              <span style="font-size:11px; color:#ff003c; font-weight:bold; border:1px solid #ff003c; padding:2px 6px; border-radius:3px;">🔒 NO CLUES (ROUND 2)</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> ${clickDir}
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Type your decrypted solution into the <span style="background:rgba(0,255,102,0.15); border:1px solid #00ff66; padding:1px 6px; border-radius:3px; color:#fff; font-weight:bold;">[PASSCODE TRANSMISSION]</span> box directly below and click <span style="background:#00f0ff; color:#000; padding:1px 6px; border-radius:3px; font-weight:bold;">[TRANSMIT CIPHER KEY &rarr;]</span>.
            </div>
          </div>
        `;
        viewport.innerHTML = guideBanner + activePz.render();
      }"""

if old_render_viewport in text:
    text = text.replace(old_render_viewport, new_render_viewport)
    print("Updated renderRound2Arena active puzzle rendering.")

# 3. Update requestTacticalClue to block in Round 2
old_req_clue = "function requestTacticalClue() {"
new_req_clue = """function requestTacticalClue() {
      if (currentRound >= 2) {
        appendTaraMessage("AI", `<strong style="color:var(--combat-red);">🔒 ROUND 2 PROTOCOL:</strong> Clues are strictly disabled in Round 2 Core Reconstruction. All 15 puzzles must be decoded through independent forensic analysis!`);
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playWarning) tacticalSound.playWarning();
        return;
      }"""

if old_req_clue in text and "if (currentRound >= 2)" not in text[text.find(old_req_clue):text.find(old_req_clue)+300]:
    text = text.replace(old_req_clue, new_req_clue, 1)
    print("Updated requestTacticalClue with strict Round 2 blocker.")

# 4. Broadcast reset on startup & Round 1 first enforcement
startup_fix = """
    // Reset broadcast every time application opens
    localStorage.removeItem("failsafe_global_broadcast");
    window.lastBroadcastId = -1;
    window.lastLocalBcastId = -1;
    const initialToast = document.getElementById("broadcast-toast");
    if (initialToast) initialToast.style.display = "none";

    // Strictly enforce Round 1 first unless Round 1 is 100% completed or test mode is unlocked
    const storedR1Stage = parseInt(localStorage.getItem('failsafe_stage') || '1', 10);
    const r1FullyFinished = (storedR1Stage >= 16 && localStorage.getItem('failsafe_r1_done') === 'true');
    if (!r1FullyFinished && !window.testModeUnlockedAll) {
      currentRound = 1;
      localStorage.setItem('failsafe_current_round', '1');
      const r2Cont = document.getElementById('round2-arena-container');
      if (r2Cont) r2Cont.style.display = 'none';
      const r1Left = document.querySelector('.forensic-sector');
      if (r1Left) r1Left.style.display = 'flex';
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'none';
      const breakModal = document.getElementById('modal-round1-break');
      if (breakModal) breakModal.style.display = 'none';
    }
"""

pos_boot = text.find('loadStoredTeamSession();')
if pos_boot != -1:
    text = text[:pos_boot] + startup_fix + "\n      " + text[pos_boot:]
    print("Inserted startup broadcast reset and Round 1 enforcement.")

# 5. Broadcast polling update: ignore historical broadcasts on first load
old_bcast_poll = """          if (data.broadcasts && data.broadcasts.length > 0) {
            const latest = data.broadcasts[data.broadcasts.length - 1];
            if (typeof window.lastBroadcastId === 'undefined') window.lastBroadcastId = 0;
            if (latest.id > window.lastBroadcastId) {
              window.lastBroadcastId = latest.id;
              showBroadcastToast(latest.message);
            }
          }"""

new_bcast_poll = """          if (data.unlock_all_levels) {
            handleUnlockAllLevelsTriggered();
          }
          if (data.lock_all_levels) {
            handleLockAllLevelsTriggered();
          }
          if (data.broadcasts && data.broadcasts.length > 0) {
            const latest = data.broadcasts[data.broadcasts.length - 1];
            if (typeof window.lastBroadcastId === 'undefined' || window.lastBroadcastId === -1) {
              // Synchronize silently on first load without popping up historical broadcasts
              window.lastBroadcastId = latest.id;
            } else if (latest.id > window.lastBroadcastId) {
              window.lastBroadcastId = latest.id;
              showBroadcastToast(latest.message);
            }
          }"""

if old_bcast_poll in text:
    text = text.replace(old_bcast_poll, new_bcast_poll)
    print("Updated broadcast polling to ignore historical messages on startup.")

# 6. Add handleUnlockAllLevelsTriggered and handleLockAllLevelsTriggered
test_mode_handlers = """
    function handleUnlockAllLevelsTriggered() {
      window.testModeUnlockedAll = true;
      console.log("🛠️ TEST MODE: Organizer unlocked all levels.");
      for (let s = 1; s <= 16; s++) {
        const meta = NEXUS_STAGES_META[s];
        if (meta && meta.targetCard) {
          const card = document.getElementById(meta.targetCard);
          if (card) {
            card.classList.remove('locked');
            card.style.opacity = '1';
            card.style.pointerEvents = 'auto';
            card.style.filter = 'none';
          }
        }
      }
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'inline-block';
      round2StagesCleared = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];

      let testBanner = document.getElementById('organizer-test-banner');
      if (!testBanner) {
        testBanner = document.createElement('div');
        testBanner.id = 'organizer-test-banner';
        testBanner.style.cssText = 'position:fixed; top:4px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(255,215,0,0.18); border:1px solid #ffd700; color:#ffd700; padding:4px 16px; border-radius:4px; font-family:var(--font-mono); font-size:11px; font-weight:bold; letter-spacing:1px; box-shadow:0 0 15px rgba(255,215,0,0.4); display:flex; gap:12px; align-items:center;';
        testBanner.innerHTML = '<span>🛠️ ORGANIZER TEST MODE: ALL LEVELS UNLOCKED</span> <button type="button" onclick="toggleRoundView()" style="background:#ffd700; color:#000; font-size:10px; font-weight:bold; border:none; padding:2px 8px; border-radius:3px; cursor:pointer;">SWITCH R1 / R2</button>';
        document.body.appendChild(testBanner);
      } else {
        testBanner.style.display = 'flex';
      }
      logTerm("🛠️ [ORGANIZER OVERRIDE]: Test Mode Activated. All 16 Round 1 Stages & 15 Round 2 Puzzles unlocked for testing.", "amber");
    }

    function handleLockAllLevelsTriggered() {
      window.testModeUnlockedAll = false;
      console.log("🔒 TEST MODE DEACTIVATED: All levels locked back to Stage 01.");
      const testBanner = document.getElementById('organizer-test-banner');
      if (testBanner) testBanner.style.display = 'none';
      handleRemoteResetTriggered();
      handleRemoteResetR2Triggered();
      currentRound = 1;
      localStorage.setItem('failsafe_current_round', '1');
      const r2Cont = document.getElementById('round2-arena-container');
      if (r2Cont) r2Cont.style.display = 'none';
      const r1Left = document.querySelector('.forensic-sector');
      if (r1Left) r1Left.style.display = 'flex';
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'none';
      logTerm("🔒 [ORGANIZER OVERRIDE]: Test Mode Deactivated. All levels locked. Workstation reset to Stage 01.", "green");
    }
"""

if 'handleUnlockAllLevelsTriggered' not in text:
    pos_reset = text.find('function handleRemoteResetR2Triggered() {')
    if pos_reset != -1:
        text = text[:pos_reset] + test_mode_handlers + "\n" + text[pos_reset:]
        print("Inserted test mode handlers.")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Final aditi_os_widget.html updated! Length: {len(text)}")
