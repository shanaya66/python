class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, id, name, salary, post):
        super().__init__(id, name)
        self.salary = salary
        self.post = post

    def display_details(self):
        self.display()
        print(f"Post: {self.post}")
        print(f"Salary: {self.salary}")


# Creating an Employee object
emp1 = Employee("101", "Anish", 60000, "Engineer")
emp1.display_details()
