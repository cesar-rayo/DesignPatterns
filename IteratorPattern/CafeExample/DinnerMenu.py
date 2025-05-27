from IteratorPattern.CafeExample.Menu import Menu
from IteratorPattern.CafeExample.MenuItem import MenuItem
from IteratorPattern.CafeExample.DinerIterator import DinerIterator


class DinerMenu(Menu):
    MAX_ITEMS = 6

    def __init__(self):
        self.menu_items = [None, None, None, None, None, None]
        self.number_of_items = 0
        self.addItem("Vegetarian BLT",
                     "(Fakin') Bacon with lettuce & tomato on whole wheat",
                     True,
                     2.99)
        self.addItem("BLT",
                     "Bacon with lettuce & tomato on whole wheat",
                     False,
                     2.99)
        self.addItem("Soup of the day",
                     "Soup of the day, with a side of potato salad",
                     False,
                     3.29)
        self.addItem("Hotdog",
                     "A hot dog, with saurkraut, relish, onions, topped with cheese",
                     False,
                     3.05)
        self.addItem("Steamed Veggies and Brown Rice",
                     "Steamed vegetables over brown rice",
                     True,
                     3.99)
        self.addItem("Pasta",
                     "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
                     True,
                     3.89)

    def addItem(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        if self.number_of_items >= DinerMenu.MAX_ITEMS:
            print("Menu is fill, can't add item to menu")
        else:
            self.menu_items[self.number_of_items] = menu_item
            self.number_of_items += 1

    def getMenuItems(self):
        return self.menu_items

    def createIterator(self):
        return DinerIterator(self.menu_items)
