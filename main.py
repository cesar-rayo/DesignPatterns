from StrategyPattern.InterfaceExample.MallardDuck import MallardDuck as InterfaceExampleMallardDuck
from StrategyPattern.InterfaceExample.DecoyDuck import DecoyDuck as InterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.MallardDuck import MallardDuck as BehaviorInterfaceMallardDuck
from StrategyPattern.BehaviorInterfaceExample.DecoyDuck import DecoyDuck as BehaviorInterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.RubberDuck import RubberDuck as BehaviorInterfaceRubberDuck
from StrategyPattern.PhoneCameraApp.CameraPlusApp import CameraPlusApp
from StrategyPattern.PhoneCameraApp.BasicCameraApp import BasicCameraApp
from AdapterPattern.DuckExample.DuckSimulator import DuckSimulator


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


def StrategyCameraApp():
    b_camera = BasicCameraApp("Basic App")
    b_camera.take()
    b_camera.save("pic 1")
    b_camera.share_text()
    b_camera.share_social_media()

    p_camera = CameraPlusApp("Plus App")
    p_camera.take()
    b_camera.save("pic 2")
    b_camera.share_email()
    b_camera.share_social_media()


def AdapterPattern():
    DuckSimulator()


if __name__ == '__main__':
    # StrategyInterfaceExample()
    # StrategyBehaviorInterfaceExample()
    # StrategyCameraApp()
    AdapterPattern()
