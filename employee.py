def get_salary_grade(salary):
    if salary >= 80000:
        return "Grade A"
    elif salary >= 60000:
        return "Grade B"
    elif salary >= 40000:
        return "Grade C"
    elif salary >= 25000:
        return "Grade D"
    else:
        return "Grade E"


def main():
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Monthly Salary: "))

    grade = get_salary_grade(salary)

    print("\n--- Employee Details ---")
    print(f"Name       : {name}")
    print(f"ID         : {emp_id}")
    print(f"Department : {department}")
    print(f"Salary     : ₹{salary}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
