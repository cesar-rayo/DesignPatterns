import abc
from DecoratorPattern.CoffeeShopExample.Beverage import Beverage


class CondimentDecorator(Beverage):
    @abc.abstractmethod
    def getDescription(self):
        pass
