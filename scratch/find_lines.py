with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if 'id="modal-memory"' in line:
            print(f"modal-memory found at line {i}")
        if 'function renderV1MemoryCards' in line:
            print(f"renderV1MemoryCards found at line {i}")
