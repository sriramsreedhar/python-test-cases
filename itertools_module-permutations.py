#!/usr/bin/python
items=['a','b','c']
from itertools import permutations
for p in permutations(items):
 print(p)
