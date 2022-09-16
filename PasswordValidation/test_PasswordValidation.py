# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_PasswordValidation
# @Date     : 2022-08-31T16:17:08
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from PasswordValidation import *


@pytest.fixture()
def standard_validator():
    # validator_builder = StandardBuilder()
    # validator_director = Director()
    # validator_director.construct(validator_builder)
    # validator = validator_builder.validator
    yield StandardValidator()


def test_create_password_validator(standard_validator):
    assert isinstance(standard_validator, StandardValidator)


def test_can_input_password(standard_validator):
    assert standard_validator.validate("password") is False


def test_password_less_than_8_characters(standard_validator):
    assert standard_validator.validate("abcdj") is False


def test_password_has_uppercase_letter(standard_validator):
    assert standard_validator.validate("abcdefgij") is False


def test_password_has_lowercase_letter(standard_validator):
    assert standard_validator.validate("AAAAAAAAA") is False


def test_password_has_number(standard_validator):
    assert standard_validator.validate("Aaaaaaaaa") is False


def test_password_has_underscore(standard_validator):
    assert standard_validator.validate("Aaaaaaaa1") is False


def test_password_has_all_conditions(standard_validator):
    assert standard_validator.validate("Aaaaaaa_1") is True
