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
        numeral = ""
        number, numeral = RomanNumerals.check_for_100s(number, numeral)
        number, numeral = RomanNumerals.check_for_90(number, numeral)
        number, numeral = RomanNumerals.check_for_50(number, numeral)
        number, numeral = RomanNumerals.check_for_40(number, numeral)
        number, numeral = RomanNumerals.check_for_10s(number, numeral)
        if number // 9:
            numeral += "IX"
            return numeral
        div_5_quot, div_5_remain = divmod(number, 5)
        if div_5_remain <= 3:
            numeral += div_5_quot * "V" + div_5_remain * "I"
            return numeral
        else:
            numeral += "IV"
            return numeral

    @staticmethod
    def check_for_100s(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 100, "C")

    @staticmethod
    def check_for_90(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 90, "XC")

    @staticmethod
    def check_for_50(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 50, "L")

    @staticmethod
    def check_for_40(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 40, "XL")

    @staticmethod
    def check_for_10s(numb: int, rom_numer: str) -> tuple[int, str]:
        return RomanNumerals.check_for_mult(numb, rom_numer, 10, "X")

    @staticmethod
    def check_for_mult(numb: int, rom_num: str, divisor: int, rn_to_add: str)\
            -> tuple[int, str]:
        div_quot, div_remain = divmod(numb, divisor)
        if div_quot:
            rom_num += rn_to_add * div_quot
            numb = div_remain
        return numb, rom_num

    @staticmethod
    def insert_i_before_last_char(numeral: str) -> str:
        last_char = numeral[-1]
        return numeral[:-1] + "I" + last_char
