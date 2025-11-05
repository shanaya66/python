# 2digit_primes.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True

def main():
    print("Two-digit prime numbers are:")
    for num in range(10, 100):  # only 2-digit numbers
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()
