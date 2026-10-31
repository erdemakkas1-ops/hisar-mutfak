"""Make the site's photos from Hisar Mutfak's own Instagram posts (instagram-raw/, 640 px thumbnails).

  python tools/photos.py

Each entry: raw file -> post shortcode (for reference) and crop box (left, top, right, bottom) or None.
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "instagram-raw")
OUT = os.path.join(ROOT, "img")

PHOTOS = {
    "lightblue": ("DfC8mPjDXFf", None),   # light blue lake kapak, Oct 2026
    "yesil": ("DKmZNk3IuL8", None),       # yeşil lake gönçük kapak
    "antrasit": ("DeZHiugDYJM", None),    # kapak yenileme, panel kapak
    "mentese": ("DeCjxesjQKt", None),     # Menteşe, gizli LED
    "kizilagac": ("DPGwH0zjfqd", None),   # Kızılağaç, lake mutfak
    "vestiyer": ("DPE_B_KDW_b", None),    # Ula, sürme kapaklı vestiyer
    "soft": ("DKmtDQhI-tQ", None),        # Bodrum, kendinden kulplu soft kapak
    "tvunite": ("DMiYQIqoNQn", None),     # Yeşilyurt, TV ünitesi
    "dresuar": ("DKeS6gTo-ig", None),     # CNC kesim lake dresuar
    "gardrop": ("DJXC5y5oyjZ", None),     # Yatağan, sürgülü gardırop
    "kasmir": ("DecPPWeDWGS", None),      # kaşmir, ceviz, krem porselen numuneleri
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (_, box) in PHOTOS.items():
        im = Image.open(os.path.join(RAW, name + ".jpg")).convert("RGB")
        if box:
            im = im.crop(box)
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=86, method=6)
        print(name, im.size)


if __name__ == "__main__":
    main()
