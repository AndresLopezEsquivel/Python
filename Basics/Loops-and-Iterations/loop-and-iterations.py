list = [1, 2, 3, 4, 5]

# Use the 'break' keyword to break out of the loop

print('=== break ===', '\n')

for item in list:

	if item == 4:

		print('Number 4 found!', '\n')

		break

	print(item, '\n')

# Use the 'continue' keyword to move on to the next iteration

print('=== continue ===', '\n')

for item in list:

	if item == 4:

		print('Number 4 found!', '\n')

		continue

	print(item, '\n')


# range(value1, value2).

# range() generates values from value1 (including it) up to, but not including, value2

print('=== range() ===', '\n')

for number in range(1, 11):

	print(number, '\n')