---
name: "payment-brand-editorial-graphics"
description: "Create light editorial social graphics for Zepapay (ZepaPay) and the other payment brands (Secure Payment Services, AltPay, Sepa Mint, Offrampr, Onrampr, Ape Card, Pure Labs, Swipe Wire Pay, Card Payz, Fiat Pay): stats, screenshots in a Mac window over a public domain painting, cloudy sky or anime-style sky with pastel halftone filter, in each brand's accent colour and with its licence rules, for LinkedIn, X and carousels."
---

# Payment brand editorial graphics

A brand-aware clone of `light-editorial-graphics` (knivef/creatives). Same look, same steps, but every slide is made for one payment brand: its accent colour, its wordmark, its domain, and its licence and claims rules. Zepapay is the default brand when the request only says "payments" or names no brand.

Use this to make kvn's "light editorial" style images for a payment brand: off-white page with thin grid lines, a dark headline, white stat cards, and a background panel (a public domain painting, a cloud and sky photo, or an anime-style sky, all with a pastel halftone filter) holding a macOS-style window that shows a screenshot or chart. Built as HTML, rendered to PNG/JPG with Playwright.

## Step 0: Pick the brand

Brand data lives in `brands.json` next to this file (synced from the private `knivef/payment-brand-wireframes` repo with `scripts/sync_brands.py`). For the chosen brand, run:

```bash
python3 <skill dir>/scripts/brand_kit.py zepapay ./kit
```

It prints the brand record and writes `tokens.css`, `wordmark_black.svg`, `wordmark_white.svg` and `mark.svg` into `./kit`. Fields that matter here:

| Field | Use |
|---|---|
| `name` | Exact display casing. The brand book writes "Zepapay"; if the user writes "ZepaPay", ask once which one ships and use it on every slide. |
| `mark` | 2 to 3 letter monogram for the fallback wordmark and tight spaces. |
| `domain` | Footer, next to the source line (e.g. `zepapay.com`). |
| `accent` | Brand colour as a fill: stat underline bar, first stat dot, wordmark tile, swipe chevron. |
| `accent_fg` | Text placed on an `accent` fill. |
| `accent_ink` | The accent darkened to read on the light page (4.5:1 on `#f7f7f7`). Use it for any accent coloured text or thin lines. Never set text in raw `accent` on the light page: Zepapay green, Ape Card yellow and Card Payz lime all fail. |
| `licence` | What the brand may claim. See "Licence and claims" below. |
| `status`, `type` | `Idea` brands have no live product: ask before making public graphics for one. `Burnable` and `Permanent` brands must never appear together on one slide or carousel. |

A brand not in `brands.json` (e.g. NexFlow, or any brand-book idea without a page yet): ask for its name, accent and licence, add it to `brands.json` by hand, and say so.

**One brand per carousel.** Never show two brands side by side, never mention a sister brand, and never reuse one brand's screenshot (dashboard, settlement log, invoice) for another.

## Licence and claims (binding)

- Only **Zepapay** and **Secure Payment Services** hold a licence: a UAE payment service provider (PSP) licence. Their slides may say "Licensed UAE payment service provider". NexFlow holds a Canadian MSB licence.
- **Every other brand holds no licence.** Its slides must never state or imply one: no "licensed", "regulated", "authorised", "compliant", "bank-grade", regulator names or licence numbers. A partner structure can be described only with words the user supplies.
- Numbers (fees, limits, volumes, settlement times, corridors) come only from the user, their screenshots, or the brand's live page copy, and the user confirms them before export. The internal brand book price lists are not public: never put a rate card or margin on a graphic unless the user says that rate is public.
- Anything still in `[BRACKETS]` or `[CONFIRM: ...]` in the brand's page copy is unverified and never goes on a slide.
- Never name banks, acquirers, partners or clients unless the user says they are public.
- If the request conflicts with any of this, stop and ask instead of softening the wording.

## Before starting

