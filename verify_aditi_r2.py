# -*- coding: utf-8 -*-
with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check puzzle 5
assert 'COORDINATES: (1,3) &nbsp; (2,4) &nbsp; (3,5) &nbsp; (2,3) &nbsp; (1,5) &nbsp; (4,2)' in text
print('PASS: Puzzle 5 coordinates verified to match CIPHER!')

# Check puzzle 12
assert 'ROUND 02 // PUZZLE 12 OF 16' in text
assert '#00f0ff;">N</div>' not in text
assert '#00f0ff;">O</div>' not in text
assert '#00f0ff;">D</div>' not in text
assert '#00f0ff;">C</div>' not in text
print('PASS: Puzzle 12 grid highlights removed!')

# Check puzzle 13
assert 'ROUND 02 // PUZZLE 13 OF 16' in text
assert 'THE ALTERNATING CHECKER PATTERN' in text
assert 'Step 6' in text
print('PASS: Puzzle 13 Alternating Checker verified!')

# Check Perimeter removed
assert 'R2_13_PERIMETER' not in text
assert 'Perimeter Geometry Box Count' not in text
print('PASS: Old Puzzle 13 Perimeter Geometry deleted!')

# Check puzzles 14, 15, 16
assert 'ROUND 02 // PUZZLE 14 OF 16' in text
assert 'THE SHIFTED RING CIPHER' in text
assert 'ROUND 02 // PUZZLE 15 OF 16 [THE RED QUESTION]' in text
assert 'ROUND 02 // PUZZLE 16 OF 16' in text
assert 'HARDWARE FAILSAFE ALIGNMENT (KILL SWITCH)' in text
print('PASS: Puzzles 14, 15, 16 verified!')

# Check R2_ANSWERS has 16 entries and no 17
m = re.search(r'const R2_ANSWERS = \{(.*?)\};', text, re.DOTALL)
assert m
ans_block = m.group(1)
assert '16: ["0110"]' in ans_block
assert '17:' not in ans_block
print('PASS: R2_ANSWERS has exactly 16 stages!')

print('ALL ADITI OS WIDGET ASSERTIONS PASSED!')
