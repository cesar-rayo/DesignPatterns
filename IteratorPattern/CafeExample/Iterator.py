import abc


class Iterator:
    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def hasNext(self):
        pass
