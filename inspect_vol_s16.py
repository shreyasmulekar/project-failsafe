import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('VOLUNTEER_PUZZLE_GUIDE.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx16 = text.find('Stage 16')
if idx16 != -1:
    print(text[idx16-50:idx16+1500])
else:
    print("Stage 16 not found in VOLUNTEER_PUZZLE_GUIDE.md")
