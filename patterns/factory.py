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


if __name__ == '__main__':
    d = get_pet("cat")
    print(d.speak())

    d = get_pet("dog")
    print(d.speak())