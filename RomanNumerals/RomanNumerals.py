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

        div_90_quot, div_90_remain = divmod(number, 90)
        if div_90_quot:
            numeral += "XC"
            number = div_90_remain

        div_50_quot, div_50_remain = divmod(number, 50)
        if div_50_quot:
            numeral += "L"
            number = div_50_remain

        div_40_quot, div_40_remain = divmod(number, 40)
        if div_40_quot:
            numeral += "XL"
            number = div_40_remain

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
    def mult_10_converter(numb: int) -> str:
        return (numb // 10) * "X"

    @staticmethod
    def mult_5_converter(numb: int) -> str:
        return (numb // 5) * "V"

    @staticmethod
    def insert_i_before_last_char(numeral: str) -> str:
        last_char = numeral[-1]
        return numeral[:-1] + "I" + last_char
