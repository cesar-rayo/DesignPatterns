import abc


class PizzaStore:
    @abc.abstractmethod
    def createPizza(self):
        pass

    @abc.abstractmethod
    def orderPizza(self):
        pass

    def printStatus(self):
        print(f"The store [{self.name}] has baked: {self.sold_pizzas} Pizzas")
