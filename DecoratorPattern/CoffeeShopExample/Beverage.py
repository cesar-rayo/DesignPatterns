import abc


class Beverage:
    def getDescription(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass
