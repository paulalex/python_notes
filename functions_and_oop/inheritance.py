from abc import ABC, abstractmethod


class Superclass(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def method(self):
        print("Superclass definition")

    def get_name(self):
        return self.__name


class SuperclassTwo:
    def __init__(self, age):
        self.__age = age

    def method(self):
        print("SuperclassTwo definition")

    def get_age(self):
        return self.__age


class Subclass(Superclass, SuperclassTwo):
    def __init__(self, name, age):
        # How do I call super() of SuperclassTwo and pass it the age property
        # passed into this constructor?
        super(Subclass, self).__init__(name)

    def method(self):
        print("Method in child")


subclass = Subclass("Ella", 3)
print(f"Name: {subclass.get_name()}")
print(f"Age: {subclass.get_age()}")
