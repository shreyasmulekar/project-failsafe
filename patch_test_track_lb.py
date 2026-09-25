with open('test_track_completion.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('state = get("/api/admin/state")', 'lb = get("/api/admin/leaderboard?pin=admin")\nstate = lb')
text = text.replace('state_final = get("/api/admin/state")', 'lb_final = get("/api/admin/leaderboard?pin=admin")\nstate_final = lb_final')

# Also in R2 solve, fix "password": k
text = text.replace('"password": "pass",\n        "stage": s,\n        "passcode": k,', '"stage": s,\n        "password": k,')

with open('test_track_completion.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated test_track_completion.py with /api/admin/leaderboard?pin=admin")
