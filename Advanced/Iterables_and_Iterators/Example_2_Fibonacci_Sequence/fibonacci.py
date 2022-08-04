class Fibonacci:

	def __init__(self, sequence_length = 0):

		self.sequence_length = sequence_length

		self.index_of_current_number = 1

		self.first_number = 0

		self.second_number = 1


	def __iter__(self):

		return self


	def __next__(self):

		if self.index_of_current_number <= self.sequence_length:

			aux = self.first_number + self.second_number

			self.first_number = self.second_number

			self.second_number = aux

			self.index_of_current_number += 1

			return self.first_number

		else:

			raise StopIteration