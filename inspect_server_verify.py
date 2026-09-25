import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'def _handle_verify\s*\(|def _handle_submit\s*\(|path\s*==\s*[\'\"].*verify.*[\'\"]', text)
if m:
    start = m.start()
    print("Found verify in server.py at char", start)
    print(text[start:start+1800])
else:
    # Search for STAGES check
    for m2 in re.finditer(r'STAGES\.get\(|keys', text):
        start = max(0, m2.start() - 50)
        end = min(len(text), m2.end() + 200)
        print(text[start:end])
        print("="*40)
        break
