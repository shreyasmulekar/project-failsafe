import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="modal-clue-confirm"' in line:
        print(f"modal-clue-confirm at line {i+1}:")
        print(''.join(lines[i-2:i+20]))
        break

for i, line in enumerate(lines):
    if 'function updateModalTaraBanner' in line:
        print(f"updateModalTaraBanner at line {i+1}:")
        print(''.join(lines[i:i+40]))
        break
