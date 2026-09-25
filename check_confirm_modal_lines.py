import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="modal-clue-confirm"' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i:i+60]))
        break
