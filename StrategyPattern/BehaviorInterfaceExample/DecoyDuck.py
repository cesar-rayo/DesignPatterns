from StrategyPattern.BehaviorInterfaceExample.Duck import Duck
from StrategyPattern.BehaviorInterfaceExample.QuackBehavior import Silence
from StrategyPattern.BehaviorInterfaceExample.FlyBehavior import FlyNoWay


class DecoyDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
        self.quack_behavior = Silence()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print(f"{self.name} is a Decoy duck!")
