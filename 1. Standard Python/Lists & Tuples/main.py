"""
This is a Python Doc String. The Doc string should exist to describe the overall goal of this particular file.
"""

# Traditional Lists
list_ = ["a", "b", "c"]
for i in range(0, len(list_)):  # Iterates through the list indexes
    print(list_[i])
for item in list_:
    print(item)

# Nested Lists
nlist = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]
for i in range(0, len(nlist)):
    for j in range(0, len(nlist[i])):
        print(nlist[i][j])

for lis in nlist:
    for c in lis:
        print(c)

# Traditional Tuples - An immutable list of things
tup = ("a", "b", "c")
for i in range(0, len(tup)):
    print(tup[i])
for item in tup:
    print(item)

# Named tuples examples
from collections import namedtuple

color = namedtuple('color', ['hue', 'saturation', 'brightness'])

p = color(170, 20, 50)
if p.hue > 100:             # instead of p[0]
    print('do something')
if p.saturation <= 50:      # instead of p[1]
    print('do something')