#!/usr/bin/env python3 

from functools import partial 

'''
The partial() is used for partial function application which "freezes"
some portion of a function's arguments and/or keywords resulting in a new object
with a simplified signature. For example, partial() can be used to 
create a callable that behaves like the int() function where the base argument defaults to two.
'''

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print( basetwo('10010') )

def power(base, exponent):
    return base ** exponent

def square(base):
    return power(base, 2)

def cube(base):
    return power(base, 3)

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

def test_partials():
    assert square(2) == 4
    assert cube(2) == 8

def test_partial_docs():
    assert square.keywords == {"exponent": 2}
    assert square.func == power

    assert cube.keywords == {"exponent": 3}
    assert cube.func == power

test_partials()
test_partial_docs()