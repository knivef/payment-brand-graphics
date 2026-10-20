---
name: "payment-brand-social-graphics"
description: "Create editorial social graphics in light or dark mode for ZepaPay and the other payment brands (Secure Payment Services, AltPay, Sepa Mint, Offrampr, Onrampr, Ape Card, Pure Labs, Swipe Wire Pay, Card Payz, Fiat Pay): stat cards and screenshots in a macOS window over a public domain painting, cloudy sky, anime-style sky or abstract brand shapes, with halftone or text-texture overlays, in the brand's accent and within its licence rules. Use for LinkedIn and X posts, multi-image albums, PDF carousels and X banners. For one-pagers, rate cards or decks use payment-brand-collateral instead."
---

# Payment brand social graphics

Social posts for one payment brand at a time: off-white or near-black page with thin grid lines, a headline, stat cards, and a background panel holding a macOS-style window that shows a screenshot or chart. Built as HTML from `templates/slide_square.html`, rendered with `scripts/render.py`. A brand-aware clone of `light-editorial-graphics` (knivef/creatives).

Read `reference/brand-rules.md` before writing any copy: it holds brand data, the licence and claims rules (binding) and the copy rules. Read `reference/backgrounds.md` when the background is a painting, clouds or anime sky. Sales documents (one-pagers, rate cards, terms decks) belong to the `payment-brand-collateral` skill.

## Ask first (always, before generating anything)

Before writing any HTML or rendering, ask these four in one AskUserQuestion call, even when the request seems to answer them. The recommended option goes first. If the request already answered a question, make that answer the recommended option rather than skipping it.

1. **Format:** 1080x1350 portrait (recommended for LinkedIn albums) / 1080x1080 square (single-image posts) / 1500x600 banner (X Article header, 5:2).
2. **Mode:** light / dark. Light is the house default for feed posts. Dark stands out in a light feed and suits launch or metrics posts.
3. **Design direction:** follow the skill (the editorial house style below) / new design cues (flat filled cards in two tones, plain bold headings, a filled accent band for the call to action, a hand-drawn accent underline on the key word, as in `payment-brand-collateral`). Never mix the two in one carousel.
4. **Background:** painting / clouds and sky / anime sky / abstract brand shapes / flat. Pitch each in one line from `reference/backgrounds.md`, with a recommendation.

If the background is painting, clouds or anime sky, follow up with one more question for the overlay (halftone dots, text texture or none) and its intensity (subtle or medium).

## Before starting

After the questions, confirm (or infer from the request and state the assumption):
1. Brand. Default ZepaPay. See `reference/brand-rules.md`.
2. How it will be posted: single image, multi-image album, or PDF document carousel. This decides the crop rules.
3. Number of slides and the story each one tells (see "Presenting data").
4. Logo file (transparent PNG preferred). Black in light mode, white in dark mode. With no logo file, use the kit wordmark and say it is a placeholder.
5. Source screenshots and raw numbers.

## Step 1: Brand kit

```bash
python3 <skill dir>/scripts/brand_kit.py zepapay ./kit
```

Writes `tokens.css` (light and dark sets), `wordmark_black.svg`, `wordmark_white.svg` and `mark.svg`. Field meanings and the rules that come with them are in `reference/brand-rules.md`.

## Step 2: Background

Painting, clouds or anime sky: source and filter it as in `reference/backgrounds.md` (including the dark-mode filter). Abstract shapes and flat: nothing to prepare.

## Feed cropping (design for it, don't fight it)

LinkedIn multi-image albums show each image as a roughly 4:5 tile in a sideways-scrolling row. A 1080x1080 square loses about 108px on the left and right (only the centre 864x1080 shows). The tile also covers the image with LinkedIn's own controls: a "1/4" count badge in the top-right corner and a round "›" next button halfway down the right edge. X crops multi-image posts too (side-by-side tiles for 2 to 4 images). A PDF document carousel is not cropped.

Seen in a real post: the eyebrow "30 days on Reddit" became "days on Reddit", the headline lost its first digit ("3 posts" became "posts"), the "1 / 4" page count and "Swipe for the receipts" were cut, and left-aligned text ran straight into the crop edge, which looked like a mistake.

**Choose the format first**
- Multi-image album: render 1080x1350 (4:5), so the tile shows the whole image. Still keep the safe zone below, because tile shapes change with image count and screen width.
- Uncropped carousel: give the PDF from Step 5 and suggest posting it as a document.
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

