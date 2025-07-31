# 🌀 Fibonacci Series Generator 🌀

print("🌼 Welcome to the Fibonacci Funhouse! 🌼")

# Function to generate Fibonacci series
def fibonacci(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

# Input from user
terms = int(input("✨ How many terms do you want to generate? "))

# Generate and print the sequence
if terms <= 0:
    print("⚠️ Please enter a number greater than 0!")
else:
    sequence = fibonacci(terms)
    print("🔢 Your Fibonacci Sequence:")
    print(" ➤ ".join(map(str, sequence)))
