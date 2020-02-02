my_list = [1, 4, 5]
my_list.append(5)

print(my_list)
print(my_list.count(5))

second_list = [4, 5, 6]
my_list.extend(second_list)
print(my_list)

# -------------------------------

my_list.insert(2, 'string')
print(my_list)
my_list.pop(-1)
print(my_list)

my_list.remove(5)
print(my_list)

new_list = [8, 9, 45, 2, 7, 82, 62, 6, 554, 5, 6, 5]

new_list.sort()
print(new_list)
