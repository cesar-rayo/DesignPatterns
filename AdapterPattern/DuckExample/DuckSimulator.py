from AdapterPattern.DuckExample.MallardDuck import MallardDuck
from AdapterPattern.DuckExample.WildTurkey import WildTurkey
from AdapterPattern.DuckExample.TurkeyAdapter import TurkeyAdapter


class DuckSimulator:
    def __init__(self):
        duck = MallardDuck("Green Duck")
        self.testDuck(duck)

        turkey = WildTurkey("Black Turkey")
        adapted_turkey = TurkeyAdapter(turkey)
        self.testDuck(adapted_turkey)
        # 'WildTurkey' object has no attribute 'quack'

    @staticmethod
    def testDuck(duck):
        duck.quack()
        duck.fly()
