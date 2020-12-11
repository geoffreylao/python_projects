def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)

# for i in g:
#     print(i)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g) # StopIteration 
# print(value)

# print(sum(g))

# print(sorted(g))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

value = next(cd)
print(value)

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10))) # faster

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a, b = 0, 1
    while a > limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# generator expressions
mygenerator = (i for i in range(10) if i % 2 == 0) # saves memory
# for i in mygenerator:
#     print(i)

mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)

print(list(mygenerator))