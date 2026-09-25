import urllib.request
import json

BASE_URL = 'http://localhost:8000'

# First login as ALFA-1 to ensure team exists
login_req = urllib.request.Request(
    f'{BASE_URL}/api/teams/login',
    data=json.dumps({'team_id': 'ALFA-1', 'password': 'alfa2026'}).encode(),
    headers={'Content-Type': 'application/json'}
)
try:
    res = urllib.request.urlopen(login_req)
    print("Login ALFA-1:", json.loads(res.read().decode()).get("message"))
except Exception as e:
    print("Login error:", e)

# Test verification for stages 1 to 11
keys = [
    (1, 'ORIGIN'),
    (2, '629'),
    (3, '28/02/2025'),
    (4, '22:46'),
    (5, 'SAFE'),
    (6, 'ARIAL'),
    (7, 'CORRUPTED'),
    (8, 'WHITE'),
    (9, 'SHADOW_CORE'),
    (10, 'BYPASS'),
    (11, 'ailnors')
]

all_passed = True
for stage_num, key in keys:
    payload = {
        'team_id': 'ALFA-1',
        'stage': stage_num,
        'round': 1,
        'password': key
    }
    req = urllib.request.Request(
        f'{BASE_URL}/api/stage/unlock',
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json'}
    )
    try:
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode())
        success = data.get('success')
        next_stage = data.get('next_stage')
        msg = data.get('message')
        print(f"Stage {stage_num:2d} ({key:12s}): Success={success} | Next={next_stage} | Msg='{msg}'")
        if not success:
            all_passed = False
    except Exception as e:
        print(f"Stage {stage_num:2d} error:", e)
        all_passed = False

print("\nAll 11 Stages Verified Successfully!" if all_passed else "\nSome Stages Failed!")
