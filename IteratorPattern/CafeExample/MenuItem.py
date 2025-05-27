class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
