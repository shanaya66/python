# armstrong number
n = int(input("enter a number"))
temp = n
sum = 0
while temp >0:
    rem = temp % 10
    sum = sum +rem ** 3
    temp = temp//10

if sum == n :
    print(n,"the given no is a armstrong number")
else:
    print(n, " is not a armstrong number")
