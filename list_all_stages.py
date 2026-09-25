import server

print("=== ROUND 1 STAGES (server.STAGES) ===")
for s, data in server.STAGES.items():
    title = data.get('title', '').encode('ascii', 'replace').decode()
    print(f"Stage {s:2d}: {title} | keys={data.get('keys')}")

print("\n=== ROUND 2 STAGES (server.ROUND2_STAGES) ===")
if hasattr(server, 'ROUND2_STAGES'):
    for s, data in server.ROUND2_STAGES.items():
        title = data.get('title', '').encode('ascii', 'replace').decode()
        print(f"R2 Stage {s:2d}: {title} | keys={data.get('keys')}")
else:
    print("No ROUND2_STAGES in server.py")
