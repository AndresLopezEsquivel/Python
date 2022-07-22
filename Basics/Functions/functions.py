# args is a tuple, whereas kwargs is a dictionary

# args is used for positional arguments while kwargs for keyword arguments

def example_function(*args, **kwargs):

	print('type(args) = {}'.format(type(args)), '\n')

	print('args = {}'.format(args), '\n')

	print('type(kwargs) = {}'.format(type(kwargs)), '\n')

	print('kwargs = {}'.format(kwargs), '\n')

"""

example_function(1, name = "Andrés", 2, age = 22, 3, major = 'EE') <= This is not going to work

SyntaxError: positional argument follows keyword argument 

"""

print('=== First example ===', '\n')

example_function(1, 2, 3, 4, name = 'Andrés', age = 22, major = 'EE')


print('=== Second example ===', '\n')

numbers = [1, 2, 3, 4]

info = {'name' : 'Andrés', 'age' : 22, 'major' : 'EE'}

example_function(*numbers, **info)
