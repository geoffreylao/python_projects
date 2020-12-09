# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_object = groupby(a, key=smaller_than_3)
for key, value in group_object:
    print(key, list(value))

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3]
for i in cycle(a):
    print(i)

for i in repeat(1, 4): # repeat 4 times
    print(i)