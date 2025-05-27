from DecoratorPattern.PizzaShopExample.ToppingDecorator import ToppingDecorator


class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription() + ", Cheese"

    def cost(self):
        return self.pizza.cost() + .50
