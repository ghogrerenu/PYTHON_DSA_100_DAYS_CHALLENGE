""" Employee Class with Performance Evaluation
Attributes:
name: Name of the employee.
age: Age of the employee.
gender: Gender of the employee.

phone: Phone number of the employee.
salary: Salary of that employee
Methods:
__init__(self, name, age, gender, phone,salary): Constructor method to
initialize the employee object with name, age, gender, and phone number,
salary attributes.
change_salary(self): Method that asks within the new salary and updates
the salary of that employee
display_details(self): Method to display all details of the employee,
including name, age, gender, phone number, salary."""


class Employee:
    def __init__(self, name, age, gender, phone, salary):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.salary = salary

    def change_salary(self):
        # Ask for the new salary and update it
        new_salary = float(input("Enter the new salary: "))
        self.salary = new_salary
        print(f"Salary updated to {self.salary}")

    def display_details(self):
        # Display all details of the employee
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")
        print(f"Salary: {self.salary}")

# Example usage
employee = Employee("John Doe", 30, "Male", "123-456-7890", 50000)
employee.display_details()
employee.change_salary()
employee.display_details()


