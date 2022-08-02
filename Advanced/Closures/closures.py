# To know more about closures, check out https://www.youtube.com/watch?v=swU3c34d2NQ

"""

Corey Schafer says: A closure is an inner function that remembers and has access to

variables in the local scope in which it was created, even after the outer function

has finished executing

"""

def divide_by(divisor):

	assert divisor != 0, 'You cannot divide by zero'

	assert type(divisor) == int or type(divisor) == float, 'You must divide by a numeric value'

	def divider(number_to_divide):

		assert type(number_to_divide) == int or float, 'You must divide by a numeric value'

		return number_to_divide / divisor

	return divider

# Trying to divide by zero

print('=== Trying to divide by zero ===', '\n')

try:

	divide_by_0 = divide_by(0)

except AssertionError as assertion_error:

	print(assertion_error, '\n')

# Trying to divide by a non-numeric value

print('=== Trying to divide by a non-numeric value ===', '\n')

try:

	divide_by_str = divide_by('2')

except AssertionError as assertion_error:

	print(assertion_error, '\n')

print('=== Dividing by three ===', '\n')

divide_by_3 = divide_by(3)

print(f'0/3 = {divide_by_3(0)}', '\n')

print(f'1/3 = {divide_by_3(1)}', '\n')
