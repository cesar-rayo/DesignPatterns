from ObserverPattern.WeatherStation.Observer import Observer


class UserInterface(Observer):
    def __init__(self, subject):
        self.temperature = 0
        self.wind_speed = 0
        self.pressure = 0
        self.subject = subject
        self.subject.registerObserver(self)

    def changeTemperature(self, value):
        self.temperature = value

    def changeWindSpeed(self, value):
        self.wind_speed = value

    def changePressure(self, value):
        self.pressure = value

    def display(self):
        print("=================== UI ===================")
        print("UI - The conditions are:")
        print(f"Temperature: {self.temperature}")
        print(f"Wind Speed: {self.wind_speed}")
        print(f"Pressure: {self.pressure}")
        print("=================== UI ===================")
