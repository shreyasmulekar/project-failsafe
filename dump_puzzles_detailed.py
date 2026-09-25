with open('puzzles_from_step25.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by section 4. Comprehensive Puzzle Master Sheets
idx = text.find("4. Comprehensive Puzzle Master Sheets")
if idx != -1:
    content = text[idx:]
else:
    content = text

with open('puzzles_detailed.txt', 'w', encoding='utf-8') as out:
    out.write(content)

print("Wrote puzzles_detailed.txt")
