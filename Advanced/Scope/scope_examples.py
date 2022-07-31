# Scope is where variables can be accessed from within the code

"""

LEGB stands for Local, Enclosing, Global and Built-in

Local Scope -> Variables defined within a function

Enclosing -> Variables in the local scope of enclosing functions

Global -> Variables defined at the top level of the module or explicitly declared using the 'global' keyword

Built-in -> Names that are preassigned in Python

For more about Scope, check out https://youtu.be/QVdf0LgmICw

"""

import builtins

x = 'global x'

def my_func_1():

	print('=== my_func_1 ===', '\n')

	# 'x' is not overwritten (there is a global 'x'), instead a new local 'x' variable  is created

	# That means id(local x) != id(global x)

	x = 'local x'

	print('id(x) =', id(x), '\n')

	print('Value of x printed from my_func_1: ', x, '\n')

	# 'y' is a local variable, so it can be only accessed inside my_func

	y = 'local y'

	print(y, '\n ')


def my_func_2():

	print('=== my_func_2 ===', '\n')

	# To work with the global 'x' variable, use the 'global' keyword

	global x

	print('Value of x printed from my_func_2: ', x, '\n')


def outer():

	print('=== outer ===', '\n')

	# outer is an enclosing clousure

	x = 'x from outer'

	def inner():

		# x is now an enclosing variable and not a local one

		nonlocal x

		x = 'x from inner'

		print('Value of x printed from inner(): ', x, '\n')


	print('Value of x printed from outer() before inner() is executed: ', x, '\n')

	inner()

	print('Value of x printed from outer() after inner() was executed: ', x, '\n')


print('id(x) =', id(x), '\n')

print('Value of x printed from the main body of the code: ', x, '\n')

# Uncomment and run the next line to check what the built-in variables are

# print(dir(builtins))

my_func_1()

my_func_2()

outer()
