import abc
from DecoratorPattern.PizzaShopExample.Pizza import Pizza


class ToppingDecorator(Pizza):
    @abc.abstractmethod
    def getDescription(self):
        pass
