# Brand rules (shared by every payment brand skill)

Source of truth: `shared/reference/brand-rules.md` in knivef/payment-brand-graphics. Each skill carries a copy made by `scripts/bundle.py`; edit the shared file, never the copy.

## Pick the brand

Brand data lives in `brands.json` next to this file (synced from the private `knivef/payment-brand-wireframes` repo with `scripts/sync_brands.py`). For the chosen brand, run:

```bash
python3 <skill dir>/scripts/brand_kit.py zepapay ./kit
```

It prints the brand record and writes `tokens.css` (light set on `:root`, dark set under `[data-theme="dark"]`), `wordmark_black.svg`, `wordmark_white.svg` and `mark.svg` into `./kit`. Fields that matter here:

| Field | Use |
|---|---|
| `name` | Exact display casing, used on every slide. ZepaPay is always "ZepaPay" (capital P), even though the brand book and wireframe repo write it with a lowercase p. `scripts/sync_brands.py` keeps this casing on every re-sync. |
| `mark` | 2 to 3 letter monogram for the fallback wordmark and tight spaces. |
| `domain` | Footer, next to the source line (e.g. `zepapay.com`). |
| `accent` | Brand colour as a fill: stat underline bar, first stat dot, wordmark tile, swipe chevron. |
| `accent_fg` | Text placed on an `accent` fill. |
| `accent_ink`, `accent_ink_dark` | Light page: the accent darkened to read on the light page (4.5:1 on `#f7f7f7`). Use it for any accent coloured text or thin lines. Never set text in raw `accent` on the light page: ZepaPay green, Ape Card yellow and Card Payz lime all fail. Dark page: the accent lightened to 4.5:1 on `#0f0f10`. `tokens.css` maps the right one to `--accent-ink`. |
| `licence` | What the brand may claim. See "Licence and claims" below. |
| `status`, `type` | `Idea` brands have no live product: ask before making public graphics for one. `Burnable` and `Permanent` brands must never appear together in one piece of work. |

A brand not in `brands.json` (e.g. NexFlow, or any brand-book idea without a page yet): ask for its name, accent and licence, add it to `brands.json` by hand, and say so.

**One brand per piece.** Never show two brands side by side, never mention a sister brand, and never reuse one brand's screenshot (dashboard, settlement log, invoice) for another.

## Licence and claims (binding)

- Only **ZepaPay** and **Secure Payment Services** hold a licence: a UAE payment service provider (PSP) licence. Their slides may say "Licensed UAE payment service provider". NexFlow holds a Canadian MSB licence.
- **Every other brand holds no licence.** Its slides must never state or imply one: no "licensed", "regulated", "authorised", "compliant", "bank-grade", regulator names or licence numbers. A partner structure can be described only with words the user supplies.
- Numbers (fees, limits, volumes, settlement times, corridors) come only from the user, their screenshots, or the brand's live page copy, and the user confirms them before export. The internal brand book price lists are not public: never put a rate card or margin on a graphic unless the user says that rate is public.
- Rate cards and terms decks are sent privately to prospects, not posted. They may use a brand book price list only when the user names the list and confirms the numbers. Label them "Indicative" with a footnote that the written agreement is binding, and never reuse them as a public social post.
- Contact slides: names, emails, photos and QR codes only from the user. Never invent a person or copy one from a reference document.
- Anything still in `[BRACKETS]` or `[CONFIRM: ...]` in the brand's page copy is unverified and never goes on a slide.
- Never name banks, acquirers, partners or clients unless the user says they are public.
- If the request conflicts with any of this, stop and ask instead of softening the wording.

## Copy rules

No em dashes and no `--` as punctuation anywhere (rewrite the sentence instead), direct human phrasing, brand names in the exact casing from `brands.json`, plain payment language a merchant would use ("paid to your bank account", not "fiat egress"), and the licence rules above.

## Logo variants

No logo file: use the kit wordmarks (`wordmark_black.svg` in light mode, `wordmark_white.svg` in dark mode, `mark.svg` where space is tight) and tell the user it is a placeholder.

If the logo is a transparent PNG, recolor from its alpha channel (check `im.mode`; if RGBA with a transparent background, use the alpha, not the RGB):

```python
import numpy as np
a = np.array(Image.open(logo))[...,3].astype(float)/255
ys, xs = np.where(a>.1); a = a[ys.min():ys.max()+1, xs.min():xs.max()+1]
for name, col in [('black',(17,17,17)),('white',(255,255,255))]:
    out = np.zeros(a.shape+(4,), np.uint8); out[...,:3] = col; out[...,3] = (a*255).astype(np.uint8)
    Image.fromarray(out).save(f'logo_{name}.png')
```
If the logo sits on a white background instead, derive alpha from `(255 - blue)/235` clipped to 0..1.
