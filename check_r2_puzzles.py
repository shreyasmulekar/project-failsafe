with open("aditi_os_widget.html", encoding="utf-8") as f:
    text = f.read()

import re

# Check ROUND2_PUZZLE_DATA keys
match = re.search(r'const ROUND2_PUZZLE_DATA = \{(.*?)\n    \};', text, re.DOTALL)
if match:
    data_str = match.group(1)
    for i in range(1, 16):
        key_pattern = rf'^\s*{i}:\s*\{{'
        has_key = bool(re.search(key_pattern, data_str, re.MULTILINE))
        print(f"Round 2 Puzzle {i:02d}: {'[OK] PRESENT' if has_key else '[FAIL] MISSING'}")
else:
    print("[FAIL] ROUND2_PUZZLE_DATA not found!")
