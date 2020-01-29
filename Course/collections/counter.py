from collections import Counter

lista = [ 1, 2, 22, 2, 2 , 2 , 4, 5 , 54, 66, 4, 5, 5 ]
print(Counter(lista))

print('')

string = 'sou juma joojojoj'
print(Counter(string))

print('')

sentence = 'I am a sentence how much words words do I I have have ??'
split = sentence.split()

counter = Counter(split)

print(counter.most_common(3))
print(set(counter))