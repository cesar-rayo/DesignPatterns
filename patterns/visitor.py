class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    """Abstract Visitor"""
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor"""
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    """Concrete visitor"""
    def visit(self, house):
        house.work_on_electricity(self)


if __name__ == "__main__":
    hv = HvacSpecialist()
    e = Electrician()

    h = House()
    h.accept(hv)
    h.accept(e)


