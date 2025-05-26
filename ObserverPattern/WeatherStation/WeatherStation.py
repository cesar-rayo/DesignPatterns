from ObserverPattern.WeatherStation.Subject import Subject


class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.wind_speed = 0
        self.pressure = 0

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def changeTemperature(self, value):
        print(f"Changed Temperature from {self.temperature} to {value}")
        self.temperature = value
        for observer in self.observers:
            observer.changeTemperature(value)

    def changeWindSpeed(self, value):
        print(f"Changed Wind Speed from {self.wind_speed} to {value}")
        self.wind_speed = value
        for observer in self.observers:
            observer.changeWindSpeed(value)

    def changePressure(self, value):
        print(f"Changed Pressure from {self.pressure} to {value}")
        self.pressure = value
        for observer in self.observers:
            observer.changePressure(value)

