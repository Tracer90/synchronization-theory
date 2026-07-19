import re, os

with open("C:\\Projects\\FREE_EVER\\research\\axis_of_transition\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract the NEW CSS (between <style> and </style>)
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css = style_match.group(1) if style_match else ""

# Extract sections by their <!-- SECTION NUM. NAME --> markers
sections_raw = re.split(r'<!-- =+ -->\n<!-- (\d+)\. ([^<]+) -->\n<!-- =+ -->', html)

sections = []
for i in range(1, len(sections_raw), 3):
    if i+2 < len(sections_raw):
        num = sections_raw[i].strip()
        title = sections_raw[i+1].strip()
        content = sections_raw[i+2]
        sections.append((num, title, content))

# Section title map (display names)
title_map = {
    "1": "Суть открытия",
    "2": "История циклов",
    "3": "Девять принципов",
    "4": "Архитектура",
    "5": "Negative & Positive Intelligence",
    "6": "Природа связей",
    "7": "Религии",
    "8": "Расшифровка рисунка",
    "9": "Практическое применение",
    "10": "Техническая спецификация",
    "11": "Предсказания",
    "12": "Гипотеза работы"
}

# Generate nav with prev/next + portal links
def nav(current_num):
    links = ""
    # Portal link
    links += f"<a href='../../'>Главная</a><a href='../index.html'>Статья</a>"
    # Section links
    for n, t, _ in sections:
        cls = " sel" if n == current_num else ""
        fn = f"{int(n):02d}_{t.lower().replace(' ', '_').replace('&','')}.html"
        fn_encoded = fn.replace('%', '%25')
        # Use direct cyrillic filename
        links += f"<a href='{fn}'{cls}>{n}</a>"
    # Next/Prev
    nums = [int(s[0]) for s in sections]
    cur = int(current_num)
    if cur > 1:
        for n, t, _ in sections:
            if int(n) == cur - 1:
                fn = f"{int(n):02d}_{t.lower().replace(' ', '_').replace('&','')}.html"
                links += f"<a href='{fn}' style='margin-left:auto'>&larr; Назад</a>"
                break
    if cur < len(sections):
        for n, t, _ in sections:
            if int(n) == cur + 1:
                fn = f"{int(n):02d}_{t.lower().replace(' ', '_').replace('&','')}.html"
                links += f"<a href='{fn}'>Вперёд &rarr;</a>"
                break
    return f"<div class='nav'>{links}</div>"

def make_section(num, title_comment, content):
    t = title_comment.lower().replace(' ', '_').replace('&','')
    fname = f"{int(num):02d}_{t}.html"
    display_title = title_map.get(num, title_comment)
    
    # Clean content: remove footer section
    out_parts = []
    for line in content.split('\n'):
        if '<div class="ft">' in line:
            break
        out_parts.append(line)
    clean_content = '\n'.join(out_parts)
    
    page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{num}. {display_title} | Ось Перехода</title>
<style>{css}
</style>
</head>
<body>
{nav(num)}
<div class="c">
<h2>{num}. {display_title}</h2>
{clean_content}
</div>
<div class="ft">
<p><a href="../index.html">⬆ К полной статье</a> · <a href="../../">Исследование. Теория всего</a></p>
<p style="margin-top:6px;font-size:.85em;color:#444466">Ось Перехода · IAC v8 · Свободно для распространения</p>
</div>
</body>
</html>"""
    return fname, page

# Write sections
for num, title, content in sections:
    fname, page = make_section(num, title, content)
    path = os.path.join("C:\\Projects\\FREE_EVER\\research\\axis_of_transition\\sections", fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  {fname}")

print(f"\nTotal: {len(sections)} sections")
