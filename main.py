from StrategyPattern.InterfaceExample.MallardDuck import MallardDuck as InterfaceExampleMallardDuck
from StrategyPattern.InterfaceExample.DecoyDuck import DecoyDuck as InterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.MallardDuck import MallardDuck as BehaviorInterfaceMallardDuck
from StrategyPattern.BehaviorInterfaceExample.DecoyDuck import DecoyDuck as BehaviorInterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.RubberDuck import RubberDuck as BehaviorInterfaceRubberDuck


def StrategyInterfaceExample():
    mallard_duck = InterfaceExampleMallardDuck("Green Duck")
    mallard_duck.fly()
    mallard_duck.swim()
    mallard_duck.quack()
    decoy_duck = InterfaceDecoyDuck("Wooden Duck")
    decoy_duck.swim()
    decoy_duck.quack()
    # This strategy becomes problematic since each duck class will have to implement quack and fly methods


def StrategyBehaviorInterfaceExample():
    mallard_duck = BehaviorInterfaceMallardDuck("Green Duck")
    mallard_duck.display()
    mallard_duck.performFly()
    mallard_duck.swim()
    mallard_duck.performQuack()

    decoy_duck = BehaviorInterfaceDecoyDuck("Wooden Duck")
    decoy_duck.display()
    decoy_duck.swim()
    decoy_duck.performQuack()

    rubber_duck = BehaviorInterfaceRubberDuck("Yellow Duck")
    rubber_duck.display()
    rubber_duck.performQuack()


if __name__ == '__main__':
    # StrategyInterfaceExample()
    StrategyBehaviorInterfaceExample()
