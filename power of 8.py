def isPowerOf8(n):
    if n <= 0:
        return False
    
    while n % 8 == 0:
        n //= 8

    return n == 1


# ---- Main program ----
num = int(input("Enter a number: "))
if isPowerOf8(num):
    print("YES")
else:
    print("NO")
