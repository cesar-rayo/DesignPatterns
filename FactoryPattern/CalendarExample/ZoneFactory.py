from FactoryPattern.CalendarExample.ZoneUSCentral import ZoneUSCentral
from FactoryPattern.CalendarExample.ZoneUSEastern import ZoneUSEastern
from FactoryPattern.CalendarExample.ZoneUSMountain import ZoneUSMountain
from FactoryPattern.CalendarExample.ZoneUSPacific import ZoneUSPacific


class ZoneFactory:
    @staticmethod
    def createZone(zone):
        if zone == "Central":
            return ZoneUSCentral()
        elif zone == "Eastern":
            return ZoneUSEastern()
        elif zone == "Mountain":
            return ZoneUSMountain()
        elif zone == "Pacific":
            return ZoneUSPacific()
        else:
            raise Exception(f"Time Zone [{zone}] not supported yet")
