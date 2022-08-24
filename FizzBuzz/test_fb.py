from FizzBuzz import fizz_buzz as fb
import pytest


@pytest.mark.parametrize("test_input,expected", [(1, '1'), (2, '2'), (4, '4')])
def test_number_to_string(test_input, expected):
    assert fb(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(3, 'Fizz'), (6, 'Fizz'), (9, 'Fizz')])
def test_mult_3_to_fizz(test_input, expected):
    assert fb(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(5, 'Buzz'), (10, 'Buzz'), (20, 'Buzz')])
def test_mult_5_to_buzz(test_input, expected):
    assert fb(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(15, 'FizzBuzz'),
                                                 (30, 'FizzBuzz'),
                                                 (45, 'FizzBuzz')])
def test_mult_3_5_to_fizzbuzz(test_input, expected):
    assert fb(test_input) == expected
