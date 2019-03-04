#!/usr/bin/env python3

'''
    Finalizer Objects

'''

# The main benefit of using finalize is that it makes it simple to register a callback
# without needing to preserve the returned finalizer object. For instance

import weakref

class Object:
    pass

baverzl = Object()
weakref.finalize(baverzl, print, "You killed baverzl!")
del baverzl

# The finalizer can be called directly as well. However, the finalizer will invoke the callback at most once.
def callback(x, y, z):
    print('CALLBACK')
    return x + y + z

obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
assert f.alive
assert f() == 6

assert not f.alive
f()          # callback not called because finalizer dead
del obj      # callback not called because finalizer dead

# You can unregister a finalizer using its detach() method. This kills the finalizer and returns the arguments passed
# to the constructor when it was created.
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
f.detach()
newobj, func, args, kwargs = _
assert not f.alive
assert newobj is obj
assert func(*args, **kwargs) == 6

# Unless you set the atexit attribute to False, a finalizer will be called when the program exits if it is still alive. For instance 
obj = Object()
weakref.finalize(obj, print, "obj dead or exiting")
exit()

