# * * * * * * *
result = 5 * 7 # multiplication
print(result) 

result = 2 ** 4 # power operation
print(result)

zeros = [0,1] * 10 # create lists/tuples/strings with repeating elements
print(zeros)

def foo(a, b, *args, **kwargs): # as many args/keyword args as you wants
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6,seven=7)

def bar(a,b,c):
    print(a,b,c)

my_list = [0,1,2]
bar(*my_list) # unpacks list/tuple/dict into function, must have same amount of arguements as elements

numbers = [1,2,3,4,5,6]
*beginning, last = numbers
print(beginning) # unpacks all numbers except last into list
print(last)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3}

mydict = {**dict_a, **dict_b}
print(my_dict)