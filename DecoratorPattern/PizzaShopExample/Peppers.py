from DecoratorPattern.PizzaShopExample.ToppingDecorator import ToppingDecorator


class Peppers(ToppingDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription() + ", Peppers"

    def cost(self):
        return self.pizza.cost() + .10
