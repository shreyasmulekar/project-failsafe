# scratch/inspect_modal_headers.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = [
    (1, 'modal-recovery', 'ISHAAN Recovery Terminal', 'Kernel Boot Lifecycle', 'ACCESS'),
    (2, 'modal-memory', 'ISHAAN Memory Core', 'Chronological Timestamp Order', '123456'),
    (3, 'modal-acrostic', 'Aditi Memo', 'First letter of each sentence', 'SAFE'),
    (4, 'modal-incident-logs', 'Incident Logs', 'Non-leap year calendar anomaly', '28/02/2025'),
    (5, 'modal-clearance', 'Clearance Code', 'A1Z26 Alphabet Position Cipher', 'POLARIS'),
    (6, 'modal-comments', 'System Diagnostics', 'Inspect resolved comments margin', 'MARGIN_KEY'),
    (7, 'modal-font', 'Authentic Log', 'Typography Font Parity (Arial vs Times)', 'ARIAL'),
    (8, 'modal-spectro', 'Audio Log 07', 'CW Morse Code Spectrogram', 'WHITE'),
    (9, 'modal-version-hist', 'Version Scrub', 'Git Reflog Rollback', 'REVERT_COMMIT_7B'),
    (10, 'modal-honeypot', 'DO NOT RUN.exe', 'Evade execution binary; quarantine bypass', 'DISARM'),
    (11, 'modal-failsafe', 'IEEE WIE Core Values', 'Letter lengths: Wisdom(6), Integrity(9), Empowerment(11)', '6-9-11'),
    (12, 'modal-whiteout', 'The Whiteout Signature', 'Select all (Ctrl+A) to expose hidden white text', 'CLEARANCE_ALPHA'),
    (13, 'modal-rot4', 'Transmitted ROT-4 Signal', 'ROT-4 Caesar shift cipher', 'ADITIS13'),
    (14, 'modal-atbash', 'Atbash Inversion Stream', 'Atbash A<->Z alphabet mirror cipher', 'PROJECT'),
    (15, 'modal-polybius', 'Polybius Square Coordinate Stream', '5x5 Polybius grid coordinates', 'FAILSAFE'),
    (16, 'modal-frequency', 'Frequency Monogram Cipher', 'Letter frequency distribution count', 'CIPHER')
]

for stg, mid, title, mechanism, key in modals:
    pos = text.find(f'id="{mid}"')
    if pos == -1:
        print(f"Stage {stg} ({mid}): NOT FOUND")
        continue
    # find mil-modal-body
    body_pos = text.find('class="mil-modal-body', pos)
    body_start = text.find('>', body_pos) + 1
    sample = text[body_start:body_start+400].strip()
    print(f"=== STAGE {stg:02d}: {title} ({mid}) ===")
    print(f"Body start sample:\n{sample[:150]}...")
