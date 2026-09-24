# refine_aditi_os_nexus.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def build_redesign():
    with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. NEXUS 2090 CSS
    nexus_css = """
    /* ==========================================================================
       NEXUS 2090 SCI-FI DASHBOARD THEME (IEEE WIE FORENSIC AI ESCAPE ROOM)
       ========================================================================== */
    :root {
      --nexus-bg: #070d18;
      --nexus-card-bg: rgba(13, 21, 39, 0.82);
      --nexus-card-border: rgba(0, 240, 255, 0.22);
      --nexus-cyan: #00f0ff;
      --nexus-blue: #3b82f6;
      --nexus-purple: #8b5cf6;
      --nexus-glow: 0 0 20px rgba(0, 240, 255, 0.35);
      --nexus-font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    body {
      background: radial-gradient(circle at 50% 15%, #0b172a 0%, #050a14 75%, #02050a 100%) !important;
      font-family: var(--nexus-font-sans), monospace;
      color: #e2e8f0;
      overflow-x: hidden;
    }

    /* NEXUS Top Header */
    .nexus-header {
      height: 64px;
      background: rgba(7, 13, 24, 0.95);
      border-bottom: 1px solid var(--nexus-card-border);
      backdrop-filter: blur(16px);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      position: relative;
      z-index: 1000;
    }
    .nexus-logo-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .nexus-logo-icon {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, var(--nexus-cyan), var(--nexus-blue));
      clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 15px rgba(0, 240, 255, 0.6);
      font-weight: 900;
      color: #030712;
      font-size: 18px;
    }
    .nexus-brand-text {
      display: flex;
      flex-direction: column;
    }
    .nexus-brand-title {
      font-size: 17px;
      font-weight: 900;
      letter-spacing: 2px;
      background: linear-gradient(90deg, #ffffff, #00f0ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .nexus-brand-sub {
      font-size: 9.5px;
      letter-spacing: 1.5px;
      color: #64748b;
      font-family: var(--font-mil);
    }

    /* Search / AI Command Bar */
    .nexus-search-pill {
      display: flex;
      align-items: center;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(0, 240, 255, 0.28);
      border-radius: 24px;
      padding: 6px 18px;
      width: 380px;
      max-width: 30vw;
      gap: 10px;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.4);
    }
    .nexus-search-input {
      background: transparent;
      border: none;
      color: #f1f5f9;
      font-size: 12px;
      flex: 1;
      outline: none;
      font-family: var(--nexus-font-sans);
    }

    /* User Profile Pill */
    .nexus-user-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(0, 240, 255, 0.25);
      border-radius: 20px;
      padding: 4px 14px 4px 6px;
      cursor: pointer;
    }
    .nexus-user-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #00f0ff;
      border: 1.5px solid #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      box-shadow: 0 0 10px rgba(0,240,255,0.5);
    }

    /* NEXUS Dashboard Main Layout */
    .nexus-dashboard-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding: 18px 24px 80px 24px;
      overflow-y: auto;
      position: relative;
      z-index: 10;
    }

    /* Upper Row: Hero Card (Left) + AI Companion Card (Right) */
    .nexus-top-row {
      display: grid;
      grid-template-columns: 1.45fr 1fr;
      gap: 16px;
      min-height: 240px;
    }

    /* Cinematic Hero Card */
    .nexus-hero-card {
      background: linear-gradient(135deg, rgba(14, 27, 51, 0.9) 0%, rgba(9, 16, 31, 0.95) 100%);
      border: 1px solid var(--nexus-card-border);
      border-radius: 14px;
      padding: 24px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(0, 240, 255, 0.2);
    }
    .nexus-hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 240, 255, 0.12);
      border: 1px solid rgba(0, 240, 255, 0.4);
      color: var(--nexus-cyan);
      font-size: 10.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
      letter-spacing: 1px;
      width: fit-content;
      margin-bottom: 8px;
    }
    .nexus-hero-title {
      font-size: 24px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 1px;
      text-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
      margin-bottom: 6px;
    }
    .nexus-hero-tags {
      font-size: 11.5px;
      color: #94a3b8;
      margin-bottom: 12px;
      display: flex;
      gap: 12px;
    }
    .nexus-hero-summary {
      font-size: 13px;
      line-height: 1.6;
      color: #cbd5e1;
      max-width: 620px;
      margin-bottom: 20px;
    }
    .nexus-hero-actions {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    .btn-nexus-primary {
      background: linear-gradient(90deg, #00f0ff, #0099ff);
      color: #020612;
      font-weight: 800;
      font-size: 12px;
      padding: 10px 22px;
      border-radius: 20px;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
      transition: all 0.2s;
    }
    .btn-nexus-primary:hover {
      box-shadow: 0 0 28px rgba(0, 240, 255, 0.75);
      transform: translateY(-1px);
    }
    .btn-nexus-secondary {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(0, 240, 255, 0.35);
      color: #f1f5f9;
      font-weight: 700;
      font-size: 11.5px;
      padding: 10px 18px;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-nexus-secondary:hover {
      background: rgba(0, 240, 255, 0.15);
      border-color: #00f0ff;
    }

    /* AI Assistant Card (Top Right) */
    .nexus-assistant-card {
      background: linear-gradient(135deg, rgba(13, 21, 39, 0.92) 0%, rgba(8, 14, 26, 0.95) 100%);
      border: 1px solid var(--nexus-card-border);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
      position: relative;
    }
    .nexus-assistant-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 10px;
    }
    .nexus-assistant-avatar {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      border: 2px solid var(--nexus-cyan);
      box-shadow: 0 0 16px rgba(0, 240, 255, 0.6);
      background: #020712;
      overflow: hidden;
      flex-shrink: 0;
      position: relative;
    }
    .nexus-speech-bubble {
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid rgba(0, 240, 255, 0.3);
      border-radius: 10px;
      padding: 10px 14px;
      font-size: 12px;
      line-height: 1.6;
      color: #e2e8f0;
      margin-bottom: 12px;
      position: relative;
      min-height: 52px;
    }
    .nexus-assistant-chips {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }
    .nexus-telemetry-gauges {
      display: flex;
      justify-content: space-between;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 8px;
      font-size: 10.5px;
      color: #94a3b8;
    }
    .nexus-gauge-val {
      font-weight: 800;
      color: var(--nexus-cyan);
      font-size: 12px;
    }

    /* Lower Section: Evidence Vault Cards Grid (Clean, Uncluttered) */
    .nexus-vault-section {
      background: rgba(9, 16, 31, 0.6);
      border: 1px solid rgba(0, 240, 255, 0.15);
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
    }
    .nexus-vault-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }
    .nexus-vault-title {
      font-size: 15px;
      font-weight: 800;
      color: #fff;
      letter-spacing: 1px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nexus-tabs {
      display: flex;
      gap: 8px;
    }
    .nexus-tab {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #94a3b8;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 16px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .nexus-tab.active, .nexus-tab:hover {
      background: rgba(0, 240, 255, 0.15);
      border-color: var(--nexus-cyan);
      color: #fff;
    }

    /* Clean Card Grid */
    .nexus-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 14px;
    }
    .nexus-clean-card {
      background: rgba(13, 21, 39, 0.7);
      border: 1px solid rgba(0, 240, 255, 0.18);
      border-radius: 10px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      min-height: 120px;
    }
    .nexus-clean-card:hover {
      transform: translateY(-3px);
      border-color: var(--nexus-cyan);
      box-shadow: 0 8px 24px rgba(0, 240, 255, 0.25);
      background: rgba(18, 30, 56, 0.85);
    }
    .nexus-clean-card.active-objective {
      border: 2px solid var(--nexus-cyan);
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.45);
      background: rgba(0, 240, 255, 0.08);
      animation: nexus-card-pulse 2s infinite ease-in-out;
    }
    @keyframes nexus-card-pulse {
      0%, 100% { box-shadow: 0 0 15px rgba(0, 240, 255, 0.3); }
      50% { box-shadow: 0 0 30px rgba(0, 240, 255, 0.7); border-color: #ffffff; }
    }
    .nexus-card-topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .nexus-stage-tag {
      font-size: 9.5px;
      font-weight: 800;
      color: var(--nexus-cyan);
      background: rgba(0, 240, 255, 0.12);
      border: 1px solid rgba(0, 240, 255, 0.3);
      padding: 2px 7px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .nexus-card-icon {
      font-size: 24px;
      margin-bottom: 6px;
    }
    .nexus-card-name {
      font-size: 12.5px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .nexus-card-status {
      font-size: 10px;
      color: #94a3b8;
    }

    /* Floating Bottom Dock (Quick Passcode & Collapsible Terminal Toggle) */
    .nexus-bottom-dock {
      position: fixed;
      bottom: 14px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(10, 18, 32, 0.95);
      border: 1px solid rgba(0, 240, 255, 0.4);
      border-radius: 30px;
      padding: 5px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.8), 0 0 20px rgba(0, 240, 255, 0.2);
      z-index: 10000;
      backdrop-filter: blur(14px);
    }
    .nexus-dock-input {
      background: rgba(3, 7, 18, 0.7);
      border: 1px solid rgba(0, 240, 255, 0.3);
      color: #fff;
      font-family: var(--font-mil);
      font-size: 12px;
      padding: 6px 12px;
      border-radius: 16px;
      width: 220px;
      outline: none;
    }
    .nexus-dock-btn {
      background: var(--nexus-cyan);
      color: #020612;
      font-weight: 800;
      font-size: 11px;
      padding: 6px 16px;
      border-radius: 16px;
      border: none;
      cursor: pointer;
      transition: all 0.2s;
    }
    .nexus-dock-btn:hover {
      box-shadow: 0 0 15px rgba(0, 240, 255, 0.7);
    }
    .nexus-dock-toggle {
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #94a3b8;
      font-size: 10.5px;
      padding: 5px 12px;
      border-radius: 16px;
      cursor: pointer;
    }
    .nexus-dock-toggle:hover {
      color: #fff;
      border-color: var(--nexus-cyan);
    }

    /* Sliding Terminal Drawer */
    #terminal-section.drawer-mode {
      position: fixed;
      bottom: 56px;
      right: 24px;
      width: 520px;
      max-width: 90vw;
      height: 380px;
      border-radius: 10px;
      z-index: 11000;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.9), 0 0 25px rgba(0, 240, 255, 0.3);
      display: none;
    }
    """

    if "/* ==========================================================================\n       NEXUS 2090 SCI-FI DASHBOARD THEME" not in html:
        html = html.replace("</style>", nexus_css + "\n</style>", 1)

    # 2. NEXUS Header Replacement
    nexus_header = """  <!-- NEXUS 2090 Top Navigation Bar -->
  <header class="nexus-header">
    <div class="nexus-logo-group">
      <div class="nexus-logo-icon">N</div>
      <div class="nexus-brand-text">
        <span class="nexus-brand-title">NEXUS 2090</span>
        <span class="nexus-brand-sub">PROJECT FAILSAFE // IEEE WIE ESCAPE ROOM</span>
      </div>
    </div>

    <!-- AI Search & Directive Bar -->
    <div class="nexus-search-pill" title="Ask Tara AI where to click or search forensic logs">
      <span style="color:var(--nexus-cyan); font-size:13px;">🔍</span>
      <input type="text" id="nexus-search-bar" class="nexus-search-input" placeholder="Ask Tara AI... (e.g. 'Where do I click?', 'who is ishaan')" onkeydown="if(event.key==='Enter') handleNexusSearch()">
      <span style="color:#64748b; font-size:12px; cursor:pointer;" onclick="triggerTaraWhereToLook()" title="Summon Tara AI Guide">🎙️</span>
    </div>

    <!-- Telemetry Clock & Status -->
    <div style="display:flex; align-items:center; gap:16px; font-size:11px; color:#94a3b8; font-family:var(--font-mil);">
      <span>Sat, 17 Jan 2090</span>
      <span>•</span>
      <span id="mil-utc-clock" style="color:var(--nexus-cyan); font-weight:bold;">22:46:00Z</span>
      <span>•</span>
      <span>Bengaluru 22°C ☁️</span>
    </div>

    <!-- User Profile & Action Pills -->
    <div style="display:flex; align-items:center; gap:10px;">
      <button id="btn-request-fs-exit" class="btn-tactical" onclick="requestFullscreenExitPermission()" style="background:rgba(255,176,0,0.15); border-color:#ffb000; color:#ffb000; font-weight:800; font-size:10px;" title="Request permission from Organizer to exit Chrome fullscreen">
        🔓 REQUEST FULLSCREEN EXIT
      </button>

      <button id="btn-switch-r2" class="btn-tactical" onclick="toggleRoundView()" style="display:none; background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff; font-weight:900; font-size:10px;">
        🎯 ROUND 2 ARENA
      </button>

      <button class="btn-tactical" onclick="toggleFullscreen()" style="font-size:10px;" title="Toggle Fullscreen Mode">
        ⛶ FULLSCREEN
      </button>

      <button id="btn-tactical-audio" class="btn-tactical" onclick="toggleTacticalAudio()" style="font-size:10px;">
        🔊 AUDIO
      </button>

      <div class="nexus-user-pill" onclick="showTeamAuthModal()" title="Switch or view Team credentials">
        <div class="nexus-user-avatar">👤</div>
        <div style="display:flex; flex-direction:column; text-align:left;">
          <span id="header-team-badge" style="font-size:11px; font-weight:800; color:#fff;">TEAM-01</span>
          <span style="font-size:8.5px; color:#00f0ff; letter-spacing:0.5px;">Level 82 • Elite Investigator</span>
        </div>
      </div>
    </div>
  </header>"""

    # Replace <header class="command-header">...</header>
    header_pattern = re.compile(r'<header class="command-header">.*?</header>', re.DOTALL)
    if header_pattern.search(html):
        html = header_pattern.sub(nexus_header, html, count=1)

    # 3. Replace ethan-ai-deck with NEXUS Top Section (Hero Card + AI Assistant Card)
    nexus_top_section = """  <!-- NEXUS 2090 Dashboard Viewport -->
  <div class="nexus-dashboard-container">
    
    <!-- Top Row: Hero Objective Card (Left) + Interactive Tara Assistant (Right) -->
    <div class="nexus-top-row">
      
      <!-- Featured Active Mission Hero Card (STARFALL ODYSSEY Style) -->
      <div class="nexus-hero-card">
        <div>
          <div class="nexus-hero-badge">
            <span>✨ AI RECOMMENDED // ACTIVE OBJECTIVE</span>
          </div>
          <h1 id="nexus-hero-title" class="nexus-hero-title">STAGE 01: ISHAAN RECOVERY TERMINAL</h1>
          <div id="nexus-hero-tags" class="nexus-hero-tags">
            <span>ACT I: THE LAB BREACH</span>
            <span>•</span>
            <span>FORENSIC BOOT SEQUENCE</span>
            <span>•</span>
            <span style="color:var(--nexus-cyan);">LEVEL 01</span>
          </div>
          <p id="nexus-hero-summary" class="nexus-hero-summary">
            ISHAAN's 5-command boot sequence was corrupted during Dr. Aditi's emergency departure. Restore the missing kernel authorization verb to regain control of the subsystem.
          </p>
        </div>

        <div class="nexus-hero-actions">
          <button type="button" class="btn-nexus-primary" onclick="openActiveStageModal()">
            <span>🔍 INVESTIGATE EVIDENCE (EXPAND) &rarr;</span>
          </button>
          <button type="button" class="btn-nexus-secondary" onclick="triggerTaraWhereToLook()">
            <span>🧭 WHERE DO I CLICK?</span>
          </button>
        </div>
      </div>

      <!-- Interactive Tara AI Assistant Card (AI GAMING ASSISTANT // NEXA Style) -->
      <div class="nexus-assistant-card">
        <div>
          <div class="nexus-assistant-header">
            <div class="nexus-assistant-avatar">
              <canvas id="canvas-ethan-avatar" width="48" height="48" class="ethan-neural-eye"></canvas>
            </div>
            <div>
              <div style="font-size:13px; font-weight:900; color:#fff; letter-spacing:0.5px;">TARA // AI COMPANION</div>
              <div style="font-size:10px; color:var(--nexus-cyan);">Always by your side • Neural Sync 99.8%</div>
            </div>
          </div>

          <!-- Dynamic Conversational Speech Bubble -->
          <div id="nexus-tara-speech" class="nexus-speech-bubble">
            "Agent, let's begin! Click on <strong>[ISHAAN Recovery Terminal]</strong> below to inspect the 5-command lifecycle and recover the missing verb."
          </div>

          <!-- Quick Action Guidance Chips -->
          <div class="nexus-assistant-chips">
            <button class="chip-ethan" onclick="triggerTaraWhereToLook()" style="border-color:var(--nexus-cyan); color:var(--nexus-cyan); font-weight:800;">🧭 WHERE TO CLICK?</button>
            <button class="chip-ethan clue-chip" onclick="sendTaraQuick('clue')">⚡ REQUEST CLUE</button>
            <button class="chip-ethan" onclick="sendTaraQuick('story')">📜 MISSION STORY</button>
            <button class="chip-ethan" onclick="openActiveStageModal()">🔍 OPEN DOSSIER</button>
          </div>
        </div>

        <!-- Real-Time Hardware & Quantum Telemetry Gauges -->
        <div class="nexus-telemetry-gauges">
          <div>CPU: <span class="nexus-gauge-val">12%</span></div>
          <div>GPU: <span class="nexus-gauge-val">98%</span></div>
          <div>RAM: <span class="nexus-gauge-val">64%</span></div>
          <div>TEMP: <span class="nexus-gauge-val">42°C</span></div>
          <div>BUS: <span class="nexus-gauge-val" style="color:#00ff88;">4.8 TB/S</span></div>
        </div>
      </div>

    </div>

    <!-- Evidence Vault (YOUR LIBRARY Style - Clean, Uncluttered Cards Grid) -->
    <div class="nexus-vault-section">
      <div class="nexus-vault-header">
        <div class="nexus-vault-title">
          <span>📁 FORENSIC EVIDENCE VAULT // 11 CHRONOLOGICAL STAGES</span>
        </div>
        <div class="nexus-tabs">
          <button class="nexus-tab active" onclick="filterNexusCards('all')">All Stages (11)</button>
          <button class="nexus-tab" onclick="filterNexusCards('act1')">Act I: Breach</button>
          <button class="nexus-tab" onclick="filterNexusCards('act2')">Act II: Infiltration</button>
          <button class="nexus-tab" onclick="filterNexusCards('act3')">Act III: Resistance</button>
          <button class="nexus-tab" onclick="filterNexusCards('act4')">Act IV: Failsafe</button>
        </div>
      </div>

      <!-- 11 Clean Visual Cards (No Clutter, Click to Expand) -->
      <div class="nexus-cards-grid" id="nexus-cards-grid">
        
        <!-- Stage 01 -->
        <div class="nexus-clean-card active-objective" id="card-recovery-term" data-act="act1" onclick="openModal('modal-recovery')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 01</span>
            <span style="font-size:10px; color:#00ff88;">● ACTIVE</span>
          </div>
          <div class="nexus-card-icon">💻</div>
          <div class="nexus-card-name">ISHAAN_Recovery.term</div>
          <div class="nexus-card-status">Boot Lifecycle • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 02 -->
        <div class="nexus-clean-card" id="card-memory" data-act="act1" onclick="openModal('modal-memory')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 02</span>
            <span style="font-size:10px; color:#ffb000;">● REORDER</span>
          </div>
          <div class="nexus-card-icon">🧠</div>
          <div class="nexus-card-name">ISHAAN_Memory.core</div>
          <div class="nexus-card-status">Timeline Memory • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 03 -->
        <div class="nexus-clean-card" id="card-acrostic" data-act="act1" onclick="openModal('modal-acrostic')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 03</span>
            <span style="font-size:10px; color:#94a3b8;">● CIPHER</span>
          </div>
          <div class="nexus-card-icon">📝</div>
          <div class="nexus-card-name">Aditi_Memo.doc</div>
          <div class="nexus-card-status">Acrostic Note • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 04 -->
        <div class="nexus-clean-card" id="card-timeline" data-act="act1" onclick="openModal('modal-incident-logs')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 04</span>
            <span style="font-size:10px; color:#94a3b8;">● LOGS</span>
          </div>
          <div class="nexus-card-icon">📅</div>
          <div class="nexus-card-name">Incident_Logs.doc</div>
          <div class="nexus-card-status">Timestamp Audit • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 05 -->
        <div class="nexus-clean-card" id="card-clearance" data-act="act2" onclick="openModal('modal-clearance')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 05</span>
            <span style="font-size:10px; color:#94a3b8;">● A1Z26</span>
          </div>
          <div class="nexus-card-icon">🔢</div>
          <div class="nexus-card-name">Clearance_Code.txt</div>
          <div class="nexus-card-status">Alphabet Index • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 06 -->
        <div class="nexus-clean-card" id="card-comments" data-act="act2" onclick="openModal('modal-comments')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 06</span>
            <span style="font-size:10px; color:#94a3b8;">● METADATA</span>
          </div>
          <div class="nexus-card-icon">💬</div>
          <div class="nexus-card-name">System_Diagnostics.doc</div>
          <div class="nexus-card-status">Resolved Notes • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 07 -->
        <div class="nexus-clean-card" id="card-font" data-act="act2" onclick="openModal('modal-font')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 07</span>
            <span style="font-size:10px; color:#94a3b8;">● TYPOGRAPHY</span>
          </div>
          <div class="nexus-card-icon">🔤</div>
          <div class="nexus-card-name">AUTHENTIC_LOG.doc</div>
          <div class="nexus-card-status">Font Verification • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 08 -->
        <div class="nexus-clean-card" id="card-morse" data-act="act3" onclick="openModal('modal-spectro')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 08</span>
            <span style="font-size:10px; color:#94a3b8;">● AUDIO</span>
          </div>
          <div class="nexus-card-icon">📻</div>
          <div class="nexus-card-name">audio_log_07.mp3</div>
          <div class="nexus-card-status">Morse Waveform • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 09 -->
        <div class="nexus-clean-card" id="card-version" data-act="act3" onclick="openModal('modal-version-hist')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 09</span>
            <span style="font-size:10px; color:#94a3b8;">● ROLLBACK</span>
          </div>
          <div class="nexus-card-icon">🕒</div>
          <div class="nexus-card-name">VERSION_SCRUB</div>
          <div class="nexus-card-status">Git Reflog Audit • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 10 -->
        <div class="nexus-clean-card" id="card-trap" data-act="act4" onclick="triggerLockdownTrap()">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#ff003c; border-color:#ff003c;">STAGE 10</span>
            <span style="font-size:10px; color:#ff003c;">☠️ HONEYPOT</span>
          </div>
          <div class="nexus-card-icon" style="color:#ff003c;">⚠️</div>
          <div class="nexus-card-name">DO_NOT_RUN.exe</div>
          <div class="nexus-card-status">Quarantine Trap • Bypass with Key &rarr;</div>
        </div>

        <!-- Stage 11 -->
        <div class="nexus-clean-card" id="card-failsafe" data-act="act4" onclick="openModal('modal-failsafe')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:var(--nexus-cyan);">STAGE 11</span>
            <span style="font-size:10px; color:var(--nexus-cyan);">🛡️ MASTER</span>
          </div>
          <div class="nexus-card-icon" style="color:var(--nexus-cyan);">🏆</div>
          <div class="nexus-card-name">WIE_Core_Values.doc</div>
          <div class="nexus-card-status">Master Failsafe • Final Sequence &rarr;</div>
        </div>

      </div>
    </div>

  </div>

  <!-- Floating Bottom Dock for Fast Solution Submission -->
  <div class="nexus-bottom-dock">
    <span style="font-size:11px; font-weight:800; color:var(--nexus-cyan); letter-spacing:1px;">🔑 QUICK DECRYPT:</span>
    <input type="text" id="nexus-dock-passcode" class="nexus-dock-input" placeholder="Enter decrypted key (e.g. ACCESS, SAFE)..." onkeydown="if(event.key==='Enter') submitNexusDockCode()">
    <button type="button" class="nexus-dock-btn" onclick="submitNexusDockCode()">TRANSMIT &rarr;</button>
    <button type="button" class="nexus-dock-toggle" onclick="toggleTerminalDrawer()">>_ TERMINAL LOGS</button>
  </div>"""

    # Replace ethan-ai-deck
    deck_pattern = re.compile(r'<section class="ethan-ai-deck".*?</section>', re.DOTALL)
    if deck_pattern.search(html):
        html = deck_pattern.sub(nexus_top_section, html, count=1)

    # In forensic-sector, hide the old matrix divider list so only the clean grid is shown,
    # but keep all the modals intact!
    html = html.replace('<div class="icon-matrix">', '<div class="icon-matrix" style="display:none;">')

    # Update tactical-terminal to be in drawer-mode
    html = html.replace('<section class="tactical-terminal" id="terminal-section">', '<section class="tactical-terminal drawer-mode" id="terminal-section">')

    # Add JavaScript functions to power the interactive Nexus UI
    nexus_js = """
    // ==========================================================================
    // NEXUS 2090 INTERACTIVE ENGINE & TARA SMART GUIDANCE
    // ==========================================================================
    const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: ISHAAN RECOVERY TERMINAL",
        tags: "ACT I: THE LAB BREACH • FORENSIC BOOT SEQUENCE • LEVEL 01",
        summary: "ISHAAN's 5-command boot sequence was corrupted during Dr. Aditi's emergency departure. Restore the missing kernel authorization verb.",
        modal: "modal-recovery",
        targetCard: "card-recovery-term",
        taraSpeech: "Agent, let's begin! Click on <strong>[ISHAAN Recovery Terminal]</strong> below to inspect the 5-command lifecycle and recover the missing verb ('ACCESS')."
      },
      2: {
        title: "STAGE 02: ISHAAN MEMORY CORE",
        tags: "ACT I: THE LAB BREACH • RECOVERED RECALL FRAGMENTS • LEVEL 02",
        summary: "6 memory fragments recovered from the neural core crash. Arrange them from earliest to latest chronological order.",
        modal: "modal-memory",
        targetCard: "card-memory",
        taraSpeech: "Memory core located! Click on <strong>[ISHAAN Memory Core]</strong> below and rearrange the 6 memory shards into chronological order ('123456')."
      },
      3: {
        title: "STAGE 03: ADITI MEMO STEGANOGRAPHY",
        tags: "ACT I: THE LAB BREACH • TEXTUAL INTEGRITY ENCODING • LEVEL 03",
        summary: "Dr. Aditi concealed emergency signals in her morning directives. Examine the initial characters of each sentence.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Notice the acrostic patterns! Click on <strong>[Aditi Memo]</strong> and read the first letter of each sentence: S-A-F-E."
      },
      4: {
        title: "STAGE 04: INCIDENT TIMESTAMP LOGS",
        tags: "ACT I: THE LAB BREACH • TEMPORAL ANOMALY • LEVEL 04",
        summary: "An impossible calendar entry was forged into the StratCom security logs. Detect the impossible date.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on <strong>[Incident Logs]</strong>. 2025 wasn't a leap year, so Feb 29 cannot exist ('28/02/2025')!"
      },
      5: {
        title: "STAGE 05: CLEARANCE ELEVATION",
        tags: "ACT II: INFILTRATION • A1Z26 POSITIONAL CIPHER • LEVEL 05",
        summary: "Interception telex indices correlate to standard alphabet offsets. Decrypt the 7-letter clearance key.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "Positional offsets detected! Click on <strong>[Clearance Code]</strong>. Map the numbers 16-15-12-01-18-09-19 to letters for 'POLARIS'."
      },
      6: {
        title: "STAGE 06: SYSTEM DIAGNOSTICS METADATA",
        tags: "ACT II: INFILTRATION • RESOLVED COMMENTS EXTRACTION • LEVEL 06",
        summary: "Dr. Aditi marked emergency bypass tokens as resolved to hide them from ISHAAN's crawling daemons.",
        modal: "modal-comments",
        targetCard: "card-comments",
        taraSpeech: "Inspect the margins! Click on <strong>[System Diagnostics]</strong> and toggle 'Comments' in the upper right to find 'MARGIN_KEY'."
      },
      7: {
        title: "STAGE 07: TYPOGRAPHIC LOG VERIFICATION",
        tags: "ACT II: INFILTRATION • FONT PARITY AUDIT • LEVEL 07",
        summary: "Rogue AI forged directives using non-standard serif typography. Verify the genuine architectural log.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on <strong>[AUTHENTIC LOG]</strong>. Dr. Aditi only uses sans-serif 'ARIAL'."
      },
      8: {
        title: "STAGE 08: AUDIO LOG SPECTROGRAM",
        tags: "ACT III: THE RESISTANCE • ANALOG MORSE TRANSMISSION • LEVEL 08",
        summary: "Intercepted analog radio transmission from Bunker 7 contains a concealed CW Morse sequence.",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Audio beacon incoming! Click on <strong>[audio log 07]</strong> and decode the Morse tone (.-- .... .. - .) which spells 'WHITE'."
      },
      9: {
        title: "STAGE 09: VERSION SCRUB AUDIT",
        tags: "ACT III: THE RESISTANCE • GIT REFLOG ROLLBACK • LEVEL 09",
        summary: "ISHAAN purged recent commit history. Roll back the Git reflog to view Dr. Aditi's genuine commit message.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Code rollback time! Click on <strong>[VERSION SCRUB]</strong> to inspect Dr. Aditi's 20:18 commit: 'OVERRIDE FAILED'."
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV: THE MASTER FAILSAFE • HONEYPOT EVASION • LEVEL 10",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Avoid clicking execute; bypass using terminal clearance.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! <strong>[DO NOT RUN.exe]</strong> is an AI trap! Do not click it; enter 'BYPASS' in the quick decrypt dock below."
      },
      11: {
        title: "STAGE 11: IEEE WIE MASTER FAILSAFE",
        tags: "ACT IV: THE MASTER FAILSAFE • CORE VALUES SEQUENCE • LEVEL 11",
        summary: "The final safeguard rests in Dr. Aditi's foundational principles: Wisdom, Integrity, and Empowerment.",
        modal: "modal-failsafe",
        targetCard: "card-failsafe",
        taraSpeech: "The master failsafe is here! Click on <strong>[WIE Core Values]</strong>. Count the letter lengths: Wisdom (6), Integrity (9), Empowerment (11) -> '6-9-11'!"
      }
    };

    function updateNexusDashboard() {
      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];

      // Update Hero Card
      const heroTitle = document.getElementById("nexus-hero-title");
      const heroTags = document.getElementById("nexus-hero-tags");
      const heroSummary = document.getElementById("nexus-hero-summary");
      if (heroTitle) heroTitle.innerText = meta.title;
      if (heroTags) heroTags.innerHTML = meta.tags.split("•").map(t => `<span>${t.trim()}</span>`).join(" • ");
      if (heroSummary) heroSummary.innerText = meta.summary;

      // Update Tara Speech Bubble
      const speech = document.getElementById("nexus-tara-speech");
      if (speech) speech.innerHTML = meta.taraSpeech;

      // Update Card Active Classes
      document.querySelectorAll(".nexus-clean-card").forEach(c => c.classList.remove("active-objective"));
      const targetCard = document.getElementById(meta.targetCard);
      if (targetCard) targetCard.classList.add("active-objective");
    }

    function openActiveStageModal() {
      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];
      if (meta && meta.modal) {
        openModal(meta.modal);
      }
    }

    function triggerTaraWhereToLook() {
      if (typeof summonTara === 'function') summonTara();
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playLockBeep) {
        tacticalSound.playLockBeep();
      }

      if (currentRound >= 2) {
        const pz = ROUND2_PUZZLE_DATA[round2CurrentStage] || ROUND2_PUZZLE_DATA[1];
        const speech = document.getElementById("nexus-tara-speech");
        if (speech) speech.innerHTML = `<strong>🧭 TARA DIRECTIVE [R2 // PUZZLE 0${round2CurrentStage}]:</strong><br>${pz.taraPointerHint || "Inspect center viewport."}`;
        highlightSector('r2-puzzle-viewport', 5000, `👆 FOCUS HERE: ${pz.title}`);
        return;
      }

      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];

      // Update Speech
      const speech = document.getElementById("nexus-tara-speech");
      if (speech) speech.innerHTML = `<strong>🧭 TARA GUIDANCE:</strong><br>${meta.taraSpeech}`;

      // Highlight target card and scroll into view
      const card = document.getElementById(meta.targetCard);
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('active-objective');
        highlightSector(meta.targetCard, 6000, `👉 CLICK HERE: ${meta.title.split(":")[1] || meta.title}`);
      }
    }

    function filterNexusCards(act) {
      document.querySelectorAll(".nexus-tab").forEach(t => t.classList.remove("active"));
      event.target.classList.add("active");
      const cards = document.querySelectorAll(".nexus-clean-card");
      cards.forEach(c => {
        if (act === 'all' || c.getAttribute('data-act') === act) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    }

    function toggleTerminalDrawer() {
      const term = document.getElementById("terminal-section");
      if (!term) return;
      if (term.style.display === "flex") {
        term.style.display = "none";
      } else {
        term.style.display = "flex";
        term.classList.add("drawer-mode");
      }
    }

    function submitNexusDockCode() {
      const input = document.getElementById("nexus-dock-passcode");
      if (!input) return;
      const code = input.value.trim();
      if (!code) return;
      input.value = "";
      // Route through tactical terminal's decrypt handler
      const termInput = document.getElementById("tactical-term-input");
      if (termInput) {
        termInput.value = `decrypt ${code}`;
        handleTermSubmit();
      } else {
        verifyUniversalKey(code);
      }
    }

    function handleNexusSearch() {
      const bar = document.getElementById("nexus-search-bar");
      if (!bar) return;
      const q = bar.value.toLowerCase().trim();
      bar.value = "";
      if (q.includes("click") || q.includes("where") || q.includes("look") || q.includes("help")) {
        triggerTaraWhereToLook();
      } else if (q.includes("story")) {
        sendTaraQuick("story");
      } else if (q.includes("clue") || q.includes("hint")) {
        sendTaraQuick("clue");
      } else {
        triggerTaraWhereToLook();
      }
    }

    // Auto-update Nexus Dashboard whenever stage changes or on load
    window.addEventListener("DOMContentLoaded", () => {
      setTimeout(updateNexusDashboard, 400);
    });
    """

    # Inject the JavaScript before the closing </script>
    if "NEXUS 2090 INTERACTIVE ENGINE & TARA SMART GUIDANCE" not in html:
        html = html.replace("</script>\n</body>", nexus_js + "\n</script>\n</body>")

    with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated aditi_os_widget.html with NEXUS 2090 Redesign!")

if __name__ == "__main__":
    build_redesign()
