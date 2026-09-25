import json

with open(r'C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step == 0:
            with open("step_0.txt", "w", encoding="utf-8") as out:
                out.write(data.get('content', ''))
        elif step == 27:
            with open("step_27.txt", "w", encoding="utf-8") as out:
                out.write(data.get('content', ''))
print("Extracted steps 0 and 27")
