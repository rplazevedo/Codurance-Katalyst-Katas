from FizzBuzz import fizz_buzz as fb
import pytest


@pytest.mark.parametrize("test_input,expected", [(1, '1'), (2, '2'), (4, '4')])
def test_number_to_string(test_input, expected):
    assert fb(test_input) == expected
