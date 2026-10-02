from pathlib import Path

root = Path('/home/ubuntu/hoiku-note')
base = 'https://hoikunote-rhueltws.manus.space'
article_root = root / 'client/public/articles'
slugs = sorted(p.name for p in article_root.iterdir() if p.is_dir())

# Use explicit static document URLs. This is reliable on the managed static host
# without changing server-side routing.
for path in sorted(article_root.glob('*/index.html')):
    text = path.read_text()
    for slug in slugs:
        text = text.replace(f'/articles/{slug}/"', f'/articles/{slug}/index.html"')
        text = text.replace(f'/articles/{slug}/)', f'/articles/{slug}/index.html)')
    text = text.replace(f'{base}/articles/{path.parent.name}/"', f'{base}/articles/{path.parent.name}/index.html"')
    path.write_text(text)

sitemap = root / 'client/public/sitemap.xml'
text = sitemap.read_text()
for slug in slugs:
    text = text.replace(f'{base}/articles/{slug}/', f'{base}/articles/{slug}/index.html')
sitemap.write_text(text)

home = root / 'client/src/pages/Home.tsx'
text = home.read_text().replace('href={`/articles/${topic.slug}/`}', 'href={`/articles/${topic.slug}/index.html`}')
home.write_text(text)
print('article endpoints:', len(slugs))
