import sys
sys.stdout.reconfigure(encoding='utf-8')
import server

print('STAGES count:', len(server.STAGES))
for k in sorted(server.STAGES.keys()):
    print(f"  R1 Stage {k:2d}: {server.STAGES[k]['title']} -> next: {server.STAGES[k]['next_stage']} | keys: {server.STAGES[k]['keys']}")

print('\nROUND2_STAGES count:', len(server.ROUND2_STAGES))
for k in sorted(server.ROUND2_STAGES.keys()):
    print(f"  R2 Stage {k:2d}: {server.ROUND2_STAGES[k]['title']} -> next: {server.ROUND2_STAGES[k]['next_stage']} | keys: {server.ROUND2_STAGES[k]['keys']}")
