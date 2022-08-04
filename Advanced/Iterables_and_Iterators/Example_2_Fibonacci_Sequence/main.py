from fibonacci import Fibonacci

if __name__ == '__main__':

	sequence_length = 11

	sequence = Fibonacci(sequence_length)

	print(f'== {sequence_length} digits of the fibonacci sequence ==', '\n')

	for number in sequence:

		print(number)