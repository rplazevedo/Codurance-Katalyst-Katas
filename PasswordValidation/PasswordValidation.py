# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : PasswordValdation
# @Date     : 2022-08-31T16:16:47
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

from abc import ABC, abstractmethod


class PasswordValidator(ABC):
    invalid = False
    valid = True

    @staticmethod
    @abstractmethod
    def validate(password: str) -> bool:
        raise NotImplementedError


class StandardValidator:
    def __init__(self):
        pass

    invalid = False
    valid = True

    @staticmethod
    def validate(password: str) -> bool:
        conditions = (len(password) <= 8
                      or password.islower()
                      or password.isupper()
                      or password.isnumeric()
                      or not StandardValidator.contains_number(password)
                      or not StandardValidator.contains_underscore(password))
        if conditions:
            return StandardValidator.invalid
        else:
            return StandardValidator.valid

    @staticmethod
    def contains_number(password: str) -> bool:
        for character in password:
            if character.isnumeric():
                return True
        return False

    @staticmethod
    def contains_underscore(password: str) -> bool:
        for character in password:
            if character == "_":
                return True
        return False
