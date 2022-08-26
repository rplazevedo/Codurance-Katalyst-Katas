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

        div_num_tup = ((1000, "M"),
                       (900, "CM"),
                       (500, "D"),
                       (400, "CD"),
                       (100, "C"),
                       (90, "XC"),
                       (50, "L"),
                       (40, "XL"),
                       (10, "X"),
                       (9, "IX"),
                       (5, "V"),
                       (4, "IV"),
                       (1, "I"))

        for divisor, div_numer in div_num_tup:
            number, numeral = RomanNumerals.check_for_mult(number, numeral,
                                                           divisor, div_numer)
        return numeral

    @staticmethod
    def check_for_mult(numb: int, rom_num: str, divisor: int, rn_to_add: str)\
            -> tuple[int, str]:
        div_quot, div_remain = divmod(numb, divisor)
        if div_quot:
            rom_num += rn_to_add * div_quot
            numb = div_remain
        return numb, rom_num
