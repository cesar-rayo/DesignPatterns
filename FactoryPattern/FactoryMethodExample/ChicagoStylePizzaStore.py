from FactoryPattern.FactoryMethodExample.PizzaStore import PizzaStore
from FactoryPattern.FactoryMethodExample.ChicagoCheesePizza import ChicagoCheesePizza
from FactoryPattern.FactoryMethodExample.ChicagoVeggiePizza import ChicagoVeggiePizza
from FactoryPattern.FactoryMethodExample.ChicagoClamPizza import ChicagoClamPizza
from FactoryPattern.FactoryMethodExample.ChicagoPepperoniPizza import ChicagoPepperoniPizza


class ChicagoStylePizzaStore(PizzaStore):
    def __init__(self):
        self.name = "Chicago Store"
        self.sold_pizzas = 0

    @staticmethod
    def createPizza(pizza_type):
        if pizza_type == "Cheese":
            return ChicagoCheesePizza()
        elif pizza_type == "Veggie":
            return ChicagoVeggiePizza()
        elif pizza_type == "Clam":
            return ChicagoClamPizza()
        elif pizza_type == "Pepperoni":
            return ChicagoPepperoniPizza()
        else:
            raise Exception(f"Pizza type {pizza_type} not implemented yet")

    def orderPizza(self, pizza_type):
        pizza = ChicagoStylePizzaStore.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        self.sold_pizzas += 1
        return pizza
