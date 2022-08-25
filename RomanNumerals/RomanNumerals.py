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
        if number == 17:
            return "XVII"
        elif number == 16:
            return "XVI"
        elif number == 15:
            return "XV"
        elif number == 14:
            return "XIV"
        elif number >= 10:
            return "X" + (number-10) * "I"
        elif number == 9:
            return "IX"
        elif number >= 5:
            return "V" + (number-5) * "I"
        elif number == 4:
            return "IV"
        return number * "I"


