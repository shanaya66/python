# lcm_project.py

def gcd(a, b):
    # Euclid's algorithm
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)  # safe from overflow in other languages

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter whole numbers only.")
        return

    print(f"LCM of {a} and {b} is {lcm(a, b)}")

if __name__ == "__main__":
    main()
