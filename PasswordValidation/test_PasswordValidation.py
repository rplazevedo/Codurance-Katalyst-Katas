# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_PasswordValidation
# @Date     : 2022-08-31T16:17:08
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from PasswordValidation import PasswordValidator


@pytest.fixture()
def password_validator():
    yield PasswordValidator()


def test_create_password_validator(password_validator):
    assert isinstance(password_validator, PasswordValidator)


def test_can_input_password(password_validator):
    assert PasswordValidator.validate("password") == False


def test_password_less_than_8_characters(password_validator):
    assert PasswordValidator.validate("abcdj") == False


def test_password_has_uppercase_letter(password_validator):
    assert PasswordValidator.validate("abcdefgij") == False


def test_password_has_lowercase_letter(password_validator):
    assert PasswordValidator.validate("AAAAAAAAA") == False


def test_password_has_number(password_validator):
    assert PasswordValidator.validate("Aaaaaaaaa") == False


def test_password_has_underscore(password_validator):
    assert PasswordValidator.validate("Aaaaaaaa1") == False


def test_password_has_all_conditions(password_validator):
    assert PasswordValidator.validate("Aaaaaaa_1") == True
