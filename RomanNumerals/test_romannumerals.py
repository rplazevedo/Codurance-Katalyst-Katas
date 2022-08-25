# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_leapyear
# @Date     : 2022-08-25T18:32:03
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from RomanNumerals import RomanNumerals as Rn


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(1, "I"), (2, "II"), (3, "III")])
def test_convert_1_to_3(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral
