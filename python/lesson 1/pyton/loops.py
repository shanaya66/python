# Program to print the multiplication table of a given number

# Get the number from the user
table_number = int(input("Enter the table number:"" "))

# Loop from 1 to 10 to print the table
for i in range(1, 11):
    result = table_number * i
    print(f"{table_number} x {i} = {result}")
