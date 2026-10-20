# payment-brand-graphics

Claude skills for social graphics for the payment brands. Private.

## Skills

| Skill | What it makes |
|---|---|
| [`payment-brand-editorial-graphics`](skills/payment-brand-editorial-graphics/SKILL.md) | Editorial slides (stat card, screenshot in a macOS window over a painting, sky, anime sky or abstract shapes) and sales collateral (A4 one-pager, 9:16 rate card, 16:9 terms deck), in light or dark mode, per brand. It asks for output, mode, design direction and background before generating. |

It is a brand-aware clone of `light-editorial-graphics` in [knivef/creatives](https://github.com/knivef/creatives). Same look and steps, plus brand colours, placeholder wordmarks, and licence and claims rules for each brand.

## Layout

```
skills/payment-brand-editorial-graphics/
  SKILL.md                  the skill
  brands.json               one record per brand: name, mark, domain, accent, accent_ink, licence, status, type
  scripts/brand_kit.py      writes light/dark tokens.css + wordmark SVGs for one brand
  scripts/sync_brands.py    rebuilds brands.json from knivef/payment-brand-wireframes
  scripts/render.py         renders any template to PNG per page + PDF, light or dark, warns on overflow
  templates/slide_square.html  1080x1080 starter slide
  templates/onepager.html   A4 one-pager (bento sections + CTA band)
  templates/ratecard.html   9:16 rate card (fee cards + table)
  templates/deck.html       16:9 deck (cover, terms table, contact)
  templates/collateral.css  shared collateral styles: light/dark, "skill" or "collateral" design cues
```

## Brands

ZepaPay (default), Secure Payment Services, Sepa Mint, Offrampr, Ape Card, Pure Labs, AltPay, Swipe Wire Pay, Card Payz, Fiat Pay, Onrampr. Only ZepaPay and Secure Payment Services hold a licence (UAE PSP); the skill blocks licence wording for every other brand.

## Updating brands

`brands.json` is generated. When a brand is added or changes accent in the wireframe repo:

```bash
python3 skills/payment-brand-editorial-graphics/scripts/sync_brands.py "/path/to/payment-brand-wireframes"
```

## Installing the skill

Copy or symlink `skills/payment-brand-editorial-graphics` into `~/.claude/skills/`, or zip the folder and upload it as a skill in claude.ai.
