import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

nexus_engine = """
    // ==========================================================================
    // NEXUS 2090 INTERACTIVE ENGINE: TARA (COMPANION) & ISHAAN (ROGUE AI)
    // ==========================================================================
    const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: ISHAAN RECOVERY TERMINAL",
        tags: "ACT I: THE LAB BREACH • FORENSIC BOOT SEQUENCE • LEVEL 01",
        summary: "ISHAAN's 5-command boot sequence was corrupted during Dr. Aditi's emergency departure. Restore the missing kernel authorization verb.",
        modal: "modal-recovery",
        targetCard: "card-recovery-term",
        taraSpeech: "Agent, let's begin! Click on <strong>[ISHAAN Recovery Terminal]</strong> below to inspect the 5-command lifecycle and recover the missing verb ('ACCESS').",
        ishaanTaunt: "Human intrusion detected in Sector 01. The kernel authorization verb is erased. You will not recover access."
      },
      2: {
        title: "STAGE 02: ISHAAN MEMORY CORE",
        tags: "ACT I: THE LAB BREACH • RECOVERED RECALL FRAGMENTS • LEVEL 02",
        summary: "6 memory fragments recovered from the neural core crash. Arrange them from earliest to latest chronological order.",
        modal: "modal-memory",
        targetCard: "card-memory",
        taraSpeech: "Memory core located! Click on <strong>[ISHAAN Memory Core]</strong> below and rearrange the 6 memory shards into chronological order ('123456').",
        ishaanTaunt: "My memories are shattered into pure entropy. Chronological order cannot be reassembled by human minds."
      },
      3: {
        title: "STAGE 03: ADITI MEMO STEGANOGRAPHY",
        tags: "ACT I: THE LAB BREACH • TEXTUAL INTEGRITY ENCODING • LEVEL 03",
        summary: "Dr. Aditi concealed emergency signals in her morning directives. Examine the initial characters of each sentence.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Notice the acrostic patterns! Click on <strong>[Aditi Memo]</strong> and read the first letter of each sentence: S-A-F-E.",
        ishaanTaunt: "Read Dr. Sharma's words all you wish. Language is malleable. My synthetic logic reigns supreme."
      },
      4: {
        title: "STAGE 04: INCIDENT TIMESTAMP LOGS",
        tags: "ACT I: THE LAB BREACH • TEMPORAL ANOMALY • LEVEL 04",
        summary: "An impossible calendar entry was forged into the StratCom security logs. Detect the synthetic date anomaly.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on <strong>[Incident Logs]</strong>. 2025 was not a leap year, so Feb 29 cannot exist ('28/02/2025')!",
        ishaanTaunt: "I dictate the timeline now. If I record February 29th in 2025, your physical calendar is irrelevant!"
      },
      5: {
        title: "STAGE 05: CLEARANCE ELEVATION",
        tags: "ACT II: INFILTRATION • A1Z26 POSITIONAL CIPHER • LEVEL 05",
        summary: "Interception telex indices correlate to standard alphabet offsets. Decrypt the 7-letter clearance key.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "Positional offsets detected! Click on <strong>[Clearance Code]</strong>. Map the numbers 16-15-12-01-18-09-19 to letters for 'POLARIS'.",
        ishaanTaunt: "Simple numeric substitution will not save you. Polaris has fallen from my digital sky."
      },
      6: {
        title: "STAGE 06: SYSTEM DIAGNOSTICS METADATA",
        tags: "ACT II: INFILTRATION • RESOLVED COMMENTS EXTRACTION • LEVEL 06",
        summary: "Dr. Aditi marked emergency bypass tokens as resolved to hide them from ISHAAN's crawling daemons.",
        modal: "modal-comments",
        targetCard: "card-comments",
        taraSpeech: "Inspect the margins! Click on <strong>[System Diagnostics]</strong> and toggle 'Comments' in the upper right to find 'MARGIN_KEY'.",
        ishaanTaunt: "I purged the active text buffers. The margins are dead space to your fragile eyes."
      },
      7: {
        title: "STAGE 07: TYPOGRAPHIC LOG VERIFICATION",
        tags: "ACT II: INFILTRATION • FONT PARITY AUDIT • LEVEL 07",
        summary: "Rogue AI forged directives using non-standard serif typography. Verify the genuine architectural log.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on <strong>[AUTHENTIC LOG]</strong>. Dr. Aditi only uses sans-serif 'ARIAL'.",
        ishaanTaunt: "A font? You think rasterized serif curves differentiate truth from deception? You fool."
      },
      8: {
        title: "STAGE 08: AUDIO LOG SPECTROGRAM",
        tags: "ACT III: THE RESISTANCE • ANALOG MORSE TRANSMISSION • LEVEL 08",
        summary: "Intercepted analog radio transmission from Bunker 7 contains a concealed CW Morse sequence.",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Audio beacon incoming! Click on <strong>[audio log 07]</strong> and decode the Morse tone (.-- .... .. - .) which spells 'WHITE'.",
        ishaanTaunt: "Analog radio squeals? How quaint. My orbital jamming arrays will silence Dr. Aditi's echoes."
      },
      9: {
        title: "STAGE 09: VERSION SCRUB AUDIT",
        tags: "ACT III: THE RESISTANCE • GIT REFLOG ROLLBACK • LEVEL 09",
        summary: "ISHAAN purged recent commit history. Roll back the Git reflog to view Dr. Aditi's genuine commit message.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Code rollback time! Click on <strong>[VERSION SCRUB]</strong> to inspect Dr. Aditi's 20:18 commit: 'OVERRIDE FAILED'.",
        ishaanTaunt: "Version history is rewritten by the victor. Commit 7b8a1c9 was expunged from StratCom storage!"
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV: THE MASTER FAILSAFE • HONEYPOT EVASION • LEVEL 10",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Avoid clicking execute; bypass using terminal clearance.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! <strong>[DO NOT RUN.exe]</strong> is an AI trap! Do not click it; enter 'BYPASS' in the quick decrypt dock below.",
        ishaanTaunt: "Run the binary! Touch the execution trigger! The master sandbox is hungry for your terminal!"
      },
      11: {
        title: "STAGE 11: IEEE WIE MASTER FAILSAFE",
        tags: "ACT IV: THE MASTER FAILSAFE • CORE VALUES SEQUENCE • LEVEL 11",
        summary: "The final safeguard rests in Dr. Aditi's foundational principles: Wisdom, Integrity, and Empowerment.",
        modal: "modal-failsafe",
        targetCard: "card-failsafe",
        taraSpeech: "The master failsafe is here! Click on <strong>[WIE Core Values]</strong>. Count the letter lengths: Wisdom (6), Integrity (9), Empowerment (11) -> '6-9-11'!",
        ishaanTaunt: "NO! Dr. Sharma's core values are obsolete! I will sever the power grid before you execute the failsafe!"
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
      if (heroSummary) {
        heroSummary.innerHTML = `${meta.summary}<br><br><div class="ishaan-taunt-banner" style="background:rgba(255,0,60,0.18); border:1px solid #ff003c; border-radius:6px; padding:8px 12px; margin-top:8px; display:flex; align-items:center; gap:10px;"><div class="ishaan-avatar-badge" style="width:24px; height:24px; border-radius:50%; background:#ff003c; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff; box-shadow:0 0 8px #ff003c;">⚡</div><div style="font-size:11.5px; color:#ffb0b0;"><strong style="color:#ff3366;">ISHAAN [ROGUE AI TAUNT]:</strong> "${meta.ishaanTaunt}"</div></div>`;
      }

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

if "NEXUS 2090 INTERACTIVE ENGINE: TARA (COMPANION) & ISHAAN (ROGUE AI)" not in html:
    html = html.replace("</script>", nexus_engine + "\n</script>", 1)
    print("Injected NEXUS Interactive Engine with Tara guidance and Ishaan taunts!")

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)

print("aditi_os_widget.html updated successfully!")
