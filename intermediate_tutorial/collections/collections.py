# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(2))

print(list(my_counter.elements())) 

from collections import namedtuple

Point = namedtuple('Point' , 'x,y')

pt = Point(1,-4)

print(pt.x, pt.y)

from collections import OrderedDict # deprecated

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2

print(ordered_dict)

from collections import defaultdict

d = defaultdict(int) # default value will be 0
d['a'] = 1
d['b'] = 2
print(d['c'])

from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3) # appends to left side
print(d)

d.pop()
print(d)

d.clear()
print(d)

d.extendleft([3,4,5])
print(d)
