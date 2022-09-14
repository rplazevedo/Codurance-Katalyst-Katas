# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_PasswordValidation
# @Date     : 2022-08-31T16:17:08
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from PasswordValidation import StandardValidator


@pytest.fixture()
def standard_validator():
    yield StandardValidator()


def test_create_password_validator(standard_validator):
    assert isinstance(standard_validator, StandardValidator)


def test_can_input_password(standard_validator):
    assert StandardValidator.validate("password") == False


def test_password_less_than_8_characters(standard_validator):
    assert StandardValidator.validate("abcdj") == False


def test_password_has_uppercase_letter(standard_validator):
    assert StandardValidator.validate("abcdefgij") == False


def test_password_has_lowercase_letter(standard_validator):
    assert StandardValidator.validate("AAAAAAAAA") == False


def test_password_has_number(standard_validator):
    assert StandardValidator.validate("Aaaaaaaaa") == False


def test_password_has_underscore(standard_validator):
    assert StandardValidator.validate("Aaaaaaaa1") == False


def test_password_has_all_conditions(standard_validator):
    assert StandardValidator.validate("Aaaaaaa_1") == True
