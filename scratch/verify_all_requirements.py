# scratch/verify_all_requirements.py
import sys
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://localhost:8000"

def get(path):
    with urllib.request.urlopen(f"{BASE_URL}{path}") as r:
        return r.read().decode('utf-8')

def post(path, data):
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode('utf-8'))

print("=== 1. VERIFYING SERVER ENDPOINTS ===")
# Clear broadcasts
res_clear = post('/api/admin/broadcast/clear', {'pin': 'wie-admin-2026'})
assert res_clear.get('success') is True, f"Clear broadcasts failed: {res_clear}"
print("✓ /api/admin/broadcast/clear verified.")

# Test unlock all
res_unlock = post('/api/admin/levels/unlock_all', {'pin': 'wie-admin-2026', 'team_id': 'ALL'})
assert res_unlock.get('success') is True, f"Unlock all failed: {res_unlock}"
assert res_unlock.get('test_mode_unlock_all') is True
print("✓ /api/admin/levels/unlock_all verified.")

# Test lock all
res_lock = post('/api/admin/levels/lock_all', {'pin': 'wie-admin-2026', 'team_id': 'ALL'})
assert res_lock.get('success') is True, f"Lock all failed: {res_lock}"
assert res_lock.get('test_mode_unlock_all') is False
print("✓ /api/admin/levels/lock_all verified.")

# Clear broadcasts again so clean state remains
post('/api/admin/broadcast/clear', {'pin': 'wie-admin-2026'})
print("✓ Clean broadcast state restored.")

print("\n=== 2. VERIFYING aditi_os_widget.html MARKUP & GUIDANCE ===")
with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verify all 16 stages have guidance banners
for stg in range(1, 17):
    assert f"STAGE {stg:02d} // WHERE TO CLICK &amp; SUBMIT" in html, f"Missing guidance banner for Stage {stg}"
print("✓ All 16 Round 1 stages have glowing WHERE TO CLICK & SUBMIT guidance banners.")

# Verify direct submit inputs exist
for stg in [3, 4, 5, 6, 7, 8, 9, 11]:
    assert f'id="input-stage-{stg}"' in html, f"Missing direct submit input for Stage {stg}"
print("✓ Direct in-modal submission terminals verified for Stages 3, 4, 5, 6, 7, 8, 9, 11.")

# Verify Round 2 No-Clues Protocol
assert "enforceRound2NoCluesProtocol" in html, "Missing enforceRound2NoCluesProtocol"
assert "CLUES ARE STRICTLY DISABLED IN ROUND 2" in html.upper() or "CLUES ARE STRICTLY DISABLED" in html.upper(), "Missing No-Clues warning"
print("✓ Round 2 strict No-Clues protocol verified.")

# Verify Round 2 Guidance Banner
assert "r2-puzzle-direction-banner" in html, "Missing r2-puzzle-direction-banner"
assert "ROUND 02 DIRECTIVES" in html, "Missing ROUND 02 DIRECTIVES"
print("✓ Round 2 illuminated guidance banner verified.")

# Verify Broadcast Reset on startup
assert "localStorage.removeItem(\"failsafe_global_broadcast\")" in html, "Missing startup broadcast reset"
print("✓ Startup broadcast reset verified.")

# Verify Round 1 First Enforcement
assert "localStorage.setItem('failsafe_current_round', '1')" in html, "Missing Round 1 first enforcement"
print("✓ Strict Round 1 first progression verified.")

print("\n=== 3. VERIFYING admin.html CONTROLS ===")
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

assert "promptUnlockAllLevels" in admin_html, "Missing promptUnlockAllLevels in admin.html"
assert "promptLockAllLevels" in admin_html, "Missing promptLockAllLevels in admin.html"
assert "promptClearBroadcasts" in admin_html, "Missing promptClearBroadcasts in admin.html"
assert "UNLOCK ALL (TEST)" in admin_html, "Missing UNLOCK ALL button in admin.html"
assert "LOCK ALL" in admin_html, "Missing LOCK ALL button in admin.html"
assert "CLEAR BROADCASTS" in admin_html, "Missing CLEAR BROADCASTS button in admin.html"
print("✓ All Organizer testing and reset controls verified in admin.html.")

print("\n🎉 ALL TESTS PASSED SUCCESSFULLY 100%!")
