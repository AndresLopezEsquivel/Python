# Use of textual data

# Using single quotes on the inside, while using double quotes on the outside

message_1 = "Andres' car"

print(" === Messsage 1 === ")

print(message_1)


# Using single quotes on the outside, while using double quotes on the inside

message_2 = 'I love "Hitchiker\'s guide to the galaxy" book'

print(" === Messsage 2 === ")

print(message_2) 

# Multiline string

message_3 = """The guy was listening to a glorious piece of music, 
when, suddenly, at the end of the recording, a dreadful
screeching sound appeared. The guy said, quite sadly,
that the experience was ruined, when in reality, just
the memory of the experience was ruined
"""

print(" === Messsage 3 === ")

print(message_3)

# Accessing to an specific character inside the string (Slicing)

message_4 = "How is it going?"

print(" === Messsage 4 === ")

"""
string_variable[a : b]

a => starting value (inclusive). If a = 0, then, 'a' can be omitted (string_variable[:b])

b => end value (exclusive). If b = len(string_variable) - 1, then, 'b' can be omitted (string_variable[a:])

"""

print(message_4[:5])

print(message_4[4:])

# String methods

print(" === Messsage 5 === ")

message_5 = 'Hello World'

print(message_5.lower())

print(message_5.upper())

print(message_5.count('Hello'))

print(message_5.find('universe'))

message_5 = message_5.replace('World', 'Mexico')

print(message_5)

# Concatenating strings

word_1 = "Hello"

word_2 = "Andrés"

print(word_1 + ", " + word_2)

print("{}, {}".format(word_1, word_2))

print(f"{word_1}, {word_2}")

# Getting help

a = "Hola"

print(dir(a))

print(help(str))

print(help(str.lower))