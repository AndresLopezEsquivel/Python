import time

class MyRange:

	def __init__(self, start, end, step = 1):

		self.start = start

		self.end = end

		self.step = step

		self.current = start


	def __iter__(self):

		return self


	def __next__(self):

		if self.current < self.end:

			number = self.current

			self.current += self.step

			return number

		else:

			raise StopIteration


if __name__ == '__main__':

	max_number = 10

	list_of_numbers = [number for number in MyRange(0, max_number)]

	square_numbers = (number ** 2 for number in list_of_numbers)

	print('list_of_numbers = ', list_of_numbers, '\n')

	print('square_numbers is ', square_numbers, '\n')

	print('square_numbers = ', '\n')

	for number in square_numbers:

		print(number, '\n')