from emp import employee_details

def test_employee_details():
    expected_output = (
        "Employee Details\n"
        "----------------\n"
        "Name       : Sindhu\n"
        "ID         : 1001\n"
        "Department : IT\n"
        "Salary     : Rs. 80000\n"
        "Salary Grade: Grade A"
    )

    assert employee_details("Sindhu", "1001", "IT", 80000) == expected_output
