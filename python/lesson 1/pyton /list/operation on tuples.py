# Tuples

# Simple tuple
mytuple = (10, 20, 30, 40)
print("mytuple:", mytuple)

# Mixed data types in a tuple
mtuple = (10, 'red', 'yellow', True)
print("mtuple:", mtuple)

# Nested tuple with a list inside
n_tuple = (
    100,
    ('harsh', 'jay', 'John'),
    ['p', 'y', 't', 'h', 'o', 'n']
)
print("n_tuple:", n_tuple)

# Access element inside the tuple
print("Element at index 2 of mtuple:", mtuple[2])

# Accessing nested tuple
print("Element at index 2 of inner tuple in n_tuple:", n_tuple[1][2])

# Slicing tuple
print("Sliced n_tuple from index 1 to 2:", n_tuple[1:3])
