# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : PasswordValdation
# @Date     : 2022-08-31T16:16:47
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

from abc import ABC, abstractmethod


class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(ABC):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def _set_min_number_characters(self, min_number_characters: int) -> None:
        pass

    @abstractmethod
    def _set_with_uppercase(self) -> None:
        pass

    @abstractmethod
    def _set_with_lowercase(self) -> None:
        pass

    @abstractmethod
    def _set_with_underscore(self) -> None:
        pass

    @abstractmethod
    def _set_with_number(self) -> None:
        pass


class ValidatorBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def __init__(self) -> None:
        self._validator = PasswordValidator()

    def _min_number_characters(self, min_mumber_characters) -> None:
        self._validator._min_mumber_characters = min_mumber_characters

    def _with_uppercase(self) -> None:
        self._validator._with_uppercase = True

    def _with_lowercase(self) -> None:
        self._validator._with_lowercase = True

    def _with_underscore(self) -> None:
        self._validator._with_underscore = True

    def _with_number(self) -> None:
        self._validator._with_number = True


class PasswordValidator:
    def __init__(self, min_mumber_characters: int = 6,
                 with_uppercase: bool = False,
                 with_lowercase: bool = False,
                 with_number: bool = False,
                 with_underscore: bool = False) -> None:
        self._min_mumber_characters = min_mumber_characters
        self._with_uppercase = with_uppercase
        self._with_lowercase = with_lowercase
        self._with_number = with_number
        self._with_underscore = with_underscore

    invalid = False
    valid = True

    def validate(self, password: str) -> bool:
        raise NotImplementedError

    @staticmethod
    def contains_number(self, password: str) -> bool:
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


class StandardValidator:
    def __init__(self) -> None:
        pass

    invalid = False
    valid = True

    def validate(self, password: str) -> bool:
        conditions = (len(password) <= 8
                      or password.islower()
                      or password.isupper()
                      or password.isnumeric()
                      or not StandardValidator.contains_number(password)
                      or not StandardValidator.contains_underscore(password))
        if conditions:
            return self.invalid
        else:
            return self.valid

    @staticmethod
    def contains_number(password: str) -> bool:
        found_number = False
        i = 0
        while not found_number and i < len(password):
            found_number = password[i].isnumeric()
            i += 1
        return found_number

    @staticmethod
    def contains_underscore(password: str) -> bool:
        found_underscore = False
        i = 0
        while not found_underscore and i < len(password):
            found_underscore = password[i] == "_"
            i += 1
        return found_underscore
