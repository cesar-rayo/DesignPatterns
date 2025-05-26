from StrategyPattern.InterfaceExample.Duck import Duck


class MallardDuck(Duck):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"[ {self.name} ] flies from MallardDuck")

    def quack(self):
        print(f"[ {self.name} ] quacks from MallardDuck")
