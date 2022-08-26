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

        divisor_list = [500, 400, 100, 90, 50, 40, 10]
        div_numer_list = ["D", "CD", "C", "XC", "L", "XL", "X"]
        for divisor, div_numer in zip(divisor_list, div_numer_list):
            number, numeral = RomanNumerals.check_for_mult(number, numeral,
                                                           divisor, div_numer)
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
    def check_for_mult(numb: int, rom_num: str, divisor: int, rn_to_add: str)\
            -> tuple[int, str]:
        div_quot, div_remain = divmod(numb, divisor)
        if div_quot:
            rom_num += rn_to_add * div_quot
            numb = div_remain
        return numb, rom_num
