from DecoratorPattern.CoffeeShopExample.CondimentDecorator import CondimentDecorator


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return self.beverage.cost() + .10
