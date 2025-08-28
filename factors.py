# Program to find factors of a number

# Taking input from user
n = int(input("Enter the number: "))

print("The factors are:")

# Loop to find factors
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
