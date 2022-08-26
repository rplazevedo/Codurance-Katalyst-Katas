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


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(15, "XV"), (16, "XVI"), (17, "XVII")])
def test_convert_15_to_18(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


def test_convert_19():
    assert Rn.convert_arabic(19) == "XIX"


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(20, "XX"), (21, "XXI"), (23, "XXIII"),
                          (24, "XXIV"), (25, "XXV"), (27, "XXVII")])
def test_convert_20_to_27(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


def test_convert_29():
    assert Rn.convert_arabic(29) == "XXIX"


def test_convert_38():
    assert Rn.convert_arabic(38) == "XXXVIII"


def test_convert_39():
    assert Rn.convert_arabic(39) == "XXXIX"


def test_convert_40():
    assert Rn.convert_arabic(40) == "XL"


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(41, "XLI"), (42, "XLII")])
def test_convert_41_to_43(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(44, "XLIV"), (45, "XLV"), (47, "XLVII"),
                          (49, "XLIX")])
def test_convert_44_to_49(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(50, "L"), (51, "LI"), (52, "LII"),
                          (54, "LIV"), (56, "LVI"), (59, "LIX")])
def test_convert_50s(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


def test_convert_64():
    assert Rn.convert_arabic(64) == "LXIV"


def test_convert_89():
    assert Rn.convert_arabic(89) == "LXXXIX"


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(90, "XC"), (91, "XCI"), (92, "XCII"),
                          (99, "XCIX")])
def test_convert_90s(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(100, "C"), (101, "CI"), (102, "CII"),
                          (139, "CXXXIX"), (149, "CXLIX"), (190, "CXC"),
                          (199, "CXCIX")])
def test_convert_100s(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(200, "CC"), (299, "CCXCIX")])
def test_convert_200s(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(400, "CD"), (408, "CDVIII"), (499, "CDXCIX")])
def test_convert_400s(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(500, "D"), (501, "DI"), (502, "DII")])
def test_convert_500(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(900, "CM"), (999, "CMXCIX")])
def test_convert_900(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral


@pytest.mark.parametrize("input_number,expected_numeral",
                         [(1000, "M"), (2008, "MMVIII"), (4000, "MMMM")])
def test_convert_1000(input_number: int, expected_numeral: str):
    assert Rn.convert_arabic(input_number) == expected_numeral
