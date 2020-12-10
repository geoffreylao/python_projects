# Errors and Exceptions
a = 5
# print(a)) SyntaxError: invalid syntax
# a = 5 + '10' TypeError: unsupported operand types for int and str
# import somemodule ModuleNotFoundError: No module named somemodule
# b = c NameError: name c is not defined
# f = open('somefile.txt') FileNotFoundError: no such file or directory
# ValueError: Value does not exist
# IndexError: list index out of range
# my_dict KeyError:Age

x = -5

# if x < 0:
#    raise Exception('x should be positive')

# assert (x>=0), 'x is not postive

try:
    a = 5/0 # ZeroDivisionError
except ZeroDivisionError as e:
    print(e)

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)