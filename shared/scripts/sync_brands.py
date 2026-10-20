"""Rebuild brands.json from the payment-brand-wireframes repo.

Usage: python3 shared/scripts/sync_brands.py <path to payment-brand-wireframes checkout>
       then python3 scripts/bundle.py to copy the new brands.json into every skill.

Reads data/pages.json (name, mark, domain, accent, tagline) and
data/brand-book.json (licence, status, type), then derives accent_ink: the
accent darkened until it reads on the light page (#f7f7f7) at 4.5:1 or better,
and accent_ink_dark: the accent lightened until it reads on the dark page (#0f0f10).
"""
import colorsys, json, sys
from pathlib import Path

PAGE = (0xf7, 0xf7, 0xf7)
PAGE_DARK = (0x0f, 0x0f, 0x10)

# Display casing that differs from the wireframe repo. Applied to names and to free text.
NAME_OVERRIDES = {'Zepapay': 'ZepaPay'}

def fix(s):
    if isinstance(s, str):
        for old, new in NAME_OVERRIDES.items():
            s = s.replace(old, new)
    return s

def lum(rgb):
    def c(v):
        v /= 255
        return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = (c(v) for v in rgb)
    return .2126 * r + .7152 * g + .0722 * b

def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + .05) / (lb + .05)

def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def ink(accent, page=PAGE):
    """Darken (light page) or lighten (dark page) the accent until it reads at 4.5:1."""
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in hex2rgb(accent)))
    step = -.01 if page == PAGE else .01
    while 0 <= l <= 1:
        rgb = tuple(round(v * 255) for v in colorsys.hls_to_rgb(h, l, s))
        if contrast(rgb, page) >= 4.5:
            return '#%02x%02x%02x' % rgb
        l += step
    return '#111111' if page == PAGE else '#f5f5f5'

def main(repo):
    repo = Path(repo)
    pages = json.loads((repo / 'data/pages.json').read_text())['pages']
    book = {b['brand']: b for b in json.loads((repo / 'data/brand-book.json').read_text())['brands']}
    out = []
    for p in pages:
        b = book.get(p.get('book_key', p['name']), {})
        out.append({
            'slug': p['slug'], 'name': fix(p['name']), 'mark': p['mark'], 'domain': p['domain'],
            'accent': p['accent'], 'accent_fg': p['accent_fg'], 'accent_ink': ink(p['accent']), 'accent_ink_dark': ink(p['accent'], PAGE_DARK),
            'tagline': fix(p.get('tagline', '')),
            'licence': b.get('licence') or 'None', 'status': b.get('status'), 'type': b.get('type'),
            'sells': fix(b.get('sells')),
        })
    dest = Path(__file__).resolve().parent.parent / 'brands.json'
    dest.write_text(json.dumps({'_source': 'knivef/payment-brand-wireframes data/pages.json + data/brand-book.json',
                                'brands': out}, indent=2, ensure_ascii=False) + '\n')
    print(f'{len(out)} brands -> {dest}')

if __name__ == '__main__':
    main(sys.argv[1])
