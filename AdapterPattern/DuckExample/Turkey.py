import abc


class Turkey:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"{self.name} is a Turkey!")

    @abc.abstractmethod
    def gobble(self):
        pass

    @abc.abstractmethod
    def gobble(self):
        pass
