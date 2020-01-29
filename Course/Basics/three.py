def printLines(text):
    print()
    print('==========================================')
    print()
    print(f'*** {text} ***')
    print()

printLines('operators')

a = [ 1, 2, 3, 4, 5 ]

print('range')
print('')

print(list(range(3, len(a) + 1)))

print('')
print('enumerate')
print('')

a = 'stringaa'

for index, item in enumerate(a):
    print(f'index = {index}')
    print(f'item = {item}\n')

print('')
print('zip')
print('')

a = [ 1, 2, 3, 4 ]
b = [ 'a', 'b', 'c' ]
lista = [ 200, 3300 ]

for a, b, c in zip(a, b, lista):
    print(f'{a} - {b} - {c}')


print('')
print('in')
print('')

print('x' in 'xeeee')

dic = { 'key': 'value', 'chave': 45 }

print('key' not in dic)
print(45 in dic.values())

print('')
print('min and max')
print('')

a = [ 89, 2, 1, 4 ]

print(f'max = {max(a)} and min = {min(a)}')

print('')
print('random')
print('')

from random import shuffle, randint

lista = [ 1, 2, 3, 4, 5, 6, 7 ]
shuffle(lista)

print(lista)

print(randint(1, 10))

print('')
print('input')
print('')

# result = int(input('type something:'))

# print(f'result * 2 = {result * 2}')


printLines('list comprehenions')

string = 'lale'

lista = [i for i in string]

print(lista)

dois = [ num**2 for num in range(0, 11) if (num % 2 == 0) ]

print(dois)

lista = [ (x * y) for x in [ 2, 4, 6 ] for y in [ 1, 5, 10 ] ]

print(lista)

printLines('methods and functions')

def hello(name = 'name'):
    print(f'hello {name}')

hello('jaozinho')

def mult(num1, num2):
    return num1 * num2

res = mult(4, 5)
print(res)

def inString(word, string):
    return word in string

print(inString('f', 'abc'))

def pigLatin(word):
    vowels = [ 'a', 'e', 'i', 'o', 'u' ]

    if (word[0] in vowels):
        return word + 'ay'
    else:
        return word[1::] + word[0] + 'ay'
    
result = pigLatin('word')
print(result)

def myFunc():
    print('Hello World')

def function(*args): # param is a tuple
    return sum(args)

res = function(4, 5, 6)
print(res)

def kwargsExample(**kwargs):
    print(kwargs)

kwargsExample(a = 1, b = 2)

def kwargs(**kwargs): # param is a dictionary
    return kwargs['fruit'] + ' is a good one'

res = kwargs(fruit = 'react')
print(res)

def combo(*args, **kwargs):
    print(args)
    print(kwargs)

    print(f"I would like {args[1]} {kwargs['food']}")

combo(5, 14, 3, 4, fruit = 'aaa', food = 'jjjjj')

def myfunc(string):
    returnString = ''
    helperList = list(string)

    for i in range(len(helperList)):
        letter = helperList[i]
        returnString += (i % 2 == 0) and letter.upper() or letter.lower()
    return returnString

res = myfunc('Antropopopoo')

print(res)