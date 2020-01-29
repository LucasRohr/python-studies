# DEFAULT DICT

from collections import defaultdict, OrderedDict

dic = defaultdict(lambda : 2)

print(dic['one'])

dic['two'] = 3

print(dict(dic))

print('')
print('ORDERED DICT')
print('')
# ORDERED DICT

dic = {}

dic['a'] = 1
dic['b'] = 2

# dic2 = {}

dic2 = OrderedDict()

dic2['b'] = 2
dic2['a'] = 1

print(dic)
print(dic2)
print(dic == dic2)
