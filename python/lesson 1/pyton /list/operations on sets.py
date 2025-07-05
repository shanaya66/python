# Sets

# Creating a set
set1 = {10, 20, 30, 40}
print("Original set1:", set1)

# Adding an element to the set
set1.add(1000)
print("After adding 1000 to set1:", set1)

# Assigning one set to another
myset = set1
print("myset (copy of set1):", myset)

# Set difference and symmetric difference
seta = {'red', 'blue', 'green', 'yellow'}
setb = {'red', 'purple', 'green', 'cyan'}

print("Difference (seta - setb):", seta.difference(setb))
print("Symmetric difference (seta vs setb):", seta.symmetric_difference(setb))
