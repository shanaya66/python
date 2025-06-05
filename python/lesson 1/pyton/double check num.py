# Double check number

n = int(input("Enter the number: "))

if n > 50:
    if n % 2 == 0:
        print(f"{n} is an even number greater than 50")
    else:
        print(f"{n} is an odd number greater than 50")
else:
    print(f"{n} is less than or equal to 50")
