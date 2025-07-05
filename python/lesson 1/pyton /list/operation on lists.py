# List operations with fruits

fruits = ['apple', 'banana', 'guava', 'grapes', 'pineapple']
print("Original list:", fruits)

# Access elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# Length of the list
print("Length of the list:", len(fruits))

# Pop an element at index 1
popped_item = fruits.pop(1)
print("Popped element at index 1:", popped_item)
print("List after popping:", fruits)

# Append a new element
print("Adding 'black berry' to the list...")
fruits.append('black berry')
print("List after appending:", fruits)

# Remove a specific element
print("Removing 'guava' from the list...")
fruits.remove('guava')
print("List after removing:", fruits)

# Sort the list
print("Sorting the list...")
fruits.sort()
print("Sorted list:", fruits)

# Reverse the list
print("Reversing the list...")
fruits.reverse()
print("Reversed list:", fruits)
