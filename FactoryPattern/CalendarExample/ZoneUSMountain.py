from FactoryPattern.CalendarExample.Zone import Zone


class ZoneUSMountain(Zone):
    def __init__(self):
        self.name = "US Mountain"
        self.offset = -7
