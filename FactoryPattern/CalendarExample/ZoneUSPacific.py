from FactoryPattern.CalendarExample.Zone import Zone


class ZoneUSPacific(Zone):
    def __init__(self):
        self.name = "US Pacific"
        self.offset = -8
