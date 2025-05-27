from FactoryPattern.FactoryMethodExample.PizzaStore import PizzaStore
from FactoryPattern.FactoryMethodExample.NYCheesePizza import NYCheesePizza
from FactoryPattern.FactoryMethodExample.NYVeggiePizza import NYVeggiePizza
from FactoryPattern.FactoryMethodExample.NYClamPizza import NYClamPizza
from FactoryPattern.FactoryMethodExample.NYPepperoniPizza import NYPepperoniPizza


class NYStylePizzaStore(PizzaStore):
    def __init__(self):
        self.name = "NY Store"
        self.sold_pizzas = 0

    @staticmethod
    def createPizza(pizza_type):
        if pizza_type == "Cheese":
            return NYCheesePizza()
        elif pizza_type == "Veggie":
            return NYVeggiePizza()
        elif pizza_type == "Clam":
            return NYClamPizza()
        elif pizza_type == "Pepperoni":
            return NYPepperoniPizza()
        else:
            raise Exception(f"Pizza type {pizza_type} not implemented yet")

    def orderPizza(self, pizza_type):
        pizza = NYStylePizzaStore.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        self.sold_pizzas += 1
        return pizza
