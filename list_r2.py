import server

print("=== ROUND 2 STAGES ===")
for s, data in server.ROUND2_STAGES.items():
    title = str(data.get('title', '')).encode('ascii', 'replace').decode()
    keys = [str(k).encode('ascii', 'replace').decode() for k in data.get('keys', [])]
    print(f"R2 Stage {s:2d}: {title} | keys={keys}")
