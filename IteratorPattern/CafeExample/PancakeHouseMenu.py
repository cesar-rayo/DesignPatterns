from IteratorPattern.CafeExample.Menu import Menu
from IteratorPattern.CafeExample.MenuItem import MenuItem
from IteratorPattern.CafeExample.PancakeHouseIterator import PancakeHouseIterator


class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.addItem("K&B's Pancake Breakfast",
                     "Pancakes with scrambled eggs, and toast",
                     True,
                     2.99)
        self.addItem("Regular Pancake Breakfast",
                     "Pancakes with fried eggs, sausage",
                     False,
                     2.99)
        self.addItem("Blueberry Pancakes",
                     "Pancakes made with fresh blueberries, and blueberry syrup",
                     True,
                     3.49)
        self.addItem("Waffles",
                     "Waffles, with your choice of blueberries or strawberries",
                     True,
                     3.59)

    def addItem(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def getMenuItems(self):
        return self.menu_items

    def createIterator(self):
        return PancakeHouseIterator(self.menu_items)
