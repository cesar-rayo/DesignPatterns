from AdapterPattern.DuckExample.Duck import Duck


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def fly(self):
        for i in range(5):
            self.turkey.fly()

    def quack(self):
        self.turkey.gobble()
