# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-TDD
# @File     : fIZZbUZZ
# @Date     : 2022-08-24T15:30:55
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

def fizz_buzz(number: int) -> str:
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
