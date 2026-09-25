import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function handleRound2GrandVictory' in line:
        print(f"Line {i+1}: {line}")
        print(''.join(lines[i:i+30]))
        break
