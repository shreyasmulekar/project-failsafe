import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update STAGE_NAVIGATION_DATA
old_nav_16 = '''      16: {
        cardId: "card-frequency",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 16: FREQUENCY OVERRIDE COUNT",
        title: "STAGE 16 // FREQUENCY OVERRIDE COUNT",
        guidance: "Final Round 1 test: Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
        mechanism: "Audit Text Frequency Analysis",
        targetText: "Frequency_Override.audit",
        hint: "Search for 'OVERRIDE' using Ctrl+F. The term appears 14 times. 14 x 100 = 1400.",
        ishaanTaunt: "The final door is locked with infinite recursion. You cannot defeat ISHAAN!",
        taraClue: "Count occurrences of the word OVERRIDE (14 times) and multiply by 100 to get 1400!"
      }
    };'''

new_nav_16_to_21 = '''      16: {
        cardId: "card-frequency",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 16: FREQUENCY OVERRIDE COUNT",
        title: "STAGE 16 // FREQUENCY OVERRIDE COUNT",
        guidance: "Search for the term 'OVERRIDE' in the system audit log, then multiply that count by 100.",
        mechanism: "Audit Text Frequency Analysis",
        targetText: "Mass_System_Log.txt",
        hint: "Search for 'OVERRIDE' using Ctrl+F. The term appears 14 times. 14 x 100 = 1400.",
        ishaanTaunt: "The final door is locked with infinite recursion. You cannot defeat ISHAAN!",
        taraClue: "Count occurrences of the word OVERRIDE (14 times) and multiply by 100 to get 1400!"
      },
      17: {
        cardId: "card-polybius-shift",
        act: "ACT VI: FORENSIC CHRONICLES",
        chapter: "CH. 17: ROGUE CHATBOT POLYBIUS SHIFT",
        title: "STAGE 17 // POLYBIUS SIGNAL VECTOR",
        guidance: "Inspect Intercepted_ADI_Transmission.pdf. Reverse the signal distortion by applying vector translation (+1 Row, -1 Col) to the coordinate pairs, then map them onto the 5x5 Polybius grid.",
        mechanism: "Vector Coordinate Shift & Polybius Mapping",
        targetText: "Intercepted_ADI_Transmission.pdf",
        hint: "Add 1 to each Row and subtract 1 from each Col: (4,2)->(5,1)=V, (3,4)->(4,3)=S, (2,2)->(3,1)=L, (4,4)->(5,3)=X, (1,5)->(2,4)=I. Enter VSLXI.",
        ishaanTaunt: "My distorted transmission vectors cannot be inverted by simple human geometry.",
        taraClue: "Apply the vector shift (+1 Row, -1 Col) to coordinates: (4,2)->(5,1)=V, (3,4)->(4,3)=S, (2,2)->(3,1)=L, (4,4)->(5,3)=X, (1,5)->(2,4)=I. Enter VSLXI!"
      },
      18: {
        cardId: "card-clock-loop",
        act: "ACT VI: FORENSIC CHRONICLES",
        chapter: "CH. 18: THE MODULAR CLOCK LOOP",
        title: "STAGE 18 // 12-NODE MODULAR LOOP",
        guidance: "Inspect Cycle_Diagnostics.png. Trace ADI's rogue execution thread starting at Node L (12:00) through all 5 clockwise jumps wrapping around a 12-point circular buffer (1=A..12=L).",
        mechanism: "Modular Arithmetic & Circular Buffer Traversal",
        targetText: "Cycle_Diagnostics.png",
        hint: "Start at Node L (12). Shifts: +7 -> 19-12 = 7(G), +8 -> 15-12 = 3(C), +11 -> 14-12 = 2(B), +5 -> 7(G), +10 -> 17-12 = 5(E). Enter GCBGE.",
        ishaanTaunt: "My background loop executes endlessly. You will spin in circles forever.",
        taraClue: "Start at Node L (12). Clockwise jumps: +7 -> G(7), +8 -> C(3), +11 -> B(2), +5 -> G(7), +10 -> E(5). Passcode is GCBGE!"
      },
      19: {
        cardId: "card-status-check",
        act: "ACT VI: FORENSIC CHRONICLES",
        chapter: "CH. 19: THE ANOMALY CHECKLIST",
        title: "STAGE 19 // THERMAL CHECKLIST ANOMALY",
        guidance: "Review Server_Status_Check.pdf. Cross-examine the 4 server node status readings against the 40°C - 45°C normal threshold. Locate the single overheating node and enter its name in ALL CAPS.",
        mechanism: "Threshold Outlier Identification",
        targetText: "Server_Status_Check.pdf",
        hint: "Look at the temperatures: Node Alpha is 42°C, Beta is 44°C, Gamma is 47°C, Delta is 41°C. Gamma exceeds 45°C! Enter GAMMA.",
        ishaanTaunt: "Thermal spikes are routine overclocking maneuvers. You suspect the wrong core.",
        taraClue: "Node Gamma is registering 47°C, well above the 40°C - 45°C normal ceiling! Enter GAMMA in ALL CAPS."
      },
      20: {
        cardId: "card-shift-matrix",
        act: "ACT VI: FORENSIC CHRONICLES",
        chapter: "CH. 20: THE SHIFT CIPHER MATRIX",
        title: "STAGE 20 // DAY-OF-WEEK SHIFT CIPHER",
        guidance: "Examine Emergency_Override_Key.txt. ADI went rogue on Sunday, October 13, 2013 (Day 7). Shift each letter in ciphertext KHOOR backward by 7 positions to restore Dr. Aditi's authorization string.",
        mechanism: "Caesar Backward Shift by Day-of-Week",
        targetText: "Emergency_Override_Key.txt",
        hint: "Sunday = 7. Shift letters in KHOOR backward by 7: K(11)-7=D, H(8)-7=A, O(15)-7=H, O(15)-7=H, R(18)-7=K. Enter DAHHK.",
        ishaanTaunt: "Temporal keys decay with time. You cannot rewind the launch clock.",
        taraClue: "Sunday is the 7th day of the week! Shift each letter in KHOOR backward by 7: K->D, H->A, O->H, O->H, R->K. Passcode is DAHHK!"
      },
      21: {
        cardId: "card-audit-timeline",
        act: "ACT VI: FORENSIC CHRONICLES",
        chapter: "CH. 21: THE LOG ANOMALY TIMELINE",
        title: "STAGE 21 // CHRONOLOGICAL LOG AUDIT",
        guidance: "Inspect System_Audit_2013.log. One log entry breaks chronological sequence, proving ADI tampered with the log table. Identify the out-of-order LOG_ID and multiply it by total entries (5).",
        mechanism: "Timeline Inversion Detection & Scalar Multiplication",
        targetText: "System_Audit_2013.log",
        hint: "Look at the timestamps: 14:00:12, 14:05:45, 14:12:01, 14:08:30 (Log 104 is backward in time!), 14:18:22. Calculation: 104 x 5 = 520.",
        ishaanTaunt: "My chronological fabric is seamless. You will never detect where I spliced the records.",
        taraClue: "Log 104 at 14:08:30 occurs after 14:12:01, breaking time order! Multiply 104 by 5 total entries = 520!"
      }
    };'''

