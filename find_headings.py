with open('all_puzzles_clean.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('headings.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        line_s = line.strip()
        if len(line_s) > 0 and len(line_s) < 80:
            if any(ch in line_s for ch in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'Phase', 'Stage', 'Puzzle', 'Mechanism', 'Setup', 'Master Output', 'Key:']):
                out.write(f"Line {i:4d}: {line_s}\n")

print("Wrote headings.txt")
