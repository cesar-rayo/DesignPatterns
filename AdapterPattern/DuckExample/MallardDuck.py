from AdapterPattern.DuckExample.Duck import Duck


class MallardDuck(Duck):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(f"{self.name} is a Mallard duck!")

    def fly(self):
        print(f"{self.name} flies")

    def quack(self):
        print(f"{self.name} quacks")
