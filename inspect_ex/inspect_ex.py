#!/usr/bin/env python3

import os
import inspect
import modules

# directory where the file exists
print(os.path.dirname(inspect.getfile(modules)))
# parent of the directory
print(os.path.dirname(os.path.dirname(inspect.getfile(modules))))
print(os.path.basename(inspect.getfile(modules)))
print(os.path.splitext(os.path.basename(inspect.getfile(modules))))
print(os.path.splitext(os.path.basename(inspect.getfile(modules)))[0])
