import sys
import re

files = ['server.py', 'aditi_os_widget.html', 'admin.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {fn} ===")
    for i, line in enumerate(lines):
        if any(pattern in line for pattern in [
            '>= 16', '> 16', '== 16', 's <= 16', 'stage <= 16', 'stages cleared', 'stages resolved',
            '>= 15', '> 15', '== 15', 'round_2_stage >=', 'round_2_stage >'
        ]):
            print(f"  Line {i+1}: {line.strip()}")
