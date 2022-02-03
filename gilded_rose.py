# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            if item.name not in [
                "Sulfuras, Hand of Ragnaros",
                "Aged Brie",
                "Backstage passes to a TAFKAL80ETC concert"
            ]:
                if item.sell_in > 0 and item.quality >= 1:
                    item.quality -= 1
                if item.sell_in <= 0 and item.quality >= 2:
                    item.quality -= 2
                if item.sell_in < 0 and item.quality >= 1:
                    item.quality -= 1

            if item.quality in range(0, 50):  # проверка качества товара 0 < quality < 50
                if item.name == "Aged Brie":
                    item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality != 0:
                    if item.sell_in >= 11 and item.quality <= 48:
                        item.quality += 1
                    if item.sell_in < 11 and item.quality <= 47:
                        item.quality += 2
                    if item.sell_in < 6 and item.quality <= 46:
                        item.quality += 3
                    if item.sell_in == 0:
                        item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
