#!/usr/bin/env python3 

list_to_check = [True for _ in range(3)]

# check if all are true.
print(all(list_to_check))

list_to_check[1] = False

print(all(list_to_check))

list_to_check = [False for _ in range(3)]

# check if any is true.
print(any(list_to_check))

list_to_check[1] = True 

print(any(list_to_check))
