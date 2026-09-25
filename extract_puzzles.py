with open('step_25.txt', 'r', encoding='utf-8') as f:
    text25 = f.read()

with open('step_2342.txt', 'r', encoding='utf-8') as f:
    text2342 = f.read()

with open('all_puzzles_clean.txt', 'w', encoding='utf-8') as out:
    out.write("=== STEP 25 (MASTER DOCUMENT) ===\n")
    out.write(text25)
    out.write("\n\n=== STEP 2342 (ADDITIONAL PUZZLES) ===\n")
    out.write(text2342)

print("Saved all_puzzles_clean.txt")
