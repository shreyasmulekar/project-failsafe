with open('step_25_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    l = line.strip()
    if any(k in l.lower() for k in ['stage 1', 'stage 2', 'stage 3', 'stage 4', 'stage 5', 'stage 6', 'stage 7', 'stage 8', 'stage 9', 'stage 10', 'stage 11', 'stage 12', 'stage 13', 'stage 14', 'stage 15', 'stage 16', '3.', '4.', '5.', '6.', '7.', '8.', 'puzzle']):
        print(f"L{i:4d}: {l[:100]}")
