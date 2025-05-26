class QuackBehaviorInterface:
    def quack(self):
        print(f"> Method not implemented")


class Quack(QuackBehaviorInterface):
    def quack(self):
        print(f"Quak!")


class Squeak(QuackBehaviorInterface):
    def quack(self):
        print(f"Squeak!")


class Silence(QuackBehaviorInterface):
    def quack(self):
        print(f"....")
