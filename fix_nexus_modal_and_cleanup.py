# fix_nexus_modal_and_cleanup.py
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

fix_css = """
    /* Make mil-modal a floating high-tech centered popup */
    .mil-modal {
      position: fixed !important;
      top: 50% !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
      width: 920px !important;
      max-width: 92vw !important;
      height: 640px !important;
      max-height: 88vh !important;
      border-radius: 12px !important;
      z-index: 999999 !important;
      box-shadow: 0 0 50px rgba(0, 240, 255, 0.4), 0 20px 60px rgba(0, 0, 0, 0.95) !important;
      border: 1.5px solid var(--nexus-cyan) !important;
      background: rgba(6, 12, 24, 0.98) !important;
    }

    /* Hide redundant old floating assistant and old forensic sector header */
    #ethan-hunt-box {
      display: none !important;
    }
    .sector-header {
      display: none !important;
    }
    .forensic-sector {
      display: contents !important;
    }
    .main-workspace {
      display: contents !important;
    }
"""

if "/* Make mil-modal a floating high-tech centered popup */" not in html:
    html = html.replace("</style>", fix_css + "\n</style>", 1)

with open("aditi_os_widget.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied modal and cleanup CSS successfully!")
