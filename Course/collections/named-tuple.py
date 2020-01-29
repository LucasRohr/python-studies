from collections import namedtuple

tup = (1, 2, 3)

print(tup[0])

Dog = namedtuple('Dog', 'name age breed')

dogo = Dog('otis', 42, 'lab')

print(dogo.name)
