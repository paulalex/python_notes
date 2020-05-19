my_string = "A new string"

print(len(my_string))

print(my_string[::-1])

print(my_string[0::len(my_string) - 1])

# name = str(input("Enter your name: "))
# grade = int(input("Enter your grade: "))
# print("My name is %s and my grade is %s" % (name, grade))
# print("My name is {0} and my grade is {1}".format(name, grade))
# print(f"My name is {name} and my grade is {grade}")
# print("Exponent %e" % 2)

name = "paul"
name = name.capitalize()
print(name)

print("Missisipi".count("i"))

name = "Some string"
print(name.find("str"))
print(name)
print(name.istitle())
name = "A Small Man"
print(name.istitle())

my_string = "This is a longer sentence and I want to find all the letter e in it"

def get_items(index):
    return my_string[index]

indexes = [get_items(i) for i, value in enumerate(my_string) if value == 'e']
print(indexes)

arr = ["Hello", "World!"]
print(' '.join(arr))

test_str = "Here is a big string"
print(len(test_str.split(" ")))

test_str = "Here is a big string"
print(list(test_str))

# Find ASCII code point of letter
print(ord("A"))
