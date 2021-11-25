from patterns.factory import get_pet

if __name__ == '__main__':

    d = get_pet("cat")
    print(d.speak())

    d = get_pet("dog")
    print(d.speak())

