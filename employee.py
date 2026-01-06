class Employee:
    def __init__(self, employee_name, employee_id, department, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print("\n--------------------- EMPLOYEE DETAILS ---------------------")
        print(f"Employee Name : {self.employee_name}")
        print(f"Employee ID   : {self.employee_id}")
        print(f"Department    : {self.department}")
        print(f"Salary        : Rs. {self.salary}")
        print("-----------------------------------------------------------")

    def check_salary_grade(self):
        if self.salary >= 80000:
            grade = "Grade A"
        elif self.salary >= 60000:
            grade = "Grade B"
        elif self.salary >= 40000:
            grade = "Grade C"
        elif self.salary >= 25000:
            grade = "Grade D"
        else:
            grade = "Grade E"

        print(f"Salary Grade  : {grade}")


def main():
    employee_name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = float(input("Enter monthly salary: "))

    employee = Employee(employee_name, employee_id, department, salary)
    employee.display_details()
    employee.check_salary_grade()


if __name__ == "__main__":
    main()
