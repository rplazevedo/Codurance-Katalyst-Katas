# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : LeapYear
# @Date     : 2022-08-25T15:25:50
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

class Year:
    def __init__(self):
        pass

    @staticmethod
    def is_leapyear(year: int) -> bool:
        return Year.div_by_400(year) or (
                Year.div_by_4(year) and Year.not_div_by_100(year))

    @staticmethod
    def not_div_by_100(year: int) -> bool:
        return not year % 100 == 0

    @staticmethod
    def div_by_4(year: int) -> bool:
        return year % 4 == 0

    @staticmethod
    def div_by_400(year: int) -> bool:
        return year % 400 == 0

