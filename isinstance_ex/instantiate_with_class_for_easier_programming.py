#!/usr/bin/env python3


class Dog:

  def __init__(self, name):
    self.name = name


class Cat:

  def __init__(self, name):
    self.name = name


animals = []
animals.append(Dog('puppy-1'))
animals.append(Cat('kitty'))
animals.append(Dog('puppy-2'))

dogs = [animal for animal in animals if isinstance(animal, Dog)]

for idx, dog in enumerate(dogs):
  print(idx + 1, dog.name)
