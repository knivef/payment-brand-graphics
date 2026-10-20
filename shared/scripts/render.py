"""Render a template (slide or collateral) to PNGs and a PDF.

Usage: python3 render.py <file.html> [out_dir] [--theme light|dark] [--cues skill|collateral] [--scale 2]

Finds every <section class="sheet ..." id="pN"> (or treats the file as one 1080x1080
slide), screenshots each sheet at its own size, and prints all sheets to one PDF.
--theme / --cues override the attributes on <html> for this render only, so one
source file gives the light and dark versions. Uses Playwright when it is
installed, otherwise headless Google Chrome.
"""
import argparse, re, shutil, subprocess, sys, tempfile
from pathlib import Path

SIZES = {'a4': (1240, 1754), 'story': (1080, 1920), 'wide': (1920, 1080)}
CHROME = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
          shutil.which('google-chrome') or '', shutil.which('chromium') or '']

# Marks any sheet whose content runs past its fixed size, so render.py can warn.
CHECK = ('<script>addEventListener("load",function(){document.querySelectorAll(".sheet,.page").forEach(function(s){'
         'var r=s.getBoundingClientRect(),b=r.bottom;s.querySelectorAll("*").forEach(function(e){b=Math.max(b,e.getBoundingClientRect().bottom)});'
         'if(s.scrollHeight>s.clientHeight+1||b>r.bottom+1)document.body.setAttribute("data-overflow",(document.body.getAttribute("data-overflow")||"")+" "+(s.id||"slide"))})})</script>')

def warn(dom):
    m = re.search(r'data-overflow="([^"]+)"', dom)
    if m: print(f'WARNING: content overflows sheet(s):{m.group(1)}. Shorten copy or tighten spacing.')

def sheets(html):
    found = re.findall(r'<section class="sheet (\w+)[^"]*" id="(p\d+)"', html)
    return [(pid, SIZES[k]) for k, pid in found] or [('', (1080, 1080))]

def variant(src, theme, cues):
    html = src.read_text()
    if theme: html = re.sub(r'data-theme="\w+"', f'data-theme="{theme}"', html, 1)
    if cues: html = re.sub(r'data-cues="\w+"', f'data-cues="{cues}"', html, 1)
    if (theme and 'data-theme=' not in html) or (cues and 'data-cues=' not in html):
        html = html.replace('<html', f'<html data-theme="{theme or "light"}" data-cues="{cues or "skill"}"', 1)
    html = html.replace('</body>', CHECK + '</body>', 1)
    tmp = src.with_name(f'.render_{src.stem}.html')   # same folder so kit/ and images resolve
    tmp.write_text(html)
    return tmp, html

def chrome_bin():
    for c in CHROME:
        if c and Path(c).exists(): return c
    sys.exit('No Playwright and no Chrome found. Install one: npm i playwright (never playwright install).')

def main():
    a = argparse.ArgumentParser()
    a.add_argument('html'); a.add_argument('out', nargs='?', default='out')
    a.add_argument('--theme'); a.add_argument('--cues'); a.add_argument('--scale', type=float, default=2)
    o = a.parse_args()
    src = Path(o.html).resolve(); out = Path(o.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    tmp, html = variant(src, o.theme, o.cues)
    tag = '_'.join(x for x in [src.stem, o.theme, o.cues] if x)
    try:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                b = p.chromium.launch()
                for pid, (w, h) in sheets(html):
                    pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=o.scale)
                    pg.goto(tmp.as_uri() + (f'#{pid}' if pid else '')); pg.wait_for_timeout(800)
                    pg.screenshot(path=str(out / f'{tag}_{pid or "slide"}.png'))
                pg = b.new_page(); pg.goto(tmp.as_uri()); pg.wait_for_timeout(800); warn(pg.content())
                pg.pdf(path=str(out / f'{tag}.pdf'), prefer_css_page_size=True, print_background=True)
                b.close()
        except ImportError:
            c = chrome_bin()
            base = [c, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=3000']
            with tempfile.TemporaryDirectory() as prof:
                base.append(f'--user-data-dir={prof}')
                for pid, (w, h) in sheets(html):
                    subprocess.run(base + [f'--force-device-scale-factor={o.scale}', f'--window-size={w},{h}',
                                           '--screenshot=' + str(out / f'{tag}_{pid or "slide"}.png'),
                                           tmp.as_uri() + (f'#{pid}' if pid else '')], capture_output=True)
                warn(subprocess.run(base + ['--window-size=2000,2000', '--dump-dom', tmp.as_uri()],
                                    capture_output=True, text=True).stdout)
                subprocess.run(base + ['--no-pdf-header-footer', f'--print-to-pdf={out / (tag + ".pdf")}', tmp.as_uri()],
                               capture_output=True)
    finally:
        tmp.unlink(missing_ok=True)
    for f in sorted(out.glob(f'{tag}*')): print(f)

if __name__ == '__main__':
    main()
