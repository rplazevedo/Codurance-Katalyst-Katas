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


invalid = "Invalid password."
valid = "Valid Password."


def test_can_input_password(password_validator):
    assert PasswordValidator.validate("password") == invalid
