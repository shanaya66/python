#programm to check if user input numbers are equal without using any comparision operator
def checkifsame(n1,n2):
    if((n1^n2)!=0):
        print("numbers are not equal")
    else:
        print("both numbers are equal")
n1=int(input("enter the first number to compare"))
n2=int(input("enter the first number to compare"))
checkifsame(n1,n2)