import numpy as np

# Create a new array
array = np.array([1, 3, 3, 4])

print(array)

array = np.array((1, 3, 3, 4))

print(array)
print(array*2)

arr1 = np.array([3, 7, 4])
arr2 = np.array([45, 656, 65])
print(arr1 + arr2)

print(np.arange(65))

print(np.arange(65, 90))

print(np.zeros(10))

print((np.zeros(10)).dtype)

print((np.zeros(10, dtype=int)).dtype)

print(np.linspace(10, 1000, 20))

# Printing out docs for a function or object
print(np.arange.__doc__)

