with open('test_track_completion.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"password": "pass",\n        "stage": s,\n        "passcode": k,', '"stage": s,\n        "password": k,')

with open('test_track_completion.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated test_track_completion.py with correct password key")
