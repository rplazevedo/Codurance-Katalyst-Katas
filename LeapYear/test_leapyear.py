# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_leapyear
# @Date     : 2022-08-25T15:37:41
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from LeapYear import Year

@pytest.mark.parametrize("input_year,expected",
                         [(1990, False), (1992, True), (1996, True),
                          (2004, True)])
def test_div_by_4_leap(input_year: int, expected: bool):
    assert Year.is_leapyear(input_year) == expected

@pytest.mark.parametrize("input_year,expected",
                         [(1600, True), (1200, True), (2000, True)])
def test_div_by_400_leap(input_year: int, expected: bool):
    assert Year.is_leapyear(input_year) == expected

@pytest.mark.parametrize("input_year,expected",
                         [(1900, False), (1800, False), (1700, False)])
def test_div_by_100_not_leap(input_year: int, expected: bool):
    assert Year.is_leapyear(input_year) == expected

