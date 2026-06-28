
# Q8. (Tuples + Dictionaries + OOP)
# Create a class Employee with:
# Attributes: emp_id, name, details (a tuple containing department and salary).
# Method show_details() to print all information.
# Create a dictionary where employee ID is the key and Employee object is the
# value.
# Add 3 employees and display all using a loop.

class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()

# Dictionary to store employees

employees = {}

# Add 3 employees

for i in range(3):
    
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)

    employees[emp_id] = emp


# Display all employees

print("\nEmployee Records:")

for emp_id, emp in employees.items():
    emp.show_details()


