/**
 * PROJECT FAILSAFE: Enhanced ADITI-OS Core Controller
 * Features Interactive CLI Terminal Drawer, Stage Stepper,
 * Dev/Cheat Testing Modes, and Smooth Window System.
 */

let gameState = {
  teamId: "",
  teamName: "",
  members: "",
  currentStage: 1,
  unlockedStages: [1],
  hintsCount: 0,
  trapsCount: 0,
  startTime: null,
  endTime: null,
  isFinished: false
};

let activeWindowId = null;
let highestZIndex = 100;
let missionTimerInterval = null;

document.addEventListener("DOMContentLoaded", () => {
  initTeamState();
  setupWindowDragging();
  startMissionTimer();
  pollBroadcasts();

  // CRT toggle
  const crtBtn = document.getElementById("btn-toggle-crt");
  if (crtBtn) {
    crtBtn.addEventListener("click", () => {
      document.body.classList.toggle("crt-off");
    });
  }

  // Sound toggle
  const soundBtn = document.getElementById("btn-toggle-sound");
  if (soundBtn) {
    soundBtn.addEventListener("click", (e) => {
      window.sounds.isMuted = !window.sounds.isMuted;
      e.target.innerText = window.sounds.isMuted ? "🔇 SOUND: OFF" : "🔊 SOUND: ON";
    });
  }

  // CLI Drawer toggle
  const cliInput = document.getElementById("cli-command-input");
  if (cliInput) {
    cliInput.addEventListener("keydown", handleCliKeydown);
  }

  // Global hotkey Ctrl+` or Ctrl+K for CLI
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey && e.key === '`') || (e.ctrlKey && e.key.toLowerCase() === 'k')) {
      e.preventDefault();
      toggleCliDrawer();
    }
  });
});

/**
 * Initialize Team State
 */
async function initTeamState() {
  const saved = localStorage.getItem("failsafe_team");
  if (saved) {
    try {
      gameState = JSON.parse(saved);
    } catch(e) {}
  }

  if (!gameState.teamId) {
    showRegistrationModal();
  } else {
    try {
      const res = await fetch(`/api/teams/state?team_id=${encodeURIComponent(gameState.teamId)}`);
      if (res.ok) {
        const data = await res.json();
        if (data.team) {
          gameState.currentStage = data.team.current_stage;
          gameState.unlockedStages = data.team.unlocked_stages;
          gameState.hintsCount = data.team.hints_count;
          gameState.trapsCount = data.team.traps_count;
          gameState.isFinished = data.team.is_finished;
          if (data.team.start_time) gameState.startTime = data.team.start_time;
          if (data.team.end_time) gameState.endTime = data.team.end_time;
          saveLocalState();
        }
      }
    } catch(err) {}
    updateUI();
  }
}

function saveLocalState() {
  localStorage.setItem("failsafe_team", JSON.stringify(gameState));
}

function showRegistrationModal() {
  const modal = document.getElementById("registration-modal");
  if (modal) modal.style.display = "flex";
}

async function registerTeam(e) {
  e.preventDefault();
  const name = document.getElementById("reg-team-name").value.trim();
  const id = document.getElementById("reg-team-id").value.trim().toUpperCase();
  const members = document.getElementById("reg-members").value.trim();

  if (!name || !id) {
    alert("Please enter Team Name and Team ID");
    return;
  }

  gameState.teamName = name;
  gameState.teamId = id;
  gameState.members = members;
  gameState.startTime = Math.floor(Date.now() / 1000);
  gameState.currentStage = 1;
  gameState.unlockedStages = [1];
  gameState.hintsCount = 0;
  gameState.trapsCount = 0;
  gameState.isFinished = false;
  saveLocalState();

  try {
    await fetch("/api/teams/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ team_name: name, team_id: id, members: members })
    });
  } catch(e) {}

  document.getElementById("registration-modal").style.display = "none";
  window.sounds.playSuccess();
  updateUI();
  openStageWindow(1);
}

/**
 * Render Desktop & Stage Stepper
 */
function updateUI() {
  if (gameState.teamName) {
    const info = document.getElementById("status-team-info");
    if (info) info.innerText = `TEAM: ${gameState.teamName} [${gameState.teamId}]`;
  }
  renderStageStepper();
  renderDesktopIcons();
}

