#!/usr/bin/python3

from distutils.version import LooseVersion, StrictVersion
import numpy

# built-in but undocumented and conformant only to the superseded PEP 386

print(LooseVersion(numpy.__version__) >= LooseVersion('1.18.0'))
print(LooseVersion('1.0.0a'))

print(StrictVersion('1.0.0'))
print(StrictVersion('1.0.0a')) # Invalid format
