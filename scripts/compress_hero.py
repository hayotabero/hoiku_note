from pathlib import Path
from PIL import Image

source = Path('/home/ubuntu/webdev-static-assets/hoiku-note-hero.png')
out = Path('/home/ubuntu/webdev-static-assets/hoiku-note-hero-compressed.jpg')
image = Image.open(source).convert('RGB')
image.thumbnail((1400, 1050), Image.Resampling.LANCZOS)
image.save(out, 'JPEG', quality=78, optimize=True, progressive=True)
print(f'{source.stat().st_size} -> {out.stat().st_size} bytes, {image.size}')
