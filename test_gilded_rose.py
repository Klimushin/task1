# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_quality(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=3, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=30),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
            Item(name="Conjured Mana Cake", sell_in=0, quality=6),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("+5 Dexterity Vest", items[0].name)
        self.assertEquals(3, items[0].sell_in)
        self.assertEquals(19, items[0].quality)

        self.assertEquals("Aged Brie", items[1].name)
        self.assertEquals(2, items[1].sell_in)
        self.assertEquals(1, items[1].quality)

        self.assertEquals("Elixir of the Mongoose", items[2].name)
        self.assertEquals(5, items[2].sell_in)
        self.assertEquals(6, items[2].quality)

        self.assertEquals("Sulfuras, Hand of Ragnaros", items[3].name)
        self.assertEquals(0, items[3].sell_in)
        self.assertEquals(80, items[3].quality)

        self.assertEquals("Sulfuras, Hand of Ragnaros", items[4].name)
        self.assertEquals(-1, items[4].sell_in)
        self.assertEquals(80, items[4].quality)

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[5].name)
        self.assertEquals(15, items[5].sell_in)
        self.assertEquals(21, items[5].quality)

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[6].name)
        self.assertEquals(0, items[6].sell_in)
        self.assertEquals(0, items[6].quality)

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[7].name)
        self.assertEquals(5, items[7].sell_in)
        self.assertEquals(49, items[7].quality)

        self.assertEquals("Conjured Mana Cake", items[8].name)
        self.assertEquals(3, items[8].sell_in)
        self.assertEquals(5, items[8].quality)

        self.assertEquals("Conjured Mana Cake", items[9].name)
        self.assertEquals(0, items[9].sell_in)
        self.assertEquals(4, items[9].quality)


if __name__ == '__main__':
    unittest.main()