from StrategyPattern.InterfaceExample.MallardDuck import MallardDuck
from StrategyPattern.InterfaceExample.DecoyDuck import DecoyDuck


def StrategyInterfaceExample():
    mallard_duck = MallardDuck("Green Duck")
    mallard_duck.fly()
    mallard_duck.swim()
    mallard_duck.quack()
    decoy_duck = DecoyDuck("Wood Duck")
    decoy_duck.swim()
    decoy_duck.quack()
    # This strategy becomes difficult to maintain since each duck class will have to implement quack and fly methods


if __name__ == '__main__':
    StrategyInterfaceExample()
