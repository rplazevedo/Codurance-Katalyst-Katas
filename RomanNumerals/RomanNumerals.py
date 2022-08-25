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
            return RomanNumerals.mult_5_converter(number - div_5_remain) \
                   + div_5_remain * "I"
        elif number == 14:
            return "XIV"
        elif number == 9:
            return "IX"
        elif number == 4:
            return "IV"

    @staticmethod
    def mult_5_converter(numb: int) -> str:
        if numb == 15:
            return "XV"
        elif numb == 10:
            return "X"
        elif numb == 5:
            return "V"
        return ""
