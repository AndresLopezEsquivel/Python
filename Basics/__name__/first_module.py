"""

__name__ variable helps you decide which code will be
executed depending on whether the file is being running
directly by Python or it is being imported

"""

if __name__ == "__main__":

	print('first_module.py is being run directly by Python. ', '\n')

	print('First module\'s __name__: ', __name__, '\n')

else:

	print('first_module.py is being imported by another file. ', '\n')

	print('First module\'s __name__: ', __name__, '\n')