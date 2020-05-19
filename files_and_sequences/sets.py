my_set = {1, 2, 3, 1}
my_set_2 = {7, 33, 83, 881}
print(my_set)

# Union of two sets
union_set = my_set | my_set_2
print(union_set)

# Intersection - What is common in both sets
# Union of two sets
my_set = {1, 2, 3, 1}
my_set_2 = {7, 33, 83, 881, 1, 3}
intersection_set = my_set & my_set_2
print(intersection_set)

# Difference
my_set = {1, 2, 3, 1}
my_set_2 = {1, 2, 3, 1, 9}

# All the items in set one are in set two so there is nothing returned
# What items are in set A that are not in set B
difference_set = my_set - my_set_2
print(difference_set)

# Set two has one difference (9) so it is returned
difference_set = my_set_2 - my_set
print(difference_set)

# Will throw an error because 110 is not present
my_set = {1, 2, 3, 1}

try:
 my_set.remove(110)
except Exception as e:
    pass

# Same as remove but it will not throw exception
my_set.discard(110)
