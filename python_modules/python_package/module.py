import sys


def my_fun(x):
    if not isinstance(x, int):
        try:
            raise Exception("Not an int")
        except Exception as e:
            print(e)
            print(sys.exc_info())
    return x * x
