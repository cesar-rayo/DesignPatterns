from DecoratorPattern.CoffeeShopExample.CondimentDecorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .50
