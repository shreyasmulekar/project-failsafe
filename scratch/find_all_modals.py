import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

modal_ids = re.findall(r'id=["\'](modal-[^"\']+)["\']', html)
print(f"Found {len(modal_ids)} modal IDs:")
for m in sorted(set(modal_ids)):
    print(" -", m)
