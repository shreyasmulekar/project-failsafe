import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    text = f.read()

# Check Round 1 Ishaan Taunts
idx1 = text.find("const snarls = [")
if idx1 != -1:
    idx2 = text.find("];", idx1)
    snarls_block = text[idx1:idx2]
    print("=== Round 1 Ishaan Snarls block ===")
    print(snarls_block)

# Check Round 2 ishaanTaunt occurrences
import re
r2_taunts = re.findall(r'ishaanTaunt:\s*"([^"]+)"', text)
print(f"\n=== Round 2 Ishaan Taunts Count: {len(r2_taunts)} ===")
for i, t in enumerate(r2_taunts, 1):
    print(f"Pz {i:02d}: {t}")
