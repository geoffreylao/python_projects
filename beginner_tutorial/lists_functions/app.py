# Lists functions

lucky_numbers = [ 1, 2, 3, 4, 5]
friends = ["Kevin", "Mike", "Loh", "Jess", "Ryan"]

friends.append("Creed") # append to end of list
friends.insert(1, "Kellen") # append to index 1
friends.remove("Loh") # remove specific element
print(friends)

friends.pop() # remove last element
print(friends)
print(friends.index("Kevin")) # find index of kevin
print(friends.count("Kevin")) # count how many times element appears in list

friends.sort() # sort list
print(friends) 

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
