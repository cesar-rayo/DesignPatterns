import abc


class Duck:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f"[ {self.name} ] swims from Duck")

    @abc.abstractmethod
    def display(self):
        pass

    def performFly(self):
        print(f"[ {self.name} ] tries to fly: ")
        self.fly_behavior.fly()

    def performQuack(self):
        print(f"[ {self.name} ] tries to quack:")
        self.quack_behavior.quack()
