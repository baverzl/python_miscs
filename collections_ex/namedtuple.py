#!/usr/bin/env python3

from collections import namedtuple 

Account = namedtuple('Account', ['name', 'age', 'sex', 'id'])

acc = Account(name='TonyStark', age=11, sex='M', id='tonystark')
print(acc)
