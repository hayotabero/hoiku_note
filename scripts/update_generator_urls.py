from pathlib import Path
p=Path('/home/ubuntu/hoiku-note/scripts/generate_seo_pages.py')
s=p.read_text()
s=s.replace("url = f'{BASE}/articles/{a[\"slug\"]}/'", "url = f'{BASE}/articles/{a[\"slug\"]}/index.html'")
s=s.replace("{BASE}/articles/{x[\"slug\"]}/", "{BASE}/articles/{x[\"slug\"]}/index.html")
s=s.replace("{BASE}/articles/{a[\"slug\"]}/</loc>", "{BASE}/articles/{a[\"slug\"]}/index.html</loc>")
p.write_text(s)
print('generator URL format updated')
