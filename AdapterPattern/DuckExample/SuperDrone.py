from AdapterPattern.DuckExample.Drone import Drone


class SuperDrone(Drone):
    def __init__(self, name):
        super().__init__(name)

    def beep(self):
        print(f"{self.name} Beep beep beep")

    def spin_rotors(self):
        print(f"{self.name} rotors are spinning")

    def take_off(self):
        print(f"{self.name} Taking off")
