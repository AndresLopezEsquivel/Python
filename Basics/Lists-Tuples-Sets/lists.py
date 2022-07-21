# Lists

books = ["Think Fast, Think Slow", "Steve Jobs", "Man's Search for Meaning"]

# Insert an item at the end of the list

print('=== append() ===\n')

books.append("Hitchhiker's guide to the galaxy")

print(books,'\n')

# Insert an item at a desired index

print("=== insert() ===\n")

books.insert(0, "Naked Statistics")

print(books, '\n')

# Insert various items at the end of the list

print("=== extend() ===\n")

books.extend(["The Theory of Everything", "Victus", "Ikigai"])

print(books, '\n')

# Remove an item from the list

print('=== remove() ===\n')

books.remove("The Theory of Everything")

books.remove("Naked Statistics")

print(books, '\n')

# Remove the last item of the list. Pop function is useful when the list is treated as a stack or queue

print('=== pop() ===\n')

popped_item_1 = books.pop()

popped_item_2 = books.pop()

print(books, '\n')

print(f'First popped item: {popped_item_1}', '\n')

print(f'Second popped item: {popped_item_2}', '\n')

# To sort the list. The sort() function modifies the original list

print('=== sort() ===\n')

# List of letters

letters = ['c', 'a', 'b', 'f', 'x', 'd']

# To sort alphabetically in ascending order

letters.sort()

print('List ordered alphabetically in ascending order', '\n')

print(letters, '\n')

# To sort alphabetically in descending order

letters.sort(reverse = True)

print('List ordered alphabetically in descending order', '\n')

print(letters, '\n')

# List of numbers

numbers = [100, 200, 1000, 5, 1, 500]

# To sort numerically in ascending order

numbers.sort()

print('List ordered numerically in ascending order', '\n')

print(numbers, '\n')

# To sort numerically in descending order

numbers.sort(reverse = True)

print('List ordered numerically in descending order', '\n')

print(numbers, '\n')

# To sort a list without modifying the original list. The sorted() function returns the sorted list

print('=== sorted() ===', '\n')

numbers = [100, 200, 1000, 5, 1, 500]

sorted_list_of_numbers = sorted(numbers)

print(f'Original list: {numbers}', '\n')

print(f'Modified list: {sorted_list_of_numbers}', '\n')

# To reverse the order of a list

print('=== reverse() ===', '\n')

print(f'Original list: {numbers}', '\n')

numbers.reverse()

print(f'Reversed list: {numbers}', '\n')

# To find the index of a certain item

# If you try to find the index of a non existent item, then an error will be prompted

print('=== index() ===', '\n')

list_of_items = ['item1', 'item2', 'item3', 'item4']

index_of_item1 = list_of_items.index('item1')

print(f'List of items: {list_of_items}', '\n')

print(f'Index of item 1: {index_of_item1}', '\n')

# To check if an item exists within a list

print('=== item in list ====', '\n')

print(f"item1 exists in list_of_items: {'item1' in list_of_items}", '\n')

print(f"item5 exists in list_of_items: {'item5' in list_of_items}", '\n')

# To loop through a list and have access to each index and item in it

print('=== Looping through a list ===', '\n')

for item_index, item_value in enumerate(list_of_items, start = 1):

	print(item_index, item_value, '\n')

# Convert a list into a string using the join() method

print('=== join() ===', '\n')

items_string = '-'.join(list_of_items)

print(f"List converted into a string: {items_string}", '\n')

# Split up a string into a list using the split() method

print('=== split() ===', '\n')

new_list_of_items = items_string.split('-')

print(f'New list of items: {new_list_of_items}', '\n')