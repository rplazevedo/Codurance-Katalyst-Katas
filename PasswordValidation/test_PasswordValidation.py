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
    validator_builder = ValidatorBuilder()
    director = Director()
    director.builder = validator_builder
    director.builder.min_number_characters(
            9).need_underscore().need_number().need_lowercase(
            ).need_uppercase()
    standard_validator = director.builder.build()
    yield standard_validator


@pytest.fixture()
def validator_2():
    validator_builder = ValidatorBuilder()
    director = Director()
    director.builder = validator_builder
    director.builder.min_number_characters(7).need_number().need_lowercase(
            ).need_uppercase()
    validator = director.builder.build()
    yield validator


@pytest.fixture()
def validator_3():
    validator_builder = ValidatorBuilder()
    director = Director()
    director.builder = validator_builder
    director.builder.min_number_characters(17)
    director.builder.need_underscore()
    director.builder.need_lowercase()
    director.builder.need_uppercase()
    validator = director.builder.build()
    yield validator


def test_create_password_validator(standard_validator):
    assert isinstance(standard_validator, PasswordValidator)


def test_can_input_password(standard_validator):
    assert standard_validator.validate("password") == (False, "Too short\n"
                                                              "No uppercase\n"
                                                              "No number\n"
                                                              "No "
                                                              "underscore\n")


def test_password_less_than_8_characters(standard_validator):
    assert standard_validator.validate("abcdj") == (False, "Too short\n"
                                                           "No uppercase\n"
                                                           "No number\n"
                                                           "No "
                                                           "underscore\n")


def test_password_has_uppercase_letter(standard_validator):
    assert standard_validator.validate("abcdefgij") == (False, "No uppercase\n"
                                                               "No number\n"
                                                               "No "
                                                               "underscore\n")


def test_password_has_lowercase_letter(standard_validator):
    assert standard_validator.validate("AAAAAAAAA") == (False, "No lowercase\n"
                                                               "No number\n"
                                                               "No "
                                                               "underscore\n")


def test_password_has_number(standard_validator):
    assert standard_validator.validate("Aaaaaaaaa") == (False, "No number\n"
                                                               "No "
                                                               "underscore\n")


def test_password_has_underscore(standard_validator):
    assert standard_validator.validate("Aaaaaaaa1") == (False, "No "
                                                               "underscore\n")


def test_password_has_all_conditions(standard_validator):
    assert standard_validator.validate("Aaaaaaa_1") == (True, "")


def test_2nd_validator_less_than_7_characters(validator_2):
    assert validator_2.validate("Aa_4") == (False, "Too short\n")


def test_2nd_validator_no_number(validator_2):
    assert validator_2.validate("Aa_aaaaa") == (False, "No number\n")


def test_2nd_validator_pass(validator_2):
    assert validator_2.validate("Aaaa1235") == (True, "")


def test_3nd_validator_less_than_17_characters(validator_3):
    assert validator_3.validate("Aa_aaaa6") == (False, "Too short\n")


def test_3nd_validator_no_underscore(validator_3):
    assert validator_3.validate("Aa1aaaaaaaaaaaaaa") == (False,
                                                         "No underscore\n")


def test_3nd_validator_pass(validator_3):
    assert validator_3.validate("Aaaa_aaaaaaaaaaaa") == (True, "")
