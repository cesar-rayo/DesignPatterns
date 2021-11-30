import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        # updates attributes
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.model = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{}|{}|{}".format(self.model, self.color, self.options)


if __name__ == '__main__':
    c1 = Car()
    prototype = Prototype()
    prototype.register_object("first_car", c1)

    c2 = prototype.clone("first_car", model="Mustang", color="Blue", options="None")

    print(c1)
    print(c2)
