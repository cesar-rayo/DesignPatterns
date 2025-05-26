import abc


class Observer:
    @abc.abstractmethod
    def changeTemperature(self, value):
        pass

    @abc.abstractmethod
    def changeWindSpeed(self, value):
        pass

    @abc.abstractmethod
    def changePressure(self, value):
        pass
