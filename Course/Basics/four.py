def printLines(text):
    print()
    print('==========================================')
    print()
    print(f'*** {text} ***')
    print()

lista = [ 2, 4, 5, 6, -7 ]

mappedSquare = map(
    lambda item :
        item**2,
    lista
)
print(list(mappedSquare))

def splicer(word):
    return word == 'a' and 'PORA MEO' or word

itera = 'fala maa'
mappedString = map(lambda word : splicer(word), itera)
print(list(mappedString))

lista = [ 2, 1, 7, 8, 9, 10, 12, 15, 16 ]

filteredList = filter(lambda value : value % 2 == 0, lista)
print(list(filteredList))

printLines('scope')

x = 50

def func():

    #x = 50
    global x
    x = 12

    def inside():
        #x = 12
        print(x)

    inside()

func()
print(x)

