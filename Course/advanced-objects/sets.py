set_list = {1, 4, 5, 5, 5, 5}
set_list.add(4)
print(set_list)

copy = set_list.copy()

set_list.clear()
print(set_list)
print(copy)

# ----------------------------

new_set = {1, 2, 3}
second_set = {4, 2, 6, 14}

print(f'difference 1 to 2 {new_set.difference(second_set)}')
print(f'difference 2 to 1 {second_set.difference(new_set)}')

#new_set.difference_update(second_set)
print(new_set)

# ---------------------------

second_set.discard(6)
print(f'discarded {second_set}')

# -------------------------

print(new_set.intersection(second_set))

new_set.intersection_update(second_set)
print(new_set)

new_set = {1, 2, 3}
second_set = {1, 2, 4, 3}
third_set = {4, 5}

print(new_set.isdisjoint(third_set))

# ------------------

print(f'new_set.issubset(second_set) = {new_set.issubset(second_set)}')
print(f'second_set.issuperset(new_set) = {second_set.issuperset(new_set)}')

# ---------------------

print(new_set.symmetric_difference(second_set))

# -----------------------------------

print(new_set.union(second_set))
new_set.update(second_set)
print(new_set)
