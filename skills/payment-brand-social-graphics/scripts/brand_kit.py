"""Write a brand's tokens and fallback wordmarks into a working folder.

Usage: python3 brand_kit.py <slug or name> [out_dir]

Writes:
  tokens.css          light and dark custom properties for every template
  wordmark_black.svg  mark tile (accent) + name in ink, for the light page
  wordmark_white.svg  same, name in white, for dark panels
  mark.svg            the mark tile alone (avatars, favicons, tight corners)
Use these only when the user has no real logo file for the brand.
"""
import json, sys
from html import escape
from pathlib import Path

BRANDS = Path(__file__).resolve().parent.parent / 'brands.json'

def find(key):
    key = key.lower().replace(' ', '-')
    for b in json.loads(BRANDS.read_text())['brands']:
        if key in (b['slug'], b['name'].lower().replace(' ', '-'), b['mark'].lower()):
            return b
    sys.exit(f'No brand "{key}" in {BRANDS}. Add it there first.')

def tile(b, x=0):
    return (f'<rect x="{x}" y="0" width="56" height="56" rx="12" fill="{b["accent"]}"/>'
            f'<text x="{x + 28}" y="36.5" text-anchor="middle" font-family="Inter, Helvetica, Arial, sans-serif" '
            f'font-size="{22 if len(b["mark"]) <= 2 else 17}" font-weight="700" letter-spacing="-0.02em" '
            f'fill="{b["accent_fg"]}">{escape(b["mark"])}</text>')

def wordmark(b, ink):
    w = 72 + int(len(b["name"]) * 18.5)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 56" height="56">{tile(b)}'
            f'<text x="70" y="38" font-family="Inter, Helvetica, Arial, sans-serif" font-size="32" '
            f'font-weight="650" letter-spacing="-0.03em" fill="{ink}">{escape(b["name"])}</text></svg>\n')

def main(key, out='.'):
    b, out = find(key), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'tokens.css').write_text(
        '/* Light is the default. Put data-theme="dark" on <html> for dark mode. */\n'
        ':root{\n  --page:#f7f7f7; --ink:#111; --muted:#6b6b6b; --line:#e4e4e4; --card:#fff; --card-border:#e3e3e3;\n'
        '  --card-alt:#eef0f4; --card-alt-ink:#111; --chrome:linear-gradient(#f1f1f1,#e6e6e6); --chrome-ink:#555;\n'
        f'  --accent:{b["accent"]}; --accent-fg:{b["accent_fg"]}; --accent-ink:{b["accent_ink"]};\n'
        '  --dot-2:#111; --dot-3:#9a9a9a;\n}\n'
        '[data-theme="dark"]{\n  --page:#0f0f10; --ink:#f5f5f5; --muted:#9a9a9e; --line:#26262a; --card:#1c1c1f; --card-border:#2a2a2e;\n'
        '  --card-alt:#f2f2f2; --card-alt-ink:#111; --chrome:linear-gradient(#2c2c30,#232327); --chrome-ink:#b5b5b9;\n'
        f'  --accent-ink:{b["accent_ink_dark"]};\n'
        '  --dot-2:#f5f5f5; --dot-3:#6b6b70;\n}\n')
    (out / 'wordmark_black.svg').write_text(wordmark(b, '#111111'))
    (out / 'wordmark_white.svg').write_text(wordmark(b, '#ffffff'))
    (out / 'mark.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" height="56">{tile(b)}</svg>\n')
    print(json.dumps(b, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main(*sys.argv[1:3])
