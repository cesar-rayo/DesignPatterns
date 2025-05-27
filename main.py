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

from DecoratorPattern.CoffeeShopExample.DarkRoast import DarkRoast
from DecoratorPattern.CoffeeShopExample.HouseBlend import HouseBlend
from DecoratorPattern.CoffeeShopExample.Milk import Milk
from DecoratorPattern.CoffeeShopExample.Mocha import Mocha
from DecoratorPattern.CoffeeShopExample.Whip import Whip
from DecoratorPattern.CoffeeShopExample.Soy import Soy
from DecoratorPattern.PizzaShopExample.ThinCrustPizza import ThinCrustPizza
from DecoratorPattern.PizzaShopExample.ThickCrustPizza import ThickCrustPizza
from DecoratorPattern.PizzaShopExample.Cheese import Cheese
from DecoratorPattern.PizzaShopExample.Peppers import Peppers
from DecoratorPattern.PizzaShopExample.Olives import Olives

from IteratorPattern.CafeExample.Cafe import Cafe

from FactoryPattern.SimplePizzaFactoryExample.PizzaStore import PizzaStore
from FactoryPattern.FactoryMethodExample.ChicagoStylePizzaStore import ChicagoStylePizzaStore
from FactoryPattern.FactoryMethodExample.NYStylePizzaStore import NYStylePizzaStore
from FactoryPattern.CalendarExample.PacificCalendar import PacificCalendar
from FactoryPattern.CalendarExample.MountainCalendar import MountainCalendar


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


def DecoratorCoffeeShop():
    beverage1 = DarkRoast()
    beverage1 = Mocha(beverage1)
    beverage1 = Milk(beverage1)
    beverage1 = Whip(beverage1)
    print(f"beverage1: {beverage1.getDescription()} ${beverage1.cost()}")

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    beverage2 = Soy(beverage2)
    beverage2 = Whip(beverage2)
    beverage2 = Whip(beverage2)
    beverage2 = Whip(beverage2)
    print(f"beverage1: {beverage2.getDescription()} ${beverage2.cost()}")


def DecoratorPizzaShop():
    pizza1 = ThickCrustPizza()
    pizza1 = Cheese(pizza1)
    pizza1 = Cheese(pizza1)
    pizza1 = Peppers(pizza1)
    print(f"pizza1: {pizza1.getDescription()} ${pizza1.cost()}")

    pizza2 = ThinCrustPizza()
    pizza2 = Cheese(pizza2)
    pizza2 = Olives(pizza2)
    pizza2 = Peppers(pizza2)
    print(f"pizza2: {pizza2.getDescription()} ${pizza2.cost()}")

    pizza3 = ThickCrustPizza()
    pizza3 = Cheese(pizza3)
    pizza3 = Cheese(pizza3)
    print(f"pizza3: {pizza3.getDescription()} ${pizza3.cost()}")


def IteratorCafeExample():
    cafe = Cafe()
    cafe.printMenu(cafe.dinerMenu.createIterator())
    cafe.printMenu(cafe.pancakeHouseMenu.createIterator())


def FactoryPizzaStore():
    pizza_store = PizzaStore()
    pizza_store.orderPizza("Cheese")
    pizza_store.orderPizza("Veggie")
    pizza_store.orderPizza("Clam")


def FactoryMethodPizzaStore():
    chicago_store = ChicagoStylePizzaStore()
    chicago_store.orderPizza("Cheese")
    chicago_store.orderPizza("Pepperoni")

    ny_store = NYStylePizzaStore()
    ny_store.orderPizza("Veggie")
    ny_store.orderPizza("Clam")
    ny_store.orderPizza("Cheese")
    ny_store.orderPizza("Clam")

    chicago_store.printStatus()
    ny_store.printStatus()


def FactoryCalendarExample():
    p_calendar = PacificCalendar()
    p_calendar.createCalendar()
    m_calendar = MountainCalendar()
    m_calendar.createCalendar()


if __name__ == '__main__':
    # StrategyInterfaceExample()
    # StrategyBehaviorInterfaceExample()
    # StrategyCameraApp()
    # AdapterPattern()
    # ObserverPattern()
    # ObserverWeatherStation()
    # DecoratorCoffeeShop()
    # DecoratorPizzaShop()
    # IteratorCafeExample()
    # FactoryPizzaStore()
    # FactoryMethodPizzaStore()
    FactoryCalendarExample()
