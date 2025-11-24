def reverseBits(n):
    # Convert number to binary string (remove '0b')
    binary = bin(n)[2:]
    
    # Reverse the binary string
    reversed_binary = binary[::-1]
    
    # Convert reversed binary back to integer
    return int(reversed_binary, 2)


# ---- Main program ----
num = int(input("Enter a number: "))
print(reverseBits(num))
