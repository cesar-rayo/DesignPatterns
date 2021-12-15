class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    def __init__(self):
        self.name = "British"

    # Note the method name is different than the one in Korean class
    def speak_english(self):
        return "Hello"


class Adapter:
    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


if __name__ == '__main__':
    objects = []
    korean = Korean()
    british = British()
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(british, speak=british.speak_english))
    for obj in objects:
        print("{} says '{}'".format(obj.name, obj.speak()))
