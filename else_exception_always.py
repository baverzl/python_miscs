#!/usr/bin/env python3 

a = int(input())

if a < 10:
	print('value smaller than 10')
elif a < 100:
	print('value is in the range of [10, 100)')
else:
	raise ValueError('value should be less than 100')
