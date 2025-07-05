# Student Inheritance Example

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display_name(self):
        print(f"The name is: {self.fname} {self.lname}")


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def display_details(self):
        self.display_name()
        print(f"Graduation Year: {self.year}")


# Creating a student object
student1 = Student("Harish", "Ragavendra", 2023)
student1.display_details()
