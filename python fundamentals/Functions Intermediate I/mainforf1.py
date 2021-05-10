import random


def randInt(min=0, max=100):
    num = 0
    if min <= max and max > 0:
        num = random.random()*(max-min)+min
    return int(num)


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
