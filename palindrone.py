# Palindrome Checker

def palindrome(n):
    num = n
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    if n == rev:
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")

# Input from user
n = int(input("Enter the number: "))
palindrome(n)
