from StrategyPattern.BehaviorInterfaceExample.Duck import Duck
from StrategyPattern.BehaviorInterfaceExample.QuackBehavior import Quack
from StrategyPattern.BehaviorInterfaceExample.FlyBehavior import FlyWithWings


class MallardDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print(f"{self.name} is a Mallard duck!")
