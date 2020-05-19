# If a value is zero or empty, None or False it will appear as boolean False
empty = "a"
if empty:
    print("a")
else:
    print("b")

# Do all values in the collection values equate to True?
all_collection = ["True", 9, 4, 7, 9]
print(all(all_collection))
all_collection = ["False", 9, 4, 7, 9]
print(all(all_collection))


# Do ANY values in the collection values equate to True?
all_collection = [None, 0, [], (), {}, "True", False]
print(any(all_collection))
all_collection = [None, 0, [], (), {}, "", False]
print(any(all_collection))

# Return character for an ASCII Code Point
print(chr(65))

# Print ASCII code point for cha

print(ord("A"))
print(chr(ord("A")+1))

# Global variables defined
dictionary = globals().items()
print(dictionary)


# Sum the values of a collection
my_arr = [3, 5, 56, 89, 4]
print(sum(my_arr))

# Lambda function
out = (lambda a, b: a + b)(100, 400)
print(out)

# Lambda function with list comprehension
my_list = [2, 4, 6, 8]
my_list = [(lambda i: i**2)(i) for i in my_list]
print(my_list)

# Map
my_list = [2, 4, 6, 8]
my_list = list(map(lambda i: i**2, [2, 4, 6, 8]))
print(my_list)

# Filter
print(list(filter(lambda i: i > 3, [2, 4, 6, 8])))

# Pass value from lambda into function
def my_worker(v):
    return v * 200


my_list = list(map(lambda i: my_worker(i), [2, 4, 6, 8]))
print(my_list)

# Globals
a = 200

def my_function():
    global a
    a = 1
    print(a * 200)

my_function()

print(a)

def func(name="default", age=0):
    print(f"{name}  {age}")

func()

func(age=104, name="Paul")

def func_2(*args, **kwargs):
    print(type(args)) # * Unpacks into a tuple
    print(type(kwargs)) # Unpacks into a dictionary

func_2(1, 2, 3, abc="abc", defg="defg")