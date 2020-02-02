alpha = 'abcde'
dic_comprehension = {alpha[num]: (num ** 2) for num in range(5)}
print(dic_comprehension)

dic_comprehension = {k: (v ** 2) for (k, v) in zip(alpha, range(5))}
print(dic_comprehension)

for item in dic_comprehension.items():
    print(item)

print(dic_comprehension.values())