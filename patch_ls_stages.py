import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_s16_dir = '''          logTerm("    [STAGE 16] Mass_System_Log.txt       (Frequency Override Count)");
          logTerm("  ─────────────────────────", "cyan");'''

new_dir_16_to_21 = '''          logTerm("    [STAGE 16] Mass_System_Log.txt       (Frequency Override Count)");
          logTerm("  ── ACT VI: FORENSIC CHRONICLES ──", "amber");
          logTerm("    [STAGE 17] Intercepted_ADI_Transmission.pdf (Rogue Chatbot Polybius Shift)");
          logTerm("    [STAGE 18] Cycle_Diagnostics.png     (The Modular Clock Loop)");
          logTerm("    [STAGE 19] Server_Status_Check.pdf   (The Anomaly Checklist)");
          logTerm("    [STAGE 20] Emergency_Override_Key.txt (The Shift Cipher Matrix)");
          logTerm("    [STAGE 21] System_Audit_2013.log     (The Log Anomaly Timeline)");
          logTerm("  ─────────────────────────", "cyan");'''

if old_s16_dir in text:
    text = text.replace(old_s16_dir, new_dir_16_to_21)
    print("Updated directory listing with Stages 17..21")
else:
    print("Warning: old_s16_dir not found")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)
