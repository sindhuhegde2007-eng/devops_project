import sys

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
    # If arguments are passed, use them
    if len(sys.argv) == 5:
        name = sys.argv[1]
        emp_id = sys.argv[2]
        department = sys.argv[3]
        salary = float(sys.argv[4])
    else:
        # Default values (project requirement – all in code)
        name = "Sindhu"
        emp_id = "1001"
        department = "IT"
        salary = 80000

    grade = get_salary_grade(salary)

    print("Employee Details")
    print("----------------")
    print(f"Name       : {name}")
    print(f"ID         : {emp_id}")
    print(f"Department : {department}")
    print(f"Salary     : {salary}")
    print(f"Salary Grade: {grade}")


if __name__ == "__main__":
    main()
