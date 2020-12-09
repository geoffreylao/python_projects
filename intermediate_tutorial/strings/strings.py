# Strings: ordered, immutable, text representation

my_string = 'Hello World I\'m a programmer'
print(my_string)

substring = my_string[1:5]
print(substring)

greeting = "Hello" # concat multiple strings
name = "Tim"
sentence = greeting + " " + name
print(sentence)

for x in greeting: # iterate through string
    print(x)

if 'ell' in greeting: # if else for sub string
    print("yes")
else:
    print("no")

print(my_string.endswith('programmer')) # boolean check

print(my_string.find('o')) # substring find

print(my_string.count('o')) # substring count

print(my_string.replace('World', 'Universe')) # string replacement

my_list = my_string.split() # default delimiter is space

print(my_list)

new_string = ''.join(my_list) 
print(new_string)

my_list_2 = ['a'] * 5 # converting list to string
print(my_list_2)

my_string_2 = ''.join(my_list_2)
print(my_string_2)

var = "Tom"
my_string = "the variable is %s" % var # old formatting method
print(my_string)

var = 3.2
my_string = "the variable is %.2f" % var
print(my_string)

var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2) # new format method
print(my_string)

my_string = f"the variable is {var*2} and {var2}" # newest format method
print(my_string)