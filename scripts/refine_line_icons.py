from pathlib import Path
root=Path('/home/ubuntu/hoiku-note/client/public/articles')
icon='<span class="line-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 11.5c0 4.1-3.6 7.5-8 7.5-1.1 0-2.1-.2-3-.5L4 20l1.1-3.2A7 7 0 0 1 4 11.5C4 7.4 7.6 4 12 4s8 3.4 8 7.5Z"/><path d="M8 12h.01M12 12h.01M16 12h.01"/></svg></span>'
for path in root.glob('*/index.html'):
    s=path.read_text().replace('<span class="line-icon">吹</span>', icon).replace('<div class="modal-icon">吹</div>', '<div class="modal-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 11.5c0 4.1-3.6 7.5-8 7.5-1.1 0-2.1-.2-3-.5L4 20l1.1-3.2A7 7 0 0 1 4 11.5C4 7.4 7.6 4 12 4s8 3.4 8 7.5Z"/><path d="M8 12h.01M12 12h.01M16 12h.01"/></svg></div>')
    path.write_text(s)
print('refined icons on', len(list(root.glob('*/index.html'))), 'articles')
