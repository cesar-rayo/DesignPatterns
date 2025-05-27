from FactoryPattern.CalendarExample.Zone import Zone


class ZoneUSCentral(Zone):
    def __init__(self):
        self.name = "US Central"
        self.offset = -6
