# Expression Class Assignment - OOP Concept
# Submitted by: [Your Name]
# Date: July 3, 2025

class Expression:
    def __init__(self, expression):
        # Encapsulated attribute
        self.__expression = expression

    def solve(self):
        try:
            # Evaluating the expression safely
            result = eval(self.__expression)
            return result
        except Exception as e:
            return f"Invalid expression! ❌ Error: {e}"

    def print_result(self):
        result = self.solve()
        print("📘 Expression:", self.__expression)
        print("✅ Result:", result)

# Main function
def main():
    print("╔════════════════════════════════════╗")
    print("║      🧠 Expression Solver Class      ║")
    print("║     OOPs Concept | Python Project   ║")
    print("╚════════════════════════════════════╝")
    
    # User Input
    expr = input("🔢 Enter a mathematical expression: ")

    # Create Object
    my_expression = Expression(expr)

    # Print result
    my_expression.print_result()

# Run the program
if __name__ == "__main__":
    main()
