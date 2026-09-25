import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("PARTICIPANT_UI_GUIDE_GOOGLE_DOC.md length:", len(text))
print(text[:800])
