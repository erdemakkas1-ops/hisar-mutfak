# Hisar Mutfak Muğla — renk filmi demo

One-page demo for Hisar Mutfak Muğla (@hisarmutfakmugla): kitchen cabinets, door renewal, bathroom
cabinets, wardrobes, TV units and consoles in Muğla. Same family as the Arkhera and Maviron demos
(a pinned opener scrubbed by page scroll, then editorial sections), with its own identity: warm
paper ground, ink and the red of their logo's "mutfak" tag, Archivo condensed for display type.

Live: https://erdemakkas1-ops.github.io/hisar-mutfak/ (GitHub Pages, repo `erdemakkas1-ops/hisar-mutfak`,
branch `gh-pages`). `pages/` is a checkout of `gh-pages` (kept out of git). To update the live site:

```bash
py -3 tools/build.py https://erdemakkas1-ops.github.io/hisar-mutfak
cp -r dist/index.html dist/favicon.svg dist/og.jpg dist/img pages/
cd pages && git add -A && git commit -m "Update site" && git push
```

## The film

Four of Hisar's own kitchens, scrubbed by scroll over film seconds 0–10:

1. **Light blue** — framed lacquer doors (`lightblue`).
2. **Yeşil** — green lacquer shaker doors (`yesil`).
3. **Antrasit** — door renewal on an existing kitchen (`antrasit`).
4. **Füme & ışık** — Menteşe, hidden LED (`mentese`); closing call to action.

Each new kitchen lifts up from below behind a red edge, like a door, and the whole ground blends into
that kitchen's door colour (`data-bg` / `data-tone` on each `.chap`). The colour rail jumps between them.
`prefers-reduced-motion`, no JS, or `?still` show the four chapters stacked, each on its own colour.

The film was planned as AI keyframes of one kitchen (empty room → carcasses → doors → evening),
but the Gemini key on this machine was rejected (401), so it uses only real photos.

## Build and preview

```bash
py -3 tools/photos.py         # only after changing photos (needs instagram-raw/)
py -3 tools/build.py [https://site-url]
node tools/serve.js           # dist/ on http://localhost:5531
```

`hisar.html` has no `<html>`/`<head>`: the claude.ai artifact wraps it itself, and `build.py`
wraps it for the real site (favicon, share image, canonical/og URLs with a site URL).

## Content sources

- Bio ("Mutfak - Banyo - Dekorasyon"), phone numbers, places, door types and descriptions:
  their Instagram profile and captions (October 2026). Customer names in captions are left out.
- Photos: 640 px thumbnails of their own posts (`instagram-raw/`), each card links to the post.

## Before going live

- Ask Hisar for full-resolution photos (the thumbnails are 480–640 px, soft on large screens)
  and a vector logo (the header wordmark is redrawn from the 150 px profile picture).
- Confirm which number is on WhatsApp (assumed 0532 593 76 22, the one on their holiday post),
  the free "keşif ve çizim" offer, and the service area (Menteşe, Ula, Yatağan, Bodrum, Kızılağaç
  come from captions).
- The business is "Hisar Mutfak **Muğla**"; no "Hisar Mutfak Tuğla" account was found.
