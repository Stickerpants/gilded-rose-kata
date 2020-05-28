# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [Item("cupcake", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Item name shouldn't change
        self.assertEqual("cupcake", items[0].name)
        # Sell-In should decrease as expected
        self.assertEqual(-1, items[0].sell_in)
        # Quality can't be negative
        self.assertEqual(0, items[0].quality)
        # Items shouldn't magically duplicate or disappear
        self.assertEqual(1, len(items))

    def test_multiple_foo(self):
        items = [Item("cupcake", 0, 0), Item("cupcake", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Ensure all items are processed, if there are multiple
        for i in items:
            self.assertEqual(-1, i.sell_in)

    def test_quality_degrades(self):
        items = [Item("cupcake", 1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Quality decreases by 1 every day
        self.assertEqual(2, items[0].quality)

        gilded_rose.update_quality()
        # until an item expires, then the rate is doubled
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 1, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Brie increases in quality as it gets older
        self.assertEqual(48, items[0].quality)

        gilded_rose.update_quality()
        # doubling in speed once it expires
        self.assertEqual(50, items[0].quality)

        gilded_rose.update_quality()
        # but cannot exceed 50
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80), Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Sulfuras should never expire, and never change in quality. It's a legendary!
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(80, items[1].quality)

    def test_backstage_passes_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Backstage passes get more valuable
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # With <=10 days to sell, quality increases by 2
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # With <=5 days to sell, quality increases by 3
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_4(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # If sell_in is negative, then backstage passes become worthless
        self.assertEqual(23, items[0].quality)

        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        for _ in range(2):
            gilded_rose.update_quality()

        # Quality can't grow beyond 50
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
