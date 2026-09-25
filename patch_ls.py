with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_ls = '''          logTerm("  ── ACT I: BREACH ──", "amber");
          logTerm("    [STAGE 01] ISHAAN_Recovery.term      (System Boot Lifecycle)");
          logTerm("    [STAGE 02] ISHAAN_Memory.core        (ISHAAN's Neural Reconstruction)");
          logTerm("    [STAGE 03] Aditi_Memo.doc            (Confidential Lab Memo)");
          logTerm("  ── ACT II: INFILTRATION ──", "amber");
          logTerm("    [STAGE 04] Incident_Logs.doc         (Calendar Event Anomaly)");
          logTerm("    [STAGE 05] Clearance_Code.txt        (Positional Substitution Cipher)");
          logTerm("    [STAGE 06] System_Diagnostics.doc    (Margin Note Metadata)");
          logTerm("    [STAGE 07] AUTHENTIC_LOG.doc         (Counterfeit Typography Audit)");
          logTerm("  ── ACT III: RESISTANCE ──", "amber");
          logTerm("    [STAGE 08] Audio_Spectrogram         (Phosphor Spectral Frequency)");
          logTerm("    [STAGE 09] Version_Scrub             (Git Reflog Audit 02:15)");
          logTerm("  ── ACT IV: FAILSAFE ──", "amber");
          logTerm("    [STAGE 10] Quarantine_Honeypot       (DO_NOT_RUN Quarantine Trap)");
          logTerm("    [STAGE 11] WIE_Core_Values.doc       (IEEE WIE Master Failsafe)");'''

new_ls = '''          logTerm("  ── ACT I: BREACH ──", "amber");
          logTerm("    [STAGE 01] Farewell.doc              (Disappearing Whiteout Message)");
          logTerm("    [STAGE 02] README.doc                (Directory ORIGIN ASCII Summation)");
          logTerm("    [STAGE 03] Incident_Logs.doc         (Non-Leap Year Calendar Anomaly)");
          logTerm("    [STAGE 04] Security_Audit.pdf        (Timestamp Murder Mystery)");
          logTerm("  ── ACT II: INFILTRATION ──", "amber");
          logTerm("    [STAGE 05] Aditi_Memo.doc            (Simple Acrostic Directive)");
          logTerm("    [STAGE 06] AUTHENTIC_LOG.doc         (Font Style Verification)");
          logTerm("    [STAGE 07] Incident_Report.doc       (Revision History Conflict)");
          logTerm("  ── ACT III: RESISTANCE ──", "amber");
          logTerm("    [STAGE 08] audio_log_07.mp3          (Morse Audio Transmission)");
          logTerm("    [STAGE 09] Dark_Terminal.png         (The Steganography Mask)");
          logTerm("  ── ACT IV: FAILSAFE ──", "amber");
          logTerm("    [STAGE 10] DO_NOT_RUN.exe            (Quarantine Honeypot Trap)");
          logTerm("    [STAGE 11] CLEARANCE_CODE.txt        (The Binary Master A1Z26)");'''

text = text.replace(old_ls, new_ls)

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated handleCommand dir/ls listing!")
