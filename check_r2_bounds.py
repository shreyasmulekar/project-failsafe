import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

files = ['server.py', 'aditi_os_widget.html', 'admin.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {fn} ===")
    for i, line in enumerate(lines):
        if any(pattern in line for pattern in [
            'round_2_stage', 'round2CurrentStage', 'round2_current_stage', 'R2', 'r2'
        ]) and any(n in line for n in ['15', '16', '17']):
            print(f"  Line {i+1}: {line.strip()}")
