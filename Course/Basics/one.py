a = [ 5, 4, -4, 89, 75, 104, -1 ]

for i in range(len(a)):
    index = i
    for y in range(i + 1, len(a)):
        if(a[y] < a[i]):
            index = y
        
    if(index != i):
        aux = a[i]
        a[i] = a[index]
        a[index] = aux

print(a)

def some(value):
    return value**2

mapped = map(
    lambda value : some(value),
    a
)
print(list(mapped))



''' =============================================== '''

print( 16 % 5 )

''' ==================================== '''

a = 0
a += (a + 12)

print(a)

a = ((10, 12), (12, 'sla'))

print(a[1][1])

print(type(a))

''' ======================================= '''

print()
print('==========================================')
print()

string = 'nkjf ndscv gdfggff'

print(string[0 : len(string) : 2])
print('penultimo: ' + string[-2])
print(string.index('ff', 0, len(string)))
print( string[2 : -5] )

print('size: ' + string[::10])
print('reverse: ', string[::-1])

print('he yo\nboi')

print(string.split('f'))

print('boi\tyay')

print(str(2) + ' pess')

print(string.isupper())

print('yo {}'.format(string))

print(' {a} {a} {a} '.format(a = 'nlon', b = 'b', c = 'c'))

number = 0.4515678648

print('number is {num:1.2f}'.format(num = number))

print(f'number is {number:1.3f}')

lista =  [ 12, 456, 61, 6 , 56  ]
sla = [ 'fdsfd', 'fgfdg' ]

print(lista[2:])
print(lista + sla * 5)
lista.append(89)
lista.pop(-2)
print(lista)
print(lista[::-1])

# ======================================

print()
print('==========================================')
print()
print('sort')

sortedList = sorted(lista)
sortedList.append(45)
print(sortedList)

print(sorted(lista))
print(lista)

lista.sort()

print(lista)

print()
print('==========================================')
print()
print('reverse')

a = [ 45, 6, 78]
print(list(reversed(a)))
print(a)

a.reverse()
print(a)

def printLines(text):
    print()
    print('==========================================')
    print()
    print(f'*** {text} ***')
    print()

# ======================================================

printLines('dicts')

dic = { 'key': 'value', 1: [], 'dict': { 'inside': [ 1, 2, 3 ] } }

print(dic)
print(dic['key'])
print(dic['dict']['inside'])

print(list(dic.values()))
print(list(dic.keys()))

print(dic.get('sla', 'default'))

print(dic.__contains__('key'))

dic.update({ 'dome': 1 })
dic['new'] = 'value' * 2
print(f'Updated disc: {dic}')

dic.pop('key')
print(dic)
