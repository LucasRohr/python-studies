from one import oneFunc

def twoFunc():
    print('two func')

oneFunc()

def sampleFunc():
    print('logic if two was executed directly')

print('top level in two')

if (__name__ == '__main__'):
    print('two executed directly')
    sampleFunc()
else:
    print('two has been imported')