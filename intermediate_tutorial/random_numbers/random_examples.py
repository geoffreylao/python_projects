import random

random.seed(1) # random module can be seeded (pseudorandom)

a = random.random() # random float from 0-1
print(a)

a = random.uniform(1,10) # random float in range
print(a)

a = random.randint(1,10) # random int beteween 1-10
print(a)

a = random.randrange(1,10) # random int between 1-9

a = random.normalvariate(0,1) # random with mean of 0 and standard deviation of 1 (???)
print(a)

mylist = list("ABCDEFGH")
print(mylist)
a = random.sample(mylist, 3) # collects random samples from list
# a = random.choices(mylist, k=3) can collect the same sample multiple times
print(a)
random.shuffle(mylist) # shuffles list
print(mylist)

import secrets

a = secrets.randbelow(10) # produce a random integer from 0-9
print(a)

a = secrets.randbits(4) # produce a random integer with k random bits
print(a) #1010

a = secrets.choice(mylist) 