"""Copy shared/ into every skill so each skill folder works on its own.

Usage: python3 scripts/bundle.py          copy shared files into each skill
       python3 scripts/bundle.py --check  exit 1 if any skill copy differs from shared/

Edit files in shared/, never the copies inside skills/. Run this before every commit.
"""
import filecmp, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / 'shared'
FILES = ['brands.json', 'reference/brand-rules.md', 'reference/backgrounds.md',
         'scripts/brand_kit.py', 'scripts/render.py']   # sync_brands.py stays in shared/ (maintenance only)
SKILLS = sorted(p.parent for p in (ROOT / 'skills').glob('*/SKILL.md'))

def main(check):
    stale = []
    for skill in SKILLS:
        for f in FILES:
            src, dst = SHARED / f, skill / f
            if dst.exists() and filecmp.cmp(src, dst, shallow=False):
                continue
            if check:
                stale.append(str(dst.relative_to(ROOT)))
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print('copied', dst.relative_to(ROOT))
    if check and stale:
        sys.exit('Out of date, run python3 scripts/bundle.py:\n  ' + '\n  '.join(stale))
    print(f'{len(SKILLS)} skills in sync with shared/')

if __name__ == '__main__':
    main('--check' in sys.argv)
