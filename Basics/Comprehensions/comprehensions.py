# Comprehensions are an easier and readable way to create lists, dictionaries and sets

# List comprehension

numbers = [x for x in range(11)]

print('numbers: ', numbers, '\n')

# Getting the square of each number in list 'numbers' and saving the results in 'square_numbers'

square_numbers = [number ** 2 for number in numbers]

print('square_numbers: ', square_numbers, '\n')

# For each item in the 'numbers' list, if the number is even, select it

even_numbers = [number for number in numbers if number  % 2 == 0]

print('even_numbers: ', even_numbers, '\n')

# Create a (letter, number) pair for each letter in 'ABCD' and each number in '12345'

letters_numbers = [(letter, number) for letter in 'ABCD' for number in  '12345']

print('letters_numbers: ', letters_numbers, '\n')

# Dictionary comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']

heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

names_and_heroes = {name : heroe for name, heroe in zip(names, heroes) if name != 'Logan'}

print('names_and_heroes: ', names_and_heroes, '\n')

# Set comprehension

numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

set_of_numbers = {number for number in numbers}

print('set_of_numbers: ', set_of_numbers, '\n')

# Generator expression

generated_numbers = (number for number in range(11))

print('generated_numbers: ', generated_numbers, '\n')