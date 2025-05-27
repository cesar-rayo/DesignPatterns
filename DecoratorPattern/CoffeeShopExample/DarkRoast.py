from DecoratorPattern.CoffeeShopExample.Beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return .99
