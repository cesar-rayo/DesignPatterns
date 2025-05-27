from FactoryPattern.CalendarExample.Zone import Zone


class ZoneUSEastern(Zone):
    def __init__(self):
        self.name = "US Eastern"
        self.offset = -5
