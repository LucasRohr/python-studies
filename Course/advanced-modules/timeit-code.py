import timeit

time = timeit.timeit('[n for n in range(100)]', number = 10000)
print(time)

time = timeit.timeit('(n for n in range(100))', number = 10000)
print(time)

time = timeit.timeit('map(str, range(100))', number = 10000)
print(time)
