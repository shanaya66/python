# 🧮 Polygon Area Calculator
# Topic: Polymorphism & Encapsulation
# Created by: [Your Name]
# Date: July 17, 2025

class Polygon:
    def __init__(self, name):
        self.__name = name  # Encapsulation

    def calculate_area(self):
        return 0

    def print_area(self):
        print(f"📐 Polygon: {self.__name}")
        print(f"✅ Area: {self.calculate_area()} units²\n")


# 🟥 Square class
class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.__side = side

    def calculate_area(self):
        return self.__side ** 2


# ▭ Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width


# 🔺 Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.__base = base
        self.__height = height

    def calculate_area(self):
        return 0.5 * self.__base * self.__height


# 🧪 Main function
def main():
    print("╔════════════════════════════════════════╗")
    print("║     🎯 Polygon Area Calculator (OOP)     ║")
    print("║   Using Polymorphism & Encapsulation   ║")
    print("╚════════════════════════════════════════╝\n")

    # Create objects
    s = Square(6)
    r = Rectangle(8, 4)
    t = Triangle(10, 5)

    # Polymorphic behavior
    for shape in [s, r, t]:
        shape.print_area()

if __name__ == "__main__":
    main()
