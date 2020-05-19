class Edureka:
    def __init__(self):
        self.pub = "Public attribute"
        self._prot = "Protected"
        self.__private = "Private"
        self._percent = 0.3

    def investment_returns(self, amount):
        output = amount + amount * self._percent
        print(int(output))


class EdurekaTwo:
    x = "Is it class level"

    def __init__(self, n):
        self.name = n

    def __del__(self):
        print("Object is being destroyed")

    def __str__(self):
        return "Formatted version of this method"


objTwo = EdurekaTwo("P")
objThree = EdurekaTwo("E")
objThree.x = "Change"

print(objTwo.x)
print(objThree.x)
print(objThree)

obj = Edureka()
obj.investment_returns(1000)
obj._prot = "Not protected"
obj.__private = "Not private, its a new variable attached to this object"
obj._Edureka__private = "Mangled not private"
print(obj._prot)
print(obj.__private)
print(obj._Edureka__private)
print(dir(obj))

