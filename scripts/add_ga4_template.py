from pathlib import Path
import re

root = Path('/home/ubuntu/hoiku-note')
script = '<script>window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};window.gtag("js",new Date());(function(){var id="G-REPLACE_WITH_YOUR_MEASUREMENT_ID";if(!id.includes("REPLACE")){var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+id;document.head.appendChild(s);window.gtag("config",id);}})();</script>'
paths = [root / 'client/index.html', *sorted((root / 'client/public/articles').glob('*/index.html'))]
for path in paths:
    text = path.read_text()
    text = re.sub(r'<script>window\.dataLayer=.*?</script>', '', text, count=1, flags=re.S)
    if '<meta charset="utf-8">' in text:
        text = text.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + script, 1)
    else:
        text = text.replace('<meta charset="UTF-8" />', '<meta charset="UTF-8" />' + script, 1)
    path.write_text(text)
print(f'GA4 template added to {len(paths)} pages')
