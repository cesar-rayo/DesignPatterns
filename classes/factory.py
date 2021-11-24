class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """Factory Method"""
    pets = dict(cat=Cat("Peace"), dog=Dog("Hope"))
    return pets[pet]
