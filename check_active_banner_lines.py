import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="active-clue-banner"' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i-2:i+30]))
        break
