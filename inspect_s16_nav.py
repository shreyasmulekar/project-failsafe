import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx16 = text.find('16: {\n        cardId: "card-frequency"')
if idx16 == -1:
    idx16 = text.find('16: {')
print("STAGE_NAVIGATION_DATA 16 at", idx16)
print(text[idx16:idx16+1000])

idx_meta16 = text.find('16: {\n        title: "STAGE 16:')
if idx_meta16 == -1:
    idx_meta16 = text.find('16: {', 700000)
print("NEXUS_STAGES_META 16 at", idx_meta16)
print(text[idx_meta16:idx_meta16+1000])
