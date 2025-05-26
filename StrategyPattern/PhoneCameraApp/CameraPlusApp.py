from StrategyPattern.PhoneCameraApp.PhoneCameraApp import PhoneCameraApp


class CameraPlusApp(PhoneCameraApp):
    def __init__(self, name):
        super().__init__(name)

    def edit(self):
        print(f"{self.name} CameraPlusApp edit")
