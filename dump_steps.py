import json

with open(r'C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            step = data.get('step_index')
            if step in [25, 2342] or step > 15000:
                print(f"=== STEP {step} ===")
                with open(f"step_{step}.txt", "w", encoding="utf-8") as out:
                    out.write(data.get('content', ''))
                print(f"Wrote step_{step}.txt")
