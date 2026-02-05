import random

a = random.sample(range(100), 35)
b = random.sample(range(100), 25)

print(a, b)

c = [x for x in a for y in b if y == x]
print(c)