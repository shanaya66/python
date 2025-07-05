# Dictionary operations

# Creating a dictionary
person = {
    "name": "Joy",
    "age": 13
}
print("Original Dictionary:", person)

# Dictionary with mixed keys
mixed_dict = {
    "name": "Zainab",
    1: [10, 20, 30]
}
print("Mixed Keys Dictionary:", mixed_dict)

# Accessing a value
print("Name from 'person':", person["name"])

# Adding a new key-value pair
person["phone"] = "123456"
print("After adding phone:", person)

# Updating an existing value
person["name"] = "Mathew"
print("After updating name:", person)

# Accessing a value using get()
print("Age using get():", person.get("age"))

# Removing a key-value pair using pop()
print("Removed age:", person.pop("age"))
print("After removing age:", person)

# Clearing all entries from the dictionary
person.clear()
print("After clearing:", person)
