with open('step_25_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract from line 107 (3. Recommended Puzzle Progression Matrix) to the end
lines = text.split('\n')
with open('puzzles_from_step25.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines[105:]):
        out.write(f"{line}\n")

print(f"Wrote {len(lines[105:])} lines to puzzles_from_step25.txt")
