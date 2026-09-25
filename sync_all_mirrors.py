import shutil
import os

print("--- Syncing All Mirrors ---")
files_to_sync = ["aditi_os_widget.html", "admin.html", "server.py"]
targets = [
    "public",
    "project-failsafe-2.0",
    "project-failsafe-2.0/public"
]

for src in files_to_sync:
    if not os.path.exists(src):
        print(f"Source file {src} not found!")
        continue
    src_size = os.path.getsize(src)
    for target_dir in targets:
        if os.path.exists(target_dir):
            dest = os.path.join(target_dir, src)
            shutil.copy2(src, dest)
            dest_size = os.path.getsize(dest)
            print(f"Copied {src} ({src_size}B) -> {dest} ({dest_size}B)")

print("--- Mirror Sync Completed ---")
