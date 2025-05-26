from StrategyPattern.BehaviorInterfaceExample.Duck import Duck
from StrategyPattern.BehaviorInterfaceExample.QuackBehavior import Squeak
from StrategyPattern.BehaviorInterfaceExample.FlyBehavior import FlyNoWay


class RubberDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
        self.quack_behavior = Squeak()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print(f"{self.name} is a Decoy duck!")