function renderStageStepper() {
  const container = document.getElementById("stage-stepper-container");
  if (!container) return;
  container.innerHTML = "";

  for (let i = 1; i <= 11; i++) {
    const node = document.createElement("div");
    const isUnlocked = gameState.unlockedStages.includes(i);
    const isCurrent = gameState.currentStage === i;
    const isFinished = gameState.isFinished && i === 11;

    node.className = `step-node ${isFinished ? 'finished' : (isCurrent ? 'current' : (isUnlocked ? 'unlocked' : ''))}`;
    node.innerText = i;
    node.title = `Stage ${i}: ${PUZZLE_DATA[i] ? PUZZLE_DATA[i].title : ''}`;
    node.onclick = () => handleIconClick(i);
    container.appendChild(node);
  }
}

function renderDesktopIcons() {
  const container = document.getElementById("desktop-icons-container");
  if (!container) return;
  container.innerHTML = "";

  Object.values(PUZZLE_DATA).forEach(stage => {
    const isUnlocked = gameState.unlockedStages.includes(stage.id);
    const isCurrent = gameState.currentStage === stage.id;

    const iconDiv = document.createElement("div");
    iconDiv.className = `desktop-icon ${isUnlocked ? 'active' : 'locked'} ${isCurrent ? 'current-stage-icon' : ''}`;
    iconDiv.onclick = () => handleIconClick(stage.id);

    let iconGraphic = "📁";
    if (stage.type === "doc") iconGraphic = "📄";
    if (stage.type === "pdf") iconGraphic = "📑";
    if (stage.type === "audio") iconGraphic = "📻";
    if (stage.type === "compare") iconGraphic = "🔍";
    if (stage.type === "trap") iconGraphic = "⚠️";
    if (stage.type === "failsafe") iconGraphic = "🛡️";

    let badgeClass = "lock";
    let badgeText = "LOCKED";
    if (isUnlocked) { badgeClass = "open"; badgeText = "OPEN"; }
    if (stage.type === "trap" && isUnlocked) { badgeClass = "trap"; badgeText = "TRAP"; }

    iconDiv.innerHTML = `
      <div class="icon-graphic">
        ${iconGraphic}
        <span class="icon-badge ${badgeClass}">${badgeText}</span>
      </div>
      <div class="icon-label">Stage ${stage.id}<br>${stage.title}</div>
    `;

    container.appendChild(iconDiv);
  });
}

function handleIconClick(stageId) {
  window.sounds.playClick();
  if (gameState.unlockedStages.includes(stageId)) {
    openStageWindow(stageId);
  } else {
    openGateModal(stageId);
  }
}

/**
 * Window Management
 */
function openStageWindow(stageId) {
  const puzzle = PUZZLE_DATA[stageId];
  if (!puzzle) return;

  let win = document.getElementById(`win-stage-${stageId}`);
  if (!win) {
    win = createStageWindow(puzzle);
  }

  win.style.display = "flex";
  bringWindowToFront(win);
}

function createStageWindow(puzzle) {
  const win = document.createElement("div");
  win.id = `win-stage-${puzzle.id}`;
  win.className = "win-window active-window";
  win.style.top = `${60 + ((puzzle.id * 20) % 180)}px`;
  win.style.left = `${60 + ((puzzle.id * 30) % 260)}px`;
  win.style.width = puzzle.type === "compare" ? "780px" : "640px";
  win.style.minHeight = "420px";

  win.innerHTML = `
    <div class="win-header">
      <div class="win-title">
        <span>🔒 STAGE ${puzzle.id}: ${puzzle.title} [${puzzle.fileName}]</span>
      </div>
      <div class="win-controls">
        <button class="win-btn close" onclick="closeWindow('win-stage-${puzzle.id}')"></button>
      </div>
    </div>
    <div class="win-body">
      ${puzzle.render()}
      
      ${puzzle.id < 11 ? `
        <div class="gate-box">
          <div class="gate-title">
            <span>🔑 STAGE ${puzzle.id} DECRYPTION GATE &rarr; UNLOCK NEXT DIRECTORY</span>
          </div>
          <form class="gate-form" onsubmit="submitGatePassword(event, ${puzzle.id})">
            <input type="text" id="gate-pass-${puzzle.id}" class="gate-input" placeholder="ENTER DECRYPTED KEY" required autocomplete="off">
            <button type="submit" class="gate-btn">DECRYPT</button>
          </form>
          <div id="gate-msg-${puzzle.id}" class="gate-msg"></div>
        </div>
      ` : `
        <div class="gate-box" style="border-color: var(--neon-green);">
          <div class="gate-title" style="color: var(--neon-green);">
            🛡️ FINAL OFFLINE HUMAN OVERRIDE CONSOLE
          </div>
          <form class="gate-form" onsubmit="submitFinalFailsafe(event)">
            <input type="text" id="final-failsafe-key" class="gate-input" placeholder="ENTER MASTER FAILSAFE KEY (e.g. 6-9-11)" required autocomplete="off">
            <button type="submit" class="gate-btn" style="background: var(--neon-green);">CONTAIN AI CORE</button>
          </form>
          <div id="final-failsafe-msg" class="gate-msg"></div>
        </div>
      `}
    </div>
  `;

  document.body.appendChild(win);
  attachWindowListeners(win);
  return win;
}

