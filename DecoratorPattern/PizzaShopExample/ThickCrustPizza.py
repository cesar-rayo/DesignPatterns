from DecoratorPattern.PizzaShopExample.Pizza import Pizza


class ThickCrustPizza(Pizza):
    def __init__(self):
        self.description = "Thick Crust Pizza"

    def cost(self):
        return 1.60
