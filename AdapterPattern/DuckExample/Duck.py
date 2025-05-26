import abc


class Duck:
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def fly(self):
        pass

    @abc.abstractmethod
    def quack(self):
        pass
