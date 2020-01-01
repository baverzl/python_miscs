#!/usr/bin/env python3 

import abc
import six
from six import with_metaclass
from datetime import datetime 

# Below two lines could be replaced with:
#@six.add_metaclass(abc.ABCMeta)
#class AbstractCounter(object):
class AbstractCounter(with_metaclass(abc.ABCMeta)):

	def __init__(self):
		self.step = 0

	@staticmethod
	def _validate_time(curtime): # NOTE: staticmethod does not require `self` argument.
		if curtime > datetime(2030, 1, 1):
			raise ValueError('Current time should be before year 2030')

	@abc.abstractmethod
	def __call__(self, count):
		raise NotImplementedError('AbstractCounter implementation must override __call__')

	def __str__(self):
		return str(self.step)

	def increment(self):
		self.step += 1

class Watch(AbstractCounter):

	def __init__(self):
		super(Watch, self).__init__()

		self._validate_time(datetime.now()) # inherit from the abstract class.

	def __call__(self, count):
		for _ in range(count):
			self.increment()
			print(self)


watch = Watch()
watch(10)
