with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = "function updateClueBatteryDisplay() {"
replacement = """function updateClueBatteryDisplay() {
      window.cluesRemaining = cluesRemaining;"""

if target in content and replacement not in content:
    content = content.replace(target, replacement, 1)
    print("Exported window.cluesRemaining in updateClueBatteryDisplay")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved aditi_os_widget.html")
