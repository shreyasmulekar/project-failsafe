import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('VOLUNTEER_PUZZLE_GUIDE.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("VOLUNTEER_PUZZLE_GUIDE.md length:", len(text))
print(text[:1200])
