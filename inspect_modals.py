import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    text = f.read()

modals = re.findall(r'id="(modal-[^"]+)"', text)
print("Found modals:", modals)

cards = re.findall(r'id="(card-[^"]+)"', text)
print("Found cards:", cards)
