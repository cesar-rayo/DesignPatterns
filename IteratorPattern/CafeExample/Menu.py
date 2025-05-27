import abc


class Menu:
    @abc.abstractmethod
    def createIterator(self):
        pass
