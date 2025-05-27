from DecoratorPattern.PizzaShopExample.ToppingDecorator import ToppingDecorator


class Olives(ToppingDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription() + ", Olives"

    def cost(self):
        return self.pizza.cost() + .20