Confirm (or infer from context and state the assumption):
0. Brand (from `brands.json`, see Step 0). Default: Zepapay.
1. Format: 1080x1080 square (single-image posts), 1080x1350 portrait (default for LinkedIn multi-image albums, see "Feed cropping" below), or 1500x600 (X Article banner, 5:2).
2. Background style. When the user asks which background to use, or hasn't said, offer these options with a one-line pitch each and a recommendation for the post:
   - **Painting:** public domain landscape (Monet, Cezanne, Renoir). Classic, gallery feel, works for "the story" and founder posts.
   - **Clouds and sky:** a real sky photo. Calm, airy, neutral; good for product, metrics and launch posts where the screenshot should dominate.
   - **Anime sky:** an anime-style sky or landscape from a free wallpaper site (licensed for commercial use), bright blue with puffy cel-shaded clouds. Playful, eye-catching, good for build-in-public and community posts.
   Mixing styles inside one carousel looks messy: use one style per carousel unless the user asks otherwise.
3. Overlay. Every time you generate, offer the overlay choice alongside the background (one line each, plus a recommendation), even if the user only asked about the background:
   - **Halftone dots** (default): soft print look, quiet, works with every background.
   - **Text texture:** faint letters, digits and symbols like `$ 8 0 X x +` over the whole background, clouds included, with density following the brightness. A data/terminal feel that suits metrics, fintech and build-in-public posts.
   - **None:** clean background with only the pastel colour softening, for when the background itself should be the star (e.g. a striking anime sky).
   For halftone and text texture, also offer intensity: **subtle** (text `strength` 0.12, halftone dot `fill` 35) or **medium** (text 0.17, halftone 50, the defaults). Use the same overlay and intensity across a carousel. If the user wants to compare, render slide 1 with each option side by side and let them pick before doing the rest. See Step 2.
4. How it will be posted: single image, multi-image album, or PDF document carousel. This decides the crop rules.
5. Number of slides and the story each one tells (see "Presenting data" below).
6. Logo file (transparent PNG preferred). Default to the black version on this light style. If the user has no logo file for the brand, use `wordmark_black.svg` from Step 0 and say it is a placeholder wordmark, not the real logo.
7. Source screenshots and raw numbers.

Copy rules: no em dashes and no `--` as punctuation anywhere (rewrite the sentence instead), direct human phrasing, brand names in the exact casing from Step 0, plain payment language a merchant would use ("paid to your bank account", not "fiat egress"), and the licence rules above.

## Feed cropping (design for it, don't fight it)

LinkedIn multi-image albums show each image as a roughly 4:5 tile in a sideways-scrolling row. A 1080x1080 square loses about 108px on the left and right (only the centre 864x1080 shows). The tile also covers the image with LinkedIn's own controls: a "1/4" count badge in the top-right corner and a round "›" next button halfway down the right edge. X crops multi-image posts too (side-by-side tiles for 2 to 4 images). A PDF document carousel is not cropped.

Seen in a real post: the eyebrow "30 days on Reddit" became "days on Reddit", the headline lost its first digit ("3 posts" became "posts"), the "1 / 4" page count and "Swipe for the receipts" were cut, and left-aligned text ran straight into the crop edge, which looked like a mistake.

**Choose the format first**
- Multi-image album: render 1080x1350 (4:5), so the tile shows the whole image. Still keep the safe zone below, because tile shapes change with image count and screen width.
- Uncropped carousel: give the PDF from Step 6 and suggest posting it as a document.
- Square that may be cropped: follow every rule below.