**Check it** (add this to Step 4): for every slide, also save a simulated tile. Crop the centre 4:5, draw a dark rounded "1/4" badge top-right and a 40px dark circle on the right edge halfway down, and view all tiles together. Fix any slide where text touches an edge, a number is cut or hidden, or the layout looks off-centre.

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
- Footer source line names where the numbers come from ("Source: ZepaPay dashboard, Sept 2026" or "Source: Reddit Post Insights").

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

## Step 3: Build the slides (square 1080x1080)

Start from `templates/slide_square.html`: it already reads `kit/tokens.css` and the wordmark, bleeds the panel and rules off both edges, and keeps every word inside the 132 to 948 safe zone. Copy it per slide, fill the `{{...}}` slots, and change layout only where the slide needs it.

Design tokens: link `kit/tokens.css` from Step 1 and use its variables. It holds a light set on `:root` and a dark set under `[data-theme="dark"]`, so set the mode on `<html>` and never hard-code a colour. Dark: page `#0f0f10`, ink `#f5f5f5`, muted `#9a9a9e`, cards `#1c1c1f`, window chrome dark grey, accent text in `--accent-ink` (the dark-page variant from `accent_ink_dark`). Light values follow. Page `#f7f7f7`, ink `#111`, muted `#6b6b6b`, lines `#e4e4e4`, card border `#e3e3e3`, active stat underline `var(--accent)`, stat dots `var(--accent)` / `#111` / `#9a9a9a` (the accent is the only colour on the page; keep red and green for screenshots that already carry them). Accent coloured text or hairlines use `var(--accent-ink)`. Font: Inter (Google Fonts) 500/600/650/700.

The accent is a highlight, not a theme: the underline bar, the first stat dot, one emphasised word in the headline at most (in `--accent-ink`), the swipe chevron and the wordmark tile. Never tint the page, the card or the window chrome.

Structure per slide:
- Vertical guide lines on the safe-zone edge (x 120 and 960 on a square; 48px from the edges only when the image is never cropped), horizontal rules under the header and above the footer that run off both edges, small 7px rotated-square "diamonds" where rules meet the guide lines.
- Header: small eyebrow (e.g. "Settled this quarter" or "30 days on Reddit" + "1 / 4" page count), headline 52px weight 650 letter-spacing -0.035em, sub line 22px muted.
- Stat card: `var(--card)` (white in light mode), 3 cells split by 1px borders, each with a colored dot + label (17px muted) and a value (38px weight 600). First cell gets a 3px `var(--accent)` bottom bar. Uppercase 14px label above each row when there are two rows.
- Panel: `flex:1`, `background:url(paintN.jpg) center/cover` (or class `shapes` / `flat` for the no-image backgrounds), padding 16 to 26px, centers the window.
- Window: radius 12px, shadow `0 24px 60px -10px rgba(30,20,40,.45), 0 0 0 1px rgba(0,0,0,.12)`, 44px title bar (`var(--chrome)`, light or dark with the mode) with red/yellow/green 13px dots (`#ff5f57 #febc2e #28c840`) and a centered 16px title naming the source (e.g. "ZepaPay · Settlements" or "Reddit · Post Insights"). Content: the screenshot crop `img{width:100%}` with compact rows below.
- Footer: logo or wordmark (black in light mode, white in dark, ~36px tall) left, source line and domain right (e.g. "Source: ZepaPay dashboard · zepapay.com"), both inside the safe zone.
- Avoid CSS class name collisions (e.g. don't reuse `.t` for both the window title and stat tiles).

For 1080x1350, use the same template with larger type (headline 64px, stat values 50px, sub 27px). For the 1500x600 banner: text block left (eyebrow, 58px headline, stat chips), painted panel with window on the right ~640px wide, logo bottom left, same grid lines and diamonds.

## Step 4: Render and check

Preferred: `python3 <skill dir>/scripts/render.py s1.html out --theme light` (uses Playwright or falls back to headless Chrome, warns on overflow; render each slide file, or the first one with each option when comparing). The manual Playwright loop below still works for slides.

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

## Step 5: Export

- Downscale the 2x renders to exact target size with LANCZOS (e.g. 1080x1080) and save JPG quality 92.
- Combine slides into a PDF carousel for LinkedIn document posts (`imgs[0].save(pdf, save_all=True, append_images=imgs[1:])`).
- Keep earlier versions; never overwrite a previous version's files. Use folders like `zepapay/v5/` (brand first) and suffixes like `_square_`.
- If delivering an HTML gallery with base64 images and download buttons, keep it under 30 MB (drop embedded PDFs first if it grows too large).
- Send files with SendUserFile and describe the result in one or two sentences, including the brand, mode, background credits, any numbers that were estimated, and whether the logo is a placeholder wordmark.
