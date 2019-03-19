#!/usr/bin/env python3

from functools import partialmethod 

'''
Return a new partial method descriptor which behaves like partial
except that it is designed to be used as a method definition rather than being
directly callable.

func must be a descriptor or a callable (objects which are both, like normal functions,
are handled as descriptors).

When func is a descriptor (such as a normal Python function, classmethod(), staticmethod(),
abstractmethod() or another instance of partialmethod), calls to __get__ are delegated to
the underlying descriptor, and an appropriate partial object returned as the result.

WHen func is a non-descriptor callable, an appropriate bound method is created dynamically.
This behaves like a normal Python function when used as a method: the self arguemnt
will be inserted as the first positional argument, even before the args and keywords supplied to the
partialmethod constructor.

'''

class Cell(object):
    def __init__(self):
        self._alive = False
    @property 
    def alive(self):
        return self._alive 
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False) 

c = Cell()
print( c.alive )
c.set_alive()
print( c.alive )