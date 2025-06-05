# Ask the user for the number of rows
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop for printing stars in each row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after each row
    print()
