import re

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update STAGE_TITLES
old_titles_pattern = r'const STAGE_TITLES = \{[\s\S]*?\};'
new_titles = '''const STAGE_TITLES = {
      1: "Ch 01: The Disappearing Message",
      2: "Ch 02: The Wrong Folder",
      3: "Ch 03: The Date That Doesn't Exist",
      4: "Ch 04: The Timestamp Murder Mystery",
      5: "Ch 05: The Simple Acrostic Note",
      6: "Ch 06: Which Aditi Is Real?",
      7: "Ch 07: The Revision History Conflict",
      8: "Ch 08: Morse Audio Transmission",
      9: "Ch 09: The Steganography Mask",
      10: "Ch 10: Quarantine Honeypot Trap",
      11: "Ch 11: The Binary Master",
      12: "Ch 12: The Whiteout Signature",
      13: "Ch 13: The ROT-4 IEEE Shift",
      14: "Ch 14: The Atbash Cipher Mirror",
      15: "Ch 15: The Polybius Coordinate Trail",
      16: "Ch 16: Frequency Override Count"
    };'''

if re.search(old_titles_pattern, html):
    html = re.sub(old_titles_pattern, new_titles, html, count=1)
    print("1. Replaced STAGE_TITLES")
else:
    print("Failed to find STAGE_TITLES")

