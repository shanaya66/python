#program to check if the nth bit is set or not
def setornot(number,n):
    if number&(1<<(n-1)):
        print("set")
    else:
        print("not set")
number =int(input("enter the number"))
n=int(input("enter bit number"))
setornot(number,n)