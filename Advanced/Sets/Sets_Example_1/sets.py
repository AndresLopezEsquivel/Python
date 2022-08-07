# Sets are unordered collections containing unique and immutable items

# Creating a set from a list

print('=== Creating a set from a list ===', '\n')

my_list = [1, 1, 2, 2, 3, 3]

set_of_my_list = set(my_list)

print('my_list = ', my_list, '\n')

print('set_of_my_list = ', set_of_my_list, '\n')

# Creating a set from a tuple

print('=== Creating a set from a tuple ===', '\n')

my_tuple = (1, 1, 2, 2, 3, 3)

set_of_my_tuple = set(my_tuple)

print('my_tuple = ', my_tuple, '\n')

print('set_of_my_tuple = ', set_of_my_tuple, '\n')

# Adding elements to a set

print('=== Adding elements to a set ===', '\n')

my_set = {1, 2, 3, 4, 4, 5}

print('my_set before been updated: ', my_set, '\n')

my_set.add(7)

# You can update a set using different data structures

my_set.update([1,9,77], (55,66), {88, 99})

print('my_set after been updated: ', my_set, '\n')


# To discard elements

print('=== To discard elements ===', '\n')

my_set.discard(99)

my_set.discard(100)

print('my_set after using discard() = ', my_set, '\n')

# To remove elements

# To remove an element we don't know whether exists, use discard() instead of remove()

my_set.remove(66)

try:

	my_set.remove(100)

except KeyError:

	print('You cannot remove a nonexistent element with remove()', '\n')

# To get and remove a random element

print('=== To get and remove a random element ===', '\n')

element = my_set.pop()

print('Random element: ', element, '\n')

# To clear the set

print('=== To clear the set ===', '\n')

my_set.clear()

print('my_set: ', my_set, '\n')