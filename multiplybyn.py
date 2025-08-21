# MultiplyByN Project
# Introduction to Time and Space Complexity

# Function 1: Direct Multiplication (O(1) time complexity)
def multiply_direct(N, M):
    return N * M

# Function 2: Repeated Addition (O(N) time complexity)
def multiply_repeated(N, M):
    result = 0
    for _ in range(M):   # add N to itself M times
        result += N
    return result

# Main Program
if __name__ == "__main__":
    print("🌸 Multiply By N Project 🌸")
    print("---------------------------")

    # Input
    N = int(input("Enter the number N: "))
    M = int(input("Enter the number M: "))

    # Using Direct Multiplication
    direct_result = multiply_direct(N, M)

    # Using Repeated Addition
    repeated_result = multiply_repeated(N, M)

    # Output
    print("\n✨ Results ✨")
    print(f"Direct Multiplication (O(1)): {N} x {M} = {direct_result}")
    print(f"Repeated Addition (O(N)): {N} x {M} = {repeated_result}")

    # Time complexity explanation
    print("\n📘 Time Complexity:")
    print("🔹 Direct Multiplication → O(1) (constant time)")
    print("🔹 Repeated Addition → O(N) (linear time)")
