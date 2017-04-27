#!/usr/bin/python
items=['aa','bb','cc']
from itertools import combinations
for c in combinations(items,2):
	print(c)
