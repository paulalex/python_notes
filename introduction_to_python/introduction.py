# This is a comment


def get_value():
    """This is a comment inside a function"""
    return "Value"

# Variable types

# Immutable Types - Number, String, Tuple


name = "Paul"  # A String
age = 40  # An integer type
score = 87.45  # A floating point value
hex_value = 0xFF  # A hex value
a_tuple = (1, 2.0, "Three")  # A Tuple, can contain mixed data types

print(hex_value)
print(type(hex_value))

# Mutable Types


my_list = [1]  # A list (array)
my_set = {1, 2, 3}  # A set
converted_list = set(my_list)

print(2**4)

if True & False:
    print("Its bitwise")

if True & True:
    print("Definitely bitwise")

if True and False:
    print("Is it")

a = "Paul"
b = "Paul"

print(a == b)
print(a is b)
print(f"a={id(a)}, b={id(b)}")

x = 10
print(id(x))
x = x + 10
print(id(x))
z = 10
print(id(z))

list_with_dupes = [1, 2, 3, 4, 1, 3]
set_no_dupes = set(list_with_dupes)
print(set_no_dupes)

for i in range(1, 5):
    print(i)

a = True
b = False

print(id(a))
print(id(True))
print(id(b))
print(id(False))

while a:
    print("Hello")
    a = False

val = input("Give me a value: ")
print(f"You entered {val}")

guessed = False
number = 99
while not guessed:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("You won!")
    else:
        print("Guess again...")
