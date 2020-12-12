"""
- The difference between arguements and parameteres
- Positional and keyword arguements
- Default arguements
- Variable-length arguements (*args, **kwargs)
- Container unpacking into function arguments
- Local vs. global arguements
- Parameter passing (by value or by reference?)
"""

def print_name(name): # name is parameter
    print(name)

print_name('Alex') # Alex is the arguement

def foo(a,b,c,d=4): # d is the default parameter
    print(a,b,c,d)

foo(1,2,3) # positional arguements

foo(a=1,b=2,c=3) # keyword arguements (order doesn't matter)

foo(1, b=2,c=3) # keyword arguements have to follow positional

# variable length

def bar(a,b, *args, **kwargs): #'*' any amount of arguements , '**' any amount of keyword arguements
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

bar(1,2,3,4,5, six = 6, seven = 7) # 1,2 are positional args a,b / 3,4,5 are *args / six=6,seven=7 are **kwargs

# unpacking arguements

def goo(a,b,c):
    print(a,b,c)

my_list = [0,1,2] 
goo(*my_list) # must match amount of parameters

# local vs global

def nar():
    global number
    number = 3

number = 0
print(number)
nar()
print(number)

# Parameters passing by value or reference
# ints are immutable and cannot be changed via function
# lists are mutable and can be changed via function

def hoo(a_list):
    a_list.append(4)

my_list = [1,3,3]
hoo(my_list)
print(my_list)