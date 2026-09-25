import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_s16_checksum = '''        // Stage 16: Frequency Override Count (1400) -> Completes Round 1
        } else if (clean === "1400" || clean === "14" || clean === "1400HZ" || clean === "OVERRIDE" || clean === "OVERRIDE1400") {
          matched = true;
          recordStageCleared(16);
          currentStage = 16;
          localStorage.setItem('failsafe_stage', '16');
          tacticalSound.playSuccess();
          const banner = document.getElementById('active-mission-banner');
          if (banner) {
            banner.innerHTML = '<div style="color:var(--tactical-green); font-weight:bold; font-size:12px; padding:6px;">🏆 [ROUND 1 COMPLETE]: TARA LIBERATED // ROGUE AI ISHAAN PURGED // DR. ADITI LOCATED // ALL 16 STAGES CLEARED!</div>';
          }
          addTerminalLog(`[CHECKSUM ACCREDITED]: FREQUENCY OVERRIDE SYNCHRONIZED (1400). ALL 16 STAGES SOLVED!`, "green");
          reportTelemetryAction("Solved Stage 16 (Frequency Override) - Completed Round 1");
          handleMissionVictorySequence();
        }'''

new_stages_checksum = '''        // Stage 16: Frequency Override Count (1400) -> Advances to Stage 17
        } else if (clean === "1400" || clean === "14" || clean === "1400HZ" || clean === "OVERRIDE" || clean === "OVERRIDE1400") {
          matched = true;
          recordStageCleared(16);
          currentStage = 17;
          localStorage.setItem('failsafe_stage', '17');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: FREQUENCY OVERRIDE SYNCHRONIZED (1400). PROMOTED TO STAGE 17.`, "green");
          reportTelemetryAction("Solved Stage 16 (Frequency Override) - Promoted to Stage 17");
          updateMissionBanner(17, "ACT VI // CH. 17: ROGUE CHATBOT POLYBIUS SHIFT", "Apply vector translation (+1 Row, -1 Col) to intercepted coordinates to decode VSLXI.");
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 16 SOLVED!</strong><br>Frequency parity locked: 1400! Clearance elevated to Level 17.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 17] Intercepted_ADI_Transmission.pdf</strong> on the left! Reverse coordinate distortion (+1 Row, -1 Col).`);
          updateClueBatteryDisplay();

        // Stage 17: The Rogue Chatbot Polybius Shift (VSLXI)
        } else if (clean === "VSLXI") {
          matched = true;
          recordStageCleared(17);
          currentStage = 18;
          localStorage.setItem('failsafe_stage', '18');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: VECTOR SHIFT REVERSED (VSLXI). PROMOTED TO STAGE 18.`, "green");
          reportTelemetryAction("Solved Stage 17 (Polybius Shift) - Promoted to Stage 18");
          updateMissionBanner(18, "ACT VI // CH. 18: THE MODULAR CLOCK LOOP", "Trace 12-hour circular buffer shifts starting from Node L (12) to deduce thread passcode.");
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 17 SOLVED!</strong><br>Polybius transmission decoded: VSLXI! Clearance elevated to Level 18.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 18] Cycle_Diagnostics.png</strong> on the left! Follow the 12-node clock shifts starting at Node L (12).`);
          updateClueBatteryDisplay();

        // Stage 18: The Modular Clock Loop (GCBGE)
        } else if (clean === "GCBGE") {
          matched = true;
          recordStageCleared(18);
          currentStage = 19;
          localStorage.setItem('failsafe_stage', '19');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CYCLIC THREAD LOOP DISARMED (GCBGE). PROMOTED TO STAGE 19.`, "green");
          reportTelemetryAction("Solved Stage 18 (Clock Loop) - Promoted to Stage 19");
          updateMissionBanner(19, "ACT VI // CH. 19: THE ANOMALY CHECKLIST", "Cross-examine 4 server nodes against 40°C - 45°C normal threshold to find overheating core.");
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 18 SOLVED!</strong><br>Thread loop broken: GCBGE! Clearance elevated to Level 19.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 19] Server_Status_Check.pdf</strong> on the left! Locate the overheating node.`);
          updateClueBatteryDisplay();

        // Stage 19: The Anomaly Checklist (GAMMA)
        } else if (clean === "GAMMA") {
          matched = true;
          recordStageCleared(19);
          currentStage = 20;
          localStorage.setItem('failsafe_stage', '20');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: THERMAL OUTLIER ISOLATED (GAMMA). PROMOTED TO STAGE 20.`, "green");
          reportTelemetryAction("Solved Stage 19 (Anomaly Checklist) - Promoted to Stage 20");
          updateMissionBanner(20, "ACT VI // CH. 20: THE SHIFT CIPHER MATRIX", "Shift ciphertext KHOOR backward by day-of-week value for Sunday (7) to restore authorization code.");
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 19 SOLVED!</strong><br>Overheating node identified: GAMMA! Clearance elevated to Level 20.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 20] Emergency_Override_Key.txt</strong> on the left! Reverse Caesar shift for Sunday (7).`);
          updateClueBatteryDisplay();

        // Stage 20: The Shift Cipher Matrix (DAHHK)
        } else if (clean === "DAHHK") {
          matched = true;
          recordStageCleared(20);
          currentStage = 21;
          localStorage.setItem('failsafe_stage', '21');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: AUTHORIZATION CODE RESTORED (DAHHK). PROMOTED TO STAGE 21.`, "green");
          reportTelemetryAction("Solved Stage 20 (Shift Cipher Matrix) - Promoted to Stage 21");
          updateMissionBanner(21, "ACT VI // CH. 21: THE LOG ANOMALY TIMELINE", "Detect out-of-order log entry in System_Audit_2013.log and multiply LOG_ID by 5.");
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 20 SOLVED!</strong><br>Authorization restored: DAHHK! Clearance elevated to Stage 21 (ROUND 1 FINALE).<br><br><span style="color:var(--cyber-cyan);">FINAL ROUND 1 OBJECTIVE:</span> Open <strong>[STAGE 21] System_Audit_2013.log</strong> on the left! Find the timestamp anomaly.`);
          updateClueBatteryDisplay();

        // Stage 21: The Log Anomaly Timeline (520) -> Completes Round 1
        } else if (clean === "520" || clean === "104X5" || clean === "104*5") {
          matched = true;
          recordStageCleared(21);
          currentStage = 21;
          localStorage.setItem('failsafe_stage', '21');
          tacticalSound.playSuccess();
          const banner = document.getElementById('active-mission-banner');
          if (banner) {
            banner.innerHTML = '<div style="color:var(--tactical-green); font-weight:bold; font-size:12px; padding:6px;">🏆 [ROUND 1 COMPLETE]: TARA LIBERATED // ALL 21 FORENSIC STAGES CLEARED! PROCEED TO ROUND 2 QUALIFICATION!</div>';
          }
          addTerminalLog(`[CHECKSUM ACCREDITED]: TIMELINE TAMPERING VERIFIED (520). ALL 21 STAGES SOLVED!`, "green");
          reportTelemetryAction("Solved Stage 21 (Timeline Audit) - Completed Round 1");
          handleMissionVictorySequence();
        }'''

if old_s16_checksum in html:
    html = html.replace(old_s16_checksum, new_stages_checksum)
    print("Replaced runChecksumScan with Stages 17..21")
else:
    print("Warning: old_s16_checksum not found exactly")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)
