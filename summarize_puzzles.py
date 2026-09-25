with open('puzzles_from_step25.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by "Puzzle "
puzzles = re.split(r'(?=Puzzle\s+\d+)', text)

with open('puzzles_summary.txt', 'w', encoding='utf-8') as out:
    for p in puzzles:
        first_line = p.strip().split('\n')[0] if p.strip() else ""
        out.write(f"=== {first_line} ===\n")
        # Find Title, Mechanism, Clue, Key
        for line in p.split('\n')[:35]:
            out.write(f"  {line}\n")
        out.write("\n")

print("Wrote puzzles_summary.txt")
