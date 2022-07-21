student = {'Name' : 'Andrés', 'Surname' : 'López', 'Age' : 22, 'Courses' : ['DSP', 'ML', 'Microcontrollers']}

# Trying to get a value when a non existent key is given

print(student.get('University', 'Non existent key'), '\n')

# Creating a new key-value pair

student['id'] = 12345678

print('student dictionary with id key and its respective value added: ', '\n')

print(student, '\n')

# Updating (or adding) various data all in one shot

student.update({'Name' : 'Andrew', 'Age' : 23, 'Phone' : '555-555-5555'})

print('updated dictionary: ', '\n')

print(student, '\n')

# Deleting an item (key-value pair)

del student['Phone']

print('dictionary after deleting Phone key and its value: ', '\n')

print(student, '\n')

# Using the pop() function to remove and return a value according to the indicated key

popped_value = student.pop('Surname')

print('Dictionary after using the pop() function: ', '\n')

print(student, '\n')

print('Popped value: ', popped_value, '\n')

# Accesing to keys

keys = student.keys()

print('keys: ', keys, '\n')

# Accesing to values

values = student.values()

print('values: ', values, '\n')

# Accesing to key-value pairs

items = student.items()

print('items:', items, '\n')

# Looping through the dictionary

print('Looping through the dictionary: ', '\n')

for key, value in student.items():

	print(key, value, '\n')