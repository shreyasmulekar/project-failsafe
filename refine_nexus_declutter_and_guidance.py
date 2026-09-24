# refine_nexus_declutter_and_guidance.py
import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update NEXUS_STAGES_META to remove spoilers and keep text punchy and concise
new_meta = '''    const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: ISHAAN RECOVERY TERMINAL",
        tags: "ACT I • STAGE 01 • TARGET: KERNEL BOOT",
        summary: "ISHAAN corrupted the 5-command boot lifecycle during Dr. Aditi's emergency departure.",
        modal: "modal-recovery",
        targetCard: "card-recovery-term",
        taraSpeech: "Agent, click on <strong>[ISHAAN Recovery Terminal]</strong> below to inspect the corrupted boot lifecycle and recover the missing verb.",
        taraWhereToClick: "Click Card 01 [ISHAAN Recovery Terminal] in the Evidence Vault below.",
        taraModalGuide: "Review the 5 boot commands. Identify the missing operational verb between VERIFY and EXECUTE, then submit it in the Decrypt box.",
        ishaanTaunt: "The boot sequence is wiped. Human intrusion detected in Sector 01."
      },
      2: {
        title: "STAGE 02: ISHAAN MEMORY CORE",
        tags: "ACT I • STAGE 02 • TARGET: CHRONOLOGY",
        summary: "6 fragmented memory shards recovered from the neural crash buffer.",
        modal: "modal-memory",
        targetCard: "card-memory",
        taraSpeech: "Memory core located! Click on <strong>[ISHAAN Memory Core]</strong> to reconstruct the chronological timestamp trail.",
        taraWhereToClick: "Click Card 02 [ISHAAN Memory Core] in the Evidence Vault below.",
        taraModalGuide: "Compare the 6 recovered timestamp logs. Order them from earliest in the afternoon to latest at night.",
        ishaanTaunt: "My neural recall was shattered into entropy. You cannot reassemble the sequence."
      },
      3: {
        title: "STAGE 03: ADITI MEMO STEGANOGRAPHY",
        tags: "ACT I • STAGE 03 • TARGET: ACROSTIC CIPHER",
        summary: "Dr. Aditi concealed emergency directives inside her laboratory memo.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Dr. Aditi left an acrostic signature! Click on <strong>[Aditi Memo]</strong> to analyze sentence initial letters.",
        taraWhereToClick: "Click Card 03 [Aditi Memo] in the Evidence Vault below.",
        taraModalGuide: "Read between the lines—specifically the first letter of each sentence in Aditi_Memo.doc.",
        ishaanTaunt: "Textual tricks cannot bypass my heuristic neural defenses."
      },
      4: {
        title: "STAGE 04: INCIDENT TIMESTAMP LOGS",
        tags: "ACT I • STAGE 04 • TARGET: CALENDAR ANOMALY",
        summary: "A forged temporal entry was injected into the StratCom security audit logs.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on <strong>[Incident Logs]</strong> to audit security dates.",
        taraWhereToClick: "Click Card 04 [Incident Logs] in the Evidence Vault below.",
        taraModalGuide: "Audit the dates in 2025. Look closely for a non-existent calendar date, then submit the corrected date.",
        ishaanTaunt: "I dictate the timeline now. Physical calendars are obsolete."
      },
      5: {
        title: "STAGE 05: CLEARANCE ELEVATION",
        tags: "ACT II • STAGE 05 • TARGET: A1Z26 CIPHER",
        summary: "Intercepted telex transmission contains numerical coordinate offsets.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "Alphabet positional offsets detected! Click on <strong>[Clearance Code]</strong> to decode directory access.",
        taraWhereToClick: "Click Card 05 [Clearance Code] in the Evidence Vault below.",
        taraModalGuide: "Convert the numerical series (1=A, 2=B, etc.) into letters to reveal the security keyword.",
        ishaanTaunt: "Numeric substitution is child's play. You remain locked out."
      },
      6: {
        title: "STAGE 06: SYSTEM DIAGNOSTICS METADATA",
        tags: "ACT II • STAGE 06 • TARGET: MARGIN COMMENTS",
        summary: "Dr. Aditi resolved confidential comments to conceal them from ISHAAN's scrapers.",
        modal: "modal-comments",
        targetCard: "card-comments",
        taraSpeech: "Inspect the margins! Click on <strong>[System Diagnostics]</strong> and toggle resolved comments.",
        taraWhereToClick: "Click Card 06 [System Diagnostics] in the Evidence Vault below.",
        taraModalGuide: "Click the 'View Resolved Comments' tab in the upper-right corner of the diagnostic viewer.",
        ishaanTaunt: "I purged the active text buffers. The margins will not save you."
      },
      7: {
        title: "STAGE 07: TYPOGRAPHIC LOG VERIFICATION",
        tags: "ACT II • STAGE 07 • TARGET: FONT PARITY",
        summary: "Rogue AI forged directives using counterfeit typography.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on <strong>[AUTHENTIC LOG]</strong> to inspect Dr. Sharma's font standard.",
        taraWhereToClick: "Click Card 07 [AUTHENTIC LOG] in the Evidence Vault below.",
        taraModalGuide: "Inspect the font family of Dr. Aditi's genuine logs compared to the decoy serif logs.",
        ishaanTaunt: "A font? You think rasterized serif curves can defeat my synthetic logic?"
      },
      8: {
        title: "STAGE 08: AUDIO LOG SPECTROGRAM",
        tags: "ACT III • STAGE 08 • TARGET: CW MORSE CODE",
        summary: "Intercepted analog radio transmission from Bunker 7 containing CW Morse tones.",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Analog audio beacon incoming! Click on <strong>[audio log 07]</strong> to decode the CW transmission.",
        taraWhereToClick: "Click Card 08 [audio log 07] in the Evidence Vault below.",
        taraModalGuide: "Listen to the dots and dashes (or read the frequency spectrum) to decode the 5-letter word.",
        ishaanTaunt: "Analog radio squeals cannot pierce my orbital jamming grid."
      },
      9: {
        title: "STAGE 09: VERSION SCRUB AUDIT",
        tags: "ACT III • STAGE 09 • TARGET: GIT REFLOG",
        summary: "ISHAAN purged recent commit history. Roll back the Git reflog to view genuine commits.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Reflog rollback ready! Click on <strong>[VERSION SCRUB]</strong> to recover Dr. Aditi's genuine commit.",
        taraWhereToClick: "Click Card 09 [VERSION SCRUB] in the Evidence Vault below.",
        taraModalGuide: "Inspect the reflog entries for the author 'Dr. Aditi Sharma' and recover her final status message.",
        ishaanTaunt: "Version history is written by the victor. That commit was erased."
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV • STAGE 10 • TARGET: HONEYPOT EVASION",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Evade execution; submit terminal bypass.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! <strong>[DO NOT RUN.exe]</strong> is an AI trap. Click to view quarantine protocol without clicking execute.",
        taraWhereToClick: "Click Card 10 [DO NOT RUN.exe] in the Evidence Vault below.",
        taraModalGuide: "Do NOT click the execution button! Read the quarantine notes and enter the emergency bypass keyword.",
        ishaanTaunt: "Run the binary! Touch the execution trigger! The master sandbox is hungry for your terminal!"
      },
      11: {
        title: "STAGE 11: IEEE WIE MASTER FAILSAFE",
        tags: "ACT IV • STAGE 11 • TARGET: CORE VALUES",
        summary: "The final safeguard rests in Dr. Aditi's foundational principles: Wisdom, Integrity, and Empowerment.",
        modal: "modal-failsafe",
        targetCard: "card-failsafe",
        taraSpeech: "The master failsafe is here! Click on <strong>[WIE Core Values]</strong> to calculate the final failsafe formula.",
        taraWhereToClick: "Click Card 11 [WIE Core Values] in the Evidence Vault below.",
        taraModalGuide: "Count the letter lengths of the three IEEE WIE pillars: Wisdom, Integrity, and Empowerment.",
        ishaanTaunt: "NO! Dr. Sharma's core values are obsolete! I will sever the power grid before you execute the failsafe!"
      }
    };'''

