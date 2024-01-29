class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t\t{self.name}\t{self.age}\t{self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for employee in self.employees:
            print(employee)

    def sort_table(self, sort_parameter):
        if sort_parameter == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_parameter == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_parameter == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")

# Sample data
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Creating an EmployeeTable instance
employee_table = EmployeeTable([employee1, employee2, employee3, employee4])

# User input for sorting parameter
sorting_param = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))

# Sorting and displaying the table
employee_table.sort_table(sorting_param)
employee_table.display_table()
