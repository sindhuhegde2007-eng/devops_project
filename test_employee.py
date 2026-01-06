from employee import get_salary_grade

def test_salary_grade():
    result = get_salary_grade()
    assert result is not None
