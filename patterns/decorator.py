from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    @wraps(function)
    def decorator():
        ret = function()
        return "<blink>" + ret + "</blink>"
        pass

    return decorator


def hello_world_original():
    """Original function"""
    return "Hello, World!"


@make_blink
def hello_world():
    """Original function"""
    return "Hello, World!"


if __name__ == '__main__':
    print(hello_world_original())
    print(hello_world())
