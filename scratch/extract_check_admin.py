import re
import subprocess

with open("admin.html", "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"Total script tags in admin.html: {len(scripts)}")

has_error = False
for i, text in enumerate(scripts):
    if len(text.strip()) > 50:
        script_path = f"scratch/admin_script_{i}.js"
        with open(script_path, "w", encoding="utf-8") as out:
            out.write(text)
        res = subprocess.run(["node", "--check", script_path], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Script {i} (len: {len(text)}): SYNTAX OK")
        else:
            has_error = True
            print(f"Script {i} (len: {len(text)}): SYNTAX ERROR!\n{res.stderr}")

if not has_error:
    print("ALL ADMIN SCRIPTS HAVE 100% VALID SYNTAX!")
