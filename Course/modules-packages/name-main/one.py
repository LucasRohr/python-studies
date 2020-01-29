def oneFunc():
    print('one func')

print('top level in one')

if (__name__ == '__main__'):
    print('one executed directly')
else:
    print('one has been imported')