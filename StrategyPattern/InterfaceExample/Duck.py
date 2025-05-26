from StrategyPattern.InterfaceExample.Flyable import FlyInterface
from StrategyPattern.InterfaceExample.Quackable import QuackInterface


class Duck(FlyInterface, QuackInterface):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f"[ {self.name} ] swims from Duck")

    def display(self):
        print(f"[ {self.name} ] displays from Duck")