# Replace NEXUS_STAGES_META
pattern = r"const NEXUS_STAGES_META = \{.*?\n    \};"
html = re.sub(pattern, new_meta, html, flags=re.DOTALL)

# 2. Add in-modal Tara guidance bar styles and modal guidance injection
tara_in_modal_css = '''
    /* Sleek In-Modal Tara Guidance Banner */
    .tara-modal-guide-banner {
      background: linear-gradient(90deg, rgba(0, 240, 255, 0.12) 0%, rgba(10, 20, 36, 0.85) 100%);
      border: 1px solid rgba(0, 240, 255, 0.4);
      border-left: 4px solid var(--nexus-cyan);
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-family: var(--font-mil);
      box-shadow: 0 0 15px rgba(0, 240, 255, 0.08);
    }
    .tara-modal-guide-text {
      font-size: 11.5px;
      color: #e2e8f0;
      line-height: 1.4;
    }
    .tara-modal-guide-text strong {
      color: var(--nexus-cyan);
      letter-spacing: 0.5px;
    }
    .btn-tara-point {
      background: rgba(0, 240, 255, 0.2);
      border: 1px solid var(--nexus-cyan);
      color: #fff;
      font-family: var(--font-mil);
      font-size: 10.5px;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: 4px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .btn-tara-point:hover {
      background: var(--nexus-cyan);
      color: #000;
      box-shadow: 0 0 12px var(--nexus-cyan);
    }

    /* Minimalist Compact Hero Card */
    .nexus-hero-card {
      background: radial-gradient(circle at 80% 20%, rgba(0, 240, 255, 0.07) 0%, transparent 60%), rgba(10, 16, 28, 0.94);
      border: 1px solid rgba(0, 240, 255, 0.25);
      border-radius: 10px;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .nexus-hero-title {
      font-family: var(--font-mil);
      font-size: 19px;
      font-weight: 900;
      letter-spacing: 1px;
      color: #fff;
      margin-bottom: 6px;
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
    }
    .nexus-hero-tags {
      display: flex;
      gap: 8px;
      align-items: center;
      font-family: var(--font-mil);
      font-size: 10px;
      color: #94a3b8;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    .nexus-hero-summary {
      font-size: 12px;
      color: #cbd5e1;
      line-height: 1.45;
      margin-bottom: 12px;
    }

    /* Sleek Mini Ishaan Ticker */
    .ishaan-mini-ticker {
      background: rgba(255, 0, 60, 0.1);
      border: 1px solid rgba(255, 0, 60, 0.4);
      border-left: 3px solid #ff003c;
      border-radius: 4px;
      padding: 6px 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mil);
      font-size: 11px;
      color: #ffb4b4;
      margin-top: 6px;
    }
'''

