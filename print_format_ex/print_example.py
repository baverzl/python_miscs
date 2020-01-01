#!/usr/bin/env python3

import numpy

print('{required} version / {present} version'.format(
    required='1.18.0', present=numpy.__version__))
