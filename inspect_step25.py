with open('step_25.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Total length of step_25.txt: {len(text)} characters")

# Find all lines starting with numbers or uppercase titles
lines = text.split('\n')
for i, line in enumerate(lines):
    l = line.strip()
    if any(l.startswith(prefix) for prefix in ['Stage ', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '11.', '12.', 'Puzzle ', '## ']):
        print(f"L{i}: {l[:80]}")
