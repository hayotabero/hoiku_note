from pathlib import Path
root=Path('/home/ubuntu/hoiku-note/client/public/articles')
for path in root.glob('*/index.html'):
    s=path.read_text()
    if '[hidden]{display:none!important}' not in s:
        s=s.replace('</style>', '[hidden]{display:none!important}</style>', 1)
    path.write_text(s)
print('fixed modal initial visibility on', len(list(root.glob('*/index.html'))), 'articles')
