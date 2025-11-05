def bits  (n):
    count=0
    while  (n):
        count+=1
        n>>=1
    return count
n=int(input("enter youre number"))
print("total bits",bits(n))