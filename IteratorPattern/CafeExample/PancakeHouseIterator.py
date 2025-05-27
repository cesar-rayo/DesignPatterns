from IteratorPattern.CafeExample.Iterator import Iterator


class PancakeHouseIterator(Iterator):
    def __init__(self, items_list):
        self.menu = items_list
        self.position = 0

    def next(self):
        menu_item = self.menu[self.position]
        self.position += 1
        return menu_item

    def hasNext(self):
        return self.position < len(self.menu)
