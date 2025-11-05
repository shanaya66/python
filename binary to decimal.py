# binary_to_decimal_project.py

def is_binary(s: str) -> bool:
    return len(s) > 0 and all(ch in "01" for ch in s)

def binary_to_decimal(s: str) -> int:
    total = 0
    for ch in s:
        total = total * 2 + (1 if ch == '1' else 0)
    return total

def main():
    s = input("Enter a binary number (0s and 1s only): ").strip()
    if not is_binary(s):
        print("Invalid input: use only 0 and 1.")
        return
    value = binary_to_decimal(s)
    print(f"{s} in decimal is {value}")

if __name__ == "__main__":
    main()
