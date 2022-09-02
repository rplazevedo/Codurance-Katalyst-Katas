# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : PasswordValdation
# @Date     : 2022-08-31T16:16:47
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm


class PasswordValidator:
    def __init__(self):
        pass

    invalid = False
    valid = True

    @staticmethod
    def validate(password: str) -> bool:
        if len(password) <= 8:
            return PasswordValidator.invalid
        elif password != password.upper():
            return PasswordValidator.invalid
        else:
            return PasswordValidator.valid
