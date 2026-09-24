# scratch/inspect_modals.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

modals = [
    ('Stage 1', 'modal-recovery'),
    ('Stage 2', 'modal-memory'),
    ('Stage 3', 'modal-acrostic'),
    ('Stage 4', 'modal-incident-logs'),
    ('Stage 5', 'modal-clearance'),
    ('Stage 6', 'modal-system-diagnostics'),
    ('Stage 7', 'modal-authentic-log'),
    ('Stage 8', 'modal-honeypot'),
    ('Stage 9', 'modal-frequency'),
    ('Stage 10', 'modal-core-dump'),
    ('Stage 11', 'modal-failsafe-command'),
    ('Stage 12', 'modal-whiteout'),
    ('Stage 13', 'modal-rot4'),
    ('Stage 14', 'modal-atbash'),
    ('Stage 15', 'modal-polybius'),
    ('Stage 16', 'modal-frequency-count')
]

for stg, mid in modals:
    pos = text.find(f'id="{mid}"')
    if pos == -1:
        pos = text.find(f"id='{mid}'")
    if pos == -1:
        print(f'{stg} ({mid}): NOT FOUND')
        continue
    # Grab the next 3500 characters
    chunk = text[pos:pos+3500]
    inputs = re.findall(r'<input[^>]*id=["\']([^"\']+)["\']', chunk)
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', chunk, re.DOTALL)
    clean_btns = [re.sub(r'<[^>]+>', '', b).strip() for b in buttons if re.sub(r'<[^>]+>', '', b).strip() not in ['×', '✕', '◄ ARCHIVE [ESC]', '⛶ POPOUT', '⛶ POP-OUT']]
    has_submit_box = 'TRANSMIT' in chunk or 'DECRYPT' in chunk or 'SUBMIT' in chunk or 'RESTORE' in chunk
    print(f"=== {stg} ({mid}) ===")
    print(f"  Inputs: {inputs}")
    print(f"  Buttons: {clean_btns}")
    print(f"  Has submit mechanism in chunk: {has_submit_box}")
