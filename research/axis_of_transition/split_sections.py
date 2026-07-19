import re, os

with open("C:\\Projects\\FREE_EVER\\research\\axis_of_transition\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract shared CSS and style
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

# Nav template
def nav(current):
    links = ""
    for n, t, _ in sections:
        cls = " class='act'" if n == current else ""
        fn = f"{int(n):02d}_{t.lower().replace(' ', '_').replace('&','')}.html"
        links += f"<a href='{fn}'{cls}>{n}. {t}</a>"
    return f"<div class='nav'>{links}</div>"

# Template per section
def make_section(num, title, content):
    t = title.lower().replace(' ', '_').replace('&','')
    fname = f"{int(num):02d}_{t}.html"
    page = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{num}. {title} | Ось Перехода</title><style>{css}
.nav{{background:#0a0a1e;padding:10px 0;text-align:center;position:sticky;top:0;z-index:10;border-bottom:1px solid #222255;overflow-x:auto;white-space:nowrap}}
.nav a{{color:#6666aa;text-decoration:none;padding:6px 12px;font-size:0.8em;display:inline-block}}
.nav a:hover{{color:#ffd700}}
.nav a.act{{color:#ffd700;border-bottom:2px solid #ffd700}}
.ft2{{text-align:center;padding:20px;color:#444466;font-size:0.8em}}
</style></head><body>
{nav(num)}
<div class="c">
<h2>{num}. {title}</h2>
{content}
</div>
<div class="ft2"><a href="index.html">⬆ К полной статье</a> · <a href="../index.html">Все исследования</a> · Ось Перехода IAC v8</div>
</body></html>"""
    return fname, page

# Write sections
for num, title, content in sections:
    # Skip the FINAL section's bottom part (it starts with article footer)
    if num == "12":
        content = content.split('<div class="ft">')[0]
    fname, page = make_section(num, title, content)
    path = os.path.join("C:\\Projects\\FREE_EVER\\research\\axis_of_transition\\sections", fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  {fname}")

print(f"\nTotal: {len(sections)} sections")
