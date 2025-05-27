from IteratorPattern.CafeExample.DinnerMenu import DinerMenu
from IteratorPattern.CafeExample.PancakeHouseMenu import PancakeHouseMenu


class Cafe:
    def __init__(self):
        self.pancakeHouseMenu = PancakeHouseMenu()
        self.dinerMenu = DinerMenu()

    @staticmethod
    def printMenu(iterator):
        index = 1
        print("==================== Menu ====================")
        while iterator.hasNext():
            menu_item = iterator.next()
            Cafe.print_item(index, menu_item)
            index += 1
        print("==================== End of Menu ====================")

    @staticmethod
    def print_item(index, menu_item):
        print(f"{index}. {menu_item.getName()}: {menu_item.getDescription()} $ {menu_item.getPrice()}")
