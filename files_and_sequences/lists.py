string="Mississipi"
print(string[2:4])


str='russia';
print(str.capitalize())

# str = 'Module'
# print(str.index('L'))

list=["Java","R","Python"]
print(list[::-1])

list=["Java", "R", "Python"]
print(list[2])

list.pop()
print(list)

# Get all odd values
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [i for i in list if i % 2 == 0]
print(b)

# Square of all even values
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i**2 for i in list if i % 2 == 0]
print(b)

# Square of all values - filter condition is optional
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i**2 for i in list]
print(b)

# Append value at the end of the list
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.append("New value")
print(list)

# Reverse list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.reverse()
print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list[::-1]
print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.sort(reverse=True)
print(list)

# Combine two lists
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

print(list_1 + list_2)

# Combine two lists using extend()
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_1.extend(list_2)
print(list_1)

# Insert at a specific index
list = [1, 2, 3, 4]
list.insert(4, "Value")
print(list)

# Sort a list
list = [1, 2, 3, 4, 2, -1, 0, 178, 345]
list_b = sorted(list)
print(list_b)

# Sort a list
list = [1, 2, 3, 4, 2, -1, 0, 178, 345]
list.sort()
print(list_b)

# Return entire list minus last item
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list[:-1]
print(list)

# Return last item
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list[-1]
print(list)

# Return every second item
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list[::2]
print(list)

# Square of all even values passed through function


def add(item):
    return f"X{item}"


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [add(i) for i in list if i % 2 == 0]

print(b)


# Get first and last
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 54, 343]
length = len(list)
list = list[::length -1]
print(list)

# Get max item from list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 54, 343]
length = len(list)
max_val = max(list)
print(max_val)

print(type((1, 3)))
