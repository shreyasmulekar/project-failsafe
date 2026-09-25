import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('aditi_os_widget.html', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('const ROUND2_PUZZLE_DATA')
if idx != -1:
    print("Found ROUND2_PUZZLE_DATA at index:", idx)
    # print up to 10000 chars or find where puzzles 5, 12, 13, 14 are
    sub = text[idx:idx+25000]
    for p_num in [5, 12, 13, 14]:
        m = re.search(r'\b' + str(p_num) + r':\s*\{', sub)
        if m:
            print(f"=== PUZZLE {p_num} ===")
            start = m.start()
            print(sub[start:start+1800])
            print("="*60)
