# 💫 Armstrong Number Checker 💫

print("🌟 Welcome to the Armstrong Number Checker 🌟")

# Take input from user
num = int(input("🔢 Enter a number: "))
temp = num
digits = len(str(num))
result = 0

# Cute loop to calculate sum of powers
while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp //= 10

# Result check
if result == num:
    print(f"✅ Yes! {num} is an Armstrong number! 🎉")
else:
    print(f"❌ Nope! {num} is not an Armstrong number. Try again! 💡")

