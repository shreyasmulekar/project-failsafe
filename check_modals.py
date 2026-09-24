with open("aditi_os_widget.html", encoding="utf-8") as f:
    text = f.read()

modals = [
    ("Stage 01", "modal-recovery"),
    ("Stage 02", "modal-memory"),
    ("Stage 03", "modal-acrostic"),
    ("Stage 04", "modal-incident-logs"),
    ("Stage 05", "modal-clearance"),
    ("Stage 06", "modal-comments"),
    ("Stage 07", "modal-font"),
    ("Stage 08", "modal-spectro"),
    ("Stage 09", "modal-version-hist"),
    ("Stage 10", "modal-honeypot"),
    ("Stage 11", "modal-failsafe"),
    ("Stage 12", "modal-whiteout"),
    ("Stage 13", "modal-rot4"),
    ("Stage 14", "modal-atbash"),
    ("Stage 15", "modal-polybius"),
    ("Stage 16", "modal-frequency"),
]

for stg, m in modals:
    has_id = f'id="{m}"' in text
    print(f"{stg} ({m}): {'[OK] PRESENT' if has_id else '[FAIL] MISSING'}")
