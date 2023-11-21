import pytest

from cp2_csv import newGrades, mixGrades

@pytest.mark.parametrize('input_data', newGrades)
def test_grades(input_data):
    assert input_data['avg'] >= mixGrades[input_data['Grade']]
