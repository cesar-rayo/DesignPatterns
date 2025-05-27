from FactoryPattern.SimplePizzaFactoryExample.SimplePizzaFactory import SimplePizzaFactory


class PizzaStore:
    @staticmethod
    def orderPizza(pizza_type):
        pizza = SimplePizzaFactory.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
