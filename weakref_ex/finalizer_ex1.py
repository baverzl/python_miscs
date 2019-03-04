#!/usr/bin/env python3

'''
    Finalizer Objects

'''

import weakref
import shutil
import tempfile

class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        print('Temp directory created: {}'.format(self.name))
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive 

temp = TempDir()