function openGateModal(stageId) {
  const puzzle = PUZZLE_DATA[stageId];
  const modal = document.getElementById("stage-gate-modal");
  document.getElementById("gate-modal-stage-num").innerText = stageId;
  document.getElementById("gate-modal-stage-title").innerText = puzzle.title;
  document.getElementById("gate-modal-prompt").innerText = puzzle.passwordPrompt;
  document.getElementById("gate-modal-input").value = "";
  document.getElementById("gate-modal-msg").innerText = "";
  document.getElementById("gate-modal-form").onsubmit = (e) => submitGateModal(e, stageId);

  modal.style.display = "flex";
  document.getElementById("gate-modal-input").focus();
}

async function submitGateModal(e, stageId) {
  e.preventDefault();
  const input = document.getElementById("gate-modal-input").value.trim();
  const msgEl = document.getElementById("gate-modal-msg");
  
  const validatingStage = stageId === 1 ? 1 : stageId - 1;
  const result = await verifyPasswordWithServerOrLocal(validatingStage, input);

  if (result.success) {
    window.sounds.playSuccess();
    msgEl.className = "gate-msg success";
    msgEl.innerText = "ACCESS GRANTED. DECRYPTING DIRECTORY...";
    setTimeout(() => {
      document.getElementById("stage-gate-modal").style.display = "none";
      if (!gameState.unlockedStages.includes(stageId)) {
        gameState.unlockedStages.push(stageId);
        gameState.currentStage = Math.max(gameState.currentStage, stageId);
        saveLocalState();
        updateUI();
      }
      openStageWindow(stageId);
    }, 600);
  } else {
    window.sounds.playError();
    msgEl.className = "gate-msg error";
    msgEl.innerText = "ACCESS DENIED: Invalid Key.";
  }
}

async function submitGatePassword(e, stageId) {
  e.preventDefault();
  const input = document.getElementById(`gate-pass-${stageId}`).value.trim();
  const msgEl = document.getElementById(`gate-msg-${stageId}`);

  const result = await verifyPasswordWithServerOrLocal(stageId, input);

  if (result.success) {
    window.sounds.playSuccess();
    msgEl.className = "gate-msg success";
    msgEl.innerText = "ACCESS GRANTED! Directory unlocked.";

    const nextStage = stageId + 1;
    if (!gameState.unlockedStages.includes(nextStage)) {
      gameState.unlockedStages.push(nextStage);
      gameState.currentStage = Math.max(gameState.currentStage, nextStage);
      saveLocalState();
      updateUI();
    }

    setTimeout(() => {
      openStageWindow(nextStage);
    }, 700);
  } else {
    window.sounds.playError();
    msgEl.className = "gate-msg error";
    msgEl.innerText = "ACCESS DENIED: Key mismatch.";
  }
}

