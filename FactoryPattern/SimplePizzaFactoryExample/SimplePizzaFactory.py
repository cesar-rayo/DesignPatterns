from FactoryPattern.SimplePizzaFactoryExample.CheesePizza import CheesePizza
from FactoryPattern.SimplePizzaFactoryExample.VeggiePizza import VeggiePizza
from FactoryPattern.SimplePizzaFactoryExample.ClamPizza import ClamPizza
from FactoryPattern.SimplePizzaFactoryExample.PepperoniPizza import PepperoniPizza


class SimplePizzaFactory:
    @staticmethod
    def createPizza(pizza_type):
        if pizza_type == "Cheese":
            return CheesePizza()
        elif pizza_type == "Veggie":
            return VeggiePizza()
        elif pizza_type == "Clam":
            return ClamPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise Exception(f"Pizza type {pizza_type} not implemented yet")
