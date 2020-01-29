def gen_fibon(n):

    a = 0
    b = 1

    for number in range(n):
        yield a
        (a, b) = (b, b + a)

for fib in gen_fibon(10):
    print(fib)

# ---------------------------

print('')

def generator(n):

    for value in range(n):
        yield value

for i in generator(4):
    print(i)


print('')

gen = generator(5)

print(next(gen))
print(next(gen))

print('')

string = 'some string'

# print(next(string))

iterString = iter(string)

print(next(iterString))
print(next(iterString))
print(next(iterString))
print(next(iterString))