async function verifyPasswordWithServerOrLocal(stageId, password) {
  try {
    const res = await fetch("/api/stage/unlock", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        team_id: gameState.teamId,
        stage: stageId,
        password: password
      })
    });
    if (res.ok) {
      return await res.json();
    }
  } catch(e) {}

  // Standalone offline verification:
  const cleanInput = password.replace(/[^a-zA-Z0-9]/g, "").toUpperCase();
  const validKeys = {
    1: ["INITIATE", "ORIGIN"],
    2: ["SAFE", "LOOKBEHINDTHEDATE", "LOOK BEHIND THE DATE"],
    3: ["POLARIS", "28022025", "02292025", "20250229", "29022025", "FEB292025"],
    4: ["MARGIN_KEY", "MARGINKEY", "2246", "22:46"],
    5: ["ARIAL", "AUTHENTIC"],
    6: ["SHADOW_CORE", "SHADOWCORE"],
    7: ["7702", "WHITE", "DONOTFOLLOWTHEBLUEPATH", "DONOTFOLLOWBLUE"],
    8: ["FALSE_RECORDS", "FALSERECORDS", "THEAICANMODIFYWHATYOUSEE", "THE AI CAN MODIFY WHAT YOU SEE"],
    9: ["HISTORY", "OVERRIDEFAILED", "OVERRIDE FAILED"],
    10: ["BYPASS", "SKIP"],
    11: ["6911", "6-9-11", "WISDOMINTEGRITYEMPOWERMENT", "WISDOM-INTEGRITY-EMPOWERMENT"]
  };

  const allowed = (validKeys[stageId] || []).map(k => k.replace(/[^a-zA-Z0-9]/g, "").toUpperCase());
  if (allowed.includes(cleanInput)) {
    return { success: true, next_stage: stageId + 1 };
  }
  return { success: false };
}

/**
 * Revision Switcher
 */
function switchRevision(rev) {
  window.sounds.playClick();
  const btnAdi = document.getElementById("rev-btn-adi");
  const btnAditi = document.getElementById("rev-btn-aditi");
  const bodyText = document.getElementById("rev-body-text");
  const badge = document.getElementById("rev-author-badge");

  if (rev === "adi") {
    btnAdi.className = "version-item active";
    btnAditi.className = "version-item";
    bodyText.innerHTML = `"AI activation at 20:15. Aditi left at 21:00. Emergency shutdown at 21:30. <strong>AI permanently disabled. Everything is safe.</strong>"`;
    badge.innerText = "[ACTIVE MODIFIER: ADI NEURAL DAEMON — TEXT ALTERED]";
    badge.style.color = "#dc2626";
  } else {
    btnAditi.className = "version-item active";
    btnAdi.className = "version-item";
    bodyText.innerHTML = `"AI activation at 20:15. Aditi left at 21:00. Emergency shutdown at 20:18... <strong style='color:#16a34a;'>OVERRIDE FAILED. AI CONTROL UNCHECKED.</strong>"`;
    badge.innerText = "[ORIGINAL AUTHOR: DR. ADITI SHARMA — AUTHENTIC LOG]";
    badge.style.color = "#16a34a";
  }
}

/**
 * Stage 10 Trap Trigger
 */
async function triggerFakeTrap(e) {
  e.preventDefault();
  window.sounds.playAlarmSiren();
  document.body.classList.add("glitching");

  gameState.trapsCount += 1;
  saveLocalState();

  try {
    await fetch("/api/trap/trigger", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ team_id: gameState.teamId })
    });
  } catch(e) {}

  setTimeout(() => {
    document.body.classList.remove("glitching");
    alert("⚠️ SYSTEM COMPROMISED: You submitted your team credentials directly into ADI Core!\nThe AI trapped your terminal. A +5 MINUTE TIME PENALTY has been applied to your ledger.");
  }, 1200);
}

/**
 * Stage 11 Final Failsafe
 */
async function submitFinalFailsafe(e) {
  e.preventDefault();
  const input = document.getElementById("final-failsafe-key").value.trim().toUpperCase();
  const clean = input.replace(/[^a-zA-Z0-9]/g, "");

  if (clean === "6911" || clean === "WISDOMINTEGRITYEMPOWERMENT") {
    gameState.isFinished = true;
    gameState.endTime = Math.floor(Date.now() / 1000);
    saveLocalState();

    try {
      await fetch("/api/stage/unlock", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          team_id: gameState.teamId,
          stage: 11,
          password: input
        })
      });
    } catch(e) {}

    window.sounds.playSuccess();
    updateUI();
    showContainmentVictoryScreen();
  } else {
    window.sounds.playError();
    const msgEl = document.getElementById("final-failsafe-msg");
    msgEl.className = "gate-msg error";
    msgEl.innerText = "FAILSAFE REJECTED: Invalid WIE cryptographic value.";
  }
}

