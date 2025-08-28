import matplotlib.pyplot as plt
import re

print("✨ Recurrence Relations - Analysis & Space Complexity ✨")
print("Paste your recursive function code below (end with an empty line):\n")

# Read multiline code input from user
code_lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    code_lines.append(line)

code = "\n".join(code_lines)

# Detect recurrence relation heuristically
if "fib" in code or ("return" in code and code.count("return") > 1):
    recurrence = "T(n) = T(n-1) + T(n-2) + O(1)"
    complexity = "O(2^n)"
elif "merge" in code or "sort" in code:
    recurrence = "T(n) = 2T(n/2) + O(n)"
    complexity = "O(n log n)"
elif "binary" in code or "mid" in code:
    recurrence = "T(n) = T(n/2) + O(1)"
    complexity = "O(log n)"
elif "for" in code or "while" in code:
    recurrence = "T(n) = T(n-1) + O(1)"
    complexity = "O(n)"
else:
    recurrence = "T(n) = O(1)"
    complexity = "O(1)"

print("\n📌 Recurrence Relation:", recurrence)
print("⏳ Time Complexity:", complexity)

# Plot growth chart for recurrence
x = [2, 4, 8, 16, 32]
if "log" in complexity:
    y = [len(bin(i)) for i in x]
elif "n log n" in complexity:
    y = [i * len(bin(i)) for i in x]
elif "n^2" in complexity:
    y = [i**2 for i in x]
elif "2^n" in complexity:
    y = [2**(len(bin(i))-2) for i in x]
else:
    y = [i for i in x]

plt.plot(x, y, marker="o", color="#4f46e5", linewidth=3)
plt.title(f"✨ Growth of {recurrence} ✨", fontsize=14, color="#6366f1")
plt.xlabel("Input Size (n)")
plt.ylabel("Steps")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
