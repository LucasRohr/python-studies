from colorama import init, Fore
init()

class Animal():

    def __init__(self, species):
        self.species = species
    
    def eat(self):
        print('eating')
    
    def get_species(self):
        return self.species


class Eagle(Animal):

    def __init__(self, species, eatSnakes = False):
        Animal.__init__(self, species)
        self.eatSnakes = eatSnakes
    
    def checkIfEatSnakes(self):
        return self.eatSnakes and 'snakes are yummy' or 'don\'t like snakes at all'
    
    def eat(self):
        print('eagle eating')
    
brav = Eagle('white eagle', True)
eatSnakesMessage = brav.checkIfEatSnakes()
print(eatSnakesMessage)

print(brav.get_species())
brav.eat()

# ----------------------------------

print('')
print('-------- POLI --------')
print('')

print('-------- abstract class example --------')
print('')

class Animal():

    def __init__(self, name):
        self.name = name
    
    def makeSound(self):
        raise NotImplementedError('Abstract class methods must be implemented by subclasses')

animal = Animal('fred')
#animal.makeSound()

class Dog(Animal):

    def makeSound(self):
        print(f'{self.name} makes woof')

class Cat(Animal):
    
    def makeSound(self):
        print(f'{self.name} makes meow')

dog = Dog('dogiui')
cat = Cat('catty')

dog.makeSound()
cat.makeSound()

print('')
print('---------- function example ----------')
print('')

def makeAnimalSound(animal):
    animal.makeSound()

makeAnimalSound(dog)
makeAnimalSound(cat)

print('')
print('---------- loop example ----------')
print('')

for pet in [ cat, dog, cat ]:
    pet.makeSound()

# ----------------------------------

print('')
print('-------- SPECIAL METHODS --------')
print('')

class Book():

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book has been deleted')

book = Book('some book', 'alguem', 150)

print(book)
str(book)

print(len(book))

print(Fore.CYAN + 'cyan text')