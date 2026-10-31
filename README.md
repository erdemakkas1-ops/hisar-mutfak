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

Six keyframes of one kitchen from one camera (`img/film/`, 1920 × 1080 and 1080 × 1920 for phones),
scrubbed by scroll over film seconds 0–14, telling Hisar's own process:

1. **Keşif & ölçü** — the empty room, a laser level's red line on the wall (`1-kesif`).
2. **Çizim** — fades to the same kitchen as a white clay model (`2-cizim`).
3. **Üretim & montaj** — fades to carcasses without doors or worktop (`3-montaj`).
4. **Teslim** — the finished kitchen lifts up from below behind a red edge, like a door (`4-teslim`).
5. **Sizin renginizde** — the doors turn green, then light blue, the same way (`5-yesil`, `6-mavi`);
   then the closing call to action.

- The frames are Gemini images (see `GEMINI.md` for the prompts and order; the originals sit in
  `gemini/`, kept out of git). They came out at 1024 × 572, so the 1920 px frames are upscaled and
  soft; the phone frames are cut from the middle of the desktop ones. Full-size or vertical (`-m`)
  versions from Gemini would sharpen both.
  `py -3 tools/keyframes.py [folder]` aligns, crops and converts a set (default folder `gemini/`).
- The whole stage pushes in slightly (scale 1.08 → 1). Chapter captions use `data-from`/`data-to`
  in film seconds; annotation tags use `data-d` / `data-m`, a point on the desktop / phone image as
  fractions of its width and height. Re-place them when the images change.
- `prefers-reduced-motion`, no JS, or `?still` show the finished kitchen and the chapters as text.

The real photos that opened the first version (light blue, yeşil, antrasit, Menteşe) now lead the İşler track.

## Build and preview

```bash
py -3 tools/photos.py         # only after changing photos (needs instagram-raw/)
py -3 tools/keyframes.py      # only after new Gemini frames (needs gemini/)
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
