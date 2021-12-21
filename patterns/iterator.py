def count_to(count):
    """Iterator Implementation"""
    numbers_in_german = ["eins","zwei","drei","vier","funf"]

    # python built-in iterator
    iterator = zip(range(count), numbers_in_german)
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number


if __name__ == "__main__":
    numbers = count_to(3)
    print(numbers)
    for number in numbers:
        print(number)
