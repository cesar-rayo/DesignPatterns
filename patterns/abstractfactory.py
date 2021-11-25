class Dog:
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    def get_pet(self):
        """Returns Dog object"""
        return Dog()

    def get_food(self):
        """Returns Dog Food object"""
        return "Dog Food!"

class Cat:
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


class CatFactory:
    def get_pet(self):
        """Returns Cat object"""
        return Cat()

    def get_food(self):
        """Returns Cat Food object"""
        return "Cat Food!"


class PetStore:

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


if __name__ == '__main__':
    factory = DogFactory()
    shop = PetStore(factory)
    shop.show_pet()

    factory = CatFactory()
    shop = PetStore(factory)
    shop.show_pet()

