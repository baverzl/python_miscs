#!/usr/bin/env python3 

import json 

json_obj = json.loads('[{ "a": 1, "b": 2}, {"c": 3, "d": 4}]')
print(json_obj)
json_obj = json.loads('[{ "0": 1, "1": 2}, {"2": 3, "3": 4}]') # keys have to be in double quotes.
print(json_obj) # is python object
assert type(json_obj) is list
print(json.dumps(json_obj)) # is string
assert type(json.dumps(json_obj)) is str
