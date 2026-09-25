with open('puzzles_detailed.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
puzzles = re.split(r'###?\s*Puzzle\s+(\d+)', text)
if len(puzzles) <= 1:
    puzzles = re.split(r'Puzzle\s+(\d+)\s*[—–-]', text)

print(f"Found segments: {len(puzzles)}")
for i in range(1, len(puzzles), 2):
    p_num = puzzles[i]
    p_body = puzzles[i+1]
    print(f"\n==================== PUZZLE {p_num} ====================")
    # Print lines of body
    for line in p_body.strip().split('\n')[:35]:
        print(line.encode('ascii', 'replace').decode())
