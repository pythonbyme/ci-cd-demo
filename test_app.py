from app import calculate_annual_salary

def test_annual_salary():
    result = calculate_annual_salary(30000)
    assert result == 360000

def test_zero_salary():
    result = calculate_annual_salary(0)
    assert result == 0