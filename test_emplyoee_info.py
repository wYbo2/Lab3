import employee_info as core

def test_emplyoees_age_range():
    result = core.get_employees_by_age_range(25,35)
    assert len(result) == 2  # Based on data: John, Jane, Mike
    assert result[0]["name"] == "John"
    assert result[1]["name"] == "Mike"

def test_calculate_average_salary():
    result = core.calculate_average_salary()
    assert result == 60166.666666666664

def test_get_employees_by_dept():
    result = core.get_employees_by_dept("Marketing")
    assert len(result) == 2  # Jane and Mary are in Marketing
    assert result[0]["name"] == "Jane"
    assert result[1]["name"] == "Mary"