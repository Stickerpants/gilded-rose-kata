# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # Sulfuras never changes
                continue

            # Base quality change
            quality_delta = -1

            if item.name == "Aged Brie":
                # Brie increases in quality instead
                quality_delta = 1

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    # Quality drops to zero if the pass is expired
                    quality_delta = 0
                    item.quality = 0
                elif item.sell_in <= 5:
                    # Quality increases by 3 if there's 5 days or less
                    quality_delta = 3
                elif item.sell_in <= 10:
                    # Quality increases by 2 if there's 10 days or less
                    quality_delta = 2
                else:
                    # Otherwise, quality just increases by 1
                    quality_delta = 1

            if item.name == "Conjured Mana Cake":
                # Conjured items degrade twice as fast
                quality_delta *= 2

            if item.sell_in <= 0:
                # If any item is expired, double the rate of quality change
                quality_delta *= 2
            # Update quality, but clamp within acceptable bounds
            item.quality = max(0, min(50, item.quality + quality_delta))
            # This is the same for any item that needs to be sold
            item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
