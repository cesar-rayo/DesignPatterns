import abc


class Subject:
    @abc.abstractmethod
    def registerObserver(self):
        pass

    @abc.abstractmethod
    def removeObserver(self):
        pass
