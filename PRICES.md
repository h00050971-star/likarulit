# Цены для сайта likarulit.ru

> Инструкция для Claude: в каждом файле `cars/*.html` заменить цену в двух местах:
> 1. `<div class="price-val">СТАРАЯ ЦЕНА ₽ за день</div>` → новая цена
> 2. `content="...от СТАРАЯ ЦЕНА ₽ за день..."` в meta description и og:description
> Остальное не трогать.

---

## Таблица цен

| Файл | Машина | Цена на сайте сейчас | НОВАЯ ЦЕНА |
|---|---|---|---|
| audi-tt.html | Audi TT | 6 900 | 11 500 |
| audi-tt-fv.html | Audi TT FV | 6 900 | 12 000 |
| bmw-230-kabriolet.html | BMW 230 Кабриолет | 4 500 | 8 500 |
| bmw-430i-2-0-gran-coupe.html | BMW 430i 2.0 Gran Coupe | 5 900 | 10 000 |
| bmw-430i-f33.html | BMW 430i F33 Кабриолет | 5 900 | 10 500 |
| bmw-4-gran-coupe.html | BMW 4 Gran Coupe | 5 500 | 9 500 |
| bmw-520d-g30-m-sport.html | BMW 520D G30 M Sport | 5 500 | 9 500 |
| bmw-520i.html | BMW 520i | 5 800 | 9 500 |
| bmw-520i-akpp.html | BMW 520i АКПП | 5 800 | 9 500 |
| bmw-5-g30-2-0.html | BMW 5 G30 2.0 | 4 500 | 7 500 |
| bmw-5-g30-m-sport-lci.html | BMW 5 G30 M Sport LCI | 4 900 | 8 500 |
| bmw-7-740li.html | BMW 7 740Li | 3 500 | 7 000 |
| bmw-7-750li.html | BMW 7 750Li | 3 500 | 7 000 |
| bmw-m5-sport.html | BMW M5 Sport | 4 000 | 8 500 |
| bmw-m5-sport-4wd.html | BMW M5 Sport 4WD | 4 500 | 9 000 |
| bmw-x5-4-0-xdrive.html | BMW X5 4.0 xDrive | 9 900 | 17 000 |
| bmw-x5-g05.html | BMW X5 G05 | 9 900 | 16 000 |
| changan-lamore.html | Changan Lamore | 3 000 | 5 000 |
| changan-uni-t.html | Changan UNI-T | 3 900 | 6 500 |
| changan-uni-t-2.html | Changan UNI-T 2 | 3 900 | 6 500 |
| changan-uni-v.html | Changan UNI-V | 3 900 | 6 500 |
| chery-arrizo-8.html | Chery Arrizo 8 | 2 800 | 4 500 |
| chery-arrizo-8-pro.html | Chery Arrizo 8 Pro | 3 200 | 5 000 |
| chery-tiggo-7-pro-max.html | Chery Tiggo 7 Pro Max | 3 000 | 5 500 |
| chery-tiggo-8-pro-e.html | Chery Tiggo 8 Pro E | 4 000 | 7 000 |
| chery-tiggo-8-pro-max.html | Chery Tiggo 8 Pro Max | 4 000 | 7 000 |
| chery-tiggo-pro-plug-in-hybrid.html | Chery Tiggo Pro Plug-in Hybrid | 4 500 | 7 500 |
| chevrolet-camaro.html | Chevrolet Camaro | 7 000 | 12 000 |
| chevrolet-camaro-gt-8.html | Chevrolet Camaro GT | 8 000 | 14 000 |
| chevrolet-trax.html | Chevrolet Trax | 2 500 | 4 500 |
| ford-kuga.html | Ford Kuga | 3 000 | 5 500 |
| ford-mustang.html | Ford Mustang | 7 900 | 13 000 |
| ford-mustang-shelby-gt.html | Ford Mustang Shelby GT | 10 000 | 17 000 |
| geely-coolray.html | Geely Coolray | 3 500 | 6 000 |
| haval-jolion.html | Haval Jolion | 3 500 | 6 000 |
| kia-carnival.html | Kia Carnival | 4 000 | 7 000 |
| lexus-es250.html | Lexus ES250 | 4 500 | 8 500 |
| lexus-gs350.html | Lexus GS350 | 5 100 | 9 000 |
| mercedes-benz-e200-black.html | Mercedes-Benz E200 Black | 4 500 | 8 500 |
| mercedes-e200.html | Mercedes E200 | 4 500 | 8 000 |
| mercedes-glk220d.html | Mercedes GLK220d | 3 500 | 6 500 |
| nissan-patrol.html | Nissan Patrol | 4 500 | 8 500 |
| noah-gibrid.html | Toyota Noah Гибрид | 2 500 | 4 500 |
| toyota-camry.html | Toyota Camry | 3 000 | 5 500 |
| toyota-esquire.html | Toyota Esquire | 3 000 | 5 500 |
| toyota-serena.html | Toyota Serena | 2 500 | 4 500 |

---

## Финмодель — зачем эти цены

Sergey's price = его цена (уже стоит на сайте)  
Наша цена = то что ставим через блог Лики  
Маржа = разница — делится 50/50 между Ликой и Артёмом

### 10 машин, 65% загрузка = 20 дней/мес

| Группа | Машин | Наша цена | Сергей | Маржа/день | Итого/мес |
|---|---|---|---|---|---|
| Топ (Mustang, X5, 430i, Camaro GT) | 4 | 13 000–17 000 | 7 900–9 900 | 5 500 avg | 440 000 |
| Средний (BMW 5, BMW 7, 520i, Audi TT) | 4 | 7 000–11 500 | 3 500–5 800 | 3 700 avg | 296 000 |
| Бюджет (Changan, Noah, Ford Kuga) | 2 | 4 500–6 500 | 2 500–3 900 | 2 200 avg | 88 000 |
| **ИТОГО** | 10 | | | | **824 000 ₽** |
| Лика | | | | | **412 000 ₽** |
| Артём | | | | | **412 000 ₽** |

### Для 200 000 ₽ каждому нужно:
- 25 бронирований в месяц (по 4 дня avg)
- Или 1 бронирование в день со средними машинами
