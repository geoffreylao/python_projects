# lambda arguments: expression 
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2,3))

# map (func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

b = filter(lambda x: x%2==0, a)
print(list(b))

from functools import reduce

# reduce(func, seq)
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
