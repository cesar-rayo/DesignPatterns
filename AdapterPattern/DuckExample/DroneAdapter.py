from AdapterPattern.DuckExample.Duck import Duck


class DroneAdapter(Duck):
    def __init__(self, drone):
        self.drone = drone

    def fly(self):
        self.drone.spin_rotors()
        self.drone.take_off()

    def quack(self):
        self.drone.beep()
