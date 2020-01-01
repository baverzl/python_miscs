#!/usr/bin/env python3

class A:
	a = 1
	b = 2
	c = 3

print(getattr(A, 'a'))
print(hasattr(A, 'a'))
delattr(A, 'a')
assert not hasattr(A, 'a')
