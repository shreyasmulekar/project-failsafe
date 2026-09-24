# scratch/map_modals_detail.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

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
    start_line = None
    body_line = None
    for i, line in enumerate(lines):
        if f'id="{mid}"' in line:
            start_line = i + 1
        if start_line and not body_line and 'class="mil-modal-body' in line:
            body_line = i + 1
            break
    print(f"Stage {stg:02d} ({mid}): start=Line {start_line}, body=Line {body_line}")
