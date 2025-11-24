def longestOnes(n):
    binary = bin(n)[2:]   # convert to binary string without '0b'
    count = 0
    max_count = 0

    for bit in binary:
        if bit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


# ---- Main program ----
num = int(input("Enter a number: "))
print(longestOnes(num))
