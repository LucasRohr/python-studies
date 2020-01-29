def simple():

    def inside():
        print('hey inside')
    
    return inside

returnFunc = simple()

returnFunc()

# ----------------------------------------

def function(cb):
    print(f'callback returned {cb}')

def mult(value1, value2):
    return value1 * value2

function(mult(4, 5))

# ----------------------------------------

print('')

def decorator(function):

    def insideDecorator():
        print('before')
        function()
        print('after')
        function()

    return insideDecorator

@decorator
def needsDecoration():
    print('i want to be decorated')

needsDecoration()