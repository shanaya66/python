from abc import ABC, abstractmethod

# 🌐 Abstract Base Class
class Polygon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass

    def print_area(self):
        print(f"📐 Polygon: {self.name}")
        print(f"✅ Area: {self.calculate_area()} units²\n")


# 🔺 Triangle Class
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# ▭ Rectangle Class
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# 🔲 Square Class
class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def calculate_area(self):
        return self.side * self.side


# 🎯 Main Function
def main():
    print("╔════════════════════════════════════════╗")
    print("║     🧮 Polygon Area Calculator (OOP)     ║")
    print("║   Abstraction + Inheritance in Python  ║")
    print("╚════════════════════════════════════════╝\n")

    # Triangle
    t = Triangle(base=10, height=5)
    t.print_area()

    # Rectangle
    r = Rectangle(length=8, width=4)
    r.print_area()

    # Square
    s = Square(side=6)
    s.print_area()


if __name__ == "__main__":
    main()
