def fibonacci_sequence(sequence_length: int):

	first_number = 0

	second_number = 1

	for _ in range(sequence_length):

		aux = first_number + second_number

		first_number = second_number

		second_number = aux

		yield first_number


if __name__ == '__main__':

	sequence_length = 11

	print(f'== First {sequence_length} digits of fibonacci sequence ==', '\n')

	for digit in fibonacci_sequence(sequence_length):

		print(digit)