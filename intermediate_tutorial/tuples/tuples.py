# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston") # initialized with (), can be made without
print(mytuple)

tuple_from_list = tuple(["Max", 28, "List"]) # convert list to tuple

# mytuple[0] = "Tim" # won't work because tuples are immutable

for i in mytuple: # iterate through tuple
    print(i)

if "Boston" in mytuple: # check for element
    print("yes")
else:
    print("no")

print(len(mytuple)) # get length

print(mytuple.count("Max")) # count how many of specified element

my_list = list(mytuple) # convert tuple to list
print(my_list) 

b = mytuple[1:2] # slicing tuple

c = mytuple[::2] # gets every second element through stepping through the tuple

name, age, city = mytuple # unpack multiple elements with tuple
print(name)
print(age)
print(city)

i1, *i2 = mytuple # unpacks multiple elements into one variable with *
print(i1)
print(i2)

# tuples can be more efficient because they are immutable

import sys

my_list = [0, 1, 2, "Hello", True]
my_tuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))