# apply_nexus_redesign.py
import re
import sys

def apply_redesign():
    with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add Nexus 2090 CSS Styles
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
      padding: 18px 24px;
      overflow-y: auto;
      position: relative;
      z-index: 10;
    }

    /* Upper Row: Hero Card (Left) + AI Companion Card (Right) */
    .nexus-top-row {
      display: grid;
      grid-template-columns: 1.45fr 1fr;
      gap: 16px;
      min-height: 250px;
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
      font-size: 26px;
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
      font-size: 12.5px;
      padding: 10px 24px;
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
      font-size: 12px;
      padding: 10px 20px;
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
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
      position: relative;
    }
    .nexus-assistant-header {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 12px;
    }
    .nexus-assistant-avatar {
      width: 52px;
      height: 52px;
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
      padding: 12px 14px;
      font-size: 12.5px;
      line-height: 1.6;
      color: #e2e8f0;
      margin-bottom: 14px;
      position: relative;
    }
    .nexus-assistant-chips {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }
    .nexus-telemetry-gauges {
      display: flex;
      justify-content: space-between;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 10px;
      font-size: 11px;
      color: #94a3b8;
    }
    .nexus-gauge-val {
      font-weight: 800;
      color: var(--nexus-cyan);
      font-size: 12.5px;
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
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      letter-spacing: 1px;
      display: flex;
      align-items: center;
      gap: 10px;
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
      padding: 5px 14px;
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
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
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
      min-height: 130px;
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
      margin-bottom: 10px;
    }
    .nexus-stage-tag {
      font-size: 10px;
      font-weight: 800;
      color: var(--nexus-cyan);
      background: rgba(0, 240, 255, 0.12);
      border: 1px solid rgba(0, 240, 255, 0.3);
      padding: 2px 7px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .nexus-card-icon {
      font-size: 26px;
      margin-bottom: 8px;
    }
    .nexus-card-name {
      font-size: 13px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .nexus-card-status {
      font-size: 10.5px;
      color: #94a3b8;
    }

    /* Floating Bottom Dock (Quick Passcode & Collapsible Terminal Toggle) */
    .nexus-bottom-dock {
      position: fixed;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(10, 18, 32, 0.95);
      border: 1px solid rgba(0, 240, 255, 0.4);
      border-radius: 30px;
      padding: 6px 18px;
      display: flex;
      align-items: center;
      gap: 14px;
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
      padding: 6px 14px;
      border-radius: 16px;
      width: 220px;
      outline: none;
    }
    .nexus-dock-btn {
      background: var(--nexus-cyan);
      color: #020612;
      font-weight: 800;
      font-size: 11.5px;
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
      font-size: 11px;
      padding: 6px 12px;
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
      bottom: 60px;
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

    # Insert CSS before </style>
    if "/* ==========================================================================\n       NEXUS 2090 SCI-FI DASHBOARD THEME" not in content:
        content = content.replace("</style>", nexus_css + "\n</style>", 1)
        print("✓ Injected NEXUS 2090 CSS Styles")

    with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    apply_redesign()
