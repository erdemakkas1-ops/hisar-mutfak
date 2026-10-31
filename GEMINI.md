# Açılış filmi için Gemini görselleri

Açılış, **aynı mutfağın aynı kameradan çekilmiş 6 karesiyle** oynuyor. Kaydırdıkça sırayla:

| Sıra | Dosya adı | Ne görünüyor | Geçiş |
|---|---|---|---|
| 1 | `1-kesif` | Boş, sıvalı oda; lazer metre kırmızı çizgi atıyor | Açılış karesi |
| 2 | `2-cizim` | Aynı oda, beyaz 3D maket mutfak | Yumuşak geçiş |
| 3 | `3-montaj` | Gövdeler takılmış, kapaksız, tezgâhsız | Yumuşak geçiş |
| 4 | `4-teslim` | Bitmiş mutfak, kaşmir lake kapaklar, LED'ler yanık | Aşağıdan yukarı kırmızı çizgiyle açılır (kapak gibi) |
| 5 | `5-yesil` | Aynı mutfak, kapaklar yeşil lake | Kapak rengi değişir |
| 6 | `6-mavi` | Aynı mutfak, kapaklar açık mavi lake | Kapak rengi değişir |

Geçişlerin çalışması için **6 karede de kamera, pencere, tavan ve duvarlar aynı yerde** olmalı.
Bunun yolu: önce `4-teslim` karesini üret, diğer beşini **o görseli Gemini'de düzenleterek** yap
(her seferinde yeni görsel ürettirme; yoksa mutfak her karede değişir).

## Sıra ve promptlar

İngilizce prompt Gemini'de daha tutarlı çalışıyor. Görsel oranını **16:9 (yatay)** seç.

**1) Önce `4-teslim` (bitmiş mutfak)**
İstersen Hisar'ın Menteşe mutfağı paylaşımını (gizli LED'li olan) referans görsel olarak ekle.

> Photorealistic interior photograph of a newly finished modern kitchen in a bright Mediterranean house in Muğla, Turkey. Wide 16:9 frame, eye-level camera at 1.5 m standing at the room entrance, 24 mm lens, one-point perspective looking straight at the main kitchen wall. A straight run of handle-less matte lacquer base cabinets and upper cabinets up to the ceiling in a warm cashmere beige colour. On the right, two tall walnut pantry columns with a built-in oven and microwave. Cream porcelain worktop and full-height cream porcelain backsplash with soft veining, a warm LED strip glowing under the upper cabinets. On the left, a window above the sink with olive trees and white houses outside. Pale large porcelain floor tiles, smooth white ceiling with a recessed linear light. Late afternoon daylight, calm and warm. Architectural photography, no people, no text, no logos.

**2) `5-yesil`** — 1. görseli yükle ve şunu yaz:

> Edit this image. Keep the same room, the same camera angle and every object exactly where it is. Change only the colour of the lacquer cabinet doors to a deep forest green matte lacquer. Keep the walnut columns, the worktop, the backsplash and the lighting unchanged. Photorealistic.

**3) `6-mavi`** — yine 1. görseli yükle:

> Edit this image. Keep the same room, the same camera angle and every object exactly where it is. Change only the colour of the lacquer cabinet doors to a soft light blue (powder blue) matte lacquer. Keep the walnut columns, the worktop, the backsplash and the lighting unchanged. Photorealistic.

**4) `3-montaj`** — yine 1. görseli yükle:

> Edit this image. Keep the same camera angle, the same window, walls and ceiling. Show the kitchen during installation: the cabinet carcasses are mounted but have no doors and no drawer fronts, so the white melamine inside and the shelves are visible. No worktop yet, no backsplash tiles yet (plain plastered wall), the oven is not installed (empty opening). A cordless drill and a few hinges lie on the floor. Daylight, photorealistic.

**5) `2-cizim`** — yine 1. görseli yükle:

> Edit this image. Keep the same room, the same camera angle and the same shapes. Turn everything into an untextured white clay architectural 3D model: cabinets, columns, worktop, walls, floor and ceiling all in matte white and light grey, no materials or colours, soft shadows. The window stays bright. It should look like a kitchen designer's white 3D model render.

**6) `1-kesif`** — yine 1. görseli yükle:

> Edit this image. Keep the same camera angle, the same window and the same ceiling shape. Remove all cabinets, appliances, worktop and backsplash: an empty room with smooth plastered walls, a bare floor and daylight through the window. Add a laser level on a tripod in the middle of the room projecting a thin bright red horizontal line across the back wall, and a tape measure on the floor.

Sonucu 1. kareyle üst üste koyup hızlıca karşılaştır: pencere ve tavan kayıyorsa o kareyi yeniden düzenlet.

## Telefon için (isteğe bağlı ama önerilir)

Telefonda ekran dikey olduğu için yatay görselin ortası kesilir. Daha iyi sonuç için: `4-teslim`
görselini **9:16 (dikey)** olarak genişlettir (*"Extend this image to a vertical 9:16 frame, keep the
kitchen wall centred, add more floor and ceiling"*), sonra aynı 5 düzenlemeyi bu dikey görsel
üzerinde tekrarla. Adlar: `1-kesif-m`, `2-cizim-m`, … `6-mavi-m`. Yapmazsan telefon karesi yatay
görselin ortasından kesilir.

## Teslim

Görselleri (png, jpg ya da webp) proje içindeki `gemini/` klasörüne yukarıdaki adlarla koy. Sonra:

```bash
py -3 tools/keyframes.py
```

Bu komut görselleri hizalayıp 1920 × 1080 ve 1080 × 1920 WebP'ye çevirir ve `img/film/` altına
yazar. Etiketlerin ("Duvar · 412 cm", "Gizli LED" vb.) yerleri yeni görsele göre `hisar.html`
içindeki `data-d` / `data-m` değerlerinden ayarlanır.
