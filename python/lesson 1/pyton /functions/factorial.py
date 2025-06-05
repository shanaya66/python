# Factorial using recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
number = int(input("Enter the number: "))

# Calculate factorial
result = factorial(number)

# Display the result
print("The factorial of the number is:", result)
