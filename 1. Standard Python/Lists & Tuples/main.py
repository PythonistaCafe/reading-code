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


# Apply the same behaviour to all items of a list - here add 2 to each number
list_of_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(map((lambda x: x + 2), list_of_int))
# new_list = [3, 4, 5, 6, 7, 8, 9, 10, 11]
