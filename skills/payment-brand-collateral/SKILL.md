---
name: "payment-brand-collateral"
description: "Create sales collateral in light or dark mode for ZepaPay and the other payment brands (Secure Payment Services, AltPay, Sepa Mint, Offrampr, Onrampr, Ape Card, Pure Labs, Swipe Wire Pay, Card Payz, Fiat Pay): A4 product one-pagers with bento benefit grids, 9:16 rate cards and fee sheets, and 16:9 commercial terms decks with cover, terms table and contact slide, exported as PNG and PDF for Telegram, email and sales calls, in the brand's accent and within its licence rules. For LinkedIn or X post graphics use payment-brand-social-graphics instead."
---

# Payment brand collateral

Sales documents for one payment brand at a time: product one-pagers, rate cards and terms decks. Built as HTML from `templates/`, styled by `templates/collateral.css` plus the brand's `kit/tokens.css`, and rendered with `scripts/render.py` to one PNG per page and a PDF.

Read `reference/brand-rules.md` before writing any copy: it holds brand data, the licence and claims rules (binding) and the copy rules. Read `reference/backgrounds.md` when the background is a painting, clouds or anime sky. Social post graphics belong to the `payment-brand-social-graphics` skill.

## Ask first (always, before generating anything)

Before writing any HTML or rendering, ask these four in one AskUserQuestion call, even when the request seems to answer them. The recommended option goes first. If the request already answered a question, make that answer the recommended option rather than skipping it.

1. **Output:** one-pager (A4 portrait) / rate card (9:16 portrait) / terms deck (16:9).
2. **Mode:** light / dark. Recommend dark for one-pagers and decks sent on Telegram or shown on a screen, light for rate cards (printable, tables read better).
3. **Design direction:**
   - **Follow the skill:** the editorial house style. Grid guide lines, hairline-bordered cards, small uppercase section labels, accent only as an underline bar or rule.
   - **New design cues:** the collateral look in "Reference cues" below. Flat bento tiles in two alternating tones, large plain section headings, a filled accent CTA band, a hand-drawn accent underline on the key word.
   Never mix the two in one document.
4. **Background** for the art panels: abstract brand shapes / flat / painting / clouds and sky / anime sky. Pitch each in one line from `reference/backgrounds.md`, with a recommendation (abstract shapes for most collateral).

If the background is painting, clouds or anime sky, follow up with one more question for the overlay and its intensity.

## Before starting

After the questions, confirm (or infer from the request and state the assumption):
1. Brand. Default ZepaPay. See `reference/brand-rules.md`.
2. Audience and how it is sent (Telegram, email, printed, shown on a call). Rate cards and terms decks are private sends, never public posts.
3. The numbers. Fees, limits, tiers and corridors come only from the user or the brand's public page. A brand book price list is used only when the user names it and confirms the figures.
4. Contacts for a deck's contact slide: names, emails, photos, QR targets. Only from the user.
5. Logo file. Without one, use the kit wordmark and say it is a placeholder.

## Step 1: Brand kit

```bash
python3 <skill dir>/scripts/brand_kit.py zepapay ./kit
```

## Step 2: Background

Abstract shapes and flat need nothing. Painting, clouds or anime sky: source and filter as in `reference/backgrounds.md` (including the dark-mode filter), then use `<div class="art painting" style="--img:url(bg1.jpg)">`.

## Step 3: Build

In `templates/`:

| Template | Size | Use |
|---|---|---|
| `onepager.html` | A4 portrait, 1240x1754 | Product one-pager: title, three bento sections, CTA band. |
| `ratecard.html` | 9:16, 1080x1920 (add sheets for "continued" pages) | Fee sheet: headline with key word, hero fee cards, fee table, footnote. |
| `deck.html` | 16:9, 1920x1080, one `<section class="sheet wide">` per slide | Cover, commercial terms table, contact slide. |

