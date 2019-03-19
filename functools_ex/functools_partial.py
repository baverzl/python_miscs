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

