from FactoryPattern.FactoryMethodExample.Pizza import Pizza


class ChicagoVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Veggie Pizza"
