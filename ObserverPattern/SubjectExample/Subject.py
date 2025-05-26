import abc


class Subject:
    @abc.abstractmethod
    def registerObserver(self, observer):
        pass

    @abc.abstractmethod
    def removeObserver(self, observer):
        pass

    @abc.abstractmethod
    def notifyObservers(self):
        pass
