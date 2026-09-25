import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith(('.html', '.py', '.txt', '.md', '.json')) and not f.startswith('verify_') and not f.startswith('test_'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read().lower()
                    if 'mass' in content:
                        print(f"Found 'mass' in {path}")
                    if 'system log' in content or 'system_log' in content or 'system logs' in content:
                        print(f"Found 'system log' in {path}")
            except:
                pass
