# Sets: unordered, mutable, no duplicates

myset = set("Hello") 
print(myset)

myset = set() # declare empty set

myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(3) # removes element

print(myset)

print(myset.pop()) # removes element from set

for i in myset: # iterates through set
    print(i)

if 1 in myset:
    print("yes")
else:
    print("no")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # unionizes two sets
print(u)

i = odds.intersection(primes) # returns intersecting values
print(i)

diff = odds.difference(primes) # prints different elements
print(diff)

diff = odds.symmetric_difference(primes) # prints different elements for both sets
print(diff)

odds.difference_update(primes) # updates the set only with the elements that are different
print(odds) 

