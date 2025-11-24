def firstSetBit(n):
    if n == 0:
        return 0

    pos = 1
    while (n & 1) == 0:
        n >>= 1
        pos += 1

    return pos


# ------- Main program --------
n = int(input("Enter a number: "))
result = firstSetBit(n)
print(result)
