import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '/api/teams/finish' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i:i+80]))
        break
