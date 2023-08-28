class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_sorted_data(self, parameter):
        if parameter == 1:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.age)
        elif parameter == 2:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.name)
        elif parameter == 3:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter.")
            return

        print("Employee ID | Name     | Age | Salary (PM)")
        print("-" * 45)
        for emp in sorted_employees:
            print(f"{emp.employee_id}        | {emp.name} | {emp.age}   | {emp.salary}")

# Sample employee data
company = Company()
company.add_employee(Employee("161E90", "Raman", 41, 56000))
company.add_employee(Employee("161F91", "Himadri", 38, 67500))
company.add_employee(Employee("161F99", "Jaya", 51, 82100))
company.add_employee(Employee("171E20", "Tejas", 30, 55000))
company.add_employee(Employee("171G30", "Ajay", 45, 44000))

# User input for sorting parameter
print("Sort Employee Data:")
print("1. Age")
print("2. Name")
print("3. Salary")
sorting_parameter = int(input("Enter sorting parameter (1/2/3): "))

company.print_sorted_data(sorting_parameter)
