#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, os

SITE_DIR = r"C:\Users\79105\Desktop\likarulit"

with open(os.path.join(SITE_DIR, "prices.json"), encoding="utf-8") as f:
    data = json.load(f)

updated = 0
for car in data["cars"]:
    path = os.path.join(SITE_DIR, car["file"])
    new_price = car["new_price"]

    with open(path, encoding="utf-8") as f:
        html = f.read()

    original = html

    # 1. price-val div
    html = re.sub(
        r'<div class="price-val">.*?</div>',
        f'<div class="price-val">от {new_price} ₽</div>',
        html
    )

    # 2. meta tags: replace "от X ₽" in any meta content attribute
    def fix_meta(m):
        return re.sub(r'от [\d\s]+₽', f'от {new_price} ₽', m.group(0))

    html = re.sub(r'<meta name="description"[^>]+>', fix_meta, html)
    html = re.sub(r'<meta property="og:description"[^>]+>', fix_meta, html)

    if html != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"OK {car['name']}: {new_price}")
        updated += 1
    else:
        print(f"?? {car['name']}: no changes")

print(f"\nUpdated: {updated}/{len(data['cars'])}")
