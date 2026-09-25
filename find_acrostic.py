with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="modal-acrostic"' in line:
        print(f"Line {i+1}:")
        for j in range(i, min(len(lines), i+80)):
            print(f"{j+1}: {lines[j].encode('ascii', 'replace').decode()}", end="")
        break
