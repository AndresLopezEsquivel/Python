# For more information about dynamic typing and static typing, check out the following websites:

# https://docs.oracle.com/cd/E57471_01/bigData.100/extensions_bdd/src/cext_transform_typing.html

# https://docs.python.org/es/3/library/typing.html

# To know more about mypy, check out https://mypy.readthedocs.io/en/stable/getting_started.html


# To check type before executing the code, run 'mypy <file-name.py> --check-untyped-defs'

def is_palindrome(string: str) -> bool:

	string = string.replace(" ", "").lower()

	return string == string[::-1]


if __name__ == "__main__":

# Before ruunning the program, run 'mypy <file-name.py> --check-untyped-defs'	

	try:

		is_palindrome(1000)

	except AttributeError as error:

		print('Error: ', error, '\n')

	print(f"Is 'Ana' a palindrome? R: {is_palindrome('Ana')}", '\n')

	print(f"Is 'Andrew' a palindrome? R: {is_palindrome('Andrew')}", '\n')