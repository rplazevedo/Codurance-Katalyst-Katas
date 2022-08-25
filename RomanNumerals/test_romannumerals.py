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


def test_convert_4():
    assert Rn.convert_arabic(4) == "IV"


def test_convert_5():
    assert Rn.convert_arabic(5) == "V"


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(6, "VI"), (7, "VII"), (8, "VIII")])
def test_convert_6_to_8(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


def test_convert_9():
    assert Rn.convert_arabic(9) == "IX"


def test_convert_10():
    assert Rn.convert_arabic(10) == "X"


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(11, "XI"), (12, "XII"), (13, "XIII")])
def test_convert_11_to_13(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


def test_convert_14():
    assert Rn.convert_arabic(14) == "XIV"


# def test_convert_15():
#     assert Rn.convert_arabic(15) == "XV"
#
#
# @pytest.mark.parametrize("input_number,expected_numeral",
#                          [(6, "XVI"), (7, "XVII"), (8, "XVIII")])
# def test_convert_16_to_18(input_number: int, expected_numeral: str):
#     assert Rn.convert_arabic(input_number) == expected_numeral

