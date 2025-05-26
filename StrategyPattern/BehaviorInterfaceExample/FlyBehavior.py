class FlyBehaviorInterface:
    def fly(self):
        print(f"> Method not implemented")


class FlyWithWings(FlyBehaviorInterface):
    def fly(self):
        print(f"fly with wings")


class FlyNoWay(FlyBehaviorInterface):
    def fly(self):
        print(f"can't fly")
