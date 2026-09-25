import re

with open('all_puzzles_clean.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "Stage 1", "Stage 2", etc. or section headings
matches = re.findall(r'(Stage\s*(?:[0-9]{1,2}|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)[\s\S]*?)(?=Stage\s*(?:[0-9]{1,2}|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)|\Z)', text, re.IGNORECASE)

print(f"Found {len(matches)} stage sections")
with open('stages_extracted.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        out.write("--------------------------------------------------\n")
        out.write(m[:1500]) # write head of each
        out.write("\n\n")

print("Wrote stages_extracted.txt")
