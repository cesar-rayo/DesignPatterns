from DecoratorPattern.PizzaShopExample.Pizza import Pizza


class ThinCrustPizza(Pizza):
    def __init__(self):
        self.description = "Thin Crust Pizza"

    def cost(self):
        return 1.50