**Two zones**
- Safe zone: the centre 4:5 area, plus a 24px buffer inside it (on a 1080 square that's x 132 to 948). Every word, number, logo, page count and the whole macOS window goes in here.
- Bleed zone: the outer strips (x 0 to 108 and 972 to 1080 on a square). Use them only for things that still look complete when sliced: grid lines, painting, background texture, rules that run off the edge. Never put content there.

**Design tricks so the crop looks intended**
1. Move the frame inward. Put the vertical guide lines and diamonds at the safe edge (x 120 and 960 on a square), not at 48. Cropped, the slide still has a neat frame with air on both sides. Uncropped, the outer strips read as a margin.
2. Bleed the background. Run the painted panel off both side edges (full width, no radius on the sides) while the window stays centred. A crop then just shows less background, never a panel cut off at a strange point. Do the same for the header and footer rules.
3. Fill the outer strips with texture, not emptiness. A faint hatch, dot grid or a continuation of the halftone dots means the full square doesn't look padded and the crop doesn't look missing anything.
4. Use centred or fully bleeding stat cards. Either centre the card inside the safe zone, or bleed its outer two cells' borders to the edge with each label and value well inside. Keep the hero value in the middle or left-middle cell, never against an edge.
5. Clear LinkedIn's overlays. Leave the top-right corner of the safe zone (about 140x80px) free of anything that matters: put the page count top-left or in the footer. Keep the right edge halfway down free of numbers and key screenshot detail, since the "›" button sits there.
6. A swipe cue that survives the crop. Put "Swipe" text inside the safe zone. Or use a deliberate half arrow or chevron that bleeds off the right edge: cropped or not, it reads as "more to the right".
7. Optional panorama. Cut one wide painting or sky into strips (one per slide) so the painted band seems to continue as you swipe. Small gaps from the crop don't matter.

**Check it** (add this to Step 5): for every slide, also save a simulated tile. Crop the centre 4:5, draw a dark rounded "1/4" badge top-right and a 40px dark circle on the right edge halfway down, and view all tiles together. Fix any slide where text touches an edge, a number is cut or hidden, or the layout looks off-centre.

## Presenting data

**Accuracy first**
- Only use numbers the user gave or that are visible in their screenshots. Never invent, round up or "improve" a figure.
- Read every number off the screenshot yourself and cross-check against what the user said. If they disagree, ask.
- Compute totals in code (e.g. views 91K + 2.9K + 70K = 163.9K, shown as 164K) and make sure each total matches the sum of its parts.
- Anything estimated by reading a chart (e.g. "daily traffic around 300, up from 150 to 200") is flagged to the user as an estimate before publishing.
- Keep units and formats consistent across slides: "91K", "2.9K", "8,150", "250+", "0 → 9". Use the same abbreviation style everywhere.

**Hierarchy**
- One hero number per slide. On a per-item slide, lead with the most important metric (e.g. volume settled, or views for a growth post) in the first stat cell with the accent underline.
- Max 3 stats per row, max 2 rows. Group rows with a small uppercase label ("On Reddit", "On the website") when they come from different sources.
- Cover slide = the aggregate story (totals, the headline claim). Following slides = one item each, in chronological order, so the carousel reads as a narrative.
- Each slide's headline names the moment ("Post 1: The launch"), and the sub line says what happened or what was learned, in one sentence.
- The screenshot is the receipt. The stat card repeats its key numbers in large type so the slide reads at thumbnail size.
- Footer source line names where the numbers come from ("Source: Zepapay dashboard, Sept 2026" or "Source: Reddit Post Insights").

**What to leave out**
- Respect what the user wants hidden: post titles, subreddit names, usernames, comment threads, avatars, NSFW tags, private dashboards.
- In payment screenshots, always blur or patch out (Step "Working with screenshots", removing UI) before rendering: IBANs, account and card numbers, full wallet addresses and transaction hashes (keep at most `0x7f3a…c21b` style), client and counterparty names, emails, API keys, internal reference IDs, and any balance the user has not cleared for posting. Check the contact sheet for leftovers.
- Drop secondary metrics that clutter (country splits, share counts) unless the user asks for them.

## Working with screenshots

**Cropping**
- Screenshots are usually retina. Work out the scale first: `scale = actual_width / displayed_width`, pick crop boxes in displayed coordinates, then multiply by the scale.
- Crop whole UI sections along their own card edges (e.g. the "Reach" card from its top edge to the bottom of the chart scrollbar; single rows like "Upvotes" or "Comments" between their divider lines). Never cut through text, numbers or chart axes.
- After cropping, build a contact sheet of every crop and look at it before using them. Re-crop anything with a stray border, half a divider or clipped labels.
- Remove unwanted UI (e.g. a "Promote post" button) by filling its box with a pixel sampled from the card background right next to it, then check the patch is invisible.
- Save each crop as its own PNG too (e.g. `post1_reach.png`, `post1_upvotes.png`) so the user can reuse them.

**Compact rows**
For rows with a label on the left, a value on the right and empty space between, build a compact version: paste the left ~150 display px and right ~80 display px onto a canvas ~336 display px wide filled with the row's background colour. Show two compact rows side by side under the main crop, split by a 1px line.

**Scaling**
- Don't scale a crop so small that its text drops under ~11px on the final image, or so large it looks blurry. If text is too small, crop tighter or give the window more width.
- Keep the screenshot's own colours (dark mode stays dark). It sits inside the light window chrome.
- A white chart (e.g. an analytics line chart) goes in the window on a white pad (`padding:14px 10px 6px`).

## Step 1: Get the background

Use the style picked in "Before starting". Whatever the style, the window covers the middle, so pick images with interest near the edges and top, and make a contact sheet and look at it before choosing.

### Option A: Public domain paintings


Museum sites (artic.edu, metmuseum, wikimedia) may be blocked by the egress proxy. Reliable fallback: the npm package `aquarelle` bundles ~260 famous painting JPGs (~700px wide) with a `data.json` of title/author/year.

```bash
mkdir -p pd && curl -sS https://registry.npmjs.org/aquarelle/-/aquarelle-1.5.2.tgz | tar xz -C pd
# images in pd/package/images, metadata in pd/package/data.json
```

Only use works that are clearly public domain: artist died 95+ years ago AND the work was published before 1931. Safe artists in that package: Monet, Cezanne, Renoir, Seurat, Van Gogh, Gauguin, Manet, Turner, Whistler, Cassatt. Never use Picasso, Miro, Pollock, de Kooning, O'Keeffe, Kandinsky, Chagall or Mondrian.

Prefer landscapes and seascapes with structure across the frame (the window covers the middle). Good picks used before: Cezanne `cezanne-sv.jpg` (Mont Sainte-Victoire), `cezanne-le.jpg` (View from L'Estaque); Monet `monet-w6.jpg` (Water-Lilies: The Clouds); Renoir `renoir-lb.jpg` (Landscape at Beaulieu). Avoid very pale works (e.g. Turner's Norham Castle) since the filter washes them out. Use a different painting per slide. Make a contact sheet first and look at it before choosing.

Always credit the paintings (artist, title, year) in the delivery message or gallery.

### Option B: Clouds and sky

Use, in this order:
1. Sky photos the user supplies.
2. Public domain or free-licence photos: NASA and NOAA images (US government, public domain), Wikimedia Commons files marked CC0 or public domain, Unsplash or Pexels (free for commercial use, no credit needed, but credit the photographer anyway when it's easy). Record the source URL and licence for each image.
3. Painted skies, which are public domain and fit this style well: John Constable's cloud studies (1820s) and Eugene Boudin's beach skies.
If image sites are blocked by the egress proxy, ask the user for photos or fall back to Option C or A.

Pick big cumulus or soft golden-hour skies with blue gaps, not flat grey overcast (it turns to mud under the filter). Avoid planes, birds, sun flares and horizons with buildings right where the window sits. A low horizon line at the bottom of the panel looks good below the window.

### Option C: Anime sky

Source anime scenes from free wallpaper and stock sites, but only ones whose licence allows commercial use. These posts promote a brand, so "free to download" is not enough.

**Use (in this order):**
1. **Pixabay** (search "anime sky", "anime landscape", "anime clouds", "lofi sky"): Pixabay Content License, free for commercial use, no credit needed. Many are AI-generated or illustrated anime-style scenes.
2. **Freepik** free tier (same searches): commercial use allowed with attribution. Add the credit line it asks for to the delivery message.
3. **Unsplash and Pexels:** a few anime-style illustrations and lots of anime-feel skies.

For every image, open its page and confirm the licence says commercial use is allowed, then record the page URL and licence name. Skip any image that shows a recognisable character, a studio logo or a frame from a real show or film, even on these sites, because the uploader can't licence what they don't own.

**Don't use:** Wallhaven, WallpaperFlare, Wallpaper Abyss (Alpha Coders), WallpaperCave, Zedge, HDWallpapers-style sites, Pinterest or Google Images. They rehost screenshots from studios (Ghibli, Makoto Shinkai, etc.) and fan art with no licence, and using those in brand posts is a real infringement risk. The same goes for frames the user grabs from a show or film: flag the risk and suggest a licensed image or the generator below instead.

**Pick:** wide skies with big cumulus, sunsets, rooftops, fields or train-line horizons. Detail near the edges and top, calm space in the middle where the window goes. Avoid people or characters in the centre (the window would cover them anyway) and baked-in text or watermarks. Prefer 1920px wide or bigger.

**Fallback:** if wallpaper sites are blocked by the egress proxy, or nothing licensed fits, generate an original anime-style sky in code (below). It's always safe, and each seed makes a new layout. Anime-style art the user supplies and confirms they have rights to (commissioned, licensed or their own) is fine too.

Original cel-shaded sky generator (saturated blue gradient, puffy cumulus with flat bottoms, one flat shadow tone and a pale outline). Change `seed` and the cloud list `(centre x, base y, width)` for a different layout per slide, and keep the biggest clouds near the edges and top so they show around the window:

```python
import random, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops
def cloud_mask(W, H, cx, base, w, rng):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    for _ in range(int(w / 18)):                                       # puffs along a dome, bigger in the middle
        t = rng.uniform(-1, 1); r = w * rng.uniform(.10, .2) * (1.25 - abs(t) * .7)
        x = cx + t * w / 2; y = base - r * .55 - (1 - t * t) * w * .16 * rng.uniform(.6, 1.2)
        d.ellipse([x - r, y - r, x + r, y + r], fill=255)
    d.rectangle([0, base, W, H], fill=0)                                 # flat cloud bottom
    return m
def anime_sky(out, W=2200, H=1400, seed=3):
    rng = random.Random(seed)
    y = np.linspace(0, 1, H)[:, None, None]
    sky = np.array([38, 112, 210]) * (1 - y) + np.array([176, 218, 242]) * y + np.zeros((1, W, 3))
    img = Image.fromarray(sky.astype(np.uint8))
    for cx, base, w in [(380, 980, 620), (1150, 1240, 900), (1880, 760, 520), (900, 520, 300), (1600, 330, 220)]:
        m = cloud_mask(W, H, cx, base, w, rng)
        s = int(w * .07)
        lit = ImageChops.multiply(m, ImageChops.offset(m, 0, -s))       # lit if the pixel below is cloud too
        shadow = ImageChops.subtract(m, lit)
        rim = ImageChops.subtract(m, m.filter(ImageFilter.MinFilter(9)))
        img.paste((170, 190, 228), mask=m)                               # one flat shadow tone underneath
        img.paste((246, 249, 255), mask=lit)                             # white sunlit body
        img.paste((214, 228, 248), mask=ImageChops.multiply(rim, lit))   # thin pale outline
        img.paste((150, 172, 218), mask=ImageChops.multiply(rim, shadow))
    img.filter(ImageFilter.GaussianBlur(1)).save(out, quality=92)
anime_sky('anime_sky.jpg')
```

## Step 2: Texture filter

### Halftone dots (default)

```python
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
def pastelize(src, out, W=2200):
    im = Image.open(src).convert('RGB')
    im = im.resize((W, int(im.height*W/im.width)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.6))
    im = ImageEnhance.Color(im).enhance(.6)
    im = ImageEnhance.Contrast(im).enhance(.85)
    im = Image.blend(im, Image.new('RGB', im.size, (236,228,228)), .22)
    W, H = im.size
    ov = Image.new('L', (W,H), 0); od = ImageDraw.Draw(ov)
    for y in range(0, H, 5):
        for x in range(0, W, 5):
            od.ellipse([x, y, x+1.6, y+1.6], fill=50)
    Image.composite(Image.new('RGB', (W,H), (120,114,124)), im, ov).save(out, quality=90)
```

Per style: for paintings, use the defaults. For sky photos and anime skies, keep more colour so the blue stays fresh: `Color` 0.8 and the blend 0.12. For the anime sky, also drop the blur to 0.8 so the cel edges stay crisp.

If a signature shows in the visible area, shift `background-position` or zoom with `background-size:auto 125%`.

### No overlay

Run the halftone function with the dot loop removed (keep the resize, blur, colour, contrast and blend steps) so the background still gets the soft pastel palette and sits with the rest of the page. For the anime sky, drop the blur too.

### Text texture (alternative)

A subtle text-art overlay of letters, digits and symbols across the whole background panel, on top of everything in it, clouds and highlights included. Glyph density follows brightness: darker areas get dense glyphs like `$ 8 0`, mid areas `X x`, bright areas and clouds lighter ones like `x + X`, so the shapes underneath still read through. About 15% of glyphs are swapped at random so no area is a single symbol, smooth noise makes the pattern drift and thin out in patches, and a few random gaps break up the grid. Most glyphs are a darker tint of the colour under them, a few are white. Use it instead of the halftone, not on top of it.

```python
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
def font(size):
    for f in ['/System/Library/Fonts/Menlo.ttc', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf']:
        try: return ImageFont.truetype(f, size)
        except OSError: pass
    return ImageFont.load_default(size)
def ascii_texture(src, out, W=2200, cell=34, ramp='$$880OXXxx+X0x+8x', strength=.17, seed=1):
    """Subtle text-art overlay: glyph density follows brightness, with drift so it reads organic."""
    rng = random.Random(seed)
    im = Image.open(src).convert('RGB')
    im = im.resize((W, int(im.height*W/im.width)), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(.85)
    im = Image.blend(im, Image.new('RGB', im.size, (236, 232, 240)), .12)
    W, H = im.size; ch, cw = cell, int(cell*.6)
    cols, rows = W//cw + 1, H//ch + 1
    lum = ImageOps.autocontrast(im.convert('L').filter(ImageFilter.GaussianBlur(4)), cutoff=2).resize((cols, rows), Image.BOX)
    drift = Image.effect_noise((max(2, cols//8), max(2, rows//8)), 64).resize((cols, rows), Image.BICUBIC)   # patchy bands
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer); f = font(int(ch*.8))
    for j in range(rows):
        for i in range(cols):
            v = lum.getpixel((i, j))/255 + (drift.getpixel((i, j))/255 - .5)*.5 + rng.uniform(-.08, .08)
            if rng.random() < .06: continue                      # a few random gaps; bright areas and clouds still get light glyphs
            c = ramp[max(0, min(len(ramp)-1, int(v*len(ramp))))]
            if rng.random() < .15: c = rng.choice(ramp)                # mix glyphs so no area is a single symbol
            r, g, b = im.getpixel((min(W-1, i*cw), min(H-1, j*ch)))
            tone = (int(r*.55), int(g*.6), int(b*.75)) if rng.random() < .8 else (255, 255, 255)  # mostly darker, some light
            d.text((i*cw, j*ch), c, font=f, fill=tone + (int(255*strength*(1.15-min(v, 1)*.35)),))
    Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB').save(out, quality=90)
```

Tuning:
- `strength` 0.12 to 0.2. The glyphs are a texture, not content: they must never compete with the headline or the screenshot. If you can read them at thumbnail size, lower it.
- `cell` sets glyph size: 30 to 40 at W=2200 so they are clearly letters once the panel is downscaled. Smaller turns into noise; bigger gets busy.
- Apply it to the background panel only, never to the page, the stat card or the window.
- Works on all three backgrounds; best on skies and soft gradients, where the brightness changes give the glyphs shape. On busy paintings use a lower strength.
- Change `seed` per slide so the pattern isn't identical across a carousel.

## Step 3: Logo variants

No logo file: use the Step 0 wordmarks (`wordmark_black.svg` on the page, `wordmark_white.svg` on a dark panel, `mark.svg` where space is tight) and tell the user it is a placeholder.

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

## Step 4: HTML template (square 1080x1080)

Start from `templates/slide_square.html`: it already reads `kit/tokens.css` and the wordmark, bleeds the panel and rules off both edges, and keeps every word inside the 132 to 948 safe zone. Copy it per slide, fill the `{{...}}` slots, and change layout only where the slide needs it.

Design tokens: link `kit/tokens.css` from Step 0 and use its variables. Page `#f7f7f7`, ink `#111`, muted `#6b6b6b`, lines `#e4e4e4`, card border `#e3e3e3`, active stat underline `var(--accent)`, stat dots `var(--accent)` / `#111` / `#9a9a9a` (the accent is the only colour on the page; keep red and green for screenshots that already carry them). Accent coloured text or hairlines use `var(--accent-ink)`. Font: Inter (Google Fonts) 500/600/650/700.

The accent is a highlight, not a theme: the underline bar, the first stat dot, one emphasised word in the headline at most (in `--accent-ink`), the swipe chevron and the wordmark tile. Never tint the page, the card or the window chrome.

Structure per slide:
- Vertical guide lines on the safe-zone edge (x 120 and 960 on a square; 48px from the edges only when the image is never cropped), horizontal rules under the header and above the footer that run off both edges, small 7px rotated-square "diamonds" where rules meet the guide lines.
- Header: small eyebrow (e.g. "Settled this quarter" or "30 days on Reddit" + "1 / 4" page count), headline 52px weight 650 letter-spacing -0.035em, sub line 22px muted.
- Stat card: white, 3 cells split by 1px borders, each with a colored dot + label (17px muted) and a value (38px weight 600). First cell gets a 3px `var(--accent)` bottom bar. Uppercase 14px label above each row when there are two rows.
- Panel: `flex:1`, radius 10px, `background:url(paintN.jpg) center/cover`, padding 16 to 26px, centers the window.
- Window: radius 12px, shadow `0 24px 60px -10px rgba(30,20,40,.45), 0 0 0 1px rgba(0,0,0,.12)`, 44px light title bar (`linear-gradient(#f1f1f1,#e6e6e6)`) with red/yellow/green 13px dots (`#ff5f57 #febc2e #28c840`) and a centered 16px title naming the source (e.g. "Zepapay · Settlements" or "Reddit · Post Insights"). Content: the screenshot crop `img{width:100%}` with compact rows below.
- Footer: logo or wordmark (black, ~36px tall) left, source line and domain right (e.g. "Source: Zepapay dashboard · zepapay.com"), both inside the safe zone.
- Avoid CSS class name collisions (e.g. don't reuse `.t` for both the window title and stat tiles).

For 1080x1350, use the same template with larger type (headline 64px, stat values 50px, sub 27px). For the 1500x600 banner: text block left (eyebrow, 58px headline, stat chips), painted panel with window on the right ~640px wide, logo bottom left, same grid lines and diamonds.

## Step 5: Render and check

```js
const {chromium} = require('playwright');
(async()=>{const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1080,height:1080}, deviceScaleFactor:2});
for (let i=1;i<=4;i++){ await p.goto(`file://${process.cwd()}/s${i}.html`); await p.waitForTimeout(1000);
  const bottom = await p.evaluate(()=>Math.max(...[...document.querySelectorAll('body *')].map(e=>e.getBoundingClientRect().bottom)));
  console.log(i, bottom);  // must be <= viewport height
  await p.screenshot({path:`slide${i}.png`}); }
await b.close();})();
```
Chromium is preinstalled (PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers); `npm i playwright` if the module is missing, never `playwright install`.
On a Mac without Playwright, headless Chrome renders a slide directly: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=1080,1080 --screenshot=$PWD/slide1.png file://$PWD/s1.html`.

Always view a contact sheet of every slide before delivering. Check: the brand name, accent and domain are the chosen brand's on every slide, no licence wording appears for an unlicensed brand, no sensitive payment data shows, numbers match the screenshots and each other, nothing overflows or overlaps, the window is not clipped, no signature or unwanted UI shows, text in the screenshot is readable, headline and sub do not wrap awkwardly.

## Step 6: Export

- Downscale the 2x renders to exact target size with LANCZOS (e.g. 1080x1080) and save JPG quality 92.
- Combine slides into a PDF carousel for LinkedIn document posts (`imgs[0].save(pdf, save_all=True, append_images=imgs[1:])`).
- Keep earlier versions; never overwrite a previous version's files. Use folders like `zepapay/v5/` (brand first) and suffixes like `_square_`.
- If delivering an HTML gallery with base64 images and download buttons, keep it under 30 MB (drop embedded PDFs first if it grows too large).
- Send files with SendUserFile and describe the result in one or two sentences, including the brand, painting credits, any numbers that were estimated, and whether the logo is a placeholder wordmark.