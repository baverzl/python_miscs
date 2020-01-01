#!/usr/bin/env python3
"""

    There are strong references and weak references to an object.

    It the only remaining references to a referent are weak references,
    garbage collection is free to destroy the referent and reuse its memory
    for something else. (the term referent means the object which is referred to by a weak reference)

    A primary use for weak references is to implement caches or mappings holding large objects.
    where it's desired that a large object not be kept alive solely because it appears in a cache or mapping. 

    WeakDictionary and WeakValueDictionary use weak references in their implementation, setting up callback
    functions on the weak references that notify the weak dictionaries when a key or value has been reclaimed by
    garbage collection. 

    WeakSet implements the set interface, but keeps weak references to its elements, just like a
    WeakKeyDictionary does.

    Most programs should find that using one of these weak container types or finalize is all they need -- it's not
    usually necessary to create your own weak references directly. The low-level machinery is exposed by the
    weakref module for the benefit of advanced uses.

"""

# Weak Reference Objects
import weakref


class Object:
  pass


o = Object()
r = weakref.ref(o)
o2 = r()
o is o2

# If the referent no longer exists, calling the reference object returns None
del o, o2
print(r())

# Testing that a weak reference object is still live should be done using the expression ref() is not None.
# Normally, application code that needs to use a reference object should follow this pattern.

# r is a weak reference object
o = r()
if o is None:
  # referent has been garbage collected
  print('Object has been deallocated; can\'t frobnicate.')
else:
  print('Object is still live!')
  # o.do_something_useful()


# This example shows how a subclass of ref can be used to store additional information about an object
# and affect the value that's returned when the referent is accessed.
class ExtendedRef(weakref.ref):

  def __init__(self, ob, callback=None, **annotations):
    super(ExtendedRef, self).__init__(ob, callback)
    self.__counter = 0
    for k, v in annotations.items():
      setattr(self, k, v)

  def __call__(self):
    """Return a pair containing the referent and the number of
        times the reference has been called.
        """
    ob = super(ExtendedRef, self).__call__()
    if ob is not None:
      self.__counter += 1
      ob = (ob, self.__counter)
    return ob


o = Object()
r = ExtendedRef(o)
for i in range(4):
  o_tmp, count = r()
  print(count)

# Example
# This simple example shows how an application can use object IDs to retrieve objects that it has seen
# before. The IDs of the objects can then be used in other data structures without forcing the objects
# to remain alive, but the objects can still be retrieved by ID if they do.

_id2obj_dict = weakref.WeakValueDictionary()


def remember(obj):
  oid = id(obj)
  _id2obj_dict[oid] = obj
  return oid


def id2obj(oid):
  return _id2obj_dict[oid]


# Module destructor

import sys


def unloading_module():
  # implicit reference to the module globals() from the function body
  print('unloading...')


weakref.finalize(sys.modules[__name__], unloading_module)
