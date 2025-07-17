# 💫 Number Swapping Game 🎲
print("✨ Welcome to the Magical Number Swapper ✨")
print("Enter three numbers to be swapped in a cute loop! 💕")

# Getting input from user
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

print(f"\n🌸 Original Order: A = {a}, B = {b}, C = {c}")

# Swapping using a magical twist ✨
a, b, c = c, a, b

print(f"\n🔁 Swapped Order: A = {a}, B = {b}, C = {c}")
print("🎉 Ta-da! Numbers successfully swapped!")
