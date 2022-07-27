# list[start : end : step]

# 'start' is an inclusive value, whereas 'end' is not

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extracting values from index 0 up to index 6 but not including it

print('From index 0 to index 5: {}'.format(my_list[ : 6]), '\n')

# Extracting values from index 3 to index 7

print('From index 3 to index 7: {}'.format(my_list[3 : 8]), '\n')

print('From index 3 to index 7 (using negative indexes): {}'.format(my_list[-7 : -2]), '\n')

# Extracting values from index 5 to the end

print('From index 5 to the end : {}'.format(my_list[5 : ]), '\n')