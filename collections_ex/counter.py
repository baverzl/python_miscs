#!/usr/bin/env python3

from collections import Counter

words = "abcdaajasdkcajskldjklasdfjkl"

counter = Counter()
for c in words:
  counter.update(c)

for key, item in counter.items():
  print(key, item)
