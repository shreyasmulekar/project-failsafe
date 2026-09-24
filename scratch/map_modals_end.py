# scratch/map_modals_end.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

modals = [
    (1, 'modal-recovery', 3301),
    (2, 'modal-memory', 3345),
    (3, 'modal-acrostic', 3691),
    (4, 'modal-incident-logs', 4220),
    (5, 'modal-clearance', 3736),
    (6, 'modal-comments', 3777),
    (7, 'modal-font', 3834),
    (8, 'modal-spectro', 4527),
    (9, 'modal-version-hist', 4674),
    (10, 'modal-honeypot', 3484),
    (11, 'modal-failsafe', 4483),
    (12, 'modal-whiteout', 3433),
    (13, 'modal-rot4', 3529),
    (14, 'modal-atbash', 3565),
    (15, 'modal-polybius', 3601),
    (16, 'modal-frequency', 3642)
]

for stg, mid, s_line in modals:
    # search for closing </div> of the modal
    # The modal starts at s_line
    # Count open/close divs from s_line
    div_count = 0
    end_line = None
    for i in range(s_line - 1, min(len(lines), s_line + 250)):
        l = lines[i]
        div_count += l.count('<div')
        div_count -= l.count('</div')
        if div_count == 0 and i > s_line - 1:
            end_line = i + 1
            break
    print(f"Stage {stg:02d} ({mid}): {s_line} to {end_line}")
    # print the last 3 lines before end_line
    if end_line:
        for k in range(max(s_line, end_line - 4), end_line + 1):
            print(f"   {k}: {lines[k-1].strip()[:70]}")
