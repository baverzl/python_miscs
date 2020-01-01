#!/usr/bin/env python3 

import functools

def add(a, b):
	return a + b

# providing default values for parameters
add = functools.partial(add, b=3)
print(add(1))
