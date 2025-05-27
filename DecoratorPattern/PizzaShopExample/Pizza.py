import abc


class Pizza:
    def getDescription(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass
