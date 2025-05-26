from StrategyPattern.InterfaceExample.Duck import Duck


class DecoyDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
