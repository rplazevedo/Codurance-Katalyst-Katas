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
        div_5_remain = number % 5
        if div_5_remain <= 3:
            return RomanNumerals.mult_5_converter(number-div_5_remain) \
                   + div_5_remain * "I"
        else:
            close_mult_5 = RomanNumerals.mult_5_converter(number+1)
            return RomanNumerals.insert_i_before_last_char(close_mult_5)

    @staticmethod
    def mult_5_converter(numb: int) -> str:
        if numb == 25:
            return "XXV"
        elif numb == 20:
            return "XX"
        elif numb == 15:
            return "XV"
        elif numb == 10:
            return "X"
        elif numb == 5:
            return "V"
        else:
            return ""

    @staticmethod
    def insert_i_before_last_char(numeral: str) -> str:
        last_char = numeral[-1]
        return numeral[:-1] + "I" + last_char
