names = ['Bruce Wayne', 'Clark', 'Peter', 'Logan', 'Wade']

heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

list_of_heroes = {name : heroe for name, heroe in zip(names, heroes)}

try:

	# Write here the lines of code that could possibly throw an exception

	# name = 'Tony Stark'

	name = 'Logan'

	# You can also raise an exception

	if name == 'Logan':

		raise Exception

	else:

		heroe = list_of_heroes[name]

except KeyError as key_error:

	# The code written here is executed when a FileNotFoundError exception occurs

	print('The indicated key does not exist. Check it out, please.', '\n')

	print('Non existent key: ', key_error, '\n')

except Exception as exception:

	# This code is executed when any other exception occurs 

	print('Sorry, something went wrong', '\n')

	print(exception)

else:

	# The code written here is executed when an exception does not occur

	print(f'{name} is {heroe}. ', '\n')

finally:

	# The code written here is executed regardless an exceptions occurs or not

	# For example, this is a good place to close down  the connection to a database

	pass