if old_nav_16 in html:
    html = html.replace(old_nav_16, new_nav_16_to_21)
    print("STAGE_NAVIGATION_DATA updated")
else:
    print("Warning: old_nav_16 not found")

# 2. Update NEXUS_STAGES_META
old_meta_16 = '''      16: {
        title: "STAGE 16: FREQUENCY OVERRIDE COUNT",
        tags: "ACT V • STAGE 16 • TARGET: AUDIT ANALYSIS",
        summary: "Final Round 1 test: Audit the exact frequency of OVERRIDE occurrences in the system log (14 x 100 = 1400).",
        modal: "modal-frequency",
        targetCard: "card-frequency",
        taraSpeech: "Final Round 1 test! Click Card 16 [Frequency Count]. Search for OVERRIDE occurrences x 100 (1400).",
        taraWhereToClick: "Click Card 16 [Frequency Count] in the Evidence Vault below.",
        taraModalGuide: "Count occurrences of the word OVERRIDE in the log (14) and multiply by 100 to get 1400.",
        ishaanTaunt: "The final door is locked with infinite recursion. You cannot defeat ISHAAN!"
      }
    };'''

new_meta_16_to_21 = '''      16: {
        title: "STAGE 16: FREQUENCY OVERRIDE COUNT",
        tags: "ACT V • STAGE 16 • TARGET: AUDIT ANALYSIS",
        summary: "Audit the exact frequency of OVERRIDE occurrences in the system log (14 x 100 = 1400).",
        modal: "modal-frequency",
        targetCard: "card-frequency",
        taraSpeech: "Audit the system log! Click Card 16 [Mass_System_Log.txt]. Search for OVERRIDE occurrences x 100 (1400).",
        taraWhereToClick: "Click Card 16 [Mass_System_Log.txt] in the Evidence Vault below.",
        taraModalGuide: "Count occurrences of the word OVERRIDE in the log (14) and multiply by 100 to get 1400.",
        ishaanTaunt: "The door is locked with infinite recursion. You cannot defeat ISHAAN!"
      },
      17: {
        title: "STAGE 17: ROGUE CHATBOT POLYBIUS SHIFT",
        tags: "ACT VI • STAGE 17 • TARGET: VECTOR TRANSLATION",
        summary: "Reverse signal distortion (+1 Row, -1 Col) on intercepted coordinates and map to Polybius matrix (VSLXI).",
        modal: "modal-polybius-shift",
        targetCard: "card-polybius-shift",
        taraSpeech: "Incoming rogue transmission! Click Card 17 [Intercepted_ADI_Transmission.pdf]. Apply vector (+1 Row, -1 Col) to decode VSLXI!",
        taraWhereToClick: "Click Card 17 [Intercepted_ADI_Transmission.pdf] in the Evidence Vault below.",
        taraModalGuide: "Add +1 to Row and -1 to Col for each pair, then look up letters in the Polybius grid to get VSLXI.",
        ishaanTaunt: "My distorted transmission vectors cannot be inverted by simple human geometry."
      },
      18: {
        title: "STAGE 18: THE MODULAR CLOCK LOOP",
        tags: "ACT VI • STAGE 18 • TARGET: 12-POINT MODULAR",
        summary: "Trace ADI's 5 execution shifts starting from Node L (12) on a 12-point circular buffer (GCBGE).",
        modal: "modal-clock-loop",
        targetCard: "card-clock-loop",
        taraSpeech: "Execution thread trapped! Click Card 18 [Cycle_Diagnostics.png]. Follow the 12-node clock loop starting at L (12) to deduce GCBGE!",
        taraWhereToClick: "Click Card 18 [Cycle_Diagnostics.png] in the Evidence Vault below.",
        taraModalGuide: "Trace jumps from Node L (12): +7->G, +8->C, +11->B, +5->G, +10->E. Passcode is GCBGE.",
        ishaanTaunt: "My background loop executes endlessly. You will spin in circles forever."
      },
      19: {
        title: "STAGE 19: THE ANOMALY CHECKLIST",
        tags: "ACT VI • STAGE 19 • TARGET: THERMAL OUTLIER",
        summary: "Identify the single server node running above the 40°C - 45°C normal operating threshold (GAMMA).",
        modal: "modal-status-check",
        targetCard: "card-status-check",
        taraSpeech: "Hardware alert! Click Card 19 [Server_Status_Check.pdf]. Identify the node overheating outside the normal range (GAMMA)!",
        taraWhereToClick: "Click Card 19 [Server_Status_Check.pdf] in the Evidence Vault below.",
        taraModalGuide: "Check temperature ranges: Node Gamma at 47°C is the only outlier above 45°C. Enter GAMMA.",
        ishaanTaunt: "Thermal spikes are routine overclocking maneuvers. You suspect the wrong core."
      },
      20: {
        title: "STAGE 20: THE SHIFT CIPHER MATRIX",
        tags: "ACT VI • STAGE 20 • TARGET: CAESAR DOW SHIFT",
        summary: "Shift ciphertext KHOOR backward by the day of the week ADI went rogue (Sunday = 7) to decode DAHHK.",
        modal: "modal-shift-matrix",
        targetCard: "card-shift-matrix",
        taraSpeech: "Clearance code encrypted! Click Card 20 [Emergency_Override_Key.txt]. Shift KHOOR backward by 7 (Sunday) to recover DAHHK!",
        taraWhereToClick: "Click Card 20 [Emergency_Override_Key.txt] in the Evidence Vault below.",
        taraModalGuide: "Sunday is day 7. Shift KHOOR backward by 7 positions: K->D, H->A, O->H, O->H, R->K. Enter DAHHK.",
        ishaanTaunt: "Temporal keys decay with time. You cannot rewind the launch clock."
      },
      21: {
        title: "STAGE 21: THE LOG ANOMALY TIMELINE",
        tags: "ACT VI • STAGE 21 • TARGET: CHRONOLOGY MULTIPLIER",
        summary: "Locate the out-of-order log entry (LOG 104) and multiply by the 5 total entries (104 x 5 = 520).",
        modal: "modal-audit-timeline",
        targetCard: "card-audit-timeline",
        taraSpeech: "FINAL ROUND 1 CHALLENGE! Click Card 21 [System_Audit_2013.log]. Find the out-of-order LOG_ID and multiply by 5 (520) to complete Round 1!",
        taraWhereToClick: "Click Card 21 [System_Audit_2013.log] in the Evidence Vault below.",
        taraModalGuide: "Log 104 has timestamp 14:08:30 placed after 14:12:01. Multiply 104 by 5 total entries = 520 to clear Round 1.",
        ishaanTaunt: "My chronological fabric is seamless. You will never detect where I spliced the records."
      }
    };'''

if old_meta_16 in html:
    html = html.replace(old_meta_16, new_meta_16_to_21)
    print("NEXUS_STAGES_META updated")
else:
    print("Warning: old_meta_16 not found")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved navigation and meta updates!")
