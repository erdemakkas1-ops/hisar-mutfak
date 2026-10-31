"""Build the static site into dist/.

  python tools/build.py [https://site-url]

hisar.html is the single source (it is also what the claude.ai artifact publishes, which wraps
it in its own document). This script wraps it in a full HTML document, adds the favicon and the
share image, and copies img/. With a site URL it also writes absolute canonical/og URLs.
"""
import os
import shutil
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
SITE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ""

# the red "mutfak" tag of their logo, reduced to an H on red
FAVICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
    '<rect width="100" height="100" rx="14" fill="#d3132f"/>'
    '<path d="M28 22h14v22h16V22h14v56H58V56H42v22H28z" fill="#fff"/></svg>'
)


def share_image(dst):
    # the four film kitchens side by side, 1200 × 630
    w, h = 1200, 630
    out = Image.new("RGB", (w, h))
    names = ["lightblue", "yesil", "antrasit", "mentese"]
    cw = w // len(names)
    for i, n in enumerate(names):
        im = Image.open(os.path.join(ROOT, "img", n + ".webp")).convert("RGB")
        scale = max(cw / im.width, h / im.height)
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        left, top = (im.width - cw) // 2, (im.height - h) // 2
        out.paste(im.crop((left, top, left + cw, top + h)), (i * cw, 0))
    out.save(dst, "JPEG", quality=84, optimize=True, progressive=True)


def main():
    os.makedirs(DIST, exist_ok=True)
    for name in os.listdir(DIST):
        if name == ".vercel":
            continue
        path = os.path.join(DIST, name)
        shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)

    with open(os.path.join(ROOT, "hisar.html"), encoding="utf-8") as f:
        src = f.read()
    cut = src.index("</style>") + len("</style>")
    head, body = src[:cut], src[cut:].lstrip("\n")

    # relative, so the site also works from a sub-path such as <user>.github.io/hisar-mutfak/
    extra = ['<link rel="icon" href="favicon.svg" type="image/svg+xml">']
    if SITE:
        extra += [
            f'<link rel="canonical" href="{SITE}/">',
            f'<meta property="og:url" content="{SITE}/">',
            f'<meta property="og:image" content="{SITE}/og.jpg">',
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            '<meta name="twitter:card" content="summary_large_image">',
        ]

    page = (
        '<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + "\n".join(extra) + "\n" + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    )
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    with open(os.path.join(DIST, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    share_image(os.path.join(DIST, "og.jpg"))
    shutil.copytree(os.path.join(ROOT, "img"), os.path.join(DIST, "img"))

    size = sum(os.path.getsize(os.path.join(d, n)) for d, _, ns in os.walk(DIST) for n in ns)
    print(f"dist/ built, {size / 1e6:.2f} MB" + (f", site {SITE}" if SITE else ""))


if __name__ == "__main__":
    main()
