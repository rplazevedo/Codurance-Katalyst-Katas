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

    def __init__(self) -> None:
        self.builder = None

    def builder(self, builder) -> None:
        self.builder = builder


class Builder(ABC):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def min_number_characters(self, min_number_characters: int) -> None:
        pass

    @abstractmethod
    def need_uppercase(self) -> None:
        pass

    @abstractmethod
    def need_lowercase(self) -> None:
        pass

    @abstractmethod
    def need_underscore(self) -> None:
        pass

    @abstractmethod
    def need_number
        (self) -> None:
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

    def min_number_characters(self, min_mumber_characters) -> None:
        self._validator._min_mumber_characters = min_mumber_characters
        return self

    def need_uppercase(self) -> None:
        self._validator._with_uppercase = True
        return self

    def need_lowercase(self) -> None:
        self._validator._with_lowercase = True
        return self

    def need_underscore(self) -> None:
        self._validator._with_underscore = True
        return self

    def need_number(self) -> None:
        self._validator._with_number = True
        return self

    def build(self):
        return self._validator


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
        if not self.above_min_length(password):
            return self.invalid
        if self._with_lowercase and not self.has_lowercase(password):
            return self.invalid
        if self._with_uppercase and not self.has_uppercase(password):
            return self.invalid
        if self._with_underscore and not self.has_underscore(password):
            return self.invalid
        if self._with_number and not self.has_number(password):
            return self.invalid
        return self.valid

    def above_min_length(self, password: str) -> bool:
        return len(password) >= self._min_mumber_characters

    @staticmethod
    def has_uppercase(password: str) -> bool:
        return not password.islower()

    @staticmethod
    def has_lowercase(password: str) -> bool:
        return not password.isupper()

    @staticmethod
    def has_number(password: str) -> bool:
        found_number = False
        i = 0
        while not found_number and i < len(password):
            found_number = password[i].isnumeric()
            i += 1
        return found_number

    @staticmethod
    def has_underscore(password: str) -> bool:
        found_underscore = False
        i = 0
        while not found_underscore and i < len(password):
            found_underscore = password[i] == "_"
            i += 1
        return found_underscore


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
