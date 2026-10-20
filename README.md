# payment-brand-graphics

Claude skills for the payment brands' marketing graphics. Private.

## Skills

| Skill | Use it for | Asks first |
|---|---|---|
| [`payment-brand-social-graphics`](skills/payment-brand-social-graphics/SKILL.md) | LinkedIn and X posts, albums, PDF carousels, X banners: stat cards and a screenshot in a macOS window over a painting, sky, anime sky or abstract shapes. | Format, mode, design direction, background (then overlay if needed) |
| [`payment-brand-collateral`](skills/payment-brand-collateral/SKILL.md) | Sales documents: A4 one-pager, 9:16 rate card, 16:9 terms deck. PNG per page plus PDF. | Output, mode, design direction, background (then overlay if needed) |

Both cover ZepaPay (default), Secure Payment Services, Sepa Mint, Offrampr, Ape Card, Pure Labs, AltPay, Swipe Wire Pay, Card Payz, Fiat Pay and Onrampr, in light or dark mode. Only ZepaPay and Secure Payment Services hold a licence (UAE PSP); both skills block licence wording for every other brand.

The social skill is a brand-aware clone of `light-editorial-graphics` in [knivef/creatives](https://github.com/knivef/creatives). The collateral skill takes its layout cues from reference sales collateral (bento one-pager, rate card, terms deck).

## Layout

```
shared/                       source of truth for everything both skills use
  brands.json                 one record per brand: name, mark, domain, accent, accent_ink(_dark), licence, status, type
  reference/brand-rules.md    brand data, licence and claims rules, copy rules, logo variants
  reference/backgrounds.md    background options, sourcing, halftone and text-texture filters, dark-mode filter
  scripts/brand_kit.py        writes light/dark tokens.css + wordmark SVGs for one brand
  scripts/render.py           renders any template to PNG per page + PDF, light or dark, warns on overflow
  scripts/sync_brands.py      rebuilds brands.json from knivef/payment-brand-wireframes (maintenance only)
skills/payment-brand-social-graphics/
  SKILL.md, templates/slide_square.html, + bundled copies of shared files
skills/payment-brand-collateral/
  SKILL.md, templates/{collateral.css, onepager.html, ratecard.html, deck.html}, + bundled copies
scripts/bundle.py             copies shared/ into each skill; --check fails if a copy is stale
```

Each skill folder is self-contained, so either can be installed or uploaded on its own.

## Editing

Edit shared files in `shared/`, never the copies under `skills/`, then:

```bash
python3 scripts/bundle.py
```

```bash
python3 scripts/bundle.py --check
```

When a brand is added or changes accent in the wireframe repo:

```bash
python3 shared/scripts/sync_brands.py "/path/to/payment-brand-wireframes"
```

Then run `python3 scripts/bundle.py` again.

## Installing

Copy or symlink each folder under `skills/` into `~/.claude/skills/`, or zip a skill folder and upload it as a skill in claude.ai.
