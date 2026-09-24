import sys

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<header class="command-header">' in l:
        print("Header start:", i + 1)
    if '<section class="ethan-ai-deck"' in l:
        print("Deck start:", i + 1)
    if '<main class="main-workspace">' in l:
        print("Main workspace start:", i + 1)
    if 'id="modal-recovery"' in l:
        print("Modal recovery start:", i + 1)
        break
