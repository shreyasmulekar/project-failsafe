# scratch/check_all_16_modals.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = [
    (1, 'modal-recovery'),
    (2, 'modal-memory'),
    (3, 'modal-acrostic'),
    (4, 'modal-incident-logs'),
    (5, 'modal-clearance'),
    (6, 'modal-comments'),
    (7, 'modal-font'),
    (8, 'modal-spectro'),
    (9, 'modal-version-hist'),
    (10, 'modal-honeypot'),
    (11, 'modal-failsafe'),
    (12, 'modal-whiteout'),
    (13, 'modal-rot4'),
    (14, 'modal-atbash'),
    (15, 'modal-polybius'),
    (16, 'modal-frequency')
]

for stg, mid in modals:
    pos = text.find(f'id="{mid}"')
    if pos == -1:
        print(f'Stage {stg} ({mid}): NOT FOUND')
        continue
    # find where next modal starts or 3500 chars
    chunk = text[pos:pos+3500]
    has_guide = 'WHERE TO CLICK' in chunk
    inputs = re.findall(r'<input[^>]*id=["\']([^"\']+)["\']', chunk)
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', chunk, re.DOTALL)
    clean_btns = [re.sub(r'<[^>]+>', '', b).strip() for b in buttons if re.sub(r'<[^>]+>', '', b).strip() not in ['×', '✕', '◄ ARCHIVE [ESC]', '⛶ POPOUT', '⛶ POP-OUT']]
    print(f"Stage {stg:02d} ({mid}): has_guide={has_guide}, inputs={inputs}, btns={clean_btns}")
