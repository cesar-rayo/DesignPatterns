from DecoratorPattern.CoffeeShopExample.Beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return .80
