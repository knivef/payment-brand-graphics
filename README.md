# payment-brand-graphics

Claude skills for social graphics for the payment brands. Private.

## Skills

| Skill | What it makes |
|---|---|
| [`payment-brand-editorial-graphics`](skills/payment-brand-editorial-graphics/SKILL.md) | Light editorial slides (stat card, screenshot in a macOS window over a painting, sky or anime sky with a pastel halftone or text texture) for LinkedIn, X and PDF carousels, per brand. |

It is a brand-aware clone of `light-editorial-graphics` in [knivef/creatives](https://github.com/knivef/creatives). Same look and steps, plus brand colours, placeholder wordmarks, and licence and claims rules for each brand.

## Layout

```
skills/payment-brand-editorial-graphics/
  SKILL.md                  the skill
  brands.json               one record per brand: name, mark, domain, accent, accent_ink, licence, status, type
  scripts/brand_kit.py      writes tokens.css + wordmark SVGs for one brand
  scripts/sync_brands.py    rebuilds brands.json from knivef/payment-brand-wireframes
  templates/slide_square.html  1080x1080 starter slide
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
