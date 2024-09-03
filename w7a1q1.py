"""Q1. Create a class called Employee with attributes such as name, age,
gender, and phone number. Implement a constructor to initialize these
attributes.
Include methods to calculate monthly and yearly salary based on hourly
rate and hours worked. Ask hourly rate and hours worked inside the
method (local variable).
Create 2 objects and check your code."""


class Employee:
    def __init__(self, name, age, gender, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def calculate_monthly_salary(self):
        hourly_rate = float(input(f"Enter the hourly rate for {self.name}: "))
        hours_worked = float(input(f"Enter the number of hours worked in a month for {self.name}: "))
        monthly_salary = hourly_rate * hours_worked
        return monthly_salary

    def calculate_yearly_salary(self):
        monthly_salary = self.calculate_monthly_salary()
        yearly_salary = monthly_salary * 12
        return yearly_salary


# Creating two objects of the Employee class
employee1 = Employee("Alice", 30, "Female", "123-456-7890")
employee2 = Employee("Bob", 28, "Male", "098-765-4321")

# Checking the code
print(f"{employee1.name}'s Monthly Salary: ${employee1.calculate_monthly_salary():.2f}")
print(f"{employee1.name}'s Yearly Salary: ${employee1.calculate_yearly_salary():.2f}")

print(f"{employee2.name}'s Monthly Salary: ${employee2.calculate_monthly_salary():.2f}")
print(f"{employee2.name}'s Yearly Salary: ${employee2.calculate_yearly_salary():.2f}")
