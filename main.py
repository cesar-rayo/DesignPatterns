from StrategyPattern.InterfaceExample.MallardDuck import MallardDuck as InterfaceExampleMallardDuck
from StrategyPattern.InterfaceExample.DecoyDuck import DecoyDuck as InterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.MallardDuck import MallardDuck as BehaviorInterfaceMallardDuck
from StrategyPattern.BehaviorInterfaceExample.DecoyDuck import DecoyDuck as BehaviorInterfaceDecoyDuck
from StrategyPattern.BehaviorInterfaceExample.RubberDuck import RubberDuck as BehaviorInterfaceRubberDuck
from StrategyPattern.PhoneCameraApp.CameraPlusApp import CameraPlusApp
from StrategyPattern.PhoneCameraApp.BasicCameraApp import BasicCameraApp

from AdapterPattern.DuckExample.DuckSimulator import DuckSimulator

from ObserverPattern.SubjectExample.SimpleSubject import SimpleSubject
from ObserverPattern.SubjectExample.Observer import SimpleObserver
from ObserverPattern.WeatherStation.WeatherStation import WeatherStation
from ObserverPattern.WeatherStation.Logger import Logger
from ObserverPattern.WeatherStation.UserInterface import UserInterface
from ObserverPattern.WeatherStation.AlertSystem import AlertSystem

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


def ObserverPattern():
    subject = SimpleSubject()
    observer1 = SimpleObserver("o1", subject)
    observer2 = SimpleObserver("o2", subject)
    observer3 = SimpleObserver("o3", subject)
    observer2.run_process()
    subject.changeValue(2)
    observer1.run_process()
    subject.changeValue(3)
    observer3.run_process()


def ObserverWeatherStation():
    weather_system = WeatherStation()
    ui = UserInterface(weather_system)

    weather_system.changeTemperature("5")
    ui.display()
    logger = Logger(weather_system)
    alert = AlertSystem(weather_system)

    weather_system.changePressure("10")
    alert.alert()

    weather_system.changeWindSpeed("96")
    logger.log()
    ui.display()


if __name__ == '__main__':
    # StrategyInterfaceExample()
    # StrategyBehaviorInterfaceExample()
    # StrategyCameraApp()
    # AdapterPattern()
    # ObserverPattern()
    ObserverWeatherStation()
