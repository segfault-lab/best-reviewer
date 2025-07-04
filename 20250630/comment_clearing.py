# Copyright (C) emilybache, Inc. All right reserved.
# https://github.com/emilybache/GildedRose-Refactoring-Kata

class GildedRose(object):
    """
    Manages a collection of items in a store and updates their properties each day.

    Rules:
        - All items decrease in quality as they age.
        - "Aged Brie" increases in quality over time.
        - "Backstage passes" increase in quality as the concert approaches,
          but drops to 0 after the concert.
        - "Sulfuras" is a legendary item and never decreases in quality or sell_in.

    Methods:
        - update_quality: Updates the quality and sell_in values of all items.
    """
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    # 콘서트 티켓은 판매기한이 0에 수렴할수록 가격이 증가한다.
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

class Item:
    """
    Represents an item in the Gilded Rose store.
    Attributes:
        name (str): The name of the item.
        sell_in (int): The number of days until the item is no longer sellable.
        quality (int): The quality of the item, which can range from 0 to 50.
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
