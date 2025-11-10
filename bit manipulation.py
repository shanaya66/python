# 🤖 ImplementCircuit – Mini Neon Tech (Python)
# Simple bit manipulation project
# Made by Shanaya 💻⚡

# Take input
x = int(input("Enter number (x): "))
op = input("Choose operation (not / and / or / xor / shl / shr): ").lower()

# For NOT we don’t need mask
if op != "not":
    mask = int(input("Enter mask or shift value: "))
else:
    mask = 0

# Perform operation
if op == "not":
    result = ~x
elif op == "and":
    result = x & mask
elif op == "or":
    result = x | mask
elif op == "xor":
    result = x ^ mask
elif op == "shl":
    result = x << mask
elif op == "shr":
    result = x >> mask
else:
    print("Invalid operation!")
    exit()

# Show results
print("\n⚡ ImplementCircuit Result ⚡")
print("Decimal:", result)
print("Binary :", format(result & 0xFFFF, '016b'))  # 16-bit view
print("─────────────────────────────")
