#!/usr/bin/env python3

from functools import singledispatch
from decimal import *
'''
To define a generic function, decorate it with the @singledispatch decorator.
Note that the dispatch happens on the type of the first argument,
create your function accordingly.
'''

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg) 

'''
To add overloaded implementations to the function, use the register()
attribute of the generic function. For functions annotated with types, 
the decorator will infer the type of the first argument automatically:
'''

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg) 

@fun.register 
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem) 

'''
For code which doesn't use type annotations, the appropriate type argument
can be passed explicitly to the decorator itself.
'''

@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)

'''
To enable registering lambdas and pre-existing functions,
the register() attribute can be used in a functional form.
'''

def nothing(arg, verbose=False):
    print("Nothing.")

fun.register(type(None), nothing)

@fun.register(float)
@fun.register(Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)

print(fun("Hello, world."))
print(fun("test.", verbose=True))
print(fun(42, verbose=True))
print(fun(['spam', 'spam', 'eggs', 'spam'], verbose=True))
print(fun(None))
print(fun(1.23))
