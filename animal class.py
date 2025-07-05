# Abstraction Example

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        print("The base Animal class is implemented")

    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def __init__(self):
        print("Human class")

    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def __init__(self):
        print("Snake class")

    def move(self):
        print("I can crawl")


# Creating objects
h1 = Human()
h1.move()

s1 = Snake()
s1.move()
