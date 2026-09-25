import json

with open(r'C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') == 25:
            with open("step_25_full.txt", "w", encoding="utf-8") as out:
                out.write(data.get('content', ''))
            print("Extracted full step 25! Length:", len(data.get('content', '')))
            break
