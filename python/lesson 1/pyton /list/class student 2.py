class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def intro(self):
        print("I am a student")

    def display(self):
        print("My name is", self.name)
        print("My grade is", self.grade)

# Creating an object with name and grade
obj1 = Student("Joy", 10)
obj1.intro()
obj1.display()
