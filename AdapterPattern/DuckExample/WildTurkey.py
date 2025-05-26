from AdapterPattern.DuckExample.Turkey import Turkey


class WildTurkey(Turkey):
    def __init__(self, name):
        super().__init__(name)

    def gobble(self):
        print(f"{self.name} gobbles like a Wild Turkey!")

    def fly(self):
        print(f"{self.name} flies like a Wild Turkey!")