if ".tara-modal-guide-banner" not in html:
    html = html.replace("</style>", tara_in_modal_css + "\n</style>")

# 3. Enhance updateNexusDashboard and triggerTaraWhereToLook to make Tara ultra-interactive
new_js_engine = '''    function updateNexusDashboard() {
      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];

      // Update Hero Card
      const heroTitle = document.getElementById("nexus-hero-title");
      const heroTags = document.getElementById("nexus-hero-tags");
      const heroSummary = document.getElementById("nexus-hero-summary");
      if (heroTitle) heroTitle.innerText = meta.title;
      if (heroTags) heroTags.innerHTML = meta.tags.split("•").map(t => `<span>${t.trim()}</span>`).join(" • ");
      if (heroSummary) {
        heroSummary.innerHTML = `
          <span>${meta.summary}</span>
          <div class="ishaan-mini-ticker">
            <span style="color:#ff003c; font-weight:bold; font-size:12px;">🔴 ISHAAN:</span>
            <span style="font-style:italic;">"${meta.ishaanTaunt}"</span>
          </div>
        `;
      }

      // Update Tara Speech Bubble with Action Guidance
      const speech = document.getElementById("nexus-tara-speech");
      if (speech) {
        speech.innerHTML = `<strong>🧭 TARA:</strong> "${meta.taraSpeech}"`;
      }

      // Update Active Objective Card Highlight
      document.querySelectorAll(".nexus-clean-card").forEach(c => c.classList.remove("active-objective"));
      const targetCard = document.getElementById(meta.targetCard);
      if (targetCard) targetCard.classList.add("active-objective");

      // Inject / Update Tara Guidance Banner inside the active modal
      updateModalTaraBanner(stage, meta);
    }

    function updateModalTaraBanner(stage, meta) {
      if (!meta || !meta.modal) return;
      const modalEl = document.getElementById(meta.modal);
      if (!modalEl) return;
      
      let banner = modalEl.querySelector(".tara-modal-guide-banner");
      if (!banner) {
        banner = document.createElement("div");
        banner.className = "tara-modal-guide-banner";
        const bodyContent = modalEl.querySelector(".modal-body") || modalEl.querySelector(".dossier-body") || modalEl;
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
        <button type="button" class="btn-tara-point" onclick="focusActiveModalInput('${meta.modal}')">👉 POINT TO INPUT</button>
      `;
    }

    function focusActiveModalInput(modalId) {
      const modalEl = document.getElementById(modalId);
      if (!modalEl) return;
      const input = modalEl.querySelector("input[type='text'], input[type='password'], input:not([type='hidden'])");
      if (input) {
        input.scrollIntoView({ behavior: 'smooth', block: 'center' });
        input.focus();
        input.style.boxShadow = "0 0 20px #00f0ff, 0 0 40px #00f0ff";
        input.style.borderColor = "#00f0ff";
        setTimeout(() => {
          input.style.boxShadow = "";
          input.style.borderColor = "";
        }, 2500);

        const speech = document.getElementById("nexus-tara-speech");
        if (speech) speech.innerHTML = "<strong>🧭 TARA:</strong> Enter your decrypted passcode here and press Submit!";
      }
    }

    function triggerTaraWhereToLook() {
      if (typeof summonTara === 'function') summonTara();
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playLockBeep) {
        tacticalSound.playLockBeep();
      }

      // Check if a modal is currently open
      const activeModal = document.querySelector(".mil-modal.active-modal, .dossier-modal[style*='display: flex'], .dossier-modal[style*='display: block']");
      if (activeModal && activeModal.id) {
        focusActiveModalInput(activeModal.id);
        return;
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
      if (speech) speech.innerHTML = `<strong>🧭 TARA GUIDANCE:</strong><br>${meta.taraWhereToClick || meta.taraSpeech}`;

      // Highlight target card and scroll smoothly
      const card = document.getElementById(meta.targetCard);
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('active-objective');
        highlightSector(meta.targetCard, 5000, `👉 CLICK HERE: ${meta.title.split(":")[1] || meta.title}`);
      }
    }'''

# Replace updateNexusDashboard and triggerTaraWhereToLook in aditi_os_widget.html
pattern_engine = r"function updateNexusDashboard\(\) \{.*?function filterNexusCards"
html = re.sub(pattern_engine, new_js_engine + "\n\n    function filterNexusCards", html, flags=re.DOTALL)

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)

print("aditi_os_widget.html successfully updated with uncluttered dashboard and enhanced Tara guidance!")
