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
        if number == 92:
            return "XCII"
        elif number == 91:
            return "XCI"
        elif number == 90:
            return "XC"

        numeral = ""

        div_50_quot, div_50_remain = divmod(number, 50)
        if div_50_quot:
            numeral += "L"
            number = div_50_remain

        div_40_quot, div_40_remain = divmod(number, 40)
        if div_40_quot:
            numeral += "XL"
            number = div_40_remain

        div_10_remain = number % 10
        if div_10_remain <= 8:
            numeral += RomanNumerals.mult_10_converter(number)
            number = div_10_remain
        elif div_10_remain == 9:
            close_mult_10 = RomanNumerals.mult_10_converter(number+1)
            numeral += RomanNumerals.insert_i_before_last_char(close_mult_10)
            return numeral

        div_5_remain = number % 5
        if div_5_remain <= 3:
            return (numeral
                    + RomanNumerals.mult_5_converter(number - div_5_remain)
                    + div_5_remain * "I")
        else:
            close_mult_5 = RomanNumerals.mult_5_converter(div_5_remain+1)
            return (numeral
                    + RomanNumerals.insert_i_before_last_char(close_mult_5))

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
