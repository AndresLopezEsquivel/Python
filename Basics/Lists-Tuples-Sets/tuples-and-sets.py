empty_list_1 = []

empty_list_2 = list()

empty_tuple_1 = ()

empty_tuple_2 = tuple()

empty_set_1 = {}

empty_set_2 = set()


# === Tuples ===

print('=== TUPLES ===', '\n')

"""
Tuples and lists are both similar, but there is a notorious difference between them:

Tuples cannot be modified. So, lists are mutable while tuples are inmutable. 
"""

# Example of mutable

list_1 = ['item1', 'item2', 'item3', 'item4']

# list_2 is a reference to list_1, so that, they are pointing to the same memory location

list_2 = list_1

list_2[0] = 'item0'

print(f'list_1: {list_1}', '\n')

print(f'list_2: {list_2}', '\n')

# Example of mutable

tuple = ('item1', 'item2', 'item3', 'item4')

# If the next line of code is executed, an error is going to be prompted because tuples are inmutable

# tuple[0] = 'item0'

# === Sets ===

"""
Unlike lists or tuples, sets don't care about order. Sets are used when it is required to check whether a value

is part of the set. Sets don't let the existence of duplicates.

"""

print('=== SETS ===', '\n')

electrical_engineering_courses = {'Electronic Amplifiers', 'Microcontrollers', 'Integrated Analog Circuits', 'DSP'}

computer_science_courses = {'OOP', 'Microcontrollers', 'ML', 'Web Design'}

print('Electrical Engineering courses set: ', electrical_engineering_courses, '\n')

print('Computer Science courses set: ', computer_science_courses, '\n')

intersection = electrical_engineering_courses.intersection(computer_science_courses)

print('Intersection between both majors: ', intersection, '\n')

difference = electrical_engineering_courses.difference(computer_science_courses)

print('Courses Electrical Engineering has and Computer Science doesn\'t: ', difference, '\n')

union = electrical_engineering_courses.union(computer_science_courses)

print('Union between both majors: ', union, '\n')
