import abc


class Drone:
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def beep(self):
        pass

    @abc.abstractmethod
    def spin_rotors(self):
        pass

    @abc.abstractmethod
    def take_off(self):
        pass
