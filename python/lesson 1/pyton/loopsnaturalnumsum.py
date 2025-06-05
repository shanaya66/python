# Program to calculate the sum of natural numbers up to a given number

# Input from the user
number = int(input("Enter a number: "))

# Initialize the sum
total = 0

# Loop to calculate the sum
for i in range(1, number + 1):
    total += i

# Display the result
print("The sum of natural numbers is", total)
