import abc


class Calendar:
    def print(self):
        print(f"Calendar: {self.zone.name}: UTC{self.zone.offset}")

    @abc.abstractmethod
    def createCalendar(self):
        pass
