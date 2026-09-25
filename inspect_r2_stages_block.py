import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('ROUND2_STAGES = {')
idx_end = text.find('LEADERBOARD_STAGES =', idx_start)
if idx_end == -1:
    idx_end = text.find('\n\nclass', idx_start)

print("ROUND2_STAGES block length:", idx_end - idx_start)
print(text[idx_start:idx_start+800])
print("...")
print(text[idx_end-400:idx_end])
