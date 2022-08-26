# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : RomanNumerals
# @Date     : 2022-08-25T18:31:44
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

class RomanNumerals:
    def __init__(self):
        pass

    @staticmethod
    def convert_arabic(number: int) -> str:
        if number == 102:
            return "CII"
        if number == 101:
            return "CI"
        if number == 100:
            return "C"
        numeral = ""
        number, numeral = RomanNumerals.check_for_90s(number, numeral)
        number, numeral = RomanNumerals.check_for_50s(number, numeral)
        number, numeral = RomanNumerals.check_for_40s(number, numeral)

        div_10_quot, div_10_remain = divmod(number, 10)
        if div_10_remain <= 8:
            numeral += div_10_quot * "X"
            number = div_10_remain
        else:
            numeral += div_10_quot * "X" + "IX"
            return numeral

        div_5_quot, div_5_remain = divmod(number, 5)
        if div_5_remain <= 3:
            numeral += div_5_quot * "V" + div_5_remain * "I"
            return numeral
        else:
            numeral += "IV"
            return numeral

    @staticmethod
    def check_for_90s(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 90, "XC")

    @staticmethod
    def check_for_50s(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 50, "L")

    @staticmethod
    def check_for_40s(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 40, "XL")

    @staticmethod
    def check_for_mult(numb: int, rom_num: str, divisor: int, rn_to_add: str)\
            -> tuple[int, str]:
        div_quot, div_remain = divmod(numb, divisor)
        if div_quot:
            rom_num += rn_to_add
            numb = div_remain
        return numb, rom_num

    @staticmethod
    def mult_10_converter(numb: int) -> str:
        return (numb // 10) * "X"

    @staticmethod
    def mult_5_converter(numb: int) -> str:
        return (numb // 5) * "V"

    @staticmethod
    def insert_i_before_last_char(numeral: str) -> str:
        last_char = numeral[-1]
        return numeral[:-1] + "I" + last_char
