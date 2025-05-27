from FactoryPattern.FactoryMethodExample.Pizza import Pizza


class NYVeggiePizza(Pizza):
    def __init__(self):
        self.name = "NY Veggie Pizza"
