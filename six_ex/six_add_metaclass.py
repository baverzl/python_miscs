#!/usr/bin/env python3

from six import add_metaclass
from functools import partial

def power(base, exponent):
    return base ** exponent

class PowerMeta(type):
    def __init__(cls, name, bases, dct):

        # generate 50 partial power functions
        for x in range(1, 51):
            
            setattr(
                # cls represents the class
                cls,

                # name the partial
                "p{}".format(x),

                # partials created here
                partial(power, exponent=x)
            )
        
        super(PowerMeta, cls).__init__(name, bases, dct)

@add_metaclass(PowerMeta)
class PowerStructure(object):
    pass

def test_power_structure_object():
    p = PowerStructure()

    # 10 squared 
    assert p.p2(10) == 100

    # 2 to the 5th power
    assert p.p5(2) == 32

    # 2 to the 50th power 
    assert p.p50(2) == 1125899906842624

# Thanks to the power of metaclasses, we don't need to instantiate the PowerStructure class!

def test_power_structure_class():

    # 10 squared
    assert PowerStructure.p2(10) == 100

    # 2 to the 5th power
    assert PowerStructure.p5(2) == 32

    # 2 to the 50th power
    assert PowerStructure.p50(2) == 1125899906842624

print('Calling test_power_structure_object()')
test_power_structure_object()
print('Calling test_power_structure_class()')
test_power_structure_class()