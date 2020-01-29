def provideNumber():

    while True:

        try:
            numer = int(input('Please, provide a number: '))
        except ValueError:
            print('That\'s not a number')
            continue
        else:
            print('Thx!')
            break
        finally:
            print('always here')
    

#provideNumber()

def ask():
    
    while True:
        try:
            integer = int(input('Please, enter a integer value: '))
        except:
            print('An error occurred! Please try again!')
            print('')
            continue
        else:
            print(f'Input an integer: {integer}')
            print(f'Thank you, your number squared is:  {integer ** 2}')
            break

ask()