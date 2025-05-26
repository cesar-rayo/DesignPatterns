from AdapterPattern.DuckExample.MallardDuck import MallardDuck
from AdapterPattern.DuckExample.WildTurkey import WildTurkey
from AdapterPattern.DuckExample.TurkeyAdapter import TurkeyAdapter
from AdapterPattern.DuckExample.SuperDrone import SuperDrone
from AdapterPattern.DuckExample.DroneAdapter import DroneAdapter


class DuckSimulator:
    def __init__(self):
        duck = MallardDuck("Green Duck")
        self.testDuck(duck)

        turkey = WildTurkey("Black Turkey")
        # 'WildTurkey' object has no attribute 'quack'
        adapted_turkey = TurkeyAdapter(turkey)
        self.testDuck(adapted_turkey)

        drone = SuperDrone("Grey Drone")
        adapted_drone = DroneAdapter(drone)
        self.testDuck(adapted_drone)

    @staticmethod
    def testDuck(duck):
        duck.quack()
        duck.fly()