Copy `templates/*` plus `./kit` (Step 1) into the working folder, replace all sample copy (it is ZepaPay's public page copy, there only so the layout renders), then:

```bash
python3 <skill dir>/scripts/render.py onepager.html out --theme dark --cues collateral
```

It writes one PNG per sheet and one PDF of all sheets, and prints `WARNING: content overflows` when any sheet's content runs into its bottom padding or past the edge. Fix every warning by cutting copy first, spacing second. Each sheet must have `id="pN"`.

**Writing collateral copy:** tile headline max 6 words, fragment max 10, lowercase fragment unless it starts with a name. One number per tile at most. CTA button is a verb and the brand ("Start settling", "Open an account"), never "Learn more". Tables: write ranges in full ("1,000 to 1,000,000"), use the same unit style throughout, and show every price as the user gave it.

**Design direction in collateral:** `data-cues="skill"` gives bordered cards, uppercase section labels, accent underline bars, an inset accent rule on the CTA, and the vertical guide lines. `data-cues="collateral"` gives flat tiles in two tones, plain headings, a filled accent CTA band and the hand-drawn underline. Same HTML, so switching only takes a re-render.

**Art panels:** `<div class="art painting" style="--img:url(bg1.jpg)">` (same for `clouds`, `anime`) uses an image prepared in Steps 1 and 2. `<div class="art shapes">` and `<div class="art flat">` need no image. In a tile, the art sits on the right 42% and fades into the tile colour, and the tile text is kept to the left 60%.

## Reference cues

What the reference collateral (EMCD Pay one-pager, EMCD Payments terms deck, EMCD on-ramp rate card) does, and how the templates use it. These are cues only: never copy another company's logo, 3D renders, wording, people, colours or numbers.

- **One-pager layout:** big product name top left, a one-line positioning sub under it, logo top right. Then three sections in a fixed order: why partners choose us, key benefits, who it's for. Each is a two-column bento of short tiles. A tile has a 3 to 6 word headline and a lowercase fragment under it ("widget & API, go live in 1 day"). It ends with a full-width CTA band: a two-line hook on the left, one sentence in the middle, and a button on the right.
- **Tile rhythm:** two tones alternate by row (dark tiles with an image on the right, then light tiles with text only), so the page reads in bands. One full-width tile per section at most, with a short right-aligned tag ("24/7").
- **Language:** numbers lead the headlines ("600+ cryptocurrencies", "Fees from just 0.5%", "2-4x cheaper", "190+ countries", "go live in 1 day"). Benefit first, then a short proof fragment. No paragraphs, no adjectives without a number or a mechanism. Audience tiles name the segment and list three concrete examples. Our version keeps the same pattern but only with numbers this skill allows (see "Licence and claims"), no em dashes, and no comparative claims ("cheaper than", "fastest") unless the user gives the source.
- **Positioning:** B2B, merchant-facing, about integration speed, cost, coverage and getting money out. It sells outcomes (go live, convert, get paid), not technology. Match that for every brand, inside each brand's licence rules.
- **Rate card:** a centred two-line headline whose product word is set in the accent and underlined with a hand-drawn stroke. Logo top right. Hero fee cards come before the table: one tall card for the headline product with volume tiers, then one wide card with three "as low as" figures. Then a table with small uppercase accent headers (method, country, region, price). Each row has a muted sub note for currencies or exclusions and a tier list (tier label in small muted type, % right-aligned). A footnote is marked with an asterisk, and "(continued)" is added to the headline on overflow pages.
- **Terms deck:** the cover has the title top left, a large hero visual on the right, and a small "Commercial terms for B2B" line bottom left. The terms slide is a dense table with grouped column headers ("Commercial terms" over the product columns, "Transaction fees, % (monthly volume)" over the tier columns), merged cells for shared values, and "Coming soon" or "N/A" written out rather than left blank. The contact slide has a community card with link list on the left and stacked person cards (name, email, QR) on the right.
- **Mode:** the one-pager and deck are dark (near-black page, charcoal tiles, light tiles for contrast). The rate card is light (white page, pale tinted cards, accent numbers). The templates follow the "Ask first" mode answer, not the reference.

## Step 4: Check and export

- Fix every `WARNING: content overflows` from `render.py`: cut copy first, then spacing.
- View every page before delivering. Check the brand name, accent, logo and domain belong to the chosen brand; no licence wording appears for an unlicensed brand; every number matches what the user gave; nothing is clipped; tables align; footnotes say "Indicative" where prices appear.
- Deliver the PDF plus the per-page PNGs. Keep earlier versions in `<brand>/vN/` folders, never overwrite.
- Send files with SendUserFile and say in one or two sentences: brand, output, mode, design direction, background credits, and whether the logo is a placeholder.
