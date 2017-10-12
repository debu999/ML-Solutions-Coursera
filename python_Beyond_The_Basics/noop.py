"""functools.wrap demo"""

def hello():
    """Print a world known value"""
    print("Hello World.")


print(help(hello))
from pprint import pprint as pp

pp(hello.__name__)
pp(dir(hello))

def noop(f):
    def wrap_noop():
        return f()

    wrap_noop.__name__ = f.__name__
    wrap_noop.__doc__ = f.__doc__
    return wrap_noop

@noop
def hello():
    "Print a world known value to test decorator"
    print("Hello World!")


pp(hello.__doc__)
pp(hello.__name__)

import functools
def noop(f):
    @functools.wraps(f)
    def wrap_noop():
        return f()
    return wrap_noop

@noop
def hello():
    "Print a world known value to test decorator"
    print("Hello World!")


pp(hello.__doc__)
pp(hello.__name__)


def check_non_negative(index):
    print(index)
    def validator(f):
        def wraps(*args):
            print (args[index])
            if args[index] < 0:
                raise ValueError("Data sent is less than 0. Only +ve value accepted.")
            return f(*args)
        return wraps
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value]*size

print(create_list('a', 1))
pp(1)
print(create_list('abc', 3))

pp(2)
