from FactoryPattern.CalendarExample.Calendar import Calendar
from FactoryPattern.CalendarExample.ZoneFactory import ZoneFactory


class MountainCalendar(Calendar):
    def __init__(self):
        self.zone = None

    def createCalendar(self):
        self.zone = ZoneFactory.createZone("Mountain")
        self.print()
