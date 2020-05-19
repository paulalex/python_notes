from itertools import permutations
import math

fruits = ["Apple", "Orange", "Cherry", "Banana", "Kiwi"]

perms = permutations(fruits)
perms_of_three = permutations(fruits, 3)

for fruit_perm in perms_of_three:
    print(fruit_perm)

fruits = ["banana", "grape", "apple"]
print(f"Factorial of fruits is {math.factorial(len(fruits))}")

print(f"Combinations {math.ceil(3 / 2)}")
# banana + grape
# banana + apple
# grape + apple

combinations = len(fruits) ** 2

print(combinations)


class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    @classmethod
    def date(cls, day, month, year):
        return cls(year, month, day)


import datetime

print(datetime.datetime.now().strftime("%A %d %B %Y"))

today = datetime.datetime.today()
christmas = datetime.datetime(2020, 12, 25)
print(f"{christmas - today} days til Christmas")
print(dir(datetime.datetime))
