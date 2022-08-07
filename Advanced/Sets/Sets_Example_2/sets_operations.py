my_set_1 = {1, 2, 3, 4, 5}

my_set_2 = {4, 5, 6, 7, 8}

print('my_set_1: ', my_set_1, '\n')

print('my_set_2: ', my_set_2, '\n')

# Union

sets_union = my_set_1 | my_set_2

print('=== UNION ===', '\n')

print('sets_union: ', sets_union, '\n')

# Intersection

sets_intersection = my_set_1 & my_set_2

print('=== INTERSECTION ===', '\n')

print('sets_intersection: ', sets_intersection, '\n')

# Difference

print('=== DIFFERENCE ===', '\n')

print('my_set_1 - my_set_2 = ', my_set_1 - my_set_2, '\n')

print('my_set_2 - my_set_1 = ', my_set_2 - my_set_1, '\n')

# Symmetric difference

print('=== SYMMETRIC DIFFERENCE ===', '\n')

print('my_set_1 ^ my_set_2 = ', my_set_1 ^ my_set_2, '\n')

print('my_set_2 ^ my_set_1 = ', my_set_2 ^ my_set_1, '\n')