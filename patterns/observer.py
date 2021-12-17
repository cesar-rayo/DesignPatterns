class Subject(object):
    """Represents what is being 'observed'"""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        else:
            print("Observer already in the list")

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError as err:
            print("There was an error: {}".format(err))

    def notify(self, modifier=None):
        for observer in self._observers:
            # Do not notify the observer who's making the change
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:
    """Observer class"""
    def update(self, subject):
        """Method invoked each time the temp changes"""
        print("Temperature viewer: {} has Temperature {}".format(subject._name, subject._temp))


if __name__ == "__main__":
    c1 = Core("Core1")
#    c2 = Core("Core2")

    v1 = TempViewer()
    v2 = TempViewer()
    v3 = TempViewer()

    c1.attach(v1)
    c1.attach(v2)
    c1.attach(v3)

    c1.temp = 80

#   Remove observer from the list
    c1.detach(v3)
    c1.temp = 90
