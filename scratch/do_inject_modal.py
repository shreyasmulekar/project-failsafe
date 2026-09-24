with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("scratch/inject_guide_modal.py", "r", encoding="utf-8") as f:
    code = f.read()

# Extract guide_modal_html from scratch/inject_guide_modal.py
start_marker = 'guide_modal_html = """'
end_marker = '"""\n\nmodal_break_target'
p1 = code.find(start_marker) + len(start_marker)
p2 = code.find(end_marker, p1)
guide_modal_html = code[p1:p2]

if 'id="modal-puzzles-guide"' not in html:
    # insert before modal-round1-break
    target = 'id="modal-round1-break"'
    pos = html.find(target)
    div_start = html.rfind('<div', 0, pos)
    html = html[:div_start] + guide_modal_html + "\n\n  " + html[div_start:]
    with open("aditi_os_widget.html", "w", encoding="utf-8") as out:
        out.write(html)
    print("modal-puzzles-guide DIV successfully injected!")
else:
    print("Already has id=modal-puzzles-guide!")
