import random

a = random.sample(range(100), 35)
b = random.sample(range(100), 25)

print(a)
print(b)

c = [x for x in a for y in b if y == x]
print(f"The common numbers are: {c}")

#does not account for duplicates; cannot implement such using list comprehensions, for now
