my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set, len(my_set))
# Sets cannot have duplicates. They will ignore any duplicate values

my_set.discard(3)
print(my_set)

my_set.clear()
print(my_set)

my_set.update([6, 4, 2, 3])
print(my_set)


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple, len(my_tuple))
