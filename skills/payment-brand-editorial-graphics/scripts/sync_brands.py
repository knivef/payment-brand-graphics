"""Rebuild brands.json from the payment-brand-wireframes repo.

Usage: python3 sync_brands.py <path to payment-brand-wireframes checkout>

Reads data/pages.json (name, mark, domain, accent, tagline) and
data/brand-book.json (licence, status, type), then derives accent_ink: the
accent darkened until it reads on the light page (#f7f7f7) at 4.5:1 or better.
"""
import colorsys, json, sys
from pathlib import Path

PAGE = (0xf7, 0xf7, 0xf7)

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

def ink(accent):
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in hex2rgb(accent)))
    while l > 0:
        rgb = tuple(round(v * 255) for v in colorsys.hls_to_rgb(h, l, s))
        if contrast(rgb, PAGE) >= 4.5:
            return '#%02x%02x%02x' % rgb
        l -= .01
    return '#111111'

def main(repo):
    repo = Path(repo)
    pages = json.loads((repo / 'data/pages.json').read_text())['pages']
    book = {b['brand']: b for b in json.loads((repo / 'data/brand-book.json').read_text())['brands']}
    out = []
    for p in pages:
        b = book.get(p.get('book_key', p['name']), {})
        out.append({
            'slug': p['slug'], 'name': p['name'], 'mark': p['mark'], 'domain': p['domain'],
            'accent': p['accent'], 'accent_fg': p['accent_fg'], 'accent_ink': ink(p['accent']),
            'tagline': p.get('tagline', ''),
            'licence': b.get('licence') or 'None', 'status': b.get('status'), 'type': b.get('type'),
            'sells': b.get('sells'),
        })
    dest = Path(__file__).resolve().parent.parent / 'brands.json'
    dest.write_text(json.dumps({'_source': 'knivef/payment-brand-wireframes data/pages.json + data/brand-book.json',
                                'brands': out}, indent=2, ensure_ascii=False) + '\n')
    print(f'{len(out)} brands -> {dest}')

if __name__ == '__main__':
    main(sys.argv[1])
