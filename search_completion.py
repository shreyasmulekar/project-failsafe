import sys
import re

files = ['server.py', 'aditi_os_widget.html', 'admin.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {fn} ===")
    matches = list(re.finditer(r'(?:track|track[_\s]?completion|complete[_\s]?track|completion|is_finished)', text, re.IGNORECASE))
    print(f"Total matches: {len(matches)}")
    # Print distinct matching lines or phrases
    seen = set()
    for m in matches:
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        snippet = text[start:end].replace('\n', ' ')
        if snippet not in seen:
            seen.add(snippet)
            if len(seen) <= 10:
                print("  ", snippet)
