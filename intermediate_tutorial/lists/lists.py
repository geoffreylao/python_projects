# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[0] # get item from index
print(item)

for x in mylist: # loop through list
    print(x)

print(len(mylist)) # length of list

mylist.append("lemon") # append to list
print(mylist)

mylist.insert(1, "blueberry") # insert at index
print(mylist) 

pop_item = mylist.pop() # return and remove last item in list
print(item) 
print(mylist)

mylist.remove("cherry") # remove element
print(mylist) 

mylist.clear() # empty the list

mylist.sort() # sorts list alphanumerically

new_list = sorted(mylist) # create a new list with the old list but sorted
print(mylist)
print(new_list)

mylist3 = [0] * 5 # multiplies elements of list
print(mylist3)

new_list = mylist + mylist2 # concat list

a = mylist[1:2] # get range of list
print(a)

list_copy = mylist # duplicates list, both lists now refer to same list inside memory, modifying one modifies the other
list_copy_true = mylist.copy() # actual copy
list_copy.append("lemon") 
print(list_copy)
print(list_copy_true)

mynum = [1, 2, 3] # squareing elements in a list
b = [i*i for i in mynum] 

