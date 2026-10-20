# Backgrounds and overlays (shared by every payment brand skill)

Source of truth: `shared/reference/backgrounds.md` in knivef/payment-brand-graphics. Each skill carries a copy made by `scripts/bundle.py`.

## The options (pitch these when asking)

**Background**

- **Painting:** public domain landscape (Monet, Cezanne, Renoir). Classic, gallery feel, works for "the story" and founder posts.
- **Clouds and sky:** a real sky photo. Calm, airy, neutral; good for product, metrics and launch posts where the screenshot should dominate.
- **Anime sky:** an anime-style sky or landscape from a free wallpaper site (licensed for commercial use), bright blue with puffy cel-shaded clouds. Playful, eye-catching, good for build-in-public and community posts.
- **Abstract brand shapes:** soft accent coloured circles and glow, generated in CSS (`.art.shapes`). No licensing to check; the safe stand-in for the 3D renders seen in reference collateral.
- **Flat:** no image, a faint accent tint (`.art.flat`). For dense data pieces where nothing should compete with the numbers.

Mixing styles inside one carousel or document looks messy: use one style per carousel or document unless the user asks otherwise.

**Overlay** (only for painting, clouds and anime sky)

- **Halftone dots** (default): soft print look, quiet, works with every background.
- **Text texture:** faint letters, digits and symbols like `$ 8 0 X x +` over the whole background, clouds included, with density following the brightness. A data/terminal feel that suits metrics, fintech and build-in-public posts.
- **None:** clean background with only the pastel colour softening, for when the background itself should be the star (e.g. a striking anime sky).

For halftone and text texture, also offer intensity: **subtle** (text `strength` 0.12, halftone dot `fill` 35) or **medium** (text 0.17, halftone 50, the defaults). Use the same overlay and intensity across a carousel or document. If the user wants to compare, render slide 1 with each option side by side and let them pick before doing the rest. See "Texture filter" below.

Abstract shapes and flat need no image: use `<div class="art shapes">` or `<div class="art flat">` in collateral, or `<div class="panel shapes">` / `<div class="panel flat">` on a social slide. Skip the rest of this file for them.

## Get the background

Use the style picked in "Ask first". Whatever the style, the window covers the middle, so pick images with interest near the edges and top, and make a contact sheet and look at it before choosing.

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

## Texture filter

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

**Dark mode:** use a dark copy of `pastelize`: replace the light blend with `Image.blend(im, Image.new('RGB', im.size, (20,18,24)), .35)`, then `ImageEnhance.Brightness(im).enhance(.7)`, and draw the dots in `(200,200,210)` at fill 35 instead of `(120,114,124)`. The panel then sits on the near-black page without a bright hole. Text texture in dark mode: same function, blend toward `(20,18,24)` and use the white glyph share at 40% instead of 20%.

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