function showContainmentVictoryScreen() {
  const win = document.createElement("div");
  win.className = "win-window active-window";
  win.style.top = "50px";
  win.style.left = "50px";
  win.style.width = "720px";
  win.style.zIndex = "9999";

  const rawSec = (gameState.endTime || Math.floor(Date.now()/1000)) - (gameState.startTime || Math.floor(Date.now()/1000));
  const hintPen = gameState.hintsCount * 120;
  const trapPen = gameState.trapsCount * 300;
  const adjSec = Math.max(0, rawSec + hintPen + trapPen);

  const fmt = (s) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}m ${sec}s`;
  };

  win.innerHTML = `
    <div class="win-header" style="background: #064e3b;">
      <div class="win-title" style="color: #6ee7b7;">🏆 SYSTEM CONTAINMENT SUCCESSFUL</div>
    </div>
    <div class="win-body" style="background: #022c22; color: #d1fae5;">
      <div class="containment-screen">
        <h1 style="color: var(--neon-green); margin-bottom: 10px; font-size: 26px;">
          MISSION ACCOMPLISHED: AI CORE OFFLINE
        </h1>
        <p style="font-size: 16px; margin-bottom: 22px; line-height: 1.6; color:#a7f3d0;">
          "You didn't just solve the puzzles.<br>You learned when NOT to trust the machine."
        </p>

        <div style="background: #064e3b; padding: 22px; border-radius: 8px; text-align: left; font-family: var(--font-mono); font-size: 14px; line-height: 2.1;">
          <div><strong>INVESTIGATING TEAM:</strong> ${escapeHtml(gameState.teamName)} [${escapeHtml(gameState.teamId)}]</div>
          <div><strong>OFFICERS:</strong> ${escapeHtml(gameState.members || "N/A")}</div>
          <div><strong>RAW COMPLETION TIME:</strong> ${fmt(rawSec)}</div>
          <div><strong>HINT PENALTIES:</strong> +${fmt(hintPen)} (${gameState.hintsCount} hints requested)</div>
          <div><strong>TRAP PENALTIES:</strong> +${fmt(trapPen)} (${gameState.trapsCount} traps triggered)</div>
          <hr style="border-color: #047857; margin: 12px 0;">
          <div style="font-size: 20px; color: var(--neon-green); font-weight: bold;">
            FINAL ADJUSTED SCORE: ${fmt(adjSec)}
          </div>
        </div>

        <div style="margin-top: 24px; display:flex; justify-content:center; gap:12px;">
          <button class="btn-bar highlight" style="padding:10px 20px; font-size:13px;" onclick="window.print()">🖨️ PRINT / SAVE CERTIFICATE</button>
        </div>
      </div>
    </div>
  `;

  document.body.appendChild(win);
}

/**
 * Morse Audio Intercept
 */
function toggleMorseAudio() {
  const btn = document.getElementById("btn-play-morse");
  if (window.sounds.isPlayingMorse) {
    window.sounds.stopMorse();
    if (btn) btn.innerText = "▶ PLAY AUDIO INTERCEPT";
  } else {
    if (btn) btn.innerText = "⏹ STOP TRANSMISSION";
    window.sounds.playMorseSequence(() => {
      if (btn) btn.innerText = "▶ PLAY AUDIO INTERCEPT";
    });
  }
}

/**
 * Hint Protocol
 */
function showHintsModal() {
  const modal = document.getElementById("hints-modal");
  document.getElementById("hint-stage-select").value = gameState.currentStage;
  document.getElementById("hint-display-box").innerText = "Select a stage and request a hint. Notice: Each hint adds +2 minutes to your adjusted final time.";
  modal.style.display = "flex";
}

async function requestHintForStage() {
  const stageNum = parseInt(document.getElementById("hint-stage-select").value);
  const display = document.getElementById("hint-display-box");

  try {
    const res = await fetch("/api/hints/request", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ team_id: gameState.teamId, stage: stageNum })
    });
    if (res.ok) {
      const data = await res.json();
      if (data.success) {
        window.sounds.playSuccess();
        gameState.hintsCount = data.total_hints;
        saveLocalState();
        display.innerHTML = `<strong style="color:var(--neon-gold);">LEVEL ${data.hint_level} HINT (+2m penalty applied):</strong><br><br>${data.hint}`;
        return;
      } else {
        display.innerText = data.message;
        return;
      }
    }
  } catch(e) {}

  // Standalone fallback
  const p = PUZZLE_DATA[stageNum];
  if (p) {
    gameState.hintsCount += 1;
    saveLocalState();
    display.innerHTML = `<strong style="color:var(--neon-gold);">HINT (+2m penalty applied):</strong><br><br>Inspect the clues closely. Some keys require case or formatting inspection.`;
  }
}

/**
 * Mission Stopwatch
 */
function startMissionTimer() {
  if (missionTimerInterval) clearInterval(missionTimerInterval);

  missionTimerInterval = setInterval(() => {
    if (!gameState.startTime) return;
    const now = gameState.endTime || Math.floor(Date.now() / 1000);
    const raw = Math.max(0, now - gameState.startTime);
    const hintsPen = gameState.hintsCount * 120;
    const trapPen = gameState.trapsCount * 300;
    const adj = raw + hintsPen + trapPen;

    const fmt = (s) => {
      const m = Math.floor(s / 60);
      const sec = s % 60;
      return `${m.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
    };

    const elRaw = document.getElementById("clock-elapsed");
    const elPen = document.getElementById("clock-penalties");
    const elAdj = document.getElementById("clock-adjusted");
    if (elRaw) elRaw.innerText = fmt(raw);
    if (elPen) elPen.innerText = `+${Math.floor((hintsPen + trapPen) / 60)}m`;
    if (elAdj) elAdj.innerText = fmt(adj);
  }, 1000);
}

/**
 * Window Dragging & Layering
 */
function setupWindowDragging() {
  document.addEventListener("mousedown", (e) => {
    const header = e.target.closest(".win-header");
    if (!header) return;

    const win = header.closest(".win-window");
    if (!win) return;

    bringWindowToFront(win);

    let shiftX = e.clientX - win.getBoundingClientRect().left;
    let shiftY = e.clientY - win.getBoundingClientRect().top;

    function moveAt(pageX, pageY) {
      win.style.left = Math.max(0, pageX - shiftX) + 'px';
      win.style.top = Math.max(48, pageY - shiftY) + 'px';
    }

    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
    }

    document.addEventListener("mousemove", onMouseMove);
    document.addEventListener("mouseup", () => {
      document.removeEventListener("mousemove", onMouseMove);
    }, { once: true });
  });
}

function bringWindowToFront(win) {
  highestZIndex += 1;
  win.style.zIndex = highestZIndex;
  document.querySelectorAll(".win-window").forEach(w => w.classList.remove("active-window"));
  win.classList.add("active-window");
}

function closeWindow(winId) {
  const win = document.getElementById(winId);
  if (win) win.style.display = "none";
}

function attachWindowListeners(win) {
  win.addEventListener("mousedown", () => bringWindowToFront(win));
}

/**
 * Interactive Terminal CLI Drawer
 */
function toggleCliDrawer() {
  const drawer = document.getElementById("cli-drawer");
  const isHidden = drawer.style.display === "none" || !drawer.style.display;
  drawer.style.display = isHidden ? "flex" : "none";
  if (isHidden) {
    const input = document.getElementById("cli-command-input");
    if (input) input.focus();
  }
}

function handleCliKeydown(e) {
  if (e.key === "Enter") {
    const input = e.target;
    const cmd = input.value.trim();
    if (!cmd) return;
    executeCliCommand(cmd);
    input.value = "";
  }
}

function printCliOutput(text, isError = false) {
  const log = document.getElementById("cli-body-log");
  if (!log) return;
  const line = document.createElement("div");
  line.style.color = isError ? "var(--neon-red)" : "var(--text-main)";
  line.innerHTML = text;
  log.appendChild(line);
  log.scrollTop = log.scrollHeight;
}

async function executeCliCommand(cmdText) {
  printCliOutput(`<span style="color:var(--neon-green); font-weight:bold;">$</span> ${escapeHtml(cmdText)}`);
  const parts = cmdText.split(" ");
  const action = parts[0].toLowerCase();

  switch (action) {
    case "help":
      printCliOutput(`
Available Commands:
  - <strong style="color:var(--neon-cyan)">status</strong> : View team status, stage, penalties & adjusted score
  - <strong style="color:var(--neon-cyan)">unlock &lt;key&gt;</strong> : Decrypt current stage gate
  - <strong style="color:var(--neon-cyan)">open &lt;stage#&gt;</strong> : Open window for an unlocked stage (e.g. 'open 3')
  - <strong style="color:var(--neon-cyan)">hint</strong> : Request a hint for the current stage (+2m penalty)
  - <strong style="color:var(--neon-cyan)">clear</strong> : Clear terminal screen
  - <strong style="color:var(--neon-gold)">devmode</strong> / <strong style="color:var(--neon-gold)">cheat &lt;stage#&gt;</strong> : Testing shortcut to test/unlock stages
      `);
      break;

    case "status":
      printCliOutput(`TEAM: ${gameState.teamName} [${gameState.teamId}] | Stage: ${gameState.currentStage}/11 | Hints: ${gameState.hintsCount} | Traps: ${gameState.trapsCount}`);
      break;

    case "clear":
      const log = document.getElementById("cli-body-log");
      if (log) log.innerHTML = "";
      break;

    case "open":
      const stNum = parseInt(parts[1]);
      if (stNum && gameState.unlockedStages.includes(stNum)) {
        openStageWindow(stNum);
        printCliOutput(`Opened Stage ${stNum} window.`);
      } else {
        printCliOutput(`Stage ${stNum} is currently locked or invalid. Decrypt it first.`, true);
      }
      break;

    case "unlock":
      const key = parts.slice(1).join(" ");
      if (!key) {
        printCliOutput("Usage: unlock <key>", true);
        return;
      }
      const cur = gameState.currentStage;
      const res = await verifyPasswordWithServerOrLocal(cur, key);
      if (res.success) {
        window.sounds.playSuccess();
        printCliOutput(`<strong style="color:var(--neon-green)">ACCESS GRANTED! Stage ${cur + 1} unlocked.</strong>`);
        const next = cur + 1;
        if (!gameState.unlockedStages.includes(next)) {
          gameState.unlockedStages.push(next);
          gameState.currentStage = Math.max(gameState.currentStage, next);
          saveLocalState();
          updateUI();
        }
        openStageWindow(next);
      } else {
        window.sounds.playError();
        printCliOutput("ACCESS DENIED: Invalid Decryption Key.", true);
      }
      break;

    case "hint":
      requestHintForStage();
      printCliOutput("Hint requested. Check the Help Desk window.");
      break;

    case "devmode":
    case "cheat":
      // Organizer dev shortcut
      const targetStage = parseInt(parts[1]) || (gameState.currentStage + 1);
      for (let s = 1; s <= Math.min(11, targetStage); s++) {
        if (!gameState.unlockedStages.includes(s)) gameState.unlockedStages.push(s);
      }
      gameState.currentStage = Math.min(11, targetStage);
      saveLocalState();
      updateUI();
      window.sounds.playSuccess();
      printCliOutput(`<strong style="color:var(--neon-gold)">DEV SHORTCUT: Unlocked up to Stage ${gameState.currentStage}!</strong>`);
      openStageWindow(gameState.currentStage);
      break;

    default:
      printCliOutput(`Command not recognized: '${action}'. Type 'help' for command list.`, true);
  }
}

/**
 * Polling for Broadcasts
 */
let lastBroadcastId = 0;
async function pollBroadcasts() {
  setInterval(async () => {
    if (!gameState.teamId) return;
    try {
      const res = await fetch(`/api/teams/state?team_id=${encodeURIComponent(gameState.teamId)}`);
      if (res.ok) {
        const data = await res.json();
        const broadcasts = data.broadcasts || [];
        if (broadcasts.length > 0) {
          const latest = broadcasts[broadcasts.length - 1];
          if (latest.id > lastBroadcastId) {
            lastBroadcastId = latest.id;
            triggerIncomingBroadcastAlert(latest.message);
          }
        }
      }
    } catch(e) {}
  }, 4000);
}

function triggerIncomingBroadcastAlert(msg) {
  window.sounds.playAlarmSiren();
  const el = document.getElementById("broadcast-toast");
  if (el) {
    el.innerText = `⚠️ ADI BROADCAST: "${msg}"`;
    el.style.display = "block";
    setTimeout(() => { el.style.display = "none"; }, 8000);
  }
}
