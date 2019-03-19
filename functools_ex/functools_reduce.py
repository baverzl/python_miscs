#!/usr/bin/env python3

from functools import reduce 

def sum(a, b):
    return a + b

print( reduce(sum, [1, 2, 3, 4, 5]) )

from functools import wraps 

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()
print(example.__name__)
print(example.__doc__)