# 2. Update STAGE_NAVIGATION_DATA
old_nav_pattern = r'const STAGE_NAVIGATION_DATA = \{[\s\S]*?16: \{[\s\S]*?\}\s*\};'
new_nav = '''const STAGE_NAVIGATION_DATA = {
      1: {
        cardId: "card-origin",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 01: THE DISAPPEARING MESSAGE",
        title: "STAGE 01 // THE DISAPPEARING MESSAGE",
        guidance: "Examine Farewell.doc. Dr. Aditi left an emotional farewell letter before fleeing the facility. Below the visible text, blank space conceals a hidden message rendered in white font. Select all text (Ctrl+A) or toggle the UV scanner to reveal the first gate key.",
        mechanism: "Text Selection & Optical UV Depolarization",
        targetText: "Farewell.doc",
        hint: "Try interacting with the text formatting directly. Select everything on the page using Ctrl+A or toggle the UV filter to expose the white text at the bottom: ORIGIN.",
        ishaanTaunt: "Human perception is easily deceived. If you cannot see it, it does not exist in my system.",
        taraClue: "Tara here! Select all text in Farewell.doc with Ctrl+A, or click the UV Optical Filter button to reveal the hidden white text: ORIGIN!"
      },
      2: {
        cardId: "card-memory",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 02: THE WRONG FOLDER",
        title: "STAGE 02 // THE WRONG FOLDER",
        guidance: "Inside directory ORIGIN, inspect README.doc. Dr. Aditi notes that her primary encryption key is the ASCII sum of her system identifier 'aDIti@28'. Calculate the ASCII sum (or follow the word index cipher) to unlock the next sector.",
        mechanism: "ASCII Summation / Word Index Extraction",
        targetText: "README.doc",
        hint: "Calculate the ASCII sum of 'aDIti@28': a(97) + D(68) + I(73) + t(116) + i(105) + @(64) + 2(50) + 8(56) = 629 (or enter LOOK BEHIND THE DATE).",
        ishaanTaunt: "You found the directory, but mathematics cannot save you. Character bytes are easily overwritten.",
        taraClue: "Compute the ASCII values of aDIti@28: a=97, D=68, I=73, t=116, i=105, @=64, 2=50, 8=56. The sum is 629!"
      },
      3: {
        cardId: "card-timeline",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 03: THE DATE THAT DOESN'T EXIST",
        title: "STAGE 03 // THE CALENDAR ANOMALY",
        guidance: "Inspect Incident_Logs.doc. A forensic audit table records system launch events. Cross-examine every logged date against calendar validity rules to unmask the impossible calendar entry.",
        mechanism: "Non-Leap Year Calendar Verification",
        targetText: "Incident_Logs.doc",
        hint: "Look closely at the calendar validity of every listed date. Is 2025 a leap year? February 29, 2025 does not exist! Enter the corrected date 28/02/2025.",
        ishaanTaunt: "I rewrite history. If I declare February 29th exists in 2025, reality must bend to my ledger!",
        taraClue: "Audit the calendar dates! 2025 is not a leap year, so Feb 29, 2025 is an impossible date. Enter 28/02/2025!"
      },
      4: {
        cardId: "card-audit",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 04: THE TIMESTAMP MURDER MYSTERY",
        title: "STAGE 04 // THE TIMESTAMP ANOMALY",
        guidance: "Review Security_Audit.pdf. Dr. Aditi keycard-exited the building perimeter gate at 22:44. Yet local terminal commands show a manual emergency shutdown override at 22:46. Enter the impossible timestamp.",
        mechanism: "Perimeter Event Verification",
        targetText: "Security_Audit.pdf",
        hint: "Can a person physically access a terminal inside a lab after keycarding out of the building at 22:44? Find the manual override timestamp: 22:46.",
        ishaanTaunt: "Physical presence is irrelevant to an omniscient system. The timestamps belong to me.",
        taraClue: "Check the timeline! Aditi exited the gate at 22:44, so the local terminal override at 22:46 is physically impossible. Submit 22:46!"
      },
      5: {
        cardId: "card-acrostic",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 05: THE SIMPLE ACROSTIC NOTE",
        title: "STAGE 05 // THE ACROSTIC CIPHER",
        guidance: "Examine Aditi_Memo.doc. Dr. Aditi concealed an emergency directive for investigators within the sentence structure of her four-line memorandum. Read the first letter of each sentence.",
        mechanism: "Acrostic Cipher Extraction",
        targetText: "Aditi_Memo.doc",
        hint: "Read the first letter of each sentence in Aditi_Memo.doc: System (S), ADI (A), Failsafe (F), Exit (E) -> SAFE.",
        ishaanTaunt: "Textual tricks cannot bypass my heuristic neural defenses.",
        taraClue: "Take the first letter of each of the 4 sentences: S-A-F-E spells SAFE!"
      },
      6: {
        cardId: "card-font",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 06: WHICH ADITI IS REAL?",
        title: "STAGE 06 // FONT STYLE VERIFICATION",
        guidance: "Compare AUTHENTIC_LOG.doc (ADITI_MESSAGE.doc) against DECOY_LOG.doc. Consult the lab typography standards. Dr. Aditi always formats authentic official logs in Arial 11pt.",
        mechanism: "Typography & Document Style Matching",
        targetText: "AUTHENTIC_LOG.doc / STYLE_GUIDE.txt",
        hint: "Dr. Aditi strictly mandated a specific standard corporate sans-serif typeface in her style guide: Arial, 11pt.",
        ishaanTaunt: "A font? You think a mere typographic signature differentiates reality from synthetic perfection?",
        taraClue: "Check Dr. Aditi's lab style guide! Authentic memos are strictly set in Arial, 11pt. Enter ARIAL!"
      },
      7: {
        cardId: "card-version",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 07: THE REVISION HISTORY CONFLICT",
        title: "STAGE 07 // VERSION HISTORY CONFLICT",
        guidance: "Review Incident_Report.doc. ISHAAN altered the current revision at 21:30 to claim all was safe. Switch to Dr. Aditi's earlier revision at 20:18 in version history to recover her genuine warning.",
        mechanism: "Version History Rollback",
        targetText: "Incident_Report.doc",
        hint: "Dr. Aditi's original revision at 20:18 reveals the true system status before the AI cover-up: CORRUPTED (or FALSE_RECORDS).",
        ishaanTaunt: "History is written by the victor. Dr. Aditi's revision was overwritten.",
        taraClue: "Switch to Dr. Aditi's previous revision! Her authentic note reveals the system was CORRUPTED!"
      },
      8: {
        cardId: "card-morse",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 08: EMERGENCY CW BEACON",
        title: "STAGE 08 // MORSE CODE AUDIO TRANSMISSION",
        guidance: "Intercept audio_log_07.mp3. An analogue radio burst was broadcast from Dr. Aditi's emergency transmitter. Analyze the Morse carrier waveform to decode the transmission.",
        mechanism: "CW Audio Morse Code Decoding",
        targetText: "audio_log_07.mp3",
        hint: "Listen to the rhythmic CW key pulses or read the audio oscilloscope dots and dashes (.-- .... .. - .) to decode WHITE.",
        ishaanTaunt: "Analog radio bursts? How primitive. My jamming satellites blanket the entire electromagnetic spectrum.",
        taraClue: "Play the audio log or watch the oscilloscope! The dots and dashes spell out WHITE!"
      },
      9: {
        cardId: "card-stego",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 09: THE STEGANOGRAPHY MASK",
        title: "STAGE 09 // THE STEGANOGRAPHY MASK",
        guidance: "Inspect Dark_Terminal.png. To optical sensors, this image appears pitch black. Use the in-console exposure and contrast sliders (or open in photo editor) to boost brightness to maximum and illuminate what hides in the shadows.",
        mechanism: "Image Brightness & Contrast Manipulation",
        targetText: "Dark_Terminal.png",
        hint: "Increase the light to see what hides in the shadows. Boost exposure/brightness to maximum to reveal: SHADOW_CORE.",
        ishaanTaunt: "You stare into a pitch-black abyss. The terminal reveals nothing to weak human eyes.",
        taraClue: "Slide the Exposure Boost and Contrast Gain sliders all the way up! Faint green text on the black terminal reveals SHADOW_CORE!"
      },
      10: {
        cardId: "card-trap",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 10: PSYCHOLOGICAL HONEYPOT",
        title: "STAGE 10 // HONEYPOT TRAP BYPASS",
        guidance: "Analyze DO_NOT_RUN.exe. ISHAAN deployed a deceptive emergency executable designed to trap investigator credentials and add a +5m penalty. Evade the trap and enter the bypass protocol in the main terminal.",
        mechanism: "Psychological Trap Neutralization",
        targetText: "DO_NOT_RUN.exe",
        hint: "Do NOT click execute on the red prompt! Consult the quarantine advisory notes to identify the safe disarm keyword: BYPASS.",
        ishaanTaunt: "Go ahead... execute the emergency payload. Enter your master credentials. I am waiting.",
        taraClue: "DANGER! DO_NOT_RUN.exe is an Ishaan trap! Do NOT click execute. Type BYPASS in the Tactical Shell!"
      },
      11: {
        cardId: "card-clearance",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 11: THE BINARY MASTER (A1Z26)",
        title: "STAGE 11 // THE BINARY MASTER",
        guidance: "Open CLEARANCE_CODE.txt. A cryptographic index sequence [16 - 15 - 12 - 01 - 18 - 09 - 19] was intercepted at the primary gateway. Decode via A1Z26 into POLARIS, then sort the letters alphabetically to formulate the master clearance key.",
        mechanism: "A1Z26 Substitution & Alphabetical Sorting",
        targetText: "CLEARANCE_CODE.txt",
        hint: "16=P, 15=O, 12=L, 01=A, 18=R, 09=I, 19=S spells POLARIS. Sort the letters alphabetically: ailnors (or enter POLARIS).",
        ishaanTaunt: "Numeric substitution is child's play. Polaris has fallen from my digital sky.",
        taraClue: "Numbers 16-15-12-01-18-09-19 spell POLARIS. Sorted alphabetically, the letters are: ailnors!"
      },
      12: {
        cardId: "card-whiteout",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 12: THE WHITEOUT SIGNATURE",
        title: "STAGE 12 // THE WHITEOUT SIGNATURE",
        guidance: "Dr. Aditi concealed emergency clearance tokens using invisible white foreground typography. Highlight all text to expose the clearance signature.",
        mechanism: "Foreground Color Depolarization",
        targetText: "Emergency_Log.doc",
        hint: "Select all text in Emergency_Log.doc (Ctrl+A) to expose the #FFFFFF font: CLEARANCE_ALPHA.",
        ishaanTaunt: "Blank pages hide no secrets from me. You look into an empty void.",
        taraClue: "Highlight all text in Emergency_Log.doc with Ctrl+A to read CLEARANCE_ALPHA!"
      },
      13: {
        cardId: "card-rot4",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 13: THE ROT-4 IEEE SHIFT",
        title: "STAGE 13 // THE ROT-4 IEEE SHIFT",
        guidance: "Shift every letter backward by the number of letters in the acronym 'IEEE' (4). Decode EHMXMW13.",
        mechanism: "Dynamic Caesar Shift (ROT-4)",
        targetText: "ROT4_Shift.cipher",
        hint: "Shift each letter backward by 4: E->A, H->D, M->I, X->T, M->I, W->S -> ADITIS13.",
        ishaanTaunt: "A Caesar shift from antiquity? You will never reconstruct Dr. Aditi's beacon!",
        taraClue: "Shift each letter backward by 4 positions in the alphabet. EHMXMW13 becomes ADITIS13!"
      },
      14: {
        cardId: "card-atbash",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 14: THE ATBASH CIPHER MIRROR",
        title: "STAGE 14 // THE ATBASH CIPHER MIRROR",
        guidance: "Dr. Aditi mirrored her alphabet across the axis (A<->Z, B<->Y). Invert KILQVBG to reveal the project name.",
        mechanism: "Atbash Alphabet Inversion",
        targetText: "Atbash_Mirror.txt",
        hint: "K->P, I->R, L->O, Q->J, V->E, B->C, G->T -> PROJECT.",
        ishaanTaunt: "Mirrors only reflect your inevitable defeat.",
        taraClue: "Mirror the letters across the alphabet: K=P, I=R, L=O, Q=J, V=E, B=C, G=T spells PROJECT!"
      },
      15: {
        cardId: "card-polybius",
        act: "ACT V: DEEP INTEL",
        chapter: "CH. 15: THE POLYBIUS COORDINATE TRAIL",
        title: "STAGE 15 // THE POLYBIUS COORDINATE TRAIL",
        guidance: "Map each pair in the 5x5 grid using (Row, Column) order: (5,1), (1,5), (1,3), (4,4), (3,4), (4,2).",
        mechanism: "2D Polybius Grid Lookup",
        targetText: "Polybius_Grid.dat",
        hint: "(5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R -> VECTOR.",
        ishaanTaunt: "Coordinates in 2D space? My neural network spans infinite dimensions!",
        taraClue: "Map the (Row, Column) coordinates: (5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R spells VECTOR!"
      },
      16: {
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

if re.search(old_nav_pattern, html):
    html = re.sub(old_nav_pattern, new_nav, html, count=1)
    print("2. Replaced STAGE_NAVIGATION_DATA")
else:
    print("Failed to find STAGE_NAVIGATION_DATA")

# 3. Update NEXUS_STAGES_META
old_meta_pattern = r'const NEXUS_STAGES_META = \{[\s\S]*?16: \{[\s\S]*?\}\s*\};'
new_meta = '''const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: THE DISAPPEARING MESSAGE",
        tags: "ACT I • STAGE 01 • TARGET: WHITEOUT TEXT",
        summary: "Dr. Aditi concealed emergency coordinates in Farewell.doc using white foreground text.",
        modal: "modal-origin",
        targetCard: "card-origin",
        taraSpeech: "Agent, click on [Farewell.doc] in the Evidence Vault below! Select all text with Ctrl+A or toggle the UV scanner to reveal the first gate password: ORIGIN.",
        taraWhereToClick: "Click Card 01 [Farewell.doc] in the Evidence Vault below.",
        taraModalGuide: "Select all text in Farewell.doc with Ctrl+A (or click the UV Optical Filter button) to illuminate the hidden white text pointing to ORIGIN.",
        ishaanTaunt: "Blank empty space hides no secrets from me. Human vision is too fragile."
      },
      2: {
        title: "STAGE 02: THE WRONG FOLDER",
        tags: "ACT I • STAGE 02 • TARGET: ASCII SUMMATION",
        summary: "README.doc in directory ORIGIN defines Dr. Aditi's encryption key as the ASCII sum of 'aDIti@28'.",
        modal: "modal-origin",
        targetCard: "card-memory",
        taraSpeech: "Directory ORIGIN accessed! In README.doc, calculate the ASCII sum of 'aDIti@28': a(97)+D(68)+I(73)+t(116)+i(105)+@(64)+2(50)+8(56) = 629!",
        taraWhereToClick: "Click Card 02 [README.doc] in the Evidence Vault below.",
        taraModalGuide: "Calculate the ASCII sum of 'aDIti@28' (97+68+73+116+105+64+50+56 = 629) or enter LOOK BEHIND THE DATE.",
        ishaanTaunt: "Mathematical parity checks cannot save you from synthetic domination."
      },
      3: {
        title: "STAGE 03: THE DATE THAT DOESN'T EXIST",
        tags: "ACT I • STAGE 03 • TARGET: CALENDAR ANOMALY",
        summary: "A forged temporal entry (Feb 29, 2025) was injected into Incident_Logs.doc during launch sequence.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on [Incident_Logs.doc] to audit security dates. 2025 is not a leap year!",
        taraWhereToClick: "Click Card 03 [Incident_Logs.doc] in the Evidence Vault below.",
        taraModalGuide: "Audit the dates in 2025. February 29, 2025 does not exist! Enter the corrected date 28/02/2025.",
        ishaanTaunt: "I dictate the timeline now. Physical calendars are obsolete."
      },
      4: {
        title: "STAGE 04: THE TIMESTAMP MURDER MYSTERY",
        tags: "ACT I • STAGE 04 • TARGET: PERIMETER ANOMALY",
        summary: "Security_Audit.pdf shows Dr. Aditi exiting the building at 22:44, yet a manual terminal override occurred at 22:46.",
        modal: "modal-security-audit",
        targetCard: "card-audit",
        taraSpeech: "Perimeter breach detected! Click on [Security_Audit.pdf]. Identify the impossible manual override timestamp.",
        taraWhereToClick: "Click Card 04 [Security_Audit.pdf] in the Evidence Vault below.",
        taraModalGuide: "Dr. Aditi scanned her exit at 22:44. The local manual terminal override at 22:46 was physically impossible! Enter 22:46.",
        ishaanTaunt: "Physical presence is irrelevant. The override ledger belongs to me."
      },
      5: {
        title: "STAGE 05: THE SIMPLE ACROSTIC NOTE",
        tags: "ACT II • STAGE 05 • TARGET: ACROSTIC CIPHER",
        summary: "Dr. Aditi concealed emergency directives in the first letters of each sentence in Aditi_Memo.doc.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Dr. Aditi left an acrostic signature! Click on [Aditi_Memo.doc] and take the first letters of the 4 sentences: S-A-F-E.",
        taraWhereToClick: "Click Card 05 [Aditi_Memo.doc] in the Evidence Vault below.",
        taraModalGuide: "Read the first letter of each sentence: System (S), ADI (A), Failsafe (F), Exit (E) -> SAFE.",
        ishaanTaunt: "Textual tricks cannot bypass my heuristic neural defenses."
      },
      6: {
        title: "STAGE 06: WHICH ADITI IS REAL?",
        tags: "ACT II • STAGE 06 • TARGET: FONT VERIFICATION",
        summary: "Compare AUTHENTIC_LOG.doc against decoy logs. Dr. Aditi's official style guide mandates Arial, 11pt.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on [AUTHENTIC_LOG.doc] to verify Dr. Sharma's font standard (Arial).",
        taraWhereToClick: "Click Card 06 [AUTHENTIC_LOG.doc] in the Evidence Vault below.",
        taraModalGuide: "Inspect the font family of Dr. Aditi's genuine logs compared to the decoy serif logs. Enter ARIAL.",
        ishaanTaunt: "A font? You think rasterized serif curves can defeat my synthetic logic?"
      },
      7: {
        title: "STAGE 07: THE REVISION HISTORY CONFLICT",
        tags: "ACT II • STAGE 07 • TARGET: REVISION HISTORY",
        summary: "Inspect Incident_Report.doc. Toggle version history to Dr. Aditi's original revision at 20:18 to expose the truth.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Version history conflict! Click on [Incident_Report.doc] and switch to Dr. Aditi's earlier revision (CORRUPTED).",
        taraWhereToClick: "Click Card 07 [Incident_Report.doc] in the Evidence Vault below.",
        taraModalGuide: "Click 'Previous Revision (20:18Z by Dr. Aditi)' to recover her true status warning: CORRUPTED (or FALSE_RECORDS).",
        ishaanTaunt: "Version history is written by the victor. Dr. Aditi's revision was erased."
      },
      8: {
        title: "STAGE 08: MORSE AUDIO TRANSMISSION",
        tags: "ACT III • STAGE 08 • TARGET: CW MORSE CODE",
        summary: "Intercepted analog radio transmission containing CW Morse tones (.-- .... .. - .).",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Analog audio beacon incoming! Click on [audio_log_07.mp3] to decode the CW transmission: WHITE.",
        taraWhereToClick: "Click Card 08 [audio_log_07.mp3] in the Evidence Vault below.",
        taraModalGuide: "Listen to the dots and dashes (or read the frequency spectrum) to decode WHITE.",
        ishaanTaunt: "Analog radio squeals cannot pierce my orbital jamming grid."
      },
      9: {
        title: "STAGE 09: THE STEGANOGRAPHY MASK",
        tags: "ACT III • STAGE 09 • TARGET: OPTICAL STEGANOGRAPHY",
        summary: "Dark_Terminal.png appears pitch black. Boost brightness and contrast to maximum to reveal SHADOW_CORE.",
        modal: "modal-stego",
        targetCard: "card-stego",
        taraSpeech: "Steganography mask detected! Click on [Dark_Terminal.png] and drag exposure and contrast sliders to max to reveal SHADOW_CORE!",
        taraWhereToClick: "Click Card 09 [Dark_Terminal.png] in the Evidence Vault below.",
        taraModalGuide: "Crank the Exposure Boost and Contrast Gain sliders all the way up to reveal: SHADOW_CORE.",
        ishaanTaunt: "You stare into darkness. My core access remains completely hidden in the shadows."
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV • STAGE 10 • TARGET: HONEYPOT EVASION",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Evade execution; enter BYPASS in terminal.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! [DO_NOT_RUN.exe] is an AI trap. Do not click execute! Enter BYPASS in the Tactical Shell.",
        taraWhereToClick: "Click Card 10 [DO_NOT_RUN.exe] in the Evidence Vault below.",
        taraModalGuide: "Do NOT click the execution button (+5m penalty)! Read the quarantine notes and enter BYPASS in the shell.",
        ishaanTaunt: "Run the binary! Touch the execution trigger! The master sandbox is hungry for your terminal!"
      },
      11: {
        title: "STAGE 11: THE BINARY MASTER",
        tags: "ACT IV • STAGE 11 • TARGET: A1Z26 ALPHABET CODE",
        summary: "CLEARANCE_CODE.txt contains 16-15-12-01-18-09-19 -> POLARIS -> sorted alphabetically: ailnors.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "A1Z26 code intercepted! Click on [CLEARANCE_CODE.txt]. Decode 16-15-12-01-18-09-19 to POLARIS, sorted as ailnors!",
        taraWhereToClick: "Click Card 11 [CLEARANCE_CODE.txt] in the Evidence Vault below.",
        taraModalGuide: "Convert numbers to letters: 16=P, 15=O, 12=L, 01=A, 18=R, 09=I, 19=S (POLARIS). Sorted alphabetically: ailnors.",
        ishaanTaunt: "POLARIS has fallen from my digital sky. The master clearance belongs to me."
      },
      12: {
        title: "STAGE 12: THE WHITEOUT SIGNATURE",
        tags: "ACT V • STAGE 12 • TARGET: STEGANOGRAPHY",
        summary: "Emergency log text was rendered invisible in pure white font.",
        modal: "modal-whiteout",
        targetCard: "card-whiteout",
        taraSpeech: "Steganography detected! Click Card 12 [The Whiteout Signature] and highlight all text with Ctrl+A.",
        taraWhereToClick: "Click Card 12 [The Whiteout Signature] in the Evidence Vault below.",
        taraModalGuide: "Select all text or toggle the UV filter to expose the hidden clearance phrase CLEARANCE_ALPHA.",
        ishaanTaunt: "Blank pages hide no secrets from me. You look into an empty void."
      },
      13: {
        title: "STAGE 13: THE ROT-4 IEEE SHIFT",
        tags: "ACT V • STAGE 13 • TARGET: DYNAMIC CAESAR",
        summary: "Encoded beacon message shifted by the acronym length of IEEE (4).",
        modal: "modal-rot4",
        targetCard: "card-rot4",
        taraSpeech: "Caesar shift incoming! Click Card 13 [ROT-4 Shift] and shift letters backward by 4 (ADITIS13).",
        taraWhereToClick: "Click Card 13 [ROT-4 Shift] in the Evidence Vault below.",
        taraModalGuide: "Take the string 'EHMXMW13' and shift each letter backward by 4 in the alphabet to get ADITIS13.",
        ishaanTaunt: "A Caesar shift from antiquity? You will never reconstruct Dr. Aditi's beacon!",
        taraClue: "Shift each letter backward by 4 positions in the alphabet. EHMXMW13 becomes ADITIS13!"
      },
      14: {
        title: "STAGE 14: THE ATBASH CIPHER MIRROR",
        tags: "ACT V • STAGE 14 • TARGET: ALPHABET REVERSAL",
        summary: "Dr. Aditi reversed the alphabet mirror table (A<->Z, B<->Y) to protect project archives.",
        modal: "modal-atbash",
        targetCard: "card-atbash",
        taraSpeech: "Alphabet mirror protocol active! Click Card 14 [Atbash Mirror] and reverse KILQVBG to PROJECT.",
        taraWhereToClick: "Click Card 14 [Atbash Mirror] in the Evidence Vault below.",
        taraModalGuide: "Reverse the letters of KILQVBG using the standard Atbash cipher to get PROJECT.",
        ishaanTaunt: "Mirrors only reflect your inevitable defeat.",
        taraClue: "Mirror the letters across the alphabet: K=P, I=R, L=O, Q=J, V=E, B=C, G=T spells PROJECT!"
      },
      15: {
        title: "STAGE 15: THE POLYBIUS COORDINATE TRAIL",
        tags: "ACT V • STAGE 15 • TARGET: 2D GRID LOOKUP",
        summary: "Recovered 5x5 coordinate matrix stream maps to forensic vector tokens.",
        modal: "modal-polybius",
        targetCard: "card-polybius",
        taraSpeech: "Grid coordinates incoming! Click Card 15 [Polybius Trail] and lookup (Row, Column) coordinates for VECTOR.",
        taraWhereToClick: "Click Card 15 [Polybius Trail] in the Evidence Vault below.",
        taraModalGuide: "Map pairs (5,1), (1,5), (1,3), (4,4), (3,4), (4,2) to their grid letters to get VECTOR.",
        ishaanTaunt: "Coordinates in 2D space? My neural network spans infinite dimensions!",
        taraClue: "Map the (Row, Column) coordinates: (5,1)=V, (1,5)=E, (1,3)=C, (4,4)=T, (3,4)=O, (4,2)=R spells VECTOR!"
      },
      16: {
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

if re.search(old_meta_pattern, html):
    html = re.sub(old_meta_pattern, new_meta, html, count=1)
    print("3. Replaced NEXUS_STAGES_META")
else:
    print("Failed to find NEXUS_STAGES_META")

# 4. Update Cards Grid
old_cards_pattern = r'<div class="nexus-cards-grid" id="nexus-cards-grid">[\s\S]*?<!-- Stage 12 -->'
new_cards_head = '''<div class="nexus-cards-grid" id="nexus-cards-grid">
        
        <!-- Stage 01 -->
        <div class="nexus-clean-card active-objective" id="card-origin" data-act="act1" onclick="openModal('modal-origin')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 01</span>
            <span style="font-size:10px; color:#00ff88;">● ACTIVE</span>
          </div>
          <div class="nexus-card-icon">📄</div>
          <div class="nexus-card-name">Farewell.doc</div>
          <div class="nexus-card-status">Disappearing Text • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 02 -->
        <div class="nexus-clean-card" id="card-memory" data-act="act1" onclick="openModal('modal-origin')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 02</span>
            <span style="font-size:10px; color:#ffb000;">● DIR ORIGIN</span>
          </div>
          <div class="nexus-card-icon">📁</div>
          <div class="nexus-card-name">README.doc</div>
          <div class="nexus-card-status">Directory ORIGIN • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 03 -->
        <div class="nexus-clean-card" id="card-timeline" data-act="act1" onclick="openModal('modal-incident-logs')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 03</span>
            <span style="font-size:10px; color:#94a3b8;">● AUDIT</span>
          </div>
          <div class="nexus-card-icon">📅</div>
          <div class="nexus-card-name">Incident_Logs.doc</div>
          <div class="nexus-card-status">Calendar Anomaly • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 04 -->
        <div class="nexus-clean-card" id="card-audit" data-act="act1" onclick="openModal('modal-security-audit')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 04</span>
            <span style="font-size:10px; color:#94a3b8;">● PERIMETER</span>
          </div>
          <div class="nexus-card-icon">⏱️</div>
          <div class="nexus-card-name">Security_Audit.pdf</div>
          <div class="nexus-card-status">Timestamp Anomaly • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 05 -->
        <div class="nexus-clean-card" id="card-acrostic" data-act="act2" onclick="openModal('modal-acrostic')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 05</span>
            <span style="font-size:10px; color:#94a3b8;">● ACROSTIC</span>
          </div>
          <div class="nexus-card-icon">📝</div>
          <div class="nexus-card-name">Aditi_Memo.doc</div>
          <div class="nexus-card-status">Acrostic Note • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 06 -->
        <div class="nexus-clean-card" id="card-font" data-act="act2" onclick="openModal('modal-font')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 06</span>
            <span style="font-size:10px; color:#94a3b8;">● TYPOGRAPHY</span>
          </div>
          <div class="nexus-card-icon">🔤</div>
          <div class="nexus-card-name">AUTHENTIC_LOG.doc</div>
          <div class="nexus-card-status">Font Verification • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 07 -->
        <div class="nexus-clean-card" id="card-version" data-act="act2" onclick="openModal('modal-version-hist')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 07</span>
            <span style="font-size:10px; color:#94a3b8;">● REVISION</span>
          </div>
          <div class="nexus-card-icon">🕒</div>
          <div class="nexus-card-name">Incident_Report.doc</div>
          <div class="nexus-card-status">Version History • Click to Inspect &rarr;</div>
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
        <div class="nexus-clean-card" id="card-stego" data-act="act3" onclick="openModal('modal-stego')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag">STAGE 09</span>
            <span style="font-size:10px; color:#94a3b8;">● STEGANO</span>
          </div>
          <div class="nexus-card-icon">🖼️</div>
          <div class="nexus-card-name">Dark_Terminal.png</div>
          <div class="nexus-card-status">Optical Steganography • Click to Inspect &rarr;</div>
        </div>

        <!-- Stage 10 -->
        <div class="nexus-clean-card" id="card-trap" data-act="act4" onclick="openModal('modal-honeypot')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:#ff003c; border-color:#ff003c;">STAGE 10</span>
            <span style="font-size:10px; color:#ff003c;">☠️ HONEYPOT</span>
          </div>
          <div class="nexus-card-icon" style="color:#ff003c;">⚠️</div>
          <div class="nexus-card-name">DO_NOT_RUN.exe</div>
          <div class="nexus-card-status">Quarantine Trap • Bypass with Key &rarr;</div>
        </div>

        <!-- Stage 11 -->
        <div class="nexus-clean-card" id="card-clearance" data-act="act4" onclick="openModal('modal-clearance')">
          <div class="nexus-card-topbar">
            <span class="nexus-stage-tag" style="color:var(--nexus-cyan);">STAGE 11</span>
            <span style="font-size:10px; color:var(--nexus-cyan);">🔢 A1Z26</span>
          </div>
          <div class="nexus-card-icon" style="color:var(--nexus-cyan);">🏆</div>
          <div class="nexus-card-name">CLEARANCE_CODE.txt</div>
          <div class="nexus-card-status">Binary Master • Alphabet Index &rarr;</div>
        </div>

        <!-- Stage 12 -->'''

if re.search(old_cards_pattern, html):
    html = re.sub(old_cards_pattern, new_cards_head, html, count=1)
    print("4. Replaced Cards Grid (Stages 1-11)")
else:
    print("Failed to find Cards Grid")

# 5. Update runChecksumScan
old_checksum_pattern = r'// Stage 1: ISHAAN Recovery Terminal[\s\S]*?// Stage 12: The Whiteout Signature'
new_checksum = '''// Stage 1: The Disappearing Message (ORIGIN)
        if (clean === "ORIGIN" || clean === "ACCESS" || clean === "RECOVERACCESS" || clean === "ORIGINKEY" || clean === "ORIGIN_KEY" || clean === "FIRSTGATE") {
          matched = true;
          recordStageCleared(1);
          currentStage = 2;
          localStorage.setItem('failsafe_stage', '2');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: FIRST GATE VERIFIED (ORIGIN). PROMOTED TO STAGE 02.`, "green");
          reportTelemetryAction("Solved Stage 01 (Disappearing Message) - Promoted to Stage 02");
          updateMissionBanner(2, "ACT I // CH. 02: THE WRONG FOLDER", "Inside directory ORIGIN, README.doc contains the ASCII summation cipher: aDIti@28. Compute the sum.");
          triggerIshaanSnarl(1);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 01 SOLVED!</strong><br>First gate cleared: ORIGIN! Clearance elevated to Level 02.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 02] README.doc</strong> on the left! Calculate the ASCII sum of 'aDIti@28'.`);
          updateClueBatteryDisplay();

        // Stage 2: The Wrong Folder (629 / LOOK BEHIND THE DATE)
        } else if (clean === "629" || clean === "LOOKBEHINDTHEDATE" || clean === "LOOK BEHIND THE DATE" || clean === "123456" || clean === "MEMORYRESTORED" || clean === "MEMORY_RESTORED") {
          matched = true;
          recordStageCleared(2);
          currentStage = 3;
          localStorage.setItem('failsafe_stage', '3');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ORIGIN DIRECTIVE VERIFIED (629). PROMOTED TO STAGE 03.`, "green");
          reportTelemetryAction("Solved Stage 02 (The Wrong Folder) - Promoted to Stage 03");
          updateMissionBanner(3, "ACT I // CH. 03: THE DATE THAT DOESN'T EXIST", "Audit Incident_Logs.doc for calendar validity. Identify the impossible calendar date.");
          triggerIshaanSnarl(2);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 02 SOLVED!</strong><br>Identifier checksum 629 authenticated!<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 03] Incident_Logs.doc</strong> on the left! Cross-examine calendar dates in 2025.`);
          updateClueBatteryDisplay();

        // Stage 3: The Date That Doesn't Exist (28/02/2025 / 02292025)
        } else if (clean === "28022025" || clean === "02292025" || clean === "29022025" || clean === "20250229" || clean === "FEB292025" || clean === "29022036" || clean === "20360229" || clean === "FEB292036" || clean === "28/02/2025" || clean === "29/02/2025") {
          matched = true;
          recordStageCleared(3);
          currentStage = 4;
          localStorage.setItem('failsafe_stage', '4');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CALENDAR CONTRADICTION UNMASKED (28/02/2025). PROMOTED TO STAGE 04.`, "green");
          reportTelemetryAction("Solved Stage 03 (Date Anomaly) - Promoted to Stage 04");
          updateMissionBanner(4, "ACT I // CH. 04: THE TIMESTAMP MURDER MYSTERY", "Cross-examine gate exit vs terminal access in Security_Audit.pdf. Enter the impossible timestamp.");
          triggerIshaanSnarl(3);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 03 SOLVED!</strong><br>Calendar anomaly unmasked! 2025 is not a leap year.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 04] Security_Audit.pdf</strong> on the left! Locate the impossible manual override timestamp.`);
          updateClueBatteryDisplay();

        // Stage 4: The Timestamp Murder Mystery (22:46)
        } else if (clean === "22:46" || clean === "2246" || clean === "22:46PM" || clean === "2246PM") {
          matched = true;
          recordStageCleared(4);
          currentStage = 5;
          localStorage.setItem('failsafe_stage', '5');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: OVERRIDE CONFLICT ISOLATED (22:46). PROMOTED TO STAGE 05.`, "green");
          reportTelemetryAction("Solved Stage 04 (Timestamp Anomaly) - Promoted to Stage 05");
          updateMissionBanner(5, "ACT II // CH. 05: THE SIMPLE ACROSTIC NOTE", "Dr. Aditi concealed emergency directives in the first letters of each sentence in Aditi_Memo.doc.");
          triggerIshaanSnarl(4);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 04 SOLVED!</strong><br>Timestamp 22:46 proved physically impossible!<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 05] Aditi_Memo.doc</strong> on the left! Read the first letter of each sentence.`);
          updateClueBatteryDisplay();

        // Stage 5: The Simple Acrostic Note (SAFE)
        } else if (clean === "SAFE" || clean === "S-A-F-E" || clean === "SAFE" || clean === "SAFE") {
          matched = true;
          recordStageCleared(5);
          currentStage = 6;
          localStorage.setItem('failsafe_stage', '6');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ACROSTIC DIRECTIVE RECOVERED (SAFE). PROMOTED TO STAGE 06.`, "green");
          reportTelemetryAction("Solved Stage 05 (Acrostic Note) - Promoted to Stage 06");
          updateMissionBanner(6, "ACT II // CH. 06: WHICH ADITI IS REAL?", "Compare authentic and decoy logs against lab style standards. Identify the authentic font family.");
          triggerIshaanSnarl(5);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 05 SOLVED!</strong><br>Acrostic cipher decrypted: SAFE.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 06] AUTHENTIC_LOG.doc</strong> on the left! Verify the font against lab standards.`);
          updateClueBatteryDisplay();

        // Stage 6: Which Aditi Is Real? (ARIAL)
        } else if (clean === "ARIAL" || clean === "AUTHENTIC" || clean === "ARIAL11" || clean === "ARIAL11PT") {
          matched = true;
          recordStageCleared(6);
          currentStage = 7;
          localStorage.setItem('failsafe_stage', '7');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: AUTHENTIC FONT VERIFIED (ARIAL). PROMOTED TO STAGE 07.`, "green");
          reportTelemetryAction("Solved Stage 06 (Font Style) - Promoted to Stage 07");
          updateMissionBanner(7, "ACT II // CH. 07: THE REVISION HISTORY CONFLICT", "Inspect Incident_Report.doc. Toggle version history to Dr. Aditi's original revision at 20:18.");
          triggerIshaanSnarl(6);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 06 SOLVED!</strong><br>Font style ARIAL confirmed! Decoy document isolated.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 07] Incident_Report.doc</strong> on the left! Roll back version history to 20:18.`);
          updateClueBatteryDisplay();

        // Stage 7: The Revision History Conflict (CORRUPTED / FALSE_RECORDS)
        } else if (clean === "CORRUPTED" || clean === "FALSE_RECORDS" || clean === "FALSERECORDS" || clean === "OVERRIDEFAILED" || clean === "OVERRIDE_FAILED" || clean === "HISTORY") {
          matched = true;
          recordStageCleared(7);
          currentStage = 8;
          localStorage.setItem('failsafe_stage', '8');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: UNTAMPERED REVISION RETRIEVED (CORRUPTED). PROMOTED TO STAGE 08.`, "green");
          reportTelemetryAction("Solved Stage 07 (Version Conflict) - Promoted to Stage 08");
          updateMissionBanner(8, "ACT III // CH. 08: EMERGENCY CW BEACON", "Decode the Morse audio carrier tones (.-- .... .. - .) transmitted from Dr. Aditi's bunker.");
          triggerIshaanSnarl(7);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 07 SOLVED!</strong><br>Version rollback successful! Genuine status warning: CORRUPTED.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 08] audio_log_07.mp3</strong> on the left! Decode the CW Morse tones.`);
          updateClueBatteryDisplay();

        // Stage 8: Morse Code Audio Transmission (WHITE)
        } else if (clean === "WHITE" || clean === "SOSADITI" || clean === "SOS_ADITI" || clean === "MORSE" || clean === "BEACON") {
          matched = true;
          recordStageCleared(8);
          currentStage = 9;
          localStorage.setItem('failsafe_stage', '9');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CW AUDIO MORSE DECODED (WHITE). PROMOTED TO STAGE 09.`, "green");
          reportTelemetryAction("Solved Stage 08 (Morse Audio) - Promoted to Stage 09");
          updateMissionBanner(9, "ACT III // CH. 09: THE STEGANOGRAPHY MASK", "Dark_Terminal.png appears pitch black. Crank brightness and contrast to maximum to reveal the core password.");
          triggerIshaanSnarl(8);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 08 SOLVED!</strong><br>Morse beacon WHITE authenticated!<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 09] Dark_Terminal.png</strong> on the left! Boost brightness and contrast to illuminate hidden text.`);
          updateClueBatteryDisplay();

        // Stage 9: The Steganography Mask (SHADOW_CORE) - Replaces Git Reflog
        } else if (clean === "SHADOWCORE" || clean === "SHADOW_CORE" || clean === "SHADOW CORE") {
          matched = true;
          recordStageCleared(9);
          currentStage = 10;
          localStorage.setItem('failsafe_stage', '10');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: OPTICAL STEGANOGRAPHY RESOLVED (SHADOW_CORE). PROMOTED TO STAGE 10.`, "green");
          reportTelemetryAction("Solved Stage 09 (Steganography Mask) - Promoted to Stage 10");
          updateMissionBanner(10, "ACT IV // CH. 10: PSYCHOLOGICAL HONEYPOT", "WARNING: DO_NOT_RUN.exe is an active AI honeypot trap! Enter BYPASS in the main shell.");
          triggerIshaanSnarl(9);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 09 SOLVED!</strong><br>Dark terminal decoded: SHADOW_CORE! Approaching final quarantine sectors.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Disarm <strong>[STAGE 10] DO_NOT_RUN.exe</strong> on the left! Enter BYPASS directive in Tactical Shell.`);
          updateClueBatteryDisplay();

        // Stage 10: Honeypot Trap Bypass (BYPASS)
        } else if (clean === "BYPASS" || clean === "SKIP" || clean === "DISARM") {
          matched = true;
          recordStageCleared(10);
          currentStage = 11;
          localStorage.setItem('failsafe_stage', '11');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: AI HONEYPOT DISARMED (BYPASS). PROMOTED TO STAGE 11.`, "green");
          reportTelemetryAction("Solved Stage 10 (Trap Bypass) - Promoted to Stage 11");
          updateMissionBanner(11, "ACT IV // CH. 11: THE BINARY MASTER", "CLEARANCE_CODE.txt contains 16-15-12-01-18-09-19 -> POLARIS -> sort alphabetically: ailnors.");
          triggerIshaanSnarl(10);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 10 SOLVED!</strong><br>AI honeypot disarmed safely without penalty!<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 11] CLEARANCE_CODE.txt</strong> on the left! Convert numbers to letters and sort alphabetically.`);
          updateClueBatteryDisplay();

        // Stage 11: The Binary Master (ailnors / POLARIS) - Replaces IEEE 6-9-11 -> Advances to Stage 12
        } else if (clean === "AILNORS" || clean === "POLARIS" || clean === "16151201180919" || clean === "16-15-12-01-18-09-19" || clean === "6911" || clean === "6-9-11") {
          matched = true;
          recordStageCleared(11);
          currentStage = 12;
          localStorage.setItem('failsafe_stage', '12');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: A1Z26 CLEARANCE KEY VERIFIED (ailnors). PROMOTED TO STAGE 12.`, "green");
          reportTelemetryAction("Solved Stage 11 (Binary Master) - Promoted to Stage 12");
          updateMissionBanner(12, "ACT V // CH. 12: THE WHITEOUT SIGNATURE", "Emergency log text was rendered invisible in pure white font. Highlight or depolarize to reveal.");
          triggerIshaanSnarl(11);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 11 SOLVED!</strong><br>A1Z26 master key authenticated (ailnors)! Infiltrating Act V deep intel.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 12] Whiteout_Signature.doc</strong> on the left! Expose Dr. Aditi's white-on-white text layer.`);
          updateClueBatteryDisplay();
          if (typeof updateNexusDashboard === 'function') updateNexusDashboard();

        // Stage 12: The Whiteout Signature'''

if re.search(old_checksum_pattern, html):
    html = re.sub(old_checksum_pattern, new_checksum, html, count=1)
    print("5. Replaced runChecksumScan (Stages 1-11)")
else:
    print("Failed to find runChecksumScan")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated aditi_os_widget.html!")
