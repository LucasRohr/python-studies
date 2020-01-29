class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

# --------------------------------------

class Programmer(Person):

    likesCoffee = True

    def __init__(self, techs, name, age):
        super().__init__(name, age)
        self.techs = techs
    
    def showTechs(self):
        return f'{super().getName()} techs are {self.techs}'

# ---------------------------------------

person = Person(name = 'ben-largado', age = 40)
lolo = Person('senhor', 456)

print(person.getName())
print(lolo.getName())

programmer = Programmer(name = 'php', age = 23, techs = [ 'Java', 'Python', 'React' ])

print(programmer.getName())
print(programmer.showTechs())
print(programmer.likesCoffee)

# --------------------------------------------------------------

print('-----------------------------------------------------------')

class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * Circle.pi * self.radius

circle = Circle(30)
print(circle.get_circumference())