def printLines(text):
    print()
    print('==========================================')
    print()
    print(f'*** {text} ***')
    print()

printLines('tuples')

tup = ( ('key', 'value'), (12, 45), 'key', 'key' )
print(tup)
print(tup[1][1])

# ========= tuples are immutable tup[0] = 500 =========

print(tup.index('key'))
print(tup.count('key'))

a = [ 1, 2, 3 ]
print(a.index(1))

printLines('sets')

seti = set()
seti.add('a')
print(seti)

a = [ 1, 4, 4, 5, 6, -7, -7 ]
a.sort()
a = set(a)
print(list(a))
print(a.union([1, 2, 3, 3, 4, 4, 7, 7, -1]))

print(set('Mississipi'))

printLines('booleans')

print(10 > 20)
if(10 < 30):
    print('a')
else:
    print('b')

printLines('files')

file = open('./folder/file.txt')

print(file.read())
file.seek(0)

print(file.read())
file.seek(0)

lines = file.readlines()
print(lines)

file.close()


with open('./folder/file.txt', mode = 'a') as testFile:
    testFile.write('\njao jao jao jao')

with open('./folder/file.txt', mode = 'r') as testFile:
    content = testFile.readlines()
    print(content)

with open('./folder/new-file.txt', mode = 'w') as newFile:
    newFile.write('new file created\nyay')



printLines('booleans')

boole = 3 > 4
sla = 78 < 89

print('2' == 2)
print( boole and sla )
print( boole or sla )
print( not boole )


printLines('conditions')

if(boole == False):
    print('liar')
else:
    print('gub boi')

if(sla == True):
    print('sla')
elif((sla or boole) == True):
    print('or')
else:
    print('else')

printLines('for loops')

a = [ 0, 1, 2, 3, 4, 5 ]
soma = 0

for i in range(1, len(a) + 1):
    soma += i*2
    print(a[-i])

print(f'soma = {soma}\n')

string = 'sou uma string'

for i in string:
    print(i)

print()

tupList = [ (0, 1), (12, 45), (7, 8) ]

for (a, b) in tupList:
    print(f'a = {a}')
    print(f'b = {b}\n')

dic = { 'key': 'value', 'chave': 45 }

for i in dic:
    print(i)

print()

for i in dic:
    print(dic[i])

print()

for key, value in dic.items():
    print(f'key = {key}')
    print(f'value = {value}')

printLines('while loops')

x = 10

while x > 0:
    x -= 1
    print(x)
else:
    print('vava')

print()
print('pass')
print()

x = 10

while x > 2:
    x-= 1
    print(x)
    pass


print()
print('break')
print()

x = 10

while x > 2:
    x-= 1
    print(x)
    if(x == 5): break

print()
print('continue')
print()

x = 10

while x > 2:
    x-= 1
    if(x == 5): 
        continue
    else:
        print(x)