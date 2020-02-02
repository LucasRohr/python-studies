string = 'hello my boi'

print(string.capitalize())
print(string.title())
print(string.center(20, '='))
print(f'string.islower() {string.islower()}')
print(f'string.isalpha() {string.isalpha()}')
print(f'string.istitle() {string.istitle()}')

split = string.split('o')
partition = string.partition('o')

print(f'splitted {split}')
print(f'partition {partition}')

a = (1, 2)